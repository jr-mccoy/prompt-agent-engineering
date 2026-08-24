---
title: PACU Orientation Curriculum Designer
category: pacu/orientation-curriculum
task_type: CREATE
audience: PACU educator, preceptor, or nurse manager designing a Phase 1 PACU orientation pathway for a specific orientee
updated: "2026-05-15"
tags:
  - pacu
  - orientation
  - curriculum
  - keystone
  - preceptor
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-02
  - ED-02
  - DS-06
difficulty: advanced
related_prompts:
  - prompts/pacu_orientation_first_day_packet.md
  - prompts/pacu_orientation_first_week_plan.md
  - prompts/pacu_orientee_weekly_learning_plan.md
  - prompts/pacu_orientation_skill_acquisition_timeline.md
  - prompts/pacu_background_specific_pathway_adapter.md
  - prompts/pacu_orientation_surgical_mix_mapper.md
  - prompts/pacu_orientation_simulation_calendar_designer.md
  - prompts/pacu_orientee_evaluation_meta_prompt.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
  - Benner, P. — From Novice to Expert
---

# PACU Orientation Curriculum Designer

> Safety reminder: This is a curriculum scaffold, not the facility orientation program. Anchor against ASPAN *Standards of Perianesthesia Nursing Practice* and the facility's existing orientation program before adopting. Every output is a draft the unit educator edits.

## Objective

Produce a **week-by-week PACU Phase 1 orientation pathway** tailored to a specific orientee's background, the facility's surgical mix, and the target orientation length. Output sequences topics, competency targets (Independent / With Cues / With Direction / Not Yet), shift-level learning activities, source-chapter readings, simulation touchpoints, and evaluation checkpoints from Week 0 through final sign-off.

## Why a designer prompt

Stock 10-week orientation plans treat every orientee identically. A new-grad RN, an experienced ICU transfer, and a returning float-pool RN need substantively different sequencing, even if the end-state competencies are identical. This prompt produces the *specific* pathway for the orientee in front of the educator.

## Inputs

Ask for all five before generating. If any is missing or vague, ask a clarifying question first.

- **Target orientation length:** {{e.g., 8 weeks | 10 weeks | 12 weeks | 14 weeks}}
- **Orientee background:** {{new-grad RN | experienced RN with no PACU | experienced ICU RN | experienced ED RN | experienced L&D RN | experienced OR RN | float-pool RN returning to PACU | other — describe}}
- **Facility surgical mix (rough % or top 5 services):** {{e.g., 35% ortho, 25% general, 15% GYN, 10% urology, 10% ENT, 5% other}}
- **Competency framework source:** {{facility framework pasted in | "use a sensible PACU default" labeled clearly as a starting point | ASPAN Standards as baseline}}
- **Known constraints:** {{e.g., orientee already has TNCC/PALS, no peds rotation available, night-shift only, condensed timeline}}

## Audience / Scope

- **Primary:** PACU unit educator, lead preceptor, or nurse manager designing an orientation pathway.
- **Secondary:** Hand off the output to `pacu_orientee_weekly_learning_plan.md` (for week-level expansion), `pacu_orientation_skill_acquisition_timeline.md` (for sign-off-level mapping), and `pacu_orientee_evaluation_meta_prompt.md` (for the evaluation scaffolds that pace the orientation).
- **Scope:** Phase 1 PACU orientation only. Out of scope: Phase 2 / fast-track ambulatory orientation, pre-op interview training, charge-nurse orientation, annual competencies.

## Output requirements

