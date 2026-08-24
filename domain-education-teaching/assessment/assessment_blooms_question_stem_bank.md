---
title: "Bloom's Question Stem Bank by Subject"
category: education-teaching/assessment
description: "Build a leveled bank of question stems across all six Bloom's revised levels, customized to a specific subject and grade — so teachers can move a class up the cognitive ladder during discussion, exit tickets, or cold-call cycles."
techniques:
  - CM-01  # Context Framing
  - ST-02  # Sequential Steps
  - DS-01  # Framework Application (Bloom's revised taxonomy)
  - OC-01  # Output Templates
  - QA-02  # Adversarial Verification
difficulty: intermediate
tags:
  - assessment
  - blooms-taxonomy
  - questioning
  - discussion
  - exit-tickets
  - cold-call
  - middle-school
  - high-school
updated: "2026-05-10"
related_prompts:
  - domain-education-teaching/assessment/assessment_dok_item_generator.md
  - domain-education-teaching/teaching_socratic_discussion_facilitator.md
  - domain-education-teaching/teaching_exit_ticket_generator.md
---

# Bloom's Question Stem Bank by Subject

## Objective

Produce a leveled question-stem bank across all six revised Bloom's levels (Remember, Understand, Apply, Analyze, Evaluate, Create), customized to a specific subject, grade, and topic. Output gives teachers ready-to-use stems for in-class questioning, exit tickets, cold-call cycles, and discussion — calibrated to escalate cognitive demand within a single lesson.

## When to Use

- Building a stem bank teachers reference during class to push thinking
- Pre-planning a discussion where the teacher can move up the ladder as students engage
- Differentiating questioning during cold-calls
- Generating exit-ticket items at varied levels

## When NOT to Use

- Generating items at all 4 DOK levels for an assessment — use `assessment_dok_item_generator.md`
- Designing a Socratic discussion arc — use `teaching_socratic_discussion_facilitator.md`
- Generating a single exit ticket for one lesson — use `teaching_exit_ticket_generator.md`

> **Bloom's vs. DOK note:** Bloom's classifies cognitive *kinds* (remembering, evaluating, etc.); DOK classifies cognitive *depth* (recall, strategic, extended). Both are useful and don't perfectly map. This prompt uses Bloom's; for DOK, use the related prompt above.

---

## Inputs Needed

- **Subject and grade:** [...]
- **Specific topic / unit:** [The content the stems will pull from]
- **Use case:** [Discussion / exit tickets / cold-call deck / writing prompts]
- **Stems per level:** [4–8 typical]
- **Teacher tone / register:** [Formal / classroom-conversational]
- **Format constraint:** [Stems must be open / can include yes-no / must end in question mark / etc.]

---

## Instructions

### Step 1: Confirm the Six Levels

Use the revised Bloom's taxonomy:

| Level | What it asks the student to do |
|-------|--------------------------------|
| **Remember** | Recall, recognize, identify |
| **Understand** | Explain, summarize, interpret, classify |
| **Apply** | Use a procedure or concept in a new situation |
| **Analyze** | Differentiate, organize, attribute |
| **Evaluate** | Check, critique, judge with criteria |
| **Create** | Generate, plan, produce |

### Step 2: Topic Anchoring

For the specified topic, list 4–6 specific concepts, processes, texts, or phenomena the stems will operate on. Generic stems don't help teachers — topic-anchored stems do.

Example for "ecosystems and energy flow (grade 7 science)":
- Trophic levels
- Food webs
- 10% rule of energy transfer
- Decomposers and the carbon cycle
- Ecosystem disruption (introduced species, climate)

### Step 3: Generate Topic-Anchored Stems by Level

For each level, generate stems that reference the specific concepts (Step 2), not generic placeholders. Output as a per-level table:

```
LEVEL: REMEMBER
1. What is a trophic level?
2. Identify the producers in this food web diagram.
3. What does "decomposer" mean?
4. Name three primary consumers in our local ecosystem.

LEVEL: UNDERSTAND
1. Explain why energy decreases at each trophic level.
2. Summarize the role of decomposers in the carbon cycle.
3. Classify these organisms by trophic level: [list].
4. In your own words, what does the 10% rule mean?

LEVEL: APPLY
1. Use the 10% rule to predict how many primary producers are needed to support one tertiary consumer.
2. Given this disrupted food web, explain what would likely happen to the population of [organism].
3. Apply the concept of trophic level to explain why apex predators are often rare.

LEVEL: ANALYZE
1. Differentiate between energy flow and matter cycling in this ecosystem.
2. What's the underlying reason that ecosystems can't have unlimited trophic levels?
3. How does the introduction of [invasive species] change the relationships in this food web?

LEVEL: EVALUATE
1. Is the 10% rule a precise law or a useful approximation? Defend your answer.
2. Evaluate this proposed solution for restoring a damaged ecosystem. What would work, what wouldn't, and why?
3. Which is more important to ecosystem stability: producer biomass or biodiversity? Justify with evidence.

LEVEL: CREATE
1. Design a closed, sustainable mini-ecosystem (specify components and roles).
2. Propose a research plan to investigate the decline of [species] in [region].
3. Construct a model that shows how energy and matter move differently through an ecosystem.
```

