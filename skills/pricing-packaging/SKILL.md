---
name: pricing-packaging
description: Decide what to charge and how to structure free and paid tiers. Use for questions about pricing, free tiers, freemium vs trial, monetization, or open source commercialization.
metadata:
  version: 1.0.0
---

# Pricing and packaging

## Meter by depth, not by time

The single most transferable pricing decision in the case ledger.

Notion capped the free tier at **300 blocks**, not 30 days. A time limit cuts
people off *before* attachment forms. A usage limit cuts them off *at peak*
attachment, when the decision to pay is easiest.

Dropbox did the same with storage. Cursor does it with 2,000 completions/month.

## Freemium vs. trial

| Model | Conversion | Tag |
|---|---|---|
| Freemium | 2-8%, median 4.5% | [R] |
| Freemium, broad-market tool | 1-5% | [R] |
| Freemium, tightly targeted | 5-15% | [R] |
| **Opt-out trial with credit card** | **35-55%, median 44%** | [R] |

The credit-card trial converts dramatically better because the friction filters
for intent. It also generates far less top-of-funnel. Choose based on whether you
need volume for a network effect or revenue for a runway.

## Underprice deliberately when the category is fragmented

Notion charged **$8, then $4**, for something replacing Jira, Confluence, and
Evernote. At $4, declining to try it looks foolish. That is a deliberate
friction-removal decision, not a failure to capture value.

This works when you are consolidating several tools. It does not work when you
are one tool among many.

## Finding the number

**Van Westendorp price sensitivity meter.** Four questions:
- At what price is this **too expensive** to consider?
- At what price is it **expensive but you would still consider it**?
- At what price is it a **bargain**?
- At what price is it **so cheap you would question the quality**?

Sample size: 150-200 for a single audience; 100-150 per segment if comparing
enterprise vs. SMB or by geography.

**Value-based rule of thumb:** price at 10-30% of the value you create, depending
on competitive intensity.

**Segment first.** Value perception varies enormously by vertical, company size,
and use case. A single price for all segments leaves the most money on the table
of any pricing mistake.

## Open source commercialization

**Open core is the standard model** in 2026: core is free and open, and you charge
for what enterprises need — advanced security, compliance, team management, SSO,
policy, SLAs, priority support.

The pattern across GitLab, MongoDB, HashiCorp: **enterprises pay for removal of
operational and legal stress**, not for features. Hosting, long-term support,
SBOMs, audit exports, migration help, security fixes.

GitLab, Confluent, and MongoDB each passed $1B ARR only after **many rounds of
pricing iteration**. Nobody got it right first.

Revenue is shifting toward usage-based pricing, managed hosting, and
sovereignty-friendly packaging that helps buyers pass audits.

**The license question.** Elastic relicensed when AWS offered managed
Elasticsearch; Redis followed. If a cloud provider could resell your work as a
service, decide your license posture before you are big enough for it to matter.
Retroactive relicensing costs enormous community goodwill.

## Referrals as an alternative currency

Notion: 150 blocks per friend, unlimited at six. Students who will never pay cash
will pay in friends. If your audience is price-sensitive but socially connected,
this converts better than a discount.
