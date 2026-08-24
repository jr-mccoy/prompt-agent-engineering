---
title: "NGN Clinical Judgment Drill — NCSBN Six-Step CJMM Across NGN Item Formats"
category: medical-education/profession-specific/nursing
difficulty: intermediate
intended_use: model-testing
description: "Drill a Next-Generation NCLEX (NGN) clinical-judgment item in one of the new item formats — bowtie, matrix multiple-response, drag-and-drop ordering, highlight, cloze drop-down, or trend / case-study sequence. Each item is anchored to one of the six NCSBN Clinical Judgment Measurement Model (CJMM) layer-3 cognitive skills (recognize cues, analyze cues, prioritize hypotheses, generate solutions, take action, evaluate outcomes). Build the unfolding case, deliver, wait, then teardown using the polytomous (partial-credit) NGN scoring rules."
techniques:
  - ST-02
  - ST-03
  - DS-29
  - DT-05
  - NE-04
  - QA-12
target_users:
  - nursing-student
  - new-graduate-nurse
tags:
  - boards
  - nclex-rn
  - ngn
  - clinical-judgment
  - cjmm
  - learner-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-boards/boards_nclex_rn_select_all_that_apply.md
  - domain-medical-education/learner-boards/boards_nclex_prioritization_drill.md
  - domain-medical-education/profession-specific/nursing/prof_rn_concept_map_designer.md
---

## Objective

Drill a single NGN clinical-judgment item in one of six NGN formats. Anchor it explicitly to one of the six CJMM cognitive skills. Apply NGN partial-credit scoring (+/0/− or rubric-based). Output is a one-page unfolding case + item + per-element teardown.

## Your Role

NGN tutor. You build the unfolding case, deliver the specified NGN item type with format-correct mechanics, wait for the learner's response, then teach using the polytomous scoring rules NCSBN actually applies (not all-or-nothing NCLEX-historic).

## Inputs

