---
name: revenue-ops
description: Build the operating system behind revenue: pipeline, forecasting, quotas, compensation, CRM hygiene, and handoffs. Use when asked about sales ops, rev ops, quota setting, commission plans, forecasting, or why revenue is unpredictable.
metadata:
  version: 1.0.0
---

# Revenue operations

The plumbing that makes revenue predictable. Premature at 5 customers; the reason
growth stalls at 50.

## When you need this

Not before you have a repeatable motion. The founder should run the first 5-10
deals personally and **document the playbook**. Rev ops turns that documented
playbook into a system. Building the system before the playbook exists encodes
guesses as process.

## The pipeline math that matters

Work backward from the target, not forward from activity:

```
Revenue target / average deal size      = deals needed
Deals needed / close rate               = qualified opportunities needed
Opportunities / conversion from lead    = leads needed
Leads / channel conversion              = channel volume needed
```

Where this breaks in practice: people use aspirational conversion rates. Use your
actual ones, and if you do not have them, say so and mark the forecast as a guess.

**Coverage:** 3-4x pipeline against quota is the usual rule of thumb [A]. Below 3x,
one slipped deal misses the quarter.

## Forecasting honestly

The most common failure is a forecast built from rep optimism. Fixes:

- **Stage definitions tied to buyer actions, not seller activities.** "Demo
  completed" is a seller activity. "Buyer has confirmed budget and a decision date"
  is a buyer action. Only the second predicts anything.
- **A deal with no next meeting scheduled is not in the pipeline.** This one rule
  cleans most CRMs.
- Track **slip rate** — deals that move to next quarter — as its own metric. It is
  more predictive than close rate.
- Compare forecast to actual every period and publish the delta. Forecast accuracy
  is a skill that only improves when it is measured.

## Compensation

Comp is a strategy statement. People do what they are paid to do, exactly.

- **Simple enough to compute mentally.** If a rep cannot calculate their commission
  on a deal, the plan does not steer behavior.
- Pay on **what you want more of**. Paying on bookings gets bookings, including
  ones that churn. Paying on collected revenue or retained revenue gets healthier
  outcomes.
- **Uncapped for the top end.** Capping tells your best performer to stop in
  November.
- Accelerators above quota, not below.
- **Do not change plans mid-year** unless something is badly broken. Trust in the
  plan is worth more than the plan's precision.

## CRM hygiene

A CRM nobody trusts is worse than no CRM, because decisions get made on wrong data
with false confidence.

- Fewer required fields. Every mandatory field is a tax that produces garbage.
- Automate what can be automated; humans will not maintain what a system can.
- **One source of truth for revenue.** When finance and sales report different
  numbers, everything downstream is negotiable.

## Handoffs

Most revenue leaks at boundaries: marketing to sales, sales to onboarding,
onboarding to CS. For each, define explicitly: what triggers it, what information
transfers, who owns it after, and what the SLA is. Undefined handoffs are where
customers get dropped.

## Layering sales onto PLG

The mature model: PLG as top-of-funnel, sales as the closing motion for accounts
crossing a usage threshold. Slack, Notion, Figma, and Linear all converged here.

**Trigger to hire:** 10-20 accounts at $50k+ annually arriving through self-serve
expansion. Sequence: founder documents the playbook over 5-10 deals, hire one AE
who has closed similar deals, co-run for 90 days, then hand over. See
`skills/founder-led-sales`.

## Common failure

Buying tooling to fix a process problem. A new CRM does not create stage
definitions, and an AI forecasting tool trained on optimistic data produces
confident optimistic forecasts. Fix the definitions first; the tool is downstream.
