# Benchmarks

What "good" looks like. Use these to tell someone whether their number is a
problem or normal. Tags per `evidence-tiers.md`.

**All figures verified 2026-09-04.** Half-life for benchmark data is roughly 12
months; platform mechanics rot faster. See `VERIFIED.md`.

## Where these come from

| Section | Primary source | Sample | Tag |
|---|---|---|---|
| Conversion, freemium, trials | [acceleroi PLG benchmarks](https://www.acceleroi.com/blog/benchmarks/saas-plg-free-to-paid-conversion-rate), [Flowjam PLG](https://www.flowjam.com/blog/product-led-growth-playbook-2025-no-fluff-guide-for-saas) | Vendor aggregates, sample not disclosed | [R] |
| Landing pages | [Unbounce](https://unbounce.com/conversion-benchmark-report/) via [LanderLab](https://landerlab.io/blog/landing-page-conversion-rate) | 464M visits, 41k pages | [R] |
| Retention and churn | [Koji](https://www.koji.so/blog/saas-churn-rate-benchmarks-2026), [ever-help](https://www.ever-help.com/blog/saas-retention-rate-benchmarks) | Vendor aggregates | [R] |
| Activation and time-to-value | [Userpilot](https://userpilot.com/blog/aha-moment/), [Amplitude](https://amplitude.com/blog/time-to-value-drives-user-retention) | Product-analytics vendors | [A] |
| Virality / K-factor | [LaunchList](https://getlaunchlist.com/blog/viral-coefficient-k-factor-guide), [Sam Shev](https://www.samshev.com/blog/math-behind-virality-k-factor-cycle-time) | Formula is definitional; benchmarks asserted | [A] |
| Cold email | [Instantly 2026 Benchmark Report](https://instantly.ai/cold-email-benchmark-report-2026), [Amplemarket](https://www.amplemarket.com/blog/cold-email-benchmarks) | Platform-wide send data | [R] |
| Paid acquisition | [Lighter Capital](https://www.lightercapital.com/blog/cac-payback-period), [culta CAC benchmarks](https://culta.ai/blog/cac-benchmarks-startups-2026) | Vendor aggregates | [R] |
| Product-market fit | [Reforge / Sean Ellis 40% test](https://www.reforge.com/guides/measure-and-improve-product-market-fit), [First Round on Superhuman](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/) | ~100 startups (Ellis) | [R] |
| Realistic outcomes | Indie-founder surveys, no primary data | Unknown | [A] |

**Caveat that applies to every `[R]` row here:** these are vendor benchmark
reports. The companies publishing them sell software to the market they are
measuring, and none disclose full methodology. They are the best available and
they are not peer-reviewed. Segment-level variance is large and mostly unreported
— a "median" across all B2B SaaS describes very few actual companies.

---

## Conversion and monetization

| Metric | Range | Note | Tag |
|---|---|---|---|
| Freemium free-to-paid | 2-8%, median 4.5% | Broad tools 1-5%; tightly targeted 5-15% | [R] |
| Opt-out trial w/ credit card | 35-55%, median 44% | Friction is the filter | [R] |
| Activation rate | ~37.5% | **Predicts revenue better than any other PLG metric** | [R] |
| Time to value | ~36 h median | The clock activation runs against | [R] |
| Net revenue retention | 110-130% top performers | SMB-focused median 100-105% | [R] |
| PQL conversion, top performers | 20-30% | | [R] |
| Landing page conversion, all industries | median 4.3% | Unbounce reports 6.6% for dedicated LPs | [R] |
| Landing page, SaaS free trial | ~7.2% | | [R] |
| Landing page, ecommerce | ~3.1% | | [R] |
| Mobile LP conversion | ~58% of desktop rate | 2.8% vs 4.8% | [R] |
| LP copy at 5th-7th grade reading level | 11.1% vs 5.3% for college-level | Nearly 2x | [A] |

## Retention and churn

| Metric | Healthy | Tag |
|---|---|---|
| Monthly logo churn, enterprise | <0.5% | [R] |
| Monthly logo churn, mid-market | 0.5-1.5% | [R] |
| Monthly logo churn, SMB/prosumer | 2-4% | [R] |
| Monthly churn, consumer subscription | many brands lose 5-10% | [R] |
| Revenue churn, best in class | <1% | [R] |
| **Share of annual churn in first 90 days** | **60-70%** | [A] |

The last row is the most actionable number in this file. If most churn happens
in the first 90 days, onboarding is the retention lever, not win-back campaigns.

Later cohorts should outperform earlier ones. If your July cohort retains better
at month 6 than your January cohort did, the product and ICP targeting are
improving. Blended churn hides this completely.

## Activation

| Finding | Tag |
|---|---|
| Products delivering the aha moment within 5 min show **+40% 30-day retention** vs. 15+ min | [A] |
| Teams measuring time-to-value instead of completion rate see 15-25% higher trial-to-paid | [A] |
| Scientifically identifying the aha moment: 2-3x activation improvement within 90 days | [A] |

Known aha moments: Slack at 2,000 team messages. Dropbox at first shared folder.
Notion at second page created. Facebook's was 7 friends in 10 days.

## Virality

`K = i x c` where `i` = invites per user, `c` = invite conversion rate.

| Value | Meaning | Tag |
|---|---|---|
| K > 1 | Self-sustaining viral growth. **Rare and usually temporary.** | [A] |
| K = 1 | Linear | [A] |
| K = 0.3-0.7 | Where healthy products actually land; still compounds meaningfully | [A] |
| Dropbox's reported K | ~0.35 | [A] |

**Cycle time matters as much as K.** A 3-day loop at K=0.4 outgrows a 30-day
loop at K=0.5. Shortening the loop is usually easier than raising K.

Double-sided incentives reported to convert up to 3x better than single-sided. [A]

## Sales

| Metric | Value | Tag |
|---|---|---|
| Warm introduction conversion | 30-50% | [A] |
| Cold outreach conversion | 2-5% | [A] |
| Cold email reply rate, average | 3.43% | [R] |
| Cold email reply, top decile | 8-12% | [R] |
| Cold email referencing a specific buying signal | 15-25% | [A] |
| Sales requiring 5+ follow-ups | 80% (most founders stop at 2) | [A] |
| Replies generated by step one of a sequence | 58% (so 42% come from follow-ups) | [R] |
| Optimal cold email length | 50-125 words | [R] |
| Safe send volume per mailbox/day | 50-100 | [R] |
| Acceptable bounce rate | <3%; best in class <1.5% | [R] |
| Spam complaint ceiling | <0.1% | [R] |
| Domain warmup before scaling | ~3 weeks | [R] |
| First outreach to first paying customer | 4-8 weeks | [A] |

**Deliverability, not copy, sets the ceiling.** A large gap between raw sends and
replies is a deliverability problem; rewriting the email will not fix it.

## Paid acquisition

| Metric | Target | Tag |
|---|---|---|
| CAC payback period | <12 months; <6 ideal for DTC | [R] |
| Early-stage CAC payback | ~4.8 months (early adopters convert easily) | [R] |
| Test budget to get signal | 300-500 EUR across 2-3 creatives | [A] |

Paid amplifies what already works. Running ads before organic traction buys
expensive proof that the message is wrong. For early stage use payback period,
not LTV/CAC — LTV is a guess before you have retention data.

## Realistic outcomes

| Expectation | Value | Tag |
|---|---|---|
| Solo builder, year-one audience | 500-2,000 followers | [A] |
| Useful repo, active promotion, to 1k stars | 1-3 months | [A] |
| Same repo, no promotion | 6-12 months | [A] |
| Solo SaaS never reaching $1k MRR | ~30% | [A] |
| Repos above 10k stars | top 0.1% | [R] |

**Survivorship warning.** Every case study is a survivor. The projects that
followed identical advice and stalled at 40 stars do not write blog posts. When
someone's numbers are below these, the honest read is usually "this is normal,"
not "you did it wrong."

## Product-market fit

The Sean Ellis test: ask users "how would you feel if you could no longer use
this?" **40% answering "very disappointed"** is the threshold. Below 40%,
companies almost always struggled to grow; above it, they almost always had
traction. Benchmarked across ~100 startups. [R]

Superhuman's use of it (Rahul Vohra): started at 22%, segmented down to the
users who loved it most to find the signal, reached 33%, then nearly doubled to
58% within three quarters of focused work. The method is the contribution: the
score is not a grade, it is a segmentation instrument. [R]
