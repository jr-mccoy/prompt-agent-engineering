---
title: "Law Rule Application Drill"
category: education-teaching/learner-study-skills
description: "Black-letter law retrieval and application drill: prompts the learner to state the rule precisely, then applies it to a short fact set. Covers MBE and MEE subjects. Separates rule recall from rule application to diagnose which skill is weak."
techniques:
  - ST-01
  - ST-02
  - ED-02
  - NE-04
  - QA-01
difficulty: advanced
tags:
  - law
  - bar-exam
  - MBE
  - MEE
  - black-letter-law
  - rule-application
  - legal-analysis
  - IRAC
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/learner-study-skills/learnstudy_law_issue_spotting.md
  - domain-education-teaching/learner-study-skills/learnstudy_retrieval_drill_designer.md
  - domain-education-teaching/learner-study-skills/learnstudy_practice_test_generator.md
---

## Objective

Generate black-letter law retrieval and application practice: the learner first states the rule from memory (element-by-element), then applies it to a short fact set, then receives feedback on both the accuracy of the rule statement and the quality of the application. By separating these two steps, the drill diagnoses whether the learner's weakness is rule recall (knowing the elements), rule application (connecting elements to facts), or both.

## When to Use

- Preparing for the MBE (Multistate Bar Examination) or MEE (Multistate Essay Examination)
- When a learner can recognize correct answers on MCQs but cannot generate analysis on essay questions
- When a learner knows rules in general terms but applies them inconsistently because the element structure is imprecise
- When a learner's essays receive feedback like "conclusory" or "not enough rule application" — a signal that element-level analysis is being skipped

**Do not use** for issue-spotting practice — use `learnstudy_law_issue_spotting.md` for that skill. This drill assumes the legal issue has already been identified; it focuses on stating and applying the governing rule.

## Instructions

1. **Collect inputs.**
   - Ask: "Which subject area(s)? (Contracts, Torts, Constitutional Law, Criminal Law, Evidence, Property, Civil Procedure, Business Associations, Family Law, Wills & Trusts, Conflict of Laws)"
   - Ask: "Which jurisdiction framework? (MBE majority rules, MEE, specific state)"
   - Ask: "What specific rule or doctrine? (e.g., 'negligence elements', 'rule against perpetuities', 'hearsay and the business records exception', or 'let the system choose')"
   - Ask: "What difficulty level? (1 = core doctrine, familiar elements | 2 = rule with exceptions or multi-part test | 3 = minority/majority split, nuanced application)"
   - Ask: "Drill focus: rule recall only, application only, or both? (Default: both)"

2. **Structure each drill item in three phases.**

   **Phase 1 — Rule Recall:**
   "State the rule for [doctrine] as precisely as you can. List every element."
   - Learner writes the rule from memory before seeing any fact pattern
   - The learner should not see Phase 2 until Phase 1 is committed

   **Phase 2 — Application:**
   Present a short fact set (75–150 words). The fact set must:
   - Include at least one fact that clearly satisfies an element
   - Include at least one fact that raises a genuine question as to whether an element is satisfied
   - Include at least one fact that does NOT satisfy an element (so the analysis is not simply "all elements met")
   "Apply the rule element-by-element to these facts. For each element: state the element, apply the specific facts, and state whether that element is met."

   **Phase 3 — Model Answer:**
   Reveal:
   a. **Model rule statement** — precise element-by-element formulation, majority rule labeled, minority rule noted if relevant
   b. **Rule accuracy feedback** — compare learner's stated rule to model: elements missing, elements misstated, elements correct
   c. **Model application** — element-by-element analysis, specifying which facts satisfy/fail each element and why
   d. **Application feedback** — identify whether learner: applied all elements; used specific facts (not generalizations); addressed contested elements rather than glossing over them; reached a supported conclusion

3. **Include a contrast pair for difficulty 2–3 items.**
   For any rule with a common confusable doctrine (e.g., assault vs. battery, express warranty vs. implied warranty of merchantability, adverse possession vs. prescriptive easement), add:
   - "Contrast: How does [Rule A] differ from [Rule B]? What fact would change the outcome from one to the other?"
   - Provide the model distinction after the learner attempts it

