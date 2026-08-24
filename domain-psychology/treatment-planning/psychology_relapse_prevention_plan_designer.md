---
title: "Relapse Prevention Plan Designer"
category: psychology/treatment-planning
description: "Design an end-of-treatment relapse prevention plan with individualized warning signs, high-risk situations, coping responses, and support contacts."
techniques:
  - DT-01
  - ST-04
  - DS-02
  - NE-10
  - CM-01
difficulty: intermediate
intended_use: model-testing
tags:
  - relapse-prevention
  - discharge-planning
  - treatment-planning
  - maintenance
  - high-risk-situations
  - coping-skills
updated: "2026-06-08"
related_prompts:
  - domain-psychology/treatment-planning/psychology_smart_treatment_goal_generator.md
  - domain-psychology/treatment-planning/psychology_golden_thread_writer.md
  - domain-psychology/treatment-planning/psychology_measurement_based_care_plan.md
  - domain-psychology/documentation/psychology_initial_treatment_plan.md
---

# Relapse Prevention Plan Designer

## Objective

Build a personalized, end-of-treatment relapse prevention plan (RPP) that the client leaves with as a usable document. The RPP translates the gains made in treatment into a forward-looking self-management guide: it names the early warning signs specific to this client, the high-risk situations most likely to trigger deterioration, the evidence-based coping skills the client has practiced, the support contacts available, and the decision rules for when and how to re-engage with care. The plan must be actionable, readable at the client's literacy level, and suitable for the clinical chart.

## When to Use

- In the final 2–4 sessions of a planned treatment episode, while the client is still engaged and gains are consolidated.
- When a client is transitioning from IOP or PHP to standard outpatient and the discharge plan requires a documented RPP.
- When a client is ending a treatment episode by choice or insurance limit and maintenance support needs to be scaffolded.
- When a client's history includes prior relapse and the current episode has addressed the relapse pattern specifically.
- When the clinician and client are reviewing the treatment arc and formalizing what was learned.

## Inputs / Context Required

- **Primary diagnosis and current clinical status**: diagnosis at discharge, current outcome measure scores, functional status.
- **Treatment gains summary**: what symptoms improved, what skills were learned, what maintaining factors were addressed.
- **Client-identified warning signs**: the client's own language for early signs that they are beginning to struggle (distinct from the clinician's clinical markers).
- **Identified high-risk situations**: specific circumstances, people, places, times, or emotional states that historically precede deterioration.
- **Coping skills practiced in treatment**: the specific techniques the client has used and found helpful. Name the skills with their technique name (e.g., "progressive muscle relaxation," "cognitive restructuring worksheet," "DBT TIPP skills").
- **Support system**: names and roles of people in the client's life who can provide support; community resources; crisis contacts.
- **Re-engagement threshold**: the client's agreed-upon criterion for returning to care (e.g., two consecutive weeks at PHQ-9 ≥ 10; any return of suicidal ideation; substance use after 90 days abstinence).
- **Preferred care access**: clinician contact for booster sessions, crisis line, emergency protocol.
- `[clinician input required: client's language for their warning signs — do not substitute clinical descriptors]`
- `[clinician input required: any safety considerations that modify the re-engagement threshold, e.g., prior high-lethality attempt]`

## Constraints

### Must

- Write the RPP in accessible language calibrated to the client's literacy level; avoid unexplained clinical jargon.
- Use the client's own words for warning signs wherever possible; append the clinical translation in parentheses if needed for chart purposes.
- Ground the high-risk situations in this client's actual history, not generic population risk lists.
- Name the specific coping skills the client has practiced, not general categories (e.g., "DEAR MAN practice for assertiveness with supervisor" not "communication skills").
- Include a three-tier response ladder: Early Warning (self-management), Moderate Warning (activate support system), Crisis (re-engage professional care).
- Specify at least one concrete action for each tier that the client can execute without clinician involvement.
- Include at least one named re-engagement criterion that is observable and specific.
- End with a maintenance schedule: what the client will do to maintain gains (e.g., monthly self-monitoring with PHQ-9, weekly check-ins with sponsor, daily mindfulness practice).

### Must Not

