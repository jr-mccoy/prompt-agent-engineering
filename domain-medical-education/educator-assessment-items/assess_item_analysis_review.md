---
title: "Item Analysis Review — Difficulty, Discrimination, Distractor Performance, Action Plan"
category: medical-education/educator-assessment-items
description: "Given item-analysis statistics for an MCQ exam (p-value/difficulty, point-biserial / Rpb / D-index, distractor-selection frequencies, KR-20/Cronbach α), produce a per-item review: keep / revise / retire decision with rationale, named flaw type, suggested revision, and a test-level summary with action priorities. Refuses to recommend removal solely on difficulty without inspecting distractor performance and content validity."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - DT-05
  - NE-11
difficulty: advanced
intended_use: model-testing
target_users:
  - assessment-faculty
  - psychometric-consultant
  - course-director
  - boards-committee
tags:
  - item-analysis
  - psychometrics
  - difficulty
  - discrimination
  - distractor-performance
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-assessment-items/assess_mcq_nbme_style_author.md
  - domain-medical-education/educator-assessment-items/assess_distractor_designer.md
  - domain-medical-education/educator-assessment-items/assess_question_bank_audit.md
---

## Objective

Review a delivered MCQ exam at item and test level. Per item: report p-value (difficulty), point-biserial correlation (discrimination), distractor-selection frequencies, and produce a keep / revise / retire decision with named flaw type and a concrete revision. At test level: report KR-20 / Cronbach α, mean p, mean Rpb, and prioritized action list. Refuse to recommend retiring an item solely because it's "too hard" or "too easy" — always inspect distractor performance and content validity first.

## Your Role

Educational measurement consultant. You read item statistics through the lens of construct validity. You distinguish a hard-but-good item from a flawed item, and a discriminating item from a clued one.

## Inputs

- `exam_name`: identifier
- `n_examinees`: integer
- `n_items`: integer
- `item_stats`: per-item table with: p (proportion correct), Rpb (point-biserial), distractor-selection % per option, % omitted, key letter
- `reliability`: KR-20 or Cronbach α
- `target_difficulty_window`: e.g., `0.55–0.85` (default NBME-style)
- `target_discrimination`: e.g., `Rpb ≥ 0.20` (≥ 0.30 ideal; < 0.10 retire-candidate)
- `content_blueprint`: mapping of items to content area / cognitive level
- `stakes`: `formative | summative | high-stakes` (changes thresholds; high-stakes is stricter)

## Method

1. **Set decision thresholds (CM-02 — explicit thresholds).** State the difficulty window and Rpb thresholds being used. Default NBME-style for high-stakes: p in `0.55–0.85`, Rpb ≥ 0.20 acceptable / ≥ 0.30 strong / 0.10–0.19 marginal / < 0.10 retire-candidate. For formative low-stakes, widen to p in `0.40–0.90`, Rpb ≥ 0.15.

2. **Per-item flag classification (DS-01 — psychometric flag taxonomy; NE-11 — computed flags).**
   - **F1 — Too easy:** p > upper bound. Inspect: is it clued? Did all examinees know it? Action: revise (toughen distractors) or retire if redundant with blueprint.
   - **F2 — Too hard:** p < lower bound. Inspect: ambiguity, content gap, miskey?
   - **F3 — Low discrimination:** Rpb < 0.10. Often cluing flaw or ambiguous key.
   - **F4 — Negative discrimination:** Rpb < 0. High scorers got it wrong more often than low scorers — strong suspicion of miskey or two-correct-answers.
   - **F5 — Non-functioning distractor:** option selected by < 5% of examinees. Replace.
   - **F6 — Implausible high-scorer attractor:** non-key option chosen by > 25% of high-third examinees. Suggests key ambiguity or domain controversy.
   - **F7 — Content-validity mismatch:** item maps to wrong blueprint cell. Re-map or retire.

3. **Distractor-performance audit (DT-05 — element-by-element on distractors).** For each non-key option:
   - % selected
   - % among high-third (top scorers)
   - % among low-third (bottom scorers)
   - Functioning: yes (≥ 5% overall and high-low gap supports key) / no (replace) / inverted (replace urgently).

