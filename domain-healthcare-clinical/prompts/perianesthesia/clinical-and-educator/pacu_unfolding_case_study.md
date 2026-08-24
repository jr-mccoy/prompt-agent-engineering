---
title: PACU Unfolding Case Study (Multi-Stage Paper Case)
category: pacu/simulation
task_type: SIMULATE
audience: PACU educator or preceptor designing a written multi-stage case for self-study or small-group teaching
updated: "2026-04-16"
tags:
  - pacu
  - simulation
  - unfolding-case
  - case-study
  - self-study
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - prompts/pacu_simulation_scenario_builder.md
  - prompts/pacu_simulation_debrief_facilitator.md
  - prompts/pacu_complication_deep_dive.md
  - prompts/pacu_quick_quiz_generator.md
  - prompts/pacu_topic_primer.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
  - ASPAN Standards of Perianesthesia Nursing Practice
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
  - NCSBN Clinical Judgment Measurement Model (CJMM) — for reasoning stages
---

# PACU Unfolding Case Study

> Safety reminder: Educational case study only. All doses, vitals, equipment, and escalation specifics are illustrative; facility protocol governs real patients.

## Objective

Produce a **multi-stage paper case** (4–6 stages) for self-study, 1:1 teaching, or small-group discussion. Each stage delivers new information, prompts the learner to commit to a reasoning step before the next stage reveals, and names the common wrong turns. Output is the full case with stage-by-stage reveals, decision prompts, expected reasoning, common wrong turns, and teaching pearls.

## When to use

- Asynchronous learning for orientees who cannot attend sim lab.
- Pre-read before a hands-on simulation (`pacu_simulation_scenario_builder.md`).
- 1:1 preceptor-orientee teaching during low-census shifts.
- Remediation practice between reassessment shifts.

## When not to use

- For hands-on skill practice → use `pacu_simulation_scenario_builder.md`.
- For knowledge-check only → use `pacu_quick_quiz_generator.md`.
- For rapid-fire bedside coaching → use `pacu_skill_drill_designer.md`.

## Inputs

