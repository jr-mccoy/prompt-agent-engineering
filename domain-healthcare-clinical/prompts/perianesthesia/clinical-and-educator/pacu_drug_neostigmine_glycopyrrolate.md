---
title: PACU Drug Monograph — Neostigmine + Glycopyrrolate (Cholinesterase-Inhibitor Reversal)
category: pacu/pharmacology
task_type: LEARN
audience: PACU orientee (any phase) or preceptor for huddle
updated: "2026-07-07"
tags:
  - pacu
  - pharmacology
  - neostigmine
  - glycopyrrolate
  - neuromuscular-reversal
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - pacu_drug_sugammadex.md
  - pacu_delayed_emergence.md
  - pacu_medication_profile.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — pharmacology and neuromuscular chapters
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Hospital pharmacy monograph (facility-specific; confirm current version)
---

# Neostigmine + Glycopyrrolate — PACU Drug Monograph

> Safety reminder: This is a **paired** reversal — neostigmine reverses non-depolarizing blockade but produces muscarinic effects (bradycardia, secretions), so an antimuscarinic (glycopyrrolate) is co-administered to blunt them. It works only from a block that has already partly recovered, and recurarization remains possible. All dosing is per provider order; this monograph states no doses. See `../SAFETY_PREAMBLE.md`.

## Objective

Produce a PACU-focused reference on the neostigmine/glycopyrrolate pair that teaches the reason for the pairing, the muscarinic vs antimuscarinic effects to watch, and recurarization surveillance — with all pharmacology provider-ordered.

## Inputs

- **Reversal agents used in your facility:** {{neostigmine + glycopyrrolate (or atropine) pairing}}
- **Facility protocol for reversal + neuromuscular monitoring:** {{order set / train-of-four practice}}
- **Populations of note:** {{asthma/reactive airway, bradycardia-prone, PONV-prone}}

## Audience

- Orientee at any phase — reversal pharmacology + heart-rate/secretion effects.
- Preceptor building a neuromuscular-recovery or rhythm-awareness huddle.

## Output requirements

```markdown
# Neostigmine + Glycopyrrolate — PACU Profile

> Safety reminder: Paired reversal. Neostigmine → bradycardia/secretions; glycopyrrolate blunts them. Watch HR both directions + recurarization. All dosing per order.

## Class & mechanism
- Neostigmine — class: acetylcholinesterase inhibitor. How it works: inhibits acetylcholinesterase, raising acetylcholine at the neuromuscular junction so it out-competes the non-depolarizing blocker → reversal. Rising acetylcholine also hits muscarinic receptors (heart, glands, gut, airway) → bradycardia, secretions, bronchoconstriction, salivation, GI stimulation, miosis.
- Glycopyrrolate — class: antimuscarinic (anticholinergic). How it works: blocks muscarinic receptors to counter neostigmine's muscarinic effects (bradycardia, secretions). It does not cross the blood-brain barrier appreciably (less central effect than atropine) and its onset is paired to neostigmine's muscarinic peak.

## Why they're paired
- Neostigmine's therapeutic action (reversal) and its muscarinic side effects are inseparable, so the antimuscarinic is given with it to prevent bradycardia and secretions. Think of them as one reversal event with two counter-balanced drugs.

## When it's used in PACU
- Reversal of non-depolarizing neuromuscular blockade **when adequate twitches / partial recovery are already present** (it cannot reverse a deep block), given per order and per provider judgment. PACU role: recognize residual weakness, monitor recovery + rhythm, escalate.

## What you want to see vs what you watch for
- Want to see: return of sustained strength and effective ventilation without a swing in heart rate.
- Watch for: bradycardia (neostigmine predominating), tachycardia/dry mouth/blurred vision (glycopyrrolate predominating), increased secretions/bronchospasm, PONV, and residual/recurring weakness.

## Onset / duration (per pharmacy monograph)
- Defer figures to monograph. The teaching point is the balance: heart rate can move either way depending on which agent's effect predominates at a given moment.

## Dose
- Per order (weight/depth dependent, provider-set). This monograph states no doses, mg/kg, ratios, or concentrations.

## Recurarization / residual weakness (key surveillance)
- Reversal from an insufficiently-recovered block, or an underdose, can leave or allow the return of weakness. Assess sustained strength (5-second head-lift, firm grip, clear swallow/speech, adequate breathing) — not a single movement.

## Cautions / interactions in PACU
- Reactive airway / asthma: increased secretions and bronchoconstriction from the muscarinic effect can aggravate bronchospasm.
- Bradycardia-prone patients: monitor rhythm closely around administration.
- PONV: the cholinergic GI effect can contribute to nausea/vomiting.
- Cannot reverse a deep block — that is a provider/timing issue, not a nursing fix.

## Monitoring in PACU
- Reassess strength (sustained head-lift/grip), respiratory adequacy, airway protection, HR/rhythm, and secretions on the facility interval and after any change.
- Specific assessment: sustained head-lift + grip + swallow/speech + breathing depth; heart-rate trend in both directions; secretion burden / wheeze; nausea.
- Continue recurarization surveillance per facility interval — recovery is trended, not declared once.

## Red flags that require escalation
- Returning/worsening weakness, poor airway protection, or ineffective ventilation → call {anesthesia provider by role}; support ventilation (BVM ready).
- Symptomatic bradycardia or new dysrhythmia → call {provider by role}; monitor rhythm.
- Worsening bronchospasm / secretion-driven distress → call {provider by role}.

## Common orientee mistakes
- Expecting the fast, clean, total reversal of sugammadex — this pairing is slower, partial-recovery-dependent, and can leave residual weakness.
- Mixing up which agent does what to heart rate (neostigmine → slows; glycopyrrolate → speeds/dries).
- Not anticipating secretions/bronchospasm in a reactive-airway patient.
- Reading one twitch of movement as adequate strength.

## Teaching pearls
- One reversal, two balanced drugs — heart rate can swing either way; watch both.
- It needs a block that's already coming back; it won't rescue a deep block.

## Sources
- *Drain's PeriAnesthesia Nursing*, pharmacology / neuromuscular chapters
- Hospital pharmacy monograph (facility-specific; confirm current version)
```

