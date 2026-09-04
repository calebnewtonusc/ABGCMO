---
name: consumer-apps
description: Grow a consumer app or B2C product, where the buyer is a person spending their own time and money. Use for mobile apps, games, social products, direct-to-consumer, or anything without a business buyer.
metadata:
  version: 1.0.0
---

# Consumer apps

Consumer growth is a different discipline from B2B and most growth writing is
about B2B. The differences that matter:

| | B2B | Consumer |
|---|---|---|
| Buyer | Spends company money | Spends their own |
| Decision | Committee, weeks | One person, seconds |
| Retention | Contracts create inertia | Nothing keeps them |
| Monthly churn benchmark | 0.5-4% | **5-10% is common** [R] |
| Growth ceiling | Deal size | Frequency and habit |

That churn row is the whole game. Consumer products have no contractual inertia,
so **retention is the product**, not a downstream metric.

## Habit is the moat

Nothing structural keeps a consumer coming back, so the return has to be built in.

- **Duolingo's streak**: the longer it runs, the higher the cost of breaking it.
  Combined with leagues and reminders it produces genuine daily habit. Works only
  because the daily action is small.
- **Wordle's one puzzle a day**: scarcity capped how much time it could take,
  which paradoxically made people *more* likely to return daily.
- **Spotify Wrapped**: an annual event on a fixed calendar date.

Design the return trigger deliberately. If there is no reason to open it tomorrow,
retention will follow the benchmark down.

## The shareable artifact

Consumer distribution runs on artifacts, not referrals. Wordle went from **90
players to over 2,000,000 in about two months** on one design decision: a
spoiler-free emoji grid.

Why it worked, and the principles to copy:
- Encoded the result **without spoiling** the experience for the recipient
- **Socially safe to post** — sharing carried no cost to the sharer
- Plain text, so it traveled to any surface
- Every share was a peer recommendation containing **no ask**

Most products bolt on a share button that broadcasts an ad. Design for what makes
the **sharer** look good.

## Distribution reality

**App stores:** search drives 65% of iOS discovery and 58% on Google Play [A] —
the single largest acquisition channel. Tap-through-to-install averages 33.4% iOS
and 27.7% Play. Conversion wins come from the icon and the first two screenshots.
Apple now OCRs screenshot caption text and indexes it. See `data/algorithm-weights.md`.

**Short-form video:** TikTok and Reels run on interest graphs, not social graphs.
Follower count is not a ranking factor and every video is tested on its own merit,
so a zero-follower account can reach millions. See `skills/short-form-video`.

**Creators:** short-form has unusually good ROI because creators without large
followings still get large views. See `skills/creator-partnerships`.

## Monetization

- **Freemium consumer conversion is low.** 2-8%, median 4.5% [R]. Broad consumer
  products land at the bottom of that range.
- **Meter by depth, not time.** Notion capped free at 300 blocks, not 30 days. A
  time limit cuts people off before attachment forms.
- **Referrals as currency.** Notion gave 150 blocks per friend, unlimited at six.
  Users who will never pay cash will pay in friends.
- Ads only work at scale most products never reach. Do not plan on them.

## Measurement

D1, D7, and D30 retention curves, by cohort, are the primary instrument. The
question is whether the curve **flattens** — a curve that flattens at 20% is a
business; a curve that keeps declining has no floor and no amount of acquisition
will fix it.

## Common failure

Buying installs before the retention curve flattens. Consumer acquisition is
cheap enough to be tempting and the churn is fast enough that you can spend a
budget filling a bucket with no bottom. Get D30 to flatten first.
