---
title: "Bug Bounty Skill-Development Plan"
category: bug-bounty/learning
description: "Build a measurable, time-boxed skill-development plan for bug bounty hunting: deliberate practice in safe labs, reading disclosed reports, and a progression from labs to live findings"
techniques:
  - ST-01
  - ST-02
  - DS-06
  - ED-01
  - DD-07
difficulty: beginner
tags:
  - bug-bounty
  - skill-development
  - deliberate-practice
  - learning
  - labs
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_getting_started_orientation.md
  - domain-software-engineering/bug-bounty/bugbounty_report_postmortem.md
  - domain-software-engineering/bug-bounty/bugbounty_access_control_idor_hunt.md
---

# Bug Bounty Skill-Development Plan

**Objective:** Turn "I want to get good at bug bounties" into a measurable, time-boxed plan that builds skill where mistakes are safe (labs, CTFs, disclosed-report study) and graduates to live, in-scope hunting — so progress compounds instead of being random.

## When to Use
- You're new (or plateaued) and want a structured practice plan, not just "go find bugs."
- You have a fixed weekly time budget and want to spend it on the highest-growth activities.
- You want to build depth in one vuln class before spreading across many.

## Inputs / Context
- **Your current skills** (languages, web/API/mobile/cloud familiarity, any security background).
- **Time budget** (hours/week) and **horizon** (e.g., 12 weeks).
- **Target vuln class(es)** you want to specialize in first.

## Instructions

1. **Authorization/safety note.** All practice happens on **deliberately-vulnerable training infrastructure, CTFs, or in-scope program assets** — never on systems you aren't authorized to test. The plan must respect this boundary.

2. **Pick a beachhead class** to specialize in first (depth beats breadth early). Match it to the user's background (e.g., web/API dev → broken access control / IDOR; someone who likes puzzles → business logic).

3. **Define the deliberate-practice loop** for that class: study the mechanism → solve graded labs → read 3–5 *disclosed* real-world reports of that class → attempt the class on a live in-scope program → debrief each attempt. Reading disclosed reports is one of the highest-ROI activities — it teaches what real bugs and good reports look like.

4. **Set measurable milestones** with checkable outputs, not vague goals (e.g., "solve the access-control lab set," "summarize 5 disclosed IDOR reports," "submit one report"). Each milestone should be pass/fail.

5. **Allocate the weekly budget** across study / labs / report-reading / live hunting / debrief, weighted toward hands-on. Adjust to the user's hours.

6. **Plan the graduation** from labs → live: when to start applying skills on a real program, and how to use the hunting prompts in this directory for each session.

7. **Build a feedback mechanism:** a simple log of attempts, what was tried, outcomes, and lessons (feeds `bugbounty_report_postmortem.md`). Skill compounds through reflection, not raw hours.

8. **CRITICAL — verify the plan is realistic and measurable:**
   - Confirm every milestone has a concrete, checkable output (not "understand X").
   - Confirm the weekly hours sum to the user's actual budget and are hands-on-weighted.
   - Confirm all practice targets are safe/authorized (labs, CTFs, in-scope assets).
   - Confirm the plan builds depth in one class before breadth.

## False-Positive Prevention (MUST follow)
- ❌ Do NOT set vague milestones ("get better at XSS") — every milestone must be checkable.
- ❌ Do NOT suggest practicing on any non-authorized live site; only labs/CTFs/in-scope assets.
- ❌ Do NOT front-load passive study; weight the plan toward hands-on practice and report-reading.
- ❌ Do NOT spread a beginner across five vuln classes at once — depth first.
- ✅ DO make milestones pass/fail with concrete outputs.
- ✅ DO budget by the user's real hours, hands-on-weighted.
- ✅ DO include disclosed-report reading as a core activity.

## Output Format
```
## Beachhead Class & Why
[Class + fit to background]

## Weekly Budget Allocation (total = user's hours)
| Activity | Hours | Why |

## Deliberate-Practice Loop
[Study → labs → disclosed reports → live attempt → debrief]

## Milestones (checkable)
| Week(s) | Milestone | Pass/fail output |

## Graduation to Live
[When + how, which hunting prompts per session]

## Feedback Log Format
[Fields to track per attempt]

## Self-Audit
[All milestones checkable; hours = budget; targets authorized; depth-first]
```

## Example Output
```
## Beachhead Class & Why
Broken access control / IDOR — matches your Node/REST background; high frequency + high payout; provable
with two test accounts.

## Weekly Budget Allocation (total = 6h)
| Activity | Hours | Why |
|----------|-------|-----|
| Labs (access-control sets) | 2.5 | hands-on skill core |
| Disclosed-report reading | 1.5 | learn real bugs + report style |
| Live in-scope hunting | 1.5 | apply on a real program |
| Debrief/log | 0.5 | compounding via reflection |

## Deliberate-Practice Loop
Study the access-control model → solve the lab set → read 5 disclosed IDOR/BOLA reports and summarize the
pattern → run bugbounty_access_control_idor_hunt.md on your live program → log what worked/failed.

## Milestones (checkable)
| Week(s) | Milestone | Pass/fail output |
|---------|-----------|------------------|
| 1-2 | Access-control lab set solved | all labs green |
| 2-3 | 5 disclosed reports summarized | a notes file with the 5 patterns |
| 4-6 | First recon + scope analysis on live program | attack-surface map + test plan |
| 7-10 | First access-control attempt + report | one submitted report |
| 11-12 | Debrief + pick second class | postmortem + next-class decision |

## Graduation to Live
After the lab set + report summaries (≈week 3), start live hunting on your chosen program. Per session:
scope analyzer → recon → access-control hunt → triage → (if GO) severity → PoC → report.

## Feedback Log Format
Date · Program · Endpoint · Hypothesis · What I tried · Outcome · Lesson · Next step.

## Self-Audit
Every milestone has a concrete output; 2.5+1.5+1.5+0.5 = 6h (your budget), hands-on-weighted; all targets
are labs/disclosed reports/your in-scope program; depth-first on one class.
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — a measurable, time-boxed plan as the goal.
- **ST-02 (Structured Sequential Instructions)** — the study→labs→reports→live→debrief loop.
- **DS-06 (Prioritization Guidance)** — depth-first beachhead and hands-on-weighted budget.
- **ED-01 (Iterative Scaffolding)** — graduates the learner from safe labs to live hunting.
- **DD-07 (Self-Audit Table)** — verification enforces checkable milestones and authorized targets.
