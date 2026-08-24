---
title: PACU Background-Specific Pathway Adapter
category: pacu/orientation-curriculum
task_type: IMPROVE
audience: PACU educator adapting an existing orientation pathway for a specific orientee background
updated: "2026-05-15"
tags:
  - pacu
  - orientation
  - background-adaptation
  - icu-halo
  - cross-specialty
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - ED-02
  - DS-06
difficulty: advanced
related_prompts:
  - prompts/pacu_orientation_curriculum_designer.md
  - prompts/pacu_orientation_skill_acquisition_timeline.md
  - prompts/pacu_preceptor_orientation_pacing_diagnostic.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
  - Benner, P. — From Novice to Expert
---

# PACU Background-Specific Pathway Adapter

> Safety reminder: An "experienced RN" is not automatically PACU-ready. Adaptations compress only the axes that genuinely transfer; PACU-distinctive content stays on the default curve. Verify against ASPAN scope.

## Objective

Take a **stock PACU orientation pathway** (typically the output of `pacu_orientation_curriculum_designer.md` with a "use a sensible default" framework) and adapt it for a specific orientee background: **where to compress, where to expand, and which biases to flag**.

## Inputs

- **Stock pathway:** {{paste the curriculum-designer output, or describe target length + default theme sequence}}
- **Orientee background:** {{new-grad RN | experienced med-surg → PACU | experienced ICU → PACU | experienced ED → PACU | experienced L&D → PACU | experienced OR → PACU | float-pool returning to PACU | other — describe with prior unit and tenure}}
- **Concrete evidence of relevant prior practice:** {{e.g., 4 yrs medical ICU with vent-titration competency; 2 yrs ED with airway exposure; 5 yrs L&D with neuraxial-block recovery experience — concrete, not "feels confident"}}
- **Constraints:** {{condensed timeline / no peds rotation / etc.}}

## Audience / Scope

- **Primary:** Unit educator or lead preceptor adapting the pathway after orientee assignment is known.
- **Secondary:** `pacu_preceptor_orientation_pacing_diagnostic.md` consumes the adaptation notes to detect bias drift mid-orientation.
- **Scope:** Adjustments to the stock pathway only. Does not regenerate the full pathway.

## Output requirements

```markdown
# Pathway Adaptation — {Background}

> Safety reminder: Adaptation reflects expected transfer of prior practice; verify shift-by-shift, not assumed.

## Stock pathway summary

1-line restatement of the orientation length and stock theme sequence (so the reader sees what's being adapted).

## Where to compress

For each axis that genuinely transfers from prior practice:
- **Axis:** {competency}
- **Evidence of transfer:** {one line tying to the orientee's specific declared prior practice — not "they have ICU experience"}
- **Compression action:** {what to shorten, by how many shifts/weeks}
- **Risk if compression is wrong:** {what failure looks like}

(3–6 items typical.)

## Where to expand

For each axis that is PACU-distinctive and does not transfer:
- **Axis:** {competency}
- **Why it doesn't transfer:** {one line}
- **Expansion action:** {what to lengthen or add}

(3–6 items typical.)

## Biases to flag

Pre-named PACU-specific bias vectors. For each one that applies given the background, flag it:
- **ICU-halo bias** (assuming PACU readiness from ICU titration competence): applies — flag for Week {X} pacing diagnostic.
- **ED-acuity bias** (assuming PACU is "low acuity" because admissions are stable): applies — flag.
- **OR-procedure bias** (orientee defaults to procedural mindset, weak on monitoring continuity).
- **L&D-neuraxial bias** (orientee knows post-spinal recovery from one population, generalizes incorrectly to others).
- **License-pathway bias** (BSN vs ASN signals — do not use, ever; flag here as a "do not" reminder).
- **Tenure bias** (10-year RN ≠ 10-year PACU RN).
- **Confidence-as-competence bias** (orientee speaks fluently, may be With Cues, not Independent).

## Adaptation summary (≤ 5 lines)

A short summary the lead preceptor reads at week kickoff: "Compressed [axes] by [duration]; expanded [axes]; watch [bias] at Week [X]."

## Re-run cadence

This prompt should be re-run if:
- New evidence emerges that prior practice doesn't transfer as expected.
- The orientee transfers from a different prior unit than declared.
- Mid-orientation pacing reveals compression was wrong (`pacu_preceptor_orientation_pacing_diagnostic.md` triggers re-run).

## Sources / reference

- ASPAN *Standards* — scope of PACU practice.
- *Drain's* — PACU-distinctive content chapters (regional block resolution, emergence phenomena, post-anesthesia hemodynamics).
- Benner — cueing-decay framing.
```

## Must / Must not

**Must:**
- Tie every compression to **concrete declared evidence** of prior practice (vent-titration, neuraxial recovery, etc.), not generic "they have ICU experience."
- Name PACU-distinctive axes that don't transfer (emergence phenomena, regional block resolution in mixed populations, family/discharge teaching).
- Flag at least one bias relevant to the background.
- Default compression caps: no axis compresses below the minimum exposure needed for safe practice in PACU (use facility minimums; if unknown, recommend "verify with facility orientation program").
- Reference the pacing diagnostic for bias-detection mid-orientation.

