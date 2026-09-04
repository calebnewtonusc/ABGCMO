---
name: lifecycle-messaging
description: Email, SMS, push, and in-product messaging that keeps users rather than annoying them. Use when asked about onboarding emails, drip campaigns, newsletters to existing users, push notifications, win-back, or lifecycle marketing.
metadata:
  version: 1.0.0
---

# Lifecycle messaging

Messaging to people who already signed up. Different discipline from cold outreach
(`skills/founder-led-sales`) and from audience building (`skills/newsletter-growth`).

## Where the leverage actually is

**60-70% of annual churn happens in the first 90 days** [A]. So the onboarding
sequence is worth more than every other lifecycle message combined, and win-back
campaigns operate on the smaller half of the problem.

If you are building lifecycle messaging and starting with win-back, you are
starting at the wrong end.

## The onboarding sequence

Every message should push toward the **aha moment** — the countable event that
predicts retention (Slack: 2,000 team messages; Dropbox: first shared folder;
Notion: second page created). See `skills/activation-retention`.

| When | Message | Job |
|---|---|---|
| Immediately | Welcome + **the single next action** | Not a feature tour. One action. |
| Day 1, if not activated | The specific blocker they hit | Requires knowing where they stopped |
| Day 3 | The use case closest to why they signed up | Personalize on signup source |
| Day 7 | Social proof from their segment | Someone like them succeeded |
| Day 14, if inactive | A human asking what went wrong | Highest-information message you will send |

**Behavior-triggered beats time-based.** A message sent because someone got stuck
converts far better than one sent because it is Tuesday.

## Push notifications

The most easily abused channel. One bad push gets the whole app muted, permanently,
and you cannot get that permission back.

- Ask for permission **after** delivering value, never on first launch
- Every push must be **about the user**, not about you. "Sarah replied to you" is
  a push. "Check out our new feature" is a mute.
- Duolingo's streak reminders work because the daily action is genuinely small. A
  streak on a demanding action produces guilt and then abandonment.
- Set a frequency cap and honor it

## SMS

Highest open rate, lowest tolerance, and legally regulated. Explicit opt-in is
required in most jurisdictions. Reserve for genuinely time-sensitive and
genuinely wanted: delivery, security, an appointment. Marketing SMS burns the
channel fast.

## Streaks and habit

Duolingo's streak is the cheapest retention mechanic that exists. The longer it
runs the higher the psychological cost of breaking it. They also learned to market
**streak revival**, because the alternative to giving people a way back is losing
them permanently after one missed day.

Only works when the daily action is small. Test: could someone do it while
waiting in line?

## Measurement

Track **downstream behavior, not opens**. Open rate is corrupted by privacy
protections that pre-fetch images. The real question is whether people who got the
message activated, retained, or converted at a higher rate than a holdout.

**Always keep a holdout group.** Without one you cannot tell whether the sequence
helped or whether those users would have activated anyway. Most lifecycle programs
have never been tested against doing nothing.

## Common failure

Sending more messages when metrics dip. Volume is the easiest lever and the one
that most reliably makes things worse, because unsubscribes and mutes are
permanent while a dip is usually temporary.
