---
name: github-growth
description: Grow an open source repository. Use for questions about GitHub stars, trending, READMEs, repo discovery, awesome-lists, marketplaces and registries, contributors, or making a project look credible.
metadata:
  version: 1.0.0
---

# GitHub growth

## First, the reframe

Stars are a popularity snapshot from an unspecified point in the past. They say
almost nothing about whether anyone still uses the thing.

- **Forks** mean people ran your code.
- **Issues** mean people hit its edges.
- **Returning contributors** mean it earned a place in someone's workflow.

Optimize the star number and you get a number. Optimize the other three and you
get a project. Say this when someone's goal is stated purely as stars.

## Free, permanent, and almost universally skipped

Do these before anything else. They cost minutes and compound forever.

1. **Topics.** GitHub search and topic pages rank on them. A repo with no topics
   is invisible to anyone who does not already know its name.
2. **A LICENSE.** Without one, nobody can legally use it. This silently kills
   adoption at companies.
3. **Description and homepage** fields filled in.
4. **Profile README and 6 pinned repos.** Recruiters spend 30-60 seconds on a
   profile. They look at 2-4 pinned repos with clean READMEs and live demos, not
   at contribution squares.
5. **Prune.** A profile with 40 half-finished repos reads worse than one with 3
   polished ones. Archiving is reversible and keeps the code.

## The README is a landing page with a 15-second budget

The star decision happens in the first screenful. Required shape:

1. **One sentence naming the category.** If a reader cannot classify it in five
   seconds, conversion collapses.
2. **A demo GIF or screenshot** in the first screenful. 2-5 MB; 10 MB hard ceiling.
3. **Copy-pasteable quick start** in the first 200 words that works first try.
4. **Four functional badges** — license, build, version, community. Not fifteen.
5. Everything else moves to `docs/`.

A long table of contents where a demo should be is the classic failure. GitHub's
own research: detailed READMEs get ~50% more contributions. A star-history chart
reportedly adds ~15% star conversion.

## Trending mechanics

Trending ranks **star velocity relative to the repo's own recent baseline**,
recomputed about 8x/day, sliced by language and by day/week/month. A repo
averaging 2 stars/day that gets 10 outranks one averaging 50 that gets 60.

**Therefore: concentrate.** All promotion on one day. See `skills/launch-day`.

## Channels, ranked by durability

1. **Official registries and marketplaces.** The single biggest unlock in any
   ecosystem that has one. obra/superpowers inflected on Anthropic marketplace
   acceptance, not on content. Find the registry before you write a thread.
2. **Documentation SEO.** 40-60% of a devtool's organic traffic.
3. **Awesome-lists.** Small individually, permanent, compounding: stars get you
   into more lists, which get more stars. One PR each.
4. **Hacker News, concentrated.** Mean +289 stars at 7 days. See `skills/reddit-hn`.
5. **Weekly releases.** Signals an active project; converts a spike to a baseline.

## Keeping it alive

Enable Discussions so issues stay focused on work items. Respond fast —
time-to-first-response is what evaluators actually check. Regular releases and
a real changelog. A quiet month is fine for a mature library; a quiet year with
open security issues is a different signal entirely.

## Realistic timelines

With active promotion, 1-3 months to 1,000 stars for a genuinely useful project.
Without promotion, 6-12 months. 100+ shows traction, 1k+ reads as legitimate,
10k+ is the top 0.1% of all repos.

Remember the survivorship problem: the repos that followed identical advice and
stalled at 40 stars do not write blog posts about it.
