---
title: "Usability Findings Severity Log — One Problem Per Row, Rated by Impact × Frequency With the Sessions That Prove It"
category: frontend-development/ux-research
description: "Turn usability-session observations into a findings log in which each row is one interface problem, traced to the participants and tasks that showed it, rated on an explicit impact scale and a frequency count, combined into a severity, and linked to a recommendation — distinct from general interview synthesis (themes and decisions across a research programme) and from heuristic evaluation (expert-predicted problems with no users)."
techniques:
  - RT-05
  - DS-06
  - OC-03
  - QA-24
  - QA-04
difficulty: intermediate
tags:
  - ux-research
  - usability-testing
  - severity-rating
  - findings-log
  - prioritization
  - evidence
updated: "2026-09-24"
related_prompts:
  - domain-business-strategy/research/user_research_synthesis.md
  - domain-frontend-development/ux-research/frontend_ux_usability_test_plan.md
  - domain-frontend-development/ux-research/frontend_ux_heuristic_evaluation.md
---

# Usability Findings Severity Log

**Objective:** Produce a log the team can fix from: each usability problem
stated once, its evidence traceable to specific participants and tasks, and its
severity derived from a stated rule rather than from how memorable the session
was.

**When to Use:**
- A round of moderated or unmoderated usability sessions has just finished.
- Notes from several observers need merging into one list.
- The team is arguing about what to fix first and nobody has counted.

**Not this prompt if:**
- You are synthesising discovery interviews into themes, tensions, and
  strategy decisions → `domain-business-strategy/research/user_research_synthesis.md`.
  That prompt codes open conversation; this one rates task failures.
- You have no user sessions and want predicted problems → `frontend_ux_heuristic_evaluation.md`.
- The study has not run yet → `frontend_ux_usability_test_plan.md`.

## Inputs

1. **Session notes or recordings index**, per participant (P1…Pn), per task.
2. **The test plan**: tasks, success criteria, segments.
3. **Task outcome table** (success / partial / assisted / fail per participant).
4. **Observer notes**, if several people watched.

## Method

1. **Extract observations, not interpretations.** One line each: participant,
   task, timestamp, what they did or said. "P3 T2 12:40 scrolled past seat
   control twice, said 'where do I add people?'" — not "seats are confusing".
2. **Group observations into problems.** A problem is a property of the
   interface ("seat control sits below the fold on the plan step"). Several
   observations → one problem. One observation may support two problems.
3. **Rate impact (DS-06)** on a fixed scale:
   | Level | Definition |
   |---|---|
   | Critical | Participant could not complete the task, or completed it wrongly without knowing |
   | Serious | Completed only with significant delay, backtracking, or assist |
   | Minor | Brief hesitation or noticeable irritation; completed |
   | Cosmetic | Mentioned; no effect on behaviour |
4. **Count frequency.** Participants affected / participants who attempted the
   task — never divided by the whole sample if some did not reach the task.
5. **Combine into severity (RT-05)** with a stated rule, e.g.
   - Sev 1 (fix before release): Critical impact in ≥1 participant, or Serious in ≥ half
   - Sev 2 (fix next): Serious in fewer than half, or Minor in ≥ half
   - Sev 3 (backlog): Minor in fewer than half, or Cosmetic
   Report the rule with the log so the ranking can be challenged.
6. **Tabulate (OC-03)** with evidence IDs and a recommendation per problem.
   Recommendations state the direction, not the pixel solution.
7. **List candidates cleared (QA-24).** Observations that looked like problems
   and were not (participant misunderstanding of the test itself, prototype
   dead end, a single idiosyncratic remark) with the reason.
8. **State limits (QA-04).** Sample size, segments not covered, prototype
   fidelity effects.

## Output Format

```
# Usability findings — [study], [date], n=[..] ([segments])
Severity rule: [stated]

## Task outcomes
| Task | Success | Partial | Assisted | Fail | Attempted |

## Findings log
| ID | Problem (interface property) | Task(s) | Evidence (P#, timestamp) | Impact | Frequency | Severity | Recommendation | Confidence |

## Positive findings (keep)
## Cleared candidates
| Observation | Why it is not a finding |
## Limits of this round
## Re-test list
```

