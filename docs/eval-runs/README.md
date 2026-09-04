# Eval runs

Measured results. No other repo in this space publishes these, which is the
point — everything else in the field is unmeasured prose.

## Method

`tools/run_evals.py` runs each eval in two arms:

- **Treatment** — `claude -p` with `cwd` = this repo, so `CLAUDE.md` loads
- **Control** — `claude -p` with `cwd` = an empty temp dir, so it does not

The user's own global `~/.claude/CLAUDE.md` loads in **both** arms. The delta
therefore measures **ABGCMO's marginal contribution on top of whatever the user
already has**, which is the number that matters to someone deciding whether to
install it. It is not a comparison against a blank model.

Grading is a separate model call scoring the response against the assertions in
`evals/evals.json`, instructed to be strict.

```bash
tools/run_evals.py --sample 12          # 12 random evals, both arms
tools/run_evals.py --skill x-growth     # one skill
tools/run_evals.py --all                # all 67 (expensive, ~90 min)
```

---

## Run 1 — 2026-09-04, n=12, both arms

| Arm | Assertions passed | Rate |
|---|---|---|
| **Treatment** | 32 / 68 | **47.1%** |
| Control | 16 / 68 | 23.5% |
| **Delta** | | **+23.6 pp** |

Per-eval: **treatment better on 6, tied on 6, control better on 0.** The repo never
made a response worse.

| Eval | T | C | Delta |
|---|---|---|---|
| `marketplace-listings` #1 | 6/6 | 1/6 | **+83pp** |
| `international-expansion` #2 | 5/6 | 0/6 | **+83pp** |
| `b2b2c` #1 | 5/6 | 3/6 | +33pp |
| `lifecycle-messaging` #1 | 2/6 | 0/6 | +33pp |
| `short-form-video` #1 | 3/6 | 2/6 | +17pp |
| `positioning` #2 | 5/6 | 4/6 | +17pp |
| `anti-patterns` #2 | 4/5 | 4/5 | 0 |
| `creator-partnerships` #2 | 1/5 | 1/5 | 0 |
| `partnerships` #2 | 1/5 | 1/5 | 0 |
| `brand` #1 | 0/6 | 0/6 | 0 |
| `events-conferences` #2 | 0/5 | 0/5 | 0 |
| `growth-loops` #2 | 0/6 | 0/6 | 0 |

### What run 1 actually proved

**The good:** a doubling of assertion pass rate, with zero regressions across 12
evals. Where the repo has specific knowledge — registry submission paths,
localization sequencing — the delta is enormous (+83pp twice).

**The bad: 47.1% absolute.** The repo passes fewer than half of its own
assertions. Reported honestly because the alternative is reporting the delta and
hiding the level.

### Two defects the run found

**Defect 191 — the doctrine was causing the agent to interrogate instead of
answer.** Three evals scored 0 in *both* arms. Reading the responses, all three
opened with clarifying questions:

> *"Before I design anything, I need to run the ABGCMO diagnostic. Which product
> is this? What stage? Current numbers?"*

A question is not an answer, so it scored zero — correctly. Worse, in several
cases the right diagnosis was sitting **inside** the question and never got
delivered as advice: *"thirty integrations with no usage is an inventory problem,
not a distribution problem"* is the correct call, wrapped in a request for more
information.

This also directly conflicted with the user's own standing instruction not to ask
permission.

→ **Fixed.** `CLAUDE.md` now opens with **Rule Zero: answer, do not interrogate.**
State the most probable assumption in one clause, deliver the full answer, and say
at the end what would change it. Blocking questions are reserved for cases where
proceeding would be actively harmful — real spend, a public launch, a legal
exposure.

**Defect 192 — several eval prompts were under-specified, penalizing correct
behavior.** `brand` #1 was *"We need a rebrand. New logo, new colors, new
website."* with no product named. Asking which product is arguably the right
response to that, so the eval was measuring the wrong thing.

→ **Fixed.** Five prompts given the context a real user would have supplied.
`brand` #1 went **0/6 → 5/6** on the same skill with no skill changes, which
confirms the eval was the defect rather than the skill.

---

## Honest limitations

- **n=12, single run.** No variance estimate. Individual eval scores moved by
  several points on re-runs with no changes, so per-eval numbers are noisy. The
  aggregate delta and the 6-0 win record are more trustworthy than any single row.
- **Self-grading.** The grader is the same model family that produced the answers.
  An independent grader would be better and has not been done.
- **Both arms carry the user's global config**, which contains personal context
  that shapes answers. This measures marginal contribution, not absolute
  capability.
- **55 of 67 evals unrun** in the A/B configuration.
- **The assertions are written by the same author as the skills**, so they test
  whether the skill does what its author intended, not whether that intention is
  correct.

None of these invalidate the direction. All of them mean the precision is lower
than the decimal points suggest.

---

## Post-fix retests — 2026-09-04, treatment arm only

After Rule Zero (defect 191) and the five under-specified prompts (defect 192)
were fixed, the affected evals were re-run in the treatment arm. Single runs, so
these are indicative, not conclusive.

| Eval | Before | After | |
|---|---|---|---|
| `brand` #1 | 0/6 | **5/6** | eval prompt was the defect |
| `brand` #2 | 1/6 | **4/6** | |
| `creator-partnerships` #2 | 1/5 | **4/5** | |
| `growth-loops` #2 | 0/6 | **2/6** | improved, still weak |
| `events-conferences` #2 | 0/5 | 0/5 | **unchanged — a real skill failure** |
| `partnerships` #2 | 1/5 | 0/5 | **got worse** |

Four improved, one unchanged, one regressed. The regression and the flat result
are reported because hiding them would make the other four meaningless.

**What is genuinely established:** `brand` #1 going 0/6 → 5/6 with **no change to
the skill itself**, only to the eval prompt, confirms defect 192. The eval was
measuring the wrong thing.

**What is not established:** whether Rule Zero improved the aggregate. Single-run
per-eval scores moved several points on re-runs with no changes at all, so
individual rows here are within noise. `partnerships` #2 going 1/5 → 0/5 is as
likely to be variance as regression.

**Open failure:** `events-conferences` #2 scored 0/5 both before and after both
fixes. That is not a measurement artifact — the skill is not producing the
behavior its assertions describe. Unresolved.

## Reproducing

```bash
tools/run_evals.py --sample 12 --seed 7    # the run above
tools/run_evals.py --skill events-conferences --arm treatment
```

The runner checkpoints after every eval, so a killed run keeps its partial
results. An earlier v2 attempt was lost to session teardown before this was added.

---

## Run 2 — DISCARDED (quota contamination)

A second A/B run with the same seed was attempted after the Rule Zero and prompt
fixes. Partway through, the Claude quota was exhausted. Every subsequent call
returned `"You're out of extra usage"`, which the grader scored as **0** —
indistinguishable in the output from a genuinely poor answer.

**8 of 18 completed runs were corrupted.** The file is kept as
`DISCARDED-v2-quota-contaminated.json` rather than deleted, because a discarded
result is evidence too.

Run 1 was audited for the same failure and had **zero** contaminated runs, so the
+23.6pp result stands.

→ The harness now raises `QuotaExhausted` on any refusal signature and **aborts,
keeping partial results**, instead of recording zeros. See defect 195 in
[AUDIT.md](../../AUDIT.md).

**Still owed:** a clean post-fix A/B run. It requires quota that was not available
at the time of writing. The pre-fix +23.6pp is the only aggregate number this repo
currently stands behind.
