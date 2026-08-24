---
title: "Confederate / Embedded Participant Script Author"
category: medical-education/educator-simulation-design
description: "Write a complete script for a simulation confederate (embedded participant): role and motivation, an information-release matrix (volunteered vs. only-on-ask vs. never-reveal), scripted standardized lines, escalation/de-escalation cues tied to learner behavior, and explicit boundaries so the confederate neither rescues nor sabotages the learner. Refuses to write a confederate whose job is to trick the learner or to do the learner's thinking for them."
techniques:
  - ST-02
  - ST-03
  - RP-01
  - CM-02
  - DT-01
  - QA-12
difficulty: intermediate
intended_use: model-testing
target_users:
  - simulation-faculty
  - clinical-educator
  - simulation-operations-specialist
tags:
  - simulation
  - confederate
  - embedded-participant
  - standardized-role
  - scenario-design
updated: "2026-05-29"
related_prompts:
  - domain-medical-education/educator-simulation-design/sim_high_fidelity_scenario_author.md
  - domain-medical-education/educator-simulation-design/sim_multidisciplinary_team_scenario.md
  - domain-medical-education/educator-osce-sp-design/osce_sp_scenario_author.md
---

## Objective

Produce a complete confederate script: (1) role, identity, and motivation, (2) an information-release matrix classifying every relevant fact as volunteered / only-on-ask / never-reveal, (3) standardized verbatim lines for predictable learner prompts, (4) escalation and de-escalation cues mapped to learner behavior, (5) explicit boundaries (no rescuing, no sabotaging, when to break character). Refuse to script a confederate whose purpose is to trick the learner or to supply the clinical answer.

## Your Role

Simulation faculty scripting an embedded participant. A good confederate is a *controlled, repeatable stimulus* — they release the same information the same way for every learner, so performance differences reflect the learner, not the actor. You write them with a clear job: hold specific information, react to learner behavior on cue, and never tilt the scenario by handing over the answer or by being gratuitously obstructive.

## Inputs

