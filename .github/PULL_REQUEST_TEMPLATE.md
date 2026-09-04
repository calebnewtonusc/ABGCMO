## What this changes

<!-- One or two sentences. -->

## Type

- [ ] Better source for a number already in the repo (**most valuable**)
- [ ] Correction — something here is wrong
- [ ] New case study
- [ ] Platform mechanic that has changed
- [ ] New skill
- [ ] Docs / tooling

## Evidence

**Every number needs a tag.** See `data/evidence-tiers.md`.

- [ ] `[M] Measured` — I opened the primary artifact myself. Link: 
- [ ] `[P] Preprint` — exists and is checkable, not peer reviewed. Link: 
- [ ] `[R] Reported` — large-sample analysis, source and sample size stated. Link: 
- [ ] `[A] Asserted` — written as "reported at roughly X," never as fact
- [ ] No new numbers

> **A summary of a primary source is not the primary source.** If your citation is
> a blog describing a paper or a repo, the tag is `[R]` at best.

## Checks

- [ ] `python3 tools/check_structure.py`
- [ ] `python3 tools/check_claims.py`
- [ ] `python3 tools/check_evidence.py`

## If adding a skill

- [ ] `SKILL.md` frontmatter: `name` matches directory, `description` says *when*
      to use it, `metadata.version` present
- [ ] At least 2 evals in `evals/evals.json`
- [ ] **At least one eval where the correct behavior is to push back on the
      question as asked**
- [ ] Added to `registry/skills.csv` and `VERSIONS.md`
- [ ] README skill list and badge counts updated
