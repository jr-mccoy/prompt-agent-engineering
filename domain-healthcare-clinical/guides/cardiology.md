---
title: "Cardiology Guide"
category: healthcare-clinical/guides
description: "Cardiology routing guide: trigger phrases, the existing prompts to route first, when not to use this guide, and the required safety cautions and escalation boundaries."
techniques:
  - CM-03
  - CM-09
  - DS-36
  - IT-26
difficulty: intermediate
tags:
  - cardiology
  - anticoagulation
  - escalation
updated: "2026-10-06"
---

# Cardiology Guide

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
- "chest pain workup", "ACS rule-out", "troponin trend"
- "heart failure", "HFrEF", "HFpEF", "volume status", "GDMT titration"
- "atrial fibrillation", "rate vs rhythm", "CHA2DS2-VASc", "HAS-BLED"
- "syncope", "palpitations", "arrhythmia risk"
- "anticoagulation decisions", "DOAC vs warfarin"
- "cardiac risk stratification", "perioperative cardiac risk"

## Recommended Prompt Map (Existing + New)

### Existing prompts to route first
- `domain-healthcare-clinical/prompts/medicine_heart_failure_titration_advisor.md`
- `domain-healthcare-clinical/prompts/medicine_anticoagulation_decision_support.md`
- `domain-healthcare-clinical/prompts/medicine_emergency_triage_decision_support.md`
- `domain-healthcare-clinical/prompts/medicine_lab_diagnostic_interpreter.md`
- `domain-healthcare-clinical/prompts/medicine_clinical_decision_support.md`
- `domain-healthcare-clinical/prompts/medicine_drug_interaction_checker.md`
- `domain-healthcare-clinical/prompts/medicine_renal_hepatic_dose_adjustment.md`

### New prompts to add when repeated demand appears
- **Cardiology ACS Risk Stratifier Prompt** (HEART/TIMI-style framing + disposition options)
- **Arrhythmia Evaluation and Monitoring Prompt** (symptom timeline, trigger analysis, ambulatory monitoring options)
- **Valvular Disease Progression Review Prompt** (echo trend synthesis + follow-up timing)

## When Not to Use

Do **not** use this guide as primary routing when:
- The request is primarily psychiatric, behavioral, or psychotherapy-focused.
- The request is patient-facing direct medical advice without clinician mediation.
- The task requires real-time bedside emergency response rather than structured documentation or reasoning support.
- The dominant problem is non-cardiac (e.g., infectious source control, endocrine titration) and cardiology is secondary.

## Required Safety Cautions and Escalation Boundaries

- Treat all outputs as **clinical decision support**, not final medical decisions.
- Require explicit uncertainty language for diagnosis and disposition decisions.
- Always include immediate escalation triggers for:
  - ongoing ischemic chest pain
  - hemodynamic instability
  - malignant arrhythmia concern
  - syncope with high-risk features
- Never provide medication initiation or dose-change instructions without clinician oversight.
- Always prompt for contraindication checks (renal function, bleeding risk, drug-drug interactions, pregnancy when relevant).
- Escalate to cardiology/emergency evaluation when high-risk findings are present or data is incomplete for safe triage.

## False-Positive Prevention

When using this guide:

❌ **DON'T:**
- Route to a prompt-map path without confirming it resolves; the `prompts/medicine_*` paths listed above predate the domain's subfolders, so locate each file with `pae search` first.
- Pick this guide because a trigger phrase matched ("troponin trend", "CHA2DS2-VASc") when the case's dominant problem is non-cardiac; check the When Not to Use list against the case first.
- Treat the escalation cautions as covered because the routed prompt has some safety section; it must name all four triggers listed here.

✅ **DO:**
- Check that the routed prompt's output asks for the contraindication inputs this guide requires (renal function, bleeding risk, interactions, pregnancy) and mark any not supplied.
- Confirm that a risk score named in a trigger phrase (HEART, TIMI, CHA2DS2-VASc, HAS-BLED) is recomputed from its components in the output, not echoed from the request.
- Regard the "New prompts to add" entries as unbuilt; do not cite them as available resources.
