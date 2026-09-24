---
title: "Ideation Workshop Facilitation Plan — Agenda, Diverge/Converge Sequencing, Roles, Remote Variant"
category: ideation/facilitation
description: "Design a 90-minute to full-day ideation workshop: a timed agenda that never mixes divergence and convergence in the same block, exercise choices drawn from this domain, named roles (facilitator, decision owner, timekeeper, scribe), pre-work, materials, energy management, and a remote/hybrid variant with its own timings. Ends with how outputs become owned next steps. Distinct from ideation_crazy_eights.md (one exercise) and domain-productivity/workplace/work_meeting_agenda_builder.md (routine meetings, not generative workshops)."
techniques:
  - NE-02
  - DP-23
  - CM-02
  - DS-40
  - QA-01
difficulty: intermediate
tags:
  - ideation
  - workshop
  - facilitation
  - agenda-design
  - remote-workshop
  - diverge-converge
updated: "2026-09-24"
reasoning:
  styles: [procedural, planning, collaborative]
  stakes: moderate
  horizon: short
  uncertainty: moderate
  evidence_quality: not_applicable
  domain_complexity: moderate
  collaboration: team
  output_format: structured
  user_role: [facilitator, pm, designer, team_lead, founder]
  mode: [plan]
related_prompts:
  - domain-ideation/ideation_crazy_eights.md
  - domain-ideation/ideation_idea_convergence_dot_voting.md
  - domain-productivity/workplace/work_meeting_agenda_builder.md
---

# Ideation Workshop Facilitation Plan

**Objective:** Produce a run-ready plan for an ideation workshop: what happens minute by minute, which exercise runs in each block and why, who does what, what participants do beforehand, and how the output leaves the room with owners. The plan's backbone is strict phase separation — frame, diverge, converge, commit — because the most common workshop failure is judging ideas while they are still being generated. It also produces a remote or hybrid variant, since the same agenda run on video loses energy and time in predictable ways.

---

## When to Use

- You are running a 90-minute to full-day session whose goal is new ideas plus a shortlist.
- You have been handed a workshop with a topic and a date but no design.
- A previous session produced a long list nobody acted on.
- The workshop will be remote or hybrid and you need timings that survive video.

**Distinct from:**
- `domain-ideation/ideation_crazy_eights.md` and the other exercise prompts in this domain — each is one block. This prompt chooses and sequences them.
- `domain-productivity/workplace/work_meeting_agenda_builder.md` — agendas for routine meetings (updates, decisions). Workshops need phase design, exercises, and energy management that meeting agendas do not.
- `domain-AI-ML/feature-engineering/mlfeature_ideation_workshop.md` — a workshop specialised for ML feature ideas.

**When NOT to use:**
- The decision is already made and you need buy-in — that is a communication session, not ideation.
- Fewer than three participants — run the exercise prompts directly.

---

## Inputs / Context

1. **Goal.** The question the workshop answers, ideally as a How Might We (see `ideation_how_might_we_reframe.md`).
2. **Decision owner.** Who will act on the output, and whether they attend.
3. **Participants.** Number, roles, seniority mix, any known dominant voices.
4. **Duration and format.** In-person, remote, or hybrid; time zones if remote.
5. **Desired output.** E.g., "3 concepts ready to test", "a prioritised backlog of 10".
6. **Materials and tools.** Room, whiteboard, sticky notes, or digital board.

---

## Method

### Step 1 — Fix the output and the owner
Write the outcome in one sentence and name the decision owner. If there is no owner, flag it: the plan can proceed, but the commit phase will produce suggestions, not decisions.

### Step 2 — Allocate time across four phases
Default split: **Frame** 10–15% · **Diverge** 35–40% · **Converge** 30–35% · **Commit** 10–15%. Add a break every 60–90 minutes in person, every 45–60 minutes remote.

### Step 3 — Choose exercises per phase
- **Frame:** context brief, HMW read-out, one warm-up.
- **Diverge (solo first, then group):** e.g., `ideation_crazy_eights.md`, `ideation_forced_quantity_100_ideas.md`, `ideation_scamper.md`, `ideation_worst_idea_first.md` for polite groups.
- **Converge:** `ideation_affinity_clustering.md` for large piles, then `ideation_idea_convergence_dot_voting.md`.
- **Commit:** owner decision, next steps, test plan.
State why each exercise suits this group and goal. Never place a divergence and convergence activity in one block.

### Step 4 — Assign roles
Facilitator (runs process, stays neutral on content), decision owner (decides in commit, speaks last in diverge), timekeeper, scribe/board keeper. In groups over eight, add breakout leads. The facilitator should not also be the decision owner.

