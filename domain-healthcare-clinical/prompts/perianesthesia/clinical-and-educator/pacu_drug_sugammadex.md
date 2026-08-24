---
title: PACU Drug Monograph — Sugammadex (Steroidal NMB Reversal)
category: pacu/pharmacology
task_type: LEARN
audience: PACU orientee (any phase) or preceptor for huddle
updated: "2026-07-07"
tags:
  - pacu
  - pharmacology
  - sugammadex
  - neuromuscular-blockade
  - reversal
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - pacu_drug_neostigmine_glycopyrrolate.md
  - pacu_delayed_emergence.md
  - pacu_medication_profile.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — pharmacology and neuromuscular chapters
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Hospital pharmacy monograph (facility-specific; confirm current version)
---

# Sugammadex — PACU Drug Monograph

> Safety reminder: Sugammadex reverses **steroidal** non-depolarizing blockers (rocuronium, vecuronium) — it does **not** reverse benzylisoquinolinium agents (atracurium, cisatracurium). Reversal is not a guarantee of full, permanent recovery — recurarization, hypersensitivity/anaphylaxis, and bradycardia are recognized risks, and it interacts with hormonal contraception. All dosing is per provider order; this monograph states no doses. See `../SAFETY_PREAMBLE.md`.

## Objective

Produce a PACU-focused reference on sugammadex that teaches which blockers it reverses, residual-weakness/recurarization surveillance, and the counseling and safety cautions (contraception interaction, anaphylaxis, bradycardia) — with all pharmacology provider-ordered.

## Inputs

- **Neuromuscular blocker(s) used in your ORs:** {{rocuronium, vecuronium — steroidal; atracurium/cisatracurium — not sugammadex-reversible}}
- **Facility protocol for reversal + monitoring:** {{order set / neuromuscular monitoring practice}}
- **Populations of note:** {{renal impairment, patients on hormonal contraception, prior reaction history}}

## Audience

- Orientee at any phase — reversal pharmacology tied to residual-weakness recognition.
- Preceptor building a neuromuscular-recovery huddle.

## Output requirements

```markdown
# Sugammadex — PACU Profile

> Safety reminder: Reverses steroidal NMBs only. Watch for recurarization, anaphylaxis, bradycardia. All dosing per order.

## Class & mechanism
- Class: selective relaxant binding agent (a modified gamma-cyclodextrin).
- How it works: encapsulates steroidal non-depolarizing neuromuscular blocking agents (rocuronium, and to a lesser degree vecuronium) into an inactive complex, rapidly reversing neuromuscular blockade. It does not bind benzylisoquinolinium agents (atracurium, cisatracurium), so it does not reverse them.

## When it's used in PACU
- Reversal of rocuronium/vecuronium-induced neuromuscular blockade, given per order and per provider judgment (often guided by neuromuscular monitoring / train-of-four). PACU role: recognize residual weakness, monitor recovery, escalate.

## What you want to see vs what you watch for
- Want to see: sustained return of strength — adequate sustained head-lift/grip, effective ventilation, protected airway.
- Watch for: residual or recurring weakness (recurarization), hypersensitivity/anaphylaxis, and bradycardia (occasionally severe).

## Onset / duration (per pharmacy monograph)
- Rapid onset; defer figures to monograph. Even after reversal, recovery adequacy is a clinical + neuromuscular-monitoring judgment, not an assumption.

## Dose
- Per order (typically depth-of-block dependent). This monograph states no doses, mg/kg, or concentrations.

## Recurarization / residual weakness (key surveillance)
- Reversal does not guarantee permanent, complete recovery — weakness can persist or recur if dosing was insufficient for the depth of block. Assess sustained strength, not a single twitch of movement.
- Specific bedside signs of residual weakness: inability to sustain a 5-second head-lift, weak grip, difficulty swallowing/speaking, shallow breathing, "floppy"/uncoordinated movement, airway compromise.

## Safety cautions / interactions in PACU
- Hormonal contraception: sugammadex can reduce the effectiveness of hormonal contraceptives — patients should be counseled per facility/provider to use an additional non-hormonal method for the interval stated in the monograph.
- Hypersensitivity / anaphylaxis: recognized risk — watch for rash, wheeze, facial/airway swelling, hypotension.
- Bradycardia: reported, sometimes marked — monitor rhythm.
- Renal impairment: caution per provider (renal clearance).
- Not applicable to atracurium/cisatracurium blockade — reversal there is a different pathway.

## Monitoring in PACU
- Reassess strength (sustained head-lift/grip), respiratory adequacy, airway protection, and HR/rhythm on the facility interval, and again after any change.
- Specific assessment: sustained head-lift + grip + swallow/speech + breathing depth; allergic-reaction screen; rhythm strip if bradycardic per order.
- Continue surveillance for recurarization per facility interval — recovery is trended, not declared once.

## Red flags that require escalation
- Returning/worsening weakness, poor airway protection, or ineffective ventilation → call {anesthesia provider by role}; support ventilation (BVM ready).
- Signs of anaphylaxis (wheeze, facial/airway swelling, hypotension, rash) → call {provider by role} immediately; prepare airway/anaphylaxis support per facility.
- Symptomatic bradycardia → call {provider by role}; monitor rhythm.

## Common orientee mistakes
- Assuming "reversed" means "fully and permanently recovered" — recurarization is possible.
- Not recognizing that sugammadex does nothing for atracurium/cisatracurium blockade.
- Forgetting the hormonal-contraception counseling point.
- Reading one twitch of movement as adequate strength instead of testing sustained head-lift/grip.

## Teaching pearls
- Steroidal only — roc/vec yes, atracurium/cisatracurium no.
- Trend strength; don't declare recovery from a single sign.

## Sources
- *Drain's PeriAnesthesia Nursing*, pharmacology / neuromuscular chapters
- Hospital pharmacy monograph (facility-specific; confirm current version)
```

