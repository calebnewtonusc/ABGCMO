# Contributing

The most valuable contributions, in order:

1. **A better source for a number already in the repo.** If a figure is tagged
   `[A] Asserted` and you have a `[M]` or `[R]` source, that is the highest-value
   change you can make. Same if a number here is simply wrong.
2. **A new case.** With the mechanism named and a source.
3. **A correction to a platform mechanic that has changed.** These go stale fast.
4. **A new skill**, if it covers ground no existing skill does.

## The rules

**Every number carries an evidence tag.** `[M]` measured (peer-reviewed,
open-sourced code, platform-published), `[R]` reported (large-sample analysis by
an organization with the data), `[A]` asserted (repeated across blogs with no
traceable origin). An untagged number will be rejected. See
`data/evidence-tiers.md`.

**Never state an asserted number as fact.** "Reported at roughly X," not "is X."

**Cases go in the file matching the mechanism, not the industry.** Tinder is in
`marketplaces.md` because it solved a hard side, not in a consumer-social file.

**No invented statistics.** If there is no data, say so.

## Adding a case

Each case needs: what happened with dates, **the structural decision** that moved
it, what transfers, and what does not. If your case concludes "they posted
consistently," you have not found the mechanism yet — keep digging. In every case
currently in this repo, the win was structural.

## Adding a skill

```
skills/<name>/
├── SKILL.md          frontmatter: name (matches dir), description, metadata.version
└── evals/evals.json  at least 2 evals with prompt, expected_output, assertions
```

Write at least one eval where **the correct behavior is to push back on the
question as asked.** That is the behavior this repo exists to produce, and a
skill without one probably prescribes too eagerly.

Bump `metadata.version` and add the row to `VERSIONS.md` in the same PR.

## Validation

```bash
python3 -c "import json,glob; [json.load(open(f)) for f in glob.glob('skills/*/evals/evals.json')]; print('ok')"
```
