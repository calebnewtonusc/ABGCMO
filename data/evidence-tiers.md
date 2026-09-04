# Evidence tiers

Every number in this repo carries one of three tags. Carry the tag when you cite
the number.

| Tag | Definition | Trust |
|---|---|---|
| **[M] Measured** | Read directly from a primary artifact: published source code, a platform's own published figure, or a peer-reviewed paper. **Someone opened the actual thing.** | Cite as fact, with the source |
| **[P] Preprint** | A paper that exists and is checkable but has not cleared peer review | Cite with the caveat stated out loud |
| **[R] Reported** | Large-sample analysis by an organization with real access to the data (Buffer's 4.8M posts, AuthoredUp's 3M posts, GitHub's own research) | Cite with the source and the sample size |
| **[A] Asserted** | Repeated across marketing blogs with no traceable origin | Cite as "reported at roughly X," never as fact |

**A summary of a primary source is not the primary source.** A blog describing
open-sourced code is `[A]`, not `[M]`, no matter how confident it sounds. This
repo learned that the hard way; see the section at the bottom of this file.

## Why this matters more than it sounds

The growth-content ecosystem is dominated by companies selling growth software.
They publish numbers to rank for search terms. Those numbers get copied between
blogs until a figure with no origin reads like consensus.

Two live examples from this repo:

1. **"Show HN" is universally recommended.** The only controlled study
   (arXiv 2511.04453, n=138, single-author preprint) found **no effect** once you control for the fact
   that Show HN posts skew earlier-stage: beta = -119.2, SE = 138.3, p = 0.39.
   Every [A] guide says to use it. The one [M] source says it does not matter.

2. **LinkedIn comment weight** is quoted as "15x a like" in dozens of places.
   Sources actually range from 2x to 15x with no primary origin. Direction is
   solid; magnitude is invented.

## Rule

When [A] contradicts [M], [M] wins and you say so out loud. When you only have
[A], give a range and name it as unverified. Never manufacture precision.


## The trap this repo fell into, and the rule that came out of it

The first version of this repo tagged X's engagement weights `[M] Measured` on the
strength of a blog post that claimed to summarize the open-sourced algorithm. When
the actual repository was read on 2026-09-03, four things were wrong:

- Retweets were listed as 1x a like. The real ratio is 2x; the blog quoted the raw
  weight as if it were a ratio.
- Profile clicks were listed as 12x. The real ratio is 24x, same error.
- The largest positive weight in the entire model — `reply_engaged_by_author` at
  150x — was **absent from every secondary source consulted.**
- The blogs dated the open-sourcing to January 2026. The repository was last pushed
  2025-09-08 and the weights are dated April 5, 2023.

**Rule: a summary of a primary source is not the primary source.** `[M]` requires
that someone opened the actual artifact. If the citation is a blog describing a
paper or a repo, the tag is `[R]` at best, and usually `[A]`.

The arXiv Hacker News study cited throughout this repo is tagged **[P] Preprint**
for the same reason: it exists and is checkable (arXiv 2511.04453, Obada Kraishan,
submitted 2025-11-06), but it is a single-author preprint with n=138 that has not
cleared peer review. It is the best available evidence on that question and it is
still weaker evidence than the tag `[M]` would imply.
