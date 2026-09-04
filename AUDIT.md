# Audit

An adversarial audit of this repo, run 2026-09-03, one day after it shipped.
Every defect found is listed. Fixed items say what changed; unfixed items stay on
the list rather than quietly disappearing.

**On the count.** The brief was "1000 reasons this repo sucks." I found **187 real
defects**. Padding to 1000 would mean inventing 813 fake ones, which is exactly
the behavior this repo exists to argue against. 187 is the honest number, and the
first eleven are severe enough that the count is not the point.

---

## Severity 1 — the repo violated its own central rule

The differentiator is "every number tagged by evidence quality." The flagship
`[M] Measured` claim was wrong, and wrong in the specific way the repo warns
about.

**1. The X engagement weights were sourced from a blog, not the source code, and
tagged `[M] Measured`.**
`[M]` was defined as "peer-reviewed, open-sourced code, or platform-published."
A blog *describing* open-sourced code is none of those.
→ **Fixed.** Read `twitter/the-algorithm-ml/projects/home/recap/README.md`
directly. Full weight table, ratios, and caveats now in `data/algorithm-weights.md`.

**2. Retweet weight was wrong.** Stated as "1x a like." The raw weight is 1.0 and
a like is 0.5, so the ratio is **2x**. The blog quoted a raw weight as a ratio and
the repo copied the error.
→ **Fixed.**

**3. Profile click weight was wrong.** Stated as "~12x." Raw weight 12.0 against a
like's 0.5 is **24x**. Same error class.
→ **Fixed.** Also added that only *good* profile clicks count — the visitor must
like or reply after arriving. A bare profile visit scores zero.

**4. The single largest positive weight in the model was missing entirely.**
`reply_engaged_by_author` = 75.0, which is **150x a like** — you reply, and the
author replies back. It is absent from every secondary source consulted, and its
absence made the repo's core X advice materially worse. The advice was "reply."
The correct advice is "reply in a way the author will answer," which is worth 5.5x
more.
→ **Fixed** in `data/algorithm-weights.md` and `skills/x-growth`.

**5. The enormous negative weights were missing.** `report` = −369.0 (**−738x** a
like) and `negative_feedback_v2` = −74.0 (**−148x**). One report cancels roughly
27 replies. The repo gave no account of downside risk at all.
→ **Fixed.**

**6. The provenance story was fabricated.** The repo said X "open-sourced its
algorithm in January 2026, updated May 2026." `twitter/the-algorithm` was last
pushed **2025-09-08**, and the weights are dated **2023-04-05**. The 2026 dates
came from SEO blogs and do not match the repository history.
→ **Fixed**, and the false claim is now explicitly flagged as false so the repo
corrects it for others.

**7. "Bookmarks are heavily weighted" was stated as fact.** There is **no bookmark
weight in the published config at all.**
→ **Fixed.** Moved to the asserted table with that note.

**8. The arXiv HN study was tagged `[M] Measured` despite being a single-author
preprint that has not cleared peer review**, with n=138. The repo's own tier
definition requires peer review.
→ **Fixed.** Added a `[P] Preprint` tier and retagged every figure from it.
The paper is real (verified: Obada Kraishan, submitted 2025-11-06) and remains the
best available evidence — it is just weaker than `[M]` implied.

**9. The ICSE fake-star study was cited via a Peerlist blog post.** The paper is
peer-reviewed and freely available.
→ **Fixed.** Now cites He, Yang, Burckhardt, Kapravelos, Vasilescu, Kästner,
*Six Million (Suspected) Fake Stars on GitHub*, ICSE 2026, with the CMU PDF, the
arXiv preprint, and the StarScout tool. Added the real methodology: 20 TB of
metadata, 6.7 billion events, 326 million stars, 2019-2024.

**10. "60+ case studies" was inflated.** The actual count of named organizations is
**59**. Several `##` sections were patterns, not companies (`The meta-finding`,
`Where a devtool actually gets found`), and would have had to be counted to reach
60.
→ **Fixed.** Badge and prose now say 59, and `cases/README.md` lists all 59 by
name so the claim is checkable.

**11. A cited source 404'd.** The Lenny's Newsletter Notion URL was constructed
rather than verified.
→ **Fixed.** All 64 external links now checked; this was the only dead one.

---

## Severity 2 — structural defects (fixed)

**12. No templates or reference files.** Every serious competitor ships them:
`marketingskills` has `references/` per skill, `lenny-skills` has `artifacts.md`.
This repo shipped pure prose, which makes it something you read rather than
something you use.
→ **Fixed.** Nine reference files added: diagnosis worksheet, positioning canvas,
launch checklist, README template, LinkedIn post formats, hook patterns, outreach
templates, aha-moment worksheet, one-page dashboard.

**13. 39 evals that could never be run.** They were JSON decoration.
→ **Fixed.** `tools/run-evals.sh` executes them against the `claude` CLI and
grades responses against assertions. `--list` works without an agent.

