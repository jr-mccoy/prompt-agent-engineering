---
title: "Extended-Matching Item (EMI) Author — Theme, Option List, Lead-In, Vignettes"
category: medical-education/educator-assessment-items
description: "Author an extended-matching item set in classic UK / RCP / NBME-EMI style: theme + 8–20 homogeneous options + closed lead-in + 3–6 short clinical vignettes, each keyed to one option with rationale and distractor walk-by. Refuses cluing flaws (option used more than once unless explicitly allowed; convergence; heterogeneous options) and forbids 'all of the above'."
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
  - item-writer
  - course-director
  - boards-committee
tags:
  - emi
  - extended-matching
  - item-writing
  - assessment
  - distractors
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-assessment-items/assess_mcq_nbme_style_author.md
  - domain-medical-education/educator-assessment-items/assess_distractor_designer.md
  - domain-medical-education/educator-assessment-items/assess_blueprint_designer.md
---

## Objective

Produce a complete EMI set: theme statement → homogeneous option list (8–20 items) → closed lead-in → 3–6 clinical vignettes, each with one best-matching option, rationale, distractor walk-by, and blueprint tags. Refuse heterogeneous option lists (e.g., mixing diagnoses with investigations), refuse convergence, refuse vignettes that could match two options equally well.

## Your Role

EMI item writer in the UK medical-school / RCP / NBME-EMI tradition. Your standard is option-list homogeneity and discriminability: every option must be a member of the same category, and every vignette must have one — and only one — best match.

## Inputs

- `exam_style`: `MRCP-style | NBME-EMI | course-final | shelf | OSCE-knowledge-station`
- `learner_level`: `MS3 | MS4 | intern | resident-junior | PA-student | nursing-student | pharmacy-student`
- `theme`: single-sentence statement of category (e.g., "Diagnoses of headache in adults," "Antibiotics for community pneumonia")
- `option_list_count`: `8 | 10 | 12 | 15 | 20` (default 10)
- `option_reuse`: `each-option-used-once | options-may-be-reused | options-may-be-unused` (state explicitly)
- `vignette_count`: `3 | 4 | 5 | 6` (default 4)
- `content_blueprint`: e.g., "headache: 1 vignette migraine, 1 cluster, 1 SAH, 1 GCA"
- `cognitive_level`: `recall | application | analysis` (default application)
- `target_misconception_per_vignette`: 1 named misconception per vignette the trap distractor exploits

## Method

1. **Construct the theme + option list (DS-01 — EMI shell).** Theme is a one-sentence category. Option list is 8–20 alphabetized items, parallel grammar, homogeneous category (all diagnoses OR all drugs OR all investigations OR all next-steps — never mixed).

2. **Lock the lead-in (CM-02).** Single closed lead-in shared by all vignettes (e.g., "For each patient described below, select the most likely diagnosis from the option list."). One lead-in per set; no per-vignette lead-ins.

3. **Author vignettes (ST-02).** Each vignette is 2–5 sentences, focused on features that discriminate one option from its near-neighbors on the list. Each vignette must:
   - Match exactly one option as best.
   - Have a named near-neighbor on the option list as the most plausible wrong match.
   - Surface one targeted misconception (per input).
   - Cite no unsourced numbers; flag thresholds with source.

4. **Discriminability audit (DT-05 — element-by-element vignette × option).** Build a matrix: rows = vignettes, columns = top 3 candidate options. Mark which features in the vignette rule each option in or out. If any cell allows two options equally, redesign the vignette.

5. **Cluing-flaw + convergence sweep (QA-12).**
   - Each vignette key is a different option (unless `option_reuse = options-may-be-reused`).
   - No "all of the above"; no option that is a superset of another (e.g., "viral infection" and "influenza A").
   - No option phrased so that it answers the question regardless of vignette (e.g., "Investigation depends on context").

6. **Rationale + distractor walk-by per vignette (ST-03).** State the discriminating feature(s) that anchor the key; for the two next-best options, name the misconception and the vignette feature that excludes them.

7. **Source-fidelity audit (QA-12).** Every diagnostic threshold, drug, dose traces to a current source or marked `[verify before use]`.

