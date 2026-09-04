# Failures

Every other file in this ledger is a survivor. This one is the correction.

The projects that followed identical advice and stalled do not write blog posts,
so the sample everyone learns from is the winners. These are documented cases
where a real growth mechanic **did not work, stopped working, or actively caused
harm** — including inside companies that succeeded overall.

---

## Notion, 2013-2015 — the packaging failure that nearly killed it

Same founders, same vision, same core technology as the version that later reached
100M+ users. It nearly went bankrupt.

Ivan Zhao described it as *"collaborative building apps, kind of like document
editing, and kind of like Xcode for the web."* Nobody understood it and nobody
needed it. By mid-2015 the product was buggy and the money nearly gone. He laid
off everyone except his cofounder, borrowed **$150k from his mother**, and moved
to Kyoto.

**What failed:** not the product. The frame. Zhao's own diagnosis was that "most
people just want an off-the-shelf thing that solves their problem really quickly.
Tool makers are rare in the world."

**Transferable:** a product can be correct and still fail entirely on the sentence
describing it. Before concluding the product is wrong, check whether the category
is.

---

## Figma's closed beta — a growth tactic they publicly regretted

Figma launched as a closed beta with a waitlist. It worked as scarcity. The team
later said they **would have preferred an open beta**, because gating slowed
feedback velocity at exactly the stage when learning rate matters most.

**Transferable:** waitlists trade learning speed for perceived scarcity. Superhuman
made that trade correctly, because they needed positioning and network control.
Figma needed learning. **Same tactic, opposite verdict, and the variable is which
one you need.**

---

## Glossier — community-led growth has a ceiling

Community-led growth built a billion-dollar brand. Then it stopped.

Once Glossier had converted most of its natural audience from the Into The Gloss
blog and its Instagram following, **organic growth plateaued**. The transition to
paid acquisition afterward was genuinely hard, because the paid channel does not
carry the trust the community did.

**Transferable:** community-led growth is capped by the size of the community.
Model that ceiling before you hit it, and start building the next motion while the
first one still works.

---

## OpenClaw — winning the load test and failing it

9,000 stars on launch day, 25,000 in a single day at peak, 190,000 within two
weeks, beating React's ten-year GitHub record in sixty days.

Within the same two weeks:
- **CVE-2026-25253**, a one-click RCE compromising any instance in milliseconds
- **135,000+ instances exposed on the public internet**, many with no auth at all
- **ClawHavoc**: 1,184 malicious "skills" flooded into the official plugin
  registry — **20% of the entire marketplace**

**What failed:** the growth worked perfectly. Everything the growth loaded did not.
Built for capability first and security roughly never, then deployed at enormous
scale before anyone read the architecture.

**Transferable:** viral growth is a load test on every system you did not build.
If your growth plan works, the weakest part of your stack becomes your defining
public story. Fix defaults, auth, and any third-party submission surface *before*
the launch.

---

## Midjourney — absorbed by the platform

A top-10 staple on a16z's consumer AI rankings for years. **Fell to #46** once
ChatGPT and Gemini integrated high-quality image generation directly into chat.

Nothing Midjourney did got worse. The category moved underneath it.

**Transferable:** if your product is one capability, it is a feature waiting to be
absorbed. Survivors either go deep enough that absorption is uneconomical
(ElevenLabs on voice cloning and dubbing) or own a workflow rather than a
capability. This is the defining strategic risk of the current era.

---

## Crypto airdrops — incentives that bought the wrong users

The first wave of blanket airdrops and yield farming created **armies of mercenary
farmers** who sold immediately. Protocols saw TVL cliffs the moment incentives
ended, and tokens collapsed. One analysis put the failure rate at **88%**, with
high FDV named the single most damaging factor.

**What failed:** the campaigns hit every activity metric they set. Participant
counts were enormous. The users were worthless.

**Transferable:** any incentive that can be gamed will be, and the users an
exploitable incentive attracts are precisely the ones you least want. **Measure
post-campaign retention, never participant count.** The later, better designs used
Sybil resistance, engagement weighting, vesting, and retroactive rewards for
genuine use.

---

## Product Hunt as a whole-launch bet

Outside the top 10, expect **under 500 visitors**. Even top-3 traffic drops
**80-90% within 72 hours**, and B2B conversion runs ~1-2%.

Meanwhile founders stacking 4-5 smaller focused directories report **14-23%
conversion versus Product Hunt's ~3.1%**.

**Transferable:** the platform everyone optimizes for is outperformed by the
unglamorous directories nobody talks about. Launching there is fine. Betting the
launch on one day there is a lottery.

---

## "Show HN" — the advice everyone gives that the data does not support

Every launch guide recommends the tag. The only controlled study
([arXiv 2511.04453](https://arxiv.org/abs/2511.04453), n=138, preprint) found **no
statistical advantage** after controlling for confounds: β = −119.2, SE = 138.3,
**p = 0.39**.

**Transferable:** this is what a widely repeated claim with no measurement behind
it looks like. It survived because it is plausible, free to repeat, and nobody
checked. Assume there are others.

---

## Buying stars — a market with 6 million units sold and a legal ceiling

Peer-reviewed evidence (He et al., *Six Million (Suspected) Fake Stars on GitHub*,
ICSE 2026): ~**6 million suspected fake stars across 18,617 repositories** from
~301,000 accounts, found by scanning 20 TB of GitHub metadata.

GitHub deleted **90.42%** of flagged repositories. The FTC Consumer Review Rule
(effective 2024-10-21) prohibits buying fake indicators of social media influence,
with penalties to **$53,088 per violation**.

**Transferable:** the tactic is detectable, it is illegal in the US, and it
destroys your own attribution permanently. Every repository in that dataset
believed it would not be caught.

---

## This repo, one day after shipping

Documented in full in [AUDIT.md](../AUDIT.md). **189 defects, eleven severity-1.**

The flagship `[M] Measured` claim — X's engagement weights — had been taken from a
blog *describing* the open-sourced algorithm rather than from the algorithm. Three
weights were wrong, the largest positive signal in the model was missing entirely,
and the provenance story ("open-sourced January 2026") was false.

**Transferable, and the reason this section exists:** the repo that exists to
argue for evidence quality got its own headline evidence wrong, in exactly the way
it warns others about. **A summary of a primary source is not the primary source.**
Assume this failure is present in your own work until you have opened the artifact
yourself.
