---
title: "RAI FDA AI/ML SaMD Compliance Assessment"
category: AI-ML/responsible-ai-governance
description: "Assess an AI/ML-based Software-as-a-Medical-Device against FDA framework concepts — intended use/indications, risk categorization, Good Machine Learning Practice principles, and a Predetermined Change Control Plan for adaptive models — producing a readiness assessment and documentation gaps without inventing guidance numbers, clearance pathways, or thresholds."
techniques:
  - DS-01
  - ST-02
  - CM-02
  - QA-12
  - DS-06
difficulty: advanced
tags:
  - fda
  - samd
  - gmlp
  - pccp
  - responsible-ai
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_model_risk_assessment.md
  - domain-AI-ML/specialized-ml/computer-vision/cv_medical_imaging_considerations.md
  - domain-AI-ML/responsible-ai-governance/rai_model_card_authoring.md
---

# RAI FDA AI/ML SaMD Compliance Assessment

**Objective:** Assess an AI/ML-based Software-as-a-Medical-Device (SaMD) against FDA framework concepts — intended use/indications for use, risk categorization, Good Machine Learning Practice (GMLP) principles, and a Predetermined Change Control Plan (PCCP) for models that learn or update — producing a readiness assessment and documentation gaps, while requiring the user (and regulatory affairs) to confirm scope and without inventing specific guidance document numbers, clearance/submission pathways, or numeric thresholds.

**When to Use:**
- To structure a first-pass readiness review of an AI/ML SaMD before formal regulatory work.
- To map existing engineering, clinical, and quality documentation onto FDA framework concepts.
- To scope a Predetermined Change Control Plan for a model intended to update post-deployment.

**When NOT to Use:**
- As regulatory or clinical advice — this is a structured pre-assessment; consult regulatory affairs and FDA's current guidance.
- As a substitute for a qualified regulatory specialist or qualified counsel.
- For non-FDA jurisdictions or non-medical software — confirm the regulatory context first.

## Inputs / Context

- **Intended use & indications** — what the device is for, the condition, the population, the clinical claim.
- **User & environment** — clinician vs patient use; care setting; degree of autonomy in the clinical workflow.
- **Risk profile** — significance of information provided and seriousness of the health situation.
- **Model behavior** — locked vs adaptive/continuously-learning; update mechanism.
- **Existing documentation** — clinical evaluation, performance/validation data, quality system records, model card.
- **User-confirmed scope** — that this is an FDA-regulated device and the framework version applies (ask; do not assume).

## Constraints

**Must:**
- Anchor everything to the stated intended use / indications for use — risk and obligations flow from it.
- Describe GMLP principle *areas* and PCCP *components* in general terms tied to the framework's structure.
- Separate evidenced documentation from gaps and route conclusions to regulatory affairs.

**Must Not:**
- NO-FABRICATION: never invent specific guidance document numbers/titles, clearance or submission pathway names, classification codes, statutory/regulatory text, numeric thresholds, dollar amounts, or deadlines from memory; the user confirms which framework and version applies; map the device to the framework's STRUCTURE and obligations at a conceptual level and explicitly flag any specific document, pathway, or threshold as "verify against FDA's current guidance."
- Declare the device "cleared," "approved," or "compliant" — produce a readiness/gap assessment and route to regulatory affairs.
- Assume the device is FDA-regulated or guess its risk category; confirm with the user.

**Instructions:**

1. **Confirm scope and framework version.** Establish that this is an FDA-regulated SaMD and which framework version the user is working from. Mark unknowns as open regulatory questions.

2. **Define intended use & indications.** Restate the intended use, target condition, population, and clinical claim precisely — all downstream analysis depends on it.

3. **Propose a candidate risk categorization.** Based on the significance of the information and seriousness of the situation, propose a *candidate* risk level and explicitly route confirmation to regulatory affairs. Do not assign classification codes from memory.

4. **Map GMLP principle areas.** Walk the GMLP principle areas generically (e.g., data representativeness, reference standard quality, model design appropriate to clinical context, robust validation, transparency to users, monitoring of real-world performance). Note evidence and gaps.

5. **Assess the change-control posture (PCCP).** Determine whether the model is locked or adaptive. If adaptive, outline the PCCP components conceptually (the types of planned modifications, the protocol/methods for making them, and the impact assessment) and flag gaps. Do not quote required content from memory.

6. **Compile documentation gaps.** For each area, separate what exists from what is missing.

7. **Rank gaps and route to regulatory affairs.** Prioritize by significance and effort; mark items needing regulatory or clinical interpretation.

**Output Format:**

