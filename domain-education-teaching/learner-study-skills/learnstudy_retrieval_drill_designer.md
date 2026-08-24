---
title: "Retrieval Drill Designer"
category: education-teaching/learner-study-skills
description: "Designs a multi-round retrieval practice drill sequence: generates questions at increasing difficulty, alternates formats (cued recall, free recall, application, transfer), and tracks which concepts have been tested."
techniques:
  - ST-01
  - ST-02
  - ED-02
  - ED-03
  - QA-01
difficulty: intermediate
tags:
  - retrieval-practice
  - active-recall
  - drill
  - spaced-practice
  - interleaving
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/learner-study-skills/learnstudy_active_recall_from_notes.md
  - domain-education-teaching/learner-study-skills/learnstudy_practice_test_generator.md
  - domain-education-teaching/learner-study-skills/learnstudy_self_quiz_loop.md
---

## Objective

Design a structured retrieval drill sequence for a set of concepts — generating questions at four difficulty levels, alternating retrieval formats to prevent false fluency, and tracking concept coverage across multiple rounds.

## When to Use

- When the learner has studied material once and is ready to practice retrieval (not during initial encoding)
- When a topic has been reviewed but retention is uncertain — drill strengthens the memory trace
- When preparing for an exam that includes application and transfer questions (not just recall)
- When passive review (re-reading) has been the main study strategy and active recall is needed

**Do not use** before the learner has done any initial study — retrieval practice requires something to retrieve. Also do not use `learnstudy_active_recall_from_notes.md` instead — that prompt generates one-shot questions; this prompt designs a multi-round drill system.

## Instructions

1. **Collect inputs.**
   - Ask for the concept list or topic (paste notes, a chapter summary, or a list of concepts to drill)
   - Ask: "How many concepts or topics should be included in the drill?"
   - Ask: "Roughly how long is this study session? (to set number of rounds)"
   - Ask: "What format is the exam you're preparing for?" (MCQ, short answer, problem-solving, essay, clinical)

2. **Organize concepts into drill groups.**
   - Group 2–4 related concepts per drill cluster (interleaving related concepts prevents false fluency from massed practice)
   - If concepts are clearly sequential (A must precede B), order them accordingly within the cluster
   - Label each cluster with a theme

3. **Design four difficulty levels for each concept.**

   **Level 1 — Cued recall:** Provide a strong contextual cue; learner supplies the answer
   - "The [term] is defined as ___"
   - "Name the [term] for the process that does X"

   **Level 2 — Free recall:** No cues; learner generates the answer entirely
   - "What is [term]? Describe it."
   - "Explain [concept] in your own words."

   **Level 3 — Application:** Learner applies the concept to a new but familiar-type scenario
   - "Given [scenario], what would [concept] predict?"
   - "If [condition changes], how does [concept] respond?"

   **Level 4 — Transfer:** Learner applies concept to a genuinely novel or cross-domain scenario
   - "A [unfamiliar context] shows [pattern]. How does [concept] explain this?"
   - "Design a simple experiment that could test [concept]"

4. **Build the drill sequence across 3 rounds.**

   **Round 1 (15–20 min):** Level 1–2 questions for all concepts. Goal: baseline retrieval. Fast pass.
   **Round 2 (20–25 min):** Level 2–3 questions, interleaved across clusters. Goal: strengthen and mix.
   **Round 3 (15–20 min):** Level 3–4 questions only, mixed order. Goal: application and transfer.

   After each round: learner marks each concept as ✓ (recalled correctly), △ (partial), ✗ (failed). Failed concepts are re-queued in the next round.

5. **Generate all questions explicitly.**
   - Write out the full text of each question (not just placeholders)
   - For Level 3–4, ensure the scenario is novel enough that the learner cannot answer by pattern-matching to examples from the lecture

6. **Include a concept coverage tracker.**
   A table showing which concepts appear in which rounds and at which level, so the learner can confirm nothing was skipped.

7. **After the drill, provide a 3-sentence performance summary template.**
   - What went well (concepts recalled correctly in Round 1)
   - What needs another round (concepts marked △ or ✗)
   - Recommended next action

## Output Format

