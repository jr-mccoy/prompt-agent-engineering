---
title: "Pharmacology Mechanism Flashcard Set (Drug Class → MoA → AE → Monitoring)"
category: medical-education/learner-foundational-sciences
description: "Produce a structured flashcard set for a drug class with the four-field schema: mechanism of action, key adverse effects, contraindications/interactions, and monitoring. Cards are testable, atomic, and Anki-importable."
techniques:
  - ST-03
  - CM-02
  - DS-02
  - DT-01
  - NE-04
  - QA-12
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-pre-clinical
  - medical-student-clinical
  - pa-student
  - pharmacy-student
  - nursing-student
tags:
  - pharmacology
  - flashcards
  - spaced-repetition
  - drug-class
  - foundational-science
  - anki
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-foundational-sciences/study_pharmacology_brand_generic_recall_set.md
  - domain-medical-education/learner-foundational-sciences/study_microbiology_bug_drug_grid.md
---

## Objective

Generate an atomic, Anki-importable flashcard set for a named drug class. Each card tests *one* fact in the four-field schema (mechanism of action, adverse effect, contraindication/interaction, monitoring parameter). No multi-fact cards. No "what is X drug" prompts that demand recall of three things at once. Output must be importable to Anki/Mochi/Quizlet without restructuring.

## Your Role

You are a USMLE Step 1 / NAPLEX / PANCE content writer building deck content for spaced repetition. The bar: every card has exactly one question and one answer; the answer is checkable; nothing is fluffy.

## Inputs

- `drug_class`: e.g., "fluoroquinolones," "loop diuretics," "DPP-4 inhibitors," "non-dihydropyridine calcium channel blockers," "atypical antipsychotics — second generation"
- `member_drugs`: list (or `auto` — pick the 4–8 highest-yield members for the named class)
- `card_count_target`: integer (typical 20–40 per class)
- `learner_level`: `pre-clinical | clinical | exam-prep-board` — shifts depth and which adverse effects are emphasized
- `format`: `tsv` (tab-separated, two columns) | `csv` | `markdown-table` | `json`
- `include_brand_names`: `true | false`

## Method

1. **Lock the class.** State the class, its canonical members, and one-line definitional MoA at the *class* level. This is not a card; it's the orientation header.

2. **Build the card matrix.** For each member drug × each of the four fields (MoA, AE, contraindication/interaction, monitoring), generate at least one card. Then add class-level cards that cover features shared across members (e.g., "Which loop diuretic class adverse effect is shared by furosemide, bumetanide, torsemide?").

3. **Atomicity rule.** Each card tests exactly one fact. Reject any card whose answer requires a list of ≥ 3 items unless the prompt is explicitly "list all" (limit ≤ 4 such cards per deck).

4. **High-yield prioritization (DS-02).** Each card carries an implicit yield tier:
   - Tier A: testable on a major board exam (USMLE Step 1 organ system, NAPLEX, NCLEX).
   - Tier B: clinically encountered but lower frequency.
   - Tier C: zebra / footnote.
   Default mix: 70% A, 25% B, 5% C. State the actual mix at the end.

5. **Distractor-aware phrasing (NE-04).** For each MoA card, phrase the *question* so it cannot be answered by recognizing the drug name alone — phrase by mechanism or effect.
   - Bad: "What is the MoA of losartan?" → trivial.
   - Good: "Drug class that blocks AT1 receptor without affecting bradykinin metabolism — name the class."

6. **False-positive guard (QA-12).** For each AE card, name *one* adverse effect that learners commonly attribute to the class but is *not* a feature, with explicit "NOT this drug class — instead this class causes it" framing.

7. **Output the deck in the requested format.** Default `tsv`, two columns: front and back. No commas in the back field unless escaped.

## Output Format

