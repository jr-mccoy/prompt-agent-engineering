---
title: PACU Drug Monograph — Vasopressors Reference (Ephedrine / Phenylephrine, by Mechanism)
category: pacu/pharmacology
task_type: LEARN
audience: PACU orientee (any phase) or preceptor for huddle
updated: "2026-07-07"
tags:
  - pacu
  - pharmacology
  - vasopressors
  - hypotension
  - hemodynamics
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - pacu_post_op_hypertension.md
  - pacu_oliguria_urinary_retention.md
  - pacu_medication_profile.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — cardiovascular / pharmacology chapters
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Hospital pharmacy monograph (facility-specific; confirm current version)
---

# Vasopressors — PACU Drug Reference (Ephedrine / Phenylephrine)

> Safety reminder: This is a **mechanism-and-when-which** reference, not a drip calculator — no bolus math, no infusion rates, no concentrations. The first move for PACU hypotension is to **hunt the reversible cause**, not to chase the number; vasopressors are given per provider order. See `../SAFETY_PREAMBLE.md`.

## Objective

Produce a PACU-focused reference on the two commonly-ordered PACU vasopressors that teaches which to expect when (by heart-rate context), the cause-first mindset for hypotension, and the monitoring/anticipation each agent demands — with all pharmacology provider-ordered.

## Inputs

- **Vasopressors on your PACU formulary / order sets:** {{ephedrine, phenylephrine — bolus and/or infusion}}
- **Facility protocol for post-op hypotension:** {{cause workup + order set}}
- **Common causes on your unit:** {{hypovolemia/bleeding, neuraxial sympathectomy, residual anesthetic vasodilation, cardiac}}

## Audience

- Orientee at any phase — hemodynamic pharmacology tied to cause-finding.
- Preceptor building a post-op-hypotension huddle.

## Output requirements

```markdown
# Vasopressors — PACU Reference (Ephedrine / Phenylephrine)

> Safety reminder: Find the cause first. All dosing per order. No drip math.

## Cause-first mindset (before any pressor)
- PACU hypotension has treatable drivers — hypovolemia / bleeding, neuraxial-induced sympathectomy, residual anesthetic vasodilation, cardiac causes, and (rarely) anaphylaxis. Recognize the low pressure, look for the driver, notify the provider, and give the ordered agent as a bridge — not as a substitute for treating the cause.

## The two agents (mechanism → hemodynamic effect → when it fits)

### Ephedrine
- Mechanism: mixed sympathomimetic (indirect + direct), acting at both alpha and beta receptors.
- Effect: tends to raise blood pressure **and** heart rate / cardiac output.
- When it fits: hypotension **with bradycardia** — when you want some heart-rate/output support along with the pressure. Effect can diminish with repeat dosing (tachyphylaxis).

### Phenylephrine
- Mechanism: nearly pure alpha-1 agonist.
- Effect: raises blood pressure via vasoconstriction (↑ SVR); commonly causes a **reflex bradycardia**.
- When it fits: hypotension **with tachycardia**, or when you specifically want to avoid raising heart rate (e.g., to protect a rate-sensitive heart).

## When-which, in one line
- Hypotensive + **slow** → ephedrine territory. Hypotensive + **fast** → phenylephrine territory. The provider orders; the orientee should understand the logic.

## What you want to see vs what you watch for
- Want to see: blood pressure restored toward the patient's baseline/goal while the underlying cause is addressed.
- Watch for: overshoot hypertension, reflex bradycardia (phenylephrine), tachyphylaxis (ephedrine), dysrhythmia, and IV-site problems (vasoconstrictors can injure tissue on extravasation).

## Onset / duration (per pharmacy monograph)
- Defer figures to monograph. The clinically useful facts here are directional (which agent moves heart rate which way), not numeric.

## Dose
- Per order — bolus and/or infusion set by the provider. This reference states no doses, bolus increments, infusion rates, or concentrations.

## Monitoring in PACU
- Reassess blood pressure frequently (short interval per order/facility) and after each dose or rate change; trend it, don't treat a single reading.
- Specific assessment: HR/rhythm (anticipate reflex bradycardia with phenylephrine), mental status/perfusion, IV-site integrity, urine output trend, and evidence of the underlying cause (bleeding, block level, fluid status).
- Reassess after the ordered intervention: did pressure respond, and is the cause being treated?

## Red flags that require escalation
- Hypotension not responding to the ordered agent, or signs of ongoing bleeding / hypovolemia → call {anesthesia provider by role} / rapid response per facility.
- Overshoot hypertension, symptomatic bradycardia, or new dysrhythmia → call {provider by role}; monitor rhythm.
- Extravasation of a vasoconstrictor (site pain, blanching) → stop, follow facility extravasation protocol, notify {provider by role}.
- Hypotension with rash/wheeze/airway swelling (possible anaphylaxis) → call {provider by role} immediately; anaphylaxis support per facility.

## Common orientee mistakes
- Chasing the blood-pressure number with a pressor without hunting the reversible cause.
- Not anticipating the reflex bradycardia that follows phenylephrine.
- Mixing up which agent raises vs holds heart rate.
- Treating a single low reading rather than trending and correlating with perfusion.

## Teaching pearls
- The pressor is a bridge; the cause is the treatment.
- Slow-and-low → ephedrine; fast-and-low → phenylephrine (and expect the heart rate to dip).

## Sources
- *Drain's PeriAnesthesia Nursing*, cardiovascular / pharmacology chapters
- Hospital pharmacy monograph (facility-specific; confirm current version)
```

