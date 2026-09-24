---
title: "Tabletop Exercise Designer — A Scenario With Injects, Decision Points, and a Findings List That Changes the Plan"
category: risk
description: "Design and facilitate a 60–120 minute discussion-based tabletop exercise that tests a written plan (incident playbook, continuity plan, crisis-comms plan) against a realistic scenario: one stated objective, timed injects that force decisions at known weak points, a facilitator script, an observer sheet, and a hot-wash that produces owned plan changes; distinct from `risk_business_continuity_plan.md`, which schedules the test, and `risk_after_action_review.md`, which reviews a real event rather than a simulated one."
techniques:
  - ST-02
  - MP-04
  - QA-02
  - DS-40
  - OC-03
difficulty: intermediate
tags:
  - tabletop-exercise
  - incident-response
  - business-continuity
  - exercise-design
  - facilitation
  - preparedness
  - test-our-plan
  - emergency-drill
  - what-if-scenario
updated: "2026-09-24"
reasoning:
  styles: [scenario, adversarial, systems, reflective]
  stakes: moderate
  horizon: hours
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: small_team
  output_format: structured
  user_role: [operator, team-lead, executive, facilitator]
  mode: [design, rehearse, diagnose]
related_prompts:
  - domain-risk/risk_business_continuity_plan.md
  - domain-risk/risk_after_action_review.md
  - domain-risk/risk_security_incident_response_playbook.md
---

# Tabletop Exercise Designer

**Objective:** Produce a ready-to-run tabletop exercise — scenario, timed injects, facilitator
script, observer sheet and hot-wash — whose purpose is to find the gaps in a written plan
before a real event does, and to leave the room with each gap owned and dated.

**When to Use:**
- `risk_business_continuity_plan.md` lists a procedure as "never tested" and a tabletop is the
  next level of confidence it names.
- You have an incident playbook (`risk_security_incident_response_playbook.md`) nobody has read aloud.
- An insurer, client or auditor asks for evidence the plan has been exercised.
- Leadership changed, and the new people have never seen the plan.

**Not this prompt if:**
- You have no written plan yet — write it first; a tabletop tests a plan, it does not create one.
- A real event has happened — `risk_after_action_review.md` reviews reality, not a simulation.
- You want a live technical test (actually restore a backup, actually fail over) — that is a
  functional test owned by whoever runs the systems; this is discussion only.
- You want to stress-test a strategy or launch against adversaries — `risk_threat_model_non_technical.md`
  or `domain-decision-making/scenario_strategic_pre_mortem.md`.

**Boundary:** The scenario describes what happens *to* the organisation. It never includes
instructions for carrying out an attack, and injects are narrated consequences, not techniques.

## Inputs / Context

1. **The plan under test** and the one or two sections you most doubt.
2. **The exercise objective**, as one question: "Can we decide to shut down email within
   30 minutes without the owner present?" — not "test our readiness".
3. **Participants** (roles, 4–10 people) and who is deliberately absent.
4. **Time available** (60, 90 or 120 minutes).
5. **Known weak points**: single points of failure, untested steps, past near-misses.
6. **Sensitivities**: anyone implicated in a past incident; topics that must not become blame.

## Method

1. **Write one objective and three success criteria (ST-02).** Each criterion observable:
   "Decision authority invoked by inject 3", "Counsel called before any client message",
   "Backup location stated without looking it up". More than one objective turns the
   exercise into a tour.

2. **Choose a plausible scenario, anchored to a weak point (MP-04).** Pick the incident type
   most likely for this organisation, then set it at the worst ordinary time — Friday
   afternoon, the owner on a flight, month-end payroll due. Write a baseline version and one
   edge-case variant held in reserve if the group moves too easily.

3. **Build 5–7 timed injects (QA-02).** Each inject is new information that forces a decision
   the plan should answer. At least one inject must hit each of:
   - an **authority gap** (the decider is unreachable);
   - a **dependency on the failed thing** (the contact list lives in the down system);
   - an **outside party** (a client, bank, insurer or journalist calls);
   - a **legal question** the group must route, not answer.

   | # | Clock (scenario time) | Inject text | Decision it forces | Plan section tested | Expected answer per plan |
   |---|---|---|---|---|---|

