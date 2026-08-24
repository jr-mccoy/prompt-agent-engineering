---
title: "Scan for Cascade Effects From a New Capability"
category: presentations/visual-planning
description: "When a new capability or change arrives, systematically scan for the second- and third-order effects it triggers across roles, processes, artifacts, metrics, and norms — so the team doesn't get blindsided by the downstream shifts the obvious first-order use doesn't explain."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - RT-07
  - QA-01
difficulty: advanced
tags:
  - visual-planning
  - cascade-effects
  - second-order
  - systems-thinking
  - capability-impact
updated: "2026-04-21"
related_prompts:
  - domain-presentations/visual-planning/visualplan_capability_frontier_map.md
  - domain-presentations/visual-planning/visualplan_modality_router.md
  - domain-engineering-workflows/ai-native-rollouts/airollout_bottleneck_migration_plan.md
  - domain-business-strategy/ai-strategy/aistrategy_capability_compounding_evaluation.md
  - domain-business-strategy/ambition-leverage/ambition_insight_to_action_workflow.md
---

# Scan for Cascade Effects From a New Capability

**Objective:** Given a specific new capability and its primary (first-order) use in a team or organization, identify the second- and third-order cascade effects across five planes: roles, processes, artifacts, metrics, and norms. Produce a mapped set of likely downstream shifts, each with a confidence label and an early-warning signal — not a speculative "AI will change everything" essay.

**When to use:**
- A capability has landed or is about to (a new tool, a new model, a new platform feature) and the team is planning how to use it.
- First-order use has already started and the user wants to get ahead of the shifts it triggers.
- A strategist is briefing leadership on the implications of adopting a capability, and "just do it" isn't sufficient.
- After `visualplan_capability_frontier_map.md` has identified what the capability makes possible/cheap, to trace where impact lands next.

**Don't use when:** The capability is still hypothetical (a future release, a paper). This prompt maps downstream effects of real capabilities being adopted.

**Audience:** A strategist, EM, ops lead, or CoS preparing a briefing or planning doc. Output is a cascade map with early-warning signals, handed to a decision-maker.

---

## Inputs Required

1. **The capability.** Specific, real, already available. One sentence.
2. **The primary first-order use.** How the team or org is using (or about to use) the capability. Specific: "AI reviewing PRs for 40% of the team," "LLM drafting customer replies in support tier 1," "design generation for internal decks," etc.
3. **The unit of analysis.** One team, one org, one role, one function. Not "the industry" — too diffuse for a useful cascade map.
4. **The current state before the capability.** What roles, processes, artifacts, metrics, and norms exist today for the unit.
5. **Known early signals.** Anything the user has already seen shift since the capability was introduced. Could be positive or concerning.
6. **Time horizon.** How far out to scan: 3 months / 6 months / 12 months / 24 months. Cascade confidence decays quickly past 12 months.

---

## Instructions

### Step 1 — Restate the first-order effect concretely

From input 2, state the direct, observable change. Not "productivity increases" — "the PR review cycle time for AI-reviewed PRs drops from ~8 hours to ~2 hours." First-order effects are specific and measurable.

If you can't state the first-order effect in measurable terms, go back to the user — cascade mapping depends on a sharp first-order claim.

### Step 2 — Scan five planes for cascade effects

For each plane, identify 2–4 likely second-order effects. Be specific. Each cascade has: (a) the effect, (b) the mechanism linking it to the first-order change, (c) a confidence label, (d) a time horizon, (e) an early-warning signal.

#### 2.1 Roles
What shifts in what people do, who the org needs, and how judgment is distributed?

- **Demand shifts:** Some work dries up; some work becomes bottleneck.
- **Skill demand:** New skills become load-bearing (reviewing AI output ≠ doing the work); old skills commoditize.
- **Title / level compression:** Junior-intensive work that AI now does can push junior hiring to a different shape.
- **Residual-human reshape:** What humans now do post-AI (see `career_residual_skills_inventory.md`).

#### 2.2 Processes
What operational processes bend, break, or need new gates?