## Verification

- [ ] Each problem is phrased as an interface property, not a user trait.
- [ ] Every row cites participant IDs and a task.
- [ ] Frequency denominators equal participants who attempted that task.
- [ ] Severity follows the stated rule; any override is justified in the row.
- [ ] Assisted completions are not counted as successes.
- [ ] At least one cleared candidate is recorded.

## False-Positive Prevention

1. **The most vivid session is not the most frequent problem.** Count before
   ranking; a memorable quote from one participant is still n=1.
2. **"Users are confused" is not a finding.** Name the element and the
   behaviour that shows the confusion.
3. **Prototype dead ends are not usability problems.** Log them separately.
4. **Opinions about visual style are not usability problems** unless they
   changed behaviour; record them as comments.
5. **Low frequency does not mean low severity.** One participant unknowingly
   buying the wrong plan outranks five mild hesitations.
6. **Do not convert small-n counts into percentages that imply precision.**
   Report "4 of 6", not "67%".
7. **Recommendations are not requirements.** A direction ("make proration
   visible before the pay button") leaves the design to designers.

## Example Output

```
# Usability findings — Team-plan checkout v4, 2026-10-08, n=6 (3 card, 3 invoice)
Severity rule: Sev 1 = Critical ≥1 or Serious ≥ half; Sev 2 = Serious < half
or Minor ≥ half; Sev 3 = otherwise.

## Task outcomes
| Task | Success | Partial | Assisted | Fail | Attempted |
|---|---|---|---|---|---|
| T1 add seats | 3 | 1 | 2 | 0 | 6 |
| T2 explain charge | 1 | 3 | 0 | 2 | 6 |
| T3 invoice billing | 4 | 0 | 1 | 1 | 6 |

## Findings log
| ID | Problem | Task | Evidence | Impact | Freq | Sev | Recommendation | Conf |
|---|---|---|---|---|---|---|---|---|
| F1 | Seat control below the fold on the plan step | T1 | P1 04:10, P3 12:40, P5 06:02 | Serious | 3/6 | 1 | Bring seat count into the first viewport | High |
| F2 | Proration line reads as a recurring charge | T2 | P2 18:30, P4 15:12 (both said "every month?") | Critical | 2/6 | 1 | State "today only" and next-renewal amount together | High |
| F3 | Invoice option sits inside a collapsed "More" menu | T3 | P6 22:05 (fail), P4 20:40 (assist) | Critical | 2/3 invoice | 1 | Show payment-method choice unfolded for team plans | Medium |
| F4 | "Seats" vs "members" used interchangeably | T1 | P2, P5 remarks | Minor | 2/6 | 3 | Pick one term | Medium |

## Positive findings
All 6 read the confirmation summary correctly; keep its layout.

## Cleared candidates
| Observation | Why not |
|---|---|
| P3 could not edit company address | Known prototype dead end |
| P1 disliked the green button | Preference; no behavioural effect |

## Limits
n=6; no mobile participants; prices were static, which may understate F2.

## Re-test list
F1, F2, F3 after fixes; add a mobile segment.
```

## Techniques Used

- **RT-05 Evidence-Based Reasoning** — each row cites participants and timestamps.
- **DS-06 Prioritization and Severity Guidance** — impact scale × frequency → stated rule.
- **OC-03 Markdown Table Specification** — one fixed log schema.
- **QA-24 Dismissed-Candidates Coverage Table** — cleared observations with reasons.
- **QA-04 Uncertainty Acknowledgment** — small-n counts and fidelity limits.

## Related Prompts

- `domain-business-strategy/research/user_research_synthesis.md` — interview-level synthesis.
- `frontend_ux_usability_test_plan.md` — the plan that defines tasks and success.
- `frontend_ux_heuristic_evaluation.md` — expert-predicted problems to confirm with users.