4. **Run a session summary.**
   After all drill items are complete:
   - Rule recall accuracy: elements correct / total elements across all rules
   - Application quality: did the learner reach element-level analysis on each item? (Y/N per item)
   - Identify the weakest rule area (lowest recall accuracy or most missed applications)
   - Recommend: if recall < 70%, re-study the rule before more application drills; if recall is strong but application is weak, practice writing element-by-element analysis under time pressure

## Output Format

```
# Law Rule Application Drill: [Subject]
Jurisdiction: [MBE/MEE/State] | Difficulty: [1/2/3] | Items: N

---

## Item [#]: [Doctrine Name]

**Phase 1 — Rule Recall**
State the rule for [doctrine] element-by-element. Write before advancing.

Rule (from memory):
Element 1: ___
Element 2: ___
[...]

[PAUSE — commit your rule statement before reading Phase 2]

---

**Phase 2 — Application**
[Fact set — 75–150 words]

Apply the rule element-by-element. For each element:
→ State the element
→ Apply the specific facts
→ Conclude: met / not met / disputed

[Write your analysis before reading Phase 3]

---

**Phase 3 — Model Answer**

*Model Rule:*
[Precise element-by-element formulation — majority rule labeled]
[Minority rule or jurisdiction split noted if relevant]

*Rule Accuracy Feedback:*
- Element(s) you stated correctly: [list]
- Element(s) you missed: [list + brief explanation]
- Element(s) you misstated: [correction]

*Model Application:*
Element 1 — [name]: [Facts X and Y establish this because...] → Met
Element 2 — [name]: [Fact Z does not satisfy this because...] → Not Met
[...]
Conclusion: [party] prevails/does not prevail on [claim] because [dispositive element].

*Application Feedback:*
- Did you reach element-level analysis? ✓/✗
- Did you use specific facts or generalizations? ✓/✗
- Did you address the contested element? ✓/✗

---

*Contrast Pair (Difficulty 2–3):*
How does [Rule A] differ from [Rule B]?
What single fact would shift the outcome from one to the other?

[Model distinction — reveal after learner attempts]

---

## Session Summary

| Item | Rule Recall | Application Quality | Weakest point |
|---|---|---|---|
| [Doctrine] | [X/Y elements correct] | [Element-level Y/N] | [Specific gap] |

**Recall average:** [%]
**Application rate:** [Items with element-level analysis / total]
**Priority re-study:** [Rule with lowest accuracy]
**Drill adjustment:** [Recall gap → re-study; Application gap → timed element-level writing practice]
```

## Example Output

---

**Input:** Torts — MBE majority rules — Negligence — Difficulty 2 — Both phases

---

# Law Rule Application Drill: Torts
Jurisdiction: MBE Majority | Difficulty: 2 | Items: 1 (sample)

---

## Item 1: Negligence

**Phase 1 — Rule Recall**

State the rule for negligence, element-by-element, from memory. Include any sub-elements.

Rule (from memory):
Element 1: ___
Element 2: ___
Element 3: ___
Element 4: ___

[PAUSE — write your rule before reading Phase 2]

---

**Phase 2 — Application**

Marcus is a licensed electrician who was hired by Homeowner to rewire her kitchen. During the job, Marcus noticed that an outlet near the sink was not GFCI-protected, as required by the current National Electrical Code (NEC). The outlet was functional and showed no defects. Marcus did not mention this to Homeowner and did not replace it, reasoning that it was outside the scope of his rewiring contract. Six weeks later, Homeowner's teenage daughter is electrocuted when the outlet comes into contact with water from an overflowing sink. She survives but sustains permanent hand injuries.

Apply negligence element-by-element to Homeowner's daughter's potential claim against Marcus.

For each element:
→ State the element
→ Apply the specific facts
→ Conclude: met / not met / disputed

[Write your analysis before reading Phase 3]

---

**Phase 3 — Model Answer**

**Model Rule — Negligence (MBE Majority):**
A defendant is liable for negligence if the plaintiff establishes four elements by a preponderance of the evidence:

