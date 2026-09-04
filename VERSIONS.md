# Versions

Per-skill versions. Bump on any shipped change; an unbumped change is invisible to installed users.

## 1.0.0 — 2026-09-03

Initial release. 19 skills, 39 evals, 60+ cases, 4 data references.

| Skill | Version |
|---|---|
| `activation-retention` | 1.0.0 |
| `anti-patterns` | 1.0.0 |
| `cold-start` | 1.0.0 |
| `community-led-growth` | 1.0.0 |
| `content-engine` | 1.0.0 |
| `founder-led-sales` | 1.0.0 |
| `github-growth` | 1.0.0 |
| `growth-diagnosis` | 1.0.0 |
| `growth-loops` | 1.0.0 |
| `launch-day` | 1.0.0 |
| `linkedin-growth` | 1.0.0 |
| `metrics` | 1.0.0 |
| `newsletter-growth` | 1.0.0 |
| `positioning` | 1.0.0 |
| `pricing-packaging` | 1.0.0 |
| `reddit-hn` | 1.0.0 |
| `seo-geo` | 1.0.0 |
| `short-form-video` | 1.0.0 |
| `x-growth` | 1.0.0 |

## 1.1.0 — 2026-09-03

Adversarial audit. 187 defects found, 11 severity-1. See [AUDIT.md](AUDIT.md).

**Corrections**
- X Heavy Ranker weights re-read from the primary source. Retweet 1x → **2x**,
  profile click 12x → **24x**, and added `reply_engaged_by_author` at **150x** —
  the largest positive weight in the model, absent from every secondary source.
  Added the negative weights: report **−738x**, negative feedback **−148x**.
- Removed the false claim that X open-sourced its algorithm in 2026. The repo was
  last pushed 2025-09-08; weights are dated 2023-04-05.
- Removed "bookmarks are heavily weighted" — no bookmark weight exists in the config.
- Added `[P] Preprint` tier; retagged the arXiv HN study from `[M]`.
- ICSE fake-star study now cites the peer-reviewed paper, not a blog.
- Case count corrected 60+ → **59**, with a machine-parseable roster.
- Fixed one dead source link.

**Added**
- 9 reference templates across 9 skills
- `tools/run-evals.sh` — the evals are now runnable
- `data/VERIFIED.md` — staleness log per claim class
- `AUDIT.md` — full defect list including what is not fixed
- CI: table-aware evidence-tag enforcement, `[M]`-requires-primary-source check,
  self-claim count verification, monthly link checking

| Skill | Version |
|---|---|
| `x-growth` | 1.1.0 |
| `anti-patterns` | 1.0.1 |
| `growth-diagnosis`, `positioning`, `launch-day`, `github-growth`, `linkedin-growth`, `founder-led-sales`, `activation-retention`, `content-engine`, `metrics` | 1.1.0 |

## 1.2.0 — 2026-09-04

Every remaining item from AUDIT.md addressed. 19 → 33 skills, 39 → 67 evals.

**New skills:** `competitive-intelligence` · `partnerships` · `pr-earned-media` ·
`events-conferences` · `creator-partnerships` · `paid-acquisition` ·
`lifecycle-messaging` · `customer-success` · `brand` · `consumer-apps` ·
`international-expansion` · `b2b2c` · `revenue-ops` · `marketplace-listings` (all 1.0.0)

**`anti-patterns` → 1.1.0.** The 2026-09-04 eval run found the refusal transferred
reliably but the citations did not. Load-bearing figures moved out of prose into a
table with sources on the line, and the skill now states citation is required.

**Also:** `cases/failures.md`, three new commands, two worked example outputs,
repo hygiene files, benchmarks sourced and dated, first eval baseline recorded.
