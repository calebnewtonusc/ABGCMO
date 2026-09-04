---
name: launch-day
description: Plan and execute a concentrated launch across Hacker News, Reddit, Product Hunt, X, and LinkedIn. Use when someone is about to launch a product, repo, or feature, or asks how and when to announce something.
metadata:
  version: 1.0.0
---

# Launch day

## The one rule: concentrate

GitHub trending ranks **star velocity**. Product Hunt is a single day. Hacker News
has a ~24-hour half-life. Every one of these rewards concentration and punishes
spreading.

**Fire every channel on the same day.** A concentrated burst of 80 stars in one day
beats a steady trickle totalling far more across a month. Spreading a launch
across three weeks is the most common self-inflicted wound in this whole file.

The exception: compounding placements (registries, awesome-lists, SEO, docs) have
no timing component. Do those whenever; just do them.

## Before you launch — this is where the measured effect lives

The controlled study on HN launches (arXiv 2511.04453, n=138) found the predictors
in order: **HN score, existing star count, posting hour, documentation quality.**
Three of those four are fixed before you post.

- [ ] README rewritten: one-sentence category line, demo GIF (2-5 MB), quick start
      in the first 200 words that works on the first try, four functional badges
- [ ] Docs actually complete
- [ ] LICENSE present (without one, nobody can legally use it)
- [ ] Repo topics set
- [ ] Positioning checked against `skills/positioning` — five-second test
- [ ] Security and defaults reviewed. **Viral growth is a load test on everything
      you did not build.** See OpenClaw in `cases/open-source.md`: 135,000 exposed
      instances and a poisoned plugin registry within two weeks of going viral.
- [ ] You can be at a keyboard all day to answer comments

## Timing

| Channel | Window | Source |
|---|---|---|
| Hacker News | **12:00-17:00 UTC**, Tue-Thu | [M] ~+200 stars vs. poor timing |
| Product Hunt | 12:01 AM PT (list reset) | [A] |
| LinkedIn | Tue-Thu, 10am-12pm local, or Wed 4pm | [R] |
| X | When your audience is awake; first 30 min sets ~70% of reach | [A] |

## Hacker News

- Front page needs roughly **30-50 upvotes in the first hour**.
- **Do not agonize over the "Show HN" tag.** The only controlled study found no
  significant effect (beta = -119.2, p = 0.39). Every guide recommends it; the
  data does not support it.
- Point at the **repo**, not a landing page. HN readers convert better to stars
  and forks than to signups.
- **Answer every comment fast.** Maintainer responsiveness keeps the thread alive,
  and the thread is the distribution.
- Realistic: mean +121 stars at 24h, +189 at 48h, +289 at 7 days. **Medians run far
  below these means.** Most launches are modest; a few go vertical.

## Reddit

Different rules and they are enforced socially.
- Frame the post as a **lesson, guide, or question**. The tool is context.
- No link in the title. No bare pitch.
- The ~10:1 rule: self-promotion should be under ~10% of your activity. If you
  have never posted in the subreddit, you are not ready to launch there.
- Comments that perform read like honest advice from a friend, including
  acknowledging where competitors are better.

## Product Hunt

Top 3 pulls 5,000-15,000 visitors; top 10 pulls 1,000-3,000; outside top 10,
under 500. Traffic drops 80-90% within 72 hours and B2B conversion is ~1-2%.

Ranking now weights **comment quality** alongside upvotes. Founders stacking 4-5
smaller focused directories report better conversion (14-23%) than Product Hunt
alone (~3.1%). Do not bet the launch on one day here.

## X and LinkedIn on launch day

- **X:** lead with the *finding*, not the announcement. Link in the first
  self-reply, never the main post. See `skills/x-growth`.
- **LinkedIn:** narrative framing, no external link in the post body, and the
  first-comment workaround is penalized now. See `skills/linkedin-growth`.

## After

- Traffic half-life is about 24 hours. Have the follow-up ready.
- Check the repo's Insights → Traffic tab to see **which referrer actually sent
  stargazers**. This is the only honest attribution you will get, and it decides
  where to spend next time.
- Weekly releases afterward signal an active project, which is what converts a
  spike into a baseline.
