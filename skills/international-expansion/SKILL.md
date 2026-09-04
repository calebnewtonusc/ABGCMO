---
name: international-expansion
description: Expand a product into new countries and languages without wasting the effort. Use when asked about localization, international growth, entering a new market, translation, or global launches.
metadata:
  version: 1.0.0
---

# International expansion

## Follow the traffic you already have

The cheapest international expansion is the one already happening. Before planning
anything, look at where your users are.

```bash
# GitHub: where traffic comes from
gh api repos/OWNER/REPO/traffic/popular/referrers --jq '.[]|"\(.count)\t\(.referrer)"'
```

Notion discovered **700,000 people from one country** visiting the site and traced
it to a single YouTube video, which is how their creator program started. A
43,000-member Notion community grew in Korea organically, and community leaders
there were eventually hired as certified consultants. See `cases/plg-saas.md`.

**A market that is already growing without you is the one to invest in.** Picking
a market off a TAM spreadsheet is far riskier.

## Localization is not translation

Translating the interface is the smallest part. In order of actual impact:

1. **Payment methods.** The single biggest conversion blocker. Cards are not
   universal; local methods often are.
2. **Pricing in local currency**, at a locally sensible number, not a converted one.
3. **Legal and tax**: VAT, GDPR, data residency, invoicing requirements.
4. **Support in the language**, in local business hours.
5. **Documentation** — often higher impact than UI strings for technical products.
6. **UI strings.** Last, because it is what everyone does first.

For a developer tool specifically, English documentation is frequently acceptable
while local payment methods are not.

## The distribution multiplier

MrBeast dubs videos into **40+ languages**, so one video concept earns from North
America, South America, Europe, and Asia simultaneously. That multiplies the
return on every dollar of production. See `cases/creator-media.md`.

The generalization: **content you have already made is the cheapest thing to
localize**, because the creation cost is sunk. Translate your best-performing
existing assets before making new ones.

## Sequence

1. **Confirm demand exists** in the traffic data
2. **Localize payment and pricing** — often produces most of the lift alone
3. **Find one local community leader.** Notion's Korea growth ran on one person.
4. **Then** localize content and support
5. **Then** consider a local entity, hiring, and a go-to-market motion

Most companies do this in reverse and spend heavily before proving demand.

## Where growth mechanics differ

- Platform mix varies enormously by country; do not assume your home stack.
- **Compensation arbitrage cuts both ways.** Mercor sourced elite IIT engineers
  with prizes totalling $71 because local big-tech offers were ~$5/hour. Costs and
  willingness-to-pay both move.
- Trust signals are cultural. Logos, testimonials, and guarantees carry different
  weight in different markets.

## Common failure

Machine-translating the site into twelve languages at once. It produces twelve
markets you cannot support, twelve versions of stale copy to maintain, and SEO
that ranks for nothing. **One market, done completely**, beats twelve done
partially — the same containment principle as `skills/cold-start`.
