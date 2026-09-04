# Platform algorithm mechanics

Ranking signals per platform. Tags per `evidence-tiers.md`.

---

## X (Twitter)

xAI open-sourced the recommendation algorithm in January 2026, updated May 2026.
This is the only major platform where weights are directly observable.

| Signal | Weight vs. a like | Tag |
|---|---|---|
| Reply | **27x** | [M] |
| Profile click | **~12x** | [M] |
| Like | 1x | [M] |
| Retweet | ~1x | [M] |
| Bookmark | Heavy, multiplier undisclosed | [M] |
| Dwell time | Described as outweighing all click-based signals | [M] |

**Structural fact:** the For You feed pulls ~1,500 candidates per session and
scores them on replies, bookmarks, and author reputation — **not follower
count**. This is why a zero-follower account can be surfaced at all. [M]

| Decay | Value | Tag |
|---|---|---|
| Share of eventual reach set in first 30 min | ~70% | [A] |
| Share of lifetime impressions within 2 h | ~80% | [A] |
| Reach remaining at hour 6 | <20% | [A] |

| Format vs. single text post | Effect | Tag |
|---|---|---|
| Thread (5-9 posts) | ~3x | [A] |
| Native video | +40-60% | [A] |
| Image | +15-25% | [A] |
| Poll | 2-3x or -50% | [A] |
| **External link in main post** | **-30 to -70%** | [A] |
| External link, non-Premium acct (since Mar 2026) | reported median engagement of zero | [A] |
| X Premium reach multiplier | 2-4x | [A] |

**Operating rule:** link goes in the first self-reply, never the main post.

---

## LinkedIn

Ranking shifted from viral reach toward "depth and authority." Dwell time governs.

| Signal | Value | Tag |
|---|---|---|
| Engagement rate, 0-3 s dwell | 1.2% | [R] |
| Engagement rate, 61+ s dwell | 15.6% | [R] |
| Spread attributable to dwell alone | **13x** | [R] |
| Comment weight vs. like | 2x-15x (sources disagree, direction agreed) | [A] |
| External link reach penalty | ~-60% | [R] |
| Algorithm evaluation window | 60-90 min | [R] |
| Lift from replying to comments | ~+30%, strongest inside 15 min | [R] |
| Feed post reach as share of followers | 8-12% | [A] |

| Format | Engagement | vs. average | Tag |
|---|---|---|---|
| **Document / PDF carousel** | **6.60%** | +39% reach, +30% engagement | [R] |
| Native video | 5.60% | — | [R] |
| Text post | baseline | 1.0x | [R] |
| Long-form article | — | **0.69x** (median 596 people) | [R] |

Carousel spec: portrait 4:5 (1080x1350), 7-10 slides is the sweet spot, 5-15 acceptable. [R]

**Closed loophole:** link-in-first-comment is penalized as of early 2026. This is
the exact inverse of X. Do not carry the habit across. [R]

**Timing:** Tue-Thu, 10 AM-12 PM local as baseline. 2026 shift: late afternoon
now beats morning; Wednesday 4 PM is the single strongest slot. Correct timing
worth +30-50% impressions. [R]

**Newsletters bypass the feed.** First edition auto-invites every existing
connection and follower. New followers get auto-prompted. No external-link
penalty, because reach is notification-driven. Platform-wide newsletters grew
150% YoY to 450M+ subscribers. [A]

---

## GitHub

No published algorithm. Observable behavior:

- Trending ranks on **star velocity relative to the repo's own recent baseline**,
  recomputed ~8x/day, sliced by language and by day/week/month. [A]
- A repo averaging 2 stars/day that gets 10 outranks one averaging 50 that gets 60. [A]
- **Consequence:** a concentrated burst of 80 stars in one day beats a steady
  trickle totalling far more over a month. Fire every channel on the same day.

Hacker News effect, from the only controlled study (arXiv 2511.04453, n=138 AI/LLM repos, 2024-25):

