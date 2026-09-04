---
name: growth-diagnosis
description: Diagnose what is actually blocking growth before recommending any tactic. Use FIRST whenever someone asks how to grow, get users, get traction, go viral, or market something, and whenever a growth effort is not working. Routes to the right specialist skill.
metadata:
  version: 1.1.0
---

# Growth diagnosis

This runs before any other growth skill. Prescribing without diagnosing is the
single most common failure, because the same tactic is correct at one stage and
actively harmful at another.

## Step 1: Establish stage

| Stage | Test | What growth work is appropriate |
|---|---|---|
| Pre-product | Nothing shipped | Talk to people. No growth work exists yet. |
| Pre-PMF | Shipped, users leave | **Retention and positioning only.** Acquisition here accelerates churn. |
| Post-PMF | Users stay, growth is slow | Now channels matter. This is where most advice assumes you are. |
| Scaling | A channel works | Depth in that channel, plus a second one. |

**Sean Ellis test to place them:** ask users "how would you feel if you could no
longer use this?" 40% "very disappointed" is the PMF threshold. Below that, do
not run acquisition. Segment to the users who love it most and find out why
(see Superhuman in `cases/plg-saas.md`).

## Step 2: Find the binding constraint

Only one of these is usually binding. Work on the others and nothing happens.

| Constraint | Symptom | Where to go |
|---|---|---|
| **Awareness** | Almost no traffic at all | Channel selection: `skills/launch-day`, platform skills |
| **Comprehension** | Traffic arrives, bounces immediately | `skills/positioning` — they do not understand what it is |
| **Conversion** | They understand, do not sign up | `skills/positioning`, landing page benchmarks in `data/benchmarks.md` |
| **Activation** | Sign up, never reach value | `skills/activation-retention` |
| **Retention** | Reach value, leave anyway | `skills/activation-retention`, and possibly back to PMF |
| **Referral** | Stay, tell nobody | `skills/growth-loops` — is there even a share surface? |

**Diagnostic question that cuts fastest:** "Of the people who have used this, how
many still use it, and what do the ones who stayed have in common?" If nobody
stayed, no channel will help.

## Step 3: Name the hard side

In any network there is a side that is harder to acquire and that the other side
follows. Creators before viewers. Sellers before buyers. Contributors before
users. Drivers before riders.

Get this wrong and every priority after it is wrong.

## Step 4: Get the honest baseline

Current numbers. Actual ones, not aspirations. Then check them against
`data/benchmarks.md` before calling anything a problem — most numbers people are
worried about are normal, and most people expect outcomes that only survivors got.

## Step 5: Check channel-product fit

Read the spread-mechanism table in `data/channel-economics.md`. If the product has
no multiplayer surface and produces no shareable artifact, **it will not go
viral** and you should say so directly rather than designing referral mechanics
for it.

## Output shape

1. Stage, with the evidence that placed it there
2. The binding constraint, and why it and not the others
3. The single highest-leverage action
4. What to expect and by when
5. **A stopping rule:** what result by what date would mean this is wrong

Never output a list of nine channels. That is a non-answer that offloads the
decision back onto the person who asked.
