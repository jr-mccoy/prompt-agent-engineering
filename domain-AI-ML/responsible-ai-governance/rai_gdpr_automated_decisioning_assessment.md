---
title: "RAI GDPR Automated-Decisioning Assessment"
category: AI-ML/responsible-ai-governance
description: "Assess an automated decision-making/profiling system against GDPR Article 22 concepts — whether a decision is solely automated with legal/significant effect, lawful basis, safeguards, meaningful-information/explanation obligations, and data-subject rights — without inventing article numbers beyond Art. 22, fine amounts, or recital text."
techniques:
  - DS-01
  - ST-02
  - CM-02
  - QA-12
  - DS-06
difficulty: advanced
tags:
  - gdpr
  - article-22
  - automated-decision-making
  - data-subject-rights
  - responsible-ai
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_privacy_pii_assessment.md
  - domain-AI-ML/responsible-ai-governance/rai_explainability_plan.md
  - domain-AI-ML/responsible-ai-governance/rai_eu_ai_act_compliance_assessment.md
---

# RAI GDPR Automated-Decisioning Assessment

**Objective:** Assess an automated decision-making/profiling system against GDPR Article 22 concepts — determining whether a decision is "solely automated" with legal or similarly significant effect, identifying lawful basis, mapping the safeguards (human intervention, right to express a view, right to contest), the meaningful-information/explanation obligations, and data-subject rights — while requiring the user (and counsel) to confirm applicability and without inventing article numbers beyond the well-known Art. 22 framing, fine amounts, or recital text.

**When to Use:**
- To structure a first-pass review of whether and how Article 22 concepts apply to an automated decision system.
- To map existing safeguards (human review, contest mechanism, disclosures) onto the Article 22 obligation areas.
- To prepare materials for a Data Protection Officer or counsel to verify against the official text.

**When NOT to Use:**
- As legal advice — this is a structured pre-assessment; route conclusions to a DPO/counsel.
- As a substitute for qualified counsel or a data-protection specialist when binding obligations attach.
- For systems with no GDPR nexus or where the user has not confirmed applicability — confirm first.

## Inputs / Context

- **Decision description** — what is decided, who is affected, and the effect on the data subject.
- **Automation level** — whether a human is meaningfully involved or the decision is effectively solely automated.
- **Effect** — whether the decision produces legal effects or similarly significant effects.
- **Lawful basis & special categories** — the claimed basis; whether special-category data is processed.
- **Existing safeguards** — human-review path, mechanism to express a view/contest, transparency notices.
- **User-confirmed applicability** — GDPR nexus, controller/processor role, and version (ask; do not assume).

## Constraints

**Must:**
- Treat "solely automated" and "legal/similarly significant effect" as *threshold questions to confirm*, not determinations.
- Describe safeguard and information obligation *areas* (human intervention, express-a-view, contest, meaningful information about the logic) in general terms tied to the Article 22 framing.
- Separate evidenced safeguards from gaps and route conclusions to a DPO/counsel.

**Must Not:**
- NO-FABRICATION: never invent specific article numbers beyond the well-known Art. 22 framing, recital text, regulatory/statutory text, numeric thresholds, fine amounts, deadlines, or case citations from memory; the user confirms applicability and version; map the system to the regime's STRUCTURE and obligations at a conceptual level and explicitly flag any specific provision, fine, or threshold as "verify against the current official text."
- Declare the system "compliant" or "non-compliant," or assert a specific fine exposure — produce a gap assessment and route to counsel.
- Assume GDPR applies or that the decision is in scope of Article 22; confirm the thresholds with the user.

**Instructions:**

1. **Confirm applicability and role.** Establish the GDPR nexus and whether the organization is controller or processor. Mark unknowns as open legal questions.

2. **Test the "solely automated" threshold.** Assess whether human involvement is meaningful or nominal; a rubber-stamp human step may not take the decision out of scope. Treat as a candidate finding to confirm.

3. **Test the "legal/similarly significant effect" threshold.** Characterize the effect on the data subject and whether it plausibly meets the significant-effect bar — as a candidate to confirm.

4. **Identify lawful basis and special-category considerations.** Note the claimed basis and whether special-category data raises additional considerations, flagging these for counsel.

5. **Map safeguards.** For the safeguard areas — human intervention, the right to express a view, and the right to contest — state what mechanism exists today and what is missing.

6. **Assess meaningful-information / explanation obligations.** Evaluate whether the system can provide meaningful information about the logic involved and the significance/consequences, in a form a data subject can understand. Link to the explainability plan.