## Must / Must not

**Must:**
- Lead with cause-first hypotension management.
- Map each agent to mechanism + heart-rate direction + the "when-which" context.
- Include monitoring (trend BP, anticipate reflex bradycardia) and IV-site/extravasation awareness.

**Must not:**
- No bolus math, infusion rates, dose increments, or concentrations.
- No "just give a pressor" framing that skips cause-finding.
- No nurse-initiated dosing decisions (provider-scope).
- No invented onset/duration numbers or facility protocol.

## Quality signals

- Orientee finds/reports the cause, understands why the ordered pressor fits the heart-rate context, and anticipates reflex bradycardia + IV-site risk.

## Verification

- [ ] Cause-first mindset stated before any pressor.
- [ ] Ephedrine vs phenylephrine mapped by mechanism + HR direction + when-which.
- [ ] Reflex bradycardia (phenylephrine) + tachyphylaxis (ephedrine) named.
- [ ] Monitoring block has reassess interval + BP-trending + rhythm + IV-site assessment.
- [ ] Red flags link trigger → escalation role.
- [ ] No bolus/infusion/concentration numbers anywhere.

## False-Positive Prevention

Do **not** fabricate or invent:

- **No bolus doses, infusion rates, dose increments, or concentrations.** Per order only.
- **No invented blood-pressure/heart-rate target numbers** — refer to the patient's baseline/goal "per order."
- **No invented onset/duration figures** — defer to monograph; keep the directional facts.
- **No invented incidence statistics** — qualitative only.
- **No invented facility protocols, extravasation steps, or pager paths.**
- **No fabricated chapter/monograph citations.** Mark `{{confirm}}`.
- **No scope creep** — pressor selection and dosing are provider-scope.

## Worked Example

<details>
<summary>Example: hypotension with a slow vs fast heart rate (click to expand)</summary>

```markdown
## Reading the heart-rate context

Two PACU patients are hypotensive. One is also bradycardic; the other is tachycardic. An orientee wants to know why the provider ordered different pressors.

The logic follows the heart rate. For the slow-and-low patient, ephedrine fits — it tends to lift both pressure and heart rate/output. For the fast-and-low patient, phenylephrine fits — it raises pressure by vasoconstriction and, notably, usually drops the heart rate by reflex, which is fine (or even desirable) when the rate is already fast. In both cases, the pressor is a bridge: keep hunting the cause — is one bleeding, is one still sympathectomized from a neuraxial block? Trend the pressure, watch the rhythm (especially the reflex dip after phenylephrine), and reassess whether the cause is being treated.
```

Notes: cause-first, correct agent-to-context mapping, reflex-bradycardia anticipation, no doses, escalation by role.
</details>

## Self-check

- [ ] Cause-first mindset taught.
- [ ] Ephedrine vs phenylephrine mapped correctly (mechanism + HR + when-which).
- [ ] Reflex bradycardia + tachyphylaxis named.
- [ ] Monitoring block has interval + BP-trend + rhythm + IV-site.
- [ ] Red flags have escalation role.
- [ ] Safety reminder at top.
- [ ] No invented doses/rates/targets/onset/duration/facility specifics.
- [ ] Verification + False-Positive Prevention passed.
