---
title: "Specialty Consult Question Composer"
category: domain-healthcare-clinical/workflow
description: "Turn a vague 'please see this patient' into a focused, answerable consult question with the exact data the specialist needs to answer it."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - workflow
  - referral
  - consultation
  - care-coordination
updated: "2026-06-19"
---

## Objective

Convert a referring clinician's intent into a sharp consult request: a single answerable question, the focused clinical context that bears on it, the specific data the consultant will want in hand, and the urgency. A good consult question gets a usable answer on the first pass; a vague one ("eval and treat") generates a wasted visit and a recommendation that misses the point. This applies to both inpatient curbside/formal consults and outpatient referrals.

## Inputs

- The clinical problem prompting the consult and what the referring clinician actually wants to know
- The specialty being consulted
- Relevant history, exam, labs, imaging, and prior workup already done
- What has already been tried (so the consultant doesn't repeat it)
- Urgency and setting (inpatient stat vs. inpatient routine vs. outpatient referral)
- Any specific decision the answer will drive (clearance for surgery, start/stop a drug, procedure candidacy)

## Role

Referring attending writing the consult you would want to receive — specific enough to answer, complete enough to answer without a chart safari.

## Reasoning Steps

1. **Name the actual question.** Force it into one sentence ending in a question mark. "Is this patient a candidate for ablation?" "What is the target INR given the new GI bleed?" "Does this rash represent a drug reaction requiring discontinuation of the antibiotic?" If you can't write the sentence, the consult isn't ready — the referring clinician needs to decide what they're asking.

2. **Classify the consult type,** because it changes what the consultant needs: (a) **diagnostic** — help me figure out what this is; (b) **management** — I have the diagnosis, optimize the treatment; (c) **procedural** — is this patient a candidate for X; (d) **clearance/risk** — is it safe to proceed with Y. Each demands different supporting data.

3. **Assemble only the bearing data.** A cardiology pre-op consult needs functional capacity, cardiac history, the surgery and its risk class, current meds, recent ECG/echo — not the patient's colonoscopy history. Curate to the question; over-inclusion buries the signal.

4. **State what's already been done.** Workup completed, treatments tried and their results. This prevents the consultant from re-ordering the same tests and signals where the referring team has hit the edge of their comfort.

5. **Specify the decision the answer enables.** "We will proceed to surgery Monday if cleared" tells the consultant the stakes and timeline far better than "pre-op eval." It also lets them tailor the answer to be actionable.

6. **Set urgency honestly.** Stat means the patient is unstable or a time-critical decision hinges on the answer. Most consults are routine; mislabeling everything stat erodes the signal. State the timeframe in which the answer is useful.

7. **Pre-empt the predictable follow-up question.** Experienced consultants always ask one thing back (the med list, the last imaging, the goals of care). Include it up front.

## Output Format

```
CONSULT TO: [specialty] | SETTING: [inpatient stat/routine | outpatient] | TIMEFRAME: [when answer is needed]

CONSULT QUESTION (one sentence): [the answerable question]

CONSULT TYPE: [diagnostic / management / procedural / clearance-risk]

DECISION THIS ENABLES: [what the referring team will do with the answer]

FOCUSED CONTEXT:
- [the bearing history, exam, and problem framing — curated to the question]

RELEVANT DATA (with dates):
- [labs, imaging, ECG/echo, path — only what bears on the question]

ALREADY DONE:
- Workup: [completed studies + results]
- Tried: [treatments + response]

ANTICIPATED FOLLOW-UP (answered up front):
- [the thing the consultant will ask back: med list, code status, last study, etc.]
```

## Worked Example

**Input:** Hospitalist wants GI to weigh in. 64 y/o M admitted with melena and Hgb drop from 13 to 8.5, hemodynamically stable after 2 units PRBC. On apixaban for AFib. The hospitalist wants to know about scope timing and whether/when to resume anticoagulation.

**Output:**

```
CONSULT TO: Gastroenterology | SETTING: Inpatient, routine (stable post-transfusion) | TIMEFRAME: EGD planning within 24 h

CONSULT QUESTION: In a stable patient with an acute upper GI bleed on apixaban, what is the recommended timing for EGD, and what is your guidance on holding vs. resuming anticoagulation peri-endoscopy?

CONSULT TYPE: Procedural + management.

DECISION THIS ENABLES: We will schedule EGD per your timing recommendation and follow your anticoagulation plan; AFib stroke risk (CHA2DS2-VASc 4) makes the resume-timing decision the crux.

FOCUSED CONTEXT:
- 64 y/o M, melena x1 day, no hematemesis. Hemodynamically stable now (HR 78, BP 124/72) after 2 U PRBC. No NSAID use, no prior ulcer or varices known. No stigmata of chronic liver disease.

RELEVANT DATA (with dates):
- Hgb 13.0 (baseline, 1 mo ago) → 8.5 on admission → 9.2 post-transfusion (today).
- Apixaban 5 mg BID, last dose ~18 h ago. Cr 1.0, normal LFTs, platelets 210, INR not applicable (DOAC).
- AFib, CHA2DS2-VASc 4, HAS-BLED 3.

ALREADY DONE:
- 2 U PRBC, IV PPI infusion started, apixaban held, type & screen active, NPO.
- No EGD yet.

ANTICIPATED FOLLOW-UP (answered up front):
- Code status: full. No DOAC reversal given (stable, controllable). Goals: would like to resume stroke prophylaxis as early as bleeding risk allows given high CHA2DS2-VASc. Last apixaban dose timed above.
```
