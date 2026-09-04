# Finding the aha moment

An aha moment is a **countable event** that predicts retention. "The user
understands the value" is not an aha moment; it is a hope.

## Known examples

| Product | Aha moment |
|---|---|
| Slack | 2,000 team messages sent |
| Dropbox | First file in a shared folder |
| Notion | Second page created |
| Facebook | 7 friends in 10 days |

Note all four are specific, numeric, and reachable in one or a few sessions.

## The method

1. **Split users** into retained (still active at day 30) and churned.
2. **List every meaningful action** available in the first session.
3. For each action, compute: `% of retained who did it` vs `% of churned who did it`.
4. **The largest gap is your candidate.** Look for actions where retained users
   are 3x+ more likely.
5. **Find the threshold.** Not "invited a teammate" but "invited 2+ teammates."
   Sweep the number and find where the retention curve bends.
6. **Validate causally.** Correlation is not enough. Run an experiment that pushes
   users toward the action and check whether retention actually moves.

| Action | % retained did it | % churned did it | Gap |
|---|---|---|---|
| | | | |

## Then shorten the path to it

Time to value is the control knob. Median is ~36 h; delivering the aha within
5 minutes is associated with **+40% 30-day retention** versus 15+ minutes.

- [ ] Count the steps between signup and the aha action
- [ ] Delete every step not strictly required (Dropbox cut signup to email +
      password and lifted conversion 40%+)
- [ ] Pre-fill, pre-populate, or provide sample data so the empty state is not
      the first thing they see
- [ ] Do the setup for them where you can — the Collison installation applies to
      onboarding too
- [ ] **Measure time to value, not onboarding completion.** A user who finishes
      your tour and gets nothing has completed onboarding and failed activation.

## Warning

If no action separates retained from churned users, you may not have
product-market fit rather than an onboarding problem. Run the Sean Ellis test:
40% "very disappointed" is the threshold. Below it, segment to the users who love
it most and find out what is different about them. That is product work, and
calling it correctly saves months.
