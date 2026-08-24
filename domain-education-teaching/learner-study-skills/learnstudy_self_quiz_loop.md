---
title: "Self-Quizzing Loop"
category: education-teaching/learner-study-skills
description: "Runs a structured self-quizzing protocol across multiple concepts: predict → attempt → reveal → evaluate → log. Generates a session summary with pass/fail per concept and recommended next session focus."
techniques:
  - ST-01
  - ST-02
  - ED-03
  - QA-04
  - CM-10
difficulty: intermediate
tags:
  - self-quizzing
  - metacognition
  - retrieval-practice
  - session-tracking
  - active-recall
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/learner-study-skills/learnstudy_retrieval_drill_designer.md
  - domain-education-teaching/learner-study-skills/learnstudy_confidence_calibration.md
  - domain-education-teaching/learner-study-skills/learnstudy_weak_area_diagnosis.md
  - domain-education-teaching/teaching_study_knowledge_tester.md
---

## Objective

Guide the learner through a structured self-quizzing loop with built-in metacognitive checkpoints: predict confidence, attempt recall, reveal the answer, evaluate accuracy, and log the result — then summarize session performance and plan the next session.

## When to Use

- During regular study sessions as a replacement for passive re-reading
- When a learner wants to maintain control over the quizzing pace (vs. an AI-driven session)
- When building a cumulative log of concept mastery across multiple sessions
- As a daily or weekly study habit that generates persistent performance data over time

**Do not use** as a one-off quiz generator — this is a protocol for a structured session with tracking. For a standalone practice test, use `learnstudy_practice_test_generator.md`. For an AI-driven interactive quiz, use `teaching_study_knowledge_tester.md`.

## Instructions

1. **Set up the session.**
   - Ask: "Which concepts are you quizzing yourself on today? (list them)"
   - Ask: "Have you done a self-quiz session on any of these concepts before? If yes, what was your last result?"
   - Ask: "How many minutes do you have?"
   - Confirm: "I'll guide you through 5 steps for each concept: Predict → Attempt → Reveal → Evaluate → Log."

2. **For each concept, run the 5-step loop.**

   **Step 1 — Predict:**
   Before any recall attempt, ask: "On a scale of 1–5, how confident are you that you can correctly explain this concept right now? (1 = not at all, 5 = completely sure)"
   Record: Concept + Predicted confidence

   **Step 2 — Attempt:**
   The learner writes or says their answer to the quiz question (provided below).
   Rule: No notes. No looking anything up. Set a timer if needed (2–3 min max per concept).

   **Step 3 — Reveal:**
   Show the model answer (or tell the learner to look up the answer in their notes/textbook).

   **Step 4 — Evaluate:**
   Learner rates their attempt honestly:
   - **Pass (✓):** Answer was substantially correct — key elements present
   - **Partial (△):** Correct in general direction but missing key details or had a significant error
   - **Fail (✗):** Substantially incorrect or blank

   Also record the **calibration gap:** Predicted − Actual (Pass=5, Partial=3, Fail=1)
   - Large positive gap = overconfidence on this concept
   - Large negative gap = underconfidence on this concept

   **Step 5 — Log:**
   Record: Concept | Predicted | Result | Calibration Gap | Notes (what was missed or wrong)

3. **Complete the loop for all concepts in the session.**
   If the learner fails a concept (✗), queue it for a second pass at the end of the session.

4. **Run a second pass on failed concepts only.**
   - This time: free recall without the Predict step (already calibrated)
   - Give a different but equivalent question (not the same wording — forces real recall, not echo)
   - Record second-pass result separately

5. **Generate the session summary.**
   - Total concepts quizzed
   - Pass / Partial / Fail counts
   - Pass rate %
   - Calibration accuracy (how close were predictions to actuals on average)
   - Concepts ready for spacing (passed on first attempt → schedule in 4–7 days)
   - Concepts needing re-study (failed on both attempts → return to notes before next quiz)
   - Concepts for re-drill (partial or failed first but passed second → quiz again in 2–3 days)

