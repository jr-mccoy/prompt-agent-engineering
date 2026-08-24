---
title: PACU Orientation — Day 1 Welcome Packet
category: pacu/orientation-curriculum
task_type: CREATE
audience: PACU educator, lead preceptor, or unit manager preparing a new orientee's first day
updated: "2026-05-15"
tags:
  - pacu
  - orientation
  - day-one
  - welcome
  - preceptor
techniques:
  - ST-01
  - ST-02
  - RT-02
  - ED-02
  - DS-06
difficulty: beginner
related_prompts:
  - prompts/pacu_orientation_curriculum_designer.md
  - prompts/pacu_orientation_first_week_plan.md
  - prompts/pacu_orientee_question_log_builder.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
---

# PACU Orientation — Day 1 Welcome Packet

> Safety reminder: Day-1 content only — not a substitute for facility orientation program checklists. Use alongside the facility's mandatory unit-onboarding documents.

## Objective

Produce a **Day-1 welcome packet** the orientee receives at the start of their first shift. The packet orients them to the unit, the team-by-role, the day's expectations, and what counts as a successful Day 1 — without trying to teach clinical content. Psychological-safety framing is explicit.

## Inputs

- **Orientee background:** {{new-grad RN | experienced RN | etc.}}
- **Shift hours for Day 1:** {{e.g., 0700–1530, 0900–1730 short shift}}
- **Primary preceptor's name will be:** {{role placeholder — the packet uses role, not name}}
- **Facility-specific items NOT to fabricate:** {{user can paste in actual facility items like badge access, parking, scrub color — otherwise leave as placeholders}}
- **Known restrictions:** {{e.g., orientee cannot yet pull medications, has not completed EHR training, etc.}}

## Audience / Scope

- **Primary:** New PACU orientee on Day 1.
- **Secondary:** Lead preceptor and unit educator (for review before printing).
- **Scope:** Day 1 of orientation only. Day-by-day Week-1 content lives in `pacu_orientation_first_week_plan.md`.

## Output requirements

```markdown
# Welcome to PACU — Day 1

> You are not expected to know anything clinical today. Today is about meeting the unit. Asking questions is the assignment.

## Today at a glance

| Time block | What's happening |
|---|---|
| Arrival → first 30 min | Unit tour with primary preceptor; meet the day's team; orient to bay layout, supply closet, med room, code cart |
| First 2 hours | Shadow primary preceptor through admission(s); no hands-on yet unless preceptor invites |
| Mid-shift | Lunch + 1:1 with primary preceptor — first questions logged |
| Afternoon | Shadow handoffs in and out of PACU; orient to discharge workflow |
| Last 30 min | End-of-day debrief: 3 questions, 1 observation, 1 thing that surprised you |

## Who you'll meet (by role)

- **Primary preceptor:** your main pairing for orientation.
- **Charge nurse:** runs bay assignments, flow, and escalations on the shift.
- **CRNAs / anesthesiologists:** bring the patient from OR, receive escalations.
- **Surgical teams:** rotate through; you will get to know them by service.
- **Respiratory therapist:** owns vent + BiPAP/CPAP + difficult airway support.
- **Pharmacy:** consult line for med questions; specific reach-by-role per facility.
- **Other PACU RNs and techs:** your team — names will come; roles first.

(The packet uses roles, not names. Facility may insert names at print time.)

## What "successful Day 1" looks like

You will have a successful Day 1 if you:
- Met your primary preceptor and the day's charge nurse.
- Walked the bay layout and located: code cart, intubation cart, supply room, med room, sharps disposal, BiPAP setup, suction setup, emergency oxygen.
- Watched at least one OR-to-PACU handoff (inbound) and one PACU-to-floor handoff (outbound).
- Asked at least 5 questions, logged in your question journal (see `pacu_orientee_question_log_builder.md`).
- Noticed at least one thing that surprised you.

Notice: clinical performance is not on this list. That starts later.

## What today is *not*

- Not a clinical test. You will not be assessed on clinical decisions today.
- Not a memory exam. Names, room numbers, and protocols will accumulate over weeks; no one expects them today.
- Not a silent observation day. Ask everything that occurs to you. The list is the deliverable.

## Practical things to bring / wear

- {{Scrub color / badge / footwear — per facility}}
- A notebook or phone notes app for your question log
- Snacks; PACU shifts are unpredictable
- Water bottle; nurses chronically under-hydrate

## How to ask for help today

- For anything clinical: ask your primary preceptor first.
- For anything logistical (parking, badge, lockers): ask the charge nurse or unit educator.
- For anything that feels off (you don't know what to do, you're overwhelmed): say so. That is what today is for.

## End-of-day debrief (orientee fills in)

| Prompt | Your note |
|---|---|
| One thing I saw and want to understand | |
| One thing that surprised me | |
| One question I want to start tomorrow with | |
| One person whose role I want clearer | |
| How I'm feeling, in one sentence | |

(This goes to the primary preceptor; not graded; feeds the start-of-Day-2 conversation.)

## Sources / reference

- ASPAN *Standards of Perianesthesia Nursing Practice* — orientation context only, not cited as clinical authority on Day 1.
- Facility orientation program — for all unit-specific items (badge, parking, mandatory training).
```

