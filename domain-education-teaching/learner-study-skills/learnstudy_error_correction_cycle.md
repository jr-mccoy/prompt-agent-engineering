---
title: "Error Correction Cycle"
category: education-teaching/learner-study-skills
description: "Transforms an error log into an active correction workflow: classifies error types (conceptual, procedural, careless), generates targeted remediation drills for each, and produces a do-over problem set to confirm correction."
techniques:
  - ST-01
  - ST-02
  - ED-02
  - NE-04
  - QA-12
difficulty: intermediate
tags:
  - error-analysis
  - mistake-log
  - error-correction
  - targeted-practice
  - exam-prep
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/learner-study-skills/learnstudy_mistake_log_reviewer.md
  - domain-education-teaching/learner-study-skills/learnstudy_weak_area_diagnosis.md
  - domain-education-teaching/learner-study-skills/learnstudy_retrieval_drill_designer.md
---

## Objective

Take a list of mistakes — from a practice test, homework, or quiz — classify each error type, generate a targeted correction drill for each type, and produce a "do-over" problem set to confirm the error is resolved.

## When to Use

- After getting a practice test or quiz back with errors
- When reviewing a homework set and needing to understand why answers were wrong
- When errors on similar topics keep repeating across multiple tests (pattern recognition)
- Before a major exam, to systematically close the gaps revealed by practice

**Do not use** to review correct answers — this prompt is for errors only. For general mistake pattern analysis, `learnstudy_mistake_log_reviewer.md` is better; this prompt goes further by generating correction drills and do-over problems.

## Instructions

1. **Collect the error log.**
   - Ask the learner to list their errors: for each, provide the question or problem and their wrong answer
   - Also ask: "Do you know why you got it wrong? If yes, write your diagnosis. If no, write 'unknown.'"
   - Ask: "What subject is this? What type of questions were these? (MCQ, calculation, short answer, essay)"

2. **Classify each error into one of four types.**

   **Type C — Conceptual error:** The learner misunderstood the underlying concept or had a false belief about how something works.
   - Indicators: confidently stated the wrong thing, chose a plausible-but-wrong option that reflects a common misconception, used the right formula in the wrong context
   - Fix: Needs conceptual re-learning (not more practice of the same problem)

   **Type P — Procedural error:** The learner knew the concept but made an error in the procedure (steps, calculations, method).
   - Indicators: set up the problem correctly but made arithmetic error, skipped a step, applied the procedure in the wrong order
   - Fix: Needs repeated procedural practice with a focus on the specific faulty step

   **Type G — Gap error:** The learner simply never learned or encountered this material.
   - Indicators: blank answer, wild guess, "I've never seen this before"
   - Fix: Needs initial learning (read the relevant source material) before any drill

   **Type R — Retrieval/recall error:** The learner knew the material but couldn't retrieve it under time pressure or testing conditions.
   - Indicators: "I knew it right after the test," tip-of-tongue on the answer, correct on homework but wrong on test
   - Fix: Needs more retrieval practice under timed or test-like conditions, not more content study

3. **For each error, deliver a targeted fix.**

   **For Type C:** Show the contrast — the learner's incorrect belief vs. the correct concept. Use a before/after "wrong model → correct model" pair. Then give 2–3 application questions testing the correct understanding.

   **For Type P:** Identify the exact step where the procedure failed. Show the correct step-by-step solution to the original problem. Then give 2 "same type, different numbers" problems for immediate practice.

   **For Type G:** Provide a brief (3–5 sentence) summary of the missing concept. Point to the specific source (textbook section, lecture) where it is covered. Do not drill until the learner has read the source.

   **For Type R:** Do not re-teach the content. Instead, give 3 retrieval practice questions on the same concept, timed (30 seconds each). The goal is recall fluency, not understanding.

4. **Build the do-over problem set.**
   - For each error: generate one "isomorphic" problem — same concept and difficulty, different surface details
   - Label each do-over problem by error type so the learner knows what fix to apply if they get it wrong again
   - Do-over problems should be attempted cold (no notes, no looking back at the fixes)

5. **Generate a correction completion checklist.**
   After the do-over:
   - Passed: error is corrected → schedule in spaced review in 3–5 days
   - Failed again on do-over: error is persistent → flag for extended drilling or seeking instructor help

## Output Format

```
# Error Correction Cycle: [Exam / Quiz Name]
Errors reviewed: N | Date: [today]

## Error Classification

| # | Error/Question | Wrong Answer | Error Type | Severity |
|---|---|---|---|---|
| 1 | [brief] | [learner's wrong answer] | Type C | High |

## Targeted Corrections

### Error #1 — [Type C/P/G/R]: [Topic]
**What went wrong:** ...
**Correction:** [wrong model → correct model for C; step breakdown for P; mini-summary for G; recall drills for R]
**Practice tasks:** (2–3)
1. ...
2. ...

[Repeat for each error]

## Do-Over Problem Set
*(Attempt cold — no notes. Check against corrections only after attempting.)*

**Do-Over #1** [Error type tag]:
[Problem]
[Answer key below separator]

---
## Do-Over Answer Key
1. [Answer]

## Correction Completion Checklist
| Error # | Do-Over Result | Status |
|---|---|---|
| 1 | ✓ / ✗ | Corrected / Persistent |
```