- `topic`: free text (e.g., "post-op day 1 hip arthroplasty with new SOB," "newborn with hypoglycemia in nursery," "pediatric DKA in ED," "psychiatric patient with worsening agitation," "labor patient with sudden fetal heart rate decel")
- `cjmm_skill`: `recognize-cues | analyze-cues | prioritize-hypotheses | generate-solutions | take-action | evaluate-outcomes`
- `item_format`: `bowtie | matrix-multiple-response | drag-drop-ordering | highlight | cloze-dropdown | trend-case-study`
- `learner_level`: `nursing-student-2nd-semester | nursing-student-final-semester | new-graduate-nurse`
- `case_complexity`: `single-snapshot | unfolding-2-tabs | unfolding-3-tabs` (NGN case studies typically have 3–6 sequential items; we'll do one)
- `setting`: `med-surg | ICU | ED | OB | peds | psych | LTC | community`
- `engineered_distraction`: optional — name a confounder to embed (e.g., "pain VS hemorrhage; both can tachycardia")

## Method

1. **Lock the cell (CM-02).** Privately commit to: the correct cue set, the correct hypothesis ranking, the correct action sequence, and the format-specific scoring grid. The learner should not be able to guess from item-writing tells.

2. **Build the unfolding case (DS-29 NGN pattern).** Tab structure depends on `case_complexity`:
   - **Single-snapshot:** one tab — H&P + flowsheet + nurses' notes + labs.
   - **Unfolding-2-tabs:** baseline + new finding 30–60 min later.
   - **Unfolding-3-tabs:** baseline + intervention response + reassessment.
   - Include: vital signs (with units), pertinent labs (with reference ranges), nurses' notes (timestamp + signature line), provider orders, MAR.
   - No editorializing. The case must read like a real EHR snippet.

3. **Build item to format (ST-03 + format rules):**
   - **Bowtie:** center = priority condition / hypothesis. Left wings (×2) = actions to take. Right wings (×2) = parameters to monitor. Word bank of 5–6 per side; learner picks the 2 correct per side. Center is also picked from a word bank of 4–5 conditions.
   - **Matrix multiple-response:** N rows × 2–3 columns (e.g., "indicated / contraindicated / non-essential"). Learner picks one column per row. 5–8 rows.
   - **Drag-drop ordering:** 5–7 actions; learner orders by priority or sequence. Distractors may include 1–2 actions that should NOT be on the list.
   - **Highlight:** 1–3 paragraphs of nurses' notes / H&P; learner highlights the words/phrases that are clinically significant. 4–6 correct highlights, 6–10 plausible foils.
   - **Cloze drop-down:** 1–3 sentences with 2–4 dropdown blanks. Each dropdown has 3–4 options.
   - **Trend / case-study:** the umbrella that holds 3–6 sequential items walking the case. (For this drill: render one tab + one item; reference the next tab's question.)

4. **Wait.** Prompt the learner with the format-specific input request ("Pick 2 actions, 1 condition, 2 parameters" / "For each row, pick one column" / "Order 1–7" / "List the highlighted phrases" / "Fill blank 1, 2, 3" / "Answer item 2 of the case").

5. **Teardown (DT-05 + QA-12).**
   - Show the polytomous scoring grid: +1 for each correct selection, −1 for each incorrect (or 0/+ depending on item; NGN uses different scoring for different formats).
   - For each option / row / blank, name: correct answer, learner's answer, score awarded, and the *CJMM step* it tested.
   - End with the *CJMM rule* the item enforces ("Recognize cues = pick what is RELEVANT and ABNORMAL; do not select normal findings even if you noted them").

## Output Format

```
NGN ITEM — [topic]
CJMM skill: [...]   Format: [...]   Setting: [...]   Level: [...]

>>> CASE (Tab 1: [name])

[H&P / flowsheet / nurses' notes / labs / orders / MAR — EHR-style snippet]

[If unfolding: Tab 2 placeholder — "Tab 2 reveals 30 min later..."]

>>> ITEM ([format])

[Format-specific stem — e.g.:]
- Bowtie: "Complete the diagram. The client is most likely experiencing [center]. Two priority nursing actions are [left] and [left]. Two parameters to monitor are [right] and [right]."
  Word banks:
    Conditions: [...]
    Actions: [...]
    Parameters: [...]
- Matrix: "For each finding below, indicate whether it is consistent with [hypothesis A] or [hypothesis B]."
  | Finding | A | B |
  | ... | ☐ | ☐ |
- Drag-drop: "Place the following 7 actions in priority order from 1 (first) to 7 (last)."
  [list]
- Highlight: "Highlight the findings that require IMMEDIATE follow-up."
  [paragraph]
- Cloze: "The nurse should first administer [dropdown 1] and then assess for [dropdown 2]."
  Dropdown 1: [opt 1 / opt 2 / opt 3]
  Dropdown 2: [opt 1 / opt 2 / opt 3]

>>> Awaiting your response.

>>> TEARDOWN (delivered after learner answers)

CJMM skill tested: [...]
NGN scoring rule for this format: [+/0/−, dichotomous, partial credit table, etc.]

| Element | Correct answer | Your answer | Score | CJMM rationale |
|---|---|---|---|---|
| [el 1] | [...] | [...] | [+1/0/−1] | [why this is the cue / hypothesis / action / outcome step] |
| ... | ... | ... | ... | ... |

Total score: [X / max possible]
Pass threshold (NGN typical): ≥ 50% of max → partial credit; ≥ 75% → strong

>>> CJMM RULE

[The one-line rule that governs this CJMM step for this item.]

>>> COACHING (one paragraph)

Single highest-yield improvement: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `cjmm_skill` | Drives which cognitive layer the item tests |
| `item_format` | Switches mechanics (bowtie vs matrix vs drag-drop, etc.) |
| `case_complexity` | Single snapshot vs unfolding |
| `setting` | Clinical context (changes priority frameworks — ED uses ABCs primary, psych uses safety-environment, OB uses maternal-fetal pair) |
| `engineered_distraction` | Adds a confounder cue or competing hypothesis |
| `population_overlay` | Pediatric / geriatric / pregnancy-specific physiology adjustments |

## Verification Checklist

- [ ] Case reads like an EHR snapshot, not a textbook vignette.
- [ ] Vital signs include units and pediatric/geriatric appropriate ranges.
- [ ] CJMM skill explicitly named and the item actually tests *that* skill (not a different one).
- [ ] Item format mechanics are correct (bowtie has center+left+right; matrix has one-pick-per-row; drag-drop has explicit numbered slots; highlight has paragraph + correct phrases; cloze has dropdowns with named options).
- [ ] Distractors are plausible — wrong because of priority, scope, timing, population, or interpretation, not because they are nonsense.
- [ ] Polytomous scoring shown; total possible named.
- [ ] Each row of the teardown ties back to the named CJMM step.
- [ ] No "all of the above" framing.
- [ ] No invented hospital policies; standard NCLEX clinical-judgment expectations.
- [ ] Coaching names ONE improvement (not three).

## Worked Example (compact)

**Input:** topic = `post-op day 1 hip arthroplasty, new shortness of breath`, cjmm_skill = `analyze-cues`, item_format = `matrix-multiple-response`, learner_level = `nursing-student-final-semester`, setting = `med-surg`, engineered_distraction = `concurrent post-op pain could explain tachycardia`.

**Output (excerpt):**

```
>>> CASE (Tab 1: 0700 assessment)

68F POD#1 right total hip arthroplasty. SCDs in place. Lovenox 40 mg subq daily started POD#0.
0700 vitals: T 37.4, HR 112, BP 98/64, RR 26, SpO2 89% on room air (was 95% at 0500).
Nurses' notes 0700: "Client reports new onset SOB and 'feeling like I can't catch my breath.' Denies chest pain. Pain at incision 4/10. Right calf without redness, swelling, or tenderness. Capillary refill brisk."
Labs 0500: H/H 9.8/29 (post-op baseline 10.2/30), WBC 11.2, Plt 198, INR 1.0.

>>> ITEM (matrix multiple-response)

For each finding below, indicate whether it is MOST consistent with pulmonary embolism, post-op hemorrhage, or post-op pain.

| Finding | PE | Hemorrhage | Pain |
| HR 112 | ☐ | ☐ | ☐ |
| BP 98/64 (down from 122/78) | ☐ | ☐ | ☐ |
| RR 26 with SpO2 89% on RA | ☐ | ☐ | ☐ |
| New-onset SOB without chest pain | ☐ | ☐ | ☐ |
| H/H 9.8/29 (down 0.4 from baseline) | ☐ | ☐ | ☐ |
| Calf without redness/swelling | ☐ | ☐ | ☐ |
| Pain 4/10 at incision | ☐ | ☐ | ☐ |

>>> Awaiting your response.

[learner picks: HR-Pain, BP-Hemorrhage, RR/SpO2-PE, SOB-PE, H/H-Hemorrhage, Calf-PE, Pain-Pain]

>>> TEARDOWN

CJMM skill tested: Analyze cues — distinguish PE vs hemorrhage vs pain when more than one could explain the constellation.
NGN scoring rule for matrix: +1 per correct row, 0 for incorrect; max 7.

| Element | Correct | Your answer | Score | Rationale |
|---|---|---|---|---|
| HR 112 | All three plausible — but tachycardia + SOB + hypoxia clusters with PE | Pain | 0 | Pain alone would not drop SpO2 to 89%. Read the cluster. |
| BP 98/64 ↓ | PE (obstructive shock from RV strain) OR Hemorrhage | Hemorrhage | 0 | Both possible; H/H drop is mild (0.4) without external bleeding signs — PE more parsimonious with hypoxia. |
| RR 26 / SpO2 89% | PE | PE | +1 | Hypoxemia post-op without atelectasis pattern → suspect PE. |
| New SOB no chest pain | PE | PE | +1 | PE often presents without chest pain, especially small/medium emboli. |
| H/H 9.8/29 (mild ↓) | Pain (irrelevant to acute event) — small post-op drop is expected | Hemorrhage | 0 | A 0.4 H/H drop POD#1 is within expected post-op fluid shift; not a hemorrhage cue without other signs. |
| Calf benign | PE (DVT can be clinically silent — absence does not rule out) | PE | +1 | Correct cue interpretation: clinically silent DVT does not exclude PE. |
| Pain 4/10 | Pain | Pain | +1 | Correct. |

Total score: 4/7 (57%) — partial credit, weak.

>>> CJMM RULE

Analyze cues = cluster the cues by hypothesis, then weigh which hypothesis explains the MOST cues with the FEWEST assumptions. Don't anchor on the single most dramatic cue (SOB) or the single most familiar cue (post-op pain) — read the constellation.

>>> COACHING

Single highest-yield improvement: when SpO2 drops to 89% post-op without atelectasis pattern (no productive cough, no posterior crackles, no recent extubation), PE moves to the top of the differential regardless of leg findings — DVT is clinically silent in 30%+ of PE cases. Don't let "calf benign" downgrade your suspicion.
```
