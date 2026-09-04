# Evidence tiers

Every number in this repo carries one of three tags. Carry the tag when you cite
the number.

| Tag | Definition | Trust |
|---|---|---|
| **[M] Measured** | Peer-reviewed paper, open-sourced code, or a figure the platform itself published | Cite as fact |
| **[R] Reported** | Large-sample analysis by an organization with real access to the data (Buffer's 4.8M posts, AuthoredUp's 3M posts, GitHub's own research) | Cite with the source and sample |
| **[A] Asserted** | Repeated across marketing blogs with no traceable origin | Cite as "reported at roughly X," never as fact |

## Why this matters more than it sounds

The growth-content ecosystem is dominated by companies selling growth software.
They publish numbers to rank for search terms. Those numbers get copied between
blogs until a figure with no origin reads like consensus.

Two live examples from this repo:

1. **"Show HN" is universally recommended.** The only controlled study
   (arXiv 2511.04453, n=138) found **no effect** once you control for the fact
   that Show HN posts skew earlier-stage: beta = -119.2, SE = 138.3, p = 0.39.
   Every [A] guide says to use it. The one [M] source says it does not matter.

2. **LinkedIn comment weight** is quoted as "15x a like" in dozens of places.
   Sources actually range from 2x to 15x with no primary origin. Direction is
   solid; magnitude is invented.

## Rule

When [A] contradicts [M], [M] wins and you say so out loud. When you only have
[A], give a range and name it as unverified. Never manufacture precision.
