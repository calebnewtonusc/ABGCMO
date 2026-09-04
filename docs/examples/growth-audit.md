# Example: `/growth-audit`

What the command actually produces. Real shape, illustrative numbers.

---

**Input:** `/growth-audit my SaaS — 2,000 signups in 3 months, 40 still active,
~800 visits/month, no paid spend`

---

## Baseline

| | Value | Benchmark | Verdict |
|---|---|---|---|
| Signups | 2,000 | — | — |
| Active at 30d | 40 | — | **2% retention** |
| Monthly churn (implied) | ~50%+ | 2-4% SMB/prosumer [R] | **12x worse than benchmark** |
| Traffic | 800/mo | — | Small but converting at 250% of typical, which is suspicious |

The traffic-to-signup ratio being *above* benchmark alongside 2% retention usually
means the signup is too easy and unqualified, not that marketing is working.

## Stage

**Pre-PMF.** 2% 30-day retention is not a growth problem, it is a product one.
The Sean Ellis threshold is 40% "very disappointed"; nothing at 2% retention
clears it.

## Binding constraint

**Retention.** Not awareness.

The other five are not binding: traffic converts, people sign up, and people reach
the product. They leave after. Every acquisition dollar spent now buys a faster
leak, and the chart will look worse, not better.

## The single highest-leverage action

**Interview 10 of the 40 people who stayed and 10 who left, this week.**

Not a survey. Conversations. You are looking for one thing: what did the 40 do in
their first session that the 1,960 did not? That is your aha moment, and you cannot
find it from analytics at n=40.

Reference: `skills/activation-retention/references/aha-moment-worksheet.md`.

## What to expect

Two weeks to run, and the answer is usually surprising. The nonprofit case in
`cases/movements.md` found donors were not motivated by program statistics and
volunteers were not leaving because they were busy — neither was visible in any
dashboard.

## Stopping rule

**If 20 interviews produce no action that separates the two groups, the problem is
PMF, not onboarding.** At that point narrow to the segment the 40 belong to and
rebuild for them (Superhuman: 22% → 33% by segmenting alone), or reconsider the
product.

Re-measure 30-day retention on the cohort that signs up 60 days from now.

## Free things being skipped

- No `LICENSE` on the public repo — nobody at a company can legally use it
- No repo topics — invisible to GitHub search
- One-question "how did you hear about us?" at signup, which beats attribution
  tooling at this stage