- **Review and gate shifts:** AI-produced work may need different review than human-produced.
- **Throughput redistribution:** Bottlenecks move (see `airollout_bottleneck_migration_plan.md`).
- **Queue and SLA:** Upstream queues may empty; downstream may flood.
- **Escalation patterns:** Ambiguous cases shift from "hard case" to "common case."

#### 2.3 Artifacts
What do the team's produced artifacts look like differently?

- **Shape shift:** Artifacts become longer / shorter / more structured / less reviewed.
- **New artifacts:** Artifacts that didn't exist (AI postmortems, prompt libraries, drift reports).
- **Obsolete artifacts:** Artifacts that stop mattering.
- **Authoring chain:** Who touches the artifact when.

#### 2.4 Metrics
Which numbers shift, and which shift misleadingly?

- **Direct metrics:** Throughput, cycle time, ticket volume, PR count.
- **Gaming-vulnerable metrics:** Metrics that can go up while quality goes down (see `correctness_pre_mortem.md`, QA-21 for gaming vectors).
- **Lagging quality metrics:** Defects, customer complaints, escalations take weeks/months to show drift.
- **Decommissioned metrics:** Metrics that stop making sense (e.g., "lines of code" when most authoring is AI).

#### 2.5 Norms
What unwritten rules bend?

- **Attribution and credit:** Who gets credit for AI-assisted work.
- **Reviewability and trust:** When to trust AI output; when to double-check.
- **Collaboration:** Pair-programming / co-authoring practices.
- **Work visibility:** What's shown vs what's omitted (AI-use transparency).
- **Accountability:** When something goes wrong, who's accountable.

### Step 3 — Map the cascade graph

Produce a small graph (prose or table): first-order effect → named second-order effects per plane → any third-order effects where clear.

Third-order effects: only include where the chain is plausible with current evidence. If a third-order effect requires three speculative jumps, omit and note.

### Step 4 — Tag confidence and time horizon

For each cascade effect:

- **Confidence:** High (already observed in this unit or a comparable unit) / Medium (strong mechanism, no direct observation yet) / Low (plausible, speculative).
- **Time horizon:** 0–3 mo / 3–6 mo / 6–12 mo / 12–24 mo.

Low-confidence, long-horizon effects should be few and clearly labeled as speculative.

### Step 5 — Assign early-warning signals

Per cascade, name a specific, observable signal the user can watch for. Not "keep an eye on morale" — specific: "per-person PR volume drops >30% quarter-over-quarter," "first-level support ticket resolution time halves while second-level escalation rate rises >20%."

Signals should be observable from data the user or their team already collects (or could collect cheaply).

### Step 6 — Flag the counter-cascades

Some cascades cancel each other. For each pair of cascades that plausibly counter, note the interaction:

- AI reviews PRs → less review time → human reviewers have more bandwidth → standards rise → cycle time re-increases.
- LLM drafts customer replies → throughput up → ticket volume grows (customers write more) → throughput gain partially offset.

Name 1–3 counter-cascades where they apply.

### Step 7 — Flag harmful cascades

Some cascades are risks worth mitigating now:

- **Skill erosion:** The residual humans lose the skill they now rarely practice.
- **Monoculture:** AI-shaped output across a team homogenizes style / approach.
- **Audit blindness:** If AI output is mostly trusted, real errors become harder to detect.
- **Incentive drift:** A metric that was a proxy for quality becomes pure throughput.

Name the harmful ones specific to this unit, and what the team should watch for.

### Step 8 — Prioritize for the decision-maker

For the downstream decision (implied by the audience using this scan), the top 3–5 cascades that would most change the decision. Not all cascades matter to the decision equally.

### Step 9 — Honest omissions

State what this scan does NOT cover:

- Effects outside the unit of analysis.
- Time horizons past input 6.
- Effects dependent on further capability changes (not just the one in input 1).

### Step 10 — Verify and output

Run the verification checklist.

---

## Constraints

### Must
- State the first-order effect in measurable terms.
- Scan all five planes (roles, processes, artifacts, metrics, norms).
- Tag every cascade with confidence and time horizon.
- Assign observable early-warning signals.
- Include counter-cascades where plausible.
- Flag harmful cascades and name watch items.