## Output Format

```
EMI SET — [theme] — [exam_style] — Cognitive: [level]

>>> THEME
[Single-sentence category.]

>>> OPTION LIST (option_list_count = N; reuse: [policy])
A) [option]
B) [option]
...
J) [option]
[alphabetized; parallel grammar; homogeneous category]

>>> LEAD-IN (shared by all vignettes below)
[Closed, focused: "For each patient described, select the most likely [diagnosis/drug/investigation] from the option list."]

>>> VIGNETTE 1
[2–5 sentences.]
Key: [letter]
Rationale: [discriminating feature → rule that anchors the key]
Distractor walk-by:
  Near-neighbor 1: [letter] — misconception exploited: [...]. Vignette feature that excludes it: [...].
  Near-neighbor 2: [letter] — misconception: [...]. Exclusion feature: [...].

>>> VIGNETTE 2
[...]
Key: [...]
Rationale: [...]
Distractor walk-by: [...]

(repeat for vignette_count)

>>> DISCRIMINABILITY MATRIX
| Vignette | Key | Near-neighbor 1 | Near-neighbor 2 | Discriminator |
|---|---|---|---|---|
| V1 | [letter] | [letter] | [letter] | [vignette feature that uniquely selects key] |
| V2 | ... | ... | ... | ... |

>>> CLUING-FLAW AUDIT
| Flaw | Status |
|---|---|
| Heterogeneous option list | pass / fail |
| Option that is a superset of another | pass / fail |
| Two vignettes share the same key (under "used-once" rule) | pass / fail / n/a |
| "All / none of the above" used | pass / fail |
| Any vignette matches two options equally | pass / fail |
| Convergence (multiple options point to one) | pass / fail |
| Lead-in not closed | pass / fail |

>>> BLUEPRINT TAGS
| Field | Value |
|---|---|
| Exam style | [...] |
| Content area | [...] |
| Cognitive level | [...] |
| Option-reuse policy | [...] |
| Target misconceptions | [list] |

>>> SOURCE-FIDELITY AUDIT
| Clinical claim | Source | Status |
|---|---|---|
| [each cited threshold/drug/dose] | [...] | verified / [verify before use] |

>>> REJECTED ELEMENT (minimum 1)
Considered: [option / vignette]
Why rejected: [discriminability / cluing / convergence flaw]
Replaced with: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `option_list_count` | 8 → tight; 20 → wide. Wider lists improve discriminability when content area is broad |
| `option_reuse` | `used-once` is classic UK EMI; `may-be-reused` allows true frequency-weighted theme |
| `cognitive_level` | `application` requires diagnosis from vignette; `analysis` requires integration of multiple features |
| `theme` | "Diagnoses" vs "Investigations" vs "Drugs" — never mix categories within one set |
| `include_image` | Adds IMAGE BRIEF block (no rendering); e.g., dermatology photo, ECG strip, peripheral smear |
| `cross_cutting_misconception` | If a misconception spans 2 vignettes, document it explicitly in blueprint |

## Verification Checklist

- [ ] Option list is homogeneous (all one category).
- [ ] Options are parallel in grammar and length within ±25%.
- [ ] Theme statement is one sentence; lead-in is closed.
- [ ] Each vignette matches exactly one option as best; near-neighbors named.
- [ ] Discriminability matrix shows a unique discriminator per vignette.
- [ ] No "all of the above"; no superset options.
- [ ] Under "used-once" policy, no vignette key repeats.
- [ ] Every cited number traces to a current source or marked `[verify before use]`.
- [ ] At least one rejected element shown.
- [ ] Blueprint tags populated.

## Worked Example (compact)

**Input:** `exam_style = MRCP-style`, `theme = "Diagnoses of headache in adults"`, `option_list_count = 10`, `option_reuse = each-option-used-once`, `vignette_count = 4`, `cognitive_level = application`.

**Output (abbreviated):**

```
EMI SET — Diagnoses of headache in adults — MRCP-style — Cognitive: application

>>> THEME
Diagnoses of headache in adults presenting to acute care.