## Must / Must not

**Must:**
- Frame Day 1 as relationship + orientation, not clinical performance.
- Make "asking questions" the explicit success metric.
- Use role-only references for all people (CRNA, charge, surgeon, RT, pharmacy).
- Include the end-of-day debrief section.
- Keep the packet ≤ 2 pages when printed.

**Must not:**
- Include any clinical protocol, dose, or threshold.
- Specify named individuals.
- Specify facility-specific items unless the user pasted them in (otherwise placeholder).
- Project anxiety onto the orientee ("you'll probably feel overwhelmed") — describe what's true, don't project feelings.
- Imply clinical evaluation begins on Day 1.

## Quality signals

- An orientee reading this on the train in could arrive feeling oriented to the social and physical landscape, with permission to ask basic questions.
- A primary preceptor reading it could use it as the Day-1 agenda without further prep.
- A nurse manager reading it would not see anything that contradicts the facility orientation program.

## Verification

- [ ] No clinical content (no doses, thresholds, protocols).
- [ ] All people referenced by role.
- [ ] Success-metrics list does not include clinical performance.
- [ ] End-of-day debrief is structured and orientee-fillable.
- [ ] ≤ 2 pages when printed.
- [ ] Safety reminder + FPP sections present.

## False-Positive Prevention

- **No invented facility specifics** (badge color, parking location, scrub color, locker assignment, mandatory training list). Placeholder or leave to facility insertion.
- **No invented staff names** anywhere.
- **No invented escalation phone numbers, pagers, or codes.**
- **No invented clinical protocols** ("at our facility, post-op pain is managed by …"). Day 1 is not for protocol content.
- **No fabricated psychological-state assertions** about the orientee.
- **No protected-characteristic references.**

## Worked Example

<details>
<summary>Example: new-grad RN, 0700–1530 first shift (click to expand)</summary>

```markdown
# Welcome to PACU — Day 1

> You are not expected to know anything clinical today. Today is about meeting the unit.

## Today at a glance

| Time | What's happening |
|---|---|
| 0700–0730 | Bay tour with primary preceptor; meet charge RN; locate code cart, med room, supply room. |
| 0730–0930 | Shadow primary preceptor for first OR-to-PACU handoff; no hands-on. |
| 0930–1130 | Continue shadowing admissions; watch primary preceptor's admit workflow end-to-end at least twice. |
| 1130–1200 | Lunch + first 1:1 with primary preceptor — log your first questions. |
| 1200–1430 | Shadow discharge handoffs (PACU-to-floor + PACU-to-ambulatory). |
| 1430–1500 | End-of-day debrief with primary preceptor — use the table below. |
| 1500–1530 | Wrap-up: question log saved; tomorrow's start time confirmed. |

## What "successful Day 1" looks like

- Met primary preceptor and charge RN.
- Walked the bay and found: code cart, intubation cart, med room, supply, sharps, BiPAP, suction, O₂.
- Watched one OR-to-PACU handoff and one PACU-to-floor handoff.
- Logged at least 5 questions.
- Noticed at least one surprise.

## End-of-day debrief

| Prompt | Your note |
|---|---|
| One thing I saw and want to understand | |
| One thing that surprised me | |
| One question to start tomorrow with | |
| One role I want clearer | |
| How I'm feeling, in one sentence | |
```

Notes on Tier 1 quality: relationship-first framing, role-only references, asking-questions as the success metric, no clinical content, debrief is fillable.
</details>

## Self-check

- [ ] No clinical content.
- [ ] Roles only, no names.
- [ ] Asking questions is the deliverable.
- [ ] ≤ 2 pages.
- [ ] Debrief table present.
- [ ] FPP section passed.
