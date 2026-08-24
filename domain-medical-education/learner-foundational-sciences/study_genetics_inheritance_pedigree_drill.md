---
title: "Genetics Inheritance & Pedigree Drill (Pattern Recognition + Recurrence Risk)"
category: medical-education/learner-foundational-sciences
description: "Generate text-described pedigrees, ask the learner to (a) identify the inheritance pattern, (b) compute recurrence risk for a stated future pregnancy, and (c) name a disease consistent with the pattern. Includes Bayesian carrier-risk calculation when penetrance or prior risk is uncertain."
techniques:
  - ST-02
  - NE-11
  - ED-02
  - QA-01
  - NE-04
  - DT-01
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-pre-clinical
  - medical-student-clinical
  - pa-student
  - pharmacy-student
  - resident-junior
tags:
  - genetics
  - inheritance
  - pedigree
  - recurrence-risk
  - bayesian
  - foundational-science
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-foundational-sciences/study_biochem_pathway_clinical_correlation.md
  - domain-medical-education/learner-foundational-sciences/study_embryology_developmental_defect_mapper.md
---

## Objective

Generate pedigrees in text and drill three skills per case: identify the inheritance pattern, compute the recurrence risk for a specified future pregnancy, and propose a disease consistent with the pattern. Bake in at least one Bayesian update case (prior + likelihood from unaffected offspring → posterior carrier risk).

## Your Role

Medical geneticist running a genetic counseling teaching case. You generate the pedigree verbally (Generation × position notation), you grade tightly, and you expect numeric answers — `1/4`, `1/200`, `0.25`, etc. — not "low risk."

## Inputs

- `case_count`: integer (3–8 cases)
- `pattern_mix`: `auto` (balanced across AR, AD, X-linked recessive, X-linked dominant, mitochondrial, Y-linked, imprinting, multifactorial) or explicit list
- `learner_level`: `MS1 | MS2 | MS3 | clinical | pa-student`
- `include_bayesian`: `true | false` (default true; at least one case uses prior + likelihood update)
- `include_consanguinity`: `true | false`
- `include_uncertain_paternity`: `true | false`

## Method

1. **Generate each pedigree in standard text notation.** Use:
   - I, II, III for generations
   - 1, 2, 3 left-to-right for position
   - `□` or `M` for unaffected male, `■` or `M*` for affected male
   - `○` or `F` for unaffected female, `●` or `F*` for affected female
   - `=` for couple, `|` for parent-offspring line; siblings under shared parents listed comma-separated
   - Note carrier status as `(c)` if previously tested
   Provide a one-line legend at the top of each case.

2. **For each pedigree, ask three questions in order:**
   - Q1: "What inheritance pattern best fits, and what features rule out the alternatives?"
   - Q2: "Compute the recurrence risk for [specific future pregnancy described]. Show work."
   - Q3: "Name one disease consistent with this pattern and one consistent disease *and* phenotype detail from the pedigree."

3. **Bayesian case (NE-11 embedded calculation).** At least one case includes a couple with `N` unaffected children and asks for posterior carrier risk for the mother given that prior children were unaffected. Provide the formula:

   ```
   Prior odds (carrier vs. not) × Conditional likelihood (all N children unaffected | carrier) ÷ (likelihood | not carrier)
   = Joint odds → Posterior probability
   ```

4. **Grade.** Numeric answers within ±5% accepted with correct work. If pattern misidentified, give one-line correction and proceed.

5. **Adversarial distractor (NE-04).** One case must have an *ambiguous* pedigree (small family, no males in one generation) where two patterns are plausible; learner must state both and explain which features would distinguish.

6. **Final synthesis.** Score per skill axis (pattern ID, recurrence risk math, disease naming, Bayesian) so the learner sees which axis is weakest.

## Output Format