## Example Output

---

**Input:** 4 errors from a Biology MCQ quiz on Cell Biology

---

# Error Correction Cycle: Cell Biology Quiz — Section 3
Errors reviewed: 4 | Date: 2026-05-15

---

## Error Classification

| # | Error/Question | Learner's Wrong Answer | Error Type | Severity |
|---|---|---|---|---|
| 1 | "Which organelle produces ATP via oxidative phosphorylation?" Chose Ribosome | Ribosome | **Type G** | High — never learned this |
| 2 | "Osmosis moves water from ___ to ___ solute concentration" Chose "high to high" | "high to high" | **Type C** | High — false conceptual belief |
| 3 | Calculating membrane surface area — set up correct but arithmetic error in step 3 | Correct setup, wrong arithmetic | **Type P** | Medium |
| 4 | "What is the function of the smooth ER?" Left blank | Blank | **Type R** | Medium — "I knew this right after" |

---

## Targeted Corrections

### Error #1 — Type G: ATP Production (Oxidative Phosphorylation)

**What went wrong:** This concept either was not studied or was not encoded — ribosome is a protein synthesis organelle (not ATP-related). The correct answer is the mitochondrion.

**Before reading any drills:** Read your textbook section on mitochondria and oxidative phosphorylation (10 minutes). The key passage to find: how the electron transport chain and ATP synthase work together in the inner mitochondrial membrane.

**Brief concept summary:**
Mitochondria are the primary sites of ATP production in eukaryotes via oxidative phosphorylation. The inner mitochondrial membrane contains the electron transport chain (ETC) and ATP synthase. Electrons from NADH/FADH₂ are passed down the ETC, pumping H⁺ across the membrane. H⁺ flows back through ATP synthase, driving ATP synthesis (chemiosmosis). Net yield: ~30–32 ATP per glucose.

**Practice tasks (after reading the source):**
1. "Without notes: name the two main components of the inner mitochondrial membrane involved in ATP production."
2. "In your own words, explain how the proton gradient drives ATP synthesis."
3. "A poison blocks ATP synthase. What would happen to ATP production and to the proton gradient?"

---

### Error #2 — Type C: Osmosis Direction

**What went wrong:** The learner believes osmosis moves water from high solute concentration to high solute concentration. This is incorrect — osmosis moves water from LOW solute (high water concentration) to HIGH solute (low water concentration).

**Wrong model → Correct model:**

| | Wrong Belief | Correct Concept |
|---|---|---|
| Direction of water movement | High solute → high solute | **Low solute → high solute** |
| What the solvent does | Moves toward more solute | **Water moves where it is less concentrated** |
| Driving force | Solute gradient | **Water concentration gradient (water activity)** |
| Analogy | (incoherent) | Think: water is "diluting" the concentrated side — it flows toward where it's most needed |

**Why this confusion is common:** The word "osmosis" sounds like "move toward something concentrated," and students conflate solute movement with water movement. Water and dissolved substances move in *opposite* directions during osmosis.

**Practice tasks:**
1. "A red blood cell (0.9% NaCl solution inside) is placed in distilled water. Which direction does water move? Will the cell swell, shrink, or stay the same?"
2. "A plant cell is placed in a highly concentrated salt solution. Describe what happens to the cell, naming the relevant term for each possible outcome (plasmolysis, turgidity, flaccidity)."
3. "Two solutions are separated by a semipermeable membrane: Solution A = 0.5 M glucose, Solution B = 1.5 M glucose. In which direction does water move, and what eventually happens if no pressure is applied?"

---

### Error #3 — Type P: Membrane Surface Area Calculation

**What went wrong:** The problem setup was correct (formula selected, given values identified), but an arithmetic error occurred in Step 3. This is a procedural error — no conceptual relearning needed.

**Step-by-step correct solution:**
*(Using typical values from this type of problem)*

Step 1: Identify shape — spherical cell with radius r = 5 µm
Step 2: Write formula: Surface area = 4πr²
Step 3: Calculate: 4 × π × (5)² = 4 × 3.14159 × 25 = 4 × 78.54 = **314.16 µm²**

Common arithmetic error at Step 3: computing 4 × 25 = 100 before multiplying by π → gives 314 ÷ π × 100, i.e., a computation order error.

**Fix:** Always write out each multiplication step explicitly. Do not combine steps in your head.

**Practice tasks (same procedure, different numbers):**
1. "Calculate the surface area of a spherical bacterium with radius 1.5 µm." (Show each step)
2. "A cell has radius 8 µm. Calculate its volume and surface area. Then compute the surface area-to-volume ratio." (Adds volume formula — extend the procedure)

---

### Error #4 — Type R: Smooth Endoplasmic Reticulum Function

