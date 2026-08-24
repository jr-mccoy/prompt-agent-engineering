---
title: PACU Opioid-Induced Respiratory Depression (OIRD) — Recognition & Response
category: pacu/complications
task_type: LEARN
audience: PACU orientee (any phase) or preceptor for huddle
updated: "2026-07-06"
tags:
  - pacu
  - OIRD
  - opioid
  - respiratory-depression
  - sedation-scale
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
  - pacu_delayed_emergence.md
  - pacu_red_flag_card.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — respiratory and pain chapters
  - ASPAN Standards of Perianesthesia Nursing Practice
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice — pain and respiratory modules
  - POSS (Pasero Opioid-Induced Sedation Scale)
---

# Opioid-Induced Respiratory Depression (OIRD) — PACU Deep Dive

> Safety reminder: The single most important teaching point is that **sedation precedes respiratory depression** — monitor the sedation level, not just the respiratory rate and SpO₂. Naloxone and all pharmacology are per provider order; this prompt states no doses. See `../SAFETY_PREAMBLE.md`.

## Objective

Produce a structured deep dive on OIRD that teaches sedation-first monitoring, recognizes why SpO₂ is a late indicator (especially on supplemental O₂), and frames naloxone as a titrate-to-respiration, watch-for-re-sedation intervention that is provider-ordered.

## Inputs

