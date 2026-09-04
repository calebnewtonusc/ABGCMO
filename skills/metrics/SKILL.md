---
name: metrics
description: Choose what to measure and interpret the numbers honestly. Use for questions about KPIs, North Star metrics, dashboards, analytics, attribution, or whether a number is good.
metadata:
  version: 1.1.0
---

# Metrics

## Pick one number per campaign, check it monthly

Daily checking of a weekly-moving number produces anxiety and no information.
More dashboards is almost never the answer; the failure is usually that nobody
decided which number matters.

## AARRR and the North Star, and how they relate

**AARRR (Pirate Metrics):** Acquisition, Activation, Retention, Revenue, Referral.
Useful as a *structure* — it tells you which stage is leaking.

**North Star Metric:** a single leading indicator that captures the value your
product delivers and predicts long-term growth. It must sit at the intersection of
customer value and business value, be measurable frequently, and be influenceable
by the team.

**How to use both:** use AARRR to structure the stages, then pick your North Star
from whichever stage is binding — usually activation or engagement — and use the
other stages as input metrics.

A North Star that nobody can influence is a vanity metric with a better name.

## Vanity vs. real, per channel

| Vanity | Real |
|---|---|
| GitHub stars | Forks, issues opened, **returning contributors** |
| Followers | Profile visits per week, then replies from real accounts |
| Impressions | Dwell time, saves, bookmarks |
| Signups | **Activation rate** — it predicts revenue better than any other PLG metric |
| Newsletter subscribers | Open rate by cohort, replies |
| Traffic | Traffic that activates |

The test: would this number moving tell you to do something different? If not, it
is a scoreboard, not an instrument.

## Attribution, honestly

Most attribution is a guess dressed as data. The exceptions worth trusting:

- **GitHub Insights → Traffic** shows referring sites, so you can see which launch
  or article actually sent stargazers. This is real.
- **Ask people.** A one-question "how did you hear about us" on signup beats most
  attribution tooling for early-stage products.
- **Concentrated launches destroy attribution**, which is a real cost of doing
  them. Accept it — velocity is worth more than knowing which of five channels
  did it.

## Reading a number

Before calling anything good or bad, check `data/benchmarks.md`. Most numbers
people are anxious about are normal, and most expectations come from survivor
stories.

Then check the direction and the cohort, not the level. Blended metrics hide
everything: a stable churn number can conceal your best cohorts leaving and your
worst cohorts arriving. **Later cohorts should outperform earlier ones.**

## Always set a stopping rule

Before starting any growth effort, write down: **what result, by what date, would
mean this approach is wrong?**

Without it, every effort runs forever on the argument that it needs more time.
With it, you get an honest decision on a schedule.

And when the stopping rule triggers, the answer is usually **not more volume**.
Every case in `cases/` says a stalled effort has a structural problem — wrong
category, wrong description, wrong audience, or something people do not need.
Re-read `skills/positioning` before changing the cadence.