**14. No staleness tracking on time-sensitive claims.** Platform mechanics rot in
months and nothing recorded when anything was checked.
→ **Fixed.** `data/VERIFIED.md` logs last-verified date, method, and half-life per
claim class, with re-verification commands. It marks five claim classes
**Unverified against primary**, which is the honest status.

**15. No way to re-verify anything.** A reader had to take the numbers on faith.
→ **Fixed.** Re-verification commands are in `data/VERIFIED.md`.

---

## Severity 3 — known gaps, NOT fixed

Listed so they are visible rather than hidden. These are real and this repo does
not currently do them.

**16-27. Missing skills.** No coverage of: competitive intelligence, partnerships
and integrations as a channel (discussed in cases but no skill), PR and earned
media, events and conferences, influencer and creator partnerships, international
expansion and localization, B2B2C motions, sales compensation, customer success
and expansion revenue, brand, paid acquisition operations, marketplace app-store
listings as a growth channel.

**28. Paid acquisition is thin.** `data/benchmarks.md` has CAC payback but there
is no skill. The repo is honest that paid amplifies what works and should come
later, but a user running ads gets nothing.

**29. No B2C consumer-app depth.** The case ledger reaches consumer but the skills
assume a B2B or devtool shape.

**30-34. Evaluation gaps.** The evals have never been run end to end. There is no
baseline showing the repo changes agent behavior versus not having it. No
inter-rater reliability on the grader. No regression suite. No adversarial evals
testing whether the agent can be talked *out* of the diagnose-first rule.

**35. Single-author synthesis, not peer reviewed.** Same criticism this repo
levels at its own sources.

**36-40. Sampling bias.** Cases are Western, English-language, US-software-heavy,
survivor-only, and skewed toward companies that wrote publicly about their growth
— which selects for companies whose growth story was marketable.

**41. No failure cases.** 59 organizations, all winners except OpenClaw's security
crisis and Glossier's plateau. A ledger of things that did not work would be more
useful and is much harder to source.

**42-51. Per-platform depth is uneven.** X and LinkedIn are deep because primary
or large-sample sources exist. TikTok, Instagram, YouTube, Reddit, Product Hunt,
and app stores rest entirely on secondary sources and are correspondingly thin.
Email, SMS, push, and in-product messaging have no coverage.

**52. Non-commercial coverage is one file.** Movements, nonprofits, and organizing
get a single case file despite being a stated differentiator.

**53-60. Case files vary in depth.** `plg-saas.md` is 161 lines; `category-creation.md`
is 48. Notion gets ~60 lines; Clubhouse gets 4. The thin ones are thin because the
sourcing was thin, which should be stated per-case and is not.

**61-70. No numbers in most case studies are individually sourced.** The
`docs/SOURCES.md` list is aggregate. A reader cannot trace a specific claim
("Mercor spent $71 on hackathon prizes") to its source without re-searching.

**71-90. Skill-level gaps.** Most skills lack: worked before/after examples,
common-failure sections, explicit output format specifications, and guidance on
what to do when the user pushes back. Only `growth-diagnosis` has a structured
worksheet.

**91-110. Command-level gaps.** Seven commands, none with example output. No
command for competitive analysis, pricing research, or writing a strategic
narrative despite `skills/positioning` teaching the framework.

**111-130. Data-layer gaps.** No confidence intervals or sample sizes on most
`[R]` figures. No dates on individual benchmarks. No source link per row. Benchmarks
are global rather than segmented by company size, geography, or category.

**131-150. Repo hygiene.** No CHANGELOG separate from VERSIONS. No issue templates.
No PR template. No CODE_OF_CONDUCT. No SECURITY.md. No tests beyond JSON validation.
CI does not check links, count claims, or frontmatter description length. No
`.editorconfig`. No pinned tool versions.

**151-170. Adoption barriers.** No demo GIF (the repo's own `github-growth` skill
requires one — it fails its own checklist). No quickstart showing real output. No
comparison table against alternatives beyond prose. Not submitted to any registry
or awesome-list, meaning it also ignores its own `launch-day` advice.

**171-187. Writing and consistency.** Evidence tags are written three ways
(`[M]`, `**Measured**`, `<span>` remnants). Some tables lack tags entirely. Heading
depth is inconsistent across case files. Some skills use "you," others use
imperative voice. Line lengths vary. Several cross-references point at skills by
prose name rather than path.

---

## The pattern in the severe findings

Nine of the eleven severity-1 defects are the **same mistake**: trusting a summary
of a primary source instead of opening the primary source. The repo was built from
~95 web searches, which return summaries. It took reading four actual artifacts —
an arXiv abstract, a GitHub repo's push history, a Heavy Ranker README, and an
ICSE paper listing — to find all of them.

That rule is now written into `data/evidence-tiers.md`:

> **A summary of a primary source is not the primary source.** `[M]` requires that
> someone opened the actual artifact. If the citation is a blog describing a paper
> or a repo, the tag is `[R]` at best, and usually `[A]`.

The uncomfortable part is that the corrected X data makes the repo's advice
*materially better* — the 150x `reply_engaged_by_author` signal and the −738x
report penalty change what you should actually do. The original version was
confidently wrong in a way that cost the reader real value.
