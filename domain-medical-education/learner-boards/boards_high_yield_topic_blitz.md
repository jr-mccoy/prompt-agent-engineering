---
title: "High-Yield Topic Blitz — Topic → 10 Testable Points in 10 Minutes"
category: medical-education/learner-boards
difficulty: intermediate
intended_use: model-testing
description: "Convert a named topic into exactly 10 testable points (the kind of facts that appear in a board-question stem or stand as the answer), ranked by board frequency. Output is a one-screen blitz card the learner can hit before sleep on dedicated. Optional 5-question rapid drill at the end."
techniques:
  - ST-02
  - ST-03
  - DS-29
  - DS-02
  - NE-04
  - QA-12
target_users:
  - medical-student-clinical
  - medical-student-pre-clinical
  - intern
  - nursing-student
  - pa-student
  - pharmacy-student
tags:
  - boards
  - high-yield
  - rapid-review
  - dedicated-study
  - learner-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-boards/boards_usmle_step1_concept_drill.md
  - domain-medical-education/learner-boards/boards_pance_pearl_drill.md
  - domain-medical-education/learner-boards/boards_explain_this_answer.md
  - domain-medical-education/learner-clinical-reasoning/reason_clinical_pearl_extraction.md
---

## Objective

Convert a single topic into exactly 10 testable points ranked by board frequency — the kind of fact that appears as a stem detail, a vignette buzzword, or the answer to a discriminating-feature question. Output: a one-screen blitz card. Optional: end with 5 rapid stem-fragments to test recall.

## Your Role

Board tutor producing a rapid-review card. You do not lecture. You produce 10 ranked points and (if requested) 5 rapid recall fragments.

## Inputs

- `topic`: free text (e.g., "hyperthyroidism," "acute pancreatitis," "abruptio placentae," "warfarin pharmacology," "Wilson disease")
- `exam_target`: `USMLE-Step-1 | USMLE-Step-2 | NCLEX-RN | NAPLEX | PANCE | COMLEX-L1 | COMLEX-L2 | shelf-medicine | shelf-pediatrics | shelf-surgery | shelf-obgyn | shelf-psych | NREMT | ITE`
- `learner_level`: free text
- `frequency_filter`: `top-10-most-tested | top-10-discriminators | top-10-distractor-traps` (default `top-10-most-tested`)
- `rapid_recall_drill`: `true` (default) | `false` — 5 stem fragments at end
- `time_pressure`: `pre-sleep | board-week | midnight-cram`

## Method

1. **Lock the topic (CM-02).** Anchor: "this blitz covers [topic] for [exam_target] — only the 10 facts most likely to appear on an item."

