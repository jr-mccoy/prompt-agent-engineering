---
title: "Non-Software Project Plan — WBS, Critical Path, RACI, Milestones, and Risks for Events, Facility Moves, and Rollouts"
category: operations/project-delivery
description: "Plan a physical or organizational project with a fixed date — an office move, an event, an equipment installation, a multi-site process rollout — as a deliverable-based WBS, a dependency network with the critical path and float computed, a RACI with one accountable owner per deliverable, dated milestones and go/no-go gates, and the risks that sit on the critical path."
techniques:
  - DT-01
  - RT-07
  - OC-03
  - QA-02
difficulty: intermediate
tags:
  - project-plan
  - work-breakdown-structure
  - critical-path
  - raci
  - office-move
  - event-planning
updated: "2026-09-24"
related_prompts:
  - domain-operations/supply-chain-procurement/ops_rfp_procurement_package.md
  - domain-risk/risk_register_builder.md
  - domain-product-management/prompts/product_delivery_sprint_planner.md
---

# Non-Software Project Plan

**Objective:** Produce a plan for a non-software project that shows what must be
delivered, in what order, by whom, which chain of tasks sets the end date, how much
slack everything else has, and which risks could move the date.

**When to Use:**
- A fixed-date project with physical or organizational work: facility move, office
  fit-out, event or conference, equipment install, multi-site rollout of a new
  process or policy.
- Several vendors and internal teams must hand work to each other in sequence.
- Someone has asked "are we going to make the date?" and nobody can answer with a
  path and a number.
- **Not this prompt if** you are delivering software in sprints from a PRD — use
  `domain-product-management/prompts/product_delivery_sprint_planner.md`. For a
  maintained project risk register with scoring and review cadence, use
  `domain-risk/risk_register_builder.md` (this plan feeds it the critical-path risks).
  For continuity of operations during a disruption, use
  `domain-risk/risk_business_continuity_plan.md`.

## Inputs / Context

1. **The goal and the fixed date(s)**, and what "done" means (people working at the
   new site on Monday; event doors open at 9:00).
2. **Known work**: vendors, internal teams, approvals, procurement lead times.
3. **Durations** for major tasks, with source (vendor quote, past project, estimate).
4. **Dependencies**: what cannot start until something else finishes.
5. **People and roles** available, and who can make decisions.
6. **Constraints**: permits, inspections, blackout dates, budget, building rules.

## Method

1. **Build a deliverable-based WBS (DT-01).** Decompose the goal into deliverables
   (nouns — "network live at new site"), then work packages small enough to own and
   estimate (typically 1–10 days of work or one vendor scope). The 100% rule: the
   children of each node add up to all of that node's work, nothing extra.
2. **Sequence and estimate.** For each work package: duration, predecessors, and
   source of estimate. Mark external lead times (furniture, permits) as their own
   activities — they are often the longest.
3. **Compute the critical path and float (RT-07).** Forward pass (earliest start and
   finish), then backward pass (latest start and finish) from the earliest finish.
   Total float = latest start − earliest start; the critical path is the zero-float
   chain. State the project buffer separately: fixed date minus earliest finish.
   Keeping the buffer visible as one number stops it being silently spent.
4. **Assign a RACI (OC-03).** For each deliverable: exactly one **A**ccountable,
   one or more **R**esponsible, and the **C**onsulted and **I**nformed. Two A's on a
   line means no one decides.
5. **Set milestones and go/no-go gates.** Milestones at the end of critical
   deliverables; at least one go/no-go gate with explicit criteria and a named
   decider, early enough that "no-go" still has an option.
6. **Critical-path risks (QA-02).** For each critical and near-critical activity:
   what would delay it, by how much, the early warning signal, and the response.
   Ask "what if the longest external lead time slips by its float plus one week?"
7. **Flag safety-critical and regulated work.** Structural, electrical, fire/life
   safety, occupancy permits, food safety, crowd management and similar items are
   planned here but approved by the qualified professional or authority.

## Output Format

```
# Project plan — [name]     Fixed date: [..]   Sponsor: [..]   PM: [..]

## Definition of done
## WBS
1 [deliverable]
  1.1 [work package] ...
## Schedule network
| ID | Activity | Duration | Predecessors | ES | EF | LS | LF | Float | Source |
Critical path: [IDs]   Earliest finish: [..]   Buffer to fixed date: [..]
## RACI
| Deliverable | R | A | C | I |
## Milestones and gates
| Milestone / gate | Date | Criteria | Decider |
## Critical-path risks
| Activity | Risk | Delay if it happens | Early signal | Response | Owner |
## Items requiring qualified approval
```

## Verification

