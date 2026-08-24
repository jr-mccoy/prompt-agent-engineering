---
title: "Evaluate Whether a Capability Compounds or Stays Flat Over Time"
category: business-strategy/ai-strategy
description: "A diagnostic that separates AI-enabled capabilities that compound (each use makes the next use better) from capabilities that stay flat (each use is independent), so investment is directed where compounding actually occurs."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - ai-strategy
  - compounding
  - capability-evaluation
  - moat
  - investment-prioritization
updated: "2026-04-20"
related_prompts:
  - domain-business-strategy/ai-strategy/aistrategy_context_accumulation_map.md
  - domain-business-strategy/ai-strategy/aistrategy_platform_brief.md
  - domain-business-strategy/ambition-leverage/ambition_leadership_audit.md
---

# Evaluate Whether a Capability Compounds or Stays Flat Over Time

**Objective:** Take a specific AI-enabled capability the organization has or is considering, and evaluate whether it compounds over time (each additional use produces a durable improvement the organization keeps) or stays flat (each use is independent, leaving nothing behind). Produce a score, the mechanism of compounding (or its absence), and the specific investments that would convert a flat capability into a compounding one.

**When to use:** Prioritizing among several AI initiatives. Challenging an executive's claim that a capability is "strategic." Evaluating whether a vendor's pitch for "accumulating context" actually produces accumulating advantage for your organization. Before committing multi-year investment to a capability.

**Audience:** Strategy team, CTO, investment committee, chief of staff. The output is a brief that can be used to defend or de-prioritize an investment, so the reasoning has to stand up to pushback.

---

## Inputs Required

1. **The specific capability.** Not "AI" — a named capability (e.g., "AI-assisted customer-email triage," "contract review bot," "internal search chat"). If the user names something vague, sharpen first.
2. **Who uses it, how often, and for what.** Rough volume and use-case pattern.
3. **What artifacts each use produces.** Drafts, decisions, corrections, feedback, structured data — anything that could in theory be fed back in.
4. **Current disposition of those artifacts.** Discarded, stored, reviewed, fed back into the model, written into a doc, or invisible (in-memory only).
5. **Competing capabilities** that would do the same job without AI, for comparison.

Refuse to score a capability described only at a marketing level ("our AI learns from every interaction"). Press for the specific artifacts and the specific feedback loop.

---

## Instructions

### Step 1 — Separate the three compounding channels

A capability compounds through one or more of these channels. For the named capability, evaluate each:

- **Proprietary data compounding.** Does each use produce structured data the organization keeps and that improves future uses?
- **Context / memory compounding.** Does the capability accumulate context about the organization, its users, or its domain that durably improves subsequent outputs?
- **Workflow / organizational compounding.** Does the capability change how work flows, such that the change creates opportunities the organization alone is positioned to exploit?

For each channel, rate it: **strong / weak / absent / theoretical only.** "Theoretical only" means the channel could exist but the current implementation doesn't capture it.

### Step 2 — Apply the "commoditization test"

If every competitor adopts the same capability tomorrow, what's left that's yours? Possible answers:

- **Proprietary data** that doesn't exist at competitors.
- **Context-tuned behavior** that would cost competitors months to rebuild.
- **Organizational workflows** that require the capability + something else you have (brand, distribution, relationships).
- **Nothing distinctive remains** — the capability is table stakes, valuable to retain but not a moat.

"Nothing distinctive remains" is a valid answer. A capability can be worth investment without being a moat.

### Step 3 — Draw the compounding mechanism

In one diagram or 3–5 steps, describe the actual loop:

```
Use → Artifact produced → Artifact stored → Stored artifact used by next turn → Next turn better
```

If the loop is broken — any arrow is missing or weak — name which. This is the most common failure: the artifact is produced but never stored, or stored but not used, or used but not evaluated for whether it actually improved the next turn.

### Step 4 — Estimate the compounding rate

For capabilities where the loop exists, estimate:
- How many uses per [week/month] currently.
- How much each use contributes to the compounding pool (rich / thin / invisible).
- Time until the compounding is material — weeks, quarters, years. Calibrate conservatively.

If the loop is broken, skip this step and move to Step 5.

