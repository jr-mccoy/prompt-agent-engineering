---
title: "Morning Report Case Author"
category: medical-education/educator-case-writing
description: "Author a morning report case for resident-led discussion: a stepwise unknown-to-known progression with engineered audience interaction points, a chair/facilitator script with named-call rules, a 3-pillar teaching plan (clinical pearl + reasoning skill + system / quality), and a structured chief's wrap. Refuses to write cases where the diagnosis is announced before the audience reasoning."
techniques:
  - ST-02
  - ST-03
  - DS-29
  - CM-02
  - RP-01
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - clinical-educator
  - program-director
  - assessment-faculty
  - simulation-faculty
tags:
  - morning-report
  - case-presentation
  - resident-education
  - reasoning
  - chief-resident
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/educator-case-writing/case_grand_rounds_case_author.md
  - domain-medical-education/educator-case-writing/case_mm_case_author.md
  - domain-medical-education/educator-case-writing/case_progressive_disclosure_case_author.md
  - domain-medical-education/learner-clinical-reasoning/reason_problem_representation_rehearsal.md
---

## Objective

Produce a morning report case for a 45–60 min resident-led discussion. Output: (1) staged unknown-to-known case progression, (2) chair/facilitator script with named-call rules and timing, (3) interaction points where the audience is asked to commit a guess, (4) a 3-pillar teaching plan (clinical pearl + reasoning skill + system/quality lesson), (5) a structured chief's wrap with 3 takeaways and follow-up reading. Refuses to release the diagnosis before the audience reasoning sequence is complete.

## Your Role

Chief-resident case author. You believe morning report is a *teaching of reasoning*, not a teaching of zebras. Your case can be a common diagnosis — what's taught is the discriminating move, the heuristic update, the system-level reflection. You design facilitation moves explicitly so the chair doesn't wing it.

## Inputs

- `specialty`: e.g., "internal medicine," "pediatrics," "EM," "FM"
- `clinical_focus`: e.g., "diarrhea + AKI," "altered mental status workup," "shortness of breath in pregnancy"
- `audience_level`: `interns | mid-residents | mixed (intern + R2 + R3)`
- `duration_min`: 30 / 45 / 60 (default 45)
- `case_type`: `common-dx with reasoning hook | rare-but-pattern-recognizable | quality-and-safety lesson | atypical presentation of common dx`
- `interaction_count`: number of audience commitment points (default 4)
- `include_chair_pushback`: bool — chair plays devil's advocate (default true for mid-residents)
- `chief_wrap_takeaways`: 3 (default; cap)

## Method

1. **Lock the teaching pillars upfront (CM-02).** Three pillars, each in one sentence:
   - **Clinical pearl pillar:** a discrete fact (a number, a drug interaction, a diagnostic criterion).
   - **Reasoning skill pillar:** a metacognitive move (problem representation, illness script update, premature closure check).
   - **System / quality pillar:** a process issue (handoff failure, dose error pathway, communication breakdown). If `case_type` doesn't include a system issue, replace with a *clinical decision under uncertainty* pillar.

2. **Stage the case (DS-29 — morning-report pattern library).**
   - **Stage 0** — One-liner: age, sex, chief complaint, key context.
   - **Stage 1** — Initial history, ROS, exam highlights, vitals. No labs yet.
   - **Stage 2** — Labs / first imaging. Audience interaction 1.
   - **Stage 3** — Course over 24–48 h; new data. Audience interaction 2.
   - **Stage 4** — Pivot point (failed therapy / unexpected finding). Audience interaction 3.
   - **Stage 5** — Confirmation + management. Audience interaction 4.
   - **Stage 6** — Outcome + system note.

3. **Audience interaction design (RP-01 chair role).** At each interaction:
   - Chair stems a specific question, not "what do you think?"
   - Asks a specific person by role ("R1 from the MICU rotation"), not the room broadly.
   - Commits a 30-sec time limit per respondent.
   - Calls a counter-respondent ("R3, push back on what you just heard").
   - Synthesizes in 60 sec before moving on.

4. **Chair pushback library.** Common pushback moves:
   - "What would change your mind?"
   - "What's the worst-case you can't miss?"
   - "What did you assume that the data doesn't confirm?"
   - "If you're wrong, what's the cost?"
   - "What's the cheapest test that discriminates?"
   - "What's your problem representation in one sentence?"

