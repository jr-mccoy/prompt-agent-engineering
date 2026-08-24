---
title: PACU Pediatric Considerations (Population-Specialty Teaching)
category: pacu/population-specialty
task_type: LEARN
audience: PACU orientee or preceptor rotating into (or being cross-trained on) pediatric PACU
updated: "2026-04-16"
tags:
  - pacu
  - pediatric
  - population-specialty
  - emergence-delirium
  - airway
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: advanced
related_prompts:
  - prompts/pacu_topic_primer.md
  - prompts/pacu_complication_deep_dive.md
  - prompts/pacu_medication_profile.md
  - prompts/pacu_emergence_agitation_deescalation.md
  - prompts/pacu_simulation_scenario_builder.md
  - prompts/pacu_unfolding_case_study.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — pediatric chapters
  - ASPAN Standards of Perianesthesia Nursing Practice — pediatric population
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice — pediatric module
  - PAED (Pediatric Anesthesia Emergence Delirium) scale — Sikich & Lerman
---

# PACU Pediatric Considerations

> Safety reminder: Pediatric PACU requires weight-based dosing, age-specific airway management, and family-centered communication. All doses are weight-based and provided by provider order; this teaching prompt uses placeholders ("{{per order — weight-based}}") and never invents specific mg/kg values. Verify against current provider order and facility pediatric protocols before any intervention.

## Objective

Produce a **pediatric-specific PACU considerations teaching artifact** for an adult-trained PACU nurse rotating into or cross-training on pediatric PACU. Covers what differs from adult PACU: airway anatomy, emergence delirium (PAED scale), weight-based-dosing awareness, parental presence, NPO and fluid considerations, and common pitfalls adult-PACU habits bring into the pediatric bay.

## When to use

- Orientation to pediatric PACU rotation for an adult-PACU-trained nurse.
- Cross-coverage preparation when adult PACU takes pediatric overflow.
- Pre-read before a pediatric-focused simulation (`pacu_simulation_scenario_builder.md`).
- Refresher for preceptors mentoring on pediatric cases.

## When not to use

- For general PACU orientation — use `pacu_topic_primer.md`.
- For specific complications — use `pacu_complication_deep_dive.md` and specify pediatric context.
- For dedicated NICU / PICU training — those units have separate orientation programs.

## Inputs

