---
title: "AI Vendor & Foundation-Model Selection"
category: AI-ML/ai-product-leadership
description: "Evaluate and select AI vendors or foundation models against weighted criteria — capability fit, cost, latency, data terms, lock-in, and viability — with a defensible scorecard."
techniques:
  - ST-02
  - RT-02
  - DS-06
  - CM-02
  - NE-13
difficulty: intermediate
tags:
  - vendor-selection
  - foundation-models
  - evaluation
  - lock-in
  - procurement
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/ai-product-leadership/aipm_build_buy_partner_decision.md
  - domain-AI-ML/ai-product-leadership/aipm_model_risk_brief_for_execs.md
  - domain-AI-ML/ai-product-leadership/aipm_ai_policy_authoring.md
---

# AI Vendor & Foundation-Model Selection

**Objective:** Run a structured, weighted evaluation of candidate AI vendors or foundation models for a specific use case — covering capability fit, cost at expected volume, latency/reliability, data and security terms, lock-in, and vendor viability — producing a scorecard and a recommendation that withstands procurement and security review.

**When to Use:**
- "Buy" or "partner" has been chosen and you must pick among providers/models.
- Selecting a foundation model (proprietary API vs open-weights) for a GenAI feature.
- Re-evaluating an incumbent vendor against the current market.

**When NOT to Use:**
- You haven't decided build-vs-buy yet (use `aipm_build_buy_partner_decision.md`).
- You need an internal-use policy for AI tools (use `aipm_ai_policy_authoring.md`).

## Inputs / Context

- **Use case & requirements** — what the model/vendor must do, accuracy/quality bar, latency/SLA, expected volume.
- **Candidates** — the vendors/models under consideration (and whether open-weights is in scope).
- **Constraints** — budget band, data residency/privacy, security/compliance requirements, deployment surface (cloud/on-prem).
- **Evaluation assets** — any representative test set or eval the candidates can be run against.
- **Strategic posture** — tolerance for lock-in, importance of portability.

## Constraints

**Must:**
- Score all candidates on the same weighted criteria, with weights derived from the use case (not a generic template).
- Where quality is decisive, require an evaluation on the user's representative data — do not select on vendor-published benchmarks alone.
- Include cost at realistic expected volume (not headline per-token price) and the lock-in/exit story.

**Must Not:**
- Fabricate benchmark scores, pricing, or latency figures; use the user's eval results or vendor-confirmed figures, and mark anything unverified as "to confirm."
- Treat published leaderboard rank as proof of fit for this use case.
- Ignore data-handling terms (training on your data, retention, residency) when comparing.

**Instructions:**

1. **Derive the criteria and weights from the use case.** A real-time customer feature weights latency and reliability; a batch enrichment weights cost and accuracy. State the weights and why.

2. **Define the quality bar and how it's measured.** Specify the representative eval (task, metric, slices) the candidates will be run against. If no eval exists, flag that selecting on quality is premature and recommend building one first.

3. **Score capability fit.** Use the eval results (or mark as unverified). Capture quality, plus relevant features (function calling, context window, fine-tuning, modality) the use case needs.

4. **Score cost realistically.** Model cost at expected volume including retries, context overhead, and any fine-tuning/hosting cost — as ranges. Compare per-unit-of-work, not per-token.

5. **Score operational factors.** Latency, throughput, rate limits, uptime/SLA, support, and region availability against the SLA the use case demands.

6. **Score data, security, and viability.** Data-training/retention terms, residency, certifications, and vendor stability/roadmap risk. For foundation models, weigh proprietary-API lock-in vs open-weights portability — cross-reference strategic vendor switch-cost analysis where relevant.

7. **Recommend with a portability hedge.** Name the pick, the runner-up, the conditions to switch, and an abstraction-layer recommendation that keeps a future swap cheap.

**Output Format:**

A markdown evaluation:
- **Criteria & Weights** — derived from the use case, with rationale.
- **Scorecard** — table: Criterion | Weight | Candidate A | B | C (scores + note).
- **Cost at Volume** — modeled cost ranges per candidate at expected usage.
- **Data/Security/Viability Notes** — terms and risks per candidate.
- **Recommendation** — pick + runner-up, switch conditions, and a portability/abstraction hedge.

## Verification

- [ ] Weights derived from the specific use case, not a default template.
- [ ] Quality scored from the user's eval or explicitly marked unverified.
- [ ] Cost modeled at expected volume per unit of work, not headline per-token price.
- [ ] Data-handling, residency, and viability assessed for each candidate.
- [ ] Recommendation includes lock-in mitigation and switch conditions.

## False-Positive Prevention

❌ **DON'T:**
- Pick the model topping a public leaderboard without testing it on your data and slices.
- Compare candidates on per-token price while ignoring context overhead and retries.
- Overlook that a vendor trains on submitted data or won't meet residency requirements.
- Lock into a proprietary API for a core capability with no abstraction layer.

✅ **DO:**
- Run a representative eval (with slices) and select on that, not marketing benchmarks.
- Model realistic cost-per-completed-task at expected volume, as ranges.
- Read the data terms; disqualify candidates that fail privacy/residency hard constraints.
- Recommend a thin provider abstraction so switching is a config change, not a rewrite.

## Example Output

```markdown
## Foundation-Model Selection — Support Reply Drafting (GenAI)

### Criteria & Weights (use case: customer-facing, real-time-ish, high volume)
Quality on our tickets 30 · Latency 20 · Cost@volume 20 · Data terms 15 · Lock-in 10 · Support 5

### Scorecard (1–5; quality from our 200-ticket eval)
| Criterion | Wt | Vendor A (API) | Vendor B (API) | Open-weights (self-host) |
|---|---|---|---|---|
| Quality (our eval) | 30 | 4.5 | 4.2 | 3.8 |
| Latency | 20 | 4 | 3 | 4 (regional) |
| Cost@volume | 20 | 3 | 4 | 4 (after infra) |
| Data terms | 15 | 4 (no training) | 3 | 5 (in-house) |
| Lock-in | 10 | 2 | 2 | 4 |
| **Weighted** | | **3.8** | 3.5 | 4.0 |

### Cost at Volume (≈1.2M drafts/mo, ranges)
A: mid-five-figures/mo · B: low-five-figures/mo · Open-weights: infra-bound, ~B-range at this scale but higher ops.

### Data/Security/Viability
A: SOC2, no training on our data, US/EU regions. B: cheaper but reserves training rights — flag.
Open-weights: full control, but we own uptime + drift.

### Recommendation
**Open-weights (self-host)** narrowly leads on weighted score given data control and
lock-in, but only if we can staff ops. If ops capacity is the constraint, **Vendor A**.
Hedge: route all calls through an internal LLM-gateway abstraction so A↔open-weights is a config swap. Re-evaluate at 2× volume.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** criteria → eval → score dimensions → recommend.
- **RT-02 (Multi-Dimensional Analysis Framework):** weighted multi-criteria scorecard.
- **DS-06 (Prioritization & Severity Guidance):** ranked recommendation with switch conditions.
- **CM-02 (Constraint Specification):** hard constraints (residency, data terms) as disqualifiers.
- **NE-13 (Technical-to-Business Translation):** model differences rendered as cost/risk tradeoffs.

**Related Prompts:**
- `aipm_build_buy_partner_decision.md` — confirm "buy" before selecting a vendor.
- `aipm_model_risk_brief_for_execs.md` — brief leadership on the chosen model's risks.
- `aipm_ai_policy_authoring.md` — the policy the vendor usage must comply with.