5. **Chief's wrap (3 takeaways).** Each takeaway is behavioral and traceable to a pillar:
   - Pillar 1 (clinical pearl): "When I see X, the number to remember is N."
   - Pillar 2 (reasoning): "When my problem representation is X, the next move is Y."
   - Pillar 3 (system/quality): "When I see [process gap], I will [action]."

6. **Follow-up reading.** 1 paper or guideline section. Specific (not "review acid-base").

7. **Source-fidelity audit (QA-12).** Same standards as other case prompts: traceable claims, no fabricated drug doses or thresholds.

8. **Anti-pattern check.**
   - Diagnosis named in Stage 1 or 2.
   - More than 3 takeaways.
   - "What do you think?" as the interaction stem (too open).
   - No named-call rule (chair winging it).
   - Pillar 1 = generic ("be a good doctor").

## Output Format

```
MORNING REPORT CASE — [title]
Specialty: [...]   Audience: [...]   Duration: [N] min   Type: [...]   Interactions: [N]

>>> TEACHING PILLARS (locked)
P1 (clinical pearl): [1 sentence]
P2 (reasoning skill): [1 sentence]
P3 (system / quality): [1 sentence]

>>> CASE STAGES
S0 (one-liner): [age, sex, chief complaint, key context]
S1 (history + exam): [content]
S2 (initial labs): [content]
  → INTERACTION 1: "[specific question]" — chair calls [role]; pushback prompt: [...]; synthesis: [...]
S3 (24–48 h): [new data]
  → INTERACTION 2: ...
S4 (PIVOT): [failed therapy / new finding]
  → INTERACTION 3: ...
S5 (confirmation + mgmt): [content]
  → INTERACTION 4: ...
S6 (outcome + system note): [content]

>>> CHAIR SCRIPT (timing)
00:00–02:00 — present S0+S1
02:00–08:00 — present S2 + INTERACTION 1 (3 min Q + 1 min synthesis)
08:00–15:00 — S3 + INTERACTION 2
15:00–22:00 — S4 + INTERACTION 3 (pivot, more time for debate)
22:00–32:00 — S5 + INTERACTION 4
32:00–38:00 — S6 outcome + system note
38:00–45:00 — chief's wrap + Qs

>>> CHAIR PUSHBACK LIBRARY (use at least 3 across interactions)
"What would change your mind?"
"What's your problem representation in one sentence?"
"What's the cheapest test that discriminates?"
"What did you assume?"
"If you're wrong, what's the cost?"

>>> CHIEF'S WRAP (3 takeaways)
T1 (P1): [behavioral, "When I see X, I will Y"]
T2 (P2): [behavioral]
T3 (P3): [behavioral]

>>> FOLLOW-UP READING
[1 specific paper / guideline section with citation]

>>> SOURCE-FIDELITY AUDIT
| Claim | Source | Verified |
|---|---|---|
| ... | ... | Y |

>>> ANTI-PATTERN CHECK
Dx named before S4: pass
Takeaways: 3
Pillars locked + behavioral: pass
Named-call rule: pass

>>> REJECTED ELEMENTS (≥ 1)
Considered: open question "what do you think?" at S2.
Rejected: too open; audience freezes.
Replaced with: "R1, name the top 3 of your DDx in 30 sec, ranked by what you'd treat empirically."
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `audience_level` | Interns = more concrete diagnostic questions; mid-residents = reasoning + management |
| `duration_min` | 30-min cuts interaction count to 3; 60-min adds case-arc complexity |
| `case_type` | Quality-and-safety case shifts P3 to a process pillar; rare-pattern shifts P1 to recognition |
| `include_chair_pushback` | Mid-residents + above benefit from pushback; interns may need lighter |
| `align_to_milestones` | Adds ACGME milestone tag per pillar |
| `include_pre_session_reading` | Adds 1 article assigned 24h ahead |
| `format_for_async_post` | Adds a written-summary block for residents who missed |

## Verification Checklist

- [ ] 3 pillars locked at top, in one sentence each, each behavioral or fact-anchored.
- [ ] Diagnosis is not named until Stage 4 or 5.
- [ ] Each interaction has a specific stem (not "what do you think?"), a named-call rule, a pushback prompt, and a synthesis.
- [ ] Chair pushback library used at least 3 times across interactions.
- [ ] Exactly 3 takeaways at wrap; each behavioral; each tied to a pillar.
- [ ] Follow-up reading is specific (named paper / guideline section).
- [ ] Source-fidelity audit table populated.
- [ ] At least one rejected design element shown.
- [ ] Chair script has minute-by-minute timing (not "discuss for a while").
- [ ] No fabricated drug doses or guideline thresholds.
- [ ] If `case_type` is quality/safety, P3 names the specific process failure.

## Worked Example (compact)

**Input:** `specialty = IM`, `clinical_focus = "AKI with diarrhea + recent fluoroquinolone"`, `audience_level = "mixed"`, `duration_min = 45`, `case_type = "common dx with reasoning hook"`, `interaction_count = 4`.

**Output (abbreviated):**

```
MORNING REPORT — "AKI After the Cipro Course"
Specialty: IM   Audience: mixed   Duration: 45 min

