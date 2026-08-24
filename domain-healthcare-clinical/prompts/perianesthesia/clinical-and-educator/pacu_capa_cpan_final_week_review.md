---
title: PACU CAPA/CPAN Final Week Review
category: pacu/exam-prep
task_type: CREATE
audience: PACU RN in the final week before CAPA or CPAN exam
updated: "2026-05-15"
tags:
  - pacu
  - certification
  - capa
  - cpan
  - exam-prep
  - final-week
techniques:
  - ST-01
  - ST-02
  - RT-02
  - ED-02
difficulty: beginner
related_prompts:
  - prompts/pacu_capa_cpan_blueprint_aligned_study_plan.md
  - prompts/pacu_capa_cpan_weak_area_diagnostic.md
  - prompts/pacu_capa_cpan_test_strategy_coach.md
references:
  - ABPANC official exam policies (user verifies)
---

# PACU CAPA/CPAN Final Week Review

> Safety reminder: Final-week plan emphasizes consolidation and rest. Cramming is explicitly de-emphasized. For test-anxiety affecting daily function, consult a qualified provider; this prompt does not address that.

## Objective

Produce a **final-week review plan plus day-before / day-of routine** for the candidate. Output is explicitly anti-cramming: consolidation, light targeted review, full-length practice not repeated, rest emphasized, day-of mechanics finalized.

## Inputs

- **Exam date:** {{date}}
- **Test time + location:** {{from ABPANC scheduling}}
- **Final blueprint coverage status:** {{ranked weak areas after penultimate-week full practice test}}
- **Practice-test result and missed-item domain map:** {{from penultimate week}}
- **Sleep + life constraints in the final week:** {{e.g., working final 3 days, kids, etc.}}

## Audience / Scope

