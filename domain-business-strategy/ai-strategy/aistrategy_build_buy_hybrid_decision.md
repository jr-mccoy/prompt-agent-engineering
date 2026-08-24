---
title: "AI Agent Build-vs-Buy-vs-Hybrid Decision"
category: business-strategy/ai-strategy
description: "Recommends build, buy, or hybrid for an agent capability by testing whether customization creates durable advantage, offloading undifferentiated infrastructure, and judging on business outcomes rather than token cost."
techniques:
  - RT-02
  - DS-02
  - QA-08
  - NE-02
  - DS-06
difficulty: intermediate
tags:
  - build-vs-buy
  - hybrid
  - agent-strategy
  - vendor-selection
  - roi
updated: "2026-06-19"
related_prompts:
  - domain-business-strategy/ai-strategy/aistrategy_platform_brief.md
  - domain-business-strategy/ai-strategy/aistrategy_vendor_switch_cost.md
  - domain-business-strategy/ai-strategy/aistrategy_capability_compounding_evaluation.md
---

# AI Agent Build-vs-Buy-vs-Hybrid Decision

**Objective:** Produce a defensible build / buy / hybrid recommendation for a specific agent capability — at the component level and overall — by testing whether customization creates meaningful, durable advantage, by offloading the undifferentiated execution layer, and by judging options on business outcomes rather than raw token cost.

**When to Use:**
- You are deciding how to source an agent capability (assistant, workflow automation, internal copilot) and the build/buy/hybrid choice is open.
- Engineering talent is scarce and you must decide where it earns the most return.
- A capability is stalling because someone is hand-maintaining infrastructure that adds no differentiation.

**When NOT to Use:**
- The decision is already locked by contract, compliance, or a platform mandate — there is nothing to recommend; record the constraint instead.
- You need a full board-level platform brief (use `aistrategy_platform_brief.md`) or a switch-cost estimate for an existing vendor (use `aistrategy_vendor_switch_cost.md`).

**Source:** Framework adapted from Anthropic & Material, *2026 State of AI Agents Report*, and Anthropic, *Building AI Agents for the Enterprise* (2026) — a vendor report — figures attributed inline; no source text reproduced.

## Inputs / Context

Provide what you can; the analysis degrades gracefully if some are missing:
- **The capability** — what the agent should do, for whom, and the business outcome it serves.
- **Components** — the parts that make it work (compute, memory/context store, orchestration, model access, the agentic experience/UX, domain logic).
- **Differentiation thesis** — which parts, if any, are core to how you win versus competitors.
- **Engineering capacity** — how much scarce talent is available and what it would otherwise build.
- **Outcome metrics** — the business results that define success (revenue, cycle time, quality, retention), not just cost.

## Constraints

**Must:**
- Run the differentiation gate per component: "Does customization here create meaningful, durable advantage?" No → buy/pre-built; only-in-parts → hybrid; it-is-the-core-differentiator → build.
- Offload the undifferentiated execution layer (compute, memory plumbing, orchestration) so engineering goes to the differentiated agentic experience.
- Evaluate options on business outcomes; capability matters more than token cost.

**Must Not:**
- Recommend "build" for infrastructure no one will maintain, where the capability would reach customers too late to matter.
- Optimize the decision on token/compute cost while ignoring the value of the most capable option.
- Treat hybrid as a fence-sit; every component must land on a specific build/buy/hybrid call with a reason.

**Instructions:**

1. **Decompose into components.** Break the capability into its parts (compute, memory/context, orchestration, model access, agentic experience, domain logic). Each part gets its own recommendation.

2. **Apply the differentiation gate to each component.** Ask whether customizing that part creates meaningful, durable advantage. If no, buy/pre-built; if only some parts differentiate, hybrid; if the part is the core differentiator, build.

3. **Locate the 2026 baseline.** Position against prevailing practice: fully pre-built (~21% of approaches — fastest to running, least customization for proprietary systems), hybrid (~47% — the dominant default, off-the-shelf where it works plus custom where it differentiates), fully custom (~20% — maximum control and differentiation at heavy engineering cost) (Anthropic & Material, *2026 State of AI Agents Report*).

4. **Offload the execution layer.** Flag undifferentiated infrastructure (compute, memory plumbing, orchestration) and recommend buying/offloading it, so scarce engineering invests in the differentiated agentic experience rather than maintaining plumbing.

