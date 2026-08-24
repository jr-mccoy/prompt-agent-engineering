---
title: "Cross-Domain Analogy Mining — Borrow Mechanisms from 3 Unrelated Domains"
category: ideation/analogical
description: "Mine 3 deliberately-unrelated domains for transferable mechanisms that could apply to a target problem. Each domain yields 3–5 mechanism candidates; each candidate is tested for structural similarity (does the analogy actually transfer?) and translated into the target domain's terms. Counters in-domain monoculture in idea generation."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - ideation
  - analogy
  - cross-domain
  - mechanism-transfer
  - lateral-thinking
updated: "2026-05-10"
reasoning:
  styles: [analogical, structural, transfer]
  stakes: variable
  horizon: variable
  uncertainty: variable
  evidence_quality: variable
  domain_complexity: cross_domain
  collaboration: solo_or_team
  output_format: domain_then_mechanism_then_translation
  user_role: [designer, founder, pm, researcher, strategist, engineer]
  mode: [diverge, synthesize]
related_prompts:
  - domain-ideation/ideation_forced_quantity_100_ideas.md
  - domain-ideation/ideation_inverse_problem.md
  - domain-reasoning-craft/reasoning-moves/reasoning_steelman_construction.md
---

# Cross-Domain Analogy Mining

**Objective:** For a target problem in domain X, deliberately mine three *unrelated* domains for mechanisms that could be transferred. Each domain yields 3–5 candidate mechanisms; each candidate is tested for structural similarity (does the analogy actually map?), and the surviving candidates are translated into the target domain's vocabulary as concrete proposals. Designed to defeat in-domain monoculture in ideation — the tendency to draw only on examples from the same field.

**When to use:**
- Stuck on a problem that the in-domain literature has not solved.
- Designing something genuinely new where the obvious moves are exhausted.
- Pre-mortem feels familiar; you suspect the team is recycling within-industry conventions.
- Strategy work where the category itself is mature and differentiation requires importing patterns from elsewhere.
- Personal problems where you want to escape the framing your social circle uses.

**When NOT to use:**
- The target problem has a well-known in-domain solution. Use it.
- You're early-stage with the problem and haven't surveyed the in-domain options. Do that first.
- Time pressure prohibits the disciplined transfer step (without which the analogies become decorative).

**Audience:** Designers, founders, PMs, strategists, researchers, engineers — anyone whose ideation is bounded by the conventions of their own domain.

---

## Inputs / Context

1. **The target problem.** What is being solved or designed, in the target domain's language. As specific as possible.
2. **In-domain solutions already known or tried.** Surface so the analogy-mining doesn't re-derive them.
3. **The target domain.** Industry, field, or context (so we can pick analogy domains that are deliberately unrelated).
4. **Three analogy domains.** Either user-supplied or selected here. They should be:
   - Unrelated to the target domain (different industry, different scale, different time period).
   - Familiar enough to the user (or the analyst) that mechanisms can be drawn out specifically.
5. **Translation budget.** How concretely does the user want the candidate mechanisms translated? (Concept-level, design-level, prototype-level.)

---

## Constraints

