# Method

How this repo was built, so you can judge whether to trust it.

## Research

Roughly 95 web searches across four domains (platform mechanics, growth tactics,
GTM playbooks, company case studies), plus a direct survey of the GitHub
ecosystem: repository searches for `marketing`, `growth`, `gtm`, `growth
hacking`, `go-to-market`, and `product management`, followed by reading the file
trees and doctrine files of the leading repos. That survey is in `LANDSCAPE.md`.

## Why evidence tiers exist

The growth-content ecosystem is dominated by companies selling growth software.
They publish numbers to rank for search terms, and those numbers get copied
between blogs until a figure with no origin reads like consensus.

Two live examples:

**"Show HN" is universally recommended.** The only controlled study
(arXiv 2511.04453, n=138 AI/LLM repos) found no significant effect once you
control for the fact that Show HN posts skew earlier-stage: β = −119.2,
SE = 138.3, p = 0.39. Dozens of `[A]` guides say to use it. The one `[M]` source
says it does not matter.

**LinkedIn comment weight** is quoted as "15x a like" across many sites. Sources
actually range from 2x to 15x with no traceable primary origin. The direction is
solid; the magnitude is invented.

So: `[M]` measured, `[R]` reported, `[A]` asserted. When they conflict, measured
wins and the skill says so out loud.

## Why cases are indexed by mechanism

Industry indexing produces bad matching. A student launching a dev tool on campus
does not need another dev-tool case; they need Tinder's sorority tour, because the
mechanism — solve the hard side in person, where the network already meets, with
the payoff visible in the room — is what transfers.

## The finding that shaped the doctrine

Reading 60+ cases, **almost nothing was won by posting more.** Every case turned
on a structural decision: how the thing was described, who was let in, what the
free tier metered, which registry listed it, or who was personally recruited.

Notion is the sharpest version. The product that nearly went bankrupt in 2015 and
the product that became a category leader in 2016 were **substantially the same
product**. What changed was the sentence describing it.

That is why `skills/growth-diagnosis` runs first and why the second rule in
`CLAUDE.md` is that structure beats content. A repo that answers growth questions
with content calendars would be repeating the mistake the evidence documents.

## Known limitations

- **Recency.** Platform mechanics go stale fast. Everything here is current as of
  2026-09-03. The X weights come from open-sourced code (Jan 2026, updated May)
  and are the most durable; the `[A]` reach and decay figures are the least.
- **Survivorship.** Every case is a winner. The projects that followed identical
  advice and stalled do not write blog posts. `data/benchmarks.md` carries
  failure rates alongside the success numbers, and the skills are written to say
  "this is normal" rather than "you did it wrong."
- **Western, English-language, and tech-heavy.** The case ledger reaches into
  nonprofits, movements, and church multiplication, but the center of gravity is
  US software.
- **Single-author synthesis.** Not peer reviewed. Corrections welcome, and a
  better source for an existing number is the most valuable contribution
  available.
