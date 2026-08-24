---
title: PACU Orientee Evaluation Meta-Prompt
category: pacu/preceptor-evaluation
task_type: CREATE
audience: PACU preceptor, educator, or nurse manager designing an orientee evaluation for a specific week and background
updated: "2026-04-16"
tags:
  - pacu
  - preceptor-evaluation
  - meta-prompt
  - competency
  - orientation
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: advanced
related_prompts:
  - prompts/pacu_preceptor_approach_guide.md
  - prompts/pacu_preceptor_writing_orientee_evaluation.md
  - prompts/pacu_peer_preceptor_360_feedback.md
  - prompts/pacu_preceptor_calibration_facilitator.md
  - prompts/pacu_competency_self_assessment.md
  - prompts/pacu_preceptor_debrief.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
  - Benner, P. — From Novice to Expert (cueing levels and competency framework)
---

# PACU Orientee Evaluation Meta-Prompt

> Safety reminder: This generates the evaluation *scaffold*, not the evaluation itself. Downstream prompts consume it; verify competencies against ASPAN *Standards of Perianesthesia Nursing Practice* and the facility's orientation program before use.

## Objective

Produce a **PACU-specific orientee evaluation scaffold** tailored to the orientation phase and orientee background. Output is the structural context — rubric, question bank, output template, red-flags watch-list, and handoff notes — that the preceptor approach guide, 360 feedback, written evaluation, and calibration prompts consume.

## Why a meta-prompt

Orientee expectations differ sharply between Week 2 and Week 8, and between a new-grad RN and an experienced ICU transfer. One generic scaffold hides those differences and produces vague evaluations. This prompt generates a scaffold shaped for the *specific* orientee in front of the preceptor.

## Inputs

Ask for all four before generating. If any is missing or vague, ask a clarifying question first.

- **Orientation phase:** {{Week 0–2 | Week 2–6 | Week 6–10 | final sign-off | probationary extension}}
- **Orientee background:** {{new-grad RN | experienced RN transitioning to PACU | float-pool returning to PACU | cross-specialty transfer (ICU/ED/L&D/OR)}}
- **Competency framework source:** {{facility framework pasted in | "use a sensible PACU default" | ASPAN Standards as baseline}}
- **Evaluation type:** {{mid-orientation checkpoint | end-of-phase sign-off | final orientation sign-off | probationary extension review}}

## Audience / Scope

- **Primary:** Preceptor or educator preparing to structure an orientee evaluation.
- **Secondary:** The scaffold output is consumed by `pacu_preceptor_approach_guide.md`, `pacu_preceptor_writing_orientee_evaluation.md`, `pacu_peer_preceptor_360_feedback.md`, `pacu_preceptor_calibration_facilitator.md`, and (reviewee-facing) `pacu_competency_self_assessment.md`.
- **Scope:** Phase 1 PACU orientation only. For post-orientation annual review, see facility HR tooling.

## Output requirements

