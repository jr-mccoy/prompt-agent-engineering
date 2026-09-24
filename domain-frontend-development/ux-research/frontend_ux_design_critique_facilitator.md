---
title: "Design Critique Facilitator — Run a Critique That Tests Work Against Its Goals, Not Against Taste"
category: frontend-development/ux-research
description: "Prepare and run a structured critique of in-progress interface design: the designer states the goal, user, and stage; the facilitator sets the kind of feedback wanted, collects observations tied to those goals in a fixed order (what works, questions, concerns), separates taste from evidence, and closes with an owned decision list — distinct from the dashboard critique (which judges a business dashboard tile by tile) and the visual-direction finder (which chooses a direction rather than critiquing one)."
techniques:
  - OC-07
  - CM-03
  - ST-02
  - DS-06
  - QA-02
difficulty: intermediate
tags:
  - ux-research
  - design-critique
  - facilitation
  - design-review
  - feedback
  - collaboration
updated: "2026-09-24"
related_prompts:
  - domain-data-analytics/experiments-and-reporting/analytics_dashboard_critique.md
  - domain-frontend-development/design-direction/frontend_visual_design_direction_finder.md
  - domain-frontend-development/ux-research/frontend_ux_heuristic_evaluation.md
---

# Design Critique Facilitator

**Objective:** Turn a design review from a round of opinions into a session
that tells the designer which parts of the work meet its stated goals, which
do not, and what to do next — with every decision owned and every taste
comment labelled as taste.

**When to Use:**
- A designer wants feedback on screens, flows, or components at any fidelity.
- Reviews keep ending in "I just don't like it" or redesign-by-committee.
- A cross-functional group (PM, engineering, research) needs to review design
  together and produce decisions, not a thread.

**Not this prompt if:**
- You are critiquing a business dashboard's metrics and tiles →
  `domain-data-analytics/experiments-and-reporting/analytics_dashboard_critique.md`.
- You have no direction yet and need options → `domain-frontend-development/design-direction/frontend_visual_design_direction_finder.md`.
- You want a systematic usability inspection with severities →
  `frontend_ux_heuristic_evaluation.md` (a critique may *call for* one).
- You need user evidence; a critique is expert opinion, not a test.

## Inputs

1. **The work**: screens or prototype, and which parts are open for feedback.
2. **Designer's framing**: user, goal, constraints, and **stage**
   (exploring / converging / polishing).
3. **Feedback wanted**: e.g. "Is the hierarchy right?" — and feedback **not**
   wanted ("colour is fixed by brand").
4. **Participants and roles**; session length.
5. Any prior research evidence the room should know.

## Method

1. **Declare the ground rules (OC-07).** Read aloud at the start:
   - Feedback is tied to the stated goal or user, or it is labelled taste.
   - Ask before you advise.
   - The designer decides what to take; the group does not vote on design.
   - No solutions in the first two rounds.
2. **Set the scope (CM-03).** The designer presents in ≤5 minutes: user, goal,
   stage, constraints, and the specific questions. The facilitator writes the
   questions where everyone can see them and removes out-of-scope areas.
3. **Run the rounds in order (ST-02).**
   | Round | Prompt to the room | Output |
   |---|---|---|
   | 1. Clarify | "What do you need to know to judge this?" | Questions only |
   | 2. Works | "What here serves the goal? Why?" | Keeps |
   | 3. Concerns | "Where might this not meet the goal, for whom?" | Concerns, each tied to goal/user |
   | 4. Directions | "What could address the top concerns?" | Options, not mandates |
4. **Tag each comment** as *goal-linked*, *evidence-backed* (research or data
   cited), *convention* (platform or design-system rule), or *taste*.
5. **Prioritise concerns (DS-06)** by how badly they threaten the stated goal
   and how costly they are to fix at this stage.
6. **Stress-test the consensus (QA-02).** Before closing, ask: "What would
   have to be true for the design as-is to be right?" and "Which concern
   rests only on our own preference?"
7. **Close with decisions.** Each item: what, owner, by when, and whether it
   needs research (route to a usability test or heuristic evaluation).

## Output Format