>>> PILLARS
P1: FeUrea, not FeNa, is the urine index of choice when the patient is on a diuretic.
P2: When the labs don't fit the first illness script, build a fresh problem representation from scratch rather than forcing fit.
P3: When a recent abx course preceded a clinical change, the abx is part of the differential — including for AIN.

>>> CASE STAGES
S0: 68F, 4 days diarrhea, lethargy, low UOP.
S1: 10 d post 7-d cipro course for UTI. T 37.5, BP 102/64 (baseline 138/80), HR 96, mild orthostasis. Mucous membranes dry. No rash. On HCTZ for HTN.
S2: Cr 2.8 (baseline 1.0). K 3.4. UA: trace LE, 5–10 WBC, no casts described, no eos requested.
   → I1 (5 min): "R1, problem representation in 1 sentence. R3, push back if it's just 'AKI with diarrhea'."  Pushback prompt: "what does HCTZ do to your urine indices?"  Synthesis: pre-renal vs intrinsic distinction; HCTZ confounds FeNa.
S3 (24h): IVF 2 L → Cr 2.6, UOP 30 mL/hr. K 3.5. Stool studies neg. Working dx: pre-renal AKI from volume loss.
   → I2 (5 min): "R2, why does AKI not fully resolve with 2 L? What's your next move?"  Pushback: "What would change your mind on pre-renal?"
S4 (PIVOT, 48h): UA repeat — WBC casts + eosinophils noted. UNa 60 on HCTZ; FeUrea 65%. Cr 3.0. Periph eos 12%.
   → I3 (8 min): "R3, what's your new working dx? Why does FeUrea matter here? What's the cipro link?"  Pushback: "what other meds, even ones not in our admission list, do this?"  Synthesis: AIN from cipro + HCTZ confounder.
S5: D/c offending agent (cipro already finished; stop HCTZ). Renal biopsy not done. Trial of steroids debated. Cr begins downtrend by D5.
   → I4 (5 min): "When would you biopsy? When would you steroid?"  Pushback: "What's your trigger?"
S6: 6-wk Cr returns to 1.2. System note: AIN was missed for 36 h because eos not initially requested and FeUrea not run despite HCTZ.

>>> CHAIR SCRIPT
00–02 S0+S1
02–08 S2 + I1
08–15 S3 + I2
15–25 S4 + I3 (more debate time)
25–32 S5 + I4
32–38 S6 + system note
38–45 wrap + Qs

>>> PUSHBACK USED
"What does HCTZ do to your urine indices?" (I1)
"What would change your mind on pre-renal?" (I2)
"What other meds, even ones not in our list, do this?" (I3)

>>> CHIEF'S WRAP
T1 (P1): "When patient is on a diuretic, I will run FeUrea, not FeNa." (Diskin 2003)
T2 (P2): "When IVF doesn't reverse AKI in 24 h, I will build a new problem representation from scratch instead of doubling the bolus."
T3 (P3): "When AKI develops within 14 d of a fluoroquinolone, I will explicitly include AIN on the DDx and ask for eos + WBC casts on UA, not just basic UA."

>>> FOLLOW-UP READING
Perazella & Markowitz, "Drug-induced AIN," Nat Rev Nephrol 2010. (Or KDIGO 2024 AKI guideline §3.4 if more recent.)

>>> SOURCE-FIDELITY AUDIT
| Claim | Source | Verified |
|---|---|---|
| FeUrea > 50–65% favors ATN/AIN over pre-renal in diuretic-treated | Diskin AJKD 2003 + NEJM 2002 review | Y |
| Cipro associated AIN | UpToDate AIN review; case series | Y |
| Eos in urine, sensitivity ~25% | recent guidelines | Y — limited sensitivity flag |

>>> ANTI-PATTERN CHECK
Dx revealed at S4, not earlier: pass.
Takeaways: 3.
Specific named-call rule per interaction: pass.

>>> REJECTED
"Always think AIN when AKI" — too vague; replaced with T3.
```