```markdown
# PACU Orientee Evaluation Scaffold

> Safety reminder: Scaffold only — not the evaluation itself. Verify every competency and anchor against ASPAN Standards and the facility orientation program before use.

**Orientation phase:** {phase}
**Orientee background:** {background}
**Evaluation type:** {type}
**Competency framework source:** {user-supplied | sensible default — labeled as starting point}

## Part A — Competency Rubric with Behavioral Anchors

For each competency, show three sign-off-level anchors using the scale:
**Independent / With Cues / With Direction / Not Yet**

Competencies default to (adapt to facility framework if supplied):
- Airway & breathing management (post-extubation, residual blockade recognition)
- Hemodynamic assessment & intervention (post-spinal hypotension, post-op hypertension, fluid status)
- Oxygenation & ventilation (desaturation patterns, escalation triggers)
- Post-op pain management (multimodal assessment, escalation)
- PONV recognition & escalation
- Emergence & delirium assessment
- Regional / neuraxial block assessment (level, reversal timing, safety)
- Handoff communication (SBAR inbound from OR, outbound to floor/ICU/home)
- Family communication & discharge teaching
- Clinical judgment in ambiguity (when to escalate, who to call by role)
- Documentation accuracy (vitals, meds, teaching, discharge criteria)
- Team collaboration & role recognition (CRNA, surgeon, charge, respiratory, pharmacy)

For each competency:
### {Competency name}
**Definition for this orientee's context:** [one sentence specific to phase + background]

| Sign-off level | Behavioral anchor (observable) |
|---|---|
| Independent | [...] |
| With Cues | [...] |
| With Direction | [...] |
| Not Yet | [...] |

Adjacent anchors must differ substantively. If a preceptor cannot tell "With Cues" from "Independent" from your anchors, rewrite them.

## Part B — Evidence-Gathering Question Bank (8–12 questions)

Role- and phase-specific. Bad: "Are they safe?" Good (Week 4 new-grad): "Describe a post-spinal hypotension case this rotation — what was their first action, did they cue themselves on BP trend or wait for the cuff alarm, and how did they communicate escalation?"

Cover at minimum:
- Core clinical recognition (early cues before classic signs)
- Hand-off quality (in and out of PACU)
- Escalation judgment (who they called by role, how fast, what they said)
- Independence trajectory across the phase (not a single snapshot)
- Response to cueing (do they internalize it or wait for the next cue?)
- Cross-team collaboration (CRNA, surgeon, charge, respiratory)
- Documentation integrity
- Response to a miss or near-miss

## Part C — Output Template (the downstream prompt fills this in)

Blank structured template sections:
- Summary (3–5 sentences — scope, trajectory, overall readiness)
- Demonstrated strengths (evidence-anchored, 2–4 items with shift/date anchors)
- Growth edges (evidence-anchored, 2–3 items, each naming the specific behavior to shift)
- Progress against prior debrief commitments
- Sign-off recommendation per competency (using the scale tokens above)
- Overall phase disposition (advance to next phase / extend orientation / remediation)
- Next-phase focus (3 behaviors the orientee and next preceptor will concentrate on)
- Delivery notes (for the 1:1 with orientee)

## Part D — Red Flags and Under-Counted Strengths (PACU-specific)

### Red flags (often look fine on surface)
3–5 items such as:
- Completes the PACU checklist but cannot articulate *why* each step matters ("process-without-pattern")
- Asks many questions but never offers a differential before asking
- Speaks confidently about pathophysiology outside their scope (e.g., anesthetic pharmacology specifics)
- Manages the patient in front of them well but loses situational awareness of the second bay
- Documentation trails actual events by 30+ minutes ("catches up later")

### Under-counted strengths
3–5 items such as:
- Quietly catches a potential safety issue (wrong-side block check, med reconciliation miss) without making a scene
- Admits uncertainty to the right person at the right time
- Asks the CRNA the right handoff clarifying question
- Notices a trend change before the monitor alarms
- Closes the feedback loop from the prior debrief without being prompted

## Part E — Handoff Instructions

Paragraph the preceptor pastes into downstream prompts:

> "The following scaffold is the target for this orientee's evaluation. When preparing evidence, drafting narrative, collecting peer feedback, or calibrating, treat these competencies as the framework, use these anchors to justify sign-off levels, and actively search for the red flags and under-counted strengths listed."

Then explicitly name the downstream prompts this scaffold feeds:
- `prompts/pacu_preceptor_approach_guide.md`
- `prompts/pacu_preceptor_writing_orientee_evaluation.md`
- `prompts/pacu_peer_preceptor_360_feedback.md` (peer-facing subset — only competencies peers observed)
- `prompts/pacu_preceptor_calibration_facilitator.md`
- `prompts/pacu_competency_self_assessment.md` (orientee-facing version)

## Sources / reference
- ASPAN *Standards of Perianesthesia Nursing Practice*, {relevant sections}
- *Drain's PeriAnesthesia Nursing*, {relevant chapters}
- `/corecurriculum/` {relevant modules}
- Facility orientation program document (if supplied)
```

## Must / Must not

**Must:**
- Generate anchors that are **observable behaviors**, not traits or affect ("recognizes SpO₂ downtrend at 94% and repositions jaw before cueing preceptor" not "good at airway").
- Use the sign-off scale tokens **Independent / With Cues / With Direction / Not Yet** consistently.
- Adapt weight to orientation phase (Week 0–2 emphasizes safety foundations & orientation-to-unit; Week 6–10 emphasizes independence & complex-case judgment).
- Adapt weight to background (experienced RN transitioning: emphasize PACU-specific physiology & emergence; new-grad: emphasize task-flow and cue-recognition).
- For probationary extension: surface the risk up front and recommend a real-time conversation before any documentation, using `pacu_preceptor_difficult_conversation_guide.md`.
- Label any "sensible default" competency list clearly as a starting point the facility should replace with its framework.
- Name escalation partners by role (CRNA, charge nurse, anesthesiologist on call, rapid response), never by name.

**Must not:**
- Generate generic corporate-speak competencies ("demonstrates excellence," "drives quality"). If an anchor would apply identically to a PACU RN and an accountant, rewrite it.
- Invent doses, equipment specifics, pager numbers, or facility protocols — defer to `{{per facility protocol}}`.
- Reference age, race, sex, disability, religion, national origin, pregnancy, or other protected characteristics in any anchor, question, or watch-list item.
- Reference license pathway (BSN vs ASN vs LPN-to-RN bridge) as a competency signal — this is a bias vector, not a performance signal.
- Conflate prior unit tenure with PACU competency (an experienced ICU RN is not automatically PACU-ready).
- Produce a scaffold that reads as the evaluation itself — this prompt outputs structure only.
- Fabricate citations or URLs. If source isn't known, mark as `{{cite facility orientation program or ASPAN section}}`.

