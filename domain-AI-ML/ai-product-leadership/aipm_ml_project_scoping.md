---
title: "ML Project Scoping for Delivery"
category: AI-ML/ai-product-leadership
description: "Turn a chosen ML idea into a delivery-ready scope: problem framing, measurable success criteria, data plan, milestones, and the risks that actually kill ML projects."
techniques:
  - ST-02
  - CM-02
  - DS-02
  - NE-13
  - RT-05
difficulty: intermediate
tags:
  - project-scoping
  - success-criteria
  - milestones
  - data-plan
  - delivery
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/ai-product-leadership/aipm_use_case_prioritization.md
  - domain-AI-ML/ai-product-leadership/aipm_roi_business_case.md
  - domain-AI-ML/ai-product-leadership/aipm_failed_ml_project_postmortem.md
---

# ML Project Scoping for Delivery

**Objective:** Convert a selected AI/ML idea into a scoped, delivery-ready project definition — crisp problem statement, measurable and gated success criteria, an honest data plan, sequenced milestones, and a named risk register — so the team starts with shared expectations instead of discovering them mid-flight.

**When to Use:**
- A use case has been prioritized and you must write the project charter before kickoff.
- A project feels vague ("add AI to the product") and needs hard edges.
- Stakeholders disagree on what "done" or "good enough" means.

**When NOT to Use:**
- You are still choosing among candidates (use `aipm_use_case_prioritization.md`).
- You need the dollar justification (use `aipm_roi_business_case.md`).
- The project already shipped and stalled (use `aipm_failed_ml_project_postmortem.md`).

## Inputs / Context

- **The use case** — problem, the decision/action it improves, who consumes the output.
- **Business success definition** — what outcome leadership will judge by (and the metric, even if rough).
- **Data situation** — sources, ownership, quality, labeling status, volume, access path.
- **Constraints** — deadline, budget range, regulatory/privacy requirements, latency/SLA needs.
- **Team & tooling** — who's available, current MLOps/serving capability.

## Constraints

**Must:**
- Define success at two layers: the **business metric** (what leadership judges) and the **model metric** (what the team optimizes), and state how they connect.
- Set an explicit **baseline** and a **minimum-viable bar** the model must beat to justify shipping.
- Include a data-readiness checkpoint as an early, gating milestone — not an assumption.

**Must Not:**
- Promise an accuracy/performance number; state target ranges as hypotheses to be validated against the baseline.
- Treat "deploy the model" as the finish line — define the integration into a real workflow.
- Omit the kill criteria; a scope without a stop condition becomes a zombie project.

**Instructions:**