- **Primary:** Candidate.
- **Secondary:** Coaching educator.
- **Scope:** Final 7 days through exam day. Not multi-week (that's the study plan).

## Output requirements

```markdown
# Final Week Plan — {test date}

> Safety reminder: This week is consolidation, not cramming. Sleep matters more than additional items.

**Exam date:** {date}
**Test location + time:** {location/time, verified by candidate with ABPANC}

## Principle

The final week does not raise your score by adding new content. It raises your score by:
- Consolidating what you already know.
- Closing gaps on 1–2 high-yield weak areas.
- Practicing exam mechanics, not exam content.
- Sleeping.

## Day-by-day

### Day 7 (1 week out)

- Review the penultimate-week practice test results, missed-item domain map.
- Identify 1–2 highest-yield weak areas (high weight × low score).
- Plan 2 focused review sessions for those areas this week.
- Light review: 30 min on one weak area.
- Sleep on schedule.

### Day 6

- Focused review session #1 on weak area #1 (60–90 min).
- 20 practice items on that area.
- Light reading on weak area #2.
- Sleep on schedule.

### Day 5

- Focused review session #2 on weak area #2 (60–90 min).
- 20 practice items on that area.
- Re-read your own concept summaries from earlier weeks.
- Sleep on schedule.

### Day 4

- Light review only: skim concept summaries.
- Re-read `pacu_capa_cpan_test_strategy_coach.md` brief.
- 20–30 mixed-domain practice items at exam pace.
- No new content.
- Sleep on schedule.

### Day 3

- Logistics day: confirm test location, ID, parking, travel time, ABPANC requirements.
- 10–15 mixed items at exam pace.
- Read concept summaries one more time.
- Sleep on schedule.

### Day 2

- Light review only — 30 min skim.
- Do not take a full practice test.
- Pack what you need for test day per ABPANC policy.
- Sleep on schedule.

### Day 1 (day before exam)

- No new content.
- 30-min light walk-through of concept summaries, no items.
- Verify travel time to test center.
- Eat well, hydrate normally, sleep on schedule.

### Exam day

- Routine breakfast (whatever you normally eat — exam day is not the day to change food).
- Arrive 30 min early.
- Verify ID per ABPANC policy.
- Apply pacing rule from test strategy brief.
- Apply flag-and-return rule.
- Trust your preparation.

## Day-of mechanics checklist

- [ ] ID per ABPANC requirements.
- [ ] Travel time confirmed and padded.
- [ ] Restroom before exam start.
- [ ] Pacing rule mental anchor.
- [ ] Flag-and-return rule mental anchor.
- [ ] Permission to skip-and-flag if pace falls behind.

## What this final week is NOT

- Not the week to start a new topic.
- Not the week for a second full practice test.
- Not the week to add caffeine, supplements, or new sleep medications.
- Not the week to "make up for" earlier weeks.

## After the exam

Same day or next day:
- No score-anxiety review of items. The exam is done.
- If you remember an item you're unsure about, you cannot change it. Let it go.
- Plan something restorative for the evening.

If you fail and need to retest:
- Wait at least 1 week before reviewing the missed-item domain map.
- Re-run `pacu_capa_cpan_weak_area_diagnostic.md` with fresh practice-test data after some recovery time.
- Do not start a study plan in the first 48 hours after failing.

## Sources / reference

- ABPANC official policies — candidate verifies.
```

## Must / Must not

**Must:**
- De-emphasize cramming explicitly.
- Frame the week as consolidation + mechanics, not content addition.
- Cap weak-area focus at 1–2 areas, not all gaps.
- Surface sleep, rest, and routine.
- Include a "what to do after the exam" block (both pass and retest paths).
- Reference test-strategy brief for mechanics.

**Must not:**
- Recommend a second full-length practice test in the final week.
- Recommend new topic introduction.
- Recommend caffeine, supplements, sleep medications, or other physiological interventions.
- Project pass/fail.
- Fabricate ABPANC day-of policies.
- Use anxiety-treatment framing.
- Reference protected characteristics.

## Quality signals

- A candidate reading this on Day 7 has clear day-by-day actions.
- The plan does not pressure additional studying past Day 4.
- "What this final week is NOT" lands.
- After-exam block (including retest path) is humane and concrete.

## Verification

- [ ] Day-by-day plan covers Day 7 → Day 1 → Exam day.
- [ ] Weak-area focus capped at 1–2.
- [ ] No second full practice test.
- [ ] Sleep emphasized.
- [ ] Anti-cramming framing explicit.
- [ ] After-exam block present (pass + retest).
- [ ] Safety + FPP sections present.

## False-Positive Prevention

- **No fabricated ABPANC policies** (ID, location, dress code, breaks).
- **No fabricated sleep, caffeine, or supplement prescriptions.**
- **No fabricated "the night before, top performers do X" claims.**
- **No fabricated pass-rate predictions.**
- **No clinical mental-health framing.**
- **No protected-characteristic guidance.**
- **No license-pathway guidance.**
- **No facility-specific advice.**

## Worked Example

<details>
<summary>Example: 7-day plan, 2 weak areas identified from penultimate test (click to expand)</summary>

```markdown
## Day 7

- Review missed-item domain map from Day 8 practice test.
- Identify weak areas: Domain B (high weight, 58%), Domain D (medium weight, 60%).
- Plan focused sessions: Day 6 (Domain B), Day 5 (Domain D).
- 30 min light review on Domain B.

## Day 6

- 75-min focused session on Domain B + 20 practice items.
- 30 min reading on Domain D.

## Day 5

- 75-min focused session on Domain D + 20 practice items.
- Re-read concept summaries.

## Day 4

- Skim summaries (45 min).
- Re-read test strategy brief.
- 25 mixed items at exam pace.

## Day 3

- Logistics: confirm location, ID, travel.
- 10 mixed items, pace-only.
- Skim summaries.

## Day 2

- 30-min light skim.
- Pack per ABPANC requirements.

## Day 1

- No new content. Walk-through summaries 30 min.
- Verify travel time.

## Exam day

- Routine breakfast.
- 30 min early.
- Apply pacing + flag-and-return rules.

## After exam

- No item review same day.
- Plan something restorative for evening.
```

Notes: anti-cramming, no second full practice, sleep on schedule, after-exam humane.
</details>

## Self-check

- [ ] 7-day plan present.
- [ ] Anti-cramming framing.
- [ ] No second full practice.
- [ ] Sleep emphasized.
- [ ] After-exam block (pass + retest) present.
- [ ] FPP section passed.
