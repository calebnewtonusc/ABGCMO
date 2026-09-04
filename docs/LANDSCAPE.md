# The landscape

Surveyed on 2026-09-03 by searching GitHub for `marketing`, `growth`, `gtm`,
`growth hacking`, `go-to-market`, and `product management`, then reading the file
trees of the leading repos. Star counts are as of that date.

This exists for two reasons. It stops ABGCMO from duplicating work that already
exists and is better, and it tells you where to send someone whose question this
repo does not answer well.

## The field

| Repo | Stars | What it is |
|---|---|---|
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 46,805 | **The incumbent.** 49 marketing execution skills — ads, copywriting, CRO, SEO, email, pricing, analytics. 465 files. Every skill has evals and references. |
| [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | 25,981 | 100+ product management skills, discovery through strategy |
| [goabstract/Marketing-for-Engineers](https://github.com/goabstract/Marketing-for-Engineers) | 13,219 | Curated article and tool list, not agent-installable |
| [mmccaff/PlacesToPostYourStartup](https://github.com/mmccaff/PlacesToPostYourStartup) | 6,892 | Compiled directory list from an Ask HN thread |
| [EdoStra/Marketing-for-Founders](https://github.com/EdoStra/Marketing-for-Founders) | 6,823 | First 10 / 100 / 1000 users resources |
| [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) | 6,809 | PM methods framework for coding agents |
| [draftdev/startup-marketing-checklist](https://github.com/draftdev/startup-marketing-checklist) | 5,642 | Tactic checklist |
| [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | 3,479 | Growth experiments, content ops, outbound. Has scoring rubrics and Python tooling. |
| [kuchin/awesome-ceo](https://github.com/kuchin/awesome-ceo) | 2,632 | Founder and leader resource list |
| [Eronred/aso-skills](https://github.com/Eronred/aso-skills) | 1,823 | App Store Optimization specifically |
| [RefoundAI/lenny-skills](https://github.com/RefoundAI/lenny-skills) | 1,304 | 86 PM skills distilled from Lenny's Podcast. Each skill carries `guest-insights.md`. |
| [onvoyage-ai/gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) | 1,299 | AEO and GEO — optimizing for AI answer engines |
| [gooseworks-ai/goose-skills](https://github.com/gooseworks-ai/goose-skills) | 1,195 | Growth and GTM skills plus data APIs |
| [mikiarlo3/awesome-growth-hacking-skills](https://github.com/mikiarlo3/awesome-growth-hacking-skills) | 701 | Index of growth-hacking skills |
| [gtmagents/gtm-agents](https://github.com/gtmagents/gtm-agents) | 396 | GTM agents and skills |
| [zapier/gtm-cheat-codes](https://github.com/zapier/gtm-cheat-codes) | 334 | Zapier's own. GTM **ops automation** wired to Zapier MCP. Every skill ships SETUP, SCHEMA-MAP, and an onboarding prompt. |
| [Cold-IQ/ColdIQ-s-GTM-Skills](https://github.com/Cold-IQ/ColdIQ-s-GTM-Skills) | 270 | Cold email and LinkedIn ads in depth. 137 sales triggers, 34 templates. |
| [Gingiris/gingiris-launch](https://github.com/Gingiris/gingiris-launch) | 203 | Product Hunt launch playbook from a 30x #1 winner |
| [marketinguys/awesome-gtm-engineering](https://github.com/marketinguys/awesome-gtm-engineering) | 148 | GTM engineering tool list |

## What the field is missing

Read across all of them and four gaps are consistent:

1. **Nobody tiers evidence.** Every repo states numbers as fact. Much of the
   underlying growth literature is SEO content published by companies selling
   growth software, and figures get recycled between blogs until they read like
   consensus. ABGCMO tags every number Measured, Reported, or Asserted, and there
   is at least one place where the measured data reverses the universal advice —
   the "Show HN" tag has no significant effect (arXiv 2511.04453, p = 0.39).

2. **Nobody ships a case ledger.** These repos teach methods without the worked
   examples that show when a method applies. ABGCMO carries 60+ companies in
   `cases/`, organized by **mechanism** rather than industry, so you can match a
   situation instead of a vertical.

3. **Nobody refuses to answer.** Every repo will happily produce a channel plan
   for a product with 2% retention. ABGCMO's first rule is diagnose before you
   prescribe, and `skills/growth-diagnosis` is written to decline the question as
   asked when acquisition is the wrong work.

4. **Open source and non-commercial growth are absent.** The field assumes a SaaS
   with a pricing page. There is nothing on growing a repository, and nothing on
   movements, nonprofits, or community organizing, which run on the same
   mechanics with participation as the currency instead of revenue.

## What ABGCMO is not

It is not a marketing execution pack. If you need ad creative, landing page copy,
an SEO audit, or a paid media plan, **use
[marketingskills](https://github.com/coreyhaines31/marketingskills)** — 49 skills,
deep references, and it is better at that than this repo will ever be.

If you need cold email infrastructure at depth, use
[ColdIQ](https://github.com/Cold-IQ/ColdIQ-s-GTM-Skills). If you need GTM ops
automation, use [Zapier's](https://github.com/zapier/gtm-cheat-codes). If you need
PM career and product-craft skills, use
[lenny-skills](https://github.com/RefoundAI/lenny-skills).

ABGCMO is the layer above those: **deciding what to do and whether the evidence
supports it.** Install it alongside them, not instead of them.

## Conventions borrowed from the field

Worth stating plainly since they came from reading these repos:

- Skills follow the [Agent Skills specification](https://agentskills.io/specification.md)
  and install to `.agents/skills/`, the cross-agent standard.
- Per-skill `metadata.version` plus a `VERSIONS.md` table, so installed users can
  see what changed. An unbumped change is invisible to them.
- `evals/evals.json` per skill with prompt, expected output, and assertions.
  These are as much a specification of intended behavior as they are a test.
- `AGENTS.md` alongside `CLAUDE.md` so non-Claude agents get the same guidance.
