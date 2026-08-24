---
name: pacu-case-scenario-writer
description: Write realistic PACU case scenarios for simulation, tabletop drills, or orientation debriefs — with branching complications, assessment cues, and debrief questions. Use when the user asks for a "case", "scenario", "simulation", "mock situation", or "role-play" for PACU training. Output is layered: setup, unfolding complications, expected nursing actions, debrief.
tags:
  - pacu
  - nursing-education
  - simulation
  - case-scenario
updated: "2026-04-14"
---

# PACU Case Scenario Writer

## Purpose

Produce a case scenario that a preceptor or educator can run with one orientee or a group. Scenarios unfold in phases so the facilitator can stop at decision points and assess reasoning. Ends with structured debrief questions.

## When to use

- Tabletop drill, sim-lab scenario, orientation week capstone.
- Topic-specific skill check (e.g., "deteriorating airway post-extubation", "hypotension after spinal", "PONV escalation").
- Teaching clinical reasoning in a controlled setting.

## When NOT to use

- User wants a knowledge quiz → `pacu-quiz-generator`.
- User wants a step-by-step algorithm → `pacu-algorithm-flowchart-designer`.
- User wants prose teaching → `pacu-in-depth-explainer`.

## Inputs required

1. **Learning focus** — the one skill or reasoning pattern the scenario is built to exercise.
2. **Audience** — novice orientee, mid-orientation, charge-ready.
3. **Setting constraints** — sim lab, tabletop, live preceptor at bedside (affects format).
4. **Duration target** — default 15 minutes run time.
5. **Source chapters** for expected actions.

## Workflow

1. **Confirm inputs.** Learning focus must be *singular* — push back if user lists 3+ objectives.
2. **Write phases:**
   - **Phase 0 — Setup.** Demographics, surgery, anesthesia type, arrival vitals, monitors in use, devices present. No complication yet.
   - **Phase 1 — Initial assessment.** What's reported in handoff; what the orientee should do first.
   - **Phase 2 — Deterioration.** Introduce the scenario's complication. Include timed vital changes and patient cues.
   - **Phase 3 — Decision point.** Facilitator pauses and asks "what do you do now?".
   - **Phase 4 — Resolution or escalation.** Depending on the orientee's actions, scenario resolves or escalates.
3. **For each phase**, provide: facilitator script, expected nursing actions, hidden cues (what to volunteer only if the orientee asks).
4. **Write a divergence table** — what to do if the orientee does X vs. Y vs. Z.
5. **Debrief questions:**
   - What cues prompted your reassessment timing?
   - What did you rule in / rule out before escalating?
   - If you had the same scenario with a different surgery, what would change?
   - One thing to take to your next shift.
6. **Add facilitator notes** — common orientee pitfalls for this scenario.
7. **Safety reminder. Self-check.**

## Output format

```markdown
# {Scenario title} — PACU Case Scenario

> Safety reminder: Training scenario only — not a substitute for clinical judgment or facility protocols.

## Learning focus
[single skill / reasoning pattern]

## Setting / duration
[sim lab / tabletop / bedside; ~15 min]

## Phase 0 — Setup
**Patient:** [age, surgery, anesthesia, pertinent Hx]
**On arrival (Minute 0):** VS, monitors, devices.

## Phase 1 — Initial assessment
**Handoff says:** ...
**Expected orientee actions:** ...
**Hidden cues (volunteer if asked):** ...

## Phase 2 — Deterioration
**At minute 3:** ...
**At minute 5:** ...
**Patient says:** ...

## Phase 3 — Decision point
**Facilitator pause:** "What do you do?"
**Good answer includes:** ... (cites *Drain's* Ch. XX)

## Phase 4 — Resolution / escalation
### If orientee acts correctly
...
### If orientee misses / delays
... (still safe — facilitator provides hint at minute 7)

## Divergence table
| Orientee does | Scenario shifts to | Debrief emphasis |
|---|---|---|
| ... | ... | ... |

## Debrief questions
1. ...

## Facilitator notes — common pitfalls
- ...

## Sources
- ...
```

## Source-fidelity rules

- Vitals may be invented within clinically realistic ranges but must be consistent across phases.
- Medications named in "expected actions" come from cited sources; doses are *per facility protocol* or quoted from source.
- No facility-specific paging, location, or equipment names.

## Self-check

- [ ] Single learning focus.
- [ ] 5 phases present; each has facilitator script + expected actions + hidden cues.
- [ ] Divergence table covers at least 2 orientee paths.
- [ ] Debrief has ≥ 3 reasoning questions (not just recall).
- [ ] Facilitator notes list ≥ 2 common pitfalls.
- [ ] Safety reminder at top.
