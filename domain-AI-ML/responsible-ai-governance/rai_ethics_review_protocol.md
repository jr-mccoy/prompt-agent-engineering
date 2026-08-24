---
title: "RAI Ethics Review Protocol"
category: AI-ML/responsible-ai-governance
description: "Design an ethics review protocol for an AI project — stakeholder impact, consent, recourse, and oversight — that produces accountable decisions rather than a values-statement rubber stamp."
techniques:
  - ST-02
  - RT-02
  - RP-02
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - ethics-review
  - stakeholder-impact
  - consent
  - recourse
  - oversight
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_governance_framework_design.md
  - domain-AI-ML/responsible-ai-governance/rai_model_risk_assessment.md
  - domain-AI-ML/responsible-ai-governance/rai_explainability_plan.md
---

# RAI Ethics Review Protocol

**Objective:** Design an ethics review protocol that surfaces stakeholder impacts, examines consent and data-use legitimacy, defines recourse and contestability for affected people, and establishes meaningful human oversight — producing an accountable, documented decision rather than a checkbox endorsement of stated values.

**When to Use:**
- For consequential AI projects, as the ethics gate in a governance process.
- When a project affects vulnerable populations or involves sensitive data/decisions.
- When existing "ethics review" is a values statement with no decision or recourse.

**When NOT to Use:**
- For the technical risk register — use `rai_model_risk_assessment.md`.
- For the overall governance structure — use `rai_governance_framework_design.md`.

## Inputs / Context

- **Project & purpose** — what is built, why, and the intended benefit (and who benefits).
- **Stakeholders** — affected people (incl. non-users and vulnerable groups), operators, the organization, society.
- **Data & consent basis** — how data was obtained, whether subjects consented to this use, sensitivity.
- **Decision impact** — what the system decides about people, reversibility, and existing recourse.
- **Oversight** — current human role, override ability, accountability for outcomes.
- **Regulation/framework in scope** — if any (ask the user; do not assume).

## Constraints

**Must:**
- Identify stakeholders beyond direct users, including those who can't opt out and vulnerable groups.
- Require a recourse/contestability mechanism for adverse automated decisions, or document its absence as a gap.
- Produce an accountable decision (proceed / conditions / do not proceed) with named owners and dissent recorded.

**Must Not:**
- Conclude a project is "ethical" because it aligns with stated values — assess concrete impacts, consent, and recourse.
- Treat "users agreed to the ToS" as blanket consent for any data use; examine whether consent covers this specific use.
- Invent legal consent or anti-discrimination requirements; ask the user for the jurisdiction and route legal questions to counsel.

**Instructions:**

1. **State purpose and beneficiary.** Record what the project does, the claimed benefit, and who actually benefits vs who bears the risk.

2. **Map stakeholders and impacts.** List affected parties — including non-users, those who can't opt out, and vulnerable groups — and the plausible benefits and harms to each.

3. **Examine consent and data legitimacy.** Assess whether the data's original collection consent covers this use, whether subjects could reasonably expect it, and whether sensitive data needs heightened justification.

4. **Assess recourse and contestability.** For adverse decisions, define how a person learns of the decision, contests it, and reaches a human — or flag the absence as a gap to fix.

5. **Define meaningful human oversight.** Specify the human role: real ability to review/override with time and information, not nominal sign-off; guard against automation bias.

6. **Surface value tensions.** Name tradeoffs (e.g., personalization vs privacy, accuracy vs fairness, scale vs scrutiny) and how the project resolves them.

7. **Reach an accountable decision.** Recommend proceed / proceed-with-conditions / do-not-proceed, name the accountable decision-maker, and record dissenting views.

8. **Set re-review triggers.** Define what changes (scope, population, incident) reopen the ethics review.

**Output Format:**

