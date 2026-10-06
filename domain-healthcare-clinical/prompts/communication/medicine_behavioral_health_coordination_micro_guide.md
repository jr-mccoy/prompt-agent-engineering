---
title: "Behavioral Health Coordination Micro-Guide"
category: healthcare-clinical/communication
description: "Brief framework for a clinician to coordinate medical and behavioral health plans, giving the team a shared structure for risk, follow-up, and communication."
techniques:
  - ST-01
  - ST-03
  - QA-04
difficulty: beginner
tags:
  - medicine
  - mental-health
  - care-coordination
  - communication
updated: "2026-10-06"
---

# Behavioral Health Coordination Micro-Guide

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
- A clinician needs a brief framework to coordinate medical and behavioral health plans.
- A team needs a shared structure for risk, follow-up, and communication.

## Prompt Starter
"Create a concise behavioral-health coordination note with: presenting concerns, immediate safety considerations, medical-psychiatric interaction risks, care-team handoffs, and next-visit checkpoints. Keep uncertainty explicit and include escalation triggers."

## False-Positive Prevention

❌ **DON'T:**
- Fill "safety considerations" with a generic risk-factor list or a risk level ("low suicide risk") that no documented assessment supports — state what the patient or chart actually shows and route risk formulation to a full psychiatric assessment.
- List medical–psychiatric interaction risks (QTc, lithium with NSAIDs/ACEi, serotonergic combinations, sedative stacking) that are not backed by two drugs or a condition actually present in the input.
- Assign follow-up items to a role ("the team", "BH") with no named owner and due date — the team-ownership checklist line is not met by a role.

✅ **DO:**
- Before running the Output Checklist, count each follow-up item for owner + date + escalation trigger, and trace each interaction risk to the medication list.
- Take escalation routes and crisis resources from the facility's protocol `[per facility protocol]` instead of inventing phone numbers or services.
- Check the plain-English summary keeps every escalation trigger and pending item from the clinician version.

## Output Checklist
- Safety factors and escalation conditions
- Integrated medical + behavioral considerations
- Team ownership for each follow-up item
- Patient-centered language and plain-English summary

## Related Resources
- [Psychology domain resources](../../../domain-psychology/)
- Healthcare non-coding skills
- [Psychiatric assessment support prompt](../specialty/medicine_psychiatric_assessment_support.md)