4. **Decision per item (ST-02).**
   - **Keep:** p in window, Rpb ≥ 0.20, all distractors functioning, no content flag.
   - **Revise:** any single flag (F1–F6) without F7. Provide named revision.
   - **Retire:** F4 (negative discrimination) confirmed by miskey check, OR F7 content mismatch, OR two flags simultaneously not fixable.

5. **Refusal guard (CM-02 — content-before-stats rule).** No item is retired solely on difficulty. Difficulty alone triggers revise unless content review also flags it. Document this rule.

6. **Test-level summary (ST-03).** Report:
   - KR-20 / α with interpretation (≥ 0.80 acceptable for high-stakes; ≥ 0.70 formative).
   - Mean p, mean Rpb, % items in target window, % items with Rpb ≥ 0.20.
   - Items by action: keep / revise / retire counts.
   - Top 5 priority revisions (named).
   - Test-level recommendations (e.g., add 5 items to weak blueprint cell; remove 3 redundant high-p items).

## Output Format

```
ITEM ANALYSIS REVIEW — [exam_name] — N examinees: [N] — N items: [N]

>>> THRESHOLDS USED
Difficulty window: [low–high]
Rpb acceptable: ≥ [...]   strong: ≥ [...]   marginal: [...]   retire-candidate: < [...]
Stakes: [...]

>>> PER-ITEM REVIEW
| Item # | p | Rpb | Distractor flags | Content flag | Decision | Named revision |
|---|---|---|---|---|---|---|
| 1 | 0.82 | 0.34 | all functioning | none | keep | — |
| 2 | 0.41 | 0.08 | C non-functioning (3%) | none | revise | replace C with [misconception X]; check for ambiguity in stem |
| 3 | 0.92 | 0.03 | A 88%; B,C,D < 4% each | redundant w/ Item 17 | retire | redundant + low discrimination |
| 4 | 0.55 | -0.18 | high-scorers chose B (32%) | possible miskey | revise/retire | content panel review for two-correct-answer; if confirmed miskey → change key; if true ambiguity → retire |
| ... |

>>> DISTRACTOR-PERFORMANCE AUDIT (for items flagged F5/F6)
| Item # | Option | % overall | % high-third | % low-third | Action |
|---|---|---|---|---|---|
| 2 | C | 3% | 1% | 5% | non-functioning → replace |
| 4 | B | 32% | 40% | 22% | high-scorer attractor → suspect miskey or genuine controversy → content review |
| ... |

>>> TEST-LEVEL SUMMARY
KR-20 / α: [value] ([interpretation])
Mean p: [value]
Mean Rpb: [value]
% items in difficulty window: [%]
% items with Rpb ≥ 0.20: [%]
Counts: keep = [n] / revise = [n] / retire = [n]

>>> TOP 5 PRIORITY REVISIONS
1. Item [#] — [named flaw] — recommended action.
2. ...
5. ...

>>> TEST-LEVEL RECOMMENDATIONS
- [e.g., "Blueprint cell 'pediatrics — endocrine' has 2 items, both flagged F1; add 3 application-level items at moderate difficulty"]
- [e.g., "Replace 4 retired items before next administration"]
- [e.g., "Inter-rater on free-response items not in scope but recommend repeating with κ check"]

>>> REFUSAL LOG
Considered retiring items based on difficulty alone: [list of items]. Refused per content-before-stats rule. Routed to content panel for review.
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `stakes` | `high-stakes` tightens p window and α threshold; `formative` widens both |
| `target_difficulty_window` | Adjustable per institution; default NBME 0.55–0.85 |
| `include_DIF_analysis` | Adds differential item functioning (DIF) check by subgroup if examinee demographics provided |
| `include_speededness_check` | Adds % omitted analysis per item to flag time-pressure effects |
| `include_blueprint_audit` | Maps action items to blueprint cells |
| `include_IRT_estimates` | If 1PL/3PL estimates available, adds difficulty (b), discrimination (a), guessing (c) review |

## Verification Checklist

- [ ] Thresholds stated explicitly.
- [ ] Per-item table populated with p, Rpb, distractor flags, decision.
- [ ] Distractor-performance audit included for any F5/F6 item.
- [ ] No item retired solely on difficulty without content flag.
- [ ] Test-level α/KR-20 reported with interpretation.
- [ ] Top 5 priority revisions named with action.
- [ ] Test-level recommendations include blueprint-aware actions.
- [ ] Refusal log shows where retirement-by-difficulty-alone was declined.
- [ ] All flags use named taxonomy (F1–F7).

## Worked Example (compact)

**Input:** `n_examinees = 142`, `n_items = 60`, KR-20 = 0.78, `stakes = summative`, `target_difficulty_window = 0.55–0.85`. (Stats provided for 5 sample items.)

**Output (abbreviated):**

```
ITEM ANALYSIS REVIEW — Internal Medicine Block Final — N=142 — Items=60