**Must not:**
- Compress emergence, regional block, family communication, or judgment in ambiguity for any background — these stay on default curve.
- Compress based on RN license tenure alone.
- Compress based on certifications without behavior evidence (PALS/TNCC on a resume ≠ PALS-relevant PACU practice).
- Use protected-characteristic information.
- Use license pathway (BSN/ASN/diploma/LPN-bridge) as adaptation signal.
- Conflate "experienced RN" with "PACU-ready."

## Quality signals

- A new-grad adaptation looks fundamentally different from an experienced-ICU adaptation; same with ED, L&D, OR transfers.
- Compression actions are concrete ("shorten airway-foundation block from 6 to 3 shifts") not vague ("less time on basics").
- Bias flags are wired to a specific pacing-diagnostic week.

## Verification

- [ ] Each compression tied to concrete declared evidence.
- [ ] PACU-distinctive axes stay on default curve.
- [ ] At least one bias flagged + pacing week named.
- [ ] No license-pathway adaptation.
- [ ] No tenure-only adaptation.
- [ ] Safety + FPP sections present.

## False-Positive Prevention

- **No invented prior-practice claims** beyond what the user pasted in.
- **No invented certification-to-competency equivalencies** ("PALS implies peds airway competence in PACU").
- **No invented facility orientation program minimum exposures.**
- **No invented Benner stage-to-week mappings.**
- **No invented ASPAN sections.**
- **No protected-characteristic or license-pathway adaptation.**
- **No adaptation based on age, parental status, gender, or other personal characteristics** — even if user mentions them.

## Worked Example

<details>
<summary>Example: 10-week pathway adapted for experienced ICU RN, 4 yrs medical ICU (click to expand)</summary>

```markdown
# Pathway Adaptation — Experienced Medical ICU RN

## Stock pathway summary

10-week default pathway: Wk 0 unit foundation → Wk 1–2 admit-recover task flow → Wk 3 hemodynamics → Wk 4 PONV/pain → Wk 5 regional/emergence → Wk 6 judgment → Wk 7–9 independence ramp → Wk 10 sign-off.

## Where to compress

- **Axis:** Airway titration + ventilation monitoring. **Evidence:** 4 yrs medical ICU with daily vent-titration competency declared. **Compression:** shorten airway-foundation block from 6 shifts to 3. **Risk:** orientee may miss residual neuromuscular blockade pattern that's specific to post-emergence; do not skip this content even if airway monitoring overall compresses.
- **Axis:** Hemodynamic monitoring foundations (titration, MAP-tracking, vasopressor familiarity). **Evidence:** declared vasopressor titration competency. **Compression:** shorten by ~3 shifts. **Risk:** post-spinal hypotension reasoning is distinct — preserve full coverage in Wk 3.
- **Axis:** SBAR escalation cadence and structure. **Evidence:** declared SBAR fluency from ICU. **Compression:** ~2 shifts. **Risk:** PACU escalation partners (CRNA vs floor RN vs surgeon) differ — preserve role-mapping content.
- **Axis:** Documentation pacing. **Evidence:** ICU charting fluency. **Compression:** ~1 shift.

## Where to expand

- **Axis:** Regional / neuraxial block resolution in mixed populations. **Why it doesn't transfer:** medical ICU rarely sees post-anesthesia neuraxial recovery. **Expansion:** preserve full Wk 5 + reinforcing case discussions in Wk 6.
- **Axis:** Emergence and emergence-delirium recognition. **Why it doesn't transfer:** medical ICU sedation-management ≠ post-anesthesia emergence patterns. **Expansion:** preserve full coverage.
- **Axis:** PACU-context family communication + discharge teaching. **Why:** ICU family communication patterns differ. **Expansion:** preserve.
- **Axis:** Judgment in PACU ambiguity (two-bay awareness, fast triage). **Why:** ICU 1:1–1:2 ratios don't build the same pattern. **Expansion:** preserve and emphasize.

## Biases to flag

- **ICU-halo bias** — high risk. Flag at Wk 4 pacing diagnostic. Watch for "looks Independent on airway/hemo, generalize to Independent overall."
- **Tenure bias** — moderate. 4 yrs ICU ≠ 4 yrs of relevant PACU practice on emergence and regional.
- **Confidence-as-competence bias** — moderate. Orientee will speak fluently early; cueing-decay on PACU-distinctive axes is the truer signal.

## Adaptation summary

Compressed airway/hemo/SBAR/documentation foundations by ~7 shifts total; preserved full regional/emergence/family/judgment content. Watch ICU-halo and confidence-as-competence biases at Wk 4 pacing diagnostic.

## Re-run cadence

Re-run if Wk 4 pacing diagnostic shows compression of airway/hemo was premature (e.g., residual blockade missed, post-spinal escalation late).
```

Notes on Tier 1 quality: every compression tied to declared evidence, PACU-distinctive axes preserved, ICU-halo flagged with specific pacing week, no tenure-only or license-pathway compression.
</details>

## Self-check

- [ ] Compressions tied to concrete declared evidence.
- [ ] PACU-distinctive axes preserved.
- [ ] At least one bias flagged + pacing week named.
- [ ] No protected-characteristic / license-pathway / tenure-only adaptation.
- [ ] FPP section passed.