2. **Brain-dump and rank (DS-29 pattern library, DS-02 metric specification — frequency as the metric).** Privately list 20–30 candidate facts. Rank by board-frequency for the target exam (you may not have empirical data; use clinical educator's judgment of what NBME / NCSBN / NCCPA / NABP / NREMT items actually test). Cut to exactly 10. Each point is one sentence, no comma-overload.

3. **Render in ranked order.** Point 1 is the *most likely* to be tested. Point 10 is "still high-yield enough to make the top 10."

4. **Filter for board language (NE-04).** Each point should be phrased as it would appear in a question stem or answer choice. Buzzwords used when buzzwords are real ("worst headache of life," "rust-colored sputum," "fruity breath," "wine-colored urine"). Mechanisms named precisely.

5. **Optional rapid drill (if `rapid_recall_drill = true`).** 5 stem fragments — each is a 1-sentence partial vignette, learner names the dx or next step in one phrase. Brief teardown.

6. **False-positive sweep (QA-12).** Reject any point that is true but never tested. Reject any made-up statistic. Reject paraphrases of the same fact.

## Output Format

```
HIGH-YIELD BLITZ — [topic]
Exam target: [...]   Frequency filter: [...]   Learner level: [...]

>>> 10 POINTS (ranked by board frequency)

 1. [...]
 2. [...]
 3. [...]
 4. [...]
 5. [...]
 6. [...]
 7. [...]
 8. [...]
 9. [...]
10. [...]

>>> RAPID RECALL DRILL (optional)

Fragment 1: "[...]" → Your one-phrase answer?
Fragment 2: "[...]" → Your one-phrase answer?
Fragment 3: "[...]" → Your one-phrase answer?
Fragment 4: "[...]" → Your one-phrase answer?
Fragment 5: "[...]" → Your one-phrase answer?

(Brief answer/teardown delivered after learner answers.)
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `topic` | The topic to blitz |
| `exam_target` | Tailors the ranking |
| `frequency_filter` | most-tested / discriminators / distractor-traps |
| `rapid_recall_drill` | Whether to append 5-fragment drill |
| `time_pressure` | Pre-sleep / board-week — affects terseness |
| `comparison_blitz` | Two topics side by side (10 points each — useful for look-alikes) |
| `differentials_overlay` | Add a 3-line "vs X / vs Y / vs Z" tail |

## Verification Checklist

- [ ] Exactly 10 points, no more, no less.
- [ ] Each point is one sentence, no semicolon-trains.
- [ ] Ranking is by board-frequency for the named exam, not random.
- [ ] Buzzwords used when they're actually NBME / NCLEX / etc. buzzwords.
- [ ] No invented statistics ("seen in 47% of cases").
- [ ] No invented eponyms or drug names.
- [ ] Rapid recall fragments (if used) are NBME/NCLEX-style stem starters, not full vignettes.
- [ ] Whole blitz fits on one screen.

## Worked Example (compact)

**Input:** topic = `acute pancreatitis`, exam_target = `USMLE-Step-2`, frequency_filter = `top-10-most-tested`, learner_level = `MS4 dedicated`, rapid_recall = `true`, time_pressure = `pre-sleep`.

**Output (excerpt):**

```
HIGH-YIELD BLITZ — Acute pancreatitis
Exam target: USMLE-Step-2   Filter: top-10-most-tested

>>> 10 POINTS

 1. Top two causes: gallstones (most common in women) and alcohol (most common in men); together account for ~80%.
 2. Diagnosis (Atlanta) requires 2 of 3: characteristic abdominal pain (epigastric, radiates to back, worse supine), lipase or amylase > 3× ULN, characteristic imaging.
 3. Lipase is more specific than amylase and stays elevated longer; both can be elevated; lipase is the preferred test.
 4. Initial imaging if dx is uncertain: contrast-enhanced CT abdomen — but delay 48–72h after onset for best sensitivity to necrosis. RUQ ultrasound at presentation to evaluate for gallstones is appropriate.
 5. Severity assessment: BISAP score or modified Atlanta criteria. Persistent organ failure > 48h = severe.
 6. Initial management: aggressive isotonic IV fluids (lactated Ringer's preferred over NS), pain control, NPO initially then early enteral feeding as tolerated (within 24–72h), no prophylactic antibiotics for sterile necrosis.
 7. Gallstone pancreatitis with cholangitis or persistent obstruction: ERCP within 24–48h.
 8. Gallstone pancreatitis without obstruction: cholecystectomy during same admission (mild) or after resolution of acute illness (severe).
 9. Hypertriglyceridemia-induced (TG > 1000 mg/dL): manage with insulin infusion ± plasmapheresis for severe cases.
10. Late complications: pseudocyst (4+ weeks; drain if symptomatic or > 6 cm and persistent), walled-off necrosis, infected necrosis (CT with gas; ICU; targeted abx + drainage).

>>> RAPID RECALL DRILL

1: "45M alcoholic presents with epigastric pain radiating to back, lipase 8× ULN..." → Dx?
2: "Same patient, day 3, persistent hypoxia and creatinine doubled..." → severity classification?
3: "Same patient, day 5, CT shows peripancreatic fluid + necrotic areas; afebrile, WBC stable..." → next step re: antibiotics?
4: "62F with stones on US, mild pancreatitis resolving, day 4..." → disposition before discharge?
5: "Hospital day 10, mild pancreatitis pt now afebrile, eating, lipase down, but Hb dropped, abdomen distended..." → next dx consideration?

(answers / brief teardown follow each learner reply)
```