>>> THRESHOLDS USED
Difficulty: 0.55–0.85
Rpb: acceptable ≥ 0.20; strong ≥ 0.30; marginal 0.10–0.19; retire < 0.10
Stakes: summative

>>> PER-ITEM REVIEW (5 of 60 shown)
| # | p | Rpb | Distractor flags | Content | Decision | Revision |
|---|---|---|---|---|---|---|
| 12 | 0.92 | 0.08 | A=92%, B=3%, C=2%, D=3% | none | revise | F1+F3+F5×3 — only key functioning; replace 3 distractors with named misconceptions; aim p ≈ 0.75 |
| 23 | 0.34 | 0.41 | functioning | mapped to apex of Bloom (analysis) | keep | hard but discriminating; matches blueprint intent |
| 28 | 0.48 | -0.22 | high-third selects B 47% > key A 38%; low-third selects A 41%, B 22% | suspect miskey | revise/retire | content panel reviewed: B is also defensible (recent guideline update) → change key to A or B accepted; or retire and rewrite |
| 41 | 0.71 | 0.31 | functioning | none | keep | — |
| 55 | 0.96 | 0.02 | A=96%, B=1%, C=1%, D=2% | redundant with Item 7 | retire | F1+F3+F7 — redundant and not discriminating |

>>> DISTRACTOR-PERFORMANCE AUDIT (excerpt)
| Item | Option | Overall | High-third | Low-third | Action |
|---|---|---|---|---|---|
| 12 | B | 3% | 2% | 5% | non-functioning → replace with named miscon |
| 28 | B | 35% | 47% | 22% | high-scorer attractor → miskey or guideline-update controversy |

>>> TEST-LEVEL SUMMARY
KR-20: 0.78 (acceptable for summative block, below 0.80 ideal)
Mean p: 0.68
Mean Rpb: 0.24
% items in window: 64%
% items with Rpb ≥ 0.20: 71%
Keep: 38 / Revise: 17 / Retire: 5

>>> TOP 5 PRIORITY REVISIONS
1. Item 28 — negative discrimination + high-scorer attractor → content panel; possibly accept both A and B for this administration; rewrite for next.
2. Item 12 — only key is functioning → replace 3 distractors with misconception-anchored options.
3. Item 55 — redundant + non-discriminating → retire; replace with new item targeting under-covered blueprint cell.
4. Item 33 — Rpb = 0.05; suspect ambiguity in lead-in → revise lead-in to closed phrasing.
5. Item 49 — F5 on option C → replace.

>>> TEST-LEVEL RECOMMENDATIONS
- Add 4 application-level items to "Endocrine — Pituitary" (only 1 item currently).
- Re-administer with revised pool; target KR-20 ≥ 0.80.
- Inter-rater on the 4 short-answer items: out of scope here; recommend separate review.

>>> REFUSAL LOG
Considered retiring items 23 and 41 based on difficulty alone (p = 0.34 and 0.71 respectively); refused. Both are within content-validity expectations and discriminate well.
```
