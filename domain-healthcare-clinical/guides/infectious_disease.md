---
title: "Infectious Disease Guide"
category: healthcare-clinical/guides
description: "Infectious disease routing guide: trigger phrases, the existing prompts to route first, when not to use this guide, and the required safety cautions, stewardship guardrails and escalation boundaries."
techniques:
  - CM-03
  - CM-09
  - DS-36
  - IT-26
difficulty: intermediate
tags:
  - infectious-disease
  - antibiotics
  - escalation
updated: "2026-10-06"
---

# Infectious Disease Guide

> **Medical disclaimer — read before use.** This prompt is a decision-support and
> teaching aid for **licensed clinicians**. It is **not medical advice** and is not for
> patients to diagnose or treat themselves. Drug doses, thresholds and guideline
> references in it and in its worked example may be incomplete, outdated or wrong:
> verify each one against the current guideline, the product label and your local
> formulary, and follow your institution's protocols. It does not replace examination
> or clinical judgment. **Medical emergency: call your local emergency number (911 in
> the US).**
>
> **Review status:** AI-assisted content, reviewed by AI only (2026-10-06);
> **not yet reviewed by a licensed clinician.**

## Trigger Phrases

Use this guide when requests include terms like:
- "sepsis", "septic shock", "lactate", "source control"
- "antibiotic selection", "de-escalation", "broad-spectrum coverage"
- "culture interpretation", "blood cultures", "resistance pattern"
- "antimicrobial stewardship", "duration of therapy"
- "hospital-acquired infection", "MDRO", "infection prevention"

## Recommended Prompt Map (Existing + New)

### Existing prompts to route first
- `domain-healthcare-clinical/prompts/medicine_sepsis_recognition_framework.md`
- `domain-healthcare-clinical/prompts/medicine_antibiotic_stewardship_advisor.md`
- `domain-healthcare-clinical/prompts/medicine_lab_diagnostic_interpreter.md`
- `domain-healthcare-clinical/prompts/medicine_drug_interaction_checker.md`
- `domain-healthcare-clinical/prompts/medicine_renal_hepatic_dose_adjustment.md`
- `domain-healthcare-clinical/prompts/medicine_clinical_decision_support.md`

### New prompts to add when repeated demand appears
- **ID Syndrome-Based Empiric Therapy Prompt** (site-specific differential + local resistance context)
- **Culture De-escalation Decision Prompt** (timeline-to-culture synthesis + narrowing strategy)
- **Outbreak/Cluster Investigation Prompt** (case definition, exposure mapping, control actions)

## When Not to Use

Do **not** use this guide as primary routing when:
- The task is purely non-clinical policy writing without patient-care implications.
- The request is a one-off patient education rewrite with no infectious decision-making component.
- The main need is psychiatric crisis assessment or cardiology hemodynamics.
- The user asks for direct patient-specific prescribing without licensed clinician review.

## Required Safety Cautions and Escalation Boundaries

- Never present empiric antibiotic choices as definitive treatment recommendations.
- Require red-flag escalation language for:
  - hypotension or organ dysfunction consistent with sepsis/shock
  - concern for meningitis, necrotizing infection, or rapidly progressive illness
  - immunocompromised hosts with instability
- Force explicit checks for allergies, renal/hepatic function, drug interactions, and pregnancy/lactation when relevant.
- Include stewardship guardrails: reassess at 24–72 hours, narrow by cultures, justify duration.
- Escalate to urgent ID/emergency care when severe infection signals, diagnostic uncertainty with deterioration, or high-risk host factors are present.

## False-Positive Prevention

When using this guide:

❌ **DON'T:**
- Take a prompt-map path at face value; sepsis recognition now lives under `prompts/acute-care/` and stewardship under `prompts/pharmacology/`, so confirm every path before routing.
- Accept an empiric regimen from the routed prompt that was chosen without the local antibiogram or the patient's prior cultures; "covers the likely organisms" is not a check.
- Read a positive culture as infection without the specimen type, its collection time relative to the first antibiotic dose, and contaminant likelihood (e.g. one coagulase-negative staphylococcus bottle out of two).

✅ **DO:**
- Check that the output names a reassessment point inside this guide's 24–72 h window and the culture result that would trigger narrowing.
- Verify the allergy entry carries its reaction type, and that renal or hepatic dose adjustments are computed from values actually supplied.
- Confirm any stated duration of therapy has a source-control status and a named day 1.
