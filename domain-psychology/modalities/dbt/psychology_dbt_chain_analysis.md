---
title: "DBT Behavior Chain Analysis"
category: psychology/modalities/dbt
description: "Conduct a Linehan behavior chain analysis on a specific target behavior: vulnerability factors → prompting event → links (thoughts, sensations, actions, emotions) → problem behavior → consequences → solution analysis."
techniques:
  - ST-04
  - RT-02
  - DT-02
  - ED-04
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - DBT
  - chain-analysis
  - behavior-chain
  - Linehan
  - solution-analysis
  - missing-links-analysis
intended_use: model-testing
updated: "2026-05-19"
related_prompts:
  - domain-psychology/modalities/dbt/psychology_dbt_diary_card_analyzer.md
  - domain-psychology/modalities/dbt/psychology_dbt_target_hierarchy_session_organizer.md
  - domain-psychology/risk-crisis/psychology_self_harm_functional_assessment.md
---

# DBT Behavior Chain Analysis

## Objective

Conduct a Linehan-style behavior chain analysis (BCA) on a single specific target behavior. The analysis traces vulnerability factors and prompting event through the chain of links — thoughts, body sensations, emotions, urges, behaviors — culminating in the problem behavior and its consequences. It ends with a **solution analysis** that places alternative skillful behaviors at each link, and (when relevant) a **missing-links analysis** for skills the client did not use.

## When to Use

- Any life-threatening behavior on the diary card (suicide attempt, NSSI, urges that crossed a threshold).
- Any therapy-interfering behavior (missed session, dropped group, refused homework).
- Quality-of-life-interfering behaviors when chronic (binge, purge, fight with partner, missed work).
- Standard practice in stage-1 DBT individual therapy.
- Telehealth — feasible with shared screen or whiteboard.
- Not a substitute for risk assessment if behavior was suicidal — risk assessment first, then chain.

## Inputs / Context

- The target behavior, defined operationally (what, when, where, with whom, how long, how severe).
- Time anchor: the specific incident being analyzed.
- Diary card context for the day.
- Vulnerability factors in the prior 24–72 hours (sleep, food, illness, substances, conflict, anniversaries).
- Skills the client knows and skills practiced recently.
- Function the behavior served (for self-harm: relief, communication, self-punishment, reorientation, dissociation-end, signaling).
- Prior chains on the same behavior class (looking for patterns).
- Risk plan status; safety-plan adequacy.
- Reading level / cognitive considerations.

## Constraints

### Must

- Define the **problem behavior** operationally before starting; vague targets ("acted out") yield vague chains.
- Identify **vulnerability factors** in the 24–72 hours preceding (sleep < 6h, skipped meals, alcohol use, illness, conflict, anniversaries, medication changes).
- Identify the **prompting event** (PE) — the discrete trigger; distinguish PE from the broader context.
- Build the chain of **links** in fine grain: each link is one thought / sensation / emotion / urge / action. Granularity matters; "I got upset and self-harmed" is not a chain.
- Identify **emotions** at each link with intensity (0–100) where possible.
- Identify **consequences**: immediate (within hours), short-term (24 hr), long-term (days+). Include both reinforcing and aversive consequences honestly.
- For each link, conduct **solution analysis**: what skillful behavior would have shifted the chain? Match to client's known skills.
- For high-acuity behavior (suicide attempt, life-threatening NSSI), add a **missing-links analysis**: "What skill might have worked? Why didn't you use it? Did you not know it / not think of it / not believe it would help / not want to?"
- Conclude with **commitment**: which solution(s) is the client committing to try if the chain begins again?
- Document for consultation-team review when behavior is life-threatening or therapy-interfering.

### Must Not

- Do not let the client narrate the chain in story-form without granularity; reflect back specific links.
- Do not collapse multiple incidents into one chain; one specific incident.
- Do not let solution analysis become abstract ("use skills"); each proposed solution is specific (named skill, when, with what cue).
- Do not let invalidation enter ("you shouldn't have done that"); use Linehan's dialectical stance.
- Do not skip consequences — especially reinforcing consequences that maintain the behavior.
- Do not abandon the analysis when the client gets uncomfortable; coach through it (this is the work).
- Do not generate links the client did not report; mark as `[unclear — client to clarify]`.
- Do not assume function; ask.

