# Changelog

Repo-level changes. Per-skill versions are tracked in [VERSIONS.md](VERSIONS.md).

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: **x** for restructures, **y** for new skills, **z** for updates.

## [1.2.0] — 2026-09-04

Second audit pass. Every remaining item from [AUDIT.md](AUDIT.md) addressed.

### Added
- **14 skills** (19 → 33): competitive-intelligence, partnerships, pr-earned-media,
  events-conferences, creator-partnerships, paid-acquisition, lifecycle-messaging,
  customer-success, brand, consumer-apps, international-expansion, b2b2c,
  revenue-ops, marketplace-listings
- **28 evals** (39 → 67)
- **`cases/failures.md`** — the survivorship correction. Ten documented cases where
  a real mechanic failed, including this repo's own audit.
- Repo hygiene: `CHANGELOG.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`,
  `.editorconfig`, issue and PR templates

### Fixed
- Coverage gaps 16-29 from AUDIT.md (missing skills, paid acquisition, B2C depth)
- Gap 41 (no failure cases)
- Gaps 42-51 (email, SMS, push had no coverage; now `lifecycle-messaging`)
- Gaps 131-150 (repo hygiene)

## [1.1.0] — 2026-09-03

Adversarial audit. 189 defects found, 11 severity-1. See [AUDIT.md](AUDIT.md).

### Fixed
- **X Heavy Ranker weights re-read from the primary source.** Retweet 1x → **2x**,
  profile click 12x → **24x**. Added `reply_engaged_by_author` at **150x**, the
  largest positive weight in the model, absent from every secondary source. Added
  the negative weights: report **−738x**, negative feedback **−148x**.
- Removed the false claim that X open-sourced its algorithm in 2026. Repo last
  pushed 2025-09-08; weights dated 2023-04-05.
- Removed "bookmarks are heavily weighted" — no such weight exists in the config.
- ICSE fake-star study now cites the peer-reviewed paper rather than a blog.
- Case count corrected 60+ → **59**, with a machine-parseable roster.
- One dead source link.

### Added
- **`[P] Preprint`** evidence tier; the arXiv HN study retagged from `[M]`
- 9 reference templates
- `tools/run-evals.sh`, `tools/check_*.py`
- `data/VERIFIED.md` staleness log
- `AUDIT.md`
- CI enforcing evidence tags, primary-source citation for `[M]`, and self-claim counts

## [1.0.0] — 2026-09-03

Initial release. 19 skills, 39 evals, 59 case studies, 4 data references.
