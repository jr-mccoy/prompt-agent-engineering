---
title: PACU CAPA/CPAN Practice Question Generator
category: pacu/exam-prep
task_type: CREATE
audience: PACU RN preparing for CAPA or CPAN, generating practice questions for a specific sub-topic
updated: "2026-05-15"
tags:
  - pacu
  - certification
  - capa
  - cpan
  - exam-prep
  - mcq
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-01
  - ED-02
  - DS-06
difficulty: advanced
related_prompts:
  - prompts/pacu_capa_cpan_blueprint_aligned_study_plan.md
  - prompts/pacu_capa_cpan_weak_area_diagnostic.md
references:
  - ABPANC official exam blueprint (current edition — user pastes in domains)
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
---

# PACU CAPA/CPAN Practice Question Generator

> Safety reminder: Generated questions are practice items, not endorsed by ABPANC. Item style approximates exam style; actual exam content and difficulty may differ. Always defer to the current ABPANC blueprint and published policies.

## Objective

Generate **N application-level multiple-choice practice items** on a candidate-specified sub-topic, in CPAN/CAPA-style format: stem with patient scenario → 4 options → identified key with **rationale for the correct answer AND distractor reasoning for each incorrect option**. Avoids fabricated specific dose values by using qualitative phrasing or `{{per provider order}}` placeholders in any clinical decision item.

## Inputs

