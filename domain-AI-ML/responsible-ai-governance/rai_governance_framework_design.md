---
title: "RAI Governance Framework Design"
category: AI-ML/responsible-ai-governance
description: "Design an AI governance framework — risk tiers, roles, review gates, and required documentation — proportionate to harm, without inventing regulatory obligations or adopting checkbox theater."
techniques:
  - DS-01
  - RT-02
  - CM-02
  - DS-06
  - RP-02
difficulty: advanced
tags:
  - ai-governance
  - risk-tiers
  - review-gates
  - accountability
  - responsible-ai
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_model_risk_assessment.md
  - domain-AI-ML/responsible-ai-governance/rai_ethics_review_protocol.md
  - domain-AI-ML/responsible-ai-governance/rai_eu_ai_act_compliance_assessment.md
---

# RAI Governance Framework Design

**Objective:** Design an AI governance framework that assigns risk tiers to AI use cases and attaches proportionate roles, review gates, and documentation to each tier — so oversight scales with potential harm and decisions are accountable, without imposing uniform bureaucracy or fabricating legal requirements.

**When to Use:**
- When an organization is standing up or revising AI oversight.
- When AI projects ship with inconsistent (or no) review.
- To map existing controls onto a recognized framework (NIST AI RMF, ISO/IEC 42001, internal) — ask the user which.

**When NOT to Use:**
- To assess a single model's risk — use `rai_model_risk_assessment.md`.
- To assess regulatory classification — use `rai_eu_ai_act_compliance_assessment.md`.

## Inputs / Context

- **AI footprint** — the kinds of AI use cases in scope (internal tooling, customer-facing decisions, high-stakes determinations).
- **Existing structures** — current review boards, MRM, security/privacy review, sign-off authorities.
- **Risk appetite & values** — what harms the organization most wants to prevent.
- **Reference framework** — NIST AI RMF, ISO/IEC 42001, sectoral standard, or internal (ask the user).
- **Regulatory exposure** — jurisdictions/regulations that may apply (ask the user; do not assume).

## Constraints

**Must:**
- Tie oversight intensity to a risk tier defined by potential harm and reversibility — not to model complexity alone.
- Assign clear accountable roles (who decides, who reviews, who can block) for each gate.
- Make documentation requirements proportionate: lightweight for low risk, rigorous for high risk.

**Must Not:**
- Invent statutory obligations or claim a framework is legally mandatory unless the user confirms the jurisdiction/regulation; if unknown, present the framework as best-practice and flag the legal mapping as unconfirmed.
- Design uniform heavy process for all use cases (kills low-risk velocity) or uniform light process (misses high-risk harm).
- Create review gates with no named owner or no authority to block.

**Instructions:**

1. **Confirm the reference framework and legal scope.** Ask which framework to align to and which regulations may apply; mark unknowns rather than assuming.

2. **Define risk tiers.** Establish 3–4 tiers by potential harm × reversibility × affected population × autonomy. Give each tier concrete examples from the org's footprint.

3. **Attach proportionate obligations per tier.** For each tier, specify required documentation (e.g., model card, risk assessment, bias audit), the review gate(s), and approval authority.

4. **Assign roles and RACI.** Name the accountable owner, reviewers, and who can block at each gate. Separate the building team from the approving authority for higher tiers.

5. **Define review gates in the lifecycle.** Place gates at meaningful points (problem framing, pre-training data review, pre-deployment, post-deployment monitoring) and state entry/exit criteria.

6. **Specify monitoring and re-review triggers.** Define ongoing monitoring obligations and the events (drift, incident, retrain, scope change) that force re-review.

7. **Add escalation and incident handling.** Define how concerns escalate, who owns incidents, and the rollback/kill authority.

8. **Pilot and proportionality check.** Recommend piloting on a few use cases and verify the framework doesn't impose high-tier burden on low-tier work.

**Output Format:**