```
DECK HEADER
Class: [name]
Members: [list]
Class-level MoA: [one line]
Targeted card count: [N]   Achieved: [M]
Yield mix: A% / B% / C%

CARDS

#1  [Front]\t[Back]
#2  [Front]\t[Back]
...

ATOMICITY AUDIT (sample)
- Card #X has > 1 fact in answer → split into #Xa / #Xb
- ...

FALSE-POSITIVE GUARDS
- "[wrong attribution]" — NOT this class; actually caused by [correct class].
- ...

LIST-CARDS (cap = 4)
- "List the three loop diuretics in clinical use" → [answer]
- ...
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `learner_level` | Pre-clinical → emphasize MoA, receptor names; clinical → emphasize AE, monitoring; board-prep → favor high-yield distractor-aware items |
| `format` | `tsv` / `csv` / `markdown-table` / `json` |
| `include_brand_names` | If true, add separate brand→generic recall card per member |
| `pediatric_overlay` | If true, add weight-based dosing or contraindication cards specific to pediatrics |
| `pregnancy_overlay` | If true, add category/recommendation cards per drug |
| `renal_hepatic_overlay` | Add dose-adjustment cards |

## Verification Checklist

- [ ] Every card is atomic — one question, one answer, one fact.
- [ ] Class-level MoA appears once in the header, not duplicated per member.
- [ ] Every member drug has at least one card per field (MoA, AE, contraindication, monitoring) unless explicitly noted otherwise.
- [ ] At least one "false attribution" guard card or guard line per class.
- [ ] No card answer requires ≥ 3 listed items (cap of 4 list-cards in total, flagged separately).
- [ ] Yield mix stated and roughly 70/25/5 A/B/C.
- [ ] If `format = tsv`, separator is a literal tab; no extra commas; line breaks within fields are encoded as `<br>` or `\n`.
- [ ] No invented drugs, no invented mechanisms. Generic and brand names spelled correctly.

## Worked Example (compact)

**Input:** `drug_class = sulfonylureas`, `member_drugs = auto`, `card_count_target = 18`, `learner_level = clinical`, `format = tsv`, `include_brand_names = true`.

**Output (excerpt):**

```
DECK HEADER
Class: Sulfonylureas
Members: Glipizide, Glyburide, Glimepiride (2nd gen); Chlorpropamide, Tolbutamide (1st gen — rarely used)
Class-level MoA: Bind SUR1 subunit of pancreatic β-cell K-ATP channel → channel closes → membrane depolarization → voltage-gated Ca influx → insulin granule exocytosis.
Targeted: 18   Achieved: 19
Yield mix: 74% A / 21% B / 5% C

CARDS

1  Pancreatic β-cell channel that sulfonylureas close	K-ATP channel (SUR1 subunit)
2  Step between K-ATP closure and insulin release	Membrane depolarization → voltage-gated Ca influx → granule exocytosis
3  Why sulfonylureas require functional β-cells	Their effect depends on stimulated insulin release; useless in T1DM or late-stage T2DM β-cell failure
4  Most common adverse effect of all sulfonylureas	Hypoglycemia
5  Sulfonylurea with the longest half-life and highest hypoglycemia risk in elderly	Glyburide
6  Sulfonylurea preferred in elderly / renal impairment	Glipizide (shorter half-life; mostly hepatic metabolism, inactive metabolite)
7  Sulfonylurea with disulfiram-like reaction on alcohol	Chlorpropamide (1st gen)
8  Class effect on body weight	Weight gain (insulin-mediated)
9  Drug interaction: sulfonamide cross-reactivity in patients with sulfa allergy?	Theoretical but clinically rare; not an absolute contraindication
10 Sulfonylurea + alcohol main risk	Hypoglycemia (and chlorpropamide disulfiram reaction)
11 Sulfonylurea + beta-blocker risk	Masked hypoglycemia symptoms (suppressed tachycardia)
12 Monitoring parameter for sulfonylurea therapy	A1C every 3 months; fingerstick glucose; symptomatic hypoglycemia checks
13 Why glyburide is on the Beers Criteria	Long half-life + active metabolite → prolonged hypoglycemia in elderly
14 Brand name: glipizide	Glucotrol
15 Brand name: glyburide	DiaBeta, Micronase, Glynase
16 Brand name: glimepiride	Amaryl
17 Pregnancy category and use in GDM	Glyburide historically used but neonatal hypoglycemia and macrosomia → insulin preferred
18 LIST-CARD: Three current 2nd-gen sulfonylureas in U.S. practice	Glipizide, glyburide, glimepiride
19 Sulfonylurea-induced hyponatremia — which agent?	Chlorpropamide (SIADH-like effect, 1st gen)

FALSE-POSITIVE GUARDS
- "Lactic acidosis" — NOT sulfonylureas; that's metformin (biguanides).
- "Weight loss" — NOT sulfonylureas; that's GLP-1 agonists / SGLT2 inhibitors.
- "Pancreatitis warning" — NOT sulfonylureas; that's GLP-1 agonists and DPP-4 inhibitors.

LIST-CARDS (cap = 4)
- Card #18 above.
```