### Step 4: Stem-Quality Audit

Audit each stem:

- [ ] Does the stem actually demand the cognitive level claimed?
- [ ] Is the stem topic-anchored, not generic?
- [ ] Is the stem open enough to elicit thinking, not yes/no (unless format specified)?
- [ ] Is the stem free of cueing or giving away the answer?
- [ ] Is the language age-appropriate?

Common drift:
- "Explain" is often Understand, not Analyze, even though it sounds higher
- "List the steps" is Remember if memorized, Apply if used in new situation
- "What do you think about X?" is often Evaluate-shaped but may collapse to Understand without criteria

### Step 5: Stem Combinations and Escalation

Build a sample escalation sequence the teacher can use within a single discussion. Move from lower to higher Bloom's:

```
TEACHER MOVE 1 (Remember): "Who can name the producers in this food web?"
TEACHER MOVE 2 (Understand): "Why do we call them producers?"
TEACHER MOVE 3 (Apply): "If we removed all the producers, what happens?"
TEACHER MOVE 4 (Analyze): "What's the underlying reason ecosystems collapse without producers?"
TEACHER MOVE 5 (Evaluate): "Is producer-loss the most dangerous disruption — or is something else worse?"
TEACHER MOVE 6 (Create): "Design a recovery plan for an ecosystem missing its producers."
```

This sequence is the teaching tool — the stem bank is the raw material.

### Step 6: Differentiation Notes

Provide stems written at adjusted complexity for:

- **Lower-readability versions** for ELL or developing readers (same cognitive level, simpler language)
- **Sentence frames** for response: "I think ___ because ___."
- **Stretch versions** for advanced students (additional constraint or evidence requirement)

### Step 7: Format Variants

If the use case is exit ticket vs. discussion vs. cold-call, the same stem may need formatting:

| Use case | Format adjustment |
|----------|-------------------|
| Discussion | Open, oral; can have implicit "support your answer" |
| Exit ticket | Written; usually time-bounded (60–90 sec); often combine 1 lower-level + 1 higher-level |
| Cold-call | Brief; teacher can scaffold in real time |
| Writing prompt | Includes evidence requirement; longer response expected |

### Step 8: Self-Check

- [ ] Are all six Bloom's levels represented?
- [ ] Are stems anchored in the actual topic?
- [ ] Did I check for level-drift on Analyze and Evaluate especially?
- [ ] Do I have a sample escalation sequence?
- [ ] Are differentiation versions included?

---

## Output Format

1. Topic anchors (Step 2)
2. Stem bank by level (4–8 stems each)
3. Stem-quality audit notes
4. Sample escalation sequence
5. Differentiation versions
6. Format variants for use cases
7. Self-check confirmation

---

## False-Positive Prevention

❌ **DON'T:**
- Build generic stems with [topic] placeholders — those don't help teachers
- Confuse "sounds higher" with "is higher" (Analyze vs. Understand drift)
- Ignore yes/no traps that collapse stem level to Remember
- Skip differentiation — same cognitive level, different language access matters
- Treat Create as "do a project" — it's about generating new arrangements, not crafts

✅ **DO:**
- Anchor every stem in the specific topic
- Audit for level drift on Analyze, Evaluate especially
- Provide an escalation sequence the teacher can deploy
- Adjust language for differentiation while preserving cognitive level
- Format-tune stems for the actual use case

---

## Quality Indicators

- [ ] All six Bloom's levels represented
- [ ] Stems are topic-anchored, not generic
- [ ] No level drift on higher-order stems
- [ ] Escalation sequence is provided
- [ ] Differentiation preserves cognitive level
- [ ] Format variants match use case

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **CM-01** | Subject, grade, topic, and use-case anchor stem generation. |
| **ST-02** | Eight-step build moves from levels → topic → stems → audit → escalation. |
| **DS-01** | Revised Bloom's taxonomy structures the bank and stem-level analysis. |
| **OC-01** | Per-level stem table and escalation sequence enforce reusable structure. |
| **QA-02** | Stem-quality audit and self-check stress-test for level-drift and genericness. |