A markdown readiness assessment:
- **Scope & Framework Version** — FDA nexus, framework version, open questions.
- **Intended Use & Indications** — precise restatement.
- **Candidate Risk Categorization** — proposed level + "confirm with regulatory affairs" note.
- **GMLP Area Gap Table** — Principle area (general) | Evidence present | Gap | Needs regulatory interpretation?
- **Change-Control / PCCP Posture** — locked vs adaptive; PCCP components present/missing.
- **Ranked Gaps & Handoff** — significance × effort; route to regulatory affairs.
- **INSUFFICIENT EVIDENCE** — the correct state of the candidate risk categorization until the intended-use statement is final. Categorization follows from intended use and healthcare-situation significance, so an assessment built on a draft intended use is provisional throughout. Name the unblocking datum: the finalized intended-use and indications statement, confirmed with regulatory affairs.

## Verification

- [ ] FDA scope and framework version are confirmed (or flagged open).
- [ ] Intended use / indications are restated precisely and drive the analysis.
- [ ] Risk categorization is a candidate routed to regulatory affairs, not asserted.
- [ ] No guidance document numbers, pathway names, classification codes, or numeric thresholds are invented.
- [ ] Locked vs adaptive status is determined and PCCP components addressed for adaptive models.
- [ ] No "cleared/approved/compliant" verdict is issued.
- [ ] The risk categorization is marked INSUFFICIENT EVIDENCE while the intended-use statement is still in draft, and the GMLP gap table is flagged as conditional on it.

## False-Positive Prevention

❌ **DON'T:**
- Name a specific guidance document, submission pathway, or classification code from memory — these must be verified against FDA's current guidance.
- Declare the device "510(k)-clearable," "approved," or "compliant" — that is a regulatory determination, not an engineering one.
- Treat a continuously-learning model as if a locked model's documentation suffices — adaptive models raise distinct change-control obligations.
- Assert a clinical-performance or sensitivity/specificity threshold the framework "requires."

✅ **DO:**
- Anchor risk and obligations to the precise intended use / indications.
- Describe GMLP and PCCP areas generically and flag specifics for verification against FDA's current guidance.
- Distinguish locked vs adaptive models and scope a PCCP for adaptive ones.
- Route all conclusions to regulatory affairs and qualified specialists.

## Example Output

```markdown
## FDA AI/ML SaMD Readiness Assessment: Diabetic-Retinopathy Screening Tool

### Scope & Framework Version
FDA-regulated SaMD: yes (user-confirmed). Framework version: current (user-confirmed). Open: whether a sector-specific guidance also applies — verify.

### Intended Use & Indications
Intended to screen retinal fundus images for referable diabetic retinopathy in adults in primary-care settings; outputs a refer/no-refer recommendation to a clinician.

### Candidate Risk Categorization
Candidate: higher-risk (screening influences referral for a serious condition). CONFIRM WITH REGULATORY AFFAIRS — not asserted here.

### GMLP Area Gap Table
| Principle area (general) | Evidence present | Gap | Needs regulatory? |
|---|---|---|---|
| Data representativeness | Training-set demographics documented | Limited darker-skin/comorbidity coverage | Some |
| Reference standard quality | Graded by ophthalmologists | Inter-grader agreement not reported | No |
| Validation rigor | Held-out test performance | No prospective/site-diversity study | Yes |
| Transparency to users | Clinician-facing labeling draft | Performance-by-subgroup not surfaced | Yes |
| Real-world monitoring | None | Post-deployment performance plan missing | Yes |

### Change-Control / PCCP Posture
Model: locked at release, retraining planned quarterly → adaptive intent. PCCP components: modification types (drafted), protocol/methods (missing), impact assessment (missing). Gaps significant.

### Ranked Gaps & Handoff
1. Prospective/multi-site validation (high × high) — regulatory affairs.
2. PCCP protocol + impact assessment (high × moderate) — regulatory + ML.
3. Subgroup performance in labeling (moderate × low) — clinical + regulatory.
Route all to regulatory affairs for verification against FDA's current guidance.
```

**Techniques Used:**
- **DS-01 (Framework Application):** structures the review against intended use, risk, GMLP, and PCCP concepts.
- **ST-02 (Structured Sequential Instructions):** scope → intended use → risk → GMLP → change control → gaps → handoff.
- **CM-02 (Constraint Specification):** the no-invented-guidance constraint governs the analysis.
- **QA-12 (False Positives Identification):** prevents fabricated guidance numbers, pathways, and premature clearance verdicts.
- **DS-06 (Prioritization & Severity Guidance):** ranks documentation gaps by significance and effort.

**Related Prompts:**
- `rai_model_risk_assessment.md` — the risk assessment feeding intended-use and validation evidence.
- `cv_medical_imaging_considerations.md` — imaging-specific validation and data concerns for image-based SaMD.
- `rai_model_card_authoring.md` — supplies the transparency/labeling documentation evidence.