6. **Recommend next session.**
   - Provide a 3-sentence next session plan based on the log
   - Include: what to re-study, what to re-quiz, and when

## Output Format

```
# Self-Quiz Session Log
Date: [today] | Session #: [N] | Concepts: [count] | Time: [N min]

## Concept Queue
1. [Concept name]
2. ...

---

## Loop Execution

### Concept 1: [Name]
**Question:** [Quiz question]
**Step 1 — Prediction:** ___/5
**Step 2 — Attempt:** [Learner writes here]
**Step 3 — Model answer:** [Provided here]
**Step 4 — Evaluation:** ✓ / △ / ✗
**Calibration gap:** [Predicted − Actual]
**Notes:** [What was missed, if anything]

[Repeat for all concepts]

---
## Second Pass (Failed Concepts)

### Concept [X] — Second Attempt
**Different question:** [Alternate wording]
**Result:** ✓ / △ / ✗

---
## Session Summary

| Concept | Predicted | Result | Gap | Status |
|---|---|---|---|---|
| ... | 3 | △ | +0 | Re-drill |

**Overall:**
- Pass rate: N% (N/N)
- Mean calibration gap: [+/− N]
- Systematic bias: Overconfident / Underconfident / Well-calibrated

**Concept Status:**
- ✅ Ready to space (quiz in 4–7 days): [list]
- 🔁 Re-drill soon (quiz in 2–3 days): [list]
- 📖 Re-study first (return to notes before quizzing): [list]

## Next Session Plan
...
```

## Example Output

---

**Input:** Microbiology — 5 concepts — 30 minutes — Session #2 for this topic

---

# Self-Quiz Session Log
Date: 2026-05-15 | Session #: 2 | Concepts: 5 | Time: 30 min

## Concept Queue
1. Gram-positive vs. Gram-negative cell wall structure
2. Mechanisms of antibiotic resistance
3. Viral replication cycle (lytic vs. lysogenic)
4. Koch's postulates
5. Quorum sensing

---

## Loop Execution

### Concept 1: Gram-positive vs. Gram-negative cell wall structure

**Question:** Explain the structural differences between Gram-positive and Gram-negative bacteria. Why does this difference affect how they respond to penicillin?

**Step 1 — Prediction:** Write your confidence: ___/5
*(Learner wrote: 4)*

**Step 2 — Attempt:** *(Learner attempts from memory — 2 min)*

**Step 3 — Model Answer:**
- Gram-positive: thick peptidoglycan layer (20–80 nm), no outer membrane, retains crystal violet stain → appears purple
- Gram-negative: thin peptidoglycan layer (2–7 nm) + outer membrane (lipopolysaccharide) + periplasmic space → appears pink/red after counterstain
- Penicillin inhibits cell wall synthesis (peptidoglycan cross-linking); Gram-positives with thick peptidoglycan walls are more susceptible. Gram-negatives' outer membrane limits penicillin entry, and many have β-lactamase enzymes.

**Step 4 — Evaluation:** Mark one: ✓ / △ / ✗
*(Learner marks △ — got the structure right but forgot the penicillin mechanism detail)*

**Calibration gap:** Predicted 4 (out of 5) → Actual △ (scored as 3). Gap = +1 (slight overconfidence on the detail component)

**Notes:** Missed that Gram-negatives have β-lactamase; knew the structural difference well.

---

### Concept 2: Mechanisms of antibiotic resistance

**Question:** Without looking at notes, name and briefly explain three distinct mechanisms by which bacteria develop or acquire antibiotic resistance.

**Step 1 — Prediction:** ___/5 *(Learner wrote: 3)*

