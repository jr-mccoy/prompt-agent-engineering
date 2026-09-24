---
title: "Playtest Protocol and Feedback Synthesis"
category: game-development/testing
description: "Run a playtest that answers design questions rather than collecting opinions: decision-linked research questions, participant profile, an observation protocol that separates what players did from what they said, telemetry to capture, and a synthesis that counts evidence and assigns confidence by sample — distinct from the QA gameplay test plan (does the feature work as specified) and from web/app usability studies."
techniques:
  - SV-03
  - RT-05
  - DS-06
  - QA-04
difficulty: intermediate
tags:
  - playtesting
  - user-research
  - feedback-synthesis
  - game-design
  - telemetry
  - player-experience
  - too-much-feedback
  - one-loud-tester
  - beta-testers
updated: "2026-09-24"
related_prompts:
  - domain-game-development/testing/testing_gameplay_test_plan.md
  - domain-frontend-development/ux-research/frontend_ux_usability_test_plan.md
  - domain-frontend-development/ux-research/frontend_ux_usability_findings_severity_log.md
---

# Playtest Protocol and Feedback Synthesis

**Objective:** Design a playtest around the design decisions it must inform, then
turn sessions into findings that distinguish behaviour from opinion, count how
many players showed each problem, and say how confident the team can be.

**When to Use:**
- A build is ready for outside players and the team wants more than "it was fun".
- Feedback is piling up in Discord, forms and notes with no way to weigh it.
- The team disagrees about whether a problem is real or one loud tester.

**When NOT to use:**
- Verifying that a feature behaves as specified (bugs, edge cases, regressions) —
  `testing_gameplay_test_plan.md`. That plan asks "does it work?"; a playtest is
  distinct because it asks "does the player experience what we intended?"
- Usability of a website or app UI — `domain-frontend-development/ux-research/`
  (`frontend_ux_usability_test_plan.md`, then `frontend_ux_usability_findings_severity_log.md`).
  Games differ: challenge and confusion look alike, and "hard" can be the goal.
- Large-scale live telemetry analysis — `domain-data-analytics/`.

## Inputs

1. **Build and scope**: which part of the game, how long a session lasts.
2. **Design questions**: what the team will decide based on this test.
3. **Intended experience** for the section: what players should feel and learn.
4. **Participants available**: count, recruiting source, genre familiarity.
5. **Telemetry available**: deaths, time per section, input usage, quit points.
6. **Raw material** (for synthesis): notes, recordings, survey answers, telemetry.

## Method

1. **Write research questions tied to decisions (SV-03).** "Do players learn the
   dash-cancel in run 1? If < 50% do, we add a tutorial prompt." A question with no
   decision attached is dropped.
2. **Define the participant profile.** Target players vs fresh eyes vs lapsed;
   exclude developers, friends of the team, and anyone who played the last build
   unless the question is about returning players.
3. **Write the session protocol.** Minimal intro (no mechanics explained unless the
   game would); silent observation or think-aloud (pick one, state why); what the
   observer records with timestamps; when the observer may intervene (soft-lock
   only); post-session questions, open before closed.
4. **Specify telemetry.** Per research question, the event that answers it.
5. **Synthesise by evidence type (RT-05).** For every note, tag it **Observed**
   (behaviour seen or logged), **Said** (player statement), or **Inferred**
   (observer interpretation). Findings rest on Observed; Said explains; Inferred
   is labelled.
6. **Count and prioritise (DS-06).** Each finding: n showing it / N, severity
   (blocks progress / degrades intended experience / cosmetic), and whether it
   hits the intended experience.
7. **State confidence by sample (QA-04).** With N ≤ 12, report counts, not
   percentages of the population; a finding seen in 1–2 players is a lead, not a
   conclusion.

## Output Format

```
## Protocol     — research questions → decision; participants; session script; telemetry
## Findings     — table: # | finding | evidence (Observed/Said) | n/N | severity | confidence
## Player-proposed fixes — listed separately from findings
## Decisions    — per research question: answer, decision, what would change it
## Next test    — what the next round must check
```

## Verification

