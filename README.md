<p align="center"><h1 align="center">ABGCMO</h1></p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <img src="https://img.shields.io/badge/skills-19-6e56cf" alt="Skills">
  <img src="https://img.shields.io/badge/evals-39-2f855a" alt="Evals">
  <img src="https://img.shields.io/badge/case_studies-59-b7791f" alt="Cases">
</p>

<p align="center">
  <b>Growth and GTM strategy for coding agents.</b><br>
  Every number tagged by evidence quality. Sixty case studies indexed by mechanism.<br>
  Diagnoses before it prescribes.
</p>

---

## The problem this solves

Ask any agent how to grow something and you get a plausible list of channels and
a posting cadence. That answer is confidently wrong most of the time, because the
same tactic is correct at one stage and destructive at another, and because most
of the numbers in growth writing come from SEO content published by companies
selling growth software.

ABGCMO changes three behaviors:

**It diagnoses first.** Ask it how to get more signups for a product where 2,000
people signed up and 40 stayed, and it will decline the question as asked and
tell you that acquisition will make the leak faster.

**It tags its evidence.** Numbers are marked `[M] Measured` (peer-reviewed,
open-sourced code, platform-published), `[R] Reported` (large-sample analysis by
someone with the data), or `[A] Asserted` (repeated across blogs with no
traceable origin). Where those conflict, measured wins and it says so.

**It carries worked examples.** 59 organizations in `cases/`, organized by the
mechanism that moved them rather than by industry, so a student launching a dev
tool on campus gets Tinder's sorority tour, not another dev-tool case.

## Three things it will tell you that most guides get wrong

- **The "Show HN" tag has no measurable effect.** The only controlled study
  (arXiv 2511.04453, n=138, single-author preprint) found β = −119.2, SE = 138.3, **p = 0.39** once you
  control for stage selection. Every guide recommends it. What actually predicts
  outcome is posting hour, existing stars, and documentation quality.
- **LinkedIn long-form articles underperform ordinary posts by ~31% on reach**
  (0.69x, median 596 people). The article is not the distribution — it is the
  asset. It earns 3x profile visits per impression and gets cited by AI systems.
- **On X, the largest positive ranking weight is a reply the author replies back
  to — 150x a like** (`reply_engaged_by_author` = 75.0 against a like's 0.5). It is
  absent from essentially every growth blog, which also get retweets wrong (2x, not
  1x) and profile clicks wrong (24x, not 12x). Read from
  [the source](https://github.com/twitter/the-algorithm-ml/blob/main/projects/home/recap/README.md),
  not a summary. A **report is −738x** a like, so one report cancels ~27 replies.

## Install

**As a Claude Code plugin:**
```bash
/plugin marketplace add calebnewtonusc/ABGCMO
/plugin install abgcmo
```

**Or clone it anywhere an agent reads files:**
```bash
git clone https://github.com/calebnewtonusc/ABGCMO.git
```

Skills follow the [Agent Skills spec](https://agentskills.io/specification.md), so
they work in Claude Code, Codex, Cursor, and anything else reading
`.agents/skills/`. `CLAUDE.md` and `AGENTS.md` carry the same doctrine.

## Use it

Just describe the situation. The router in `CLAUDE.md` picks the skill.

```
> we have 2000 signups and 40 active users, how do we get more signups
> my repo has 4 stars, all from friends
> should I create a new category for this product
> how do I get my first 10 customers
> someone offered to sell me github stars
```

Or run a command directly:

| Command | Does |
|---|---|
| `/growth-audit <target>` | Diagnoses the binding constraint, gives one action and a stopping rule |
| `/launch-plan <target>` | Concentrated single-day launch plan with per-channel copy |
| `/position <target>` | April Dunford's process, end to end |
| `/channel-fit <target>` | The one or two channels that fit, and why the rest do not |
| `/case <situation>` | Finds the case whose mechanism matches, and what is different |
| `/teardown <company>` | Researches and writes a sourced growth teardown |
| `/hook <work>` | Turns work into posts, finding the actual finding first |

## What is in it

```
CLAUDE.md / AGENTS.md   Doctrine. Five rules and the skill router.
skills/                 19 skills, each with evals
data/                   Algorithm mechanics, benchmarks, channel economics, evidence tiers
cases/                  60+ companies indexed by mechanism
commands/               7 slash commands
docs/                   The landscape, method, and sources
```

**Skills:** growth-diagnosis · positioning · cold-start · growth-loops ·
launch-day · github-growth · x-growth · linkedin-growth · short-form-video ·
reddit-hn · newsletter-growth · seo-geo · founder-led-sales · pricing-packaging ·
activation-retention · community-led-growth · content-engine · metrics ·
anti-patterns

**Platforms with documented mechanics:** X · LinkedIn · GitHub · TikTok ·
Instagram · YouTube · Reddit · Hacker News · Product Hunt · App stores

**Cases span:** marketplaces · devtools · open source · PLG SaaS · consumer ·
AI-native · creators and media · commerce · movements and nonprofits · category
creation

## What this is not

It is not a marketing execution pack. For ad creative, landing page copy, SEO
audits, or paid media, use
**[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**
(46.8k stars, 49 skills) — it is better at that than this will ever be. For cold
email infrastructure use [ColdIQ](https://github.com/Cold-IQ/ColdIQ-s-GTM-Skills);
for GTM ops automation use [Zapier's](https://github.com/zapier/gtm-cheat-codes);
for PM craft use [lenny-skills](https://github.com/RefoundAI/lenny-skills).

ABGCMO is the layer above those: deciding what to do, and whether the evidence
supports it. Install it alongside them. Full survey in
[docs/LANDSCAPE.md](docs/LANDSCAPE.md).

## Audit

This repo was adversarially audited one day after shipping. **187 defects found**,
including eleven severity-1 errors where it violated its own central rule — the
flagship `[M] Measured` X data had been taken from a blog summary rather than the
source code, which made three weights wrong and omitted the largest positive signal
in the model entirely.

All eleven are fixed. The rest, including the ones **not** fixed, are itemized in
[AUDIT.md](AUDIT.md). `data/VERIFIED.md` records when each claim class was last
checked against a primary source and marks five of them **Unverified against
primary**, which is their honest status.

The rule that came out of it: **a summary of a primary source is not the primary
source.** CI now enforces it — an `[M]` tag without a nearby primary-source
citation fails the build.

## Honesty policy

Every case study in this repo is a survivor. The projects that followed identical
advice and stalled do not write blog posts, so the sample you are learning from
is the winners. `data/benchmarks.md` carries realistic outcomes and failure rates
alongside the success numbers, and the skills are written to say "this is normal"
when someone's numbers are below a benchmark.

Where this repo has no data, it says so and reasons from mechanism instead of
inventing a statistic.

## Contributing

New cases and corrections are the most valuable contributions, especially a
number with a better source than the one currently cited. See
[CONTRIBUTING.md](CONTRIBUTING.md).

---

All glory to God! ✝️❤️
