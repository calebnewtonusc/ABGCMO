---
name: competitive-intelligence
description: Research competitors honestly and turn it into a decision. Use when asked who the competitors are, how to differentiate, whether a market is too crowded, how to respond to a competitor's move, or when building a comparison page.
metadata:
  version: 1.0.0
---

# Competitive intelligence

## Your competitors are not who you think

The Dunford rule: ask **"what would this person do if we did not exist?"** In B2B
roughly 40% of deals are lost to "no decision," which means the winner was a
spreadsheet, pen and paper, or an intern. Those are the real competitors and they
never appear on a competitive grid.

Rank alternatives by what customers actually consider, not by who you follow.

## How to research without lying to yourself

1. **Read their docs, not their landing page.** The landing page is aspiration;
   the docs are what shipped.
2. **Read their changelog.** Velocity and direction are more informative than
   feature lists. A quiet year means something.
3. **Read their bad reviews**, filtered to your segment. G2, Reddit, and their own
   GitHub issues. Sort by "most recent," not "most helpful."
4. **Read their job postings.** What they are hiring for is their roadmap.
5. **Actually use it.** Pay for a month. Nothing else substitutes.
6. **For open source:** stars are a lagging popularity snapshot. Check **forks,
   issue response time, contributor count, and last release date** instead. A repo
   with 40k stars and no release in a year is not a competitor, it is a tombstone.

```bash
gh api repos/OWNER/REPO --jq '{stars:.stargazers_count,forks:.forks_count,
  issues:.open_issues_count,pushed:.pushed_at,archived}'
gh api repos/OWNER/REPO/releases --jq '.[0].published_at'
gh api "repos/OWNER/REPO/contributors?per_page=100" --jq 'length'
```

## The output is a decision, not a grid

A feature matrix where you have more checkmarks is marketing, and everyone
discounts it. The useful output answers three questions:

1. **Where are they genuinely better?** Name it. Refusing to name it is what makes
   the rest of your analysis untrustworthy.
2. **What is the segment where you are obviously first?** Not "better overall."
3. **What is their structural constraint?** What can they not do without breaking
   their own model? That is the durable opening, and it usually comes from their
   pricing, their existing customers, or their architecture.

## "The market is crowded" is usually the wrong read

Crowded means demand is proven. The real questions are whether the incumbents are
*loved* and whether there is an underserved segment.

Cursor entered a market with GitHub Copilot already dominant and reached $100M ARR
in 20 months. shadcn/ui entered the most saturated category in frontend and won by
inverting one assumption — you own the code — rather than by having more
components.

**What actually disqualifies a market:** the incumbents are genuinely loved by the
segment you would target, and you have no structural advantage. Not the count.

## Comparison pages

They rank for high-intent search and are usually the highest-converting content a
company owns. Rules that make them work:

- **Be accurate about the competitor.** One wrong claim discredits the page and
  invites a correction that travels further than the page did.
- **Name where they win.** "Choose them if you need X" makes the rest credible.
- **Segment the recommendation.** "Best for teams under 10" beats "best."
- Never compare against a competitor much larger than you by name in ads; you pay
  to educate people about them.

## Common failure

Treating competitive research as a reason to add features. Every feature you add
to match a competitor moves you toward being a worse version of them. The output
of this work should more often be a **narrowing** decision than a building one.