- [ ] WBS nodes are deliverables; children cover 100% of the parent.
- [ ] Every activity has a duration source and predecessors.
- [ ] ES/EF/LS/LF are arithmetically consistent; critical path has the least float.
- [ ] Buffer to the fixed date is stated (and is not negative without an escalation).
- [ ] Each deliverable has exactly one Accountable.
- [ ] At least one go/no-go gate with criteria and a decider.
- [ ] Safety-critical and regulated items are listed for qualified approval.

## False-Positive Prevention

1. **Task lists as a WBS.** A flat to-do list has no structure to check against the
   goal. Decompose by deliverable first.
2. **Ignoring external lead times.** Furniture, permits, and specialist equipment
   often run longer than any internal work; leaving them out moves the critical path.
3. **Critical path by intuition.** The most visible task is not necessarily critical.
   Compute float.
4. **Float treated as spare time for everyone.** Float is shared along a path; if an
   early activity uses it, the later ones lose it.
5. **Two Accountables.** "Facilities and IT jointly accountable" produces a gap at
   the hand-off. Pick one.
6. **Gates with no alternative.** A go/no-go the day before the move is theatre;
   place it where "no-go" still has a fallback.
7. **Planning past a regulatory hold.** Occupancy and inspections set dates you
   do not control; do not schedule the move before the sign-off exists.

## Example Output

```
# Project plan — Office move, 85 staff to Floor 6   Fixed move weekend: end of week 14

## Definition of done
All 85 staff working at Floor 6 on Monday of week 15, network and phones live,
old floor handed back clean.

## WBS
1 Space ready: 1.1 design sign-off  1.2 fit-out  1.3 cabling & AV  1.4 furniture
2 Move executed: 2.1 movers contracted  2.2 packing & comms  2.3 move weekend
3 Settled in: 3.1 day-1 support & snag list

## Schedule network (weeks; week 0 = lease executed)
| B | Design sign-off    | 3 | —   | 0  | 3  | 0  | 3  | 0 | architect |
| C | Fit-out            | 8 | B   | 3  | 11 | 3  | 11 | 0 | contractor quote |
| E | Cabling & AV       | 2 | C   | 11 | 13 | 11 | 13 | 0 | IT vendor |
| D | Furniture lead time| 6 | B   | 3  | 9  | 6  | 12 | 3 | supplier |
| F | Furniture install  | 1 | C,D | 11 | 12 | 12 | 13 | 1 | supplier |
| G | Movers RFP & award | 4 | —   | 0  | 4  | 7  | 11 | 7 | past move |
| H | Packing & comms    | 2 | G   | 4  | 6  | 11 | 13 | 7 | estimate |
| I | Move-ready         | 0 | E,F,H | 13 | 13 | 13 | 13 | 0 | milestone |
Critical path: B → C → E (13 wk)   Earliest finish: week 13   Buffer to move weekend (wk 14): 1 week

## RACI
| Space ready   | Contractor, IT vendor | Facilities manager | Office manager | All staff |
| Move executed | Movers, office mgr    | Facilities manager | Dept heads     | All staff |
| Day-1 support | IT, facilities        | Office manager     | —              | All staff |

## Milestones and gates
| Fit-out complete + occupancy sign-off | wk 11 | inspection passed | Facilities mgr |
| Go/no-go                              | wk 12 | network test passed; furniture on site; sign-off held | Sponsor (COO) |
Fallback if no-go: move weekend shifts 2 weeks; current lease allows holdover (confirmed).

## Critical-path risks
| C | Inspection finds defects        | 1–2 wk | snag count at wk 10 walk | pre-inspection wk 10 | Facilities |
| E | Cabling access blocked by fit-out| 1 wk  | contractor 3-wk lookahead | joint schedule wk 8 | IT lead |
| D | Furniture slips >3 wk           | becomes critical | supplier ship date | hold ship-date check wk 6 | Office mgr |

## Items requiring qualified approval
Fire/life-safety and occupancy inspection; electrical work in fit-out; any change to
egress routes — approved by the building's licensed contractor and the authority, not this plan.
```

## Techniques Used

- **DT-01 Hierarchical Task Breakdown** — deliverable-based WBS under the 100% rule.
- **RT-07 Cascade Effect Analysis** — forward/backward pass shows how one slip moves the date.
- **OC-03 Markdown Table Specification** — schedule network, RACI, and risk tables.
- **QA-02 Adversarial Stress-Test** — "lead time slips by float plus one week" on each near-critical item.

## Related Prompts

- `domain-operations/supply-chain-procurement/ops_rfp_procurement_package.md` — contracting the movers or vendors.
- `domain-risk/risk_register_builder.md` — maintaining the project's full risk register.
- `domain-product-management/prompts/product_delivery_sprint_planner.md` — software delivery instead.
