---
title: PACU Emergence Agitation / Delirium De-escalation
category: pacu/complications
task_type: LEARN
audience: PACU orientee (any phase) or preceptor for bedside coaching
updated: "2026-07-06"
tags:
  - pacu
  - emergence-agitation
  - emergence-delirium
  - de-escalation
  - safety
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - pacu_complication_deep_dive.md
  - pacu_pediatric_considerations.md
  - pacu_geriatric_considerations.md
  - pacu_delayed_emergence.md
  - pacu_red_flag_card.md
  - pacu_simulation_scenario_builder.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — emergence and neurologic chapters
  - ASPAN Standards of Perianesthesia Nursing Practice
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice — neurologic module
  - PAED (Pediatric Anesthesia Emergence Delirium) scale — Sikich & Lerman 2004
  - CAM / CAM-ICU (Confusion Assessment Method) — delirium screening
---

# PACU Emergence Agitation / Delirium De-escalation

> Safety reminder: Emergence agitation is a **diagnosis of exclusion**. A hypoxic, hypercarbic, hypoglycemic, or pain-driven patient can look identical to emergence agitation — and treating agitation while missing a reversible physiologic cause is dangerous. Rule out physiology first. All medications are per provider order; this prompt never states specific doses. See `../SAFETY_PREAMBLE.md`.

## Objective

Produce a **structured de-escalation script** for the agitated or acutely confused post-op patient, usable at the bedside or as a coaching artifact. Its central teaching move is *rule out reversible physiologic causes before labeling and managing "agitation."* Covers adult emergence agitation, pediatric emergence delirium (PAED), and the under-recognized **hypoactive** delirium presentation.

## When to use

- An orientee needs a bedside-ready sequence for the thrashing, disoriented, or inconsolable post-op patient.
- Cross-referenced from `pacu_pediatric_considerations.md` and `pacu_geriatric_considerations.md` as the de-escalation script for their populations.
- Pre-read before an emergence-agitation simulation.

## When not to use

- For failure-to-wake / prolonged unresponsiveness → use `pacu_delayed_emergence.md`.
- For a general complication template → use `pacu_complication_deep_dive.md`.

## Inputs

