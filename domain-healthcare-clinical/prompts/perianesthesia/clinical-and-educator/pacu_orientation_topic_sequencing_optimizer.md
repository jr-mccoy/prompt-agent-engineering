---
title: PACU Orientation Topic Sequencing Optimizer
category: pacu/orientation-curriculum
task_type: DECIDE
audience: PACU preceptor or educator mid-orientation, choosing the next 2–3 weeks of focus
updated: "2026-05-15"
tags:
  - pacu
  - orientation
  - sequencing
  - mid-orientation
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-02
  - ED-02
difficulty: intermediate
related_prompts:
  - prompts/pacu_orientation_curriculum_designer.md
  - prompts/pacu_orientation_skill_acquisition_timeline.md
  - prompts/pacu_preceptor_orientation_pacing_diagnostic.md
  - prompts/pacu_orientation_surgical_mix_mapper.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
---

# PACU Orientation Topic Sequencing Optimizer

> Safety reminder: Sequencing recommendation only — actual shift content remains governed by the facility orientation program and patient assignments. Verify before adopting.

## Objective

Given the orientee's **current cueing-decay state** and **remaining orientation weeks**, recommend the optimal sequence for the next 2–3 weeks of focus. Designed to be re-run mid-orientation whenever pacing diverges from the original pathway.

## Inputs

- **Current week / total weeks:** {{e.g., Week 5 of 10}}
- **Current cueing-decay state by competency:** {{paste from latest evaluation or pacing diagnostic}}
- **Remaining default theme sequence:** {{from curriculum designer pathway}}
- **Open commitments from debriefs:** {{from rolling debrief log}}
- **Known scheduling constraints next 2–3 weeks:** {{e.g., orientee on PTO Wk 7, surgical-mix shift Wk 6 has no ortho exposure available}}
- **Pacing-diagnostic result (if recent):** {{ahead / on / behind, and on which axes}}

## Audience / Scope

- **Primary:** Primary preceptor mid-orientation.
- **Secondary:** Educator reviewing pacing changes.
- **Scope:** Next 2–3 weeks only. For full-pathway redesign, regenerate via `pacu_orientation_curriculum_designer.md`.

## Output requirements

```markdown
# Sequencing Recommendation — Wk {n+1} to Wk {n+3}

> Safety reminder: Recommendation only. Patient assignments and facility orientation program govern actual shift content.

## Starting state

- Current week / total: {n} of {N}
- Where ahead: {axes at I that should be at C — and how far}
- Where on: {axes at expected level}
- Where behind: {axes one level below expected — and how far}
- Open commitments: {3–5 from debrief log}

## Recommended next-3-week sequence

For each of the next 2–3 weeks:

### Week {n+1}: {theme}

**Why this theme now:** {1–2 sentences tying to the gap analysis}
**Primary competency targets:** {2–3 from gap list}
**De-prioritized for this week:** {1–2 axes that can wait}
**Required surgical exposures:** {service types}
**Open commitment closed this week:** {which prior commitment is addressed}
**Risk of this sequencing choice:** {what could go wrong, plain language}

(Repeat for n+2, optionally n+3.)

## Sequencing rationale

3–5 sentences naming the principle behind the order:
- "Cueing-decay on axis X precedes work on axis Y because Y depends on X" — name the dependency.
- "Surgical-mix scheduling forces ortho coverage in Wk n+1 — sequencing follows."
- "Pacing-diagnostic showed lagging judgment-in-ambiguity — Wk n+2 prioritizes ambiguous cases."

## Alternative considered (and rejected)

One alternative sequence + one-line reason for rejection. Surfaces the tradeoff the preceptor is making.

## Re-run trigger

If any of these happen, re-run this prompt:
- Pacing-diagnostic flips category (on → behind, etc.).
- Surgical-mix changes outside declared expectations.
- Open commitment goes 2 weeks without progress.
- Major scheduling change (preceptor change, PTO, condensed timeline).

## Sources / reference

- ASPAN *Standards* — scope.
- *Drain's* — competency dependencies (e.g., regional block recovery depends on hemodynamic monitoring foundation).
```

## Must / Must not

**Must:**
- Tie each weekly theme to a **named gap** in the current cueing-decay state.
- Name the **dependency** when one competency must precede another.
- Surface the alternative considered + reason for rejection.
- Name a re-run trigger.
- Keep recommendations to next 2–3 weeks; do not redesign the whole pathway.