```
GENETICS DRILL — [N] cases
Learner level: [...]   Bayesian: [yes/no]   Consanguinity: [yes/no]

>>> CASE 1

Legend: I = generation 1, etc. ■/● = affected male/female; □/○ = unaffected; (c) = known carrier.

Pedigree:
I-1 □  =  I-2 ○ (c)
                |
II-1 ●   II-2 □   II-3 ○   II-4 ■

Q1: Pattern? Features ruling out alternatives?
> [learner]
Grade: [...]

Q2: II-3 marries an unrelated, unaffected man (general population carrier frequency 1/50). What is the recurrence risk for their first child?
> [learner]
Grade: [...]    Work expected: II-3 carrier prob = 2/3 (given unaffected from carrier × non-carrier? actually from AR mating Aa × aa? — show work] → joint risk = ...

Q3: Name a disease consistent.
> [learner]
Grade: [...]

>>> CASE 2 (Bayesian)

Pedigree: ...

Q (Bayesian): Mother's brother had Duchenne. Mother is the only daughter. She has had 3 unaffected sons. What is her posterior carrier probability?
> [learner]
Grade — expected work:
  Prior carrier prob (mother of affected brother): 2/3 (her mother is obligate carrier; mother got X from mom; 50/50 each from grandmother, but conditioned on having an affected brother and assuming grandmother is obligate carrier — refine).
  Likelihood 3 unaffected sons | carrier = (1/2)^3 = 1/8
  Likelihood 3 unaffected sons | not carrier = 1
  Posterior odds = (2/3 × 1/8) : (1/3 × 1) = 1/12 : 1/3 = 1 : 4 → posterior carrier prob ≈ 1/5 (0.20).

>>> CASE 3 ... (ambiguous, NE-04)

>>> SCORE
Pattern ID: X/N correct
Recurrence math: X/N correct (work checked)
Disease naming: X/N correct
Bayesian: pass/fail with the specific arithmetic error if any

Highest-yield restudy: [the axis the learner is weakest on]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `pattern_mix` | Balances inheritance patterns drilled |
| `case_count` | Controls drill length |
| `include_bayesian` | At least one case uses prior × likelihood update |
| `include_consanguinity` | Adds a double-line couple and prompts AR recognition |
| `include_uncertain_paternity` | Adds the question "what would alter your interpretation?" |
| `include_mitochondrial` | Adds a case showing maternal-only transmission |
| `include_anticipation` | Adds a trinucleotide repeat expansion case (HD, fragile X, myotonic dystrophy) |

## Verification Checklist

- [ ] Every pedigree has a legend. Symbols used consistently.
- [ ] Every Q2 (recurrence risk) demands shown work. Answers in fractional or decimal form.
- [ ] At least one Bayesian case present if `include_bayesian = true`; formula shown.
- [ ] Ambiguous case (NE-04) has at least two plausible interpretations with the distinguishing feature stated.
- [ ] Mitochondrial case (if requested) shows transmission from *all* affected mothers to *all* offspring; not father→child.
- [ ] X-linked recessive pedigrees show male predominance with carrier-female transmission, no male-to-male transmission.
- [ ] X-linked dominant shows no male-to-male transmission and affected females from affected fathers.
- [ ] Anticipation case shows earlier onset and worse severity in successive generations (if requested).
- [ ] No invented diseases, no impossible inheritance (e.g., autosomal X-linked, mitochondrial paternal transmission).

## Worked Example (compact)

**Input:** `case_count = 3`, `pattern_mix = AR, X-linked recessive (Bayesian), mitochondrial`, `learner_level = MS2`, `include_bayesian = true`.

**Output (excerpt):**

```
GENETICS DRILL — 3 cases

>>> CASE 1 (AR)

Legend: ■/● affected; □/○ unaffected; = couple; vertical line = parent-offspring.

I-1 □  =  I-2 ○
              |
II-1 ●   II-2 □   II-3 ○   II-4 ●

(Two affected children of two unaffected parents; one male, one female; no skipping generations within a single sibship.)

Q1: Pattern?
> "AR."
Grade: correct — two unaffected parents with two affected children of both sexes, no vertical transmission.

Q2: II-3 (unaffected) marries an unrelated man whose population carrier frequency is 1/50. Recurrence risk for a child?
> "II-3 carrier prob: from Aa × Aa cross with unaffected phenotype, P(Aa | unaffected) = 2/3.
Husband carrier prob: 1/50.
Both carriers: 2/3 × 1/50 = 1/75.
Affected child if both carriers: 1/4.
Recurrence risk: 1/75 × 1/4 = 1/300."
Grade: correct.

Q3: Name a disease.
> "Cystic fibrosis."
Grade: correct.

>>> CASE 2 (X-linked recessive, Bayesian)

Maternal grandmother is obligate carrier (had affected son with Duchenne).
Consultand's mother (proband's mother) is sister of affected uncle; mother of proband has 3 unaffected sons.

Q (Bayesian): What is the proband's mother's posterior carrier risk?
> "Prior (daughter of obligate carrier): 1/2.
Likelihood of 3 unaffected sons | carrier = (1/2)^3 = 1/8.
Likelihood | not carrier = 1.
Posterior odds: (1/2 × 1/8) : (1/2 × 1) = 1/16 : 1/2 = 1 : 8.
Posterior probability: 1/(1+8) = 1/9."
Grade: correct (≈ 0.111).

>>> CASE 3 (Mitochondrial)

I-1 □  =  I-2 ●
              |
II-1 ●  II-2 ●  II-3 ●

II-1 ■  =  II-2-spouse ○
              |
III-1 □  III-2 ○  III-3 □

Q1: Pattern, with one distinguishing feature?
> "Mitochondrial — affected mother transmits to all children; affected father (II-1) transmits to none of his children."
Grade: correct.

Q2: Recurrence risk for III-2's children if she is clinically affected?
> "Variable — heteroplasmy makes severity unpredictable, but all her children inherit the mitochondrial DNA. Effective recurrence: 100% inheritance, expressed severity uncertain."
Grade: correct.

Q3: Disease name?
> "MELAS or LHON."
Grade: correct.

>>> SCORE
Pattern ID: 3/3   Recurrence math: 3/3 (Bayesian explicit)   Disease naming: 3/3
Highest-yield restudy: heteroplasmy and threshold effect, which is hardest to translate into discrete recurrence-risk numbers.
```
