---
title: "Psychiatry Guide"
category: healthcare-clinical/guides
description: "Psychiatry routing guide: trigger phrases, the existing prompts to route first, when not to use this guide, and the required safety cautions and escalation boundaries."
techniques:
  - CM-03
  - CM-09
  - DS-36
  - IT-26
difficulty: intermediate
tags:
  - psychiatry
  - escalation
updated: "2026-10-06"
---

# Psychiatry Guide

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
- "psychiatric assessment", "mental status exam", "diagnostic clarification"
- "suicide risk", "self-harm", "homicidal ideation", "safety planning"
- "mania", "psychosis", "catatonia", "capacity evaluation"
- "substance use with psychiatric symptoms", "withdrawal risk"
- "medication adherence", "side effect burden", "shared decision-making in psych meds"

## Recommended Prompt Map (Existing + New)

### Existing prompts to route first
- `domain-healthcare-clinical/prompts/medicine_psychiatric_assessment_support.md`
- `domain-healthcare-clinical/prompts/medicine_addiction_medicine_assessment.md`
- `domain-healthcare-clinical/prompts/medicine_goals_of_care_conversation_guide.md`
- `domain-healthcare-clinical/prompts/medicine_clinical_decision_support.md`
- `domain-healthcare-clinical/prompts/medicine_drug_interaction_checker.md`
- `domain-healthcare-clinical/prompts/medicine_clinical_documentation.md`

### New prompts to add when repeated demand appears
- **Acute Psychiatric Risk Stratification Prompt** (self-harm/violence risk factors + protective factors)
- **Complex Psychopharmacology Review Prompt** (polypharmacy burden, side-effect-risk balancing)
- **Capacity and Consent Evaluation Prompt** (decision-specific capacity framework)

## When Not to Use

Do **not** use this guide as primary routing when:
- The request is psychotherapy technique coaching better suited to psychology-focused domains.
- The need is immediate emergency intervention rather than structured assessment support.
- The request asks for direct instructions to a patient in active crisis without licensed clinician involvement.
- The main task is non-psychiatric medical stabilization.

## Required Safety Cautions and Escalation Boundaries

- Always treat outputs as adjunctive and require licensed clinician judgment.
- Include immediate escalation instructions for:
  - active suicidal intent/plan or inability to maintain safety
  - active homicidal intent or escalating violence risk
  - severe psychosis, delirium concern, or inability to care for self
- Avoid deterministic language about diagnosis; require differential framing and uncertainty acknowledgment.
- Never provide medication start/stop/titration directives without supervising prescriber oversight.
- Require emergency pathway activation (local crisis resources/ED/emergency services) for imminent safety risks.

## False-Positive Prevention

When using this guide:

❌ **DON'T:**
- Route by the prompt-map paths as listed; the assessment and addiction prompts now sit in `prompts/specialty/` and the others in sibling subfolders, so confirm each path first.
- Accept "low risk" in the routed output on the strength of no stated plan; the output must list which risk and protective factors were actually asked about and which were not.
- Let the output state a mental status or capacity finding the input does not contain; capacity is decision-specific and needs the decision named.

✅ **DO:**
- Check that each escalation trigger in this guide (intent or plan, homicidal intent, severe psychosis or delirium, inability to care for self) is addressed or marked "not assessed".
- Verify that medical and substance causes (delirium, intoxication, withdrawal) are screened in the output before a psychiatric attribution is made.
- Confirm crisis instructions name the local pathway the clinician supplied rather than a generic placeholder.