## Must / Must not

**Must:**
- Explain the pairing rationale (muscarinic effects countered by antimuscarinic).
- Assign the heart-rate/secretion effects to the correct agent.
- Teach recurarization surveillance and the "needs partial recovery already" limit.

**Must not:**
- No neostigmine/glycopyrrolate doses, mg/kg, ratios, or concentrations.
- No "complete/guaranteed reversal" language.
- No nurse-initiated dosing decisions (provider-scope).
- No invented onset/duration numbers or facility protocol.

## Quality signals

- Orientee watches heart rate in both directions, anticipates secretions in reactive-airway patients, and keeps testing sustained strength for recurarization.

## Verification

- [ ] Pairing rationale (muscarinic ↔ antimuscarinic) explained.
- [ ] Heart-rate/secretion effects correctly assigned to each agent.
- [ ] Recurarization surveillance + "needs partial recovery" limit stated.
- [ ] Monitoring block has reassess interval + specific strength/rhythm/secretion assessment.
- [ ] Red flags link trigger → escalation role.
- [ ] No doses/mg-kg/ratios/concentrations anywhere.

## False-Positive Prevention

Do **not** fabricate or invent:

- **No neostigmine/glycopyrrolate doses, mg/kg, dose ratios, or concentrations.** Per order only.
- **No invented onset/duration figures** — defer to monograph.
- **No invented incidence statistics** for bradycardia, bronchospasm, PONV, or recurarization — describe qualitatively.
- **No invented facility protocols or pager paths.**
- **No fabricated chapter/monograph citations.** Mark `{{confirm}}`.
- **No scope creep** — reversal dosing and depth-of-block judgment are provider-scope.

## Worked Example

<details>
<summary>Example: reading the heart-rate swing around reversal (click to expand)</summary>

```markdown
## Watching heart rate both directions

An orientee expects reversal to look like sugammadex — quick and clean. This patient got neostigmine with glycopyrrolate, and the monitor shows the heart rate dipping, then drifting up.

That swing is the pairing at work: neostigmine's muscarinic effect slows the heart and raises secretions, and glycopyrrolate is there to blunt exactly that — so heart rate can move either way depending on which effect predominates moment to moment. Watch the rhythm in both directions, watch for secretions/wheeze in a reactive-airway patient, and keep testing sustained strength — this reversal is partial-recovery-dependent and weakness can linger. Escalate symptomatic bradycardia or returning weakness to the provider.
```

Notes: pairing rationale, correct agent-to-effect mapping, recurarization surveillance, no doses, escalation by role.
</details>

## Self-check

- [ ] Pairing rationale explained.
- [ ] HR/secretion effects assigned to the right agent.
- [ ] Recurarization surveillance + partial-recovery limit taught.
- [ ] Monitoring block has interval + specific assessment.
- [ ] Red flags have escalation role.
- [ ] Safety reminder at top.
- [ ] No invented doses/ratios/onset/duration/facility specifics.
- [ ] Verification + False-Positive Prevention passed.