- [ ] Every research question names the decision it informs.
- [ ] Every finding has at least one Observed item; Said-only items are labelled.
- [ ] n/N counts match the session notes; no participant counted twice for one finding.
- [ ] Player-suggested solutions are separated from the problems they point at.
- [ ] Each research question has an answer, including "inconclusive".

## False-Positive Prevention

1. **Players are right about problems and often wrong about solutions.** "Make the
   boss easier" is evidence that something hurts; the fix may be a clearer tell.
2. **Difficulty complaints are not automatically defects.** Check against the
   intended experience; frustration at an intended wall, followed by success, may
   be the design working.
3. **One articulate tester is n = 1.** Weight by how many showed the behaviour, not
   by how vividly one described it.
4. **Do not report percentages as population rates.** 7 of 12 is 7 of 12.
5. **Developer and friend testers do not count toward target-player findings.**
   Report them separately if used at all.
6. **Observer hints contaminate the finding.** If the observer explained a
   mechanic, exclude that participant from the related question.
7. **Silence is not satisfaction.** No complaint about the shop means nothing
   unless telemetry shows it was used.

## Example

**Input:** Roguelite "Ember Vault", build 0.14, first hour. N = 12 (8 genre
players, 4 lapsed). Silent observation, 60-minute sessions, telemetry on.

```markdown
## Protocol
| RQ | Question | Decision if… | Telemetry |
|---|---|---|---|
| RQ1 | Do players use dash-cancel in run 1? | < 6 of 12 → add contextual prompt | dash_cancel events per run |
| RQ2 | Where do first-hour quits cluster? | any room with ≥ 3 quits → review | quit_room, session_end |
| RQ3 | Is the between-run shop understood? | < 9 of 12 buy → redesign entry | shop_open, purchase |
Observer intervenes only on soft-lock. Post-session: "What was hardest?" before the
5-point difficulty item.

## Findings
| # | Finding | Evidence | n/N | Severity | Conf. |
|---|---|---|---|---|---|
| F1 | Dash-cancel unused in run 1 | Observed: 0 events in run 1 for 7; 3 of those 7 found it by run 3 | 7/12 (4/12 never) | Degrades intended experience | High |
| F2 | "Too hard" concentrated at the Warden | Said: 5 said "too hard"; Observed: those 5 died to Warden 4.2× avg vs 1.5× for the other 7 | 5/12 | Degrades | Medium |
| F3 | Two players never noticed the shop | Observed: no shop_open; Said: "there's a shop?" | 2/12 | Degrades | Medium |
| F4 | Quit cluster in Room 6 (Warden) | Observed: 3 of 4 early quits in Room 6 | 3/12 | Blocks progress | Medium |

F2 and F4 are the same encounter: the difficulty complaint is local, not global.

## Player-proposed fixes (not findings)
- "Lower the Warden's health" (3 players) — points at F2; the evidence suggests
  the wind-up tell is missed, not that HP is too high.
- "Tutorial for dash" (1 player) — consistent with the RQ1 decision.

## Decisions
- RQ1: 5/12 used dash-cancel in run 1 (< 6) → add contextual prompt on first dash.
  Would change if a prompt-free fix (enemy that demands it) tests better.
- RQ2: Room 6 has 3 quits → review Warden tell and arena size before HP.
- RQ3: 10/12 bought something (≥ 9) → keep shop; add entry highlight for the 2.

## Next test
Round 2, N = 10 fresh genre players: re-measure RQ1 with prompt; Warden deaths
per player with new tell; confirm no new quit cluster.
```

## Techniques Used

- **SV-03 (Interview-to-Synthesis Pattern):** sessions gathered, then synthesised into decisions.
- **RT-05 (Evidence-Based Reasoning):** Observed / Said / Inferred tagging on every note.
- **DS-06 (Prioritization and Severity Guidance):** severity by effect on progress and intended experience.
- **QA-04 (Uncertainty Acknowledgment):** counts not rates; confidence by sample size.

## Related Prompts

- `domain-game-development/testing/testing_gameplay_test_plan.md` — QA verification of intended behaviour.
- `domain-frontend-development/ux-research/frontend_ux_usability_test_plan.md` — study design for app UIs.
- `domain-frontend-development/ux-research/frontend_ux_usability_findings_severity_log.md` — severity logging method.
