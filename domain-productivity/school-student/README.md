# School Student Productivity Prompts

Prompts for students managing academic workload — studying, scheduling, assignment tracking, semester planning, reading triage, and note organization. These prompts are practical and specific: they produce concrete plans tied to the student's actual material, deadlines, and constraints, not generic study advice.

---

## Prompt Directory

| File | Purpose | When to Use |
|------|---------|-------------|
| `student_study_schedule_builder.md` | Build a day-by-day study schedule for one exam or deadline, distributing specific material across specific time windows | 1–3 weeks before an exam; when the student needs a plan, not just an intention |
| `student_exam_prep_plan.md` | Design a three-phase learning strategy (Coverage → Practice → Review) for an exam, matched to exam type and past prep mistakes | When the student needs more than a schedule — they need a learning approach |
| `student_assignment_tracker.md` | Prioritize multiple simultaneous assignments into a this-week action plan, accounting for deadlines, effort, dependencies, and current progress | When 3+ assignments compete for attention and it's unclear what to work on first |
| `student_semester_planner.md` | Map the full semester's major deadlines, load levels, and high-intensity clusters onto a strategic calendar | First 1–2 weeks of semester; also useful mid-semester when the student has lost sight of the full picture |
| `student_reading_list_prioritizer.md` | Triage an assigned reading list into must-read, skim, and skip tiers when there is more material than time | Before an exam or deadline when the reading list is longer than available time allows |
| `student_note_organization_system.md` | Design a personalized note capture, filing, review, and pre-exam consolidation system for a student's specific tools and pain points | At the start of a semester, or when current notes are disorganized, unreviewed, or not helping on exams |

---

## When to Use This Directory vs. Others

**Use `school-student/` when:**
- The user is a student managing academic tasks (studying, assignments, reading, notes)
- The task is tied to a specific course, exam, or semester
- The goal is a concrete plan or system for academic work

**Use `domain-productivity/deep-work/` when:**
- The focus challenge is general (not academic-specific)
- The student needs help with focus, calendar blocking, or context-switching across any domain
- Relevant crossovers: `deepwork_decompose_complex_task.md` for breaking down a large assignment, `deepwork_chunk_project_to_calendar.md` for scheduling large projects

**Use `domain-productivity/bottlenecks/` when:**
- The student is stuck or procrastinating but the cause is unclear
- The problem is at the level of systems, not scheduling (e.g., capture system is broken, perfectionism is preventing submission)

**Use `domain-productivity/reviews/` when:**
- The student needs a weekly or monthly review of their overall productivity system, not specifically academic tasks

**Use `domain-personal-development/prompts/agency/` when:**
- The student is stuck on execution rather than planning (can't start, keeps planning instead of doing)
- Relevant: `agency_next_action_spec.md` for identifying the next concrete action, `agency_stuck_diagnosis.md` for diagnosing why they can't start

---

## Typical Use Sequences

**Start of semester:**
`student_semester_planner.md` → `student_note_organization_system.md`

**Approaching an exam (2–3 weeks out):**
`student_study_schedule_builder.md` → `student_exam_prep_plan.md`

**Overwhelmed by multiple deadlines:**
`student_assignment_tracker.md` → (if reading backlog is also a problem) `student_reading_list_prioritizer.md`

**Notes are a mess and aren't helping on exams:**
`student_note_organization_system.md` → `student_reading_list_prioritizer.md` (for reading-heavy courses)