A markdown ethics review:
- **Purpose & Beneficiary Analysis** — benefit vs risk-bearer.
- **Stakeholder Impact Map** — table: Stakeholder | Benefits | Harms | Can opt out? | Vulnerable?
- **Consent & Data Legitimacy** — assessment + gaps.
- **Recourse & Contestability** — mechanism or documented gap.
- **Human Oversight Design** — role, authority, automation-bias guard.
- **Value Tensions & Resolution**.
- **Decision** — proceed/conditions/no + accountable owner + recorded dissent.
- **Re-Review Triggers**.
- **INSUFFICIENT EVIDENCE** — an available decision alongside proceed / conditions / no. Use it where the review reasoned *about* an affected group without input *from* one, and name the unblocking datum: which stakeholder group must be consulted and on which specific question. A review that infers what a vulnerable group would accept has not established it.

## Verification

- [ ] Stakeholders include non-users, those who can't opt out, and vulnerable groups.
- [ ] Consent assessment examines this specific use, not blanket ToS.
- [ ] A recourse mechanism is defined or its absence documented as a gap.
- [ ] Human oversight is meaningful (information + time + authority), not nominal.
- [ ] An accountable decision with named owner and recorded dissent is produced.
- [ ] Legal questions are routed to counsel under a confirmed jurisdiction.
- [ ] Where an affected group was reasoned about but not consulted, the decision is INSUFFICIENT EVIDENCE naming the group and the question — not a proceed inferred on their behalf.

## False-Positive Prevention

❌ **DON'T:**
- Conclude "ethical" because the project matches the company's values poster.
- Treat ToS acceptance as consent for an unforeseen new use of the data.
- Call a rubber-stamp sign-off "human oversight."
- Ignore people who are affected but never agreed to be (non-users).

✅ **DO:**
- Assess concrete benefits/harms per stakeholder, including non-users.
- Examine whether consent actually covers this use.
- Require oversight with real review authority and automation-bias guards.
- Produce an owned, documented decision with dissent recorded.

## Example Output

```markdown
## Ethics Review: Proactive Churn-Intervention Targeting

### Purpose & Beneficiary Analysis
Targets at-risk customers with retention offers. Benefit: company revenue + some customers get better deals. Risk-bearers: customers excluded from offers (price discrimination concern).

### Stakeholder Impact Map
| Stakeholder | Benefits | Harms | Opt out? | Vulnerable? |
|---|---|---|---|---|
| Targeted customers | Discounts | Manipulation risk | No | Some (financially stressed) |
| Non-targeted customers | — | Pay more for same service | No | Possibly |
| Company | Retention | Reputational risk | n/a | n/a |

### Consent & Data Legitimacy
Behavioral data collected under ToS for "service improvement." Using it for differential pricing likely exceeds reasonable expectation — gap; needs legal + possibly fresh consent.

### Recourse & Contestability
Currently none. Gap: customers can't know or contest why they were/weren't offered a deal. Fix: transparency + opt-out before launch.

### Human Oversight Design
Marketing reviews segment definitions monthly; add a fairness check on who is systematically excluded.

### Value Tensions & Resolution
Revenue vs fairness in pricing. Resolution: prohibit using sensitive-proxy features for targeting; audit exclusion patterns.

### Decision
Proceed-with-conditions: legal review of consent, exclusion-fairness audit, customer transparency/opt-out. Owner: VP Growth. Dissent: one reviewer favors do-not-proceed pending consent clarity (recorded).

### Re-Review Triggers
Expansion to new data sources or to vulnerable-segment targeting.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** purpose → stakeholders → consent → recourse → oversight → decision.
- **RT-02 (Multi-Dimensional Analysis Framework):** impacts across stakeholders and value tensions.
- **RP-02 (Audience-Specific Framing):** tailors recourse and oversight to affected parties.
- **DS-06 (Prioritization & Severity Guidance):** weighs harms and conditions.
- **QA-12 (False Positives Identification):** blocks values-statement and ToS-as-consent fallacies.

**Related Prompts:**
- `rai_governance_framework_design.md` — the gate this protocol serves.
- `rai_model_risk_assessment.md` — technical risks complementing ethical ones.
- `rai_explainability_plan.md` — the explanations that enable recourse.