## Quality signals

- A preceptor reading the scaffold can immediately tell what to observe on the next shift.
- Two different preceptors would arrive at similar sign-off levels using the anchors.
- Evaluation type measurably changed the scaffold (mid-orientation drops the overall disposition question; final sign-off narrows to readiness for independent practice).
- Red flags name behaviors that a surface-level "looks fine" preceptor would miss.

## Verification

Before returning the scaffold, verify:

- [ ] Orientation phase + orientee background visibly shape the anchors (not generic text with a heading swap).
- [ ] Adjacent sign-off anchors are distinguishable — a preceptor can tell "Independent" from "With Cues" from "With Direction" from the wording alone.
- [ ] Every behavioral anchor uses a verb the preceptor can witness ("verbalizes," "initiates," "recognizes," "escalates") — no traits.
- [ ] Competency list matches ASPAN scope (airway, hemodynamics, oxygenation, pain, PONV, emergence, regional, handoff, family communication, judgment, documentation, team collaboration).
- [ ] Red-flag watch-list and under-counted-strengths items are PACU-specific (would not apply to a generic hospital unit).
- [ ] Handoff paragraph names downstream prompts by path.

## False-Positive Prevention

Do **not** fabricate:

- **No invented ASPAN section numbers, Drain's chapter numbers, or citation titles.** If unknown, write `{{confirm section in ASPAN Standards}}`.
- **No invented facility-specific orientation program policies** (maximum extension length, sign-off forms, HR triggers). State "per facility orientation program."
- **No invented escalation pager numbers, phone lines, or rapid-response activation codes.**
- **No invented competency rubric thresholds** ("must score 4/5 to sign off"). Defer to the facility framework.
- **No invented orientee demographics, prior-unit details, or license-pathway inferences.** Use generic placeholders.
- **No behavioral anchors that would apply identically to a PACU RN and an accountant** — that's a failure; rewrite to be PACU-specific.
- **No protected-characteristic references** in anchors, questions, or watch-lists.

## Worked Example

<details>
<summary>Example: Week 6 checkpoint, new-grad RN background, facility default framework (click to expand, abbreviated)</summary>

Shows one competency with full anchors + one evidence question + two red-flag watch-items, to demonstrate the shape:

```markdown
### Hemodynamic assessment & intervention
**Definition for this orientee's context:** At Week 6 for a new-grad, the orientee should recognize post-spinal, post-blood-loss, and post-emergence BP trends proactively; initiate standard interventions (position, fluid per order, notify) without waiting for alarm.

| Sign-off level | Behavioral anchor (observable) |
|---|---|
| Independent | On two consecutive admissions, recognizes early BP drift from baseline, initiates positional adjustment per order, notifies CRNA by role with clear SBAR, and documents within 5 minutes — without preceptor cue. |
| With Cues | Recognizes BP drift when preceptor asks "what is the trend?"; initiates intervention after a cue; SBAR is complete but requires prompting for the Recommendation. |
| With Direction | Recognizes BP change only after preceptor names it; follows step-by-step direction on intervention; SBAR is fragmentary. |
| Not Yet | Does not recognize BP drift until alarm sounds; waits for preceptor to act; does not communicate to CRNA without being told. |

**Evidence question (Week 6, new-grad):**
"Describe a post-spinal hypotension case this rotation. What cue did the orientee use first — the trend across cycles, or the alarm? How fast did they escalate? Did they initiate SBAR unprompted?"

**Red-flag watch-item (often looks fine on surface):**
"Completes the full PACU admission checklist proficiently, but does not verbalize a differential when vitals trend — operates on process without pattern recognition."

**Under-counted strength:**
"Recognizes BP drift before the monitor alarm sets and quietly repositions without announcing it — easy to miss because nothing dramatic happens."
```

Notes: Week 6 + new-grad shape the Independent anchor ("without preceptor cue" is the gate, not "independent practice"), anchors are sharply distinguishable, red flag surfaces a "process-without-pattern" failure mode specific to PACU.
</details>

## Self-check

- [ ] Orientation phase and orientee background explicitly shaped the scaffold (not a generic template).
- [ ] Every anchor describes observable behavior, not a trait.
- [ ] Adjacent sign-off levels differ substantively.
- [ ] Sign-off scale tokens used consistently: Independent / With Cues / With Direction / Not Yet.
- [ ] Escalation partners named by role, never by name.
- [ ] No invented doses, facility specifics, or fabricated citations.
- [ ] No references to protected characteristics or license pathway.
- [ ] Red flags are things that look fine on surface metrics.
- [ ] Handoff block names the downstream prompts.
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed — no invented ASPAN references, facility policies, or generic corporate-speak anchors.