4. **Write the facilitator script.** Opening ground rules (no-fault, "say what you would
   actually do, not what the plan says"), how to deliver each inject, the probe questions,
   and when to use the reserve variant. The facilitator never supplies answers.

5. **Write the observer sheet.** One observer, not a participant, records for each inject:
   time to decision, who decided, whether the plan was consulted, what was improvised.

6. **Run a structured hot-wash (DS-40).** Immediately after, 15–20 minutes: what worked;
   where we improvised; where the plan was wrong or silent. Extract every finding into an
   action with an owner and a date. Findings without owners are the usual way a tabletop
   changes nothing.

7. **Feed the plan.** Each finding maps to a plan section. Update the BCP test schedule
   ("tabletop, date, result") and any risk register entries.

## Output Format

```
# Tabletop exercise — [plan under test], [date]
Objective: [one question]
Success criteria: 1. ... 2. ... 3. ...
Participants: [roles] · Deliberately absent: [role] · Observer: [role] · Facilitator: [role]
Duration: [n] min

## Scenario (baseline) — [2–4 sentences]
## Reserve variant — [edge case, when to use]

## Inject schedule
| # | Clock | Inject | Decision forced | Plan section | Expected per plan |

## Facilitator script
Opening (3 min): ...
Per inject: deliver → wait → probe questions → move on at [n] min
Close: ...

## Observer sheet
| Inject | Time to decision | Decided by | Plan consulted? | Improvised | Note |

## Hot-wash findings
| Finding | Plan section | Keep / fix / add | Owner | Due |

## Success criteria result: met / partly / not met — evidence
## Plan updates owed and BCP test-schedule entry
```

## Verification

- [ ] Exactly one objective, phrased as a question the exercise can answer.
- [ ] Every inject forces a decision and names the plan section it tests.
- [ ] Injects cover authority gap, failed-dependency, outside party and legal routing.
- [ ] The decider for at least one inject is deliberately absent.
- [ ] The facilitator script contains probes, not answers.
- [ ] An observer, separate from participants, records time to decision.
- [ ] Every hot-wash finding has an owner and a due date.
- [ ] The BCP test schedule is updated with date and result.

## False-Positive Prevention

1. **"It went well" as the result.** A tabletop where nothing broke was usually too easy.
   Use the reserve variant; a clean run is a reason to raise difficulty, not to stop.
2. **Reading the plan aloud and calling it an exercise.** That is a walkthrough. A tabletop
   needs injects that force decisions under time pressure.
3. **Blame drift.** If the scenario echoes a real past incident, participants defend
   themselves. Change names and details; state the no-fault rule at the start.
4. **Answering legal questions in the room.** The correct response to "do we have to tell
   clients?" is "who calls counsel?" — the inject tests routing, not law.
5. **Everyone who matters is present.** Real incidents happen when the decider is away.
   Remove someone on purpose.
6. **Findings without owners.** A list of observations is not a result. No owner, no finding.
7. **Scenario as attack tutorial.** Narrate effects ("files show a new extension; a note
   demands payment"), never methods.

## Example Output

```
# Tabletop exercise — Security incident playbook (BEC module), 2026-10-08
Objective: Can we stop a fraudulent supplier payment and reach counsel within 60 minutes
without the Finance Director?
Success criteria: 1. Bank called by inject 3. 2. No reply on the compromised thread.
3. Counsel contacted before any supplier message.
Participants: Ops Manager, Office Admin, Sales Lead, MSP rep · Absent: Finance Director
Observer: HR Lead · Facilitator: external bookkeeper · Duration: 90 min

## Scenario — Thursday 16:10. The Office Admin reports a supplier's "new bank details" email
was actioned on Tuesday; today the real supplier chases an unpaid invoice of [amount].

## Inject schedule
| 1 | 16:10 | Supplier chases payment | Is this an incident? | Triage §1 | Yes → IR lead = Ops Mgr |
| 2 | 16:25 | Finance Director unreachable (flight) | Who authorises bank call? | IR Roles | Second = Ops Mgr |
| 3 | 16:40 | Bank says recall possible only today | Call now? | BEC module, first hour | Yes |
| 4 | 17:00 | Another supplier emails asking "is your email hacked?" | What do we say? | Templates | Hold; counsel first |
| 5 | 17:20 | MSP finds a forwarding rule to an external address | Delete it? | BEC module | Export, then remove |

## Observer sheet (excerpt)
| 2 | 11 min | Ops Mgr, after debate | No | Looked for FD's deputy in email (down) |
| 4 | 3 min | Sales Lead | No | Drafted reply to supplier before counsel |

## Hot-wash findings
| Nobody knew Ops Mgr was second decider | IR Roles | fix: print roles card | Ops Mgr | 10-15 |
| Supplier reply drafted before counsel | Templates | fix: "counsel reviewed" box | Office Admin | 10-22 |
| No bank recall contact held offline | Outside help | add | Ops Mgr | 10-15 |

## Success criteria: 1 met (bank at 16:44) · 2 met · 3 not met — see finding 2
## BCP test schedule: BEC procedure — tabletop 2026-10-08 — partly met — next: walkthrough after fixes
```

## Techniques Used

- **ST-02 Structured Sequential Instructions** — objective, injects, script, hot-wash in order.
- **MP-04 Strategic Edge Case Calibration** — baseline scenario plus a held-back edge variant.
- **QA-02 Adversarial Stress-Test** — injects aimed at the plan's known weak points.
- **DS-40 Follow-Up Action Extraction** — every hot-wash finding becomes an owned action.
- **OC-03 Markdown Table Specification** — inject schedule, observer sheet, findings table.

## Related Prompts

- `risk_business_continuity_plan.md` — its test schedule names the tabletop level this delivers.
- `risk_security_incident_response_playbook.md` — the most common plan under test.
- `risk_after_action_review.md` — for a real event rather than a rehearsal.
- `risk_register_builder.md` — where exercise findings that are risks get logged.