| Window | Mean stars gained | Tag |
|---|---|---|
| 24 h | +121 | [M] |
| 48 h | +189 | [M] |
| 7 days | +289 | [M] |

- Posting in the **12:00-17:00 UTC** window: ~+200 stars vs. poor timing. [M]
- **"Show HN" tag: no significant effect** (beta = -119.2, SE = 138.3, p = 0.39). [M]
- Predictors in order: HN score, baseline stars, posting hour, docs quality. [M]
- Model fit predicting 7-day stars from pre-launch data: R² = 0.48. [M]
- **Medians run far below these means.** Most repos see modest gains; a few go
  vertical. The mean is not your expectation.
- Front page needs ~30-50 upvotes in hour one. Traffic half-life ~24 h. [A]

README conversion:
- Star/no-star decision made in ~15 seconds. [A]
- Detailed READMEs get ~+50% more contributions (GitHub's own research). [R]
- Star-history chart: +15% star conversion. [A]
- Demo GIF: keep 2-5 MB, 10 MB hard ceiling. [A]

---

## TikTok

| Signal | Value | Tag |
|---|---|---|
| Watch time + completion rate share of ranking | 40-50% | [A] |
| Target completion rate | ~70% | [A] |
| Weakest signal | likes | [A] |
| Strongest signals | shares, saves, comments | [A] |

**Follower count is not a direct ranking factor.** Interest-graph, not social-graph.
Every video is shown to a small test pool first; performance there decides
whether it expands. A 15-second video watched to completion outranks a 60-second
video with more total seconds but lower completion. [A]

---

## Instagram / Reels

- Separate ranking model per surface (Feed, Reels, Stories, Explore), unified by
  a per-account trust score. [A]
- **DM shares carry the most weight for unconnected reach** (stated by Mosseri). [R]
- Completion rate is the single strongest Reels signal. [A]
- Likes are now the weakest signal. Saves, comments, shares dominate. [A]
- Accounts under 50k are described as the sweet spot for organic growth. [A]

---

## YouTube

| Metric | Healthy | Tag |
|---|---|---|
| CTR baseline | 4-8%; 10%+ strong; <2% means packaging is wrong | [A] |
| CTR target, browse, new channel | 5-8% | [A] |
| CTR target, browse, established | 7-12% | [A] |
| Average view duration | >50% strong, >70% exceptional | [A] |

Satisfaction and retention quality now outrank raw watch-time accumulation.
Every upload is tested on its own merit, so small channels do get discovered. [A]

---

## Reddit

Not an algorithm so much as an enforced social contract.

- ~10:1 rule: no more than ~10% of your activity should be self-promotional. [A]
- Frame the post as a lesson, guide, or question. The tool is context, not the pitch. [A]
- No link in the title. No bare product pitch outside designated threads. [A]
- Comments that perform read like honest advice from a friend, including
  acknowledging where competitors are better. [A]

---

## Product Hunt

| Rank | Launch-day visitors | Tag |
|---|---|---|
| Top 3 | 5,000-15,000 | [A] |
| Top 10 | 1,000-3,000 | [A] |
| Outside top 10 | <500 | [A] |

- Traffic drops 80-90% within 72 hours. [A]
- B2B conversion ~1-2%; expect 50-300 signups for a B2B tool. [A]
- Founders stacking 4-5 smaller focused directories report 14-23% conversion vs.
  Product Hunt's ~3.1%. [A]
- Ranking now weights comment quality alongside upvotes. [A]

---

## App stores (ASO)

- Search drives **65% of iOS discovery, 58% on Google Play** — the single largest
  acquisition channel. [A]
- Tap-through-to-install: 33.4% iOS, 27.7% Google Play. [A]
- Three levers: keyword relevance (title/subtitle/keyword field), conversion
  (icon, first two screenshots, video, ratings), quality signals (download
  velocity, retention, reviews, update cadence). [A]
- Apple now OCRs screenshot caption text and indexes it for keywords. [A]
