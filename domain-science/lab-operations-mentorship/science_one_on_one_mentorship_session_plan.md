---
title: "One-on-One Mentorship Session Plan"
category: science/lab-operations-mentorship
description: "Structure a recurring mentor–trainee 1:1 that balances research progress, career development, and well-being checkpoints, with trainee-set agenda items, action capture, and a route-to-professional-support note."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
difficulty: advanced
tags:
  - one-on-one
  - mentorship
  - career-development
  - well-being
  - action-items
  - trainee-agenda
  - cimer
  - check-in
updated: "2026-06-26"
related_prompts:
  - domain-science/lab-operations-mentorship/science_individual_development_plan_drafter.md
  - domain-science/lab-operations-mentorship/science_lab_meeting_agenda_designer.md
  - domain-science/lab-operations-mentorship/science_lab_onboarding_packet_designer.md
---

# One-on-One Mentorship Session Plan

**Objective:** Produce a structured, repeatable plan for a recurring mentor–trainee one-on-one that covers three tracks — research progress, career development, and well-being — without letting the research track crowd out the other two. The trainee sets part of the agenda. The output is a session template plus a question bank, action capture, and a clear note on routing well-being concerns to professional support.

**When to use:** When establishing regular 1:1s with a trainee, when existing meetings have collapsed into project-status-only check-ins, or when a mentor wants a humane structure that keeps career and well-being on the table.

**Required inputs:**
- **Discipline.** The trainee's field, so research-progress prompts fit the work.
- **Career stage.** The trainee's stage, since the balance of research vs. career vs. well-being and the relevant questions shift across stages.
- **Meeting cadence.** How often the 1:1 runs and roughly how long.

**Optional inputs:**
- Current project(s) and known sticking points.
- The trainee's active IDP or career goals, if one exists.
- Any standing concerns the trainee has flagged.
- Mentor's own goals for the mentoring relationship.

**Constraints — Must:**
- Reserve agenda space the trainee fills; the meeting is not solely the mentor's checklist.
- Cover all three tracks each cycle — research, career, well-being — even if briefly; do not let any track be permanently skipped.
- Use open, growth-oriented questions consistent with CIMER/Entering Mentoring mentoring competencies (aligning expectations, fostering independence, promoting professional development).
- Capture concrete action items with owners and follow-up at the start of the next session.
- For well-being, keep checkpoints supportive and non-diagnostic, and include an explicit route-to-professional-support note (counseling/employee assistance/health services) — this is not a clinical tool.
- Tie career-development talk to a living IDP where one exists, and to responsible, individualized assessment (DORA spirit) rather than journal-name proxies.

**Constraints — Must Not:**
- Do not invent institutional policies, named people, performance facts, or career statistics. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not script the mentor to diagnose, counsel, or manage a mental-health condition; route to professionals.
- Do not turn the well-being checkpoint into surveillance or a performance metric.
- Do not use hype language ("novel," "groundbreaking," "first-ever," "gold standard") in any drafted text.
- Do not let the template imply the mentor decides the trainee's career for them.

**Instructions:**

1. **Confirm scope.** Capture discipline, career stage, and cadence. Note current projects, IDP, and standing concerns if supplied.
2. **Open with continuity.** Begin each session by reviewing prior action items and what changed, so follow-through is visible and the trainee isn't re-explaining context.
3. **Trainee agenda block.** Reserve an explicit slot where the trainee raises whatever matters most to them first, before the mentor's items.
4. **Research-progress track.** Provide focused prompts on progress, blockers, and next experiments/analyses — framed to foster the trainee's own problem-solving rather than the mentor dictating moves. Cross-reference reproducibility/record-keeping where relevant.
5. **Career-development track.** Provide prompts that connect current work to the trainee's goals and IDP, surface skills to build, and identify exploration steps across multiple paths. Keep assessment individualized and contribution-focused.
6. **Well-being checkpoint.** Provide brief, supportive, non-diagnostic check-in prompts (workload sustainability, energy, sense of progress, support needs). Add the route-to-professional-support note and make clear the trainee may decline to discuss.
7. **Build the question bank.** Assemble a reusable bank of open questions grouped by track and by career stage, so the mentor can vary questions without going off-script.
8. **Action capture and close.** End each session by recording decisions and action items (owner + due), confirming the next meeting, and a one-line positive close that names something working.
9. **Periodic relationship check.** Add an occasional meta-question set on whether the 1:1 format and the mentoring relationship are serving the trainee, with room to adjust.

**Output format (locked):**

```
## Session Overview
- Discipline: [...]
- Career stage: [...]
- Cadence & length: [...]
- Linked IDP: [yes/no — path or [user-supplied]]

## Recurring 1:1 Agenda (template)
| Time | Segment | Owner |
|---|---|---|
| | Review prior action items | mentor + trainee |
| | Trainee's agenda (set by trainee) | trainee |
| | Research progress & blockers | both |
| | Career development | both |
| | Well-being checkpoint | both (trainee may decline) |
| | Action capture & close | both |

## Question Bank
### Research progress
- [...]
### Career development (by stage)
- [...]
### Well-being (supportive, non-diagnostic)
- [...]

## Well-Being Routing Note
- This 1:1 is not a clinical or counseling session. For persistent distress, burnout, or
  mental-health concerns, route to [counseling / employee assistance / student or
  occupational health — [user-supplied]]. In an emergency, use local emergency services.

## Action Items
| Item | Owner | Due | Status |
|---|---|---|---|

## Periodic Relationship Check
- [...]
```

**Reporting-standard alignment:** No formal reporting standard; aligns to CIMER/AAAS Entering Mentoring mentoring competencies, the NIH IDP / myIDP framework for the career-development track, DORA for responsible individualized assessment, and well-being/burnout-awareness practice with explicit routing to professional support (the prompt is not a clinical tool).

**Verification checklist (before delivering):**
- [ ] Discipline and career stage captured before tailoring questions.
- [ ] All three tracks (research, career, well-being) present in the template.
- [ ] A trainee-set agenda block precedes the mentor's items.
- [ ] Well-being prompts are supportive and non-diagnostic, with a route-to-professional-support note.
- [ ] Action capture assigns owners and due dates and is reviewed next session.
- [ ] Career track links to the IDP and uses individualized, contribution-focused assessment.
- [ ] No invented policies, names, performance facts, or career stats; gaps marked `[user-supplied]`.
- [ ] No hype adjectives in drafted text.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Status-only creep | A "balanced" template that in practice is all research progress | Reserve fixed segments for career and well-being each cycle |
| Mentor-as-therapist | Well-being prompts that drift into diagnosis or counseling | Keep checkpoints non-diagnostic; include explicit professional-support routing |
| Trainee silenced | Agenda fully owned by the mentor | Require a trainee-set block placed before mentor items |
| Vanishing actions | Good conversation, nothing tracked | Mandatory action table with owners/dates reviewed at next open |
| Proxy assessment | Career talk graded on journal name or volume | Frame assessment as individualized contribution (DORA spirit) |