- **Sedation scale used on your unit:** {{POSS | RASS | facility scale}}
- **Higher-risk populations in your unit:** {{OSA/obesity, older adults, renal impairment, opioid-naive, multimodal sedatives}}
- **Source chapters:** {{Drain's pain/respiratory chapters, ASPAN Core Curriculum}}

## Audience

- Orientee at any phase — this is a core PACU safety concept.
- Preceptor building a pain-safety huddle.

## Output requirements

```markdown
# Opioid-Induced Respiratory Depression (OIRD) — PACU Deep Dive

> Safety reminder: Sedation precedes respiratory depression. Monitor sedation level. Naloxone per order.

## Why it matters
[One paragraph — a leading preventable PACU respiratory event; the window to intervene opens at increasing sedation, before SpO₂ falls.]

## Pathophysiology
[2–4 sentences: opioids blunt the central respiratory drive and CO₂ responsiveness → hypoventilation → hypercarbia → hypoxemia. Sedation is the early behavioral marker of central depression.]

## Risk / setup (who and when)
- OSA/obesity, older adults, renal impairment, opioid-naive with higher doses, stacked sedatives (benzodiazepines, other CNS depressants), long-acting or neuraxial opioids.

## Early cues (sedation FIRST — before the SpO₂ alarm)
- Increasing sedation: harder to rouse, drifts off mid-sentence, needs stimulation to stay awake.
- Slow or shallow breathing; snoring/obstructed pattern; long pauses.
- **On supplemental O₂, SpO₂ can look "fine" while the patient is hypoventilating and hypercarbic** — trust the sedation level and respiratory pattern.

## Classic signs (later)
- Bradypnea, low tidal volume, desaturation, pinpoint pupils, unresponsiveness.

## Differential — what else looks like this?
| Mimic | How to tell them apart |
|---|---|
| Residual anesthetic / oversedation | Not opioid-specific; pupils/history differ; less response to opioid reversal |
| Residual neuromuscular blockade | Weakness, poor head-lift; breathing effort present but ineffective |
| Hypercarbia from other causes | Context; blood gas if ordered |
| Hypoglycemia / metabolic | POC glucose; other metabolic signs |

## Immediate management
1. Stimulate (verbal, then physical per facility); coach breaths; ensure airway open (reposition) → reassess in 1 min.
2. Apply/increase O₂ and support ventilation as needed (bag-valve-mask ready) → reassess continuously.
3. Notify {anesthesia provider by role}; prepare naloxone per order — titrate to adequate respiration, not to full arousal → reassess after administration.
4. Hold further opioid; review recent opioid/sedative timeline for the provider.

## Escalation
- Call {anesthesia provider by role} for rising sedation with hypoventilation, or any apnea.
- Rapid response / code per facility for apnea or unresponsiveness.

## Re-sedation watch (critical)
- Naloxone often wears off before the opioid does — the patient can re-sedate after apparent recovery. Continued heightened monitoring after reversal is mandatory, per facility interval.

## After it resolves
- Extended sedation + respiratory monitoring; re-sedation surveillance → interval per facility/provider.
- Charting: sedation trajectory, interventions, reversal timing/response, escalation.
- Handoff: flag OIRD event, reversal timing, and re-sedation window for receiving unit.

## Teaching pearls
- Sedation is the early sign; the SpO₂ number is the late sign — especially on oxygen.
- After naloxone, keep watching — re-sedation is expected, not surprising.

## Common orientee mistakes
- Reassuring on a "normal" SpO₂ while the patient is deeply sedated on oxygen.
- Assuming one dose of naloxone ends the problem.

## Sources
- ...
```

## Must / Must not

**Must:**
- Teach sedation-first monitoring and the late-SpO₂-on-O₂ caveat.
- Frame naloxone as titrate-to-respiration + re-sedation watch, per order.
- Differentiate from residual NMB, non-opioid oversedation, metabolic causes.

**Must not:**
- No naloxone/opioid doses — "per order."
- No invented sedation-scale cutoffs beyond the named scale's standard structure.
- No scope creep — no nurse-initiated dosing decisions.
- No facility-specific pager/protocol invented.

## Quality signals

- Orientee monitors and escalates on rising sedation, not on the SpO₂ alarm.
- Orientee expects and watches for re-sedation after naloxone.

## Verification

- [ ] Sedation-precedes-respiratory-depression taught explicitly.
- [ ] Late-SpO₂-on-oxygen caveat present.
- [ ] Naloxone framed titrate-to-respiration + re-sedation watch, per order.
- [ ] Differential ≥ 2 mimics.
- [ ] Management steps have reassess intervals; escalation by role.

## False-Positive Prevention

Do **not** fabricate or invent:

- **No naloxone/opioid doses, rates, or concentrations.** Per order only.
- **No invented sedation-scale numeric cutoffs** — reference the named scale (e.g., POSS) structurally.
- **No invented incidence statistics or SpO₂/RR thresholds.** Describe qualitatively.
- **No invented facility protocols or pager paths.**
- **No fabricated chapter citations.** Mark `{{confirm}}`.
- **No scope creep** — dosing/reversal decisions are provider-scope.

## Worked Example

<details>
<summary>Example: "Early cues" for a post-op patient on 2 L nasal cannula (click to expand)</summary>

```markdown
## Early cues (sedation FIRST)

Post-op patient on 2 L nasal cannula, SpO₂ 96%. On your last two checks she's harder to rouse — she answers, then drifts back off, and her breathing is shallow with occasional long pauses and a soft snore.

- Do not be reassured by the 96%. On oxygen, SpO₂ lags; the rising sedation and shallow/pausing breathing are the real signal.
- Stimulate and coach breaths, open the airway with repositioning, apply higher O₂ / have BVM ready, and call the anesthesia provider by role. Prepare naloxone per order; if given, titrate to breathing and keep watching for re-sedation.
```

Notes: sedation-first recognition; SpO₂-on-O₂ caveat applied; naloxone per order with re-sedation watch; escalation by role; no doses invented.
</details>

## Self-check

- [ ] Sedation-first monitoring taught.
- [ ] SpO₂-late-on-oxygen caveat present.
- [ ] Naloxone per order, titrate-to-respiration, re-sedation watch.
- [ ] Differential ≥ 2 mimics.
- [ ] Reassess intervals + escalation by role.
- [ ] No invented doses/cutoffs/facility specifics.
- [ ] Safety reminder at top.
- [ ] Verification + False-Positive Prevention passed.
