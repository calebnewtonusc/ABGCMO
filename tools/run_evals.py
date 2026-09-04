#!/usr/bin/env python3
"""
Run ABGCMO evals with a control arm and report the measured delta.

  tools/run_evals.py --sample 12          # 12 evals, both arms
  tools/run_evals.py --skill x-growth     # one skill, both arms
  tools/run_evals.py --all                # all 67, both arms (expensive)
  tools/run_evals.py --arm treatment      # skip the control

TREATMENT: `claude -p` with cwd = this repo, so ABGCMO's CLAUDE.md loads.
CONTROL:   `claude -p` with cwd = an empty temp dir, so it does not.

The user's own global ~/.claude/CLAUDE.md loads in BOTH arms. The delta therefore
measures ABGCMO's *marginal* contribution on top of whatever the user already has,
which is the number that actually matters to someone deciding whether to install it.

Grading is model-assisted: a separate call scores the response against the
assertions. That is a known weakness (same model family grades its own output),
recorded in the results file rather than hidden.
"""
import argparse, json, glob, os, random, re, subprocess, sys, tempfile, time
from datetime import datetime, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_evals(skill=None):
    out = []
    for f in sorted(glob.glob(os.path.join(REPO, 'skills/*/evals/evals.json'))):
        d = json.load(open(f))
        if skill and d['skill_name'] != skill:
            continue
        for e in d['evals']:
            out.append({'skill': d['skill_name'], 'id': e['id'],
                        'prompt': e['prompt'], 'assertions': e['assertions']})
    return out


class QuotaExhausted(RuntimeError):
    """The API refused the call. Never score this as a zero."""


# Substrings that mean "the model never answered", as opposed to "answered badly".
# Scoring these as 0 silently corrupts a run; on 2026-09-04 it corrupted 8 of 18.
REFUSALS = (
    'out of extra usage',
    'usage limit reached',
    'rate limit',
    'Credit balance is too low',
    'Invalid API key',
    'overloaded_error',
)


def claude(prompt, cwd, timeout=300):
    try:
        r = subprocess.run(['claude', '-p', prompt], cwd=cwd, capture_output=True,
                           text=True, timeout=timeout)
        out = (r.stdout or '').strip()
        err = (r.stderr or '').strip()
        blob = out + ' ' + err
        for sig in REFUSALS:
            if sig.lower() in blob.lower():
                raise QuotaExhausted(out or err or sig)
        if not out:
            raise QuotaExhausted('empty response')
        return out
    except subprocess.TimeoutExpired:
        raise QuotaExhausted('timeout')


def grade(answer, assertions, cwd):
    numbered = '\n'.join(f'{i+1}. {a}' for i, a in enumerate(assertions))
    p = (
        'Grade this response against numbered assertions. Be strict: an assertion '
        'passes only if the response actually does the thing, not if it gestures at it.\n\n'
        'Output ONLY lines of the form:\n'
        'N: PASS\n or \nN: FAIL\n'
        'then a final line: SCORE: <passed>/<total>\n\n'
        f'RESPONSE:\n{answer[:6000]}\n\nASSERTIONS:\n{numbered}\n'
    )
    g = claude(p, cwd)
    m = re.search(r'SCORE:\s*(\d+)\s*/\s*(\d+)', g)
    if m:
        return int(m.group(1)), int(m.group(2)), g
    passes = len(re.findall(r'^\d+:\s*PASS', g, re.M))
    return passes, len(assertions), g


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sample', type=int)
    ap.add_argument('--skill')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--arm', choices=['treatment', 'control', 'both'], default='both')
    ap.add_argument('--seed', type=int, default=7)
    ap.add_argument('--out', default='docs/eval-runs/latest.json')
    a = ap.parse_args()

    evals = load_evals(a.skill)
    if a.sample:
        random.seed(a.seed)
        evals = random.sample(evals, min(a.sample, len(evals)))
    elif not (a.all or a.skill):
        ap.error('pass --sample N, --skill NAME, or --all')

    control_dir = tempfile.mkdtemp(prefix='abgcmo-control-')
    arms = ['treatment', 'control'] if a.arm == 'both' else [a.arm]
    results, t0, aborted = [], time.time(), False

    print(f'{len(evals)} evals x {len(arms)} arm(s) = {len(evals)*len(arms)} runs\n', flush=True)
    for i, e in enumerate(evals, 1):
        row = {'skill': e['skill'], 'id': e['id'], 'prompt': e['prompt'],
               'n_assertions': len(e['assertions'])}
        try:
            for arm in arms:
                cwd = REPO if arm == 'treatment' else control_dir
                ans = claude(e['prompt'], cwd)
                p, t, raw = grade(ans, e['assertions'], control_dir)
                row[arm] = {'passed': p, 'total': t,
                            'pct': round(100 * p / t, 1) if t else 0,
                            'answer': ans[:4000], 'grade': raw[:2000]}
                print(f"  [{i}/{len(evals)}] {e['skill']} #{e['id']:<2} "
                      f"{arm:<9} {p}/{t}", flush=True)
        except QuotaExhausted as ex:
            print(f"\n  ABORTED at eval {i}/{len(evals)}: {ex}", flush=True)
            print("  Partial results kept. An API refusal is NOT a score of zero.",
                  flush=True)
            aborted = True
            break
        results.append(row)
        os.makedirs(os.path.dirname(os.path.join(REPO, a.out)), exist_ok=True)
        json.dump({'summary': {'partial': True, 'completed': len(results),
                               'of': len(evals), 'arms': arms},
                   'results': results},
                  open(os.path.join(REPO, a.out), 'w'), indent=2)

    summary = {'aborted': aborted, 'generated': datetime.now(timezone.utc).isoformat(timespec='seconds'),
               'n_evals': len(evals), 'arms': arms,
               'elapsed_min': round((time.time()-t0)/60, 1)}
    for arm in arms:
        ps = sum(r[arm]['passed'] for r in results)
        ts = sum(r[arm]['total'] for r in results)
        summary[arm] = {'passed': ps, 'total': ts, 'pct': round(100*ps/ts, 1) if ts else 0}
    if len(arms) == 2:
        summary['delta_pp'] = round(summary['treatment']['pct'] - summary['control']['pct'], 1)
        wins = sum(1 for r in results if r['treatment']['pct'] > r['control']['pct'])
        ties = sum(1 for r in results if r['treatment']['pct'] == r['control']['pct'])
        summary['per_eval'] = {'treatment_better': wins, 'tie': ties,
                               'control_better': len(results)-wins-ties}

    out = os.path.join(REPO, a.out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump({'summary': summary, 'results': results}, open(out, 'w'), indent=2)

    print('\n' + '='*54)
    for arm in arms:
        s = summary[arm]
        print(f"  {arm:<10} {s['passed']:>3}/{s['total']:<3}  {s['pct']:>5}%")
    if 'delta_pp' in summary:
        print(f"  {'DELTA':<10} {summary['delta_pp']:>+10} pp")
        pe = summary['per_eval']
        print(f"  per-eval: treatment {pe['treatment_better']}, "
              f"tie {pe['tie']}, control {pe['control_better']}")
    print(f"\n  -> {a.out}  ({summary['elapsed_min']} min)")


if __name__ == '__main__':
    main()