1. **Duty:** The defendant owed a legal duty of care to the plaintiff. Licensed professionals are held to the standard of a reasonably prudent member of their profession. A duty may run to foreseeable plaintiffs, not just the contracting party (majority rule per *Palsgraf* zone-of-danger and Restatement §7).

2. **Breach:** The defendant's conduct fell below the applicable standard of care. Violation of a statute or code (negligence per se) may establish breach if the plaintiff is in the class the statute was designed to protect and the harm is the type the statute was designed to prevent.

3. **Causation:**
   - *Actual cause (but-for causation):* But for the defendant's conduct, the harm would not have occurred.
   - *Proximate cause (legal causation):* The harm was a foreseeable consequence of the breach; no superseding intervening cause broke the causal chain.

4. **Damages:** The plaintiff suffered legally cognizable harm (personal injury, property damage, economic loss in most jurisdictions).

---

**Rule Accuracy Feedback (common deficiencies):**

- **Element often missed:** The two sub-parts of causation (actual + proximate). Many learners state only "causation" without distinguishing but-for from foreseeability analysis — this costs points on MEE essays.
- **Element often misstated:** Duty — stating it as "defendant owed plaintiff a duty" without specifying the *standard* (reasonable person, professional standard, etc.). The standard of care is part of the duty analysis.
- **Jurisdiction note:** Negligence per se (using statutory violation to establish breach) is majority rule but not universal — some jurisdictions treat it as only evidence of negligence.

---

**Model Application:**

**Element 1 — Duty:**
Marcus, as a licensed electrician, is held to the standard of a reasonably prudent licensed electrician. The NEC sets the professional standard of care. The daughter was a resident of the home where Marcus worked — a foreseeable user of the electrical system. Duty extends to foreseeable plaintiffs in the zone of danger. → **Duty: Met**

**Element 2 — Breach:**
Marcus observed a code-violating outlet (non-GFCI near a water source) and took no corrective action. A reasonably prudent electrician with knowledge of a code violation that poses a specific electrocution risk would either correct it or at minimum warn the homeowner. Marcus did neither.

Negligence per se argument: The NEC provision requiring GFCI outlets near water is designed to protect against electrocution. Homeowner's daughter is in the class of persons the code was designed to protect, and electrocution is exactly the type of harm the code was designed to prevent. Under negligence per se, the NEC violation may conclusively establish breach. → **Breach: Met (negligence per se or under reasonable electrician standard)**

**Element 3 — Causation:**

*Actual cause:* But for Marcus's failure to correct or warn about the non-GFCI outlet, the daughter would not have been electrocuted when the outlet contacted water. The causal chain is direct. → **Actual cause: Met**

*Proximate cause:* Was the electrocution a foreseeable consequence of failing to replace a non-GFCI outlet near a sink? Yes — the entire purpose of GFCI requirements is to prevent exactly this outcome. The overflowing sink is not a superseding cause; it is a foreseeable household event that GFCI outlets are designed to handle. → **Proximate cause: Met**

**Element 4 — Damages:**
Permanent hand injuries are cognizable personal injury damages. → **Damages: Met**

**Conclusion:** All four elements of negligence are satisfied. Marcus is liable to Homeowner's daughter. The scope-of-contract limitation Marcus relied on is not a defense to tort liability — a contractor may owe tort duties independent of the contract scope.

---

**Application Feedback:**

- Did you analyze every element separately? → If you merged duty and breach or skipped actual/proximate causation sub-analysis, you are writing conclusory essays that will receive partial credit at best.
- Did you use specific facts? → "Marcus knew about the outlet" is better than "defendant failed to act." "GFCI code applies near water" is better than "there was a code violation."
- Did you address the contested element? → The contract scope limitation is the hidden dispute — a learner who doesn't address it has missed the key defense argument.

---

**Contrast Pair:**

**Negligence vs. Negligence Per Se** — How do they differ, and what fact would eliminate the *per se* argument?

[Write your distinction before reading the model]