## Instructions

1. Define problem behavior operationally; confirm with client.
2. Identify vulnerability factors in the 24–72 hours preceding.
3. Identify the prompting event with time anchor.
4. Walk forward link by link: "What happened next? Then what?" Capture thoughts, body sensations, emotions (with intensity), urges, actions. Granularity high.
5. Continue chain until problem behavior occurred and immediately after.
6. List consequences: immediate / short-term / long-term, reinforcing / aversive.
7. Solution analysis at each link: what skillful behavior could have changed the trajectory? Match to the client's skills library.
8. Missing-links analysis: for the skill(s) the client did know but did not use, why?
9. Commitment: which specific solution will the client try, with what cue, in the next 24–72 hours?
10. Document; flag for consultation team if life-threatening or therapy-interfering.

## Output Format

```
=== DBT BEHAVIOR CHAIN ANALYSIS ===
Client: [Initials/MRN]    Date of session: [YYYY-MM-DD]    Date of incident: [YYYY-MM-DD HH:MM]
Target classification: [Life-threatening / TIB / QOL]    Prior chains on this behavior: [N]

PROBLEM BEHAVIOR (operationally defined)
What: [...]    When: [...]    Where: [...]    With whom: [...]
Duration / severity: [...]
Function (client-reported): [Relief / communication / self-punishment / reorientation / other]

VULNERABILITY FACTORS (prior 24–72 hours)
- Sleep: [Hours]
- Food / hydration: [...]
- Substances: [...]
- Illness / pain: [...]
- Stressors / anniversaries: [...]
- Medication changes / missed doses: [...]
- Other: [...]

PROMPTING EVENT (discrete trigger)
[Specific event, time-anchored]

CHAIN OF LINKS (sequential, fine-grained)
Link 1: [Thought / sensation / emotion / urge / action]    Emotion+intensity: [...]
Link 2: [...]
Link 3: [...]
...
Link n: [Problem behavior occurs]
Link n+1: [Immediately after]

CONSEQUENCES
Immediate (minutes–hours):  Reinforcing: [...]    Aversive: [...]
Short-term (24 hours):       Reinforcing: [...]    Aversive: [...]
Long-term (days+):           Reinforcing: [...]    Aversive: [...]

SOLUTION ANALYSIS (per link)
Link [k] → Skill or skillful behavior: [Named skill, e.g., TIPP — cold water; opposite action — go for a walk]
Link [k+1] → [...]
[Continue for each link with a feasible alternative]

MISSING-LINKS ANALYSIS (if applicable)
- Skill that could have helped: [Name]
- Why not used:
  [ ] Didn't know it
  [ ] Didn't think of it
  [ ] Didn't believe it would help
  [ ] Did think of it but didn't want to use it
  [ ] Tried but it didn't work
- What to address: [Re-teach / cue / belief work / motivation]

COMMITMENT (next 24–72 hours)
- Specific solution: [...]
- Cue: [What will tell the client to use it]
- Backup if it fails: [...]

CONSULTATION-TEAM ITEM
[Y/N — what to bring]

RISK / SAFETY
- Risk re-screen completed: [Y; outcome]
- Safety plan adequacy: [Adequate / needs update — specifics]
- Means restriction status: [...]
- Coaching-call availability reaffirmed: [...]

CLINICIAN NOTES
- Patterns vs prior chains: [...]
- Hypothesized function update: [...]
- Next session: [Date]
```

## Verification

- [ ] Problem behavior operationally defined; single incident.
- [ ] Vulnerability factors (24–72 hr) documented.
- [ ] Prompting event identified and time-anchored.
- [ ] Chain links are granular (thought / sensation / emotion / urge / action), not narrative.
- [ ] Emotions named with intensity where possible.
- [ ] Consequences cover immediate, short, and long term — including reinforcing.
- [ ] Solution analysis at each link with named skills.
- [ ] Missing-links analysis conducted for life-threatening / TIB chains.
- [ ] Specific 24–72-hour commitment captured.
- [ ] Consultation-team flag set when warranted.
- [ ] Risk assessment and safety-plan adequacy addressed.
- [ ] No fabricated links; gaps marked `[client to clarify]`.