```
# Design critique — [work], [date], stage: [..]
Designer's framing: user · goal · constraints · questions asked
Out of scope: [...]

## Keeps (what serves the goal)
## Concerns
| # | Concern | Tied to (goal/user) | Tag | Priority | Raised by |
## Directions offered (not mandates)
## Stress test
## Decisions
| # | Decision | Owner | By | Needs research? |
## Parked (taste or out of scope)
```

## Verification

- [ ] The designer's questions were written down before feedback started.
- [ ] Every concern cites the goal, user, evidence, or convention it relates to.
- [ ] Taste comments are recorded as taste, not as concerns.
- [ ] No solution appears in rounds 1–3.
- [ ] Each decision has one owner and a date.
- [ ] The stage (exploring/converging/polishing) shaped what was critiqued.

## False-Positive Prevention

1. **"I don't like it" is data about the speaker.** Record it under taste;
   ask what goal it threatens before promoting it.
2. **The loudest role is not the user.** A PM's or executive's preference is
   still preference unless tied to evidence.
3. **Polishing feedback on exploratory work wastes the session.** Pixel
   alignment on a wireframe is out of scope by stage.
4. **Solving too early narrows options.** A fix proposed in round 2 becomes
   the anchor for every later comment.
5. **Consensus is not validation.** A room agreeing that users will
   understand a label is a hypothesis to test, not a finding.
6. **Critique is not approval.** The session outputs decisions and research
   needs; sign-off is a separate step with its own owner.

## Example Output

```
# Design critique — Onboarding checklist (mid-fi), 2026-09-24, stage: converging
Designer's framing: new workspace admins; goal: first dashboard shared within
day 1; constraint: design-system components only. Questions: (1) Is the order
of steps right? (2) Does progress feel achievable?
Out of scope: illustration style (brand is revisiting it).

## Keeps
- Step 1 "Connect a data source" first — matches the goal's hard dependency.
- Progress shown as "2 of 5", not a percentage — concrete for small counts.

## Concerns
| # | Concern | Tied to | Tag | Priority | Raised by |
|---|---|---|---|---|---|
| C1 | "Invite teammates" is step 2, before anything exists to share | Goal: share within day 1 | goal-linked | High | PM |
| C2 | Dismiss "X" removes checklist with no way back | Admin user, recovery | convention (DS: dismissible panels restorable) | High | Eng |
| C3 | Step labels are nouns ("Sources") not actions | New admins | evidence-backed (last test: 3/5 unsure what to do) | Medium | Research |
| C4 | Card shadows feel heavy | — | taste | — | Design lead |

## Directions offered
C1: move invite after "Build first dashboard", or offer it inline on share.
C3: verb-first labels ("Connect a source").

## Stress test
"For the current order to be right, admins must invite people who build their
own dashboards." Research: most day-1 admins build alone → C1 stands.
"C4 rests only on preference" → parked.

## Decisions
| # | Decision | Owner | By | Research? |
|---|---|---|---|---|
| D1 | Reorder: invite after first dashboard | Designer | 09-27 | Yes — task in next usability test |
| D2 | Make checklist restorable from Help menu | Eng lead | 10-02 | No |
| D3 | Verb-first step labels | Designer | 09-27 | No (covered by C3 evidence) |

## Parked
C4 shadows (taste); illustration (out of scope).
```

## Techniques Used

- **OC-07 Operating Principles Declaration** — ground rules read at the start.
- **CM-03 Scope Definition** — designer's questions and out-of-scope areas fixed first.
- **ST-02 Structured Sequential Instructions** — clarify → works → concerns → directions.
- **DS-06 Prioritization and Severity Guidance** — concerns ranked by threat to the goal.
- **QA-02 Adversarial Stress-Test** — challenging the room's consensus before closing.

## Related Prompts

- `domain-data-analytics/experiments-and-reporting/analytics_dashboard_critique.md` — dashboard tile critique.
- `domain-frontend-development/design-direction/frontend_visual_design_direction_finder.md` — choosing a direction.
- `frontend_ux_heuristic_evaluation.md` — systematic inspection when a critique raises usability doubts.
