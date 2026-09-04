---
name: reddit-hn
description: Post on Reddit and Hacker News without getting removed or banned, and get real results. Use when planning a Show HN, a subreddit post, or asking how to promote in developer and enthusiast communities.
metadata:
  version: 1.0.0
---

# Reddit and Hacker News

Both are communities with enforced social contracts, not distribution platforms.
Treating them as channels is how people get banned.

## Hacker News

**What the only controlled study found** (arXiv 2511.04453, n=138 AI/LLM repos):

| Window | Mean stars gained |
|---|---|
| 24 h | +121 |
| 48 h | +189 |
| 7 days | +289 |

- Best window: **12:00-17:00 UTC**, worth roughly **+200 stars** vs. bad timing.
- **The "Show HN" tag has no significant effect** (beta = -119.2, SE = 138.3,
  p = 0.39) once you control for the fact that Show HN posts skew earlier-stage.
  Every guide recommends it. The data does not support it. Stop optimizing this.
- Predictors in order: HN score, existing stars, posting hour, documentation quality.
- **Medians run far below these means.** Most posts are modest; a few go vertical.

Practical:
- Front page needs roughly **30-50 upvotes in the first hour**.
- Point at the **repo**, not a landing page. HN readers convert to stars and forks.
- **Answer every comment fast.** The thread is the distribution; responsiveness
  keeps it alive.
- Traffic half-life ~24 hours. Have a follow-up technical deep dive ready for a
  few weeks later.

**Titles:** plain and factual. HN punishes marketing language harder than almost
any community. "X: a Y that does Z" beats anything with an adjective in it.

## Reddit

The rules are enforced by both mods and users, and a ban is expensive because it
is per-account and often permanent.

- **The ~10:1 rule.** Self-promotion should be under ~10% of your activity. If you
  have never posted in a subreddit, you are not ready to launch there. Build a
  comment history first — genuinely, over weeks.
- **Frame as a lesson, guide, or question.** The tool is context, never the pitch.
  "Here is what I learned building X" survives where "check out X" gets removed.
- **No link in the title.** No bare pitch outside designated threads.
- **Read the sidebar rules of the specific subreddit.** They vary enormously and
  several have a dedicated promo thread that is the only legal place to post.
- Comments that perform read like honest advice from a friend, **including
  acknowledging where competitors are better for different needs**. That single
  move buys more credibility than anything else available.

## Both

Neither community rewards polish. They reward being genuinely useful and being
straight about limitations. Leading with what your thing does *not* do is a
reliable way to be trusted on what it does.
