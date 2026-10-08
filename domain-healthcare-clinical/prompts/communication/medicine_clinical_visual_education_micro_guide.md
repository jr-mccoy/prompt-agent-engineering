---
title: "Clinical Visual Education Micro-Guide"
category: healthcare-clinical/communication
description: "Brief framework for a clinical team to draft visual explainers for patient education or workflow handoffs, keeping clinical content and image-generation prompts consistent."
techniques:
  - ST-01
  - ST-03
  - RP-02
  - QA-01
difficulty: beginner
tags:
  - medicine
  - patient-education
  - communication
  - health-literacy
updated: "2026-10-06"
---

# Clinical Visual Education Micro-Guide

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

## Use When
- A clinical team needs visual explainers for patient education or workflow handoffs.
- You need consistency between clinical content and image-generation prompts.

## Prompt Starter
"Draft a clinically accurate visual-education brief for [topic] with target audience, essential safety points, must-show anatomy/process steps, plain-language labels, and what to avoid to prevent misunderstanding."

## False-Positive Prevention

❌ **DON'T:**
- Draw anatomy, device placement, or a procedure sequence from memory when the clinician's source material does not supply it — an inverted chamber, a wrong-side organ, or a swapped step order still reads as "clinically accurate labels" at a glance.
- Put a dose, a number of days, or a "call if above X" threshold into a label or caption unless it came from the supplied care plan; otherwise write `per your care team` in the caption.
- Tick "safety-critical warnings prominently called out" because a warning sentence exists somewhere in the brief, when the image prompt itself never places it in a visible slot.
- Use a picture that implies a result the text does not promise (a fully healed wound, a cleared artery) — patients read the image before the words.

✅ **DO:**
- Before running the Output Checklist, list every label and numbered step in the image brief and trace each one to a line of the clinician's source; mark anything untraceable `[VERIFY with clinician]`.
- Confirm each safety warning appears in both the plain-language text and a named panel or callout of the image prompt, and that the step order in the image matches the text.
- Record in the versioning note which clinician, which source document, and which date the visual was checked against.

## Output Checklist
- Audience and reading-level target
- Clinically accurate labels and sequence
- Safety-critical warnings prominently called out
- Versioning notes for clinician review

## Related Resources
- Healthcare image generation prompts
- [Patient communication skill](../../../domain-agentic-resources/skills/non-coding/healthcare/patient-communication/)
- [Health literacy rewriter skill](../../../domain-agentic-resources/skills/non-coding/healthcare/health-literacy-rewriter/)
