---
title: PACU Orientee Weekly Learning Plan
category: pacu/orientation-curriculum
task_type: CREATE
audience: PACU primary preceptor planning any single week of orientation (Week 2 onward)
updated: "2026-05-15"
tags:
  - pacu
  - orientation
  - weekly-plan
  - preceptor
techniques:
  - ST-01
  - ST-02
  - RT-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - prompts/pacu_orientation_curriculum_designer.md
  - prompts/pacu_orientation_first_week_plan.md
  - prompts/pacu_orientation_skill_acquisition_timeline.md
  - prompts/pacu_preceptor_debrief.md
  - prompts/pacu_self_directed_learning_module_designer.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
---

# PACU Orientee Weekly Learning Plan

> Safety reminder: Weekly draft. Hands-on scope expansions must respect the facility orientation program. Verify topic coverage against ASPAN *Standards*.

## Objective

Produce a **single-week orientation plan** for any week from Week 2 through final sign-off. Output sequences theme, competency focus, shift-level targets, source readings, simulation touchpoints, and end-of-week debrief topics. Designed to be re-run for each week of the orientation, consuming the broader pathway from `pacu_orientation_curriculum_designer.md`.

## Inputs

- **Week number and overall orientation length:** {{e.g., Week 4 of 10}}
- **Week theme (from curriculum pathway):** {{e.g., "Regional block resolution + emergence phenomena"}}
- **Orientee background:** {{new-grad | experienced ICU | etc.}}
- **Target sign-off level for this week:** {{Independent | With Cues | With Direction | Not Yet — overall}}
- **Per-competency targets (3–5 competencies):** {{from skill-acquisition timeline}}
- **Shifts this week:** {{e.g., 3 × 12s — list days}}
- **Surgical mix on those days:** {{best-known service mix}}
- **Prior debrief commitments still open:** {{paste from `pacu_preceptor_debrief.md` rolling log}}

## Audience / Scope

- **Primary:** Primary preceptor preparing the upcoming week.
- **Secondary:** Orientee (gets the orientee-facing version as a pre-week briefing).
- **Scope:** One week. Multi-week pathway: use `pacu_orientation_curriculum_designer.md`.

## Output requirements

Produce two outputs in sequence: a **preceptor version** (full) and an **orientee-facing version** (briefer, expectations + readings).

```markdown
# Week {N} of {Total} — Preceptor Plan

> Week theme: {theme}. Target sign-off level: {level} overall.

## Competency focus

For each of 3–5 competencies, name:
- Competency
- Target level this week
- Observable evidence the preceptor will look for
- Cueing-decay expectation (how much support is reasonable)

## Shifts

Repeat for each shift this week.

### Shift {n} — {day} — {hours}

**Likely surgical mix:** {mix}
**Orientee scope:** {what they will lead / co-lead / shadow}
**Preceptor stance:** {1:1 / offstage / hands-off-with-cover}
**Mid-shift micro-check:** {one preceptor question}
**End-of-shift debrief:** {topic 1, topic 2}

## Off-shift learning (1–3 hours total)

- Source readings: {chapters with rationale}
- Self-directed module (if scheduled): {topic} — see `pacu_self_directed_learning_module_designer.md`
- Optional review: {prior topic from rolling debrief log}

## Mid-week check-in (15 min)

- Preceptor + orientee, away from bedside.
- Three prompts:
  1. Where did you feel most prepared this week?
  2. Where did you cue yourself out of a situation that you should have cued the preceptor on?
  3. What's the one thing you want from your preceptor in the back half of the week?

## End-of-week debrief

- Run through each competency: how far did cueing-decay travel?
- Update rolling debrief log (`pacu_preceptor_debrief.md`).
- Carry forward: open commitments → next week's plan.

## Sources / reference

- *Drain's*, {chapters relevant to this week's theme}.
- *Core Curriculum*, {modules}.

---

# Week {N} — Orientee Briefing

> Heads up for next week.

**Theme:** {theme}
**What you'll focus on:** {3–5 competency targets in plain language}
**What I'll be watching for:** {3 observable behaviors, framed as growth not gotcha}
**Reading (≤ 1 hr):** {2–3 chapters}
**Where I'll cue you more than usual:** {1 area}
**Where I'll cue you less than usual:** {1 area}
**One question to start the week with:** {prompt}
```

## Must / Must not

**Must:**
- Use **Independent / With Cues / With Direction / Not Yet** scale tokens for all sign-off levels.
- Tie each competency's evidence to an observable behavior (verb-based: "recognizes," "initiates," "verbalizes").
- Produce both preceptor and orientee-facing versions.
- Reference the rolling debrief log explicitly.
- Adapt cueing-decay expectations to the orientee's background.

