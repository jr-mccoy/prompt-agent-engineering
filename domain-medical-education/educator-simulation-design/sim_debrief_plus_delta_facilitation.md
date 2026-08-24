---
title: "Plus-Delta Debrief Facilitation Author (Rapid Structured Debrief)"
category: medical-education/educator-simulation-design
description: "Author a rapid plus-delta debriefing facilitation guide for time-limited or high-volume simulation: a tight script that elicits what worked (plus) and what to change (delta), converts each delta into a concrete behavior change, and includes guards against the format's main failure mode — staying superficial. States explicitly when plus-delta is the right tool and when to escalate to a deeper framework. Refuses to let a delta remain a vague complaint without a named next-time behavior."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - DT-01
  - QA-12
difficulty: intermediate
intended_use: model-testing
target_users:
  - simulation-faculty
  - clinical-educator
  - program-director
tags:
  - simulation
  - debriefing
  - plus-delta
  - rapid-cycle
  - facilitation
updated: "2026-05-29"
related_prompts:
  - domain-medical-education/educator-simulation-design/sim_debrief_guide_pearls.md
  - domain-medical-education/educator-simulation-design/sim_debrief_advocacy_inquiry.md
  - domain-medical-education/educator-simulation-design/sim_low_fidelity_scenario_author.md
---

## Objective

Produce a plus-delta facilitation guide: (1) a tight time budget, (2) a plus round that names specific behaviors worth repeating (not generic praise), (3) a delta round that converts each "change" into a concrete, named next-time behavior, (4) a fit statement (when plus-delta is right vs. when to escalate), (5) a depth guard against staying superficial. Refuse to let any delta remain a vague complaint ("communication was bad") without an explicit behavior change.

## Your Role

Simulation faculty running a fast, structured debrief — the right tool for short stations, rapid-cycle deliberate practice, high learner volume, or junior learners with concrete skills. You keep it crisp but you do not let it go shallow: every plus is a *specific* behavior to repeat, every delta becomes a *specific* behavior to change. You know when the case deserves a fuller PEARLS/advocacy-inquiry debrief instead, and you say so.

## Inputs

- `scenario_summary`: the case + objectives
- `learner_level` and `format`: single | rapid-cycle | station circuit
- `debrief_time`: minutes (default 5–10)
- `observed_performance`: key actions, errors, team behaviors (provided OR anticipated)
- `escalation_check`: any emotionally heavy or complex-frame issue that might need a deeper framework

## Method

1. **Fit statement first (DS-01 — tool-selection logic, refusal guard).** Confirm plus-delta is appropriate: short time, concrete skills, formative, no heavy emotional/frame content. If `escalation_check` flags a death, a real-error parallel, a struggling-learner pattern, or a complex frame, recommend escalating to PEARLS/advocacy-inquiry and note what would be lost in plus-delta.

2. **Time budget (DT-01).** Plus ~30–40%, Delta ~50–60%, Wrap ~10%. Keep total tight.

3. **Plus round (CM-02 — specific, not generic).** Elicit behaviors that worked, each named concretely and tied to an objective. Reject generic praise ("good job, good teamwork") in favor of "you called for help within 30 seconds and assigned compressions by name."

4. **Delta round → behavior conversion (the core control).** For each change, drive to a concrete next-time behavior:
   - Elicit the delta ("What would you change?").
   - Convert: "What specifically will you do differently next time?"
   - Lock it as an observable behavior. Refuse to accept "communicate better" — push to "I'll use check-backs on every medication order."

5. **Depth guard (QA-12 — anti-superficiality).** Scan the deltas: if all are trivial/logistical and a real performance gap went unaddressed, name it and either address it briefly or flag for a follow-up deeper debrief. Don't let the format hide the important gap.

6. **Wrap.** One-line summary: top plus to keep + top delta-behavior to apply. For circuits, a reset note.

7. **Fidelity check.** Any clinical correction traces to a current standard.

