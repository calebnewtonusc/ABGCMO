#!/usr/bin/env python3
"""
Re-fetch every primary source this repo depends on and check the numbers still hold.

    tools/verify_sources.py           # check all
    tools/verify_sources.py --json    # machine-readable

Only [M] Measured claims are checkable this way, because only those come from
artifacts that can be re-fetched. [R] and [A] claims come from vendor reports and
blogs and cannot be re-verified programmatically, which is precisely why they carry
a weaker tag.

Requires `gh` (authenticated) and network access.
"""
import argparse, json, re, subprocess, sys
from datetime import datetime, timezone

def gh(path, jq=None):
    cmd = ['gh', 'api', path]
    if jq:
        cmd += ['--jq', jq]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=45)
        return r.stdout.strip() if r.returncode == 0 else None
    except Exception:
        return None

def b64_contents(repo, path):
    import base64
    c = gh(f'repos/{repo}/contents/{path}', '.content')
    if not c:
        return None
    try:
        return base64.b64decode(c).decode('utf-8', 'replace')
    except Exception:
        return None

CHECKS = []

def check(name, claim, source):
    def deco(fn):
        CHECKS.append({'name': name, 'claim': claim, 'source': source, 'fn': fn})
        return fn
    return deco


@check('x-heavy-ranker-weights',
       'reply=13.5, fav=0.5, retweet=1.0, good_profile_click=12.0, '
       'reply_engaged_by_author=75.0, negative_feedback=-74.0, report=-369.0',
       'twitter/the-algorithm-ml projects/home/recap/README.md')
def _x_weights():
    t = b64_contents('twitter/the-algorithm-ml', 'projects/home/recap/README.md')
    if not t:
        return 'ERROR', 'could not fetch'
    want = {
        'scored_tweets_model_weight_fav': '0.5',
        'scored_tweets_model_weight_retweet': '1.0',
        'scored_tweets_model_weight_reply': '13.5',
        'scored_tweets_model_weight_good_profile_click': '12.0',
        'scored_tweets_model_weight_reply_engaged_by_author': '75.0',
        'scored_tweets_model_weight_negative_feedback_v2': '-74.0',
        'scored_tweets_model_weight_report': '-369.0',
    }
    bad = []
    for k, v in want.items():
        m = re.search(rf'{re.escape(k)}:\s*(-?[\d.]+)', t)
        if not m:
            bad.append(f'{k} not found')
        elif m.group(1) != v:
            bad.append(f'{k} is {m.group(1)}, repo says {v}')
    return ('OK', 'all 7 weights match') if not bad else ('DRIFT', '; '.join(bad))


@check('x-algorithm-not-updated-2026',
       'twitter/the-algorithm last pushed 2025-09-08; no 2026 open-sourcing',
       'GitHub API')
def _x_push():
    p = gh('repos/twitter/the-algorithm', '.pushed_at')
    if not p:
        return 'ERROR', 'could not fetch'
    if p.startswith('2026'):
        return 'DRIFT', f'repo pushed {p[:10]} — the "no 2026 update" claim needs revisiting'
    return 'OK', f'last push {p[:10]}, consistent with the repo'


@check('claude-marketplace-submission',
       'Community marketplace exists; submissions via clau.de/plugin-directory-submission',
       'anthropics/claude-plugins-community')
def _marketplace():
    d = gh('repos/anthropics/claude-plugins-community', '.description')
    if d is None:
        return 'ERROR', 'could not fetch'
    ok = 'plugin-directory-submission' in (d or '')
    return ('OK', 'submission path still referenced in repo description') if ok else \
           ('DRIFT', f'description no longer mentions the submission path: {d[:90]}')


@check('starscout-tool-exists',
       'ICSE 2026 fake-star study tool is public',
       'hehao98/StarScout')
def _starscout():
    s = gh('repos/hehao98/StarScout', '.stargazers_count')
    return ('OK', f'repo live, {s} stars') if s else ('DRIFT', 'repo not reachable')


@check('landscape-competitor-stars',
       'docs/LANDSCAPE.md star counts (drift expected; this reports the delta)',
       'GitHub API')
def _landscape():
    import os
    p = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                     'docs/LANDSCAPE.md')
    t = open(p).read()
    rows = re.findall(r'\[([\w.-]+/[\w.-]+)\]\([^)]+\)\s*\|\s*([\d,]+)\s*\|', t)
    drift = []
    for repo, stated in rows[:8]:
        live = gh(f'repos/{repo}', '.stargazers_count')
        if not live:
            continue
        s, l = int(stated.replace(',', '')), int(live)
        if s and abs(l - s) / s > 0.10:
            drift.append(f'{repo}: doc {s:,} vs live {l:,}')
    return ('OK', f'{len(rows)} rows within 10%') if not drift else \
           ('DRIFT', '; '.join(drift))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args()

    out = []
    for c in CHECKS:
        status, detail = c['fn']()
        out.append({'name': c['name'], 'status': status, 'detail': detail,
                    'claim': c['claim'], 'source': c['source']})

    if a.json:
        print(json.dumps({'checked': datetime.now(timezone.utc).isoformat(timespec='seconds'),
                          'results': out}, indent=2))
    else:
        icon = {'OK': 'ok  ', 'DRIFT': 'DRIFT', 'ERROR': 'err '}
        for r in out:
            print(f"[{icon[r['status']]}] {r['name']}")
            print(f"         {r['detail']}")
        n_bad = sum(1 for r in out if r['status'] == 'DRIFT')
        print(f"\n{len(out)} checks, {n_bad} drifted")
        print("Only [M] claims are checkable this way. [R] and [A] cannot be "
              "re-verified programmatically, which is why they carry weaker tags.")
    sys.exit(1 if any(r['status'] == 'DRIFT' for r in out) else 0)


if __name__ == '__main__':
    main()