```markdown
# PACU Phase 1 Orientation Pathway — {Orientee Background}, {N} weeks

> Safety reminder: Draft pathway. Verify every competency against ASPAN *Standards* and the facility orientation program before adopting. Anchors and sequencing are starting points the unit educator must adapt.

**Orientee background:** {background}
**Target length:** {N} weeks
**Facility surgical mix (declared):** {mix}
**Competency framework:** {user-supplied | sensible default — flagged}
**Known constraints:** {constraints}

## Pathway at a glance

| Week | Theme | Target sign-off level (overall) | Key surgical exposures | Major evaluation event |
|---|---|---|---|---|
| 0 | Onboarding / unit foundation | n/a | shadow only | unit-orientation checklist |
| 1 | Admit-to-recover task flow | With Direction | high-volume general | end-of-week debrief |
| 2 | … | … | … | … |
| … | … | … | … | … |
| N | Independent practice | Independent | full mix | final sign-off |

## Per-week detail

Repeat the block below for each week from Week 0 to Week N.

### Week {n}: {Theme}

**Target sign-off level by end of week:** {Independent | With Cues | With Direction | Not Yet} — overall, with per-competency variation noted below.

**Competency focus (3–5 competencies emphasized this week):**
- {Competency 1} — target: {level} — evidence the preceptor will look for: {observable behavior}
- {Competency 2} — target: {level} — evidence: …
- (3–5 total)

**Surgical exposure target (assignments to seek):**
- {service / case type} — rationale: {why this week}
- (1–3 items)

**Shift-level learning activities:**
- Shift 1: {pairing, observation targets, hands-on scope}
- Shift 2: …
- Shift 3: …
- (Match the unit's typical 3–4 shifts/week cadence; mark off-shift / self-study days explicitly)

**Source readings (Drain's / Core Curriculum / facility chapters):**
- {chapter title} — {≤2 line rationale}
- (2–4 items)

**Simulation / drill touchpoints (if any this week):**
- {scenario type} — see `pacu_orientation_simulation_calendar_designer.md`
- (0–2 items)

**End-of-week debrief topics:**
- {topic 1}
- {topic 2}
- (3–5 items — feeds `pacu_preceptor_debrief.md`)

**Evaluation event:** {none | mid-orientation checkpoint | end-of-phase sign-off | final sign-off} — if present, feeds `pacu_orientee_evaluation_meta_prompt.md`.

## Background-specific adjustments applied

Brief paragraph (3–5 sentences) naming exactly which sequencing and pacing choices were shaped by the orientee's background. For example: "Because this orientee is an experienced ICU RN, Weeks 1–2 compress airway-and-hemodynamic foundations from 8 shifts to 4, and Week 3 emphasizes regional anesthesia and emergence phenomena that are PACU-distinctive and not directly transferable from ICU practice. ICU-halo risk is flagged in the Week 4 pacing check."

## Surgical-exposure budget

3–4 sentence summary of how the pathway distributes orientee shifts across the declared surgical mix over the orientation length. If a service is underrepresented in the natural schedule, name it and recommend `pacu_orientation_surgical_mix_mapper.md` to engineer exposure.

## Evaluation events on this pathway

Ordered list of every evaluation event (mid-orientation checkpoint, end-of-phase sign-off, final sign-off) with target week and the downstream prompt that produces each artifact.

## Pathway dependencies

The pathway assumes:
- Existence of a facility orientation program document (for sign-off forms, mandatory competencies, HR triggers — defer to it).
- Availability of `/Drains-Perianesthesia-Nursing/` and `/corecurriculum/` source chapters.
- A primary preceptor + 1–2 secondary preceptors covering the orientee's shift mix.
- Access to a simulation or skill-drill space at least biweekly (otherwise mark simulation touchpoints as "case discussion only").

## Sources / reference

- ASPAN *Standards of Perianesthesia Nursing Practice*, {relevant sections — `{{confirm}}` if unknown}.
- *Drain's PeriAnesthesia Nursing*, {relevant chapters}.
- *ASPAN Core Curriculum*, {relevant modules}.
- Facility orientation program (if supplied).
```

## Must / Must not

**Must:**
- Sequence topics from foundational (airway, hemodynamics, handoff) to complex (multi-system emergence, regional resolution, judgment in ambiguity).
- Match week count to the user's declared target length exactly — do not silently extend or compress.
- Use the **Independent / With Cues / With Direction / Not Yet** scale tokens consistently across weeks (same scale the v2 Preceptor Evaluation Suite uses).
- Adapt the pathway to the orientee's background — and visibly name the adaptations in the "Background-specific adjustments" section.
- Name escalation partners by role (CRNA, anesthesiologist on call, charge nurse, rapid response, surgeon) only.
- Label any default competency list clearly as a starting point the facility must replace with its framework.
- Reference, but do not duplicate, the per-topic primer/quick-ref/explainer skills (the curriculum schedules them; the skills produce the content).

