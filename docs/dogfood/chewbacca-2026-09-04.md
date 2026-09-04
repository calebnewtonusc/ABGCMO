# Dogfood: `/growth-audit` on Chewbacca

Run 2026-09-04 against real GitHub API data, not estimates. Published including
the parts that make the author look bad, because a growth repo whose own projects
have four stars has a credibility problem it can only fix with evidence.

**Target:** [calebnewtonusc/Chewbacca](https://github.com/calebnewtonusc/Chewbacca) —
a Claude Code setup kit. Public since 2026-03-21.

---

## Baseline (GitHub API, 2026-09-04)

| | Value | Read |
|---|---|---|
| Stars | 4 | All four are people who know the author |
| Forks | 0 | |
| Watchers | 0 | |
| **Clones, 14d** | **122** | |
| **Unique cloners, 14d** | **42** | |
| Views, 14d | 8 | |
| Unique viewers, 14d | 2 | |
| Referrers | github.com only | No external traffic at all |
| README | 1,034 lines | |
| Images in README | **0** | |
| Releases | 0 | |
| Topics | 14 | Set during a prior session |
| License | MIT | |
| In Claude Code marketplace | **No** | |

## The anomaly worth naming first

**42 unique cloners against 2 unique viewers.** That ratio is backwards from every
normal repo, where views vastly exceed clones.

Two candidate explanations:
1. **Automated traffic** — CI, mirrors, or the author's own machines inflating it.
2. **People are cloning without ever seeing the repo page**, because the install
   command reaches them somewhere else.

Either way the honest read is the same: **the star count is not measuring what is
happening.** Four stars would suggest a dead project. 42 unique cloners in two
weeks would not.

This is `skills/github-growth`'s own argument, confirmed against its author's repo:
stars are a lagging popularity snapshot; **forks, clones, and returning
contributors** are the real signal. If Chewbacca had been optimized for stars,
none of this would have been visible.

## Stage and constraint

**Stage:** post-launch, pre-traction. Something exists and a small number of
people use it.

**Binding constraint: awareness.** Not comprehension, conversion, or retention.
- Zero external referrers. Nobody outside GitHub has ever linked to it.
- 2 unique viewers in 14 days. Nobody is finding the page.
- But clones happen anyway, which suggests that when people *do* reach it, they act.

Traffic that converts to clones at this ratio is not a conversion problem. It is
a distribution problem, and there is currently no distribution.

## What the repo's own skills say to do, in order

**1. Get into the Claude Code marketplace.** Not done. This is the single largest
documented unlock in this ecosystem: obra/superpowers went ~30k → 265k+ stars, and
the inflection was **marketplace acceptance on 15 January 2026**, not a campaign.
Submission runs through `clau.de/plugin-directory-submission`; the most common
rejection is a `plugin.json` version disagreeing with the CHANGELOG or git tags.
→ `skills/marketplace-listings`

**2. Cut the README and add a demo.** 1,034 lines with **zero images**. The star
decision happens in roughly 15 seconds in the first screenful, and the repo's own
`skills/github-growth/references/readme-template.md` calls a table of contents
where the demo should be "the single most common mistake." Chewbacca is committing
it at 1,034 lines.

Worth noting: it got *longer* since the last audit flagged it. Documentation grows
by default; conversion surface has to be defended deliberately.

**3. Ship a release.** Zero releases. Weekly releases signal an active project and
are what convert a launch spike into a baseline.

**4. Awesome-list PRs.** `hesreallyhim/awesome-claude-code` (36.8k),
`affaan-m/everything-claude-code` (141k). Two PRs, permanent, compounding.

**5. Only then, a concentrated launch day.** HN in the 12:00-17:00 UTC window
Tue-Thu, everything else the same day. Trending ranks velocity, so a spread launch
is arithmetically close to no launch.

## What NOT to do, per `skills/growth-diagnosis`

Do not write more documentation. 1,034 lines is already past the point where more
words help, and adding to it is the comfortable move that feels like progress.

Do not post about it before steps 1-3. A launch that lands people on a 1,034-line
README with no demo wastes the one concentrated shot the velocity ranking gives you.

## Stopping rule

**If marketplace listing + README cut + one release produce fewer than 25 stars in
30 days, the positioning is wrong, not the distribution.** At that point the
problem is that "my Claude Code kit" is the most crowded description in the
ecosystem, and the fix is repositioning around the macOS control layer — the part
almost no competing kit has.

Re-measure: stars, **unique cloners**, and external referrers. Not views.

## What this audit cost

About four minutes of API calls. No survey, no analytics tool, no estimates. The
`gh` commands are in `skills/competitive-intelligence` and
`skills/github-growth`, and they work on any public repo including a competitor's.

## Honest caveat

This is one audit, by the tool's author, on the author's own repo. It is a
demonstration of the method, not evidence that the method works. That requires
following the recommendations and reporting what happened, which has not been done
yet and will be appended here when it is.