1. **Frame the problem precisely.** State what is predicted/generated, the unit of prediction, the prediction-time boundary (what's known when), and the action the output drives. Ambiguity here is the #1 source of rework.

2. **Define dual success criteria.** Specify the business metric and target band, then the model metric (chosen for the cost structure of errors), the baseline to beat, and the minimum bar for shipping. Connect the two explicitly.

3. **Write the data plan.** Inventory sources, ownership, access, quality, labeling, and volume. Identify the riskiest data assumption and make verifying it the first milestone.

4. **Choose the simplest viable approach.** Default to the least complex method that could clear the bar (heuristic → classical ML → deep/GenAI), and justify any escalation in complexity by the value it buys.

5. **Sequence milestones with gates.** Lay out phases — data readiness → baseline → iteration → integration → monitored launch — each with an exit gate and a decision (continue / pivot / stop).

6. **Build the risk register.** Name the project-specific risks (data, leakage, integration, adoption, drift, regulatory) with likelihood, impact, and a mitigation owner.

7. **Define kill/pivot criteria.** State the conditions under which the project should stop or change direction, so a sunk-cost spiral is pre-empted.

8. **Translate the scope for stakeholders.** Summarize in plain language: what we're building, how we'll know it worked, what could go wrong, and when we'll know.

**Output Format:**

A markdown project scope:
- **Problem Statement** — one paragraph, with prediction-time boundary and downstream action
- **Success Criteria** — table: Layer | Metric | Baseline | Min Bar | Target Band
- **Data Plan** — sources, gaps, riskiest assumption, readiness checkpoint
- **Approach** — chosen method + why the simplest one was/wasn't enough
- **Milestone Plan** — phases with gates and decisions
- **Risk Register** — Risk | Likelihood | Impact | Mitigation | Owner
- **Kill / Pivot Criteria**
- **Plain-Language Stakeholder Summary**

## Verification

- [ ] Both business and model success metrics are defined and explicitly linked.
- [ ] A baseline and a minimum shipping bar are stated; no bare accuracy promise.
- [ ] Data readiness is an early gating milestone, not an assumption.
- [ ] The output's integration into a real workflow is specified, not just "deploy."
- [ ] Kill/pivot criteria exist and are concrete.

## False-Positive Prevention

❌ **DON'T:**
- Scope to a model metric (AUC, F1) with no line to a business outcome anyone cares about.
- Assume the data is ready because someone said "we have lots of data."
- Set "ship a model" as success without defining what the model changes downstream.
- Write a milestone plan with no gate where the project could be honestly stopped.

✅ **DO:**
- Anchor the model metric to the asymmetric cost of false positives vs false negatives for this problem.
- Make the first milestone "prove the data can support this," with a go/no-go.
- Define adoption: who acts on the output, and what makes them trust it.
- Pre-write the conditions under which you'd kill or pivot — before momentum makes that unsayable.

## Example Output

```markdown
## ML Project Scope: Support Ticket Auto-Triage

### Problem Statement
Predict the routing queue and priority for an inbound support ticket at creation time, using only fields available at submission (text, product, customer tier). Output auto-assigns the queue and suggests a priority an agent can override. Prediction-time boundary: no post-resolution fields.

### Success Criteria
| Layer | Metric | Baseline | Min Bar | Target Band |
|---|---|---|---|---|
| Business | Median time-to-first-response | current manual triage | -10% | -15% to -30% |
| Model | Routing accuracy (top-1) | rule-based router | beat by 8 pts | meaningful lift over rules |

### Data Plan
18 months of resolved tickets with final queue labels. Riskiest assumption: historical labels reflect *correct* routing, not just *where it ended up*. Readiness checkpoint (Week 2): audit label quality on a 300-ticket sample.

### Approach
Start with a text classifier on existing labels (classical, interpretable). Escalate to an LLM-based classifier only if the simple model can't clear the bar — justified by error analysis, not by default.

### Milestone Plan
1. Data readiness (gate: labels usable) → 2. Baseline beats rules (gate: min bar) → 3. Iterate → 4. Shadow-mode integration (gate: agent trust) → 5. Monitored launch with override tracking.

### Risk Register
| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Noisy historical labels | High | High | Week-2 audit; relabel sample | DS lead |
| Agents distrust auto-assignment | Med | High | Shadow mode + visible override | PM |

### Kill / Pivot Criteria
If after the baseline milestone the model cannot beat the existing rules by the min bar with clean labels, stop and revisit the rule engine instead.

### Stakeholder Summary
We're auto-routing tickets to cut response time. We'll know it works if response time drops without agents fighting the assignments. Biggest risk is that our historical data records where tickets *went*, not where they *should* have gone — we check that in week 2 before building anything.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** frame→success→data→approach→milestones→risk→kill flow.
- **CM-02 (Constraint Specification):** baseline, min bar, prediction-time boundary, kill criteria as governing constraints.
- **DS-02 (Metric Specification):** dual business/model metrics with baselines and bands.
- **NE-13 (Technical-to-Business Translation):** stakeholder summary linking model work to outcomes.
- **RT-05 (Evidence-Based Reasoning):** data-readiness gate anchors scope to verifiable reality.

**Related Prompts:**
- `aipm_use_case_prioritization.md` — choose what to scope.
- `aipm_roi_business_case.md` — justify the scope financially.
- `aipm_failed_ml_project_postmortem.md` — learn from scopes that went wrong.