7. **Map data-subject rights and compile gaps.** Address access, rectification, objection/restriction as relevant; rank gaps by significance and effort and route to a DPO/counsel.

**Output Format:**

A markdown pre-assessment:
- **Applicability & Role** — GDPR nexus, controller/processor, open questions.
- **Threshold Findings** — solely-automated? significant-effect? (candidates to confirm).
- **Lawful Basis & Special Categories** — claimed basis; flags for counsel.
- **Safeguard Gap Table** — Area (general) | Mechanism present | Gap | Needs legal interpretation?
- **Meaningful-Information / Explanation** — capability present/missing.
- **Data-Subject Rights & Ranked Gaps** — significance × effort; route to DPO/counsel.
- **INSUFFICIENT EVIDENCE** — the correct threshold finding for "solely automated" where the human reviewer's actual behaviour is unknown. A human in the workflow does not settle it; a reviewer who confirms nearly every recommendation may not constitute meaningful involvement. Name the unblocking datum: override rate and time-per-case for the reviewing step.

## Verification

- [ ] GDPR applicability and controller/processor role are addressed (or flagged open).
- [ ] "Solely automated" and "significant effect" are presented as candidates to confirm.
- [ ] No article numbers beyond the Art. 22 framing, recital text, fine amounts, or thresholds are invented.
- [ ] Safeguard areas separate mechanism-present from gap.
- [ ] Meaningful-information/explanation capability is assessed.
- [ ] No "compliant/non-compliant" verdict or fine-exposure figure is asserted.
- [ ] The solely-automated threshold is marked INSUFFICIENT EVIDENCE unless the reviewer's override rate and time-per-case are known — the presence of a human step does not settle it.

## False-Positive Prevention

❌ **DON'T:**
- Quote a specific article (beyond the Art. 22 framing), recital, or a fine amount/percentage from memory — these must be verified against the official text.
- Conclude the decision is out of scope because a human "signs off," when the human role may be nominal.
- Treat a generic privacy notice as satisfying the meaningful-information-about-the-logic obligation.
- Declare the system "GDPR-compliant" or assert a specific penalty exposure.

✅ **DO:**
- Present the solely-automated and significant-effect thresholds as candidates to confirm with counsel.
- Distinguish a meaningful human intervention path from a rubber-stamp.
- Assess whether the system can explain the logic and consequences in an understandable form.
- Route all conclusions, fines, and provisions to a DPO/counsel for verification against the current official text.

## Example Output

```markdown
## GDPR Article 22 Pre-Assessment: Automated Loan-Decline Flow

### Applicability & Role
GDPR nexus: yes (EU data subjects). Role: controller. Open: processor obligations of the scoring vendor — verify.

### Threshold Findings
Solely automated: **candidate yes** — current human "review" appears nominal; confirm with counsel. Significant effect: **candidate yes** — credit decline plausibly significant; confirm.

### Lawful Basis & Special Categories
Claimed basis: contract necessity (per business). No special-category data identified. Flag for counsel to confirm basis adequacy for automated decisioning.

### Safeguard Gap Table
| Area (general) | Mechanism present | Gap | Needs legal? |
|---|---|---|---|
| Human intervention | "Review" step exists | Likely nominal; no real override workflow | Yes |
| Express a view | None | Mechanism missing | Yes |
| Contest the decision | Email channel | Not formalized or surfaced to subject | Yes |

### Meaningful-Information / Explanation
System can surface top decline drivers but not "the logic involved" in an understandable form. Gap — link to explainability plan.

### Data-Subject Rights & Ranked Gaps
1. Establish meaningful human intervention + contest workflow (high × moderate) — product + DPO.
2. Provide meaningful information about the logic (high × moderate) — DS + legal.
Route all to DPO/counsel for verification against the current official text.
```

**Techniques Used:**
- **DS-01 (Framework Application):** structures the review against Article 22 obligation areas.
- **ST-02 (Structured Sequential Instructions):** applicability → thresholds → basis → safeguards → information → rights.
- **CM-02 (Constraint Specification):** the no-invented-legal-text constraint governs the analysis.
- **QA-12 (False Positives Identification):** prevents fabricated articles/fines and premature compliance verdicts.
- **DS-06 (Prioritization & Severity Guidance):** ranks safeguard gaps by significance and effort.

**Related Prompts:**
- `rai_privacy_pii_assessment.md` — the broader privacy/PII review feeding lawful-basis analysis.
- `rai_explainability_plan.md` — supports the meaningful-information-about-the-logic obligation.
- `rai_eu_ai_act_compliance_assessment.md` — pair Article 22 analysis with AI Act exposure.
