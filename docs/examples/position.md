# Example: `/position`

---

**Input:** `/position — a CLI that turns Figma files into React components`

---

## 1. Competitive alternatives

What would they do if this did not exist?

| Alternative | Who uses it | Why switch |
|---|---|---|
| **Hand-coding from the design** | Most teams | Slow, drifts from the design over time |
| Figma Dev Mode | Teams already in Figma | Gives specs, not components |
| Locofy / Anima | Teams that tried a tool | Output is often unusable, so they hand-code anyway |
| **Doing nothing — designers make specs, devs interpret** | The real default | Free, and everyone is used to the friction |

The last row is the actual competitor, and it is the one most positioning
exercises skip.

## 2. Unique attributes

- Runs in CI, so drift is caught on every PR
- Outputs to your existing component library rather than generating new primitives
- No plugin, no account, no browser step

## 3. Value only this delivers

**Design drift is caught automatically instead of discovered in review.** The
others generate code once; this one keeps code and design in agreement over time.

## 4. Who cares most

Not "frontend teams." → **Teams with a design system they already maintain, where
a designer and a developer have argued about drift in the last month.** The
trigger is a redesign or a component library migration.

## 5. Category

Entering an existing category as obviously-first for a segment, rather than
creating one. Category creation costs a market education budget this does not have.

- Weak: "design-to-code tool" — crowded, and the category has a bad reputation
  from tools whose output nobody shipped
- **Chosen: "design system drift detection"** — different job, less crowded, and
  it makes CI the obvious home

## Tests

| Test | Result |
|---|---|
| Five-second | **Pass** — "drift detection" names a job |
| One-line | **Pass** — "it fails the build when the component stops matching the design" |
| Portability | **Pass** (fails correctly) — no competitor could use this sentence |
| Beats "do nothing" | **Pass** — do-nothing means finding drift in review |

## Statement

> For teams maintaining a design system, [name] is a CLI that catches design
> drift in CI. Unlike design-to-code generators, it does not produce components
> you have to throw away — it checks the ones you already have.