**Must not:**
- Schedule hands-on scope that violates the facility orientation program.
- Use generic competency labels ("good communication," "professional behavior"). Anchor in observable behaviors.
- Project the orientee's emotional state ("you're probably anxious about this").
- Reference protected characteristics.
- Conflate "more weeks completed" with "higher competency level."
- Fabricate ASPAN sections or Drain's chapter numbers.

## Quality signals

- A preceptor can hand the plan to a covering preceptor mid-week and they can pick up cleanly.
- The orientee briefing version is short enough that an orientee will actually read it.
- Two different preceptors using this prompt on the same inputs would produce ~90% overlapping plans.
- Cueing-decay expectation visibly differs from last week's plan (or has a stated reason for staying flat).

## Verification

- [ ] Week number, theme, target level all match input.
- [ ] 3–5 competencies named.
- [ ] Every competency has observable evidence + cueing-decay expectation.
- [ ] Both preceptor and orientee versions produced.
- [ ] Mid-week check-in + end-of-week debrief present.
- [ ] Open commitments from prior debrief log referenced.
- [ ] Safety reminder + FPP sections present.

## False-Positive Prevention

- **No invented ASPAN sections, Drain's chapters, or Core Curriculum module numbers.** Placeholder.
- **No invented facility orientation program scope rules** (hands-on permissions, sign-off thresholds).
- **No invented staff names, pager numbers, or escalation phone lines.**
- **No invented doses, vitals thresholds, or device-brand specifics.**
- **No invented competency rubric scores.**
- **No protected-characteristic or license-pathway references.**
- **No fabricated psychological-state assertions** about the orientee.

## Worked Example

<details>
<summary>Example: Week 4 of 10, new-grad, theme "PONV cascade + multimodal pain," 3 × 12s (click to expand)</summary>

```markdown
# Week 4 of 10 — Preceptor Plan

> Theme: PONV cascade + multimodal pain. Target level: With Cues overall.

## Competency focus

- **PONV recognition & escalation** — target: With Cues. Evidence: recognizes high-PONV-risk patient pre-arrival from handoff; verbalizes risk factors; initiates first-line antiemetic per order without cue; reassesses ≤ 15 min after dose.
- **Post-op pain management** — target: With Cues. Evidence: multimodal assessment present in every admission note; pain plan articulated before first dose; reassessment timed and documented.
- **Documentation accuracy** — target: With Cues → Independent on PONV/pain documentation specifically. Evidence: meds + responses charted within 5 min.

## Shift 1 — Mon — 0700–1930

**Likely surgical mix:** mixed general + GYN open (high PONV risk).
**Orientee scope:** lead two admissions under preceptor shadow; preceptor offstage.
**Preceptor stance:** offstage but in earshot.
**Mid-shift micro-check:** "Which of today's admissions had highest PONV risk — and how did you know?"
**End-of-shift debrief:** PONV risk pattern recognition; pain reassessment timing.

## Off-shift learning (≤ 2 hours)

- *Drain's* — PONV chapter, focus on prophylaxis algorithm.
- *Core Curriculum* — multimodal pain module.
- Self-directed module (scheduled mid-week): "Multimodal pain in PACU — first 30 min" — see module designer.

## Mid-week check-in

Three prompts as standard.

## End-of-week debrief

Update rolling debrief log. Open commitment to carry to Week 5: "Independence on PONV reassessment timing — currently With Cues, target Independent."

---

# Week 4 — Orientee Briefing

**Theme:** PONV cascade + multimodal pain.
**Focus:** Recognizing PONV risk before symptoms; planning pain before the first dose; documenting on time.
**I'll be watching for:** Pre-arrival risk verbalization; reassessment timing; documentation lag.
**Reading:** Drain's PONV chapter + Core Curriculum multimodal pain module.
**More cueing than usual:** Pain plan articulation.
**Less cueing than usual:** PONV recognition (you've shown this last week).
**One question to start with:** "What does a high-PONV-risk patient look like at handoff before symptoms appear?"
```

Notes: scale tokens consistent, evidence verb-based, both versions produced, cueing-decay tied to prior week, open commitment carried forward.
</details>

## Self-check

- [ ] Scale tokens used consistently.
- [ ] Both preceptor and orientee versions present.
- [ ] Competency evidence is observable + verb-based.
- [ ] Cueing-decay expectation visible.
- [ ] Open commitments from prior week referenced.
- [ ] No invented sources, scope rules, or doses.
- [ ] Safety + FPP sections passed.
