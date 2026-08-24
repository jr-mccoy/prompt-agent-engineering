---
title: "Oral Exam / Viva Question Author (Stem, Probe Ladder, Pass-Fail Anchors)"
category: medical-education/educator-assessment-items
description: "Author oral exam / viva questions with a structured probe ladder: opening stem → 3–5 graduated follow-up probes → expected response at each rung → pass / borderline / fail anchors → examiner script for handling silence, wrong turns, and over-running answers. Refuses unbounded stems and refuses pass-fail anchors without verbatim exemplar language."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - DT-05
  - RP-04
difficulty: advanced
intended_use: model-testing
target_users:
  - oral-examiner
  - clinical-educator
  - boards-committee
  - residency-program-director
tags:
  - oral-exam
  - viva
  - probe-ladder
  - assessment
  - examiner-script
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-assessment-items/assess_short_answer_constructed_response_author.md
  - domain-medical-education/educator-case-writing/case_oral_exam_case_author.md
  - domain-medical-education/educator-rubrics-wba/assess_cbd_rubric_author.md
---

## Objective

Produce an oral-exam question packaged for examiner use: opening stem → 3–5 graduated probes that increase cognitive demand → expected response per rung → pass / borderline / fail anchors with verbatim language → examiner script for silence, wrong turns, and over-runs → blueprint tags → source-fidelity audit. Refuse unbounded stems and refuse anchors that say "demonstrates understanding" without exemplar language.

## Your Role

Oral-exam item writer trained on ABA / ABS / RCS-style viva and ACGME oral exams. Your probes get harder, not broader. Your anchors are concrete enough that two examiners give the same rating without consultation.

## Inputs

- `exam_style`: `boards-oral | OSCE-viva-station | clinical-clerkship-oral | residency-mock-oral | RCS-viva | ABA-style`
- `learner_level`: as before
- `content_domain`: e.g., "perioperative management of OSA patient for laparoscopy"
- `cognitive_level_target`: `application | analysis | evaluation` (probe ladder should walk up the levels)
- `time_budget_minutes`: `3 | 5 | 8 | 10 | 15`
- `target_competency`: e.g., "Patient Care — Intraop Management," "Medical Knowledge"
- `pass_threshold`: text description (e.g., "Reaches probe 3 with safe management plan including peri-extubation strategy")

## Method

1. **Lock the stem (CM-02 — no "tell me about X").** Stem is a focused clinical scenario with one driving question. Length: 2–4 sentences. The question is open enough to allow reasoning but anchored enough that "tell me everything you know" is not a passing response.

2. **Build the probe ladder (DS-01 — graduated probes; RP-04 — Socratic).** 3–5 probes, each:
   - Increases cognitive demand (recall → application → analysis → evaluation).
   - Has a defined expected response.
   - Has a defined "what the candidate should say next if probed correctly."
   - Is bounded by time within `time_budget_minutes`.

   Probe types:
   - **P1 — Anchor probe:** "What's your first concern?" / "What's your differential?"
   - **P2 — Reasoning probe:** "Why?" / "What evidence supports that?"
   - **P3 — Decision probe:** "What's your next step and why?"
   - **P4 — Trade-off / curveball:** "The X you ordered isn't available. Now what?" or "How would your management change if Y?"
   - **P5 — Edge / evaluation probe:** "When would you abandon plan A?" / "What's the worst-case if you're wrong?"

3. **Define pass / borderline / fail anchors at each probe (DT-05 — element-by-element).** Each rung has:
   - **Pass:** verbatim acceptable response or named bullets.
   - **Borderline:** misses one element or shows a named hesitation; recoverable with one redirect.
   - **Fail:** demonstrates the named misconception or a safety-critical error (e.g., extubates without checking neuromuscular reversal in the OSA case).

