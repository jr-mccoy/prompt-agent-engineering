---
title: PACU Post-Operative Hypertension — Recognition & Response
category: pacu/complications
task_type: LEARN
audience: PACU orientee (any phase) or preceptor for huddle
updated: "2026-07-06"
tags:
  - pacu
  - hypertension
  - cardiovascular
  - reversible-causes
  - end-organ
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
  - pacu_dysrhythmia_recognition.md
  - pacu_emergence_agitation_deescalation.md
  - pacu_oliguria_urinary_retention.md
  - pacu_red_flag_card.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — cardiovascular chapters
  - ASPAN Standards of Perianesthesia Nursing Practice
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice — cardiovascular module
---

# Post-Operative Hypertension — PACU Deep Dive

> Safety reminder: Most post-op hypertension is driven by a correctable cause (pain, bladder, hypoxia). Fix the driver before reaching for a "blood pressure number" mindset. Antihypertensives and all pharmacology are per provider order; BP targets are per provider/facility. This prompt states no values. See `../SAFETY_PREAMBLE.md`.

## Objective

Produce a structured deep dive that teaches the reversible-cause-first approach to post-op hypertension, and how to recognize the minority of cases that are a hypertensive emergency (end-organ involvement) requiring urgent escalation.

## Inputs

- **Common drivers in your unit:** {{pain, bladder distension, hypoxia/hypercarbia, agitation/anxiety, withheld home antihypertensives, hypothermia/shivering, fluid overload}}
- **Higher-risk patients:** {{chronic HTN, cardiac/vascular surgery, cerebrovascular history}}
- **Source chapters:** {{Drain's cardiovascular chapters, ASPAN Core Curriculum}}

## Audience

- Orientee at any phase — post-op hypertension is very common.
- Preceptor building a cardiovascular huddle.

## Output requirements

```markdown
# Post-Operative Hypertension — PACU Deep Dive

> Safety reminder: Find and fix the reversible driver first; recognize hypertensive emergency; escalate. Pharmacology and BP targets per provider.

## Why it matters
[One paragraph — very common; usually secondary and correctable, but can strain a fresh surgical site/anastomosis, raise bleeding risk, and — with end-organ signs — constitute a hypertensive emergency.]

## Pathophysiology / drivers
[2–4 sentences: sympathetic activation from pain, bladder distension, hypoxia/hypercarbia, agitation, withheld home antihypertensives, hypothermia/shivering, and fluid shifts raise BP. Baseline chronic hypertension amplifies the response.]

## Reversible-cause hunt (do this FIRST)
| Driver | Fast check / action |
|---|---|
| Pain | Pain assessment; treat per order |
| Full bladder | Bladder scan per facility; recent catheter removal |
| Hypoxia / hypercarbia | SpO₂, RR/pattern; O₂ per order |
| Agitation / anxiety | Reorientation; see emergence-agitation prompt |
| Withheld home antihypertensive | Medication reconciliation; flag to provider |
| Hypothermia / shivering | Temp; active warming per facility |
| Fluid overload | Fluid balance context |

## Urgency vs emergency (the key distinction)
- **Hypertensive urgency:** elevated BP **without** acute end-organ signs → treat drivers, escalate for management per order.
- **Hypertensive emergency:** elevated BP **with** end-organ signs → urgent escalation.
  - Watch for: chest pain, dyspnea/pulmonary edema, neurologic change (headache, vision change, focal deficit, altered mentation), new severe bleeding at the surgical site.

## Immediate management
1. Confirm the reading (correct cuff size/placement; re-cycle) → establish trend.
2. Hunt and treat reversible drivers within scope (pain, bladder, O₂, warmth) → reassess after each.
3. Notify {provider by role} with BP trend, drivers found, and any end-organ signs; give antihypertensive per order if directed → reassess after intervention.
4. For any end-organ sign: escalate urgently (rapid response per facility).

## Escalation
- Call {provider by role} for sustained elevation despite correcting drivers, or a fresh-surgical-site bleeding concern.
- Rapid response / urgent escalation per facility for any end-organ sign (chest pain, neuro change, pulmonary edema).

## Pharm / equipment likely used
- Correctly sized BP cuff / arterial line if present.
- Antihypertensive per order (no dose/target here); analgesia per order.

## After it resolves
- Continued BP monitoring and trend; confirm driver addressed → interval per facility.
- Charting: BP trend, drivers found/treated, meds per order, response, escalation.
- Handoff: BP trend, driver, home-med status, any end-organ concern.

## Teaching pearls
- Ask "what's driving this?" (pain, bladder, hypoxia) before "what BP med?"
- Elevated BP + end-organ signs = emergency, not just a high number.
- Confirm the reading before reacting — cuff artifact is common.

## Common orientee mistakes
- Treating the number without hunting the driver (often pain or a full bladder).
- Missing end-organ signs that convert urgency into an emergency.

## Sources
- ...
```

## Must / Must not

**Must:**
- Lead with the reversible-cause hunt (pain, bladder, hypoxia especially).
- Teach urgency vs emergency by end-organ signs.
- Confirm-the-reading step before reacting.
- Antihypertensives and BP targets per provider.

**Must not:**
- No specific BP thresholds or targets — "per provider/facility."
- No antihypertensive doses — "per order."
- No scope creep; no facility protocol/pager invented.

## Quality signals

- Orientee hunts the driver before requesting a BP med.
- Orientee recognizes end-organ signs and escalates urgently.

## Verification

- [ ] Reversible-cause hunt leads management.
- [ ] Urgency vs emergency distinguished by end-organ signs.
- [ ] Confirm-the-reading step present.
- [ ] Management steps have reassess intervals; escalation by role.
- [ ] No BP thresholds/targets or drug doses stated.

## False-Positive Prevention

Do **not** fabricate or invent:

- **No specific BP thresholds, targets, or MAP goals.** Per provider/facility.
- **No antihypertensive doses.** Per order.
- **No invented incidence statistics.** Describe qualitatively.
- **No invented facility protocols or pager paths.**
- **No fabricated chapter citations.** Mark `{{confirm}}`.
- **No scope creep.**

## Worked Example

<details>
<summary>Example: reversible-cause-first on new post-op hypertension (click to expand)</summary>

```markdown
## Reversible-cause hunt (worked)

A patient's BP is markedly elevated above their pre-op baseline 30 minutes into recovery. Before asking for a blood-pressure medication:

- Confirm the reading — correct cuff size and placement, re-cycle.
- Hunt drivers: pain score is high and guarding the incision; bladder scan per facility shows retention; SpO₂ is adequate.
- Treat pain per order and address the bladder per facility; reassess BP after each.
- Check end-organ signs: no chest pain, no neuro change, no respiratory distress → this is urgency, not emergency.
- If BP stays elevated after correcting drivers, notify the provider by role for management per order.
```

Notes: reading confirmed; drivers hunted and treated first; urgency-vs-emergency assessed; escalation by role; no BP targets or doses invented.
</details>

## Self-check

- [ ] Reversible-cause hunt leads.
- [ ] Urgency vs emergency by end-organ signs.
- [ ] Confirm-the-reading step present.
- [ ] Reassess intervals + escalation by role.
- [ ] No BP thresholds/targets/doses invented.
- [ ] Safety reminder at top.
- [ ] Verification + False-Positive Prevention passed.