- **Rotation context:** {{dedicated pediatric PACU | adult PACU taking pediatric overflow | short rotation for cross-coverage}}
- **Age range focus:** {{infant (0–1 yr) | toddler/preschool (1–5 yr) | school-age (6–12 yr) | adolescent (13–18 yr) | mixed}}
- **Learner's adult-PACU experience level:** {{Phase 1 orientee with adult background | experienced adult-PACU RN rotating}}
- **Source chapters available:** {{Drain's pediatric chapters, ASPAN pediatric module, facility pediatric protocols}}

## Audience / Scope

- **Primary:** Adult-trained PACU nurse crossing into pediatric PACU or pediatric-overflow care.
- **Scope:** Differences from adult PACU. Not a comprehensive pediatric nursing textbook; not a substitute for PALS certification or facility pediatric-specific orientation.

## Output requirements

```markdown
# Pediatric PACU Considerations — {age range}

> Safety reminder: All doses weight-based and per order. Pediatric airway and physiology differ from adult — adult habits are the most common failure mode. Verify everything against facility pediatric protocols and provider orders.

## What's different from adult PACU (at a glance)
| Domain | Adult PACU default | Pediatric PACU difference |
|---|---|---|
| Airway anatomy | Larynx C3–C4, narrowest at cords | Infant/small-child larynx higher (C2–C4); narrowest at cricoid; relatively large tongue and occiput |
| Ventilation | Tidal volume + rate recognizable by experience | Higher RR baseline; smaller tidal volumes; rapid desaturation due to lower FRC |
| Medications | Adult doses common | All doses weight-based, per order |
| Emergence | Occasional delirium, most predictable | Emergence delirium common, especially age 2–7 after volatile anesthesia; use PAED scale |
| Communication | Patient + family with patient capacity | Family-primary communication; age-appropriate reassurance; parental presence often decreases distress |
| Fluid status | ml / hr ranges adult-familiar | Weight-based maintenance per order; small margin before dehydration or overload |
| NPO / post-op feeding | Standard clear-liquid advance | Age-specific guidelines; shorter fast times often preferred per pediatric anesthesia |
| Thermal regulation | Rewarming usually routine | Infants / small children lose heat rapidly; active warming per facility |
| Pain assessment | Numeric / NRS default | Age-appropriate scales (FLACC for infants / nonverbal; Wong-Baker Faces for ~3–7; numeric ~8+) |
| Consent / assent | Patient-direct | Parent consent + age-appropriate assent |

## Airway anatomy — what adult-PACU habits miss
- **Large tongue + large occiput** in infants: positioning requires roll under shoulders, not under head, to neutralize the head.
- **Narrowest point at cricoid (pre-pubescent):** small subglottic swelling or secretion burden produces stridor fast.
- **Lower FRC:** desaturation progresses in seconds, not minutes. Adult instinct ("trend, then act") is too slow here — action and escalation occur earlier.
- **Obligate nose-breathers (young infants):** nasal obstruction is airway obstruction.

## Emergence delirium — PAED scale
The Pediatric Anesthesia Emergence Delirium (PAED) scale assesses five items (makes eye contact, actions purposeful, aware of surroundings, restless, inconsolable). Score ≥ 10 (of 20) suggests emergence delirium.

**Red-flag pattern:** Child (age ~2–7) post-volatile anesthesia, inconsolable, not making eye contact, thrashing, not responsive to parental presence. This is emergence delirium, distinct from pain.

**What's not emergence delirium:** pain, full bladder, hypoxia, hypoglycemia, first-wave PONV. Rule these out **first** before labeling emergence delirium.

See `pacu_emergence_agitation_deescalation.md` for the structured de-escalation script.

## Weight-based dosing awareness (reminders — not doses)
- **All pediatric doses are weight-based.** No "usual adult dose" applies.
- **Verify weight** (actual, not estimated) on every dose prep. Kilograms, never pounds.
- **Double-check per facility** — pediatric medication independent double-check is standard in most facilities.
- **Concentration and volume matter** — small-volume dilutions common; a 10x error is a clinically catastrophic error, not a minor one.
- **Specific doses are always per order.** This prompt does not provide mg/kg values.

## Parental presence
- **Default is to allow parental presence** at bedside in recovery, per facility policy — parents decrease separation anxiety and accelerate recognition of "something's off" (parents see subtle changes clinicians miss).
- **Brief parents at bedside** on what they'll see (monitors, IV, possible emergence agitation) in plain language.
- **Set role expectations:** parents provide comfort; clinicians manage clinical events; if a clinical event occurs, parents may be asked to step out briefly.
- **Cultural and language considerations:** request interpreter (in-person or telephonic per facility) rather than using family members as interpreters for medical information.

## NPO, fluid, and feeding
- **NPO guidelines are age-specific** and change as pediatric anesthesia literature evolves — defer to current facility pediatric anesthesia NPO policy.
- **Maintenance fluids are weight-based per order** — adult "KVO" is not appropriate for many pediatric patients without a calculated rate.
- **Resume clears when tolerating** per facility criteria (often earlier than adult post-op, depending on surgery and age).

## Pain assessment
- **FLACC (Face, Legs, Activity, Cry, Consolability)** — infants and nonverbal children.
- **Wong-Baker FACES** — ~age 3–7.
- **Numeric rating (NRS)** — age ~8+, per facility.
- Pain and emergence delirium look similar; FLACC score + response to comfort measures helps differentiate.

## Thermal regulation
- Infants have higher surface-area-to-mass ratio; they lose heat rapidly.
- Active warming (warm blankets, forced-air warmer per facility) is routine, not optional.
- Monitor temp per facility pediatric interval.

## Common adult-PACU habits that miss in pediatric PACU
- **Trending BP across multiple cycles before acting.** Pediatric desaturation and decompensation are faster; act earlier.
- **Waiting for the child to verbalize pain.** Infants and young children don't. FLACC-based assessment is primary.
- **Using adult-size BVM or airway adjuncts.** Size matters — verify pediatric-size equipment at the bedside at admission.
- **Over-reliance on SpO₂ in young infants.** Normal ranges differ; monitor work of breathing, color, and RR pattern.
- **Explaining procedures to the child in adult terms.** Age-appropriate language; short, concrete.
- **Treating emergence delirium as a discipline problem.** It's neurologic and transient; de-escalate per `pacu_emergence_agitation_deescalation.md`.

## When to call (escalation by role — pediatric-specific)
- **Pediatric anesthesia by role** for any airway concern, emergence delirium not responding to supportive measures within facility-defined window, new bradycardia (children's HR norms differ — check age-specific).
- **PICU rapid response** for decompensation or escalating respiratory concern.
- **Charge nurse** for staffing / 1:1 assignment for a severe emergence delirium episode.
- **Family liaison / social work** for non-English-speaking families, complex social situations, suspected neglect or abuse concern (mandatory-reporter context — per facility protocol).

## Sources / reference
- *Drain's PeriAnesthesia Nursing*, pediatric chapters.
- ASPAN *Standards of Perianesthesia Nursing Practice* — pediatric population.
- ASPAN *Core Curriculum for PeriAnesthesia Nursing Practice* — pediatric module.
- PAED scale — Sikich & Lerman, 2004.
- Facility pediatric anesthesia and nursing protocols: {{per facility protocol}}.
- PALS certification material (Facility-required for pediatric coverage per policy).
```

## Must / Must not

**Must:**
- Distinguish explicitly from adult PACU — the point of this prompt is cross-training gap-closure.
- Name PAED scale as the emergence-delirium assessment tool.
- Treat all doses as per-order weight-based without stating specific mg/kg values.
- Include parental-presence guidance and cultural/language notes.
- Include age-appropriate pain scales (FLACC, Wong-Baker, numeric).
- Name common adult-PACU habits that fail in pediatric PACU (the whole point of the prompt).
- Cross-reference `pacu_emergence_agitation_deescalation.md` for de-escalation.

**Must not:**
- State specific mg/kg doses, drip rates, concentrations, or vial-dilution volumes. These are always "per order."
- Fabricate age-specific vital-sign ranges. Defer to facility pediatric vital-sign reference.
- Invent NPO times — those change; defer to current facility pediatric anesthesia policy.
- Invent facility-specific pediatric protocols, pager numbers, or PICU activation criteria.
- Substitute for PALS certification or facility pediatric orientation.
- Reference age in an orientee-evaluation context (age is relevant to the patient, not the orientee).
- Reference race, religion, national origin, or other protected characteristics of patients or orientees as performance signals.
- Include patient-identifying information.
- Assume the nurse is scope-extended to perform pediatric intubation or advanced airway — always "prepare equipment and assist provider."

## Quality signals

- An adult-trained nurse reading this knows three specific adult habits that fail in pediatric PACU.
- The PAED scale and FLACC / Wong-Baker scales are named.
- Weight-based dosing awareness is explicit; no specific doses written.
- Parental presence is framed as default + managed, not debated.
- Emergence delirium is distinguished from pain, hypoxia, hypoglycemia, and full bladder.

## Verification

Before returning, verify:

- [ ] Adult-vs-pediatric contrast table is present and covers airway, medications, emergence, fluids, pain, thermal.
- [ ] PAED scale named for emergence delirium assessment.
- [ ] Age-appropriate pain scales named (FLACC, Wong-Baker, numeric).
- [ ] All doses / rates / concentrations are "per order" — no specific mg/kg values.
- [ ] Parental presence framing included with cultural/language notes.
- [ ] Common adult-PACU habits that fail are named explicitly.
- [ ] Escalation named by role (pediatric anesthesia, PICU rapid response, charge).
- [ ] Cross-reference to `pacu_emergence_agitation_deescalation.md` present.

## False-Positive Prevention

Do **not** fabricate:

- **No invented weight-based doses (mg/kg, mcg/kg/min).** Always "per order."
- **No invented pediatric vital-sign ranges** — age-specific norms vary by source and facility; defer.
- **No invented NPO times** — defer to current facility policy.
- **No invented ASPAN section / Drain's chapter citations.** Mark `{{confirm}}` when unknown.
- **No invented facility pediatric protocols, pager numbers, or PICU activation criteria.**
- **No invented PAED score cutoffs beyond the commonly cited ≥ 10 threshold** — cite Sikich & Lerman 2004 for the cutoff.
- **No invented pediatric complication incidence rates.**
- **No patient-identifying information.**
- **No protected-characteristic references** used as performance signals.
- **No scope-creep actions** — pediatric advanced airway remains provider-scope.

## Worked Example

<details>
<summary>Example: "Common adult-PACU habits that miss in pediatric PACU" section for a Week 6 adult-PACU-trained RN rotating (click to expand)</summary>

```markdown
## Common adult-PACU habits that miss in pediatric PACU

1. **Trending BP across three cycles before acting.** In a 4-year-old post-tonsillectomy, desaturation can progress within 60 seconds once breathing is compromised — action and escalation occur earlier than your adult instinct.

2. **Waiting for the child to say "I hurt."** A 2-year-old doesn't. FLACC is the primary pain assessment; if FLACC is rising, treat pain before labeling it emergence delirium.

3. **Using adult-size BVM at the bedside.** Verify pediatric-size BVM, airway adjunct (oral airway, nasal airway), and suction catheter are at the bedside at admission — not when you need them.

4. **Reading SpO₂ in isolation.** A young infant's color, work of breathing, and RR pattern matter more than the number. A well-placed nasal cannula and a calm, pink baby with a soft cry trump a 95% SpO₂ reading in importance.

5. **Explaining the emergence delirium episode to the parent in medical terms.** "This is emergence delirium — it's transient and neurologic, it's not your child being difficult." Short, concrete, parent-facing.

6. **Attempting to "calm" an emergence-delirium child with more stimulation.** Less stimulation, dim lights, quiet voices, parent present if possible. See `pacu_emergence_agitation_deescalation.md`.
```

Notes: each habit names the adult default + the pediatric correction; scope-appropriate (no provider actions); no specific doses; cross-reference to de-escalation prompt.
</details>

## Self-check

- [ ] Adult-vs-pediatric contrast table present.
- [ ] PAED scale named; age-appropriate pain scales named.
- [ ] All doses "per order" — no mg/kg values.
- [ ] Parental presence + cultural/language framing included.
- [ ] Common adult-habit failures named.
- [ ] Escalation by role.
- [ ] Cross-reference to emergence-delirium de-escalation.
- [ ] No invented NPO times, vital-sign ranges, or facility protocols.
- [ ] No patient-identifying information.
- [ ] No protected-characteristic references as performance signals.
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed.