### Must
- Pick 3 analogy domains that are unrelated to the target. "Software" mining "SaaS" is not cross-domain.
- For each analogy domain, identify **3–5 specific mechanisms** that solve a structurally-similar problem in that domain. Mechanisms, not vibes ("they have community" is not a mechanism; "they release one new tier per quarter and ladder reputation between tiers" is).
- For each mechanism, **test the structural mapping**: what's the underlying structure, does it actually fit the target, where does the analogy break?
- Translate surviving mechanisms into the target domain's vocabulary as concrete proposals (not just analogies).
- Mark each mechanism as **direct transfer**, **adapted transfer**, or **inspirational only** (the analogy informed thinking but the mechanism doesn't transfer cleanly).
- End with 3–5 concrete proposals in target-domain language, each traceable back to its source mechanism.

### Must Not
- Use analogy domains that are barely-disguised in-domain (e.g., "another B2B SaaS" for a B2B SaaS problem).
- Stop at "this is like X" without specifying the mechanism.
- Force-fit a mechanism that doesn't map structurally. The analogy mapping step exists to filter these.
- Translate so loosely that the proposals lose specificity.
- Discard the "inspirational only" mechanisms; they're often the seeds of original ideas even when the direct transfer fails.

---

## Instructions

### Step 1 — Restate the target problem
One paragraph. Include what success looks like, what the in-domain solutions are, and what's not working.

### Step 2 — Pick three analogy domains
Selected for distance from the target. Examples for varied target problems:

- For a SaaS pricing problem: airlines (yield management), gyms (membership tiers), book publishers (hardcover-paperback windowing).
- For team productivity: orchestras (rehearsal cadence), surgical teams (briefings), aviation (checklists).
- For onboarding design: museums (curator-led tours), video games (tutorial levels), cooking shows (mise en place).
- For knowledge management: libraries (cataloging systems), restaurants (kitchen station design), hospitals (handoff protocols).

State why each domain was picked.

### Step 3 — Mine each analogy domain
For each analogy domain, identify 3–5 specific mechanisms. For each mechanism:
- **Mechanism name** (specific, not vibes-level)
- **What problem it solves** in the analogy domain
- **How it works** (mechanism, not outcome)
- **Why it works** (underlying logic)

### Step 4 — Test the structural mapping
For each mechanism, ask:
- What's the underlying structure (actors, incentives, resource constraints, time dynamics)?
- Does that structure map to the target problem?
- Where does the analogy break?

Classify:
- **Direct transfer:** the structure maps cleanly; mechanism would work as-is.
- **Adapted transfer:** the structure maps with modification; mechanism needs adjustment.
- **Inspirational only:** the structure doesn't fully map, but the mechanism prompted a related thought worth keeping.

### Step 5 — Translate to target domain
For surviving mechanisms (direct or adapted transfer), translate into target-domain language. The translation:
- Uses the target's vocabulary (no mention of the source domain in the proposal itself).
- Specifies how the mechanism would actually be implemented in the target.
- Notes what would need to be true for the mechanism to work.

### Step 6 — Filter for novelty against in-domain solutions
Compare each translated proposal to the in-domain solutions already known. If the translated mechanism is just a relabeling of a known in-domain move, drop. The point is to find moves that aren't already in the in-domain repertoire.

### Step 7 — Final proposals
3–5 concrete proposals, each with:
- The proposal in target-domain language
- Source mechanism (for provenance)
- Type of transfer (direct / adapted / inspirational)
- What would need to be true for it to work
- Smallest test that would validate the transfer

### Step 8 — Inspirational-only catalog
Keep the inspirational-only mechanisms as a separate list. They didn't transfer cleanly but might seed future ideation.

---

## False-Positive Prevention

1. **Vibes-level analogy.** "We should be more like Disney" is not a mechanism. "We should pre-stage all customer interactions through a structured journey with marked transitions, the way Disney parks design crowd flow" is.
2. **Adjacent-domain pseudo-analogy.** Mining a domain that's basically the same as the target produces in-domain ideas dressed up as analogies. Pick deliberately unrelated domains.
3. **Force-fitting.** A mechanism that doesn't structurally map shouldn't be translated; it should be classified inspirational-only or discarded.
4. **Translation that loses specificity.** A vague translated proposal can't be tested. Specify what would actually be done.
5. **Analogy as authority.** "It works in [admired domain]" is not evidence it will work here. The structural mapping is the evidence.
6. **Discarding inspirationals.** Sometimes the best ideas come from analogies that didn't transfer cleanly but provoked a fresh thought. Keep them.
7. **Domain monoculture.** Picking three analogy domains that are themselves in the same family (three sports, three entertainment forms) collapses to one analogy with three flavors. Diversify across distance.
8. **Source-domain leak.** Final proposals that still mention the source domain ("like a museum tour…") aren't yet translated. Force the proposal into target language.

---

## Output Format

```
# Cross-domain analogy mining — [target problem]

## Target problem
[Restated]
- In-domain solutions already known/tried: [...]
- What's not working: [...]

## Analogy domains
1. [Domain 1] — chosen because [...]
2. [Domain 2] — chosen because [...]
3. [Domain 3] — chosen because [...]

## Domain 1: [name]
| # | Mechanism                  | Problem in source domain | How it works | Why it works |
|---|----------------------------|--------------------------|--------------|---------------|
| 1 | [specific name]            | [...]                    | [mechanism]  | [logic]       |
| 2 | …                          |                          |              |               |
| 3 | …                          |                          |              |               |

### Structural mapping
| Mechanism | Structure | Maps to target? | Where it breaks | Type |
|-----------|-----------|-----------------|------------------|------|
| 1         | [actors / incentives / resources / dynamics] | yes | [edge] | direct |
| 2         | …                                            | adapted | … | adapted |
| 3         | …                                            | no  | …  | inspirational |

## Domain 2: [name]
[Same structure]

## Domain 3: [name]
[Same structure]

## Translated proposals (in target language)
| # | Proposal | Source mechanism | Transfer type | What must be true | Smallest test |
|---|----------|------------------|---------------|-------------------|---------------|
| 1 | [target-domain proposal] | D1.M2 | direct | [conditions] | [test] |
| 2 | [proposal] | D2.M3 | adapted | [...] | [...] |
| 3 | [proposal] | D3.M1 | adapted | [...] | [...] |

## Inspirational-only catalog
- [Mechanism that didn't transfer but is worth remembering]
- [...]

## Novelty check
- Are these proposals novel against known in-domain solutions? [yes / partially / no — note any overlap]
```

---

## Verification

- [ ] Three analogy domains chosen, deliberately unrelated to the target.
- [ ] Each domain yields 3–5 specific mechanisms (not vibes).
- [ ] Each mechanism has structural mapping test (does it transfer, where does it break).
- [ ] Each mechanism classified direct / adapted / inspirational.
- [ ] 3–5 concrete proposals in target-domain language.
- [ ] Source domains not visible inside the final proposals.
- [ ] Inspirational-only mechanisms preserved separately.
- [ ] Novelty checked against in-domain solutions.
- [ ] No vibes-level analogies in the proposals.
- [ ] Each proposal has a smallest test for validation.
