---
title: PACU Preceptor Curriculum Handoff Brief
category: pacu/orientation-curriculum
task_type: COMMUNICATE
audience: Outgoing PACU primary preceptor briefing an incoming preceptor on an orientee mid-orientation
updated: "2026-05-15"
tags:
  - pacu
  - orientation
  - preceptor-handoff
  - continuity
techniques:
  - ST-01
  - ST-02
  - RT-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - prompts/pacu_orientation_curriculum_designer.md
  - prompts/pacu_orientation_skill_acquisition_timeline.md
  - prompts/pacu_preceptor_orientation_pacing_diagnostic.md
  - prompts/pacu_preceptor_debrief.md
  - prompts/pacu_orientee_evaluation_meta_prompt.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
---

# PACU Preceptor Curriculum Handoff Brief

> Safety reminder: Continuity tool. Does not transfer sign-off authority by itself; facility orientation program governs primary-preceptor assignment changes.

## Objective

Produce a **briefing document** the outgoing primary preceptor hands to the incoming primary preceptor when the orientee is mid-orientation: state-of-play, what's mastered, what's open, watch-fors, prior debrief commitments still open, and biases the incoming preceptor should know to check.

## Inputs

- **Orientation status:** {{e.g., Week 5 of 10, transitioning preceptor at Week 6}}
- **Reason for transition:** {{scheduled rotation / outgoing PTO / outgoing leave / unit-level reshuffle}}
- **Latest pacing diagnostic:** {{paste from `pacu_preceptor_orientation_pacing_diagnostic.md`}}
- **Latest evaluation (if any):** {{paste from evaluation suite if mid-orientation evaluation was run}}
- **Rolling debrief log:** {{from `pacu_preceptor_debrief.md`}}
- **Open commitments:** {{list}}
- **Background adapter notes:** {{paste from `pacu_background_specific_pathway_adapter.md`}}

## Audience / Scope

- **Primary:** Incoming primary preceptor.
- **Secondary:** Educator (CCs the brief).
- **Scope:** Mid-orientation handoff between primary preceptors. Not a sign-off transfer; sign-off authority follows facility orientation program rules.

## Output requirements

```markdown
# Preceptor Handoff — Orientee at Wk {n} of {N}

> Safety reminder: Continuity brief. Does not transfer sign-off authority.

**Outgoing preceptor:** {role/initials placeholder — no full names}
**Incoming preceptor:** {role/initials placeholder}
**Transition effective:** {date placeholder}
**Reason:** {transition reason}

## TL;DR (≤ 4 sentences)

Where this orientee is, where they're heading, and the single most important thing the incoming preceptor needs to know on Day 1 of takeover.

## Background and pathway adaptation

- Background: {declared}
- Pathway adapter applied: {3–5 sentences from adapter notes — what was compressed, what was preserved}
- Biases to watch: {2–3 from adapter}

## State of play by competency

| Competency | Current level | Pace vs expected | Notes |
|---|---|---|---|
| Airway | I | on | … |
| (etc.) | … | … | … |

(Use **I / C / D / N** scale; pace from latest pacing diagnostic.)

## Open commitments from rolling debrief log

| Commitment | First raised in week | Status |
|---|---|---|
| {commitment 1} | Wk 3 | progressing |
| {commitment 2} | Wk 4 | not yet addressed |

## Recent themes (last 2 weeks)

3–5 bullet themes from recent debriefs — not generic ("good communication") but specific behavioral observations.

## Watch-fors

- Specific patterns the incoming preceptor should look for on Day 1.
- Cueing-decay axes where Confidence-as-Competence is currently outpacing actual cueing behavior.
- Surgical exposures still gap-filling (link to surgical mix mapper output).

## What I would do next 2 weeks if I were staying

3–5 sentences. Not directive — guidance.

## Evaluation events coming up

Named, with downstream prompt references.

## What this brief is not

- Not a sign-off transfer.
- Not an HR record.
- Not a substitute for direct conversation between outgoing and incoming preceptor.

## Direct conversation prompt (15 min, before takeover)

The outgoing preceptor and incoming preceptor have a 15-min direct conversation covering:
1. The TL;DR.
2. Any biases the outgoing preceptor recognizes in themselves about this orientee.
3. Anything the incoming preceptor wants to see in their first shift.

## Sources / reference

- ASPAN *Standards* — competency framework.
- Facility orientation program — for any primary-preceptor change documentation requirement.
```

## Must / Must not

**Must:**
- Stay specific — concrete behavioral observations, not generic praise/concern.
- Distinguish current level from pace vs expected (two different signals).
- Include a "biases I recognize in myself" prompt in the direct conversation.
- Use role/initials placeholders, not full names.
- Reference facility orientation program for any change documentation requirements.