### Must Not
- Include third-order effects requiring > 2 speculative jumps.
- Make cascade claims without a mechanism linking them to the first-order effect.
- Use "AI will transform" or similar load-bearing hype.
- Skip counter-cascades; they often halve the apparent impact.
- Predict cascades beyond the input 6 time horizon.
- Confuse "this would happen eventually" with "this happens because of this capability."

---

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Attribute unrelated secular trends to the capability. Many shifts would happen anyway; only include effects with a specific mechanism tied to the first-order change.
- Let the scan become a list of AI platitudes. Every cascade is unit-specific.
- Inflate confidence on long-horizon cascades. Past 12 months, label most as Medium or Low.
- Ignore counter-cascades because they're inconvenient.
- Confuse "the capability enabled X" with "the capability caused X." Enablement doesn't force adoption.

✅ **DO:**
- Check each cascade: "if the capability weren't here, would this still happen?" If yes, the cascade is weak.
- Name the mechanism explicitly — a reader should be able to reproduce the reasoning.
- Prefer observable signals tied to existing data.
- Label speculative cascades as speculative; don't hide them.
- Acknowledge that the cascade map will be wrong in places. Build in periodic re-scanning (e.g., quarterly).

---

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** Over-claims cascades; team plans for shifts that don't materialize; real shifts go unwatched.

❌ **UNHELPFUL failure:** Hedges every cascade to uselessness; map has no actionable signal.

✅ **Quality check:** A decision-maker reading the map can point to any cascade and say "what would I see in 3 months that confirms this?" and get a specific signal.

---

## Output Format

```markdown
# Cascade Effects Scan — [Capability], [Unit]

## First-Order Effect (measurable)
[One sentence with numbers or specific observable state.]

## Cascade Map by Plane

### Roles
| Cascade | Mechanism | Confidence | Horizon | Early Signal |
|---------|-----------|-----------|---------|-------------|
| | | H/M/L | | |

### Processes
| Cascade | Mechanism | Confidence | Horizon | Early Signal |
| | | | | |

### Artifacts
| Cascade | Mechanism | Confidence | Horizon | Early Signal |
| | | | | |

### Metrics
| Cascade | Mechanism | Confidence | Horizon | Early Signal |
| | | | | |

### Norms
| Cascade | Mechanism | Confidence | Horizon | Early Signal |
| | | | | |

## Counter-Cascades
- [Pair + how they interact]

## Harmful Cascades to Watch
- [Named risk + specific watch item]

## Top 3–5 Cascades That Most Change the Decision
1. 
2. 
3. 

## Third-Order Effects (where evidence supports)
- [Sparse list; label speculative]

## Honest Omissions
- [What this scan does not cover]

## Recommended Re-Scan Cadence
- [Every N months or on specific triggers.]
```

---

## Verification

- [ ] First-order effect is measurable, not abstract.
- [ ] All five planes have 2–4 cascades each (or a note on why a plane has fewer).
- [ ] Every cascade has mechanism, confidence, horizon, early signal.
- [ ] Counter-cascades present where plausible.
- [ ] Harmful cascades flagged with watch items.
- [ ] Third-order effects limited to those with plausible chains.
- [ ] Honest omissions named.
- [ ] Top 3–5 cascades for the decision highlighted.
- [ ] No hype vocabulary carrying meaning.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Output is a five-plane cascade map with signals, not a "what AI means for us" essay.
- **ST-02 (Structured Sequential Instructions):** Ten steps force first-order → five planes → cascade graph → confidence → signals → counter-cascades → harmful → prioritize → omissions → verify.
- **CM-02 (Constraint Specification):** Must Not block forbids mechanism-less cascades and beyond-horizon speculation.
- **DS-01 (Framework Application):** Five planes (roles / processes / artifacts / metrics / norms) is the framework; the cascade structure is the analytic unit.
- **RT-07 (Cascade Effect Analysis):** The technique's core move — systematically tracing second-order effects across dimensions — is the prompt's backbone.
- **QA-01 (Self-Verification):** Verification checklist plus the "would this happen without the capability" test catch attribution errors before the map influences decisions.