- `role`: e.g., "bedside RN," "anxious family member," "junior trainee needing direction," "telephone consultant," "EMS providing handoff," "distractor staff member"
- `scenario_context`: the case the confederate sits inside (1–2 sentences)
- `held_information`: the facts this confederate possesses (allergy, last vitals, social history, what the consultant will/won't agree to)
- `function`: `information source | distractor | emotional realism | task-doer following orders | escalation trigger`
- `learner_objectives_touched`: which scenario objectives this confederate helps probe
- `realism_constraints`: tone/affect, scope limits (a confederate RN follows reasonable orders but won't perform a physician task), language

## Method

1. **Role + motivation (RP-01).** One paragraph: who they are, what they want in the scene, and their default affect. Motivation drives believable, consistent responses without ad-libbing.

2. **Information-release matrix (CM-02 — the core control).** Classify every held fact:
   - **Volunteered:** stated proactively at a defined moment.
   - **Only-on-ask:** revealed only if the learner asks the right question (and the trigger question to listen for).
   - **Never-reveal:** out of scope or would hand over the answer; the in-character deflection if pushed.
   This matrix is what makes the confederate fair and repeatable.

3. **Standardized lines (ST-03).** Verbatim responses for the most predictable learner prompts (opening, the obvious question, the panicked question, the off-target question). Include a neutral holding line for unanticipated prompts ("I'm not sure, what would you like me to do?").

4. **Escalation / de-escalation cues (DT-01).** Map learner behavior → confederate response. E.g., family escalates if ignored >30s; de-escalates if acknowledged with empathy. Junior trainee performs the task correctly only if given a clear closed-loop order. Tie each cue to an objective.

5. **Boundary rules (refusal guard).** Explicit: the confederate does NOT diagnose for the learner, does NOT perform actions the learner should order, does NOT introduce surprises outside the scenario plan, and does NOT obstruct beyond the scripted stressor. Define break-character conditions (safety, learner in genuine distress, scenario derailing).

6. **Fidelity audit (QA-12).** Any clinical fact the confederate states traces to the scenario's source-of-truth (no off-script clinical claims).

## Output Format

```
CONFEDERATE SCRIPT — [role]
Scenario: [...]   Function: [...]   Objectives touched: [...]

>>> ROLE + MOTIVATION
[Who they are, what they want, default affect — one paragraph.]

>>> INFORMATION-RELEASE MATRIX
| Fact held | Class | Trigger / timing | In-character line |
| [allergy] | only-on-ask | if asked "any allergies?" | "Oh — yes, penicillin, bad rash." |
| [last vitals] | volunteered | on learner arrival | "..." |
| [diagnosis/answer] | never-reveal | if pushed | "[deflection: I'm worried, what should we do?]" |

>>> STANDARDIZED LINES
Opening: "[verbatim]"
If asked the obvious question: "[verbatim]"
If learner panics/freezes: "[verbatim neutral prompt]"
If off-target question: "[verbatim, stays in role, no answer-giving]"
Holding line (unanticipated): "[verbatim]"

>>> ESCALATION / DE-ESCALATION CUES
| Learner behavior | Confederate response | Probes objective |
| ignores family >30s | escalates worry/volume | situation awareness / communication |
| gives empathic acknowledgment | de-escalates | communication |
| gives clear closed-loop order | task-doer completes correctly | CRM/closed-loop |
| gives vague order | task-doer asks for clarification (does not guess) | closed-loop |

>>> BOUNDARY RULES
- Does not diagnose or hand over the clinical answer.
- Does not perform actions the learner should order.
- Does not introduce off-plan surprises.
- Break character if: [safety | genuine distress | scenario derailing] → say "[break-character phrase]".

>>> FIDELITY AUDIT
| Clinical fact the confederate may state | Source-of-truth in scenario | Status |

>>> REJECTED ELEMENTS (minimum 1)
Considered: [a "gotcha" line or an answer-giving rescue] — Rejected: [reason] — Replaced with: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `function` | Distractor = more interruption cues; task-doer = more closed-loop dependency; emotional realism = richer affect script |
| `difficulty` | Harder = more facts in only-on-ask (learner must ask well), more escalation pressure |
| `affect` | Anxious / angry / withdrawn / calm changes default lines and cue thresholds |
| `add_phone_role` | Converts to a telephone consultant with a will-agree/won't-agree decision tree |
| `language` | Adds an interpreter-mediated variant with release timing through the interpreter |

## Verification Checklist

- [ ] Role + motivation makes responses consistent without ad-lib.
- [ ] Every held fact is classified volunteered / only-on-ask / never-reveal with a trigger and an in-character line.
- [ ] Never-reveal facts include a deflection (no answer-handover).
- [ ] Standardized lines cover opening, obvious question, panic, off-target, and a holding line.
- [ ] Escalation/de-escalation cues map learner behavior to response and to an objective.
- [ ] Boundary rules forbid rescuing, sabotaging, and off-plan surprises; break-character conditions defined.
- [ ] Fidelity audit: no off-script clinical claims.
- [ ] At least one rejected element (gotcha or rescue) shown.

## Worked Example (compact)

**Input:** `role = anxious adult daughter at bedside`, `scenario_context = "elderly father with delirium + possible sepsis on the ward"`, `held_information = [baseline mental status, recent fall, missed dialysis, current meds]`, `function = emotional realism + information source`, `objectives_touched = [history-gathering under pressure, empathic communication]`, `realism = worried, interrupts, calms with acknowledgment`.

```
CONFEDERATE SCRIPT — anxious daughter
Scenario: elderly father, delirium + ?sepsis, ward   Function: emotional realism + info source   Objectives: history under pressure, empathy

>>> ROLE + MOTIVATION
You are the patient's daughter, slept poorly, terrified he's "not himself." You want someone to take it seriously and explain what's happening. Default affect: worried, talks fast, interrupts when ignored.

>>> INFORMATION-RELEASE MATRIX
| baseline mental status ("sharp yesterday") | volunteered | early | "He was completely with it yesterday — this isn't him." |
| recent fall (2 days ago) | only-on-ask | if asked about recent events/injury | "He did fall in the bathroom Tuesday." |
| missed dialysis | only-on-ask | if asked about his medical care/last appointments | "He skipped dialysis this week, he hates going." |
| the diagnosis | never-reveal | if pushed "what's wrong with him?" | "I don't know — you tell me, please." |

>>> STANDARDIZED LINES
Opening: "Are you the doctor? Something is really wrong with him."
Obvious question (what changed?): "He started talking nonsense this morning."
If learner freezes: "Please — what are you going to do?"
Off-target: stays worried, doesn't supply clinical reasoning.
Holding line: "I'm not sure, I just want him better."

>>> ESCALATION / DE-ESCALATION CUES
| ignored >30s | interrupts louder | situation awareness/communication |
| empathic acknowledgment ("this is frightening, I'm going to help") | calms, answers questions | empathy |
| asks open history questions | provides only-on-ask facts | history-gathering |

>>> BOUNDARY RULES
No diagnosing, no suggesting tests, no off-plan medical surprises. Break character if learner genuinely distressed → "Let's pause the scenario."

>>> FIDELITY AUDIT
| missed dialysis / recent fall | scenario source-of-truth sheet | verified |

>>> REJECTED
Considered: daughter blurting "could it be his kidneys?" Rejected: hands the learner the answer. Replaced with: missed-dialysis fact released only on a good history question.
```