## Must / Must not

**Must:**
- State clearly it reverses steroidal (roc/vec) NMBs only — not atracurium/cisatracurium.
- Teach recurarization / residual-weakness surveillance with sustained-strength signs.
- Name the contraception interaction, anaphylaxis, and bradycardia cautions.

**Must not:**
- No sugammadex doses, mg/kg, or concentrations.
- No "fully reversed / completely safe" language.
- No nurse-initiated dosing decisions (provider-scope).
- No invented onset/duration numbers, contraception interval numbers, or facility protocol.

## Quality signals

- Orientee tests sustained strength, keeps watching for recurarization, and knows which blockers the agent does and doesn't reverse.

## Verification

- [ ] Steroidal-only scope stated (roc/vec yes; atracurium/cisatracurium no).
- [ ] Recurarization/residual-weakness surveillance with sustained-strength signs present.
- [ ] Contraception interaction + anaphylaxis + bradycardia cautions named.
- [ ] Monitoring block has reassess interval + specific strength/allergy/rhythm assessment.
- [ ] Red flags link trigger → escalation role.
- [ ] No doses/mg-kg/concentrations anywhere.

## False-Positive Prevention

Do **not** fabricate or invent:

- **No sugammadex doses, mg/kg, or concentrations.** Per order only.
- **No invented onset/duration figures** or **contraception-interval numbers** — defer to monograph, keep the counseling point qualitatively.
- **No invented incidence statistics** for anaphylaxis, bradycardia, or recurarization — describe qualitatively.
- **No invented renal thresholds.**
- **No invented facility protocols or pager paths.**
- **No fabricated chapter/monograph citations.** Mark `{{confirm}}`.
- **No scope creep** — reversal dosing is provider-scope.

## Worked Example

<details>
<summary>Example: residual-weakness surveillance after reversal (click to expand)</summary>

```markdown
## Recurarization / residual weakness

Your patient was reversed with sugammadex after rocuronium and moved to PACU moving all limbs. That is not the same as recovered.

Test sustained strength, not a flicker of movement: can she hold a 5-second head-lift, squeeze firmly, swallow and speak clearly, and breathe with adequate depth? Weakness can persist or recur if the reversal dose was light for the depth of block. Keep trending strength and respiratory adequacy on the facility interval; if strength fades or breathing weakens, support ventilation and call the provider — and remember this reversal path does nothing for an atracurium/cisatracurium block.
```

Notes: sustained-strength testing, recurarization surveillance, steroidal-only scope, no doses, escalation by role.
</details>

## Self-check

- [ ] Steroidal-only scope stated.
- [ ] Recurarization surveillance + sustained-strength signs taught.
- [ ] Contraception/anaphylaxis/bradycardia cautions named.
- [ ] Monitoring block has interval + specific assessment.
- [ ] Red flags have escalation role.
- [ ] Safety reminder at top.
- [ ] No invented doses/onset/duration/interaction numbers/facility specifics.
- [ ] Verification + False-Positive Prevention passed.
