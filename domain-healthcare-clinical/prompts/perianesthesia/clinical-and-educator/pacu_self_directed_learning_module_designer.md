---
title: PACU Self-Directed Learning Module Designer
category: pacu/orientation-curriculum
task_type: CREATE
audience: PACU educator or preceptor designing an off-shift self-directed learning module for an orientee
updated: "2026-05-15"
tags:
  - pacu
  - orientation
  - self-directed
  - module
  - off-shift
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-01
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - prompts/pacu_orientee_weekly_learning_plan.md
  - prompts/pacu_topic_primer.md
  - prompts/pacu_complication_deep_dive.md
  - prompts/pacu_orientee_question_log_builder.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
---

# PACU Self-Directed Learning Module Designer

> Safety reminder: Self-directed module is a preparation tool; it does not replace bedside teaching, preceptor cueing, or facility protocol. Patient care decisions remain governed by facility orders and protocols.

## Objective

Design a **≤ 90-minute self-directed learning module** on one PACU topic, structured as **Read → Think → Self-check → Apply-next-shift**. The orientee completes the module off-shift and brings the apply-block to their next shift for preceptor reinforcement.

## Inputs

- **Topic:** {{e.g., post-spinal hypotension, residual neuromuscular blockade, emergence delirium, multimodal pain in first 30 min}}
- **Orientation week:** {{which week — drives depth}}
- **Orientee background:** {{new-grad | experienced | etc.}}
- **Source chapters available:** {{Drain's / Core Curriculum chapters relevant to the topic}}
- **Time budget:** {{default 60 min, up to 90 min}}
- **Apply-next-shift opportunity:** {{e.g., orientee has an ortho-spinal assignment next shift — module's apply-block should align}}

## Audience / Scope

- **Primary:** Orientee, completing off-shift.
- **Secondary:** Primary preceptor, who reviews the apply-block with the orientee on next shift.
- **Scope:** One topic per module. Multi-topic study planning: use `pacu_orientee_topic_self_study_planner.md`.

## Output requirements

```markdown
# Self-Directed Module — {Topic}

> Safety reminder: Module is for preparation. Bedside decisions follow facility protocol and preceptor cueing.

**Topic:** {topic}
**Time budget:** {≤ 90 min}
**For orientation week:** {n}
**Apply-next-shift:** {planned shift / case context}

## Why this topic now (≤ 4 sentences)

State the connection between the topic, the orientee's current curriculum week, and the upcoming shift's likely exposure. Make the relevance obvious.

## Block 1 — Read (≤ 30 min)

Two reading assignments with explicit focus questions:

**Assignment 1:** {chapter title}
- Pages or section: {if known; otherwise "the chapter on …"}
- Focus while reading: {2 questions the reader should hold in mind}

**Assignment 2:** {chapter title} (optional second source)
- Focus: …

## Block 2 — Think (≤ 15 min)

3–5 open-ended prompts that force synthesis, not recall. Examples:
- "In your own words, what is the mechanism behind {phenomenon}? Write 3 sentences, not more."
- "What's one thing about this topic you didn't know before today? What's one thing you thought you knew but now see differently?"
- "If a friend who is a med-surg RN asked you 'why does post-spinal hypotension persist past the 30-min point?' how would you answer? Write the answer, then critique it."

## Block 3 — Self-check (≤ 15 min)

5–7 application-level questions with answer keys at the bottom of the module. Examples:
- "A patient arrives from spinal anesthesia at 0830. BP is 108/68 (baseline 130/80). At 0855, BP is 92/58. Mentation unchanged. What is your next action? What role would you call, and why?"
- Avoid recall items ("Which drug class is …"); favor application ("Given the situation above, what is your reasoning?").

**Answers** (collapsed at the end): preceptor-style rationale, with at least one alternative answer flagged and reasoned through.

## Block 4 — Apply on next shift (≤ 30 min including discussion)

The orientee carries this block to the next shift.

**Bring to your preceptor:**
- Your one-sentence summary of the topic (from Block 2).
- Two questions you had after reading (from Block 1 focus questions).
- One self-check item you got "wrong" or "almost right" — the most useful one to discuss.

**Look for on shift:**
- Three observable bedside signs of the phenomenon (named generally; not specific thresholds).
- The point in workflow where the phenomenon would manifest.
- The escalation partner you'd contact by role.

**End-of-shift micro-debrief with preceptor:**
- Did you see it today? If yes — when, what did you do, what would you change next time?
- If no — when do you expect to see it? What case mix would expose you to it?

## Mastery check (orientee self-rate)

Rate yourself after the apply-block:
- [ ] I can explain this topic in 3 sentences to another RN.
- [ ] I can name the 3 most common early cues.
- [ ] I can name the escalation partner by role and the SBAR shape I'd use.
- [ ] I can name what could trick me into missing this (a "looks fine on surface" pattern).
- [ ] I can name a question I still have for my preceptor.

## Sources

- *Drain's* — {chapter title}
- *Core Curriculum* — {module title}
- (No additional unsourced citations.)

## Answer key for Block 3

(Place at the very end, collapsed under a heading or details block so it's not the next thing the orientee sees.)
```

## Must / Must not

**Must:**
- Keep total time budget ≤ 90 min.
- Structure as Read → Think → Self-check → Apply.
- Self-check items at **application** level, not recall.
- Apply-block ties to a specific upcoming shift opportunity.
- Mastery check is self-rated, not graded.
- Answer key at the end, not inline.

**Must not:**
- Include specific dose values, even in self-check items (use generic patient narratives without dose specifics; or use `{{per provider order}}`).
- Include facility-specific protocols or named drugs in mandated regimens.
- Inflate to a college lecture — 90 min is a hard cap.
- Generate fill-in-the-blank recall items.
- Replace bedside teaching ("after this module you can manage this independently").
- Project the orientee's emotional state.

## Quality signals

- An orientee with 60 spare minutes between shifts could complete the module and arrive next shift better prepared.
- A preceptor reviewing the apply-block in 5 min can pick up the orientee's reasoning state.
- Self-check items are answerable from the readings + thinking, not from memorization.
- The "what could trick me" question surfaces a real failure mode.

## Verification

- [ ] Total time ≤ 90 min, allocated across 4 blocks.
- [ ] Block 1 has explicit focus questions, not just "read this."
- [ ] Block 2 prompts force synthesis.
- [ ] Block 3 items are application level.
- [ ] Block 4 ties to a specific shift context.
- [ ] Mastery check is self-rated.
- [ ] Answer key separated from question stem.
- [ ] Safety + FPP sections present.

## False-Positive Prevention

- **No invented doses or thresholds** in self-check scenarios. Use qualitative phrasing.
- **No invented Drain's / Core Curriculum page numbers** — chapter title only.
- **No invented facility-specific protocols.**
- **No invented escalation phone numbers, pagers, or named staff.**
- **No fabricated mastery percentages** ("80% mastery means …").
- **No protected-characteristic references** in self-check patient scenarios. Use generic patients without demographics unless demographics are clinically relevant (e.g., pregnancy for OB-context modules, weight only via generic adult/peds framing).
- **No license-pathway expectations** ("if you're a BSN you should grasp this faster").

## Worked Example

<details>
<summary>Example: Topic = "Post-spinal hypotension," Week 3, new-grad, apply-on-ortho-spinal shift (click to expand)</summary>

```markdown
# Self-Directed Module — Post-Spinal Hypotension

**Topic:** Post-spinal hypotension.
**Time budget:** 75 min.
**For orientation week:** 3.
**Apply-next-shift:** Ortho-spinal day, expected TKA spinal recoveries.

## Why this topic now

Week 3 expands hemodynamic competency into PACU-specific contexts. Post-spinal hypotension is the most common hemodynamic event after ortho-spinal cases on this unit's Mon schedule, and the recognition pattern (trend before alarm) is the cueing-decay target for this week.

## Block 1 — Read (25 min)

**Assignment 1:** *Drain's*, Regional Anesthesia / Neuraxial Block Management chapter.
- Focus: How does the block level shape what you expect for BP and HR? When does resolution typically begin?

**Assignment 2:** *Core Curriculum*, hemodynamic management module.
- Focus: What's the cueing pattern across two consecutive cycles vs a single drop?

## Block 2 — Think (10 min)

- In your own words, why does the block cause hypotension? Three sentences, no more.
- What's one thing you thought you knew about post-spinal hypotension that you now see differently after reading?
- If a med-surg RN floated to PACU asked you why this patient's BP keeps drifting at 30 min when "the spinal was placed at 0700," how would you answer?

## Block 3 — Self-check (15 min)

1. A patient arrives from a TKA spinal at 0830. Baseline BP 138/82. At 0850, BP is 112/68. Mentation alert, no nausea, no complaint. What is your first action — and your reasoning? What role do you call, and when?
2. Same patient. At 0905, BP is 96/56, mentation slightly less alert, mild nausea. What action? What role, what SBAR shape?
3. (… 3 more application items)

## Block 4 — Apply on next shift (25 min including discussion)

**Bring to your preceptor:**
- Your one-sentence summary of post-spinal hypotension.
- Two questions you had after the readings.
- The self-check item you found hardest.

**Look for on shift:**
- BP drift across cycles (vs single drop).
- The 30–60 min "settling" window where the second drift can appear.
- The SBAR you'd build for the CRNA, by role.

**End-of-shift micro-debrief:**
- Did you see it? What was the first cue you used?

## Mastery check

(self-rate as listed above)

## Answer key

<details><summary>Click to reveal</summary>

Item 1: First action is to verify the trend by recheck (manual cycle if needed), reposition per facility order (e.g., legs up if not contraindicated), and prepare to escalate. SBAR-by-role: CRNA or anesthesiologist on call. Alternative answer flagged: some preceptors would not escalate after a single drop in an alert patient — that's a real practice variation, name it.

(remaining items …)

</details>
```

Notes: time budget honored, self-check application-level, apply-block ties to ortho-spinal shift, no invented doses, answer key separated.
</details>

## Self-check

- [ ] Time budget ≤ 90 min.
- [ ] 4 blocks present (Read / Think / Self-check / Apply).
- [ ] Self-check items application level.
- [ ] Apply-block tied to specific shift.
- [ ] Mastery check self-rated.
- [ ] Answer key separated.
- [ ] FPP section passed.
