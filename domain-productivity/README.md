# Domain: Productivity

**Purpose:** Prompts for individual execution: daily planning, deep work, operating cadence, reviews, automation, and decision validation.

---

## What This Domain Covers

Individual productivity and life-management prompts:

1. **Automation** - Workflow and browser automation, daily routines, weekly digests
2. **Bottlenecks** - Locating real personal constraints across clarity, execution, and distribution; procrastination diagnostics; capture/triage system design; perfectionism ship-threshold; PKM architecture
3. **Daily Planning** - Daily task list building, morning planning, EOD shutdown, priority triage, overwhelm triage, errand batching, context switching, energy-task matching
4. **Deep Work** - Personal focus-system audits, designs, reloads, environment friction, future-self handoffs, experiments, meeting and message load
5. **Goals & Habits** - Annual goal breakdown, habit stack design, monthly check-ins, goal reality checks, habit repair, personal tracking dashboards
6. **Home Life** - Meal planning, chore systems, family schedule coordination, appointment prep, seasonal home maintenance, decluttering, moving, travel planning
7. **Operating Cadence** - A self-directed chief-of-staff cadence: morning briefing, end-of-day reconciliation, weekly review, meeting prep, authority boundaries, delegating to AI sub-agents
8. **Reviews** - Time audit, weekly systems review, monthly/quarterly cadence, solo-dev weekly rhythm
9. **School & Student** - Study schedules, exam prep, assignment tracking, semester planning, reading triage, note organization
10. **Validation** - Decision validation, sanity checks, reasoning verification, confidence calibration
11. **Workplace** - Meeting agendas, status updates, follow-up emails, inbox triage, deadline juggling, task delegation, saying no, 1:1 prep

**Moved out of this domain:** the 17 AI-role readiness assessments now live in `domain-personal-development/prompts/career/`; the rapid app-prototyping prompts now live in `domain-software-engineering/prototyping/`; the content-quality "slop" detectors now live in `domain-professional-writing/content-quality/`.

---

## Directory Structure

```
domain-productivity/
├── automation/               # Workflow and browser automation, routines
├── bottlenecks/              # Personal constraint diagnostics
├── daily-planning/           # Daily task management, morning/EOD rituals, priority triage
├── deep-work/                # Personal focus systems
├── goals-habits/             # Goal breakdown, habit design, tracking, habit repair
├── home-life/                # Household and life management
├── operating-cadence/        # Self-directed chief-of-staff cadence
├── reviews/                  # Cadence-based productivity-system reviews
├── school-student/           # Student productivity: study, exams, assignments
├── validation/               # Decision and reasoning validation
├── workplace/                # General workplace workflows
└── README.md
```

---

## File Count

Counts are prompt files only: every `.md` in the subfolder except `README.md`.

| Subdirectory | Count | Description |
|--------------|-------|-------------|
| `automation/` | 11 | Daily accountability, data sync, form notifications, lead routing, weekly digest, content monitoring, automation-opportunity mining; browser-automation safety check, recording blueprint, multi-tab intel, weekly audit |
| `bottlenecks/` | 12 | Constraint locator, clarity/execution/distribution diagnostics, procrastination, capture/triage, open-loop audit, perfectionism ship-threshold, PKM, knowledge-base gaps, content audit, observation capture |
| `daily-planning/` | 9 | Task list builder, priority triage, morning planning, EOD shutdown, overwhelm triage, errand batching, context switching, energy matching, energy by task type |
| `deep-work/` | 23 | Focus parameters, calendar audit, focus and reload rituals, experiments, environment friction, future-self handoff, task decomposition and calendar chunking, meeting cost/killer/async conversion, message triage, energy and self-interruption audits |
| `goals-habits/` | 6 | Annual goal breakdown, habit stack design, monthly check-in, goal reality check, habit repair, personal tracking dashboard |
| `home-life/` | 13 | Meal planning, chore rotation, family schedule, appointment prep, seasonal maintenance, declutter, moving, travel, household paperwork, after-a-death admin, Medicare/insurance enrollment prep, family caregiving coordination, caregiver respite |
| `operating-cadence/` | 11 | Morning briefing, brain dump to tasks, fuzzy-goal clarification, meeting prep and pre-reads, end-of-day reconciliation, weekly review, authority boundaries, AI workflow architecture, sub-agent task specs, CLAUDE.md memory scaffold |
| `reviews/` | 4 | Time audit, weekly systems review, monthly/quarterly cadence, solo-dev weekly operating rhythm |
| `school-student/` | 6 | Study schedule, exam prep, assignment tracker, semester planner, reading triage, note organization |
| `validation/` | 11 | Adversarial mini-check, am-I-being-nuts, quick and full reality checks, final gate, disconfirmation pass, confidence calibration, audit boundary check, session/project ground rules, judgement assessment |
| `workplace/` | 8 | Meeting agendas, status updates, follow-up emails, inbox triage, deadline juggling, delegation, saying no to overcommitment, 1:1 prep |
| **Total** | **114** | |