A markdown framework document:
- **Scope & Reference Framework** (and unconfirmed legal items).
- **Risk Tiers** — table: Tier | Criteria | Examples | Required docs | Gates | Approver.
- **Roles & RACI** — accountable owner, reviewers, blockers.
- **Lifecycle Gates** — gate | trigger | entry/exit criteria.
- **Monitoring & Re-Review Triggers**.
- **Escalation & Incident Handling**.
- **Rollout Plan & Proportionality Check**.

## Verification

- [ ] Risk tiers are defined by harm/reversibility/population/autonomy, not complexity alone.
- [ ] Each tier has proportionate documentation and gates (light→heavy).
- [ ] Every gate has a named accountable owner and a blocking authority.
- [ ] Re-review triggers (drift, incident, retrain, scope change) are defined.
- [ ] Escalation and rollback/kill authority are specified.
- [ ] No legal obligation is asserted without user confirmation.

## False-Positive Prevention

❌ **DON'T:**
- Equate "deep learning" with "high risk" — a low-stakes internal classifier can be complex but low harm.
- Create a review board with no authority to actually block a launch.
- Apply the full high-risk documentation burden to every project.
- State a framework is "required by law" without confirming the jurisdiction.

✅ **DO:**
- Tier by potential harm and reversibility; place complex-but-harmless use cases low.
- Give each gate a named owner who can say no.
- Scale documentation to tier.
- Mark legal mappings as unconfirmed pending the user's jurisdiction.

## Example Output

```markdown
## AI Governance Framework (aligned to NIST AI RMF — internal adoption)

### Scope & Reference Framework
Covers all production AI. Reference: NIST AI RMF (voluntary, internal adoption). Legal mapping to sector regs: UNCONFIRMED — pending legal.

### Risk Tiers
| Tier | Criteria | Examples | Required docs | Gates | Approver |
|---|---|---|---|---|---|
| 1 Minimal | Internal, reversible, no person affected | Doc summarizer | README | Self-review | Team lead |
| 2 Moderate | Affects people, reversible | Ticket routing | Model card + monitoring plan | Pre-deploy review | ML manager |
| 3 High | Material effect on people, hard to reverse | Credit/hiring assist | Model card + bias audit + risk assessment | Pre-data + pre-deploy + quarterly | AI Review Board |
| 4 Critical | Safety/rights, autonomous | Autonomous denial | All Tier-3 + ethics review + external sign-off | All gates + kill switch | Board + Legal |

### Roles & RACI
Building team (R), Reviewers/ML manager (A at T2), AI Review Board (A at T3+, can block).

### Lifecycle Gates
Problem framing → pre-data review → pre-deploy → post-deploy monitoring. Exit criteria documented per tier.

### Monitoring & Re-Review Triggers
Drift beyond threshold, any incident, retrain, or scope expansion → re-review at the use case's tier.

### Escalation & Incident Handling
Any reviewer can escalate to the Board. Board holds rollback/kill authority for T3+.

### Rollout Plan & Proportionality Check
Pilot on 2 T2 and 1 T3 use case; confirm T1 work isn't burdened with T3 docs.
```

**Techniques Used:**
- **DS-01 (Framework Application):** aligns to NIST AI RMF / ISO 42001 structure.
- **RT-02 (Multi-Dimensional Analysis Framework):** tiers across harm/reversibility/population/autonomy.
- **CM-02 (Constraint Specification):** gates and authorities as governing constraints.
- **DS-06 (Prioritization & Severity Guidance):** proportionate obligations by tier.
- **RP-02 (Audience-Specific Framing):** RACI tailored to org roles.

**Related Prompts:**
- `rai_model_risk_assessment.md` — the per-model assessment the gates require.
- `rai_ethics_review_protocol.md` — the ethics gate for high tiers.
- `rai_eu_ai_act_compliance_assessment.md` — regulatory classification feeding tiering.