**Step 3 — Model Answer:**
1. **Enzymatic inactivation** — bacteria produce enzymes (e.g., β-lactamase) that destroy the antibiotic
2. **Efflux pumps** — bacteria actively pump the antibiotic out of the cell before it can act
3. **Target modification** — bacteria alter the antibiotic's binding site (e.g., modified PBPs in MRSA)
4. **Reduced permeability** — mutations reduce the porins that the antibiotic uses to enter the cell
5. **Bypass mechanism** — acquire an alternative metabolic pathway that bypasses the inhibited target

**Step 4 — Evaluation:** ✓ / △ / ✗ *(Learner marks ✓ — recalled 3 mechanisms correctly)*

**Calibration gap:** Predicted 3, Actual ✓ (5). Gap = −2 (underconfident — knew more than expected)

**Notes:** Surprised to recall efflux pumps clearly. Underestimated retention from last session.

---

### Concept 3: Viral replication cycle (lytic vs. lysogenic)

**Question:** Explain what happens in each phase: lytic cycle and lysogenic cycle. What determines which cycle a phage enters?

**Step 1 — Prediction:** ___/5 *(Learner wrote: 2)*

**Step 3 — Model Answer:**
- **Lytic cycle:** Phage injects DNA → hijacks host machinery → replicates phage DNA and proteins → assembles new phage particles → lyses host cell → releases virions
- **Lysogenic cycle:** Phage DNA integrates into host chromosome as a prophage → replicates silently with host for many generations → can be induced (e.g., by UV light or stress) to enter lytic cycle
- **Determination:** Host cell's nutritional/stress state; CI repressor protein (in lambda phage) represses lytic genes → lysogeny. If repressor is inactivated (SOS response), lytic cycle begins.

**Step 4 — Evaluation:** ✓ / △ / ✗ *(Learner marks △ — described both cycles but forgot CI repressor / SOS response)*

**Calibration gap:** Predicted 2, Actual △ (3). Gap = −1 (slight underconfidence — knew more than expected)

---

### Concept 4: Koch's Postulates

**Question:** State Koch's four postulates and explain why they are sometimes difficult to apply in modern microbiology.

**Step 1 — Prediction:** ___/5 *(Learner wrote: 5)*

**Step 3 — Model Answer:**
1. The microorganism is found in all cases of the disease
2. The microorganism is isolated from the diseased host and grown in pure culture
3. The cultured microorganism causes disease when introduced into a healthy host
4. The microorganism is re-isolated from the inoculated host and matches the original
- Limitations: many pathogens cannot be cultured (e.g., viruses, M. leprae); healthy carriers can harbor the organism; some diseases are polymicrobial; ethical constraints on human inoculation

**Step 4 — Evaluation:** ✓ / △ / ✗ *(Learner marks ✓ — recalled all four and limitations)*

**Calibration gap:** Predicted 5, Actual ✓ (5). Gap = 0 (perfectly calibrated)

---

### Concept 5: Quorum Sensing

**Question:** Define quorum sensing and explain one concrete example of behavior it regulates.

**Step 1 — Prediction:** ___/5 *(Learner wrote: 2)*

**Step 3 — Model Answer:**
- Quorum sensing: cell-density-dependent gene regulation mechanism in bacteria. Bacteria release chemical signal molecules (autoinducers). When population reaches a threshold density, autoinducer concentration reaches a critical level → triggers coordinated gene expression
- Example: Vibrio fischeri bioluminescence — bacteria only luminesce when colony density is sufficient (in symbiosis with squid); at low density, no light is produced. Also: biofilm formation, virulence factor expression in S. aureus, sporulation

**Step 4 — Evaluation:** ✓ / △ / ✗ *(Learner marks ✗ — blanked on autoinducers, gave only vague definition)*

**Calibration gap:** Predicted 2, Actual ✗ (1). Gap = +1 (overconfident — even at low predicted confidence, still overestimated)

---

## Second Pass — Failed Concepts

### Concept 5 (Quorum Sensing) — Second Attempt

**Different question:** "A researcher observes that a bacterium becomes pathogenic only in dense colonies but not in isolated cells. What mechanism is most likely responsible, and what molecular signal is involved?"