### Step 5 — Design pre-work and materials
Pre-work under 20 minutes: context reading and 3–5 solo ideas submitted in advance (protects quieter participants and cuts anchoring). List materials per block.

### Step 6 — Build the remote/hybrid variant
Shorten blocks, move the context brief to pre-work, use breakouts of 3–5, run solo generation silently in a shared board with cameras optional, and add 10–15% buffer for tool friction. For hybrid, give remote participants a dedicated in-room advocate and use the digital board for everyone.

### Step 7 — Plan the exit
Define what the scribe captures, who sends the summary and when (within 48 hours), and where each shortlisted idea goes next with an owner and date.

---

## Output Format

```
# Workshop plan — [goal]

Outcome: [...]  Decision owner: [...]  Format: [in-person/remote/hybrid]

## Agenda (in-person)
| Time | Block | Phase | Exercise | Why this exercise | Output of block |

## Roles
| Role | Person | Responsibilities |

## Pre-work (≤20 min) and materials

## Remote / hybrid variant
| Time | Block | Change from in-person |

## Exit plan
| Output | Owner | Due | Next destination |

## Risks and mitigations
- ...
```

---

## Verification

- [ ] Outcome sentence and decision owner stated (or absence flagged).
- [ ] Every block labelled with exactly one phase; no diverge and converge in the same block.
- [ ] Solo generation precedes group discussion in divergence.
- [ ] Breaks scheduled at the stated intervals for the format.
- [ ] Remote variant has its own timings, not a copy of the in-person table.
- [ ] Exit plan names an owner and date for every shortlisted output.

---

## False-Positive Prevention

1. **A full agenda is not a good agenda.** Back-to-back exercises with no buffer overrun by the second block. Build in slack.
2. **Mixed phases.** "Brainstorm and discuss" in one block means discussion wins and generation stops. Separate them.
3. **The owner as facilitator.** When the person who decides also runs the room, ideas bend towards what they are known to want.
4. **Group-first generation.** Starting with open discussion lets the first speaker anchor everyone. Solo first.
5. **Remote as a copy.** A 60-minute in-person block run on video loses about a third of its useful time; redesign rather than transplant.
6. **Post-its as outcome.** A photo of the wall is not a result. The exit plan must name owners and dates.
7. **Exercise overload.** Four divergence methods in two hours produces fatigue, not breadth. Two well-run beats four rushed.

---

## Example

**Goal:** HMW help first-time customers reach their first successful report within a day? **Owner:** Head of Product (attends). **Participants:** 10 (product, design, support, sales, two engineers). **Format:** 3 hours in person, with a remote variant.

| Time | Block | Phase | Exercise | Output |
|------|-------|-------|----------|--------|
| 0:00 | Context + HMW read-out | Frame | Support-ticket highlights, 3 customer quotes | Shared problem |
| 0:20 | Solo ideas | Diverge | `crazy_eights` × 2 rounds | ~160 sketches |
| 0:45 | Share-back in pairs | Diverge | Build-on only, no critique | Expanded ideas |
| 1:10 | Break | — | — | — |
| 1:20 | Cluster | Converge | `affinity_clustering` | 8–10 themes |
| 1:50 | Vote + score | Converge | `idea_convergence_dot_voting` | Shortlist of 5 |
| 2:30 | Owner decision | Commit | Owner picks 3, explains | 3 concepts to test |
| 2:45 | Next steps | Commit | Owner + date per concept | Exit plan |

**Roles:** facilitator — design lead (not the owner); timekeeper — engineer; scribe — support lead. **Pre-work:** read five tickets, submit three ideas. **Remote variant:** 2 × 90 minutes on consecutive days; day 1 frame + diverge in a shared board, day 2 converge + commit; breakouts of 3; 10-minute buffer per session. **Exit:** summary within 48 hours; each concept gets an owner and a two-week test date.

---

## Techniques Used

- **NE-02 Phased Workflow Architecture** — frame → diverge → converge → commit with handoffs.
- **DP-23 Path Variants** — in-person and remote/hybrid branches of one plan.
- **CM-02 Constraint Specification** — phase-separation rule, break intervals, pre-work cap.
- **DS-40 Follow-Up Action Extraction** — exit plan with owners and dates.
- **QA-01 Self-Verification** — phase-labelling and remote-timing checks.

---

## Related Prompts

- `domain-ideation/ideation_crazy_eights.md` — a common divergence block.
- `domain-ideation/ideation_idea_convergence_dot_voting.md` — the standard convergence block.
- `domain-productivity/workplace/work_meeting_agenda_builder.md` — for routine meetings rather than workshops.