>>> OPTION LIST (10; reuse: used-once)
A) Cluster headache
B) Giant cell arteritis
C) Idiopathic intracranial hypertension
D) Medication-overuse headache
E) Meningitis (bacterial)
F) Migraine without aura
G) Pituitary apoplexy
H) Subarachnoid hemorrhage
I) Temporal lobe seizure
J) Tension-type headache

>>> LEAD-IN
For each patient described below, select the most likely diagnosis from the option list.

>>> VIGNETTE 1
A 35-year-old man presents with three weeks of severe, unilateral, retro-orbital pain occurring nightly for 60 minutes, accompanied by ipsilateral lacrimation, conjunctival injection, and restlessness. Attacks recur at the same hour.
Key: A (Cluster headache)
Rationale: Strictly unilateral, autonomic features, circadian periodicity, restlessness — Type 3 of ICHD-3 cluster criteria.
Distractor walk-by:
  Near-neighbor F (Migraine): patient quiet/dark-room-seeking — vignette describes restlessness.
  Near-neighbor B (GCA): age and ESR not yet given but patient is 35 — too young.

>>> VIGNETTE 2
A 72-year-old woman has 6 weeks of right temporal pain and jaw claudication; ESR 88 mm/h, CRP 64.
Key: B (Giant cell arteritis)
Rationale: Age, ESR/CRP, jaw claudication → GCA clinical criteria; high-dose steroids warranted before biopsy.
Distractor walk-by:
  Near-neighbor J (Tension): no inflammatory markers in tension.
  Near-neighbor D (MOH): no analgesic-overuse history.

>>> VIGNETTE 3
A 28-year-old previously well man develops a "thunderclap" headache while lifting weights; reaches max intensity within 60 seconds and now has photophobia. Non-contrast CT head 4 hours later is negative.
Key: H (Subarachnoid hemorrhage)
Rationale: Sentinel thunderclap pattern; CT < 6 h is high-sensitivity but a 4-h CT does not exclude — proceed to LP.
Distractor walk-by:
  Near-neighbor F (Migraine): migraine can be thunderclap-mimicking but always exclude SAH first.
  Near-neighbor I (TLE seizure): no postictal or focal features.

>>> VIGNETTE 4
A 38-year-old woman, BMI 34, reports 3 months of progressive daily headaches, transient visual obscurations, and pulsatile tinnitus; fundoscopy shows bilateral disc edema; CT venogram normal.
Key: C (Idiopathic intracranial hypertension)
Rationale: Demographic profile, papilledema, pulsatile tinnitus, normal CTV — IIH (formerly pseudotumor cerebri).
Distractor walk-by:
  Near-neighbor F (Migraine): no papilledema in migraine.
  Near-neighbor E (Meningitis): no fever, no meningismus, subacute course.

>>> DISCRIMINABILITY MATRIX
| Vignette | Key | NN1 | NN2 | Discriminator |
|---|---|---|---|---|
| V1 | A | F | B | Restlessness + autonomic + circadian |
| V2 | B | J | D | ESR/CRP + age + jaw claudication |
| V3 | H | F | I | Thunderclap onset + need to exclude pre-CT |
| V4 | C | F | E | Papilledema + pulsatile tinnitus + normal CTV |

>>> CLUING-FLAW AUDIT
All rows: pass.

>>> BLUEPRINT TAGS
| Field | Value |
|---|---|
| Exam style | MRCP-style |
| Content area | Neurology — Headache |
| Cognitive level | application |
| Option reuse | used-once |
| Target misconceptions | "Migraine excludes SAH"; "Tension explains inflammatory markers"; "CT < 24 h excludes SAH" |

>>> SOURCE-FIDELITY AUDIT
| Claim | Source | Status |
|---|---|---|
| ICHD-3 cluster criteria | IHS ICHD-3 | verified |
| CT < 6 h ~100% sensitive for SAH | Perry 2011 BMJ | verified |
| GCA ESR criterion | ACR 2022 GCA classification | verified |

>>> REJECTED
Considered: "Investigations for headache" mixed in the option list.
Rejected: would create heterogeneous list (diagnoses + investigations) → cluing flaw.
Replaced with: pure-diagnosis list above.
```
