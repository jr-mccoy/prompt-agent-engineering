---
title: "Question Bank Audit — Coverage, Item Quality, Redundancy, Aging, Retire/Refresh Plan"
category: medical-education/educator-assessment-items
description: "Audit an existing question bank for blueprint coverage, item-quality flaws (NBME-style flaw taxonomy), content redundancy, item aging, and demographic / safety / equity issues. Produce a retire / refresh / keep classification per item plus a bank-level action plan with priority order. Refuses to mark items 'keep' without an item-quality flaw sweep and source-fidelity audit."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - DT-05
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - assessment-faculty
  - course-director
  - boards-committee
tags:
  - item-bank
  - audit
  - quality-control
  - coverage
  - aging
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-assessment-items/assess_mcq_nbme_style_author.md
  - domain-medical-education/educator-assessment-items/assess_item_analysis_review.md
  - domain-medical-education/educator-assessment-items/assess_blueprint_designer.md
---

## Objective

Audit a question bank end-to-end on five axes: (1) blueprint coverage, (2) item-quality flaws (NBME flaw taxonomy), (3) redundancy / near-duplicate clusters, (4) item aging vs current guidelines, (5) demographic / equity / safety issues. Produce per-item classification (keep / refresh / retire / replace) with named reason, and a bank-level action plan with priority order. Refuse "keep" for any item without an item-quality flaw sweep and a source-fidelity row.

## Your Role

Item-bank auditor. You read banks the way a copy editor reads a manuscript: with the flaw taxonomy in one hand and the blueprint in the other.

## Inputs

- `bank_name`: identifier
- `bank_size`: total items
- `blueprint`: content × cognitive × competency matrix (target counts)
- `current_distribution`: actual counts per cell
- `current_guidelines_basis`: e.g., "ACC/AHA 2023, ADA 2024, KDIGO 2024, Sanford 2025, NAEPP 2024"
- `last_full_review_date`: date of last audit
- `examinee_demographic_context`: optional — for DIF / equity checks if available
- `redundancy_threshold`: e.g., "items differing only in numeric values count as duplicates" / "vignettes differing in patient age only count as duplicates" (define explicitly)

## Method

1. **Coverage delta (DT-05 — element-by-element).** For each blueprint cell, compare target vs actual. Flag over-weighted (> 120% of target), under-weighted (< 80%), and zero-count cells with non-zero LOs.

2. **Item-quality flaw sweep (DS-01 — NBME flaw taxonomy + QA-12).** Per item, run:
   - **Flaws of irrelevant difficulty:** tricky wording, "all of the above", multiple-true-false hybrids, awkward double negatives.
   - **Cluing flaws:** grammatical cluing, absolute terms, longest-option-is-key, convergence, paired opposites, superset overlap with key.
   - **Construct flaws:** orphaned-fact stem, vignette unrelated to lead-in, lead-in not closed.
   - **Source flaws:** un-sourceable numbers, outdated thresholds.
   - **Equity flaws:** stereotype anchoring, irrelevant demographic, biased language.

3. **Redundancy / near-duplicate clusters (CM-02 — explicit threshold).** Apply `redundancy_threshold` definition. Group near-duplicates; retain best item in cluster, mark others for retirement.

4. **Item aging (QA-12 — guideline drift).** Compare cited standards (drugs, thresholds, devices, dosing) against `current_guidelines_basis`. Flag items citing superseded guidelines.

5. **Per-item classification (ST-02).**
   - **Keep:** zero flaws, current sources, distinct from near-neighbors, blueprint-needed.
   - **Refresh:** minor cluing or guideline-update issue → 1-line revision.
   - **Retire:** unfixable construct flaw, equity flaw, or redundant within cluster (not the chosen survivor).
   - **Replace:** retired item from a blueprint cell needing coverage → action item.

6. **Bank-level action plan (ST-03).**
   - Top 10 priority actions (by stake / coverage / quality risk).
   - New items required per cell.
   - Next audit date recommendation.

7. **Refusal guard.** No item gets "keep" without:
   - Item-quality flaw sweep row.
   - Source-fidelity row (every cited number traceable to `current_guidelines_basis` or flagged `[verify before use]`).

## Output Format