- Do not write the RPP for the client — the session process is collaborative and the output reflects joint authorship; flag any section completed without client input.
- Do not list coping skills the client has not practiced or found unhelpful; relevance to this client is required.
- Do not use the RPP to introduce new interventions the client was not taught during treatment.
- Do not omit crisis contacts or the re-engagement threshold; these are safety-critical components.
- Do not set a re-engagement threshold so high that the client would need to be in acute crisis before they were prompted to return; the threshold should catch early relapse, not late.
- Do not write the plan at a literacy level above the client's capacity to use it independently.

## Instructions

1. **Build the clinical status snapshot**: Document the discharge status — current outcome measure scores, functional status, and a brief description of progress achieved. This anchors the RPP's "starting from" point and provides the baseline for future self-comparison.

2. **Identify personal warning signs** (Three stages):
   - **Earliest signs** (Stage 1): Subtle changes that the client can notice before others do — changes in sleep, appetite, withdrawal, thought patterns, irritability, small behavioral shifts. Use client's own language.
   - **Moderate signs** (Stage 2): More visible deterioration — increased avoidance, functional decline, return of specific symptoms at mild-moderate severity.
   - **Crisis signs** (Stage 3): Signs indicating immediate re-engagement is needed — return of suicidal ideation, significant functional breakdown, substance use, harm to self or others.

3. **Map high-risk situations**: List the specific situations — not generic stressors — that have historically preceded deterioration for this client. For each, annotate: (a) why it is risky (the mechanism), (b) what has helped before.

4. **Build the coping skill toolbox**: List each skill with: (a) the named technique, (b) when to use it (which warning stage or situation type), (c) a brief instruction reminder. Organize by situation type or warning stage.

5. **Build the three-tier response ladder**:
   - **Tier 1 — Early Warning** (Stage 1 signs present): Self-management actions. What does the client do on their own? Which skills? Which behaviors? What does the client look for to know it's working?
   - **Tier 2 — Moderate Warning** (Stage 2 signs present): Activate support. Who do they contact? What do they say? What do they ask for? Include non-professional supports.
   - **Tier 3 — Re-engagement** (Stage 3 signs or Tier 2 not working): Contact clinician for booster sessions; activate crisis plan if needed. Include specific contacts and decision rule.

6. **Write the re-engagement criterion**: The client's personal "return to care" threshold. Write it in the client's language. Make it observable and specific.

7. **List support contacts**: Named individuals (role and contact method), community resources, clinician re-engagement contact, and crisis contacts.

8. **Design the maintenance schedule**: Month 1 through Month 6 post-discharge — what the client will do to monitor and maintain gains. Include: self-monitoring cadence (instrument + frequency), skill practice cadence, support contacts, and booster session plan if applicable.

9. **Run verification.**

## Output Format

