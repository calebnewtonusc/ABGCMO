---
name: seo-geo
description: Get found through search and through AI assistants. Use for questions about SEO, organic traffic, documentation as a channel, programmatic SEO, or getting cited by ChatGPT, Claude, and Perplexity.
metadata:
  version: 1.0.0
---

# Search and AI citation

The slowest channel, the largest, and the only one that compounds without you.

## Documentation is the channel most teams ignore

For most devtool companies, **documentation pages drive 40-60% of total organic
traffic.** Teams treat docs as a chore rather than as the largest channel they own.

Stripe and Twilio both grew primarily on documentation. Stripe's "seven lines of
code" was a *product* decision that shaped the API, the docs, and the support
model — not a tagline.

Practical: every error message your product emits should have a docs page that
ranks for that error string. People search error text verbatim.

## Starting from zero

Three content pillars: **tutorials, comparisons, conceptual pieces.** Target
long-tail keywords harvested from Stack Overflow, Reddit, and Google's People
Also Ask. Ten solid articles on specific long-tail terms is enough to see first
organic traffic in 2-3 months.

## Programmatic SEO

Generating keyword-targeted pages at scale from a dataset. Requires three things,
and it fails without all three:

1. A **repeatable keyword pattern** that matches how people actually search
2. A **structured dataset** that makes each page genuinely different
3. A **template** that answers the query for every variation

| Example | Result |
|---|---|
| Zapier — "connect X to Y" integration pages | 2.6M organic visits/month |
| Wise — currency conversion + SWIFT code pages | 60M+ organic visits/month |
| Nomad List — city pages with live cost/weather/internet data | 50k organic visits/month |

Nomad List is the instructive one: it combines **real-time data with
user-generated content**, so pages are not just template fills. Thin programmatic
pages with no real data get treated as spam and deindexed.

## GEO — being cited by AI assistants

AI-referred sessions rose **527% year over year** in the first five months of 2025.
This is now a real channel and it behaves differently from search.

What gets cited:
- **Clear heading structure.** Assistants extract sections, not pages.
- **Named frameworks and specific factual claims.** A claim with a number and a
  source is quotable; an opinion is not.
- **Long-form with structure** far outperforms short conversational posts. This is
  a specific finding about LinkedIn articles that generalizes.
- **Recency**, especially for Perplexity, which leans hard on fresh content.

Platform behavior differs: Perplexity is citation-heavy and prefers recent
content; Claude synthesizes rather than quoting and favors well-structured,
logical content.

**Practical:** write the thing that would be the best possible source for a
question someone asks an assistant. Heading per claim, numbers with attribution,
a named framework people can reference. This repo is written that way on purpose.