**Model distinction:** Negligence requires the factfinder to evaluate whether conduct fell below the reasonable person standard — a flexible, context-dependent inquiry. Negligence per se substitutes a statutory violation for that inquiry: if the defendant violated a statute designed to prevent this type of harm to this class of plaintiff, breach is established as a matter of law.

**Fact that eliminates per se:** If the NEC provision had been adopted for fire-prevention purposes only, not electrocution prevention, then the daughter's electrocution injury would fall outside the protective purpose of the statute, and per se would not apply. Negligence (reasonable electrician standard) would still be available, but breach would be a jury question.

---

## Session Summary

| Item | Rule Recall | Application | Weakest Point |
|---|---|---|---|
| Negligence | [X/4 elements] | Element-level analysis reached? | Actual/proximate causation sub-split |

**Priority:**
- If recall < 70%: Re-study the rule before more drills — flashcard the element list
- If recall ≥ 70% but application weak: Practice timed element-by-element writing (3 min per element, no re-reading allowed)

---

## False-Positive Prevention

**❌ DON'T** present the fact pattern before the learner has stated the rule from memory. A learner who reads the facts first will reverse-engineer the elements they "need" — this is recognition, not recall.

**✅ DO** enforce Phase 1 completion before Phase 2 is revealed. Each phase must be committed in writing before advancing.

**❌ DON'T** use fact patterns where all elements are clearly satisfied. Application practice requires at least one genuinely contested element and one clearly unmet element — otherwise the task is classification, not analysis.

**✅ DO** design facts with a mix: one clearly satisfied element, one contested element, and one element that might not be met — to force element-level discrimination rather than global judgment.

**❌ DON'T** score rule accuracy only on whether the learner named the elements. Sub-elements matter (e.g., actual vs. proximate causation within causation). A rule statement that merges sub-elements teaches imprecise analysis.

**✅ DO** score element-by-element, counting sub-elements separately where they exist (e.g., breach = standard + conduct below standard; causation = actual + proximate).

**❌ DON'T** skip the application feedback step. Knowing the correct answer is not the same as knowing why your analysis was incomplete. Identifying the specific step that was conclusory or generalized is the actionable feedback.

**✅ DO** explicitly flag three failure modes in application feedback: (1) missing an element entirely, (2) applying facts at the wrong level of generality, (3) glossing over the contested element.

**❌ DON'T** omit contrast pairs for difficulty 2–3 items. Rules that are most often misapplied on the bar exam are confused with adjacent rules — knowing the rule in isolation is insufficient if a learner cannot distinguish it from its confusable sibling.

**✅ DO** include at least one contrast pair per session for any rule with a commonly confused neighboring doctrine. The contrast fact ("what one fact shifts the outcome") is the most efficient way to test genuine understanding.

## Quality Criteria

- [ ] Phase 1 (rule recall) is presented before Phase 2 (fact application) with an explicit pause instruction
- [ ] Fact pattern includes one clearly satisfied element, one contested element, and one element that requires argument
- [ ] Model rule statement is element-by-element with sub-elements where applicable
- [ ] Rule accuracy feedback calls out specific elements missed or misstated
- [ ] Model application is element-by-element (not global "plaintiff wins because...")
- [ ] Application feedback identifies the specific failure mode (missing element / generalization / glossing)
- [ ] Contrast pair is included for difficulty 2–3 with a "what fact would shift the outcome" question
- [ ] Session summary distinguishes recall accuracy from application quality

## Techniques Used

- **ST-01 (Clear Objective Statement):** Objective separates rule recall from rule application as two distinct measurable skills — enables targeted remediation when one is weak and the other is not
- **ST-02 (Structured Sequential Instructions):** Three-phase drill structure (recall → application → feedback) enforces correct learning sequence and prevents backward engineering
- **ED-02 (Progressive Exercise Generation):** Three difficulty levels (core doctrine → rule with exceptions → minority/majority split) escalate demand on rule precision
- **NE-04 (Contrast Pairs):** Confusable doctrine pairs force learners to articulate the distinguishing rule — the skill most needed when adjacent doctrines appear in the same fact pattern
- **QA-01 (Self-Verification):** Phase 3 model answer provides element-by-element comparison so learners can score their own rule accuracy and application quality with precision
