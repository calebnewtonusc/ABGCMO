# Launch day checklist

## T-14: the things that actually predict outcome

The HN study's predictors, in order, are HN score, existing stars, posting hour,
and documentation quality. Three of four are fixed before you post.

- [ ] README ≤ ~150 lines
- [ ] One-sentence category line, first screenful
- [ ] Demo GIF, 2-5 MB (10 MB hard ceiling)
- [ ] Quick start in first 200 words, works on a clean machine first try
- [ ] Four functional badges, not fifteen
- [ ] Detail moved to `docs/`
- [ ] LICENSE present
- [ ] Repo topics set
- [ ] Description + homepage fields filled
- [ ] Five-second test passed by someone who has not seen it

## T-14: the load test nobody runs

Viral growth is a load test on everything you did not build. OpenClaw hit 190k
stars and 135,000 exposed instances in the same fortnight.

- [ ] Auth defaults are safe if 10,000 people install it today
- [ ] No secrets in git history (`git log -p | grep -iE 'key|token|secret'`)
- [ ] Permission model reviewed
- [ ] If you have a plugin/extension surface, submissions are screened
- [ ] Someone else has installed it from scratch, successfully

## T-7: compounding placements (no timing component, just do them)

- [ ] Official registry / marketplace submission
- [ ] Awesome-list PRs (one per relevant list)
- [ ] Docs pages for every error string the product emits
- [ ] Profile README, 6 pinned repos

## T-1

- [ ] Copy drafted for all channels
- [ ] Calendar cleared for the full day
- [ ] Notifications on

## Launch day — ONE day, all channels

| Time (UTC) | Channel | Note |
|---|---|---|
| 12:00-17:00, Tue-Thu | Hacker News | Plain title: "X: a Y that does Z". Point at the repo. Skip the Show HN agonizing — no measured effect. |
| Same morning | Reddit | Framed as a lesson. No link in title. Only where you have history. |
| Same day | X | The finding, not the announcement. Link in first self-reply. |
| Tue-Thu 10-12 local, or Wed 16:00 | LinkedIn | Narrative. No link in body, and not in the first comment either. |
| 00:01 PT | Product Hunt | Only if consumer-ish and demoable. |

## First hour
- [ ] Answer every comment. The thread is the distribution.
- [ ] Do not argue. Thank critics and fix what is fair.

## First 24 hours
- [ ] Keep answering. Half-life is ~24 h.
- [ ] Screenshot Insights → Traffic before it rolls off

## Week 1
- [ ] Record which referrer actually sent stars — the only honest attribution
- [ ] Ship a release. Weekly releases convert a spike into a baseline.
- [ ] Write the stopping rule result down and compare