**Must not:**
- Generate generic week themes ("Week 4: Advanced Care") that could apply to any unit. Themes must name PACU-specific content (e.g., "Week 4: Regional block recovery + post-op PONV escalation").
- Invent facility-specific equipment, sign-off forms, HR escalation policies, or maximum extension lengths.
- Reference age, race, sex, disability, religion, national origin, pregnancy, or other protected characteristics anywhere in the pathway.
- Reference license pathway (BSN vs ASN vs LPN-to-RN) as a sequencing signal.
- Conflate prior unit tenure with PACU readiness (an experienced ICU RN does not skip PACU emergence foundations).
- Fabricate ASPAN section numbers or Drain's chapter numbers. Where unknown, write `{{confirm chapter in Drain's / Core Curriculum}}`.

## Quality signals

- A reader can hand the Week 3 block to a primary preceptor on Sunday night, and the preceptor can schedule next week's shifts and readings from it without further consultation.
- Two different educators using this prompt with the same inputs would produce pathways with the same overall shape (90%+ overlap on theme sequencing).
- Background adjustments are visibly different across new-grad / ICU-transfer / float-return runs of the same prompt — not a heading swap.
- Weeks 1 and N do not look like the same week with different titles.

## Verification

- [ ] Week count matches user-declared target length exactly.
- [ ] Each week has a distinct PACU-specific theme (no "Advanced Care" generic labels).
- [ ] Each week's competency focus uses the four-level scale tokens.
- [ ] Background-specific adjustments paragraph names at least 3 concrete sequencing decisions tied to the orientee's prior experience.
- [ ] Surgical mix distribution sums to roughly the declared mix percentages.
- [ ] At least one evaluation event is scheduled before the midpoint and at the end.
- [ ] Source chapters cited by title; no fabricated numbers.
- [ ] Safety reminder at top.
- [ ] False-Positive Prevention section passed.

## False-Positive Prevention

Do **not** fabricate:

- **No invented ASPAN section numbers or Drain's chapter numbers.** If unknown, write `{{confirm in ASPAN Standards}}` or `{{confirm Drain's chapter}}`.
- **No invented facility-specific orientation program policies** (sign-off form names, maximum extension length, HR triggers, probationary review thresholds). Defer to "per facility orientation program."
- **No invented escalation pager numbers, phone extensions, rapid-response codes, or named staff.**
- **No invented doses, dilutions, or vitals thresholds** anywhere a competency anchor mentions a clinical scenario. Use qualitative cues ("BP trending below baseline") or `{{per provider order}}`.
- **No invented surgical-mix percentages**. Use only the percentages the user declared; if the user said "rough mix," call your output rough.
- **No invented competency rubric thresholds** ("must score 4/5 to sign off"). Defer to facility framework.
- **No invented orientee demographics or prior-unit details** beyond what the user declared.
- **No protected-characteristic references** in any week's theme, competency, or activity.
- **No license-pathway sequencing signals** (BSN vs ASN vs LPN-to-RN). License does not change PACU readiness.

## Worked Example

<details>
<summary>Example: 10-week orientation, experienced ICU RN, ortho-heavy mix (click to expand, abbreviated)</summary>

```markdown
# PACU Phase 1 Orientation Pathway — Experienced ICU RN, 10 weeks

**Orientee background:** Experienced ICU RN, 4 yrs medical-surgical ICU; no PACU history.
**Target length:** 10 weeks
**Facility surgical mix (declared):** 35% ortho, 25% general, 15% GYN, 10% urology, 10% ENT, 5% other.
**Competency framework:** Facility framework (provided).

## Pathway at a glance (abbreviated)

| Week | Theme | Target level | Surgical exposure | Eval event |
|---|---|---|---|---|
| 0 | Unit + workflow foundation | n/a | shadow | unit checklist |
| 1 | Admit-recover task flow, OR-to-PACU handoff | With Direction | gen surg, ortho | end-of-week debrief |
| 2 | Airway after extubation + residual blockade | With Cues | gen surg, ortho | debrief |
| 3 | Hemodynamics — post-spinal, post-blood-loss | With Cues | ortho (TKA/THA), GYN | mid-orientation checkpoint |
| 4 | PONV cascade + multimodal pain | With Cues → Independent on basics | mixed | debrief |
| 5 | Regional block resolution + emergence phenomena | With Cues | ortho, urology, ENT | debrief |
| 6 | Judgment in ambiguity, second-bay awareness | With Cues → Independent | mixed | end-of-phase sign-off |
| 7 | Cross-team escalation, complex handoffs out | Independent on most | mixed | debrief |
| 8 | Surgical-mix breadth — rarer services | Independent | underexposed services | debrief |
| 9 | Independent practice with preceptor shadow | Independent | full mix | debrief |
| 10 | Final sign-off | Independent | full mix | final sign-off |

### Week 3: Hemodynamics — post-spinal, post-blood-loss

**Target sign-off level by end of week:** With Cues overall.

**Competency focus:**
- Hemodynamic assessment & intervention — target: With Cues — evidence: recognizes BP drift across 2 consecutive cycles before alarm; initiates positional or fluid intervention per order; SBAR-escalates by role.
- Regional / neuraxial block assessment — target: With Direction — evidence: identifies block level, projects expected resolution window.
- Documentation accuracy — target: With Cues — evidence: vitals + interventions charted within 5 min.

**Surgical exposure target:**
- TKA / THA (ortho) — high spinal volume, expected post-spinal hypotension exposure.
- GYN open case — expected blood-loss-related hemodynamics.

**Shift-level learning activities:**
- Shift 1: 1:1 preceptor, two spinal cases; preceptor narrates first, orientee narrates second.
- Shift 2: 1:1 preceptor, mixed cases; orientee leads admission, preceptor shadows.
- Shift 3: 1:1 preceptor; preceptor pulls back to "preceptor of record but offstage"; mid-shift check-in.
- Off-shift day: self-directed module on post-spinal hypotension (use `pacu_self_directed_learning_module_designer.md`).

**Source readings:**
- *Drain's* — Regional Anesthesia / Neuraxial Block Management chapter — focus on resolution timelines.
- *Core Curriculum* — hemodynamic management module.

**Simulation touchpoints:**
- Post-spinal hypotension scenario, mid-week — see simulation calendar.

**End-of-week debrief topics:**
- First-cue vs alarm-driven recognition (where did orientee land on each case?)
- Confidence vs accuracy on block-level assessment.
- SBAR clarity to CRNA — was Recommendation present every time?

**Evaluation event:** Mid-orientation checkpoint — feeds `pacu_orientee_evaluation_meta_prompt.md`.

## Background-specific adjustments applied

Because this orientee is an experienced ICU RN, Weeks 1–2 compress titration-and-monitoring foundations that transfer from ICU (chunked to 4 shifts instead of 6). Week 3 expands hemodynamics into PACU-specific contexts (post-spinal, post-blood-loss) that are not directly transferable from ICU. Week 5's regional-block content is built up from scratch because regional block resolution is a PACU-distinctive competency. ICU-halo risk — assuming PACU-ready because of prior ICU competence — is flagged for the Week 4 pacing diagnostic.
```

Notes on Tier 1 quality: every week has a distinct PACU theme, sign-off scale tokens used consistently, background adjustments named concretely (compressed weeks 1–2, expanded weeks 3 + 5), evaluation events scheduled, no invented doses or facility specifics.
</details>

## Self-check

- [ ] Week count matches target length.
- [ ] Themes are PACU-specific.
- [ ] Four-level scale tokens used consistently.
- [ ] Background adjustments visibly shaped sequencing.
- [ ] Surgical mix distribution declared and respected.
- [ ] Evaluation events scheduled (≥ 1 mid, 1 final).
- [ ] No invented ASPAN sections, Drain's chapters, doses, thresholds, or facility specifics.
- [ ] No protected-characteristic references.
- [ ] No license-pathway sequencing.
- [ ] Safety reminder + Verification + FPP sections present.