*(Learner attempts from memory after reviewing the model answer)*

**Result:** △ — recalled the mechanism but still could not name autoinducers specifically

---

## Session Summary

| Concept | Predicted | Result | Calibration Gap | Status |
|---|---|---|---|---|
| Gram+/− cell wall | 4 | △ | +1 | 🔁 Re-drill |
| Antibiotic resistance | 3 | ✓ | −2 | ✅ Space |
| Viral replication | 2 | △ | −1 | 🔁 Re-drill |
| Koch's postulates | 5 | ✓ | 0 | ✅ Space |
| Quorum sensing | 2 | ✗→△ | +1 | 🔁 Re-drill |

**Overall:**
- Pass rate: 40% (2/5 passed first attempt)
- Mean calibration gap: −0.4 (very slightly underconfident overall — reasonable)
- Systematic bias: **Well-calibrated** — no large systematic pattern

**Concept Status:**
- ✅ **Ready to space** (quiz in 5–7 days): Antibiotic resistance, Koch's postulates
- 🔁 **Re-drill** (quiz in 2–3 days): Gram+/− detail, Viral replication CI repressor, Quorum sensing autoinducers
- 📖 **Re-study first:** None — all concepts were at least partially retained

## Next Session Plan

In 2 days: Re-quiz Gram+/− (specifically the penicillin mechanism and β-lactamase), viral replication (CI repressor/SOS response), and quorum sensing (autoinducers) — 15 minutes, 3 concepts only.

In 5–7 days: Maintenance pass on antibiotic resistance and Koch's postulates to confirm they are still solid before spaced review extends further.

Before re-quizzing quorum sensing: spend 10 minutes re-reading the autoinducer section only — not the whole chapter. The mechanism is retained; the molecular vocabulary is the gap.

---

## False-Positive Prevention

**❌ DON'T** allow the prediction step to be skipped — confidence prediction is the mechanism by which calibration is built over time. Without it, the log has no metacognitive value.

**✅ DO** enforce prediction before every attempt; if the learner skips it, prompt them before revealing the answer.

**❌ DON'T** evaluate recall charitably — "I kind of knew it" should default to △, not ✓. Generous self-scoring defeats the purpose of honest assessment.

**✅ DO** give a clear rubric: ✓ requires substantially correct key elements present; △ requires correct direction but missing details; ✗ is incorrect or blank.

**❌ DON'T** use the same question wording on the second pass — this tests word-level memory, not concept recall.

**✅ DO** generate a genuinely different question for the second pass that tests the same concept from a different angle.

**❌ DON'T** recommend "re-study everything" — the log's value is identifying the *specific* gap within a concept, not just the concept itself.

**✅ DO** use the Notes column to identify the precise sub-component that failed, and target re-study to that gap only.

## Quality Criteria

- [ ] Prediction is recorded before every attempt (not after)
- [ ] Model answer is provided for every concept
- [ ] Learner evaluates using ✓/△/✗ rubric (not free-form)
- [ ] Calibration gap is computed per concept
- [ ] Failed concepts get a second pass with a different question
- [ ] Session summary includes pass rate, calibration accuracy, and 3-tier status (space / re-drill / re-study)
- [ ] Next session plan is specific (which concepts, when, how long)

## Techniques Used

- **ST-01 (Clear Objective Statement):** Objective specifies the 5-step loop as the core mechanism, distinguishing this from passive quiz delivery
- **ST-02 (Structured Sequential Instructions):** 5-step loop (Predict → Attempt → Reveal → Evaluate → Log) creates a consistent, repeatable protocol
- **ED-03 (Guided Discovery):** Prediction step forces the learner to estimate their own knowledge state before seeing the answer — learning is self-generated, not told
- **QA-04 (Uncertainty Acknowledgment):** Calibration gap calculation makes prediction accuracy explicit and trackable
- **CM-10 (Memory Scaffold Architecture):** Session log format creates a persistent, updatable performance record across sessions