**What went wrong:** Learner knew the answer but could not retrieve it under quiz conditions. The solution is retrieval practice, not content review.

**Functions of the smooth ER (reference — read once, then quiz without looking):**
- Lipid synthesis (phospholipids, cholesterol, steroid hormones)
- Detoxification of drugs and poisons (especially in liver cells)
- Calcium ion storage (important in muscle cells for contraction signaling)
- Carbohydrate metabolism

**Retrieval drills (30 seconds each — timed):**
1. "Name three functions of the smooth endoplasmic reticulum from memory."
2. "Which cell types would have especially abundant smooth ER, and why?"
3. "A student confuses smooth ER with rough ER. What is the key structural and functional difference?"

*(Do not look at the reference above until after all three attempts)*

---

## Do-Over Problem Set
*(Attempt cold — no notes. Do not look back at the Targeted Corrections section.)*

**Do-Over #1** [Type G — Mitochondria]:
"A researcher discovers a new drug that disrupts the electron transport chain in mitochondria. Predict: what happens to ATP levels in the cell and why?"

**Do-Over #2** [Type C — Osmosis]:
"A wilting plant is watered. Explain, using osmosis, why the plant becomes turgid again. Identify the direction of water movement and what drives it."

**Do-Over #3** [Type P — Surface Area Calculation]:
"A spherical cell has a radius of 7 µm. Calculate its surface area. Show each multiplication step separately."

**Do-Over #4** [Type R — Smooth ER]:
"A liver cell is exposed to a high dose of a toxic compound. Which organelle will be most active in detoxifying it, and what other two functions does that organelle serve?"

---

## Do-Over Answer Key

**#1:** ATP levels drop dramatically because the ETC is the source of the proton gradient that drives ATP synthase. Without ETC function, ATP synthase has no proton flow → oxidative phosphorylation stops. Cells must rely on glycolysis only (low yield: 2 ATP vs. 30+).

**#2:** Water moves by osmosis from the soil water (low solute) into the plant cell (higher solute concentration inside vacuole). This is driven by the water concentration gradient. As water enters, the vacuole expands, pushing the cell membrane against the cell wall → turgor pressure → turgidity.

**#3:** SA = 4πr² = 4 × π × 49 = 4 × 3.14159 × 49 = 4 × 153.94 = 615.75 µm²

**#4:** Smooth ER (liver cells have abundant smooth ER for drug detoxification). Other functions: lipid synthesis, calcium ion storage.

---

## Correction Completion Checklist

After completing the do-over, record:

| Error # | Topic | Do-Over Result | Status |
|---|---|---|---|
| 1 | Mitochondria / ATP | ✓ / ✗ | Corrected / Persistent |
| 2 | Osmosis direction | ✓ / ✗ | Corrected / Persistent |
| 3 | Surface area calc | ✓ / ✗ | Corrected / Persistent |
| 4 | Smooth ER | ✓ / ✗ | Corrected / Persistent |

- **Corrected errors:** Schedule for spaced review in 3–5 days
- **Persistent errors:** These need instructor help or a deeper re-study cycle — do not just repeat the drill

---

## False-Positive Prevention

**❌ DON'T** classify every error as "conceptual" — that assumption leads to re-teaching content when procedural or retrieval practice would be more effective.

**✅ DO** use the four-type classification and assign the most parsimonious error type: start with Type R (retrieval) if the learner says "I knew it right after" before moving to conceptual diagnoses.

**❌ DON'T** give the same question as the do-over — learners can memorize the answer to the exact question without learning the underlying concept.

**✅ DO** generate isomorphic do-over problems — same concept and structure, different surface details (different numbers, different scenario).

**❌ DON'T** skip the do-over phase — correction without testing whether the correction worked is a common failure mode in error review.

**✅ DO** require the do-over to be completed cold before checking the answer key.

**❌ DON'T** treat a successful do-over as permanent mastery — it confirms initial correction, not long-term retention.

**✅ DO** schedule a spaced review check 3–5 days later for all corrected errors.

## Quality Criteria

- [ ] Every error is classified into one of four types (C/P/G/R) with justification
- [ ] Fix type matches error type (conceptual re-learning for C, step practice for P, source reference for G, timed retrieval for R)
- [ ] Do-over problems are isomorphic (same concept, different surface) — not identical to original
- [ ] Do-over answer key is separated from the problems
- [ ] Correction completion checklist is included with next steps for persistent errors

## Techniques Used

- **ST-01 (Clear Objective Statement):** Objective specifies the workflow endpoint (do-over problem set confirming correction)
- **ST-02 (Structured Sequential Instructions):** Five-step process from error classification to do-over completion
- **ED-02 (Progressive Exercise Generation):** Do-over problems are calibrated to the same difficulty as the original — not easier — to confirm true correction
- **NE-04 (Good vs Bad Example Calibration):** Wrong model → correct model pairs (for Type C errors) make the contrast explicit
- **QA-12 (False Positives Identification):** Four-type classification prevents the false positive of treating all errors as conceptual when they may be procedural or retrieval failures
