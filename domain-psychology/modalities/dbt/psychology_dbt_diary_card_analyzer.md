---
title: "DBT Diary Card Analyzer (Weekly Review)"
category: psychology/modalities/dbt
description: "Process a week of DBT diary cards: target hierarchy review, skills use, urges/behaviors, emotion ratings, and produce a session agenda following Linehan's target hierarchy."
techniques:
  - ST-04
  - RT-02
  - DT-02
  - ED-04
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - DBT
  - diary-card
  - target-hierarchy
  - Linehan
  - skills-tracking
  - therapy-interfering-behavior
intended_use: model-testing
updated: "2026-05-19"
related_prompts:
  - domain-psychology/modalities/dbt/psychology_dbt_chain_analysis.md
  - domain-psychology/modalities/dbt/psychology_dbt_target_hierarchy_session_organizer.md
  - domain-psychology/risk-crisis/psychology_stanley_brown_safety_plan.md
---

# DBT Diary Card Analyzer (Weekly Review)

## Objective

Process a week's diary card data and produce a structured weekly review: target hierarchy classification, skills use audit, behavior/urge trends, emotion patterns, treatment-interfering behaviors (TIB), and a draft session agenda ordered by Linehan's target hierarchy.

## When to Use

- Standard adherent DBT (Linehan's stage 1) — individual therapy, weekly review.
- Adolescent DBT with developmentally adapted cards.
- IOP / PHP DBT programs reviewing daily cards at team or individual contact.
- Telehealth: client submits photo/scan in advance; reviewed at session start.
- Not appropriate for non-adherent DBT or DBT-informed therapy without skills training, where target hierarchy may not apply.

## Inputs / Context

- Diary card image, scan, or transcribed week (Mon–Sun, or 7-day rolling).
- Card columns minimally: urges (suicide, self-harm, substance, quit-therapy), behaviors (acted on / did not), emotions (sadness, anger, fear, joy, shame on a 0–5 scale), skills used (per Linehan code), homework practice.
- Target hierarchy in current contract: (1) life-threatening behaviors, (2) therapy-interfering behaviors, (3) quality-of-life-interfering behaviors, (4) skill deficits.
- Current treatment-stage targets and treatment plan.
- Prior weeks' diary trends (for delta/trajectory).
- Coaching call usage and outcomes.
- Risk plan and current acuity.

## Constraints

### Must

- Classify every notable behavior into Linehan's target hierarchy and route to the agenda accordingly.
- If **life-threatening behavior** (suicide attempt, NSSI, urges with means access, suicidal ideation crossing prior thresholds) appears anywhere on the card, this becomes the **#1 agenda item regardless of what else is on the card**, and a chain analysis is scheduled.
- Identify **TIB**: skipped sessions, came late, did not fill the card, dropped out of skills group, refused homework, did not pay agreed fee — name each.
- Audit **skills use** by category (mindfulness, distress tolerance, emotion regulation, interpersonal effectiveness): count entries; note whether skills were used "in moment" or post-hoc.
- Note **coaching calls**: were they used skillfully (asking for help with a skill in the moment), or for problem-solving / crisis-management drift?
- Compare to prior weeks: trend on urges, behaviors, skills use, emotions.
- Produce a session agenda in target-hierarchy order with proposed time blocks.
- If diary card was not completed or partial, classify as TIB and include in agenda (do not paper over it).
- For minors / clients with cognitive impairment: adapted-card review with caregiver where appropriate.

### Must Not

- Do not let a client steer the agenda to a non-life-threatening preferred topic when life-threatening data is on the card.
- Do not minimize TIB ("you were busy, that's fine"); a missed card is data and gets agenda time.
- Do not score skills generously; if client wrote "used DEAR MAN" but the situation involved no interpersonal request, mark as misclassified or seek clarification.
- Do not infer skill use from "I felt better" — require named skill or noted attempt.
- Do not generate emotional analysis from a single entry; require pattern across the week.
- Do not skip risk re-screen when life-threatening behavior or urges are present.
- Do not finalize the agenda without leaving room for the client to add items at level 3 / 4 of the hierarchy.

## Instructions

1. Verify the card is complete; if not, classify as TIB and proceed.
2. Scan the card for **life-threatening** indicators (suicide urges/behaviors, NSSI, AOD use that endangers life, severe quality-of-life with imminence). Flag.
3. Scan for **TIB**: missed session/group, late, did not pay, did not fill the card.
4. Note **QOL-interfering behaviors**: relationships, work/school, housing, legal, financial, eating, sleep.
5. Audit skills use across the four modules.
6. Identify emotion patterns: peak / nadir, dominant emotion, mismatch between emotion and behavior.
7. Compare to prior weeks; flag trends.
8. Audit coaching-call use.
9. Build the session agenda in target-hierarchy order: life-threatening → TIB → QOL → skills, with time blocks.
10. Note: any chain analyses scheduled; risk-plan updates required; consultation-team item flags.

## Output Format

```
=== DBT WEEKLY DIARY CARD REVIEW ===
Client: [Initials/MRN]    Week of: [YYYY-MM-DD to YYYY-MM-DD]    Card completion: [N of 7 days complete]
Treatment stage: [1 / 2 / 3 / 4]    Current contract targets: [...]

LIFE-THREATENING BEHAVIORS / URGES
- Suicide ideation: [Days present; intensity range; means-access status]
- Suicide attempts: [N this week; date(s)]
- NSSI: [Behavior; frequency; severity; medical?]
- AOD: [Substance, amount, days used; danger level]
- Urges acted-on rate: [N acted / N total urges]
- Means access changes: [...]
- → Agenda priority: #1; chain analysis scheduled: [Y]

THERAPY-INTERFERING BEHAVIORS
- Missed/late sessions: [...]
- Skills group attendance: [...]
- Card completion: [...]
- Homework completion: [...]
- Coaching-call use pattern: [Appropriate / drift / not used / overused]
- Other (fee, communication): [...]
- → Agenda priority: #2 if no Level-1 items

QUALITY-OF-LIFE-INTERFERING BEHAVIORS
- Relationships: [...]
- Work / school: [...]
- Sleep: [...]
- Eating: [...]
- Housing / legal / financial: [...]
- → Agenda priority: #3

SKILLS USE AUDIT
- Mindfulness: [N entries; notable instances]
- Distress tolerance: [N; TIPP, ACCEPTS, IMPROVE — which?]
- Emotion regulation: [N; opposite action, check the facts, PLEASE]
- Interpersonal effectiveness: [N; DEAR MAN, GIVE, FAST]
- In-moment vs post-hoc: [Ratio]
- Misclassified / aspirational entries: [...]
- → Skill deficit candidates for module re-teach: [...]

EMOTION PATTERN
- Dominant emotion(s): [...]
- Peak day / context: [...]
- Mismatch between emotion and behavior: [...]
- Trend vs prior weeks: [...]

TREND vs PRIOR WEEKS
- Urges: [↑/↓/=]; Behaviors: [↑/↓/=]; Skills: [↑/↓/=]; Emotions: [...]

DRAFT SESSION AGENDA
1. [Life-threatening item] — [N min] — chain analysis: [Y/N]
2. [TIB item] — [N min]
3. [QOL item — by client priority] — [N min]
4. [Skills coaching / module review] — [N min]
Buffer / client-added items: [N min]

CONSULTATION-TEAM FLAGS
- [Item to bring to team: e.g., chronic NSSI not responding; iatrogenic burnout signal]

RISK / SAFETY
- Risk re-screen due / completed: [...]
- Safety plan update: [Y/N — what changes]
- Means access plan: [...]

DOCUMENTATION
- Trends to monitor next week: [...]
- Diary-card changes proposed: [...]
- Next session: [Date]
```

## Verification

- [ ] Card completeness scored; missed days flagged as TIB.
- [ ] Life-threatening behaviors / urges scanned and prioritized.
- [ ] TIB explicitly named; not minimized.
- [ ] Skills use audited; misclassified entries flagged.
- [ ] Emotion patterns analyzed across the week, not single entries.
- [ ] Trend vs prior weeks reported.
- [ ] Session agenda in Linehan's target-hierarchy order with time blocks.
- [ ] Chain analyses scheduled for life-threatening / serious TIB.
- [ ] Consultation-team items flagged.
- [ ] Risk re-screen and safety plan addressed.
- [ ] No fabricated entries; data sourced from the card.