```
# Retrieval Drill: [Topic]
Session length: [N min] | Rounds: 3 | Concepts: N

## Concept Clusters
Cluster A: [Concept 1, Concept 2, Concept 3]
Cluster B: [Concept 4, Concept 5]

## Round 1 — Cued and Free Recall (Level 1–2)
[Cluster A]
Q1. [Level 1 — Cued] ...
Q2. [Level 2 — Free recall] ...
[Cluster B]
Q3. ...
[Etc.]

## Round 2 — Application (Level 2–3, Interleaved)
Q1. [Level 3 — Application] ...
Q2. [Level 2 — Free recall of different concept] ...
[Interleaved across clusters]

## Round 3 — Transfer (Level 3–4, Mixed Order)
Q1. [Level 4 — Transfer] ...
Q2. [Level 3 — Application] ...

## Concept Coverage Tracker
| Concept | R1 Level | R2 Level | R3 Level | Status |
|---|---|---|---|---|
| [Concept 1] | L1 | L2 | L4 | __ |

## Post-Drill Summary Template
- Recalled well: ...
- Needs re-drill: ...
- Next action: ...
```

## Example Output

---

**Input:** 6 concepts from an Introductory Economics lecture on Supply and Demand | 60-minute session | Exam format: MCQ + short answer

---

# Retrieval Drill: Supply and Demand
Session length: 60 min | Rounds: 3 | Concepts: 6

## Concept Clusters

**Cluster A — Market Mechanics:** Law of Demand, Law of Supply, Equilibrium
**Cluster B — Shifts and Responses:** Price Elasticity, Consumer Surplus, Producer Surplus

---

## Round 1 — Cued and Free Recall (15 min)
*Attempt each from memory. Mark ✓ (correct), △ (partial), ✗ (failed) before checking.*

**[Cluster A]**

**Q1.** [Level 1 — Cued] "According to the law of demand, when the price of a good rises, the quantity demanded ___."

**Q2.** [Level 1 — Cued] "The law of supply states that as price increases, quantity supplied ___."

**Q3.** [Level 2 — Free recall] "Without any cues: explain what market equilibrium means and what happens if a market is not in equilibrium."

**[Cluster B]**

**Q4.** [Level 1 — Cued] "Price elasticity of demand measures the ___ of quantity demanded to a ___ in price."

**Q5.** [Level 2 — Free recall] "Define consumer surplus in your own words. What does it represent on a supply-demand graph?"

**Q6.** [Level 2 — Free recall] "Explain producer surplus. How does it differ from profit?"

---

*Mark each: ✓ / △ / ✗. Failed questions are automatically re-queued in Round 2.*

---

## Round 2 — Application (20 min, Interleaved)
*Questions from both clusters are now mixed. This is intentional — interleaving prevents you from "riding" the context of the previous question.*

**Q1.** [Level 3 — Application, Cluster A] "A drought destroys 30% of the wheat crop. Using a supply-demand diagram (describe it in words if you cannot draw), explain what happens to the equilibrium price and quantity of bread."

**Q2.** [Level 2 — Free recall, Cluster B] "What makes a good 'price elastic' vs. 'price inelastic'? Give one characteristic of each."

**Q3.** [Level 3 — Application, Cluster A] "The government introduces a price ceiling on gasoline set below the current equilibrium price. What happens to quantity demanded and quantity supplied? What economic term describes this outcome?"

**Q4.** [Level 3 — Application, Cluster B] "A tax is placed on the seller of a product with highly inelastic demand. Who bears most of the tax burden — buyers or sellers? Explain using elasticity reasoning."

**Q5.** [Level 2 — Free recall, Cluster A] "Name three factors (other than price) that can shift the demand curve to the right."

**Q6.** [Level 3 — Application, Cluster B] "On a supply-demand diagram with equilibrium at P*=10, Q*=100, a price floor is set at P=12. Describe the areas of consumer surplus and producer surplus after the floor is imposed vs. before."

---

## Round 3 — Transfer (25 min, Mixed Order)
*These scenarios are novel — you will not find them word-for-word in your notes.*

**Q1.** [Level 4 — Transfer] "A streaming music platform offers a new 'artist' tier where listeners can pay more to support specific musicians directly. A music economist argues this creates a mechanism that converts consumer surplus into revenue. Using consumer surplus theory, explain whether this argument is logically sound."

**Q2.** [Level 4 — Transfer] "A study shows that a 10% increase in cigarette prices leads to only a 2% decrease in cigarettes purchased among adults but a 12% decrease among teenagers. What does this tell us about the price elasticity of demand for each group? What policy implication follows?"

