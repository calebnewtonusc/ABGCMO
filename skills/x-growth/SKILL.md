---
name: x-growth
description: Grow on X (Twitter), including from zero followers. Use for questions about Twitter/X strategy, threads, replies, the algorithm, posting cadence, or building a technical audience there.
metadata:
  version: 1.0.0
---

# X growth

X open-sourced its recommendation algorithm in January 2026 (updated May). This is
the only major platform where the weights are directly observable rather than
inferred, so reason from them.

## The weights [Measured]

| Signal | Weight vs. a like |
|---|---|
| **Reply** | **27x** |
| **Profile click** | **~12x** |
| Like | 1x |
| Retweet | ~1x |
| Bookmark | Heavy, multiplier undisclosed |
| Dwell time | Stated to outweigh all click-based signals |

**The structural fact that matters most:** the For You feed pulls ~1,500 candidates
per session and ranks on replies, bookmarks, and author reputation — **not
follower count**. This is why a zero-follower account can be surfaced at all.

## Growing from zero: reply, do not post

Of 300 accounts that grew from under 1k to 10k+ followers in Q1 2026, **84% used
replying as the primary tactic** [Asserted]. This is at least coherent with the
published weights, which is more than most growth advice manages.

The method:
- Reply within **5-15 minutes** of the original post.
- Target accounts with **5-20x your follower count**. Bigger buries you.
- Add a data point, a counterexample, or a specific mechanism. Agreement is
  invisible. Long replies beat short ones.
- Reported yield: 100-200 profile visits/day from replies alone.
- Profile clicks are weighted 12x, so a reply that makes someone check your
  profile is worth far more than a like on your own post.

Your profile is the landing page for all of this. Make it say what you do.

## Links are close to fatal

- External link in the main post: **-30 to -70% reach**.
- Non-Premium account posting a link, since March 2026: reported **median
  engagement of zero**. Practically invisible.
- Premium: reported 2-4x reach multiplier generally.

**Rule: link goes in the first self-reply, never the main post.** Note this is the
exact inverse of LinkedIn, where the first-comment workaround is now penalized.

## Timing and decay

Roughly 70% of eventual reach is set in the first 30 minutes and ~80% of lifetime
impressions land within 2 hours [Asserted]. The breakout window is about 60
minutes. Be present to reply to replies immediately after posting — replies to
your replies are the highest-weighted thing available.

## Formats

| Format | Effect vs. single text post |
|---|---|
| Thread (5-9 posts) | ~3x |
| Native video | +40-60% |
| Image | +15-25% |
| External link | -30 to -70% |

One to three threads a week. More dilutes quality.

## What actually spreads among technical people

The hook decides most of it. Four patterns recur:
- a **contrarian claim** against received wisdom
- a **surprising number**
- a **shared frustration named precisely**
- **reference material** worth bookmarking (and bookmarks are heavily weighted)

**The strongest position available to an unknown account is a specific, hard-won,
undocumented finding.** Not an opinion, not a tutorial: something that cost you
real time to learn and is not in the docs. Those get bookmarked, and bookmarks
compound.

## What not to do

Do not post announcements. "I built X" is an ad and reads like one. Post the
*finding* that came out of building X, and put the repo in the reply. The finding
earns the click; the announcement asks for it.
