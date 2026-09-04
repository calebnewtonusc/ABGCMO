# AGENTS.md

Guidance for AI agents working with or in this repository. The operating doctrine
is identical to `CLAUDE.md` — read that file first; it is the substance.

## What this repo is

**ABGCMO** — growth, GTM, and virality strategy packaged as agent skills.

- Skills follow the [Agent Skills specification](https://agentskills.io/specification.md)
  and install to `.agents/skills/` (the cross-agent standard).
- Also a Claude Code plugin marketplace via `.claude-plugin/marketplace.json`.
- License: MIT.

## Skill count

33 skills across five groups: strategy, platform, execution, revenue, motion. The
router table lives in `CLAUDE.md` and is the authority — read it before answering
any growth question.

## Structure

```
ABGCMO/
├── .claude-plugin/         marketplace.json, plugin.json
├── CLAUDE.md / AGENTS.md   Doctrine + skill router (identical guidance)
├── skills/<name>/
│   ├── SKILL.md            Required. YAML frontmatter + body.
│   ├── evals/evals.json    Behavior spec: prompt, expected_output, assertions
│   └── references/         Optional. Templates and worksheets the user fills in.
├── data/                   Reference numbers, evidence-tagged
├── cases/                  Case ledger, indexed by mechanism
├── commands/               Slash commands
├── docs/                   LANDSCAPE.md, METHOD.md, SOURCES.md
└── registry/skills.csv     Machine-readable skill index
```

## Frontmatter requirements

```yaml
---
name: skill-name          # matches directory exactly, lowercase, 1-64 chars, [a-z0-9-]
description: ...          # 1-1024 chars. State what it does AND when to use it.
metadata:
  version: 1.0.0
---
```

The `description` is the trigger. Write it so an agent knows when to load the
skill from the user's phrasing, including casual phrasing. List the situations,
not just the topic.

## The non-negotiable rules when editing content

1. **Every number carries an evidence tag.** `[M]` measured, `[R]` reported,
   `[A]` asserted. See `data/evidence-tiers.md`. Adding an untagged number is the
   one change that will be rejected outright.
2. **Never state an asserted number as fact.** Write "reported at roughly X."
3. **When asserted contradicts measured, measured wins** and the skill says so.
4. **Cases are indexed by mechanism, not industry.** A new case goes in the file
   matching how it grew, not what it sold.
5. **No invented statistics.** If the repo has no data, say so and reason from
   mechanism.

## Versioning

- Per-skill `metadata.version` bumps on any shipped change to that skill, and is
  mirrored in `VERSIONS.md`. An unbumped change is invisible to installed users.
- Repo version in `.claude-plugin/plugin.json`: **x** for restructures, **y** for
  new skills, **z** for updates to existing skills. Bump in the same PR.

## Validation

Content-only, no build step. Verify:

```bash
python3 -c "import json,glob; [json.load(open(f)) for f in glob.glob('skills/*/evals/evals.json')]"
```

- YAML frontmatter parses
- `name` matches the directory name exactly
- Every skill directory has both `SKILL.md` and `evals/evals.json`
- `registry/skills.csv` matches the skills on disk
