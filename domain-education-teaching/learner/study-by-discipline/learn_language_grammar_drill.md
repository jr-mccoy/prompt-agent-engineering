---
title: "Language Grammar Drill"
category: education-teaching/learner/study-by-discipline
description: "Pattern-based grammar internalization for language learners: generates transformation drills, error-identification sets, and production prompts for a target grammar rule. Focuses on the underlying pattern, not rote paradigm memorization."
techniques:
  - ST-01
  - ST-02
  - ED-02
  - ED-03
  - QA-12
difficulty: intermediate
tags:
  - language-learning
  - grammar
  - pattern-practice
  - error-identification
  - production-drills
  - transformation
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/learner/study-by-discipline/learn_language_vocab_acquisition.md
  - domain-education-teaching/learner/memory-and-recall/learn_retrieval_drill_designer.md
  - domain-education-teaching/learner/self-assessment/learn_error_correction_cycle.md
---

## Objective

Generate grammar internalization drills for a target rule in a second language: transformation drills (convert a sentence to use the target structure), error-identification sets (find the grammar mistake), and free production prompts (produce a sentence using the rule in a novel context). The goal is pattern internalization, not paradigm memorization — the learner should recognize and produce the pattern automatically, not by consulting a mental table.

## When to Use

- When a learner knows a grammar rule intellectually but does not use it correctly in spontaneous speech or writing
- When a grammar rule is tested on a language proficiency exam (DELF, JLPT, IELTS, DELE, HSK)
- When grammar errors in a specific area persist despite studying the rule
- When a learner is transitioning from controlled practice to free production

**Do not use** during first exposure to a grammar rule — this is a drilling tool for a rule the learner has already been taught. For vocabulary acquisition, use `learnstudy_language_vocab_acquisition.md`.

## Instructions

1. **Collect inputs.**
   - Ask: "Which grammar rule or structure do you want to drill?" (e.g., Spanish subjunctive in noun clauses, Japanese て-form, French imparfait vs. passé composé)
   - Ask: "What is your target language and your L1?"
   - Ask: "What is your current level? (A1–C2 or equivalent)"
   - Ask: "What type of errors are you making? (Using the wrong tense/form, omitting a particle, wrong word order, wrong agreement — or 'unknown')"

2. **Define the pattern, not the rule.**
   Before generating drills, state the rule as a **pattern** (not a paradigm table):
   - Pattern statement: "[Trigger condition] → [Structure to use] → [Example]"
   - Identify the three most common error triggers: the specific contexts where learners most often get this wrong
   - Identify any near-miss confusable rules: the grammar structure most often applied incorrectly in place of this one

3. **Generate three drill types.**

   **Drill Type 1 — Transformation drill (10 items):**
   Provide a sentence using a different structure; the learner transforms it to use the target grammar rule.
   - Items should escalate: early items are syntactically transparent; later items have additional clauses or vocabulary that could mask the transformation point
   - Include 2 "foil" items where NO transformation is needed — to test whether the learner applies the rule selectively, not mechanically

   **Drill Type 2 — Error identification (6 items):**
   Provide sentences, some correct and some with exactly one grammar error related to the target rule.
   - 4 sentences with errors, 2 correct — learner must identify which have errors and name/correct the error
   - Errors should represent the most common mistake types for this rule (as identified in Step 2)
   - Do not include errors unrelated to the target rule — this is not a general proofreading task

   **Drill Type 3 — Free production prompts (4 items):**
   Provide a situation or communicative goal; the learner must produce a sentence using the target structure without being told to.
   - The prompt should create a context where using the target structure is natural — not one where it is explicitly requested
   - Include one prompt where the target structure is optional but represents the more natural choice

4. **Provide all answers.**
   For Type 1: the transformed sentence + a note on what changed and why
   For Type 2: whether the sentence is correct or contains an error + the corrected version + the rule that was violated
   For Type 3: one model answer using the target structure + a note on why it's the most natural choice

5. **Include a pattern internalization test at the end.**
   Ask the learner to state the grammar pattern without looking at any notes:
   "In your own words — no looking — state the rule for when to use [grammar structure]. Then give one example you did not use during the drill."

## Output Format

