---
name: marketplace-listings
description: Get listed and ranked in registries, app stores, directories, and plugin marketplaces. Use when asked about app store optimization, plugin directories, awesome-lists, software directories, or getting into a platform's catalog.
metadata:
  version: 1.0.0
---

# Marketplace and registry listings

The highest-return, lowest-creativity growth work available. One submission,
permanent placement, and it is where people with existing intent already look.

## The general principle

**Find the registry before you write a thread.** obra/superpowers went from ~30k
to 265k+ stars, and the inflection was **acceptance into Anthropic's official
Claude Code marketplace on 15 January 2026** — a listing, not a campaign. See
`cases/open-source.md`.

Every ecosystem has one. Find yours and get in it.

## Claude Code plugin marketplaces

Two paths:
- **Official** (`anthropics/claude-plugins-official`) — curated by Anthropic,
  inclusion at their discretion
- **Community** (`anthropics/claude-plugins-community`) — open to anyone

Submit at `clau.de/plugin-directory-submission`. The pipeline runs
`claude plugin validate` plus automated safety screening (malware, credential
harvesting, known bad actors). Approved plugins get pinned to a commit SHA.

**Most common rejection cause: a `plugin.json` version that disagrees with the
CHANGELOG or git tags.** Check that before submitting.

## Awesome-lists

Small individually, permanent, and compounding — more stars gets you into more
lists, which gets more stars.

- One PR per list. Read the contribution guide; most have a strict format.
- Add yourself in the right category, alphabetized if the list is.
- Do not submit to a list you do not belong on; maintainers remember.

For the Claude Code ecosystem specifically: `hesreallyhim/awesome-claude-code`
(36.8k) is the canonical curated list, `affaan-m/everything-claude-code` (141k) is
the aggregator. 24,403 repos contained Claude Code skill or plugin definitions by
late June 2026 [A].

## App stores (ASO)

**Search drives 65% of iOS discovery and 58% on Google Play** [A] — the single
largest acquisition channel for most apps.

Three levers:
1. **Keyword relevance** — title, subtitle, iOS keyword field
2. **Conversion** — icon, first two screenshots, preview video, ratings
3. **Quality signals** — download velocity, retention, reviews, update cadence

| Metric | Value | Tag |
|---|---|---|
| Tap-through-to-install, iOS | 33.4% | [A] |
| Tap-through-to-install, Google Play | 27.7% | [A] |

**iOS renders the first three screenshots above the fold**; Google Play surfaces
description and similar apps earlier. Apple now **OCRs screenshot caption text and
indexes it for keywords**, so hybrid captions — text plus a visual cue — outperform
screenshots that expect the UI to explain itself.

## Integration marketplaces

The Shopify App Store has been named a **#1 growth channel** by some SaaS
companies; Salesforce AppExchange is the enterprise equivalent [A]. See
`skills/partnerships` for the full treatment.

## Software directories

Founders stacking **4-5 smaller focused directories report 14-23% conversion
versus Product Hunt's ~3.1%** [A]. Directories are unglamorous and outperform the
launch platform everyone obsesses over.

## Listing optimization

A listing is a landing page with less room:
- **First line names the category.** Five-second test applies.
- **First image is the demo**, not a logo.
- **Reviews drive rank.** Ask existing happy customers directly; they will not
  think to do it unprompted.
- **Update cadence is a ranking signal** in most stores. A stale listing decays.

## Common failure

Submitting once and never returning. Rankings decay, categories get added,
requirements change. Re-check listings quarterly, and re-verify what the submission
process currently requires rather than what it required when you last looked.