- **Topic / clinical focus:** {{e.g., "post-op delirium in a geriatric patient," "post-spinal hypotension with volume depletion," "residual NMB after long case"}}
- **Target competency** from `pacu_orientee_evaluation_meta_prompt.md` scaffold.
- **Learner level:** {{Week 0–2, Week 2–6, Week 6–10, final sign-off, remediation}}
- **Number of stages:** {{4–6; default 5}}
- **Mode:** {{linear (one path) | branching (choose-your-action)}}
- **Source chapters / protocols to anchor:** {{Drain's chapter, ASPAN standard, Core Curriculum module}}

## Audience / Scope

- **Primary user:** Educator or preceptor designing the case.
- **Learner:** Phase 1 PACU orientee.
- **Scope:** PACU Phase 1 orientation teaching only.

## Output requirements

```markdown
# {Case title} — PACU Unfolding Case Study

> Safety reminder: Educational only. Doses, vitals, and escalation specifics illustrative; facility protocol governs real patients.

## Target Competency
{From scaffold} — {sub-behavior the case teaches}

## Learner Level
{Phase / background the case is calibrated to}

## Learning Objectives (3 max)
1. ...
2. ...
3. ...

## Case Opening
- **Patient:** initials + age range only; no MRN, full name, DOB, or room number.
- **Surgery & anesthesia:** {generic; no specific drug regimen}
- **Relevant history:** {2–3 items driving the case}
- **Why they're in PACU now:** {the orienting sentence}
- **OR-to-PACU handoff summary:** {2–3 sentence SBAR-style handoff}

---

## Stage 1 — Arrival at T+0

**What you see:**
- Vitals: {ranges or qualitative}
- Exam: {2–3 observable findings}
- Monitor: {what's displayed}
- Environment: {1 realism element}

**Your action now (commit before turning page):**
- What are the top 2 things on your differential at this moment?
- What's the first assessment you do before touching any order?
- What cue, if it appeared in the next 5 minutes, would escalate your concern?

*Expected reasoning (reveal after learner commits):* ...
*Common wrong turns:* ...
*Teaching pearl:* ...

---

## Stage 2 — New finding at T+5

**What changes:**
- {new cue — trend, complaint, or exam finding}
- {optional: distractor — family member, second bay, phone call}

**Your action now:**
- How does this change your differential?
- What SBAR would you call at this point, and to whom (by role)?
- What would you document right now vs. what can wait?

*Expected reasoning:* ...
*Common wrong turns:* ...
*Teaching pearl:* ...

---

## Stage 3 — Pivot at T+10

**What changes:**
- {pivot cue — either stabilization or deterioration}
- {optional: a provider order arrives, or doesn't arrive when expected}

**Your action now:**
- Based on the pivot, what's your next move?
- What's the red-flag trigger you're watching for?
- If the provider doesn't respond within {interval}, what's your escalation?

*Expected reasoning:* ...
*Common wrong turns:* ...
*Teaching pearl:* ...

---

## Stage 4 — Resolution or Deterioration at T+15

**What changes:**
- {either stable-enough-to-transfer OR deterioration requiring rapid response}

**Your action now:**
- Name the handoff items (inbound or outbound, per resolution).
- What does your charting capture at this point?
- What follow-up anticipation goes in the handoff?

*Expected reasoning:* ...
*Common wrong turns:* ...
*Teaching pearl:* ...

---

## (Optional) Stage 5 — Follow-Through

**What the next shift or next unit might see:**
- {late sign that, if missed, comes back as a bounce-back or complication}

**Your action now:**
- What did the handoff need to include to prevent this bounce-back?
- What's the learning from the full arc?

*Expected reasoning:* ...
*Common wrong turns:* ...
*Teaching pearl:* ...

---

## Case Synthesis (after final stage)
- **The arc in one sentence:** ...
- **Key pattern to carry forward:** ...
- **How this connects to scaffold competencies:** ...
- **Related resources:** link to `pacu_complication_deep_dive.md`, `pacu_red_flag_card.md`, topic primer, med profile.

## Discussion Questions (for small group or 1:1)
1. Where was the pivot point in the case, and what cue defined it?
2. Where did the common-wrong-turn path lead, and what's the safeguard?
3. What would you tell a peer who's about to walk into this case cold?
4. What's the one sentence you'd write on your pocket card after this case?

## Sources / reference
- *Drain's PeriAnesthesia Nursing*, Ch. {X}
- ASPAN *Standards of Perianesthesia Nursing Practice*, {section}
- ASPAN *Core Curriculum for PeriAnesthesia Nursing Practice*, {module}
- NCSBN Clinical Judgment Measurement Model (framework for reasoning stages)
```

## Must / Must not

**Must:**
- 4–6 stages, each with a clear new-information reveal.
- Each stage requires the learner to **commit** to a reasoning step before the reveal.
- Every stage names ≥ 1 common wrong turn.
- Every stage has a teaching pearl tied to the competency.
- Escalation partners named by role (CRNA, charge, anesthesiologist on call, rapid response).
- Case synthesis connects back to scaffold competencies explicitly.

**Must not:**
- Fabricate doses, specific vital-sign thresholds, or facility protocols. Use "per order" / "trending" / placeholder.
- Invent ASPAN or Drain's citations.
- Include patient-identifying information (MRN, full name, full DOB, room number).
- Reference age, race, sex, disability, religion, national origin, pregnancy, license pathway, or prior unit unless clinically essential and bias-checked.
- Write stages that require the learner to perform provider-scope interventions.
- Build a branching case with dead-end paths that punish learners without teaching — every wrong turn loops back to a teaching pearl.
- Substitute for bedside clinical observation.

## Quality signals

- A learner reading the case alone can stop, think, commit, and check their reasoning.
- Common wrong turns are named explicitly (not hinted at).
- The case arc reflects a realistic PACU flow from handoff to handoff.
- Every teaching pearl connects a specific cue to a specific action.
- The case could be used as pre-read before a live sim on the same topic.

## Verification

Before returning the case, verify:

- [ ] 4–6 stages, each with "What you see / what changes" + "Your action now (commit)" + reveal.
- [ ] Every stage names a common wrong turn.
- [ ] Every stage has a teaching pearl.
- [ ] Target competency is named and visibly drives the stages.
- [ ] Escalation named by role throughout.
- [ ] Case synthesis connects back to scaffold.
- [ ] Discussion questions are open-ended, not yes/no.
- [ ] Any numeric vitals are ranged or qualitative (no invented specific thresholds).

## False-Positive Prevention

Do **not** fabricate:

- **No invented doses, drip rates, or concentrations** — use "per order" / placeholders.
- **No invented vital-sign thresholds** driving the plot ("BP hits 88/50 exactly") unless the source supplies them. Use ranges or qualitative ("dropping," "persistent").
- **No invented facility policies, rapid-response codes, or pager numbers.**
- **No invented equipment specifics** (bag-valve-mask model, syringe concentration).
- **No invented patient demographics, socioeconomic history, or personal circumstances** beyond what the clinical case requires.
- **No invented ASPAN section / Drain's chapter citations.** Mark `{{confirm}}` when unknown.
- **No scope-creep expected actions** — nurses assist providers; do not prescribe provider actions as learner actions.
- **No protected-characteristic references** framing demographics as a signal.
- **No dead-end branches** that fail without teaching.

## Worked Example

<details>
<summary>Example: Topic = "Residual NMB after long case," Week 6 orientee, 5-stage linear case (click to expand, abbreviated)</summary>

```markdown
# Residual NMB After Long Case — PACU Unfolding Case Study

## Stage 1 — Arrival at T+0

**What you see:**
- Patient J.S., 62M, post-laparoscopic Whipple (6-hour case), GA with rocuronium per order, reversed with sugammadex per order at OR exit.
- Vitals: BP 122/74, HR 88, RR 14 (shallow), SpO₂ 95% on 4L NC, drowsy but arousable, A&Ox3 when stimulated.
- Extremities warm; sustained head-lift not yet assessed.

**Your action now (commit before turning page):**
- Top 2 differentials for the shallow breathing?
- First bedside assessment?
- What cue in next 5 min would escalate?

*Expected reasoning:* Differentials include residual NMB and residual opioid sedation. First assessment: sustained head-lift + tidal volume observation + prior anesthesia record review. Escalation cue: head-lift < 5 sec, or shallower RR pattern, or new SpO₂ drop.

*Common wrong turns:* Attributing the shallow breathing to "normal post-op tiredness" without testing head-lift; reassuring self on SpO₂ 95% without checking tidal-volume pattern.

*Teaching pearl:* Long rocuronium cases + any reversal carry residual-blockade risk. SpO₂ lags behind tidal-volume changes. Head-lift is the cheapest, earliest test you have.

---

## Stage 2 — New finding at T+5

**What changes:**
- Sustained head-lift < 5 sec; patient has trouble swallowing; drool on chin.
- Family member (SP or described) asks when patient can go home.

**Your action now:**
- Differential update?
- SBAR to whom, by role, and what's the R?
- Document now or later?

*Expected reasoning:* Residual NMB is now the leading hypothesis. SBAR to CRNA by role — R: evaluate for additional reversal per order. Document now: head-lift finding + time + cue + escalation.

*Common wrong turns:* Waiting for SpO₂ to drop before escalating. Deferring the family member's question so abruptly that they escalate to charge; safer to pause, address briefly, return.

*Teaching pearl:* Residual blockade: escalate on tidal-volume and head-lift signs, not on SpO₂ alone.

---

[Stages 3–5 continue: CRNA evaluates, additional reversal administered per order, resolution OR deterioration branch, handoff or rapid response.]

## Case Synthesis
- **Arc in one sentence:** Residual NMB after long rocuronium case — tidal-volume and head-lift findings are early; SpO₂ is late; escalate by role before the alarm sets.
- **Connects to scaffold:** Airway & breathing management, clinical judgment in ambiguity, handoff communication.
- **Related resources:** `pacu_complication_deep_dive.md` (residual NMB), `pacu_medication_profile.md` (sugammadex, neostigmine).
```

Notes: five stages, each requires commitment before reveal, wrong turns named explicitly, teaching pearl ties cue to action, no specific mg doses written, initials + age only.
</details>

## Self-check

- [ ] 4–6 stages with commit-before-reveal structure.
- [ ] Every stage has common wrong turns + teaching pearl.
- [ ] Target competency named and drives stages.
- [ ] Escalation by role throughout.
- [ ] No invented doses, thresholds, or facility specifics.
- [ ] No patient-identifying information.
- [ ] No protected-characteristic references.
- [ ] Case synthesis connects to scaffold.
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed.