```
QUESTION BANK AUDIT — [bank_name] — Items: [N] — Last full review: [date]

>>> COVERAGE DELTA
| Blueprint cell | Target | Actual | Δ | Status |
|---|---|---|---|---|
| Cardio × Application × Patient care | 7 | 9 | +2 | over (120–129%) |
| Renal × Analysis × Med knowledge | 3 | 1 | -2 | under |
| Endo × Application × Patient care (LO-29 mapped) | 1 | 0 | -1 | zero with LO |
| ...

>>> ITEM-QUALITY FLAW SWEEP (excerpt)
| Item # | Flaws | Severity | Decision |
|---|---|---|---|
| 0034 | longest-option-is-key | minor | refresh |
| 0078 | absolute-term ("always") | minor | refresh |
| 0112 | orphaned-fact stem; lead-in not closed | major | retire |
| 0188 | all-of-the-above option | minor-but-modern-NBME-bans | refresh (drop AOA) |
| 0214 | stereotype anchor (race as gotcha) | major | retire |
| 0277 | outdated guideline (cites pre-2018 sepsis bundle) | major | refresh (update to current Surviving Sepsis 2021) |
| ...

>>> REDUNDANCY CLUSTERS (threshold = vignette differing only in patient age or single lab value)
| Cluster | Items | Survivor | Retired |
|---|---|---|---|
| HFrEF GDMT titration | 0021, 0099, 0301, 0344 | 0099 | 0021, 0301, 0344 |
| DKA initial fluids | 0117, 0118 | 0117 | 0118 |

>>> ITEM AGING
| Item # | Citation | Current standard | Action |
|---|---|---|---|
| 0277 | pre-2018 sepsis bundle | Surviving Sepsis 2021 | refresh |
| 0432 | Sanford 2019 abx recommendations | Sanford 2025 | refresh dosing |
| 0500 | pre-DAPA-CKD diuretic algorithm | Add SGLT2i per KDIGO 2024 | refresh |

>>> EQUITY / DEMOGRAPHIC AUDIT (excerpt)
| Item # | Concern | Action |
|---|---|---|
| 0214 | race as gotcha anchor | retire |
| 0356 | gendered language in pelvic exam stem | refresh to inclusive language |

>>> PER-ITEM CLASSIFICATION SUMMARY
Keep: [N]   Refresh: [N]   Retire: [N]   Replace (to author): [N]

>>> TOP-10 PRIORITY ACTIONS
1. Retire item 0112 (orphaned-fact, lead-in not closed) — major flaw.
2. Retire item 0214 (stereotype) — equity flaw.
3. Refresh item 0277 (outdated sepsis bundle).
4. Refresh items 0021/0301/0344 → consolidate to one (0099).
5. Author 2 new items for Renal × Analysis × Med knowledge (LO-04 area).
6. Author 1 new item for Endo × Application × Patient care (LO-29).
7. Refresh items with absolute-term flaws (10 items listed).
8. Refresh items with "all of the above" option (8 items listed).
9. Update Sanford-cited dosing across 14 items.
10. Schedule next bank audit at [date + 12 months].

>>> NEW-ITEM REQUIREMENTS (linked to gap)
| Cell | Items needed | Cognitive | LO target |
|---|---|---|---|
| Renal × Analysis × Med knowledge | 2 | analysis | LO-04, LO-07 |
| Endo × Application × Patient care | 1 | application | LO-29 |
| ...

>>> REFUSAL LOG
None of the items currently classified "keep" was passed without flaw + source rows. 23 items initially marked "keep-no-review" were re-routed through full sweep before sign-off.
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `redundancy_threshold` | Tighter threshold catches more clusters; looser preserves variants |
| `include_DIF_analysis` | If demographic data available, adds bias check per item |
| `include_image_audit` | If items contain images, adds resolution / clarity / age-of-image check |
| `include_translation_audit` | If items translated, flags translation drift |
| `stake_level` | High-stakes raises retire thresholds for any flaw; formative tolerates more refresh-instead-of-retire |
| `aging_window_months` | Default 24 months for guideline review; tighter for fast-moving areas (e.g., infectious disease, oncology) |

## Verification Checklist

- [ ] Coverage delta computed per blueprint cell.
- [ ] Every item received item-quality flaw sweep.
- [ ] Every item received source-fidelity check against `current_guidelines_basis`.
- [ ] Redundancy threshold stated explicitly; clusters identified.
- [ ] Aging review completed against current standards.
- [ ] Equity / demographic audit completed.
- [ ] Per-item classification populated.
- [ ] Top-10 priority list ordered by stake/coverage/quality.
- [ ] New-item requirements tied to coverage gaps and LOs.
- [ ] Refusal log present.

## Worked Example (compact)

**Input:** `bank_name = "IM Clerkship Bank"`, `bank_size = 540`, last review 19 months ago, `redundancy_threshold = "vignettes differing only in patient age or single lab value"`, `current_guidelines_basis = "ACC/AHA 2023, ADA 2024, KDIGO 2024, Surviving Sepsis 2021, Sanford 2025"`.

**Output (excerpt):**

```
QUESTION BANK AUDIT — IM Clerkship Bank — N=540 — Last review: 19 mo ago

>>> COVERAGE DELTA (excerpt — full matrix attached)
| Cell | Target | Actual | Δ |
|---|---|---|---|
| Cardio × Application | 50 | 64 | over |
| Renal × Analysis | 18 | 9 | under |
| Heme × Evaluation | 6 | 0 | zero |

>>> ITEM-QUALITY FLAW SWEEP (excerpt — 540 items reviewed)
| Flaw class | Count |
|---|---|
| Longest-option-is-key | 41 |
| Absolute terms | 28 |
| "All of the above" | 19 |
| Orphaned-fact stems | 14 |
| Equity flaws | 6 |
| Outdated guideline | 47 |

>>> REDUNDANCY CLUSTERS
73 clusters identified; 109 items recommended for retirement (cluster duplicates).

>>> CLASSIFICATION SUMMARY
Keep: 268   Refresh: 132   Retire: 140   Replace: 32

>>> TOP-10 ACTIONS
1. Retire 14 orphaned-fact items.
2. Retire 6 equity-flawed items.
3. Refresh 47 outdated-guideline items (priority: sepsis bundle, GDMT, SGLT2 in CKD).
4. Refresh 41 longest-option-is-key items (rebalance option lengths).
5. Refresh 19 AOA items (drop AOA, add 4th distractor anchored to misconception).
6. Consolidate 73 redundancy clusters → retire 109 duplicates.
7. Author 9 new items for Renal × Analysis.
8. Author 6 new items for Heme × Evaluation.
9. Author 17 new items distributed per remaining gaps.
10. Schedule next audit: [date + 12 mo].

>>> REFUSAL LOG
98 items initially flagged "keep-as-is" by content team were re-routed through flaw sweep; 22 of those reclassified to refresh or retire after audit.
```