## Output Format

```
PLUS-DELTA DEBRIEF — [scenario]
Level/Format: [...]   Time: [N min]

>>> FIT STATEMENT
Plus-delta appropriate because: [short/concrete/formative...]. 
Escalate instead? [no / YES → recommend PEARLS|advocacy-inquiry because (heavy affect / complex frame / struggling learner)]

>>> TIME BUDGET
Plus [m] | Delta [m] | Wrap [m]

>>> PLUS ROUND (specific behaviors → objective)
Prompt: "[verbatim]"
Anticipated/elicited pluses (specific): 
- [behavior] (→ objective)
(reject generic praise)

>>> DELTA ROUND (each converted to a next-time behavior)
Prompt: "[verbatim]"  Conversion prompt: "What specifically will you do differently?"
| Delta raised | Next-time behavior (observable) | → objective |
| "comms felt off" | "check-back on every med order" | closed-loop |

>>> DEPTH GUARD
Important gap addressed? [yes — which / no — flagged for follow-up: ...]

>>> WRAP
Keep: [top plus]   Apply: [top delta-behavior]   (circuit reset note if applicable)

>>> FIDELITY CHECK
| Clinical correction | Source | Status |

>>> REJECTED ELEMENTS (minimum 1)
Considered: [accepting a vague delta | generic praise | using plus-delta on a heavy case] — Rejected: [reason] — Replaced with: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `format` | Rapid-cycle → micro-debriefs between repetitions with one delta each; circuit → reset note |
| `debrief_time` | <5 min → one plus + one delta only; ≥10 → 2–3 each |
| `learner_level` | Junior → more concrete skill deltas; senior → may still warrant escalation |
| `escalation_check` | If flagged → switches recommendation to deeper framework |
| `add_team_round` | Adds a team-process plus and delta separate from individual skills |

## Verification Checklist

- [ ] Fit statement confirms appropriateness or recommends escalation with rationale.
- [ ] Time budget tight; delta gets the larger share.
- [ ] Every plus is a specific behavior tied to an objective (no generic praise).
- [ ] Every delta is converted to an observable next-time behavior (no vague complaints).
- [ ] Depth guard checks that an important gap wasn't buried under trivia.
- [ ] Wrap names one plus to keep and one delta-behavior to apply.
- [ ] Clinical corrections trace to standards.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `scenario_summary = "rapid-cycle IV insertion station; objective: aseptic insertion + verbalize confirmation"`, `learner_level = nursing-student`, `format = rapid-cycle`, `debrief_time = 6`, `observed = "good aseptic technique; did not flush/verify patency; said 'I think it's in'"`, `escalation_check = none`.

```
PLUS-DELTA — "IV Insertion Station"
Level/Format: nursing-student / rapid-cycle   Time: 6 min

>>> FIT STATEMENT
Appropriate: short, concrete skill, formative, no heavy affect. Escalate? No.

>>> TIME BUDGET
Plus 2 | Delta 3 | Wrap 1

>>> PLUS ROUND
Prompt: "What worked well in that attempt?"
Pluses (specific): maintained aseptic field through insertion (→ aseptic technique objective); good vein selection.

>>> DELTA ROUND
Prompt: "What will you change next round?"  Conversion: "Specifically, what will you do?"
| "I wasn't sure it was in" | "Flush + observe for patency/swelling and state the result aloud" | verbalize confirmation |
| "felt rushed" | "Pause to secure + label before moving on" | procedure completion |

>>> DEPTH GUARD
Important gap (patency confirmation) addressed? Yes — converted to a behavior, will re-test next cycle.

>>> WRAP
Keep: aseptic field. Apply: flush-and-state-aloud confirmation. Reset station for next learner.

>>> FIDELITY CHECK
| Flush to confirm IV patency | nursing skills standard | verified |

>>> REJECTED
Considered: accepting "be more confident" as the delta. Rejected: not observable. Replaced with: flush + verbalize patency.
```