- **Population focus:** {{adult | pediatric (PAED) | older adult (delirium) | mixed}}
- **Presentation:** {{hyperactive (thrashing, pulling lines) | hypoactive (quiet, withdrawn, not tracking) | mixed/fluctuating}}
- **Source chapters available:** {{Drain's, ASPAN Core Curriculum, facility protocols}}

## Output requirements

```markdown
# Emergence Agitation / Delirium — De-escalation Script ({population})

> Safety reminder: Rule out reversible physiologic causes before treating "agitation." All medications per order.

## Step 0 — Safety first (patient + staff)
- Protect the airway and any lines/drains/surgical site the patient could dislodge.
- Do **not** restrain reflexively; call for help early so hands-on protection is safe.
- Lower the bed, pad rails per facility, clear hazards.

## Step 1 — Rule out reversible physiology FIRST (the whole point)
Work this list before you call it emergence agitation:
| Reversible cause | Fast bedside check |
|---|---|
| Hypoxia | SpO₂ + work of breathing + color; deliver O₂ per order |
| Hypercarbia / hypoventilation | RR pattern, depth, residual sedation |
| Pain | Behavioral/appropriate pain scale; guarding, grimace |
| Full bladder | Bladder scan per facility; palpate; recent catheter removal |
| Hypoglycemia | Point-of-care glucose per facility |
| Residual neuromuscular blockade | Weak, uncoordinated movement; head-lift if able |
| Hypotension / cerebral hypoperfusion | BP trend, pallor |
| Anxiety / disorientation | Unfamiliar environment, hearing/vision aids removed |

## Step 2 — Environmental de-escalation (do before pharmacology)
- Reduce stimulation: dim lights, lower voices, one voice at a time.
- Orient calmly and repeatedly: name, place, "your surgery is over, you're safe."
- Restore sensory aids (glasses, hearing aids) as soon as feasible.
- Pediatric: parental presence at bedside (per facility) usually helps; do not over-stimulate.
- Older adult: familiar face, unhurried reorientation, avoid tethering where safe.

## Step 3 — Assess severity / trajectory
- Pediatric: PAED scale (≥ 10 of 20 suggests emergence delirium — Sikich & Lerman).
- Older adult: CAM / CAM-ICU framing for delirium; note hyperactive vs hypoactive.
- Trending worse despite Steps 1–2, or endangering airway/lines → escalate.

## Step 4 — Escalation (by role)
- Call {anesthesia provider by role} when: agitation endangers airway/lines, or a reversible cause is suspected but you cannot correct it.
- Call {anesthesia provider by role} for: pharmacologic management orders — agent and dose are **per order**, never nurse-initiated here.
- Rapid response / code criteria: per facility (e.g., airway compromise, sustained desaturation).

## Step 5 — Pharmacologic management (per order only)
- Any sedative/analgesic/antipsychotic is **per provider order**. This script does not select or dose agents.
- After any medication: heightened monitoring for over-sedation and respiratory depression → reassess per facility interval.

## The hypoactive trap
- Quiet, withdrawn, "easy" patients can be delirious too. Hypoactive delirium is under-recognized and carries worse outcomes. A patient who is *too* settled and not tracking is a screen-positive, not a convenience.

## After it resolves
- Reassessment schedule: mental status + VS per facility interval.
- Charting: presentation, reversible causes checked, interventions, response, escalation.
- Handoff: flag the episode, cause found (or not), and current mental-status baseline for the receiving unit.

## Common orientee mistakes
- ...

## Sources
- ...
```

## Must / Must not

**Must:**
- Put reversible-physiology rule-out (Step 1) **before** de-escalation and pharmacology.
- Include the hypoactive-delirium warning (under-recognized).
- Name PAED for pediatrics and CAM/CAM-ICU framing for older adults.
- Keep all medication management "per order"; escalate for pharmacology.
- Include patient-and-staff safety (Step 0) without reflexive restraint.

**Must not:**
- No specific sedative/antipsychotic doses or agent selection — always "per order."
- No invented PAED/CAM cutoffs beyond commonly cited values (PAED ≥ 10; cite Sikich & Lerman).
- No facility-specific restraint policy, pager numbers, or medication protocols.
- No scope creep — the nurse assesses, de-escalates, protects, and escalates; providers order pharmacology.
- No implication that agitation should be chemically managed before physiology is ruled out.

## Quality signals

- Orientee rules out hypoxia / pain / bladder / glucose before ever saying "emergence agitation."
- Orientee can name the hypoactive presentation as a red flag, not a relief.
- Environmental de-escalation is attempted before pharmacology is requested.

## Verification

Before returning, verify:

- [ ] Reversible-physiology rule-out precedes de-escalation and pharmacology.
- [ ] Rule-out table includes hypoxia, hypercarbia, pain, bladder, glucose, residual NMB.
- [ ] Environmental de-escalation is listed before pharmacologic management.
- [ ] Hypoactive-delirium warning present.
- [ ] PAED (peds) and CAM/CAM-ICU (older adult) named.
- [ ] All medication management is "per order"; escalation names a role.
- [ ] Safety step avoids reflexive restraint and calls for help early.

## False-Positive Prevention

Do **not** fabricate or invent:

- **No invented doses or agent selection.** Pharmacologic management is entirely "per order."
- **No invented scale cutoffs** beyond commonly cited PAED ≥ 10 (cite Sikich & Lerman 2004); do not invent CAM thresholds.
- **No invented facility restraint policy, pager paths, or medication protocols.**
- **No invented incidence statistics.** Describe qualitatively ("common in children age ~2–7 after volatile anesthesia").
- **No fabricated chapter citations.** Mark `{{confirm chapter}}` when unknown.
- **No scope creep** — no nurse-initiated sedation, no provider-scope airway actions.

## Worked Example

<details>
<summary>Example: hyperactive adult emergence agitation, Step 1 rule-out narrative (click to expand)</summary>

```markdown
## Step 1 — Rule out reversible physiology FIRST

68-year-old, post-op, thrashing and pulling at the IV 10 minutes after PACU arrival. Before labeling emergence agitation:

- SpO₂ 88% on room air, shallow breathing → apply O₂ per order, reposition airway, reassess in 1 min. (This alone may be the cause.)
- Bladder scan per facility — 600 mL retained after a long case with catheter removed in OR.
- Point-of-care glucose per facility — within expected range.
- Pain: grimacing on movement, guarding the incision — behavioral pain score elevated.

Two correctable drivers found (hypoxia + distended bladder + pain) — treat those per order and reassess before any sedative is considered. Escalate to the anesthesia provider by role for O₂/pain orders and possible bladder management.
```

Notes: physiology ruled out first; two reversible causes surfaced that would have been missed by treating "agitation"; no doses invented; escalation by role.
</details>

## Self-check

- [ ] Reversible physiology ruled out before de-escalation/pharmacology.
- [ ] Environmental de-escalation before medication.
- [ ] Hypoactive-delirium warning included.
- [ ] PAED / CAM framing named.
- [ ] All pharmacology "per order"; escalation by role.
- [ ] Safety step present, no reflexive restraint.
- [ ] No invented doses, cutoffs, or facility protocols.
- [ ] Safety reminder at top.
- [ ] Verification + False-Positive Prevention passed.