**Must not:**
- Recommend a sequence that violates the default cueing-decay order without naming the trade-off.
- Compress PACU-distinctive content (emergence, regional, family, judgment) without explicit justification.
- Adjust based on tenure-only or license-pathway.
- Invent surgical-mix availability beyond what the user declared.
- Fabricate competency dependencies (cite Drain's chapter or ASPAN scope; if unknown, leave dependency as a flagged assumption).

## Quality signals

- A preceptor reading the recommendation can apply it to next Monday's schedule.
- The rejected alternative is a real option, not a straw man.
- The sequencing rationale exposes a real trade-off rather than asserting "this is just better."
- The re-run trigger is concrete enough that a preceptor knows when to come back.

## Verification

- [ ] Next 2–3 weeks only — not full pathway.
- [ ] Each theme tied to a current gap.
- [ ] At least one dependency named.
- [ ] Alternative + rejection reason present.
- [ ] Re-run trigger present.
- [ ] Safety + FPP sections present.

## False-Positive Prevention

- **No invented surgical-mix availability** outside declared.
- **No invented orientee performance data** beyond what the user pasted.
- **No invented Drain's chapter numbers** for dependencies. Cite by chapter title or flag.
- **No invented facility orientation program compression rules.**
- **No invented competency cap thresholds** ("must hit C by Week 6 to advance").
- **No protected-characteristic or license-pathway sequencing.**
- **No tenure-only compression.**

## Worked Example

<details>
<summary>Example: Week 5 of 10, behind on judgment-in-ambiguity, ahead on documentation (click to expand)</summary>

```markdown
## Starting state

- Current week / total: 5 of 10
- Where ahead: Documentation accuracy at I (timeline expected D→C). Handoff inbound at C (expected D).
- Where on: Airway, hemodynamics, PONV, pain — all at C as expected.
- Where behind: Judgment in ambiguity at D (expected C). Regional block at D (expected C, one week behind).
- Open commitments: Independent PONV reassessment timing (carried 2 weeks); pre-arrival risk verbalization on high-PONV patients.

## Recommended next-3-week sequence

### Week 6: Ambiguity + regional block under cover

**Why now:** Judgment and regional are both lagging; regional cases offer ambiguity practice without raising acuity stakes too far.
**Primary targets:** Judgment in ambiguity (C), regional block (C).
**De-prioritized:** Documentation (already at I; no extra focus).
**Required exposures:** ortho-spinal mix, GYN regional cases.
**Open commitment closed:** PONV reassessment timing (push to Independent this week).
**Risk:** stacking two lagging axes on one week may overload — mitigate with explicit preceptor coverage on Day 1 of week.

### Week 7: Ambiguity at scale (second-bay awareness)

**Why now:** Judgment is now C on individual case; next layer is awareness across two patients.
**Primary targets:** Two-bay awareness (under judgment competency), continued regional reinforcement.
**De-prioritized:** PONV (closed).
**Required exposures:** mixed assignment with two-patient cap.

(Wk 8 optional — depends on Wk 6/7 pacing.)

## Sequencing rationale

Judgment-in-ambiguity has the longest cueing-decay curve and is currently behind; pushing it forward in Wk 6 protects time for it later. Regional block depends on hemodynamic foundations (already at C), so regional can advance now. Two-bay awareness builds on individual-case judgment, so it must follow Wk 6's individual-case work, not precede.

## Alternative considered

Reverse the order: Wk 6 family communication + handoff polishing; Wk 7 ambiguity. Rejected because ambiguity is the lagging axis and delaying it risks Wk 9 not being ready for sign-off; family communication is on curve and can wait.

## Re-run trigger

If end-of-Wk 6 debrief shows judgment still at D, re-run this prompt with new gap analysis.
```

Notes: gap-tied themes, dependency named (two-bay depends on individual judgment), alternative is real, re-run trigger concrete.
</details>

## Self-check

- [ ] Recommendation scoped to 2–3 weeks.
- [ ] Themes gap-tied.
- [ ] Dependency named.
- [ ] Alternative + rejection present.
- [ ] Re-run trigger present.
- [ ] FPP section passed.
