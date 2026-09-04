# AI-native companies

---

## ChatGPT

Fastest product ever to 100M weekly actives. Passed **1 billion weekly actives in
August 2026**. The relevant lesson for anyone else is not replicable scale but the
**interface decision**: a chat box required no instruction manual, so the entire
onboarding cost was zero. Time-to-value was measured in seconds.

---

## The consolidation warning

Midjourney was a top-10 staple for years and **fell to #46** on a16z's consumer
AI rankings once ChatGPT and Gemini integrated high-quality image generation
directly into chat.

**Transferable, and it is the defining strategic risk of this era:** if your
product is one capability, it is a feature waiting to be absorbed by a platform.
Survivors either go deep enough that absorption is uneconomical (ElevenLabs on
voice cloning and dubbing) or own a workflow rather than a capability.

ElevenLabs has appeared on every edition of that ranking since September 2023
precisely because its capabilities are specialized enough not to be replicated as
a checkbox.

---

## Cursor

See `developer-tools.md`. The compressed version: $100M ARR in 20 months with no
marketing spend, free tier as funnel, and a deliberate refusal to chase enterprise
early. Now ~$4B revenue run rate.

---

## OpenClaw

See `open-source.md` for the full rise-and-crash. The AI-specific lesson: the
product met people inside the messaging apps they already used rather than asking
them to adopt a new interface, and the community shipped an integration ecosystem
faster than the core team could have.

And then the security crisis, which is the AI-native cautionary tale: agentic
software with broad system permissions, community-built extensions, and minimal
default security controls, deployed at scale before anyone audited it.

---

## What actually differentiates in the AI era

The commodity is the model. What is not commodity:

1. **Distribution.** Cursor won on developer word of mouth, not model quality.
2. **Workflow ownership.** A capability gets absorbed; a workflow does not.
3. **Data and feedback loops.** Mercor encoded matching signals discovered
   manually — like the finding that candidates who studied abroad in Western
   countries worked better with US companies — into a model competitors did not
   have the data to build.
4. **Trust and safety posture.** After ClawHavoc this became a buying criterion,
   not a compliance chore.

---

## Sources

- ChatGPT fastest to 100M WAU; 900M WAU, passing 1B Aug-2026 — [a16z Top 100 Gen AI Consumer Apps](https://a16z.com/100-gen-ai-apps-6/), [Instant Press AI statistics](https://www.instantpress.co/ai-statistics)
- Midjourney falling from a top-10 staple to #46 as ChatGPT and Gemini integrated image generation — [a16z, 6th edition](https://a16z.com/100-gen-ai-apps-6/)
- ElevenLabs on every edition since Sept 2023 on specialization — [a16z](https://a16z.com/100-gen-ai-apps-6/)
- Gemini at ~34% of ChatGPT's web scale, 40% mobile — [a16z](https://a16z.com/100-gen-ai-apps-6/)
- Cursor figures — see `developer-tools.md` sources
- OpenClaw figures — see `open-source.md` sources
- Mercor encoding the study-abroad matching signal — [VectorShift interview](https://vectorshift.ai/blog)

**Tier note.** a16z's rankings are `[R]`: a large-sample analysis by an
organization with real data access, published to support their own investment
thesis. Directionally strong, and not disinterested.