**Must not:**
- Transfer sign-off authority through this brief.
- Use generic personality language ("she's a great learner").
- Reference protected characteristics.
- Reference license pathway.
- Project the orientee's emotional state.
- Invent commitments not in the debrief log.
- Invent pacing data not in the diagnostic.

## Quality signals

- The incoming preceptor reads the TL;DR and could run Day 1 of takeover from it.
- Concrete watch-fors land in the first shift, not as "they'll get there."
- The "biases I recognize" prompt produces at least one named bias.

## Verification

- [ ] TL;DR ≤ 4 sentences.
- [ ] State-of-play table uses I/C/D/N tokens.
- [ ] Open commitments include first-raised week.
- [ ] Watch-fors are behavior-specific.
- [ ] Direct-conversation prompt included.
- [ ] No full names; roles/initials only.
- [ ] Safety + FPP sections present.

## False-Positive Prevention

- **No invented commitments** beyond what's in the debrief log.
- **No invented pacing data** beyond what's in the diagnostic.
- **No invented evaluation results.**
- **No invented facility primary-preceptor-change paperwork.**
- **No personality assessments** ("she's a perfectionist," "he's anxious"). Behavioral only.
- **No protected-characteristic, license-pathway, or tenure-based content.**
- **No invented orientee emotional state.**
- **No full names of orientee, preceptor, or other staff** anywhere.

## Worked Example

<details>
<summary>Example: Wk 5 transition, experienced ICU RN, pacing on (click to expand)</summary>

```markdown
# Preceptor Handoff — Orientee at Wk 5 of 10

> Continuity brief. Does not transfer sign-off authority.

**Outgoing preceptor:** RN A
**Incoming preceptor:** RN B
**Transition effective:** {date}
**Reason:** scheduled rotation.

## TL;DR

Orientee is on pace overall (ICU-transfer profile). Foundations Independent; regional block one position behind, exposure-driven. Wk 6 should prioritize ortho-spinal exposure and emergence-content reinforcement. One open commitment from Wk 3 on PONV reassessment timing — almost closed.

## Background and pathway adaptation

Background: 4 yrs medical ICU. Adapter compressed airway/hemo/SBAR/documentation by ~7 shifts; preserved emergence/regional/family/judgment full coverage. Biases to watch: ICU-halo at Wk 6 still relevant; confidence-as-competence on regional block — orientee speaks fluently but cueing-decay still at D.

## State of play

| Competency | Level | Pace | Notes |
|---|---|---|---|
| Airway | I | on | quiet, consistent |
| Hemo | I | on | post-spinal cueing strong |
| PONV | I | on | pre-arrival risk verbalization improving |
| Emergence | C | on | needs more exposure |
| Regional | D | -1 | exposure-driven |
| Judgment | D | on | long-tail competency |
| Handoffs | I | on | … |
| Documentation | I | on | … |

## Open commitments

| Commitment | First raised | Status |
|---|---|---|
| Independent PONV reassessment timing | Wk 3 | nearly closed |
| Pre-arrival risk verbalization | Wk 4 | progressing |

## Recent themes

- Sets up admission without checklist drift.
- Hesitates briefly before escalating on second drift — pattern: catches on alarm, not trend. Improving.
- Speaks fluently on regional pathophys; cueing-decay says still D — confidence > competence here.

## Watch-fors

- Wk 6 ortho-spinal days: watch whether orientee cues themselves on trend or waits for alarm. Without a cue, regional cueing-decay won't shift.
- Emergence delirium scenario landing Wk 6 sim — preview the day before.

## What I'd do next 2 weeks

Re-sequence regional advancement to Wk 6. Run Wk 6 mid-orientation pacing diagnostic. If regional doesn't move by Wk 7, consider mid-orientation evaluation.

## Evaluation events

End-of-phase sign-off at Wk 6 → use `pacu_orientee_evaluation_meta_prompt.md`.

## Direct conversation prompt

15-min conversation: TL;DR, biases I recognize in myself (I underweighted regional gap for 2 weeks), what RN B wants to see Day 1.
```

Notes: role/initials only, concrete watch-fors, biases named, no personality assessments.
</details>

## Self-check

- [ ] TL;DR ≤ 4 sentences.
- [ ] State-of-play uses I/C/D/N.
- [ ] Commitments include first-raised week.
- [ ] Watch-fors behavior-specific.
- [ ] Direct-conversation prompt included.
- [ ] No full names.
- [ ] FPP section passed.