5. **Score on outcomes, not cost.** Rate each option by the business outcome it delivers; the most capable option often delivers outsized returns even at higher per-token cost (Anthropic, *Building AI Agents for the Enterprise*, 2026). Make the cost tradeoff explicit, not the deciding factor.

6. **Estimate maintenance burden.** For each build/hybrid component, state who maintains it and the risk that it stalls and reaches customers too late to matter.

7. **Synthesize the overall recommendation.** Roll the per-component calls into a single build/buy/hybrid stance, name the differentiating parts you keep in-house, and state what would change the recommendation.

**Output Format:**

A markdown decision brief:
- **Component Recommendation Matrix** — table: Component | Build/Buy/Hybrid | Rationale | Differentiation? | Maintenance burden
- **Baseline Positioning** — where this lands versus the ~21% / ~47% / ~20% split
- **Execution-Layer Offload** — what to buy so engineering stays on the differentiated experience
- **Outcome-Based ROI Note** — value of the most capable option vs. token cost
- **Overall Recommendation** — single stance + what would change it

## Verification

- [ ] Every component has a build/buy/hybrid call with a rationale.
- [ ] The differentiation gate was applied per component, not just overall.
- [ ] Undifferentiated infrastructure is offloaded, not built.
- [ ] Options are judged on business outcomes; cost is explicit but not the sole driver.
- [ ] Maintenance burden and stall risk are stated for built/hybrid parts.
- [ ] The overall recommendation names its invalidation conditions.

## False-Positive Prevention

❌ **DON'T:**
- Default to "build" because it feels more strategic, when no durable advantage is created.
- Pick the cheapest option on token cost and call it the ROI-optimal choice.
- Buy the differentiating core just to ship fast, surrendering the thing that makes you win.
- Leave critical custom infrastructure with no named owner.

✅ **DO:**
- Build only where customization creates meaningful, durable advantage; buy or hybrid everywhere else.
- Judge on the business outcome; let the most capable option win where returns justify it.
- Keep the differentiated agentic experience in-house and offload the plumbing.
- Assign an owner and a stall-risk note to every built/hybrid component.

## Example Output

```markdown
## Build/Buy/Hybrid: Claims-Triage Agent

### Component Recommendation Matrix
| Component | Build/Buy/Hybrid | Rationale | Differentiation? | Maintenance burden |
|---|---|---|---|---|
| Model access | Buy | Frontier capability is commoditized | No | Vendor-managed |
| Orchestration | Buy | Undifferentiated plumbing | No | Low (offloaded) |
| Memory/context store | Hybrid | Off-the-shelf store, custom schema | Partly | Medium |
| Domain triage logic | Build | Our regulatory edge cases win deals | Yes (core) | High — owned by claims eng |
| Agentic experience/UX | Build | How adjusters experience it differentiates | Yes | Medium |

### Baseline Positioning
Lands as hybrid — consistent with the ~47% dominant default; not fully custom (~20%) since model + orchestration are bought.

### Execution-Layer Offload
Buy compute, orchestration, and the base memory store so engineering stays on triage logic and UX.

### Outcome-Based ROI Note
The most capable model raises auto-resolution rate; the revenue from faster, more accurate triage dwarfs the higher token cost.

### Overall Recommendation
Hybrid: buy the execution layer, build the triage logic and experience. Reconsider if the regulatory edge cases become an industry-standard library a vendor sells.
```

**Techniques Used:**
- **RT-02 (Role/Stakeholder Framing):** reasons from the operator deciding where scarce engineering earns the most return.
- **DS-02 (Decision-Criteria Specification):** the differentiation gate is the explicit decision rule.
- **QA-08 (Comparative Evaluation):** weighs build vs. buy vs. hybrid against a shared baseline.
- **NE-02 (Negative-Example Avoidance):** rules out building undifferentiated, unmaintained infrastructure.
- **DS-06 (Prioritization & Severity Guidance):** prioritizes the differentiating components for in-house build.

**Related Prompts:**
- `aistrategy_platform_brief.md` — the board-level brief this component decision feeds.
- `aistrategy_vendor_switch_cost.md` — quantifies lock-in for the buy/hybrid components.
- `aistrategy_capability_compounding_evaluation.md` — tests whether a built component compounds or stays flat.
