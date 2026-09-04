# Open source and OSS-to-commercial

---

## OpenClaw — the fastest star chart in GitHub history, and the crash

**The rise.** 9,000 stars on launch day in late January 2026. **25,000 stars in a
single day** at peak. 60,000 by day three. 190,000 within two weeks. Two million
repository visitors in one week. It beat React's ten-year star record in sixty days.

**What actually drove it:**
- **Infrastructure, not demo.** Coverage focused on what it did in production.
  Developers were not starring out of curiosity; they were using it.
- **It met people where they already were.** Ran locally, connected to whatever
  model you pointed it at, and you talked to it through Signal, Telegram, Discord,
  WhatsApp — as if texting a capable assistant. No new interface to learn.
- **The ecosystem outran the core team.** Community skills for Stripe, Supabase,
  GitHub, Slack, Discord, HubSpot within two weeks; the registry went from a
  handful of official skills to 100+ community ones almost overnight.
- **Accidental FOMO.** Repeated rebrands left abandoned repos that squatters took
  over, generating security news, developer-Twitter memes, and a genuine
  "better star this before it changes names again" effect.
- Reportedly drove a surge in Mac mini sales as people rushed to self-host.

**The crash.** Within two weeks of going viral:
- **CVE-2026-25253**, a one-click RCE that could compromise any instance in
  milliseconds.
- **Over 135,000 instances exposed on the public internet**, many with no
  authentication at all.
- **ClawHavoc**: attackers flooded the official plugin registry with **1,184
  malicious skills — 20% of the entire marketplace.**

**Transferable, and this is the part people skip:** viral growth is a *load test*
on everything you did not build. The tool was built for capability first and
security roughly never, then deployed at enormous scale before anyone read the
architecture. If your growth plan works, the weakest part of your system becomes
your defining public story. Fix the registry, the auth defaults, and the
permission model **before** the launch, not after.

---

## obra/superpowers — the registry unlock

Jesse Vincent's composable skill system for Claude Code. ~30,000 stars by January
2026. **265,000+ by mid-2026**, with +19k in a single 30-day window.

The inflection was **acceptance into Anthropic's official Claude Code marketplace
on 15 January 2026.** Not a thread, not a launch — a listing.

It also was not a config dump. It was a *methodology*: composable skills that
force brainstorm → plan → TDD → review before ship. That framing is why it read
as infrastructure rather than as someone's dotfiles.

**Mechanics of the surrounding ecosystem:** 24,403 repos containing Claude Code
skill or plugin definitions by late June 2026.
`hesreallyhim/awesome-claude-code` (36.8k) is the canonical curated list;
`affaan-m/everything-claude-code` (141k) is the aggregator firehose.

Community marketplace submissions go through `clau.de/plugin-directory-submission`,
run `claude plugin validate` plus automated safety screening (malware, credential
harvesting, known bad actors), and get pinned to a commit SHA in
`anthropics/claude-plugins-community`. **Most common rejection cause: a
`plugin.json` version that disagrees with the CHANGELOG or git tags.**

**Transferable:** in any ecosystem with a curated registry, getting listed is
worth more than any amount of posting. Find the registry first.

---

## shadcn/ui — ownership as the product decision

Launched January 2023. **115,000+ stars in under three years**, #1 JavaScript
Rising Star in its launch year, past 100k stars in November.

Two mechanisms:
1. **Copy-paste, not install.** `npx` puts the component source in *your* repo.
   You own it and can change it. This inverted the entire component-library
   trade-off, which had always been "convenience for control."
2. **Then AI compounded it.** Codegen tools trained on huge volumes of shadcn
   content and adopted it as their default UI library. It is now a default in the
   Claude Code stack, Lovable, v0, and others. That is a distribution surface
   nobody could have planned for.

**Transferable:** the first mechanism was a design decision, not a marketing one.
The second was luck that the first made possible.

---

## Vercel / Next.js — the OSS-to-commercial flywheel

Build a best-in-class open-source tool (Next.js), build a passionate community
around it, then sell the best place to run it. The open-source project is the
top of funnel and the commercial product is the natural terminus.

Supabase runs the mirror image on the backend, and the two became a default pair.

---

## GitLab, MongoDB, HashiCorp, Docker — open core at scale

| Company | Model | Result |
|---|---|---|
| GitLab | Free unlimited users, $29/user Premium, custom Ultimate | ~$955M FY2026 revenue |
| MongoDB | OSS database, monetized via Atlas managed cloud | Cloud is >half of revenue |
| HashiCorp | Great OSS tool → hosted → enterprise features (SSO, policy, security) | Terraform 100M+ downloads; ~$14B at IPO |
| Docker | Containerization standard | Widespread enterprise adoption |

GitLab, Confluent, and MongoDB each passed $1B ARR only after many rounds of
pricing iteration. The pattern is consistent: **enterprises pay for the things
that remove operational and legal stress** — hosting, long-term support, SBOMs,
audit exports, migration help, security fixes — not for features.

**The license trap.** Elastic relicensed when AWS offered managed Elasticsearch;
Redis followed. If a cloud provider can resell your work as a service, decide
your license posture before you are big enough for it to matter.

**Timing:** commercialize once you have real adoption and a clear story about
what is free, what is paid, and why the paid layer deserves trust. Commercial
open source is under active pressure to prove that split is fair.