### Step 5 — Name what would move it

For a flat or weakly-compounding capability, name the specific investments that would convert the channel:

- **Proprietary data:** build the data pipe that captures outputs + corrections in structured form. Cost, owner, time.
- **Context:** stand up a retrieval layer that points at accumulated org context. Cost, owner, time.
- **Workflow:** identify the second piece (brand, distribution, relationship) that the capability composes with to create a moat. If no such piece exists, the workflow channel cannot be unlocked.

Not every capability has a viable conversion. If all three channels are absent and cannot reasonably be added, the capability is flat and should be treated as such.

### Step 6 — Comparison against non-AI alternative

Briefly: does the non-AI alternative have any compounding dynamic of its own? (E.g., a well-documented manual process compounds tacit team knowledge.) This prevents over-attributing compounding to AI when it would exist in any mature system.

### Step 7 — Verdict

One paragraph:
- **Compounding today?** Yes / No / Partial.
- **Could compound with investment?** Yes (named investment) / No.
- **Worth investing in?** Depends — state the criteria: if the capability is flat and becoming commodity, investment is maintenance; if it's flat but could compound with specific investment, that investment is the real decision.

---

## Constraints

### Must
- Evaluate all three compounding channels separately.
- Apply the commoditization test.
- Describe the actual loop or name which arrow is missing.
- Separate "compounding" from "valuable." A capability can be one without the other.
- Ground the verdict in evidence from the previous steps.

### Must Not
- Accept a marketing description ("it gets smarter over time") without naming the specific artifact and feedback loop.
- Assume a generic LLM's pretraining improvements count as your organization's compounding.
- Collapse compounding into "proprietary data" only; context and workflow channels are real.
- Invent investments that would require infrastructure the organization has not asked about.
- Conclude "yes, it compounds" without the loop being describable.

---

## False-Positive Prevention

1. **Don't confuse "users say it's useful" with compounding.** Utility per use is not the same as each use improving the next.
2. **Don't confuse model improvements with your compounding.** When your vendor ships a better model, your capability improves — but everyone using that vendor gets the same lift. That's table stakes, not compounding.
3. **Don't count "we collect logs" as proprietary data compounding.** Logs that aren't used to improve the system are not part of a loop.
4. **Don't treat context compounding as free.** If retrieval layers aren't built, accumulated context is inaccessible — so it isn't compounding.
5. **Don't overclaim workflow compounding.** Workflow moats exist, but they require a second, non-AI asset (brand, distribution, regulation, scale). Without that, workflow change alone is copyable.
6. **Be willing to conclude "flat."** Flat capabilities are often the right investment if they deliver on utility — they just shouldn't be sold to leadership as strategic moats.

---

## Output Format

```
# Compounding evaluation — [capability name]

## Capability definition
[Sharpened, specific description.]

## Channel evaluation
| Channel | Rating (strong/weak/absent/theoretical) | Evidence |
|---------|----------------------------------------|----------|
| Proprietary data |  |  |
| Context / memory |  |  |
| Workflow / organizational |  |  |

## Commoditization test
If every competitor has this tomorrow, what remains ours: [answer].

## Actual loop
Use → [artifact] → [stored where] → [used how by next turn] → [improves next turn — verified how]

Weak / missing arrow: [name it].

## Compounding rate (if loop exists)
- Uses per period: [rough]
- Contribution per use: [rich/thin/invisible]
- Time until material: [weeks/quarters/years]

## What would move it (if flat)
- Data channel: [specific investment, owner, time]
- Context channel: [specific investment, owner, time]
- Workflow channel: [required second asset, present? Y/N]

## Non-AI comparison
[Does the non-AI alternative have its own compounding dynamic?]

## Verdict
- Compounding today: [Y/N/Partial]
- Could compound with investment: [Y/N + what]
- Strategic vs table-stakes: [which]
- Worth investing in: [conditional framing]
```

---

## Verification

- [ ] All three channels evaluated separately.
- [ ] Commoditization test applied with a named answer.
- [ ] Loop described or broken arrow named.
- [ ] Non-AI alternative considered.
- [ ] Verdict distinguishes compounding from valuable.
- [ ] Marketing claims from vendor are not used as evidence.