- **Exam target:** {{CAPA | CPAN}}
- **Sub-topic:** {{e.g., "Post-spinal hypotension recognition," "Reversal agent timing," "Aldrete borderline scoring"}}
- **Blueprint domain this sub-topic maps to (per candidate's pasted blueprint):** {{domain}}
- **Number of items:** {{default 5; up to 10}}
- **Difficulty:** {{recall / application / analysis — default application}}
- **Source chapters available:** {{Drain's / Core Curriculum chapters relevant to sub-topic}}

## Audience / Scope

- **Primary:** Candidate studying for CAPA or CPAN.
- **Secondary:** Educator vetting generated items.
- **Scope:** Practice items only. Not an exam, not endorsed by ABPANC.

## Output requirements

```markdown
# Practice Items — {Sub-topic}

> Safety reminder: Practice items; not endorsed by ABPANC. Item style approximation. Always defer to current ABPANC blueprint and published policies. Vet items with an educator before relying.

**Sub-topic:** {sub-topic}
**Blueprint domain:** {domain — from candidate's blueprint paste}
**Difficulty target:** {recall / application / analysis}

## Item structure (used for all items below)

Stem (clinical scenario, ≤ 5 sentences) → Question → A/B/C/D options → Identified key (correct answer) → Rationale for correct + distractor reasoning for each incorrect option.

---

## Item 1

**Stem:**
{Patient scenario, with vital signs given qualitatively or as `{{per provider order}}` placeholders for any decision-driving thresholds. Or, if a number is essential to the item, the stem provides that number directly so the item is self-contained. Never invent a number that the item would tie a "right answer" to in a way that would conflict with current ASPAN or facility practice.}

**Question:** {What is the candidate being asked to decide?}

**Options:**
A. {option}
B. {option — distractor}
C. {option — distractor}
D. {option — distractor}

**Key:** {A | B | C | D}

**Rationale for correct answer:** {2–3 sentences tying to ASPAN scope or Drain's chapter; explicit on the reasoning}

**Distractor reasoning:**
- A: {why this is wrong — be specific; "not the most appropriate first action because …"}
- B: {…}
- C: {…}
- D: {…}

---

## (Repeat for items 2 to N)

---

## Sub-topic mastery check

Suggested mastery target on this set: ≥ 4/5 correct (or ≥ 8/10 on a 10-item set), with rationale-level understanding of every distractor in incorrect answers. Mastery is application-level reasoning, not memorization of these specific items.

## Re-generate

Re-run this prompt for the same sub-topic to get new items. Do not memorize specific items — practice question pools are deep.

## Sources / reference

- Candidate-pasted ABPANC blueprint domain.
- ASPAN *Core Curriculum* — relevant sub-topic content.
- *Drain's* — relevant chapter.
```

## Must / Must not

**Must:**
- Generate application-level (or higher) items unless candidate explicitly requests recall.
- Provide rationale for the correct answer **and distractor reasoning for every incorrect option**.
- Use qualitative phrasing or `{{per provider order}}` for clinical decision items where a specific dose value would otherwise need to be invented.
- If a number is essential to the item, embed the number in the stem so the item is self-contained — do not depend on the candidate recalling a memorized threshold.
- Avoid items that would be answered differently depending on facility protocol — or flag explicitly that "per facility protocol" applies to this item.
- Map every item to the candidate-pasted blueprint domain.

**Must not:**
- Fabricate ABPANC item bank content or claim items match the exam.
- Invent specific dose values to make an item resolve to a single answer.
- Invent threshold values (e.g., specific SpO₂ cutoff) and treat them as universally correct.
- Generate items that conflict with current ASPAN scope.
- Use ambiguous distractors that could be defended as correct.
- Reference protected characteristics in stems.
- Embed facility-named protocols in stems.
- Generate items the candidate will see again on the real exam — no claim of overlap with ABPANC content.

## Quality signals

- Distractors are tempting (plausible) but defeatable on close reading.
- The candidate learns from distractor reasoning, not just the key.
- Items would not embarrass the candidate if shown to a senior PACU educator.
- Re-running on the same sub-topic produces different items, not minor rewordings.

## Verification

- [ ] All items at requested difficulty level.
- [ ] Every item has key + rationale + distractor reasoning for every wrong option.
- [ ] No fabricated dose values where they would drive the answer.
- [ ] Numbers (if used) are self-contained in the stem.
- [ ] Distractors are plausible, not absurd.
- [ ] No items conflicting with ASPAN scope.
- [ ] Each item maps to the candidate's blueprint domain.
- [ ] Safety + FPP sections present.

## False-Positive Prevention

- **No fabricated ABPANC item content.** Items are author-style; no claim of ABPANC origin or overlap.
- **No invented specific dose values** that resolve the answer. Use `{{per provider order}}` or self-contained stem-supplied numbers, never an invented "universally correct" dose.
- **No invented threshold values** (SpO₂, MAP, temperature, Aldrete score cutoffs) as universally correct. Use qualitative cues or stem-supplied values.
- **No invented ASPAN guidance** to support a key. Tie rationale to ASPAN scope and Drain's chapter title (not section number).
- **No invented facility protocols** in stems.
- **No items that depend on facility-specific equipment brands.**
- **No protected-characteristic content** in stems.
- **No items dependent on patient demographics** unless demographics are clinically relevant (e.g., pregnancy for an OB-context item).
- **No fabricated pharmacology claims** (drug interactions, time-to-effect, half-life) beyond what's in the source chapter cited.

## Worked Example

<details>
<summary>Example: 1 application-level item on "Post-spinal hypotension recognition" (click to expand)</summary>

```markdown
## Item 1

**Stem:** A patient is admitted to PACU after a spinal anesthetic for elective TKA. The initial PACU BP is 134/78 on arrival (similar to the patient's stated pre-op baseline). At 20 minutes post-arrival, BP is 116/72; at 30 minutes, BP is 100/64. The patient is alert, denies dizziness, and is comfortable. Heart rate is unchanged across the three readings.

**Question:** What is the most appropriate next action?

**Options:**
A. Document the trend and continue routine monitoring.
B. Recheck BP with manual cycle, evaluate position, and notify the anesthesia provider by role of the trend.
C. Administer a fluid bolus immediately without further reassessment.
D. Wait one additional cycle to confirm whether the trend continues before any action.

**Key:** B

**Rationale for correct answer:** Recognition of a downward BP trend across multiple cycles after spinal anesthesia is consistent with sympathetic-block-mediated hypotension. The appropriate next action is to verify the trend (manual recheck to confirm reading accuracy), evaluate contributing factors (position, volume status), and communicate the trend to the anesthesia provider — escalation by role is appropriate before symptomatic decline. ASPAN scope supports proactive escalation on trend.

**Distractor reasoning:**
- A: Documentation alone defers action that the trend warrants; passive monitoring on a multi-cycle drift is less appropriate than verification + escalation.
- C: Administering a fluid bolus without reassessment or order skips clinical verification and the order-driven nature of bolus administration; not within PACU RN scope absent provider order or facility protocol.
- D: Waiting another cycle without intervening verification or escalation delays response on a recognizable trend; second-drift recognition is the cueing-decay target.
```

Notes: numbers self-contained in stem, no invented universally-correct threshold, distractor reasoning is specific, ASPAN scope referenced (not section number), no facility protocol named.
</details>

## Self-check

- [ ] All items at requested difficulty.
- [ ] Key + rationale + distractor reasoning per item.
- [ ] No fabricated universal-threshold numbers.
- [ ] Items map to blueprint domain.
- [ ] No facility-named protocols or named drugs as "always correct."
- [ ] No claim of ABPANC content overlap.
- [ ] FPP section passed.
