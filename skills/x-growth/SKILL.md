---
name: x-growth
description: Grow on X (Twitter), including from zero followers. Use for questions about Twitter/X strategy, threads, replies, the algorithm, posting cadence, or building a technical audience there.
metadata:
  version: 1.1.0
---

# X growth

X publishes its Heavy Ranker weights in [twitter/the-algorithm-ml](https://github.com/twitter/the-algorithm-ml).
This is the only major platform where ranking weights are directly readable rather
than inferred, so reason from them rather than from blog summaries, which get them
wrong in at least four specific ways documented in `data/algorithm-weights.md`.

## The weights [Measured — read from the source repo, not a summary]

Primary source: [`the-algorithm-ml/projects/home/recap/README.md`](https://github.com/twitter/the-algorithm-ml/blob/main/projects/home/recap/README.md),
weights dated **April 5, 2023**. Full table and caveats in `data/algorithm-weights.md`.

| Engagement | Ratio to a like |
|---|---|
| **You reply and the author replies back** (`reply_engaged_by_author`) | **150x** |
| Reply | **27x** |
| Good profile click (they visit AND like or reply) | 24x |
| Click into the conversation and engage | 22x |
| Retweet | 2x |
| Like | 1x |
| **Negative feedback** (show less, block, mute) | **-148x** |
| **Report** | **-738x** |

**Read those last two rows again.** One report costs roughly 27 replies. The
downside is wildly asymmetric, which means the highest-value strategy is not
maximizing engagement, it is producing engagement without producing irritation.

**The signal almost nobody knows about:** `reply_engaged_by_author` at 150x is the
largest positive weight in the model, and it is absent from essentially every
growth blog. The implication is precise: **the goal is not to reply, it is to
reply in a way the original author answers.** A reply that starts a conversation
is worth about 5.5x one that does not.

That single fact should reshape how you write replies. A reply that merely adds
information gets 27x. A reply that asks the author something they want to answer,
or offers a correction they will want to respond to, gets 150x.

**Also note:** a bare profile visit scores nothing. Only a "good" profile click —
where the visitor then likes or replies — counts.

**Caveats the source states outright:** the weights can be adjusted at any time,
these are from April 2023, and the released code may differ from production. The
repo was last pushed 2025-09-08; claims that X open-sourced or updated its
algorithm in 2026 do not match the repository history.

## Growing from zero: reply, do not post

Of 300 accounts that grew from under 1k to 10k+ followers in Q1 2026, **84% used
replying as the primary tactic** [A]. This is at least coherent with the
published weights, which is more than most growth advice manages.

The method:
- Reply within **5-15 minutes** of the original post.
- Target accounts with **5-20x your follower count**. Bigger buries you.
- Add a data point, a counterexample, or a specific mechanism. Agreement is
  invisible. Long replies beat short ones.
- **Write for an author response.** `reply_engaged_by_author` is 150x a like, the
  largest positive weight in the model. Ask something the author would want to
  answer, or offer a correction worth responding to. This is the highest-leverage
  single move available on the platform and almost nobody does it deliberately.
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
impressions land within 2 hours [A]. The breakout window is about 60
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
