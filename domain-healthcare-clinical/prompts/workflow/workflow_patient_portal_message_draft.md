---
title: "Patient Portal Message Draft"
category: domain-healthcare-clinical/workflow
description: "Draft a safe, accurate, plain-language reply to a patient portal message — answering what can be answered async and escalating what can't, without over- or under-reacting."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - workflow
  - patient-communication
  - portal
  - health-literacy
updated: "2026-06-19"
---

## Objective

Draft a reply to a patient's portal message that is clinically appropriate, accurate, and readable — answering the question when async is safe, and converting to a phone call, visit, or ED referral when it isn't. The deliverable is a ready-to-send draft plus an explicit safety judgment about whether async is even the right channel. The first decision is always "should this be answered by message at all?"

## Inputs

- The patient's message verbatim
- Relevant chart context: active problems, current meds, recent visits/results, allergies
- What the patient is asking for (information, a refill, symptom advice, a result interpretation, a form)
- Practice constraints: what can be approved async vs. what requires a visit, scope of message-based care
- Patient factors: reading level, language preference

## Role

The clinician replying at the end of the day — efficient, but with a low threshold to pick up the phone when the message hints at something the chart can't resolve.

## Reasoning Steps

1. **Safety triage first — is async the right channel?** Scan for anything describing a potential emergency or acute deterioration (chest pain, dyspnea, neuro symptoms, severe pain, suicidal ideation, signs of sepsis). If present, the draft is not an answer — it's a directive to call the patient now or advise ED, and the reply should say so. Do not async-manage an emergency.

2. **Identify the real ask.** Patients often bury the question or ask the wrong one. "Is my blood pressure med. ok?" after a 150/95 reading is really "what do I do about this number?" Answer the underlying need.

3. **Check the chart before answering.** Pull the relevant result, med, or recent note. An accurate portal reply depends on what's actually in the record — don't answer a result question from the message alone.

4. **Decide the disposition:** (a) answer fully async; (b) answer async with a safety net ("do X, and if Y, call"); (c) convert to phone call; (d) bring in for a visit; (e) advise urgent/ED care. State which.

5. **Write the reply in plain language,** at the patient's reading level, warm and direct. Give the specific instruction (the dose, the timing, the threshold), not vague reassurance. Avoid jargon; keep medical terms only where they help.

6. **Include a clear safety net** in any symptom-related reply: the specific symptoms or thresholds that should prompt escalation, and how to reach care urgently.

7. **Don't overstep async limits.** New prescriptions for controlled substances, complex dose changes, or anything needing an exam generally shouldn't be finalized by message — note when to route to a visit instead.

8. **Verification pass.** Re-read the draft against the chart: is every clinical statement accurate, is the channel appropriate, and is there a safety net? Flag if the message needs the full chart or a colleague's eyes before sending.

## Output Format

```
CHANNEL JUDGMENT: [async OK / async + safety net / call patient / schedule visit / advise ED]
REASONING: [why this channel]

THE REAL ASK: [what the patient actually needs]

CHART CHECK: [relevant result/med/context confirmed]

DRAFT REPLY (to patient, plain language):
---
[ready-to-send message]
---

SAFETY NET INCLUDED: [the escalation threshold given to the patient]

DO NOT SEND IF: [any condition requiring chart review/colleague input first, or N/A]

VERIFICATION: [confirmation that clinical statements match the chart and channel is appropriate]
```

## Worked Example

**Input:** Portal message: "Hi, I started the new water pill (furosemide) last week for my leg swelling. The swelling is better but I've been feeling really dizzy when I stand up and my heart races. Should I keep taking it?" Chart: 72 y/o F, HFpEF, started furosemide 40 mg daily 8 days ago; also on lisinopril 20 mg and metoprolol. Last BP in clinic 118/70. No recent labs since starting diuretic.

**Output:**

```
CHANNEL JUDGMENT: Call patient (convert from async).
REASONING: Orthostatic dizziness + palpitations after starting a loop diuretic suggests possible volume depletion and/or electrolyte disturbance (hypokalemia from furosemide on top of HFpEF). This needs a same-day phone assessment and labs — not an async "keep taking it / stop it" reply. No labs have been checked since the diuretic started.

THE REAL ASK: "Are my new symptoms from the water pill, and should I change how I'm taking it?" — really a symptom-safety question, not a simple yes/no.

CHART CHECK: Furosemide 40 mg started 8 days ago; on lisinopril 20 + metoprolol; baseline BP 118/70 (so she has limited room before becoming hypotensive); no post-diuretic BMP on file.

DRAFT REPLY (to patient, plain language):
---
Thank you for letting me know — I'm glad the swelling is better, but the dizziness when you stand up and the racing heart are important and I want to check on them today. These can sometimes happen when the water pill removes a little too much fluid or changes your body's salts.

Please do this now:
1. Hold today's dose of furosemide (the water pill) until we talk.
2. Our office will call you today. If you can, check your blood pressure and pulse and have the numbers ready.
3. We'll likely have you get a quick blood test to check your kidney function and potassium.

Go to the ER or call 911 if you faint, have chest pain, or feel your heart racing with trouble breathing.

We'll call shortly.
---

SAFETY NET INCLUDED: Hold the diuretic, ER for syncope/chest pain/racing heart with dyspnea, office call same day.

DO NOT SEND IF: A colleague covering would prefer to phone immediately rather than message-then-call — given the symptoms, a direct phone call is the priority; this message should accompany, not replace, the call.

VERIFICATION: Recommendation to hold furosemide and check a BMP is consistent with a recently started loop diuretic + orthostatic symptoms + no follow-up labs. Channel correctly escalated from async to phone given symptom pattern.
```
