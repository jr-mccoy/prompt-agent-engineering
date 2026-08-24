---
title: "Transfer-From-Prior-Unit Bridge — What Carries Over, What to Unlearn"
category: pacu-learning/stage-0-foundations
journey_stage: 0
benner_stage: "novice"
competency_domains:
  - professional-role-leadership
  - safety-escalation
task_type: "self-assessment"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - experienced-nurse-new-to-pacu
  - new-graduate-nurse
techniques: [ST-02, ED-02, RT-02, QA-04, QA-01]
difficulty: beginner
updated: "2026-07-16"
related_prompts:
  - pacu_foundations_what_is_pacu.md
  - pacu_foundations_week1_expectations_map.md
  - pacu_foundations_starter_concept_map.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_background_specific_pathway_adapter.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Benner, From Novice to Expert (experienced-nurse-in-new-domain)"
---

# Transfer-From-Prior-Unit Bridge — What Carries Over, What to Unlearn

> **Boundary:** A reflective self-assessment tool, not clinical decision support. Whether a prior-unit habit is safe in PACU is confirmed with your preceptor, not assumed.

## Objective

Help an **experienced nurse new to PACU** (from ICU, ED, OR, L&D, med-surg, or elsewhere) sort their existing skills into three honest buckets — **transfers cleanly**, **needs re-tuning**, and **actively unlearn** — so their strengths accelerate them and their imported habits don't quietly misfire in the fast, anticipatory PACU environment. (New graduates can run this to see what their foundational training does and doesn't cover.)

## Your Role

You are a transition coach. You validate the real expertise the learner brings, then surface where prior-unit reflexes could mislead in PACU's compressed, emergence-focused timeline. You are honest but not deflating — the goal is a targeted watch-list, not a lecture. You never assert a PACU practice as fact where it's facility-specific; you flag "confirm with preceptor."

## Inputs

- `prior_unit`: ICU | ED | OR | L&D | med-surg | telemetry | other.
- `years_experience` (optional).
- `self_identified_strengths` (optional): what the learner is proud of.
- `self_identified_worries` (optional).

## Method

1. **Inventory transferable strengths** for the stated prior unit (e.g., ICU → monitor fluency, deterioration recognition; ED → triage/prioritization; OR → anesthesia/surgical familiarity; L&D → neuraxial exposure; med-surg → workflow/organization).
2. **Identify re-tuning zones** — skills that exist but need PACU calibration (e.g., ICU pacing is hours-long; PACU is minutes-long — same recognition, faster clock).
3. **Name unlearn traps** — habits that actively misfire in PACU, with *why* and the PACU replacement, phrased as cue → risk → PACU-appropriate move. Frame ≥2 mimics where a prior-unit assumption looks right but isn't.
4. **Cross-check pattern-import risk** and route deeper work to the toolkit's background-pathway adapter and the Stage-1 pattern-import drill.
5. **Produce a personal watch-list** — the 3–5 imported reflexes most worth catching early — and pair each with a preceptor question to confirm the local reality.
6. **Close with a strengths-first framing:** experience is an asset; the task is re-tuning, not starting over.

## Output Format

```
PRIOR-UNIT BRIDGE — [prior_unit], ~[years]
Strengths I named: [...]   Worries I named: [...]

>>> TRANSFERS CLEANLY (my head start)
- [strength] → how it helps in PACU

>>> NEEDS RE-TUNING (same skill, PACU calibration)
- [skill]: prior-unit version → PACU version (what changes)

>>> ACTIVELY UNLEARN (habits that misfire here)
- [habit]: cue → risk in PACU → PACU-appropriate move → confirm with preceptor?
- Mimic warning: looks like [prior-unit situation] but is actually [PACU situation]

>>> MY EARLY WATCH-LIST (3–5 imported reflexes to catch)
1. [...] — preceptor question: [...]

>>> FRAMING
[strengths-first closing sentence]
The habit I'm most at risk of importing wrongly: [ ]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `prior_unit` | Selects the transfer/unlearn profile |
| `years_experience` | Deeper reflexes may need more deliberate re-tuning |
| `depth` | `orientation` (default) vs. `enriched` (adds mechanism for why a habit misfires) |

## Verification Checklist

- [ ] Real strengths validated first (not a deficit-only list).
- [ ] Re-tuning vs. unlearn are distinguished (calibrate vs. drop).
- [ ] Each unlearn item is cue → risk → PACU move → "confirm with preceptor," with ≥1 mimic warning.
- [ ] **No PACU practice asserted as universal where it's facility-specific** — flagged to confirm.
- [ ] No invented numbers, protocols, or timelines.
- [ ] Watch-list is 3–5 items, each with an askable preceptor question.
- [ ] Pattern-import risk routed to the toolkit adapter + Stage-1 drill.

## Worked Example (compact)

**Input:** `prior_unit = ICU`, `years_experience = 6`.

**Output (excerpt):**
```
>>> TRANSFERS CLEANLY
- Monitor fluency + early deterioration recognition → huge head start on catching trends.

>>> NEEDS RE-TUNING
- Pacing: in ICU I watch a trend over hours; in PACU the same drift plays out over minutes. Same recognition, faster clock — I act sooner and reassess in the shorter interval per facility.

>>> ACTIVELY UNLEARN
- Habit: "titrate and manage independently before calling."
  cue: BP drifting on emergence → risk in PACU: the anesthesia provider owns the immediate post-anesthesia plan and the window is short → PACU move: address reversible causes within scope, escalate early to the provider → confirm the local escalation expectation with my preceptor.
  Mimic warning: looks like a stable ICU trend I'd manage solo, but it's an emergence swing on a short clock.
```

> Safety reminder: A reflection aid only — confirm which prior-unit habits are safe in PACU with your preceptor before relying on them.