4. **Examiner script (ST-02 — structured examiner moves).** For each probe, specify:
   - Opening prompt phrasing (verbatim).
   - If candidate is silent > 15 s: rescue prompt (verbatim, doesn't give the answer).
   - If candidate goes wrong direction: redirect (open question, not the answer).
   - If candidate over-runs: time-cap phrasing.

5. **Pass-threshold lock (CM-02).** State exactly what passing the station requires (e.g., "Reaches P3 with a safe plan AND addresses post-extubation monitoring in P4").

6. **Source-fidelity audit (ST-03).** Every clinical claim cited in probes / anchors traces to a current source.

## Output Format

```
ORAL EXAM QUESTION — [content_domain] — [exam_style] — Time: [N min]

>>> OPENING STEM
[2–4 sentences. Sets a focused scenario.]

>>> DRIVING QUESTION (P1 / Anchor)
Examiner says (verbatim): "[opening question]"
Expected response (Pass): [verbatim or named bullets]
Borderline: [response that misses one element]
Fail: [response showing named misconception or safety error]
If silent > 15 s, examiner says: "[rescue prompt]"
If wrong direction, examiner redirects: "[open-question redirect]"
Time cap: [seconds]

>>> P2 — Reasoning probe
Examiner: "[verbatim prompt]"
Expected (Pass): [...]
Borderline: [...]
Fail: [...]
Silent: "[...]"
Wrong: "[...]"
Time: [...]

>>> P3 — Decision probe
[as above]

>>> P4 — Trade-off / curveball
[as above]

>>> P5 — Edge / evaluation probe (optional based on time_budget)
[as above]

>>> PASS THRESHOLD
[Exact rule: e.g., "Pass = reaches P3 with a safe and rationalized plan AND addresses P4 trade-off. Fail = any safety-critical misstep at P1–P3 (e.g., extubates without reversal verification)."]

>>> EXAMINER NORMS
- Don't supply the answer at any probe — only redirect with open questions.
- Allow up to 15 s of silence before rescue prompt.
- Time-cap each probe at the listed seconds; cap forces graduation to next probe.
- If candidate's plan is safe but suboptimal, mark borderline — don't downgrade for differences in defensible practice.

>>> BLUEPRINT TAGS
| Field | Value |
|---|---|
| Exam style | [...] |
| Content area | [...] |
| Cognitive level at apex | [...] |
| Competency | [...] |
| Time budget | [...] |
| Inter-rater target | κ ≥ 0.75 (oral exams tolerate slightly lower than written) |

>>> SOURCE-FIDELITY AUDIT
| Claim | Source | Status |
|---|---|---|
| [each #/threshold/practice standard cited] | [...] | verified / [verify before use] |

>>> REJECTED ELEMENT (minimum 1)
Considered: [an unbounded probe or an anchor that uses "shows good judgment" without exemplar]
Why rejected: [unscorable]
Replaced with: [bounded version]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `time_budget_minutes` | 3 min = 2-probe; 10 min = 4-probe; 15 min = 5-probe with curveball + evaluation |
| `cognitive_level_target` | Sets the apex probe (P3 = decision; P5 = evaluation/edge) |
| `include_image` | Adds IMAGE BRIEF (CXR, ECG, sim monitor) shown at P1 |
| `include_pediatric_weight` | Adds explicit weight for weight-based dose questions |
| `safety_critical_step` | Names a step (e.g., neuromuscular reversal verification) that automatically fails the station if missed |
| `style_RCS_vs_ABA` | RCS: candidate-leads with examiner punctuation; ABA: examiner-driven probe ladder |

## Verification Checklist

- [ ] Stem is 2–4 sentences and anchored.
- [ ] 3–5 probes, each with explicit cognitive level.
- [ ] Each probe has Pass / Borderline / Fail anchors with verbatim exemplar.
- [ ] Each probe has a silent-rescue and wrong-direction redirect (verbatim).
- [ ] Time caps sum within `time_budget_minutes`.
- [ ] Pass threshold stated as a rule, not a feeling.
- [ ] Safety-critical step (if any) named with automatic-fail flag.
- [ ] Source-fidelity audit table populated.
- [ ] Inter-rater target ≥ 0.75 stated.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `exam_style = boards-oral` (ABA-style), `learner_level = resident-senior`, `content_domain = "Perioperative airway plan for severe OSA patient undergoing laparoscopic cholecystectomy"`, `time_budget_minutes = 8`, `cognitive_level_target = evaluation`.

**Output (abbreviated):**

```
ORAL EXAM QUESTION — Perioperative OSA + laparoscopic chole — ABA-style — Time: 8 min

>>> OPENING STEM
A 52-year-old man, BMI 41, polysomnography-confirmed severe OSA (AHI 38), home CPAP nightly, presents for elective laparoscopic cholecystectomy. He has well-controlled hypertension and no other comorbidities. He brought his CPAP machine.

>>> P1 — Anchor (60 s)
Examiner: "What are your perioperative concerns and how do they shape your plan?"
Pass: identifies airway risk (difficult mask + intubation possible), opioid sensitivity, post-extubation airway collapse, post-op CPAP plan.
Borderline: identifies airway but misses post-op CPAP planning.
Fail: focuses solely on intraop; no peri-extubation or recovery plan.
Silent: "What stands out about this patient's airway risk profile?"
Wrong: "Beyond the cardiovascular issues, what about this patient's anatomy concerns you?"

>>> P2 — Reasoning (90 s)
Examiner: "Walk me through your induction and intubation plan."
Pass: positions ramped, pre-oxygenates 3 min at FiO2 1.0 (or 8 vital capacity breaths), considers awake fiberoptic if exam predicts difficulty, has video laryngoscope + LMA available, uses short-acting NMB.
Borderline: standard plan without difficulty-prediction step or backup device.
Fail: chooses long-acting NMB without awareness of OSA + post-op reversal risk.
Silent: "What about positioning and pre-oxygenation specifically?"
Wrong: "Step back — what does the BMI and OSA together tell you about your equipment choices?"

>>> P3 — Decision (90 s)
Examiner: "Intraop opioid plan?"
Pass: multimodal — local infiltration / TAP block / acetaminophen / ketorolac / dexmedetomidine; minimize long-acting opioid; mentions quantitative neuromuscular monitoring.
Borderline: multimodal but doesn't name quantitative TOF monitoring.
Fail: opioid-heavy plan; no regional / multimodal element.
Silent: "What's your opioid-sparing strategy?"
Wrong: "Why is intraop opioid choice particularly important in this patient?"

>>> P4 — Trade-off / curveball (90 s)
Examiner: "End of case — TOF ratio is 0.75 by quantitative monitor. Do you extubate?"
Pass: NO — extubation requires TOF ≥ 0.9; reverse appropriately (sugammadex preferred if rocuronium); reassess.
Borderline: extubates after subjective recovery without quantitative re-check.
Fail (safety-critical): extubates at TOF 0.75 with no further action.
Silent: "What's your minimum acceptable TOF for extubation in this patient?"
Wrong: "What does TOF 0.75 mean for diaphragm function vs upper airway muscles?"

>>> P5 — Evaluation (60 s)
Examiner: "Where will he recover, and on what?"
Pass: monitored bed (step-down or PACU with extended monitoring), on CPAP per home settings, capnography overnight, opioid-sparing analgesia continued.
Borderline: floor with intermittent SpO2 only.
Fail: routine PACU → floor without CPAP / capnography.
Silent: "What's your post-op monitoring plan?"
Wrong: "Why is the first 24 h post-op uniquely risky in this patient?"

>>> PASS THRESHOLD
Pass = reaches P4 safely AND addresses P5 monitoring AND avoids any safety-critical fail at P2 / P4. The TOF 0.75 step at P4 is the safety-critical step (automatic fail if extubates).

>>> EXAMINER NORMS [as standard above]

>>> BLUEPRINT TAGS
| Field | Value |
|---|---|
| Exam style | ABA-style boards-oral |
| Content area | Perioperative — OSA + Bariatric |
| Cognitive apex | evaluation |
| Competency | Patient Care — Periop |
| Time | 8 min |
| Inter-rater | κ ≥ 0.75 |
| Safety-critical | TOF < 0.9 extubation = fail |

>>> SOURCE-FIDELITY AUDIT
| Claim | Source | Status |
|---|---|---|
| TOF ≥ 0.9 for extubation | ASA 2023 NMB monitoring guideline | verified |
| Sugammadex for rocuronium reversal | sugammadex FDA labeling | verified |
| Capnography post-op for OSA | SAMBA / ASA OSA periop guidelines | verified |

>>> REJECTED
Considered: open P1 "Tell me about OSA."
Rejected: unbounded; invites encyclopedia answer.
Replaced with: focused P1 "concerns + plan."
```