```
# Grammar Drill: [Target Structure]
Language: [language] | L1: [learner's L1] | Level: [level]

---

## Pattern Statement
Pattern: [Trigger condition] → [Structure] → [Example in target language + translation]

Error triggers:
1. [Most common error context]
2. ...
3. ...

Confusable rule: [The rule most often applied incorrectly here]

---

## Drill Type 1 — Transformation (10 items)
*(Transform each sentence to use [target structure]. Items 3 and 7 may not need transformation — mark those "no change" if appropriate.)*

1. [Source sentence]
...

**Answers:**
1. [Transformed sentence] — [Why: brief explanation]
...

---

## Drill Type 2 — Error Identification (6 items)
*(Each sentence may or may not contain exactly one grammar error related to [target rule]. If there is an error, identify it and write the correction.)*

1. [Sentence]
...

**Answers:**
1. [Correct / Error: description] → [Corrected sentence]
...

---

## Drill Type 3 — Free Production (4 prompts)
*(Produce a sentence appropriate for this situation. Use the target structure if it fits naturally.)*

1. [Communicative situation]
...

**Model answers:**
1. [Target language sentence] → "[Translation]"
   [Why this structure is appropriate here]
...

---

## Pattern Internalization Test
Without looking at anything: state the rule for [target structure] in your own words.
Then write one example sentence you have not used in this drill.

[Model answer below — cover until done]
[Model rule statement]
```

## Example Output

---

**Input:** Target rule: French subjunctive in noun clauses after verbs of doubt, wish, and emotion | L1: English | Level: B2 | Error type: Uses indicative when subjunctive is required; unsure when to use which

---

# Grammar Drill: French Subjunctive in Noun Clauses
Language: French | L1: English | Level: B2

---

## Pattern Statement

**Pattern:** [Subject] + [Verb of doubt/wish/emotion/obligation] + *que* + [Subject 2] + [**Verb in subjunctive**]

- **Example:** "Je veux **que** tu **viennes**." → "I want you to come." (venir → viennes, subjunctive)
- **Contrast:** "Je sais **que** tu **viens**." → "I know you are coming." (venir → viens, indicative) — knowledge/certainty = indicative

**Pattern trigger:** The key question is: does the main clause express **certainty/knowledge** (→ indicative) or **desire/doubt/emotion/obligation** (→ subjunctive)?

**Error triggers:**
1. "Espérer" (to hope) → triggers subjunctive, but sounds like a knowledge verb → learners often use indicative
2. "Il est vrai que" (it is true that) → triggers indicative, but learners use subjunctive by rule over-generalization
3. Subordinate clause with a different subject → required for subjunctive; if subjects are the same, use infinitive, not *que* clause

**Confusable rule:** The conditional (*conditionnel*) — learners sometimes use conditional instead of subjunctive for hypothesis/desire contexts. These are different moods with different triggers.

---

## Drill Type 1 — Transformation (10 items)

*Transform each sentence: change the verb in the subordinate clause from indicative to subjunctive, if required. Some items may NOT require transformation — mark those "no change."*

1. Je sais que tu parles français.
2. Il faut que tu (finir) tes devoirs.
3. Elle est contente que nous (venir) à la fête.
4. Je pense que tu as raison.
5. Nous doutons que Pierre (pouvoir) terminer à temps.
6. Il est évident que le problème (être) grave.
7. Je veux que vous (partir) maintenant.
8. Ils croient qu'il (venir) demain.
9. Elle regrette que son frère ne (savoir) pas nager.
10. Il est possible que nous (avoir) tort.

---

**Answers:**

1. **No change** — "Je sais que" (I know that) expresses certainty → indicative is correct: *parles*

2. **Il faut que tu **finisses** tes devoirs.** — Obligation (*il faut que*) → subjunctive. *Finir* → *finisses* (irregular subjunctive stem)

3. **Elle est contente que nous **venions** à la fête.** — Emotion (*être content que*) → subjunctive. *Venir* → *venions*

4. **No change** — "Je pense que" in an affirmative statement → indicative: *as raison*. Note: "Je ne pense pas que" (negative) → subjunctive — the negation changes the trigger.

5. **Nous doutons que Pierre **puisse** terminer à temps.** — Doubt (*douter que*) → subjunctive. *Pouvoir* → *puisse* (irregular)

6. **No change** — "Il est évident que" expresses certainty → indicative: *est*. (Compare: "Il est possible que" → subjunctive)

7. **Je veux que vous **partiez** maintenant.** — Desire (*vouloir que*) → subjunctive. *Partir* → *partiez*

8. **No change** — "Croire que" in affirmative → indicative: *vient*. Note: "Je ne crois pas que" → subjunctive

9. **Elle regrette que son frère ne **sache** pas nager.** — Emotion (*regretter que*) → subjunctive. *Savoir* → *sache* (irregular)

10. **Il est possible que nous **ayons** tort.** — Possibility (*il est possible que*) → subjunctive. *Avoir* → *ayons*

---

## Drill Type 2 — Error Identification (6 items)

*Each sentence may contain exactly one grammar error related to the subjunctive. Write: Correct / Error, and if Error, write the correction.*

1. Je doute que tu peux venir.
2. Il est certain qu'elle vienne à temps.
3. Nous souhaitons qu'il fasse beau demain.
4. Elle pense que vous ayez raison.
5. Il est nécessaire que vous partiez maintenant.
6. Je suis surpris qu'il ne soit pas là.