---

## Key Patterns

### Daily & Everyday Task Management
- **Task List Builder** - Size a daily list to available hours with one MIT
- **Priority Triage** - Urgent/important quadrant for an overloaded list
- **Morning Planning** - 10-minute daily startup ritual
- **EOD Shutdown** - Close the day, set up tomorrow

### Home & Life Management
- **Meal Plan** - Weekly meals + consolidated grocery list
- **Chore Rotation** - Sustainable household task system
- **Family Schedule** - Coordinate multi-person household schedules
- **Travel Planner** - Three-artifact trip planner (planning, packing, departure)

### Student Productivity
- **Study Schedule** - Deadline-specific study block distribution
- **Exam Prep** - Three-phase preparation strategy
- **Semester Planner** - Strategic semester load map

### Workplace Workflows
- **Meeting Agenda** - Time-boxed agendas with named outcomes per item
- **Status Update** - Audience-calibrated project status writing
- **Inbox Triage** - Repeatable email decision protocol
- **1:1 Prep** - Manager and direct-report prep modes

### Goals & Habits
- **Annual Goal Breakdown** - Quarterly/monthly/weekly milestone cascade
- **Habit Stack Designer** - Anchor + cue + routine with 30-day starter plan
- **Habit Repair** - Diagnose and re-enter a broken habit

### Decision Validation
- **Adversarial Mini-Check** - Quick sanity check on decisions
- **Am I Being Nuts?** - Reality check for big decisions
- **Final Gate** - Pre-shipping verification
- **Disconfirmation Pass** - Look for the evidence that would prove you wrong

### Operating Cadence
- **Morning Briefing** - Start the day from a legible state
- **End-of-Day Reconciliation** - Close the loop between plan and reality
- **Authority Boundaries** - What a human or AI sub-agent may decide without you

---

## When to Use This Domain

Use these prompts when you need to:
- Figure out what to do today and in what order (`daily-planning/`)
- Manage household logistics: meals, chores, schedules, appointments (`home-life/`)
- Study for exams or manage academic workload (`school-student/`)
- Run workplace workflows: meetings, emails, status updates, delegation (`workplace/`)
- Build or repair a goal or habit system (`goals-habits/`)
- Audit and maintain your productivity systems (`reviews/`, `bottlenecks/`)
- Build deep work capacity and focus blocks (`deep-work/`)
- Validate a decision before committing (`validation/`)
- Run your own week like a chief of staff would (`operating-cadence/`)

**Do NOT use for:**
- Business strategy (use `domain-business-strategy/`)
- Engineering sprint planning or DevOps workflows (use `domain-engineering-workflows/`)
- Code development or technical analysis (use `domain-software-engineering/`)
- Career-level identity work or burnout (use `domain-personal-development/`)
- AI-role readiness assessments (use `domain-personal-development/prompts/career/`)
- Rapid app prototyping (use `domain-software-engineering/prototyping/`)

---

*Consolidated here from the retired pre-reorg `prompts/productivity/` tree, which no longer exists; the current files are the subfolders listed above.*