**Q3.** [Level 3 — Application] "Two substitute goods: coffee and tea. The price of coffee doubles due to a supply disruption. Walk through the full sequence of effects: What happens to coffee demand? What happens to tea demand? What happens to the tea market equilibrium?"

**Q4.** [Level 4 — Transfer] "Economists argue that rent control (a price ceiling on rent) causes housing shortages over time. Design a brief verbal explanation you could give to someone who has never taken economics, using only the supply-demand concepts from this drill."

**Q5.** [Level 3 — Application] "Calculate the price elasticity of demand given: original price = $20, new price = $25 (a 25% increase), original quantity = 400 units, new quantity = 300 units. Is this good elastic or inelastic? Interpret what this means for a business's revenue decision."

---

## Concept Coverage Tracker

| Concept | R1 | R2 | R3 | My Status |
|---|---|---|---|---|
| Law of Demand | L1 | L2 (Q5, shifts) | L3 (Q3, substitute chain) | ___ |
| Law of Supply | L1 | L3 (Q1, drought) | L3 (Q3) | ___ |
| Equilibrium | L2 | L3 (Q3, price ceiling) | L4 (Q4, rent control) | ___ |
| Price Elasticity | L1 | L3 (Q4, tax incidence) | L4 (Q2, cigarettes) + L3 (Q5, calc) | ___ |
| Consumer Surplus | L2 | L3 (Q6, price floor) | L4 (Q1, streaming) | ___ |
| Producer Surplus | L2 | L3 (Q6) | L3 (Q3) | ___ |

*Fill in your status after Round 3: ✓ Solid / △ Shaky / ✗ Needs full re-study*

---

## Post-Drill Summary Template

After completing all three rounds, fill in:

- **Recalled well (✓ in all 3 rounds):** [Topic names] — These are solid. Schedule a maintenance review in 5–7 days.
- **Shaky (△ in any round):** [Topic names] — Re-drill at Level 2–3 in your next session.
- **Failed (✗ in any round):** [Topic names] — Return to notes/lecture for these before drilling again. Drilling a concept you never encoded is ineffective.
- **Next action:** [One specific step — e.g., "Re-read the price elasticity section, then redo Q2 and Q4 from Round 2"]

---

## False-Positive Prevention

**❌ DON'T** confuse recognition with recall — if the learner can identify the right answer when shown it, that is not evidence they can recall it from scratch.

**✅ DO** ensure Round 1 questions are answered before checking notes (close the book first), even for Level 1 cued questions.

**❌ DON'T** skip interleaving in Round 2 by grouping all Cluster A questions then all Cluster B — massed practice by topic creates the illusion of fluency.

**✅ DO** explicitly mix clusters in Round 2, explaining to the learner why the ordering is intentional.

**❌ DON'T** use the same scenarios from the lecture for Level 3–4 questions — learners can recall the story without understanding the concept.

**✅ DO** generate genuinely novel application and transfer scenarios, not paraphrases of lecture examples.

**❌ DON'T** allow a ✓ on Round 1 to mean the concept is mastered — Round 1 is cued recall (the easiest format). Only consistent ✓ across all three rounds indicates solid retrieval.

**✅ DO** require ✓ in Round 3 (free recall + application) before concluding a concept is ready for maintenance-only review.

## Quality Criteria

- [ ] Concepts are grouped into clusters (not drilled individually in isolation)
- [ ] All four question levels are present (L1 cued, L2 free, L3 application, L4 transfer)
- [ ] Round 2 is interleaved across clusters (not sequential by cluster)
- [ ] Level 3–4 scenarios are genuinely novel (not lecture example paraphrases)
- [ ] Concept coverage tracker is included and links each concept to its question appearances
- [ ] Learner marks ✓/△/✗ after each round
- [ ] Post-drill summary template is provided

## Techniques Used

- **ST-01 (Clear Objective Statement):** Objective distinguishes this from one-shot question generation — it is a multi-round system
- **ST-02 (Structured Sequential Instructions):** Seven-step design process ensures nothing is skipped
- **ED-02 (Progressive Exercise Generation):** Four difficulty levels build from cued recall to genuine transfer
- **ED-03 (Guided Discovery):** Transfer questions require learners to derive answers, not retrieve memorized responses
- **QA-01 (Self-Verification):** Concept coverage tracker confirms every concept is tested at multiple levels before the drill ends