---

**Answers:**

1. **Error:** "Douter que" → subjunctive required. *peux* → **puisses**
   Correct: "Je doute que tu **puisses** venir."

2. **Error:** "Il est certain que" expresses certainty → indicative required. *vienne* → **vient**
   Correct: "Il est certain qu'elle **vient** à temps."

3. **Correct** — "Souhaiter que" → subjunctive. *fasse* is the correct subjunctive of *faire*. ✓

4. **Error:** "Penser que" in affirmative → indicative required. *ayez* → **avez**
   Correct: "Elle pense que vous **avez** raison."

5. **Correct** — "Il est nécessaire que" → subjunctive. *partiez* is correct. ✓

6. **Correct** — "Être surpris que" (emotion) → subjunctive. *soit* is correct. ✓

---

## Drill Type 3 — Free Production (4 prompts)

*Create a natural French sentence appropriate to each situation. Use the subjunctive if it fits naturally — but don't force it.*

1. You want to express to a friend that you hope they can attend your birthday dinner.
2. You are a teacher telling a student that it's essential they submit the paper before Friday.
3. You want to tell someone you are certain that the meeting is on Tuesday.
4. You are expressing that you're happy your sister got the job she wanted.

---

**Model answers:**

1. "J'espère que tu **puisses** venir à mon dîner d'anniversaire." → "I hope you can come to my birthday dinner."
   *Espérer que* → subjunctive (hope = not certain). Many learners mistakenly use indicative here.

2. "Il est essentiel que tu **rendes** le devoir avant vendredi." → "It's essential that you submit the paper before Friday."
   *Il est essentiel que* → obligation → subjunctive. *Rendre* → *rendes*

3. "Je suis certain que la réunion **est** mardi." → "I'm certain the meeting is on Tuesday."
   Certainty (*être certain que*) → indicative. This is a foil — do not use subjunctive here.

4. "Je suis content(e) que ma sœur **ait** obtenu le poste." → "I'm happy my sister got the job."
   Emotion (*être content que*) → subjunctive. Past subjunctive (*ait obtenu*) because the action (getting the job) is completed.

---

## Pattern Internalization Test

*(Cover everything above. Answer from memory.)*

**Q1:** In your own words: when do you use the subjunctive in a French noun clause after *que*?

**Q2:** Write one sentence using the subjunctive that you have NOT used in this drill.

---

**Model rule statement:**
Use the subjunctive after *que* when the main clause verb expresses doubt, desire, emotion, or obligation — anything that is not a statement of fact or certainty. Use the indicative when the main clause asserts something is known or certain to be true. In negative or interrogative forms, verbs like *croire* and *penser* also trigger the subjunctive.

---

## False-Positive Prevention

**❌ DON'T** test only transformation drills — these can be completed mechanically without internalizing the trigger condition.

**✅ DO** include error-identification and free production tasks, which require the learner to apply the rule independently without a transformational cue.

**❌ DON'T** make all error-identification items wrong — including correct sentences ensures the learner must actually evaluate each sentence rather than defaulting to "error" on everything.

**✅ DO** include at least 2 correct sentences in the error-identification set, with the learner required to explicitly mark them "Correct."

**❌ DON'T** skip the pattern statement and confusable rule. A learner who knows the rule in isolation but can't distinguish it from the confusable rule will fail in production.

**✅ DO** name the confusable rule explicitly and include at least one transformation foil that tests whether the learner applies the target rule selectively.

**❌ DON'T** make free production prompts that explicitly name the target structure ("Use the subjunctive to say...") — this removes the pattern recognition challenge.

**✅ DO** write prompts as communicative situations without grammatical instructions — the learner must recognize that the situation calls for the target structure.

## Quality Criteria

- [ ] Pattern is stated as a trigger condition → structure → example (not as a paradigm table)
- [ ] Three error triggers are named
- [ ] Confusable rule is identified
- [ ] Transformation drill includes at least 2 "no change" foils
- [ ] Error identification includes at least 2 correct sentences
- [ ] Free production prompts are communicative situations (not grammar instruction disguised as prompts)
- [ ] All answers include a brief explanation of why, not just the correct form

## Techniques Used

- **ST-01 (Clear Objective Statement):** Objective specifies pattern internalization vs. paradigm memorization as the target — the distinction drives the drill design
- **ST-02 (Structured Sequential Instructions):** Five-step process ensures pattern is defined before drills are generated
- **ED-02 (Progressive Exercise Generation):** Three drill types escalate from controlled transformation to error detection to free production
- **ED-03 (Guided Discovery):** Free production prompts require the learner to derive when to apply the rule — not prompted by the drill itself
- **QA-12 (False Positives Identification):** "No change" foils in transformation drills and correct sentences in error identification prevent mechanical application that mimics but doesn't demonstrate understanding
