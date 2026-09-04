# Platform algorithm mechanics

Ranking signals per platform. Tags per `evidence-tiers.md`.

---

## X (Twitter)

**Primary source, verified 2026-09-03:**
[twitter/the-algorithm-ml `projects/home/recap/README.md`](https://github.com/twitter/the-algorithm-ml/blob/main/projects/home/recap/README.md),
with the serving config at
[`ScoredTweetsParam.scala#L84`](https://github.com/twitter/the-algorithm/blob/main/home-mixer/server/src/main/scala/com/twitter/home_mixer/product/scored_tweets/param/ScoredTweetsParam.scala#L84).

The Heavy Ranker outputs a probability per engagement type, then takes a weighted
sum. These are the raw weights published in the repo, **dated April 5, 2023**:

| Engagement | Raw weight | Ratio to a like |
|---|---|---|
| `reply_engaged_by_author` — you reply, the author replies back | **75.0** | **150x** |
| `reply` | 13.5 | **27x** |
| `good_profile_click` — opens your profile AND likes or replies | 12.0 | **24x** |
| `good_click` — clicks into the conversation and replies or likes | 11.0 | 22x |
| `good_click_v2` — clicks in and stays 2+ minutes | 10.0 | 20x |
| `retweet` | 1.0 | **2x** |
| `fav` (like) | 0.5 | 1x (baseline) |
| `video_playback50` — watches half a video | 0.005 | 0.01x |
| `negative_feedback_v2` — show less often, block, mute | **-74.0** | **-148x** |
| `report` | **-369.0** | **-738x** |

Tag: **[M] Measured** — read from the source repository, not from a summary.

### Four things almost every secondary source gets wrong

1. **`reply_engaged_by_author` at 150x is the single largest positive signal**, and
   it is missing from essentially every growth blog. The implication is specific:
   the goal is not to reply, it is to reply in a way **the original author answers**.
   A reply that starts a conversation is worth 5.5x a reply that does not.
2. **Retweets are 2x a like, not 1x.** Blogs quote the raw 1.0 weight as a ratio.
3. **Profile clicks are 24x, not 12x** — and only "good" profile clicks count, meaning
   the visitor liked or replied after arriving. A bare profile visit scores nothing.
4. **The negative weights dwarf the positive ones.** A report is -738x a like; one
   report cancels roughly 27 replies. Negative feedback is -148x. Posting anything
   that gets muted or blocked is far more costly than any engagement is valuable.

### Caveats the source itself states

- "The exact weights in the file can be adjusted at any time." These are from
  April 2023 and the live production values are almost certainly different now.
- "There may be small differences from the production model," since the released
  code runs independently of Twitter's internal codebase.
- The repository was last pushed **2025-09-08**. Claims circulating that X
  open-sourced or updated its algorithm in January or May 2026 do not match the
  repository history and should be treated as false.

### What is NOT in the source

The following are widely repeated and are **not** in the published code. They are
`[A] Asserted` and are given as ranges, not facts:

| Claim | Reported value | Tag |
|---|---|---|
| Share of eventual reach set in first 30 min | ~70% | [A] |
| Share of lifetime impressions within 2 h | ~80% | [A] |
| External link penalty, main post | -30 to -70% | [A] |
| Non-Premium link posts, median engagement | reported near zero | [A] |
| X Premium reach multiplier | 2-4x | [A] |
| Thread (5-9 posts) vs single post | ~3x | [A] |
| Native video | +40-60% | [A] |
| Image | +15-25% | [A] |
| Bookmark weight | claimed heavy; **no bookmark weight exists in the published config** | [A] |
| "Feed pulls ~1,500 candidates" | widely repeated | [A] |

**Operating rules that survive the correction:**
- Replies are the highest-leverage action, and a reply that earns an author response
  is worth far more than one that does not.
- Never post anything likely to draw a report or a mute. The downside is asymmetric.
- Put links in a self-reply rather than the main post. The penalty is asserted, not
  measured, but the downside of being wrong is small.

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
| 24 h | +121 | [P] |
| 48 h | +189 | [P] |
| 7 days | +289 | [P] |

- Posting in the **12:00-17:00 UTC** window: ~+200 stars vs. poor timing. [P]
- **"Show HN" tag: no significant effect** (beta = -119.2, SE = 138.3, p = 0.39). [P]
- Predictors in order: HN score, baseline stars, posting hour, docs quality. [P]
- Model fit predicting 7-day stars from pre-launch data: R² = 0.48. [P]
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