```
=== RELAPSE PREVENTION PLAN ===
Client: [Initials]     Date prepared: [YYYY-MM-DD]     Clinician: [Name, credentials]

CLINICAL STATUS AT DISCHARGE
Diagnosis at discharge: [F##.##] [Descriptor]
Outcome measures at discharge:
  [Instrument]: [score] ([severity band]) — compared to baseline [score]
Functional status: [Brief description — work, relationships, self-care]
Key gains: [2–4 bullet points in plain language]

────────────────────────────────────────────────────────
MY WARNING SIGNS

Stage 1 — Early (I notice these first):
- "[Client's language]" [clinical translation if needed]
- "[...]"

Stage 2 — Building (others may start to notice):
- "[...]"
- "[...]"

Stage 3 — Re-engage now (act immediately):
- "[...]"
- "[...]"

────────────────────────────────────────────────────────
MY HIGH-RISK SITUATIONS

| Situation | Why it is risky (mechanism) | What has helped |
|-----------|----------------------------|-----------------|
| [Specific situation in client's language] | [Mechanism] | [Coping skill or action] |
| [...]     | [...]                      | [...]           |
| [...]     | [...]                      | [...]           |

────────────────────────────────────────────────────────
MY COPING SKILL TOOLBOX

| Skill | When to use | Quick reminder |
|-------|-------------|----------------|
| [Named technique — e.g., "5-4-3-2-1 grounding"] | [Stage 1 / Situation type] | [1–2 sentence how-to] |
| [Named technique] | [...] | [...] |
| [Named technique] | [...] | [...] |
| [Named technique] | [...] | [...] |
| [Named technique] | [...] | [...] |

────────────────────────────────────────────────────────
THREE-TIER RESPONSE LADDER

TIER 1 — EARLY WARNING (Stage 1 signs)
What I do on my own:
  1. [Specific action — e.g., "Use cognitive restructuring worksheet (CBT 7-column thought record)"]
  2. [...]
  3. [...]
How I know Tier 1 is working: "[Observable sign — e.g., 'PHQ-9 ≤ 9 after 1 week of Tier 1 actions']"
How I know I need to move to Tier 2: "[Observable sign — e.g., 'Still at Stage 2 warning signs after 2 weeks']"

TIER 2 — MODERATE WARNING (Stage 2 signs or Tier 1 not working)
Who I contact: [Name, role, contact method]
What I say: "[Script — e.g., 'I am noticing [warning sign] and I want to check in.']"
Community or peer support: [Group, sponsor, peer support line]
How I know Tier 2 is working: "[Observable sign]"
How I know I need to move to Tier 3: "[Observable sign or time limit]"

TIER 3 — RE-ENGAGE CARE (Stage 3 signs, or Tier 2 not working in [X] weeks)
Contact my clinician at: [Contact — phone / email / patient portal]
Message to send: "[Script — e.g., 'I need a booster session. I am noticing [sign].']"
If I cannot reach my clinician: [Crisis line — 988; local crisis line; ED]
If I am in immediate danger: 988 or go to nearest ED.

────────────────────────────────────────────────────────
MY RE-ENGAGEMENT CRITERION

"I will call for a booster session if: [Specific, observable criterion — e.g., 'my PHQ-9 is ≥ 10 on
two consecutive self-checks, OR any return of thoughts of suicide, OR I use [substance] after my
planned quit date.']"

────────────────────────────────────────────────────────
SUPPORT CONTACTS

| Name / Resource | Role | Contact |
|-----------------|------|---------|
| [Name] | [Relationship] | [Phone / method] |
| [Clinician name] | [Therapist / prescriber] | [Phone / portal] |
| [Community resource] | [Group / sponsor / peer] | [Contact] |
| 988 Suicide & Crisis Lifeline | Crisis | Call or text 988 |
| [Local crisis line] | Crisis | [Number] |

────────────────────────────────────────────────────────
MAINTENANCE SCHEDULE

Month 1:
  - Self-monitoring: [Instrument] weekly; bring to booster session or record in [method].
  - Skill practice: [Skill] [frequency].
  - Support contact: [Name/resource] [frequency].
  - Booster session: [Scheduled / available if needed].

Months 2–3:
  - Self-monitoring: [Instrument] every 2 weeks.
  - Skill practice: [Skill] [frequency].
  - Support contact: [frequency].

Months 4–6:
  - Self-monitoring: [Instrument] monthly.
  - Re-engage if: [Re-engagement criterion].

────────────────────────────────────────────────────────
SIGNATURES

Client: __________________________ Date: __________
Clinician: ________________________ Date: __________
Copy given to client: [ ] Yes    Copy in chart: [ ] Yes
```

## Verification

- [ ] Clinical status snapshot includes discharge outcome measure scores compared to baseline.
- [ ] Three-stage warning sign structure present; Stage 1 and Stage 2 use client's own language.
- [ ] High-risk situations are client-specific, not generic lists.
- [ ] Coping skill toolbox lists named techniques the client practiced in treatment, not generic categories.
- [ ] Three-tier response ladder complete: Tier 1 (self), Tier 2 (support system), Tier 3 (professional re-engagement).
- [ ] Each tier includes "how I know I need to move to the next tier" criterion.
- [ ] Re-engagement criterion is observable, specific, and calibrated to catch early relapse (not acute crisis only).
- [ ] Crisis contacts include 988 and local emergency option; not omitted.
- [ ] Support contacts include at least one non-professional support.
- [ ] Maintenance schedule covers at minimum months 1–3 post-discharge.
- [ ] Plan written in accessible language at client's literacy level.
- [ ] Signature lines and copy-given confirmation present.
- [ ] Client input was present in drafting each section; sections completed without input flagged.
