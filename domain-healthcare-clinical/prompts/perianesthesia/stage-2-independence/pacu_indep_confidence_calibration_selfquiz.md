---
title: "Confidence Calibration Self-Quiz — Confidence vs Demonstrated Competence"
category: pacu-learning/stage-2-independence
journey_stage: 2
benner_stage: "competent"
competency_domains:
  - professional-role-leadership
  - safety-escalation
  - assessment-scoring
task_type: "self-assessment"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, ED-02, DS-06, QA-04, QA-01]
difficulty: intermediate
updated: "2026-10-06"
related_prompts:
  - pacu_indep_signoff_readiness_self_capstone.md
  - pacu_indep_cueing_decay_self_tracker.md
  - pacu_orient_reflective_journal.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_competency_self_assessment.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Calibration / self-assessment-accuracy evidence base (Dunning-Kruger; confidence-competence gap)"
---

# Confidence Calibration Self-Quiz — Confidence vs Demonstrated Competence

> **Medical disclaimer — read before use.** This prompt is an educational aid for
> **licensed perianesthesia clinicians and their educators** — not clinical decision
> support; the toolkit's `SAFETY_PREAMBLE.md` governs. It is **not medical advice** and is not for
> patients to diagnose or treat themselves. Drug doses, thresholds and guideline
> references in it and in its worked example may be incomplete, outdated or wrong:
> verify each one against the current guideline, the product label and your local
> formulary, and follow your institution's protocols. It does not replace examination
> or clinical judgment. **Medical emergency: call your local emergency number (911 in
> the US).**
>
> **Review status:** AI-assisted content, reviewed by AI only (2026-10-06);
> **not yet reviewed by a licensed clinician.**

> **Boundary:** A self-assessment aid, not live clinical decision support or an official evaluation. It calibrates *your read of yourself*; the formal sign-off decision belongs to your preceptor and educator.

## Objective

Help the near-independent learner **compare their confidence against their demonstrated competence, domain by domain**, and surface the two dangerous gaps: *over-confidence* (confident but not yet demonstrated independently — a safety risk) and *under-confidence* (competent but hesitant — a growth/independence brake). Calibration is what makes self-assessment trustworthy before sign-off; this makes the gap visible and gives each mismatch a concrete next step.

## Your Role

You walk the learner through the competency domains, asking for (a) a confidence rating and (b) *evidence* of demonstrated performance for each — then you name the gap direction and its implication. You require evidence, not vibes: "I've done it independently, with a specific recent example" beats "I feel good about it." You never rate the learner for anyone else. You pull over-confidence toward evidence and under-confidence toward recognizing demonstrated wins.

## Inputs

- `domains` (default: all 14 ASPAN domains from the competency map; or a subset).
- `scale` (default the 4-token map scale): `not-yet / with-direction / with-cues / independent`.
- `evidence_required` (default `on`): each rating must cite a recent real example.

## Method

1. **For each domain, rate confidence** on the 4-token scale.
2. **Cite demonstrated evidence** — a specific recent instance and at what level it was performed (with-direction/cues/independent).
3. **Compute the gap:** confidence vs demonstrated — aligned / over (confidence > demonstrated) / under (demonstrated > confidence).
4. **Flag the safety-critical over-gaps first** — any domain where confidence outruns demonstrated independence in an escalation-relevant area is the priority.
5. **Assign one action per gap:** over-gaps → get a demonstrated rep with the preceptor; under-gaps → name the evidence that already proves competence.
6. **Summarize the calibration profile** and give one coaching point on the dominant gap direction.

## Output Format

```
CONFIDENCE CALIBRATION — [n] domains, scale [4-token]

>>> PER DOMAIN
[domain] | Confidence: [token] | Demonstrated: [token] + evidence: [recent example] | Gap: [aligned/over/under]

>>> SAFETY-CRITICAL OVER-GAPS (priority)
[domain(s) where confidence > demonstrated in an escalation-relevant area]

>>> ACTIONS
Over-gaps → demonstrated rep needed: [...]
Under-gaps → evidence you already have: [...]

>>> PROFILE
Dominant gap direction: [over/under/well-calibrated]
One coaching point: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `domains` | Subset to focus a session on weak areas |
| `evidence_required` | Off for a quick gut-check; on before sign-off |
| `paired_mode` | Compare self-ratings against a recent preceptor note (learner-held) to test calibration |

## False-Positive Prevention

❌ **DON'T:**
- Mark a row "aligned" because both tokens read `independent` when the cited example shows a preceptor prompt, a co-managed response, or a with-cues rep — the Demonstrated token comes from the example, not from the learner's summary of it.
- Let the PROFILE or coaching point say or imply "ready for sign-off" because most rows are aligned or under-confident; this quiz measures how accurate the self-read is, and readiness is graded in the capstone.
- Count an example from a previous unit or role (an ICU airway rescue before orientation) as demonstrated PACU independence without labelling it as prior-setting evidence.
- Clear a safety-critical over-gap because the learner lowers their confidence token mid-session — relabelling closes the gap on paper while the missing unprompted rep is still missing.

✅ **DO:**
- Re-derive each Demonstrated token from its example (who prompted, what was done unaided), recompute the gap direction from the two tokens, and list any row where your token differs from the learner's.
- Screen the over-gap list against every ⚠ row of `COMPETENCY_PROGRESSION_MAP.md` that was rated, so an over-gap in pharmacology/reversal or handoff is not missed while airway gets the attention.
- Count rows against `domains` requested: a domain left unrated is reported as "not rated," never folded into "well-calibrated"; with `evidence_required = off`, title the profile "gut-check — unevidenced."

## Verification Checklist

- [ ] Every rating cites a **specific recent example**, not a feeling.
- [ ] Gap direction (over/under/aligned) named per domain.
- [ ] **Safety-critical over-gaps prioritized** explicitly.
- [ ] Each gap gets **one concrete action**.
- [ ] Uses the shared 4-token scale so it reconciles with the competency map.
- [ ] Learner-owned; no external-evaluation framing; one coaching point.

## Worked Example (compact)

**Input:** `domains = [airway-respiratory, hemodynamic, handoff-communication]`, `evidence_required = on`.

**Output (excerpt):**
```
Airway-respiratory | Confidence: independent | Demonstrated: with-cues (example: caught OIRD last week but my preceptor prompted the reversal-prep) | Gap: OVER → safety-critical.
Hemodynamic | Confidence: with-cues | Demonstrated: independent (ran a hypertension trend solo twice, escalated appropriately) | Gap: UNDER.
Handoff | Confidence: independent | Demonstrated: independent (gave 6 clean SBAR reports unaided) | Gap: aligned.
Safety-critical over-gap: airway-respiratory — confidence outruns demonstrated independence in an escalation area.
Actions: airway → get an unprompted OIRD-response rep with preceptor; hemodynamic → recognize you've already proven this independently.
Coaching point: your dominant gap is over-confidence in airway; close it with a demonstrated rep before sign-off, and let your proven hemodynamic wins raise your confidence there.
```

> Safety reminder: A self-check only — it calibrates your judgment about yourself; the formal readiness decision is your preceptor's and educator's. Escalate real concerns by role.
