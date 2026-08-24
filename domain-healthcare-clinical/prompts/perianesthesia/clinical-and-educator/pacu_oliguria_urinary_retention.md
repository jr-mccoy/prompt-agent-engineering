---
title: PACU Low Urine Output — Oliguria vs Urinary Retention
category: pacu/complications
task_type: LEARN
audience: PACU orientee (any phase) or preceptor for huddle
updated: "2026-07-06"
tags:
  - pacu
  - oliguria
  - urinary-retention
  - renal
  - fluid-status
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
  - pacu_post_op_hypertension.md
  - pacu_emergence_agitation_deescalation.md
  - pacu_geriatric_considerations.md
  - pacu_red_flag_card.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — renal/genitourinary and fluid chapters
  - ASPAN Standards of Perianesthesia Nursing Practice
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice — renal/fluid module
---

# Low Urine Output: Oliguria vs Urinary Retention — PACU Deep Dive

> Safety reminder: "Low urine output" and "an empty-feeling bag" are not the same problem. A bladder scan usually separates true oliguria (low production) from urinary retention (production fine, can't void). Catheterization, fluids, and pharmacology are per provider order/facility. This prompt states no volume thresholds. See `../SAFETY_PREAMBLE.md`.

## Objective

Produce a structured deep dive that teaches the orientee to separate **true oliguria** (a production/perfusion problem — often pre-renal) from **post-op urinary retention** (an outflow/voiding problem), using a bladder-scan-first approach, and to escalate appropriately.

## Inputs

- **Common contexts in your unit:** {{neuraxial anesthesia, pelvic/hernia/urologic surgery, opioids/anticholinergics, older adults, long cases, blood loss}}
- **Source chapters:** {{Drain's renal/GU and fluid chapters, ASPAN Core Curriculum}}

## Audience

- Orientee at any phase — low urine output is a frequent PACU question.
- Preceptor building a renal/fluid huddle.

## Output requirements

```markdown
# Low Urine Output: Oliguria vs Urinary Retention — PACU Deep Dive

> Safety reminder: Bladder-scan first to separate retention from oliguria; escalate. Catheterization/fluids/pharmacology per order.

## Why it matters
[One paragraph — the two problems look similar (low output into the bag or "hasn't voided") but have opposite management: retention needs bladder emptying; true oliguria needs a perfusion/volume workup. Getting it wrong wastes time or misses hypovolemia/bleeding.]

## The two problems
| | Urinary retention | True oliguria |
|---|---|---|
| Problem | Bladder full, can't void | Kidneys producing little urine |
| Bladder scan | High volume | Low volume |
| Common drivers | Neuraxial, opioids, anticholinergics, pelvic/hernia surgery, older men/BPH | Hypovolemia/bleeding (pre-renal), hypotension, renal, obstruction of a catheter |
| First move | Empty the bladder per order | Assess volume/perfusion, check catheter patency |

## Bladder-scan-first framing
- For low output or "hasn't voided," a bladder scan per facility is the fast discriminator.
- If a catheter is in place with low output: check the catheter is patent and not kinked/clamped before assuming oliguria.

## Reversible-cause hunt (true oliguria)
- Volume status / bleeding (pre-renal is the most common post-op cause), hypotension/perfusion, catheter obstruction (post-renal at the catheter), recent nephrotoxins.

## Early cues
- Retention: suprapubic fullness/discomfort, restlessness/agitation, hypertension, urge without voiding, high bladder-scan volume.
- Oliguria: low output with an empty bladder scan, signs of hypovolemia (tachycardia, hypotension trend, bleeding, pallor).

## Immediate management
1. Bladder scan per facility (or check catheter patency if catheterized) → classify retention vs oliguria.
2. Retention: relieve per order (straight cath / indwelling / voiding measures) → reassess comfort/output.
3. Oliguria: assess volume/perfusion and bleeding; notify {provider by role} for fluid/workup per order → reassess after intervention.
4. Address contributing drivers within scope (position, privacy, pain, warmth for voiding).

## Escalation
- Call {provider by role} for confirmed low production (true oliguria), a bleeding/hypovolemia concern, or retention not relieved by ordered measures.
- Escalate promptly if oliguria accompanies hypotension/bleeding (possible hemorrhage/shock).

## Pharm / equipment likely used
- Bladder scanner, catheter/straight-cath supplies (per order), IV fluids (per order).
- No specific fluid volumes or drug doses here — per order.

## After it resolves
- Continued output monitoring and trend; document classification and response → interval per facility.
- Charting: scan result, classification, intervention, output response, escalation.
- Handoff: retention vs oliguria, action taken, current output trend, catheter status.

## Teaching pearls
- Scan before you assume — a distended bladder is retention, an empty one with low output is oliguria.
- Post-op oliguria is most often pre-renal (volume/bleeding) — look there first.
- Check the catheter before you diagnose the kidney.

## Common orientee mistakes
- Assuming "low output = needs fluids" without a bladder scan (misses retention).
- Missing a kinked/clamped catheter and working up "oliguria."

## Sources
- ...
```

## Must / Must not

**Must:**
- Separate retention from true oliguria with a bladder-scan-first approach.
- Frame post-op oliguria as most often pre-renal (volume/bleeding).
- Include the check-the-catheter step.
- Catheterization/fluids/pharmacology per order.

**Must not:**
- No specific urine-output thresholds (mL/kg/hr) or fluid volumes — "per provider/facility."
- No drug doses — "per order."
- No scope creep; catheterization per order/facility competency.
- No facility protocol/pager invented.

## Quality signals

- Orientee scans (or checks catheter) before deciding fluids vs catheterization.
- Orientee links oliguria to possible bleeding/hypovolemia.

## Verification

- [ ] Retention vs oliguria clearly separated.
- [ ] Bladder-scan-first (or catheter-patency) framing present.
- [ ] Pre-renal/volume emphasis for oliguria.
- [ ] Management steps have reassess intervals; escalation by role.
- [ ] No urine-output thresholds, fluid volumes, or doses stated.

## False-Positive Prevention

Do **not** fabricate or invent:

- **No specific urine-output thresholds (e.g., mL/kg/hr) or fluid-bolus volumes.** Per provider/facility.
- **No drug doses.** Per order.
- **No invented incidence statistics.** Describe qualitatively.
- **No invented facility protocols, catheter policies, or pager paths.**
- **No fabricated chapter citations.** Mark `{{confirm}}`.
- **No scope creep.**

## Worked Example

<details>
<summary>Example: bladder-scan-first on a patient who "hasn't voided" (click to expand)</summary>

```markdown
## Immediate management (worked)

A patient after a hernia repair under spinal anesthesia hasn't voided and is increasingly restless with suprapubic discomfort and an elevated BP.

- Don't reach for fluids or assume oliguria. Bladder scan per facility → high volume: this is urinary retention (common after neuraxial/pelvic surgery).
- Relieve per order (voiding measures or catheterization per facility competency); reassess comfort and output. The restlessness and hypertension often settle once the bladder is emptied.
- If instead the scan were empty with low output, you'd pivot to a volume/perfusion assessment (look for bleeding/hypovolemia) and escalate to the provider by role.
```

Notes: scan-first discriminated retention from oliguria; correct opposite management; escalation by role; no thresholds/volumes/doses invented.
</details>

## Self-check

- [ ] Retention vs oliguria separated.
- [ ] Bladder-scan-first / catheter-patency framing.
- [ ] Pre-renal emphasis for oliguria.
- [ ] Reassess intervals + escalation by role.
- [ ] No output thresholds/fluid volumes/doses invented.
- [ ] Safety reminder at top.
- [ ] Verification + False-Positive Prevention passed.
