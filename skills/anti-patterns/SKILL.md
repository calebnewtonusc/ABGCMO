---
name: anti-patterns
description: What not to do, including tactics that are detectable, illegal, or self-defeating. Use whenever someone asks about buying followers or stars, engagement pods, growth hacks, or any tactic that sounds like a shortcut.
metadata:
  version: 1.0.1
---

# Anti-patterns

## Never: buying engagement

**Fake GitHub stars are a measured industry, not a rumor.** [M] Peer-reviewed.

> He, Yang, Burckhardt, Kapravelos, Vasilescu, Kästner. *Six Million (Suspected)
> Fake Stars on GitHub: A Growing Spiral of Popularity Contests, Spam, and Malware.*
> ICSE 2026 (IEEE/ACM 48th International Conference on Software Engineering).
> [Paper](https://cmustrudel.github.io/papers/icse2026fakestars.pdf) ·
> [preprint](https://arxiv.org/html/2412.13459v2) ·
> [StarScout tool](https://github.com/hehao98/StarScout)

Their tool scanned **20 TB of GitHub metadata — 6.7 billion events and 326 million
stars from 2019 to 2024** — and identified approximately **6 million suspected fake
stars across 18,617 repositories** from roughly **301,000 accounts**. Public
marketplaces sell stars at $0.03-0.90 each. [A]

Why not, in order of seriousness:

1. **It is illegal in the US.** The FTC Consumer Review Rule, effective 21 October
   2024, explicitly prohibits buying or selling fake indicators of social media
   influence. Penalties up to **$53,088 per violation**.
2. **It is detected.** GitHub deleted **90.42%** of repositories flagged by
   researchers by January 2025. Detection works when they run it.
3. **It poisons your own instrumentation.** You permanently lose the ability to
   tell which channel worked, which is the only reason to measure anything.
4. **It leaves permanent historical patterns** in the star timeline that anyone
   evaluating you can see.

**Engagement pods** fail on mechanism: LinkedIn explicitly devalues engagement
from people you do not otherwise interact with, so the pod degrades the signal it
exists to fake.

## Never: spreading a launch across weeks

GitHub trending ranks velocity. Product Hunt is one day. HN has a 24-hour
half-life. Diffusing promotion across three weeks is arithmetically close to not
promoting at all. See `skills/launch-day`.

## Never: acquisition before retention

If 60-70% of churn happens in the first 90 days and people are leaving, more
traffic makes the leak faster. You will spend money to produce a worse-looking
chart. Fix activation first. See `skills/activation-retention`.

## Never: growth work before product-market fit

Below 40% on the Sean Ellis test, acquisition accelerates churn. This is the most
expensive mistake on the list because it burns money and time simultaneously and
feels like progress.

## Stop: habits that were correct and are not anymore

- **Link in the first LinkedIn comment.** Worked for years, penalized since early
  2026. Still correct on X. Do not carry one platform's habit to the other.
- **Optimizing the "Show HN" tag.** The only controlled study found no significant
  effect (p = 0.39).
- **Verbatim cross-posting.** Associated with ~65% organic traffic decline after
  six months. Use canonical tags and reshape per platform.

## Watch: things that quietly cost you later

- **Naming a public project after a trademarked character.** Lucasfilm has a
  documented history of cease-and-desists over Star Wars marks, including
  trademarking "droid" and forcing renames. A project you intend to grow is
  exactly the kind that gets noticed. Resolve this before it has anything to lose.
- **Shipping without a LICENSE.** Nobody at a company can legally use it.
- **Growing before you are secure.** OpenClaw went from 9k to 190k stars in two
  weeks and simultaneously to 135,000 exposed instances, a one-click RCE, and a
  plugin registry where **20% of listings were malicious**. Viral growth is a load
  test on everything you did not build.
- **Mercenary incentives.** Crypto airdrops that rewarded raw activity produced
  farmers who dumped immediately; TVL collapsed the moment incentives ended.
  Any incentive that can be gamed will be, and the users it attracts are the ones
  you least want. Measure post-campaign retention, never participant count.

## The meta anti-pattern

**Answering a strategy question with a content calendar.** If someone asks how to
grow and the answer is a posting schedule, the diagnosis step was skipped. Go back
to `skills/growth-diagnosis`.
