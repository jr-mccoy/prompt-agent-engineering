---
title: "Columbia (C-SSRS) Suicide Risk Assessment Drafter"
category: psychology/risk-crisis
description: "Produce a structured suicide risk assessment using the Columbia Suicide Severity Rating Scale framework (ideation severity & intensity, behavior, lethality), integrating static / dynamic / protective factors and producing an explicit risk stratification and disposition."
techniques:
  - ST-04
  - DT-02
  - RT-02
  - RT-05
  - QA-04
  - CM-02
  - DS-04
difficulty: advanced
tags:
  - suicide-risk-assessment
  - c-ssrs
  - columbia-protocol
  - risk-stratification
  - imminent-risk
  - safety-disposition
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/risk-crisis/psychology_stanley_brown_safety_plan.md
  - domain-psychology/risk-crisis/psychology_lethal_means_counseling_script.md
  - domain-psychology/risk-crisis/psychology_civil_commitment_narrative.md
  - domain-psychology/documentation/psychology_intake_assessment_note.md
---

# Columbia (C-SSRS) Suicide Risk Assessment Drafter

## Objective

Generate a clinically defensible suicide-risk write-up structured on the Columbia Suicide Severity Rating Scale (C-SSRS) framework. The assessment must:

1. Cover **Ideation Severity** (5-level), **Ideation Intensity** (frequency, duration, controllability, deterrents, reasons), and **Behavior** (preparatory, aborted, interrupted, actual attempt, NSSI), with **Lethality** for any actual attempts.
2. Synthesize **static**, **dynamic**, and **protective** factors.
3. Produce explicit **risk stratification** (low / moderate / high or chronic vs acute) with rationale.
4. Decide **imminence** and **disposition** (outpatient with safety plan / higher LOC / ED transfer / involuntary hold).
5. Document the clinician's reasoning and what would change the stratification.

## When to Use

- Intake when any positive screen on a brief instrument (PHQ-9 item 9, ASQ, brief C-SSRS).
- Any session where SI / SA / preparatory behavior emerges or escalates.
- After ED discharge, hospitalization, or post-attempt re-entry.
- Pre-discharge from inpatient or residential.
- Whenever a clinician needs structured documentation to support a hold, refusal-of-hold, or step-up/down decision.

## Inputs / Context

- Client identifiers, age, current setting (outpatient / ED / inpatient / mobile crisis).
- Date and source of last positive screen.
- Detailed answers to C-SSRS items, in client's own words where possible:
  - **Ideation Severity:** wish to be dead → non-specific active SI → SI with method (no plan, no intent) → SI with some intent (no specific plan) → SI with specific plan and intent.
  - **Ideation Intensity:** frequency, duration, controllability, deterrents, reasons for ideation.
  - **Behavior:** actual attempt, interrupted attempt, aborted/self-interrupted attempt, preparatory acts, NSSI; for each: dates, methods, lethality, intent.
- **Static** factors: prior attempts, family suicide history, age, gender, sexual orientation, race/ethnicity context, military history, history of trauma, chronic medical illness, hopelessness trait.
- **Dynamic** factors: current depression severity, anxiety/agitation, hopelessness state, substance use, sleep, recent loss, financial/legal/relational stressor, anniversary effects, recent ED visit/discharge, current psychotic symptoms, command AH/VH content.
- **Protective** factors: reasons for living, religious/cultural prohibitions, ambivalence/help-seeking, family responsibilities, treatment engagement, protective social ties.
- **Access to means:** firearms (in home, family member's home, vehicle), lethal medications (current scripts, opioids, anticholinergics, lithium, TCAs, beta blockers, glaucoma drops), other (high places, water, motor vehicles).
- **Mental status** at time of assessment.
- **Collateral information** if available, with ROI status.

## Constraints

### Must

- Output the following labeled sections in order: **Encounter Metadata**, **Source of Concern**, **Ideation Severity (C-SSRS)**, **Ideation Intensity (C-SSRS)**, **Behavior (C-SSRS)**, **Lethality of Past Attempt(s)**, **Static Factors**, **Dynamic Factors**, **Protective Factors**, **Access to Means**, **Mental Status**, **Collateral**, **Risk Stratification**, **Imminence Decision**, **Disposition**, **Safety Plan Reference**, **What Would Change This Stratification**, **Clinical Reasoning Summary**, **Signatures**.
- Use the C-SSRS 5-level ideation severity language explicitly; for each level endorsed, give frequency, duration, controllability, deterrents, reasons.
- For any past or recent attempt, document method, medical lethality (Lethality Rating Scale 0–6 if applicable), and rescue circumstances (planned vs interrupted).
- Risk stratification distinguishes **chronic risk** (lifetime/static-driven) from **acute risk** (current dynamic factors), and gives both an overall band (Low / Moderate / High) and a sentence rationale per band.
- Disposition is selected from a fixed set: Outpatient with safety plan / Outpatient with increased frequency and within-24h check-in / Mobile crisis dispatch / ED for evaluation / Voluntary inpatient admission / Involuntary hold initiated.
- Document what specific change in dynamic factors would move the stratification up or down (used by future clinicians and on-call coverage).
- Document lethal-means counseling status (offered / completed / declined; firearms removed/secured/not yet; medications secured/not yet) — link to the lethal-means counseling note if separate.
- For any imminent risk, document the time-stamp of the disposition decision and who was contacted (crisis team, emergency contact, ED).
- Include both clinician and supervisor / on-call sign-off lines for high-risk dispositions.

### Must Not

- Do not collapse C-SSRS items into a single sentence. Each item endorsed gets its own documentation.
- Do not soften client language. If the client said "I want to die," document those words.
- Do not document "no SI" without stating the items asked and the answers given.
- Do not assign Low risk in the presence of recent attempt, command AH, severe agitation, or specific plan + intent + means without specific countervailing rationale.
- Do not delegate the disposition decision to a future visit; document decision at time of assessment.
- Do not omit lethal-means status; "not addressed" is itself a documentation item.
- Do not fabricate client responses; flag missing items.

## Instructions

1. Compile encounter metadata and source of concern.
2. Walk the C-SSRS Ideation Severity items in order; document the highest level endorsed and any positive lower items.
3. For ideation present, document Intensity items (frequency, duration, controllability, deterrents, reasons).
4. Walk Behavior items: actual attempts, interrupted, aborted, preparatory, NSSI; for each, dates, methods, lethality.
5. Document static, dynamic, and protective factors with specifics (not just lists of categories).
6. Document access to means in detail.
7. Document mental status and any collateral information.
8. Stratify risk: chronic + acute, with named bands and rationale.
9. Decide imminence and disposition; document who was contacted and when.
10. Reference safety plan and lethal-means status.
11. State what would move the stratification up or down.
12. Write a clinical reasoning summary (3–6 sentences) integrating the data.
13. Run verification.

## Output Format

```
=== SUICIDE RISK ASSESSMENT (Columbia / C-SSRS) ===

ENCOUNTER METADATA
Client: [Initials/MRN]    DOB: [age, gender, pronouns]
Date of assessment: [YYYY-MM-DD]    Time: [HH:MM]    Setting: [Outpatient / ED / Inpatient / Mobile crisis / Telehealth]
Clinician: [Name, credentials, license #]    On-call / Supervisor: [Name, credentials]
Reason for assessment: [Trigger — positive screen / clinical concern / post-discharge follow-up / etc.]

SOURCE OF CONCERN
[1–3 sentences. What raised the concern; what the client said in own words: "..."]

IDEATION SEVERITY (C-SSRS — past month and lifetime)
1. Wish to be dead: [Yes / No] — Lifetime: [...]    Past month: [...]    Today: [...]
2. Non-specific active suicidal thoughts: [Yes / No] — [details]
3. Active SI with any methods (no plan, no intent): [Yes / No] — methods considered: [...]
4. Active SI with some intent to act, no specific plan: [Yes / No] — intent details: [...]
5. Active SI with specific plan and intent: [Yes / No] — plan specifics: [...]

Highest level endorsed past month: [Level X]
Highest level endorsed today: [Level X]

IDEATION INTENSITY (C-SSRS)
- Frequency: [Less than weekly / Once weekly / 2–5 per week / Daily / Many times per day]
- Duration: [Fleeting <1 min / <1 hr / 1–4 hr / 4–8 hr / Most of day]
- Controllability: [Easily able to control / Some difficulty / Real difficulty / Cannot control / Did not attempt to control]
- Deterrents: [Definitely stopped me / Probably stopped me / Uncertain / Probably didn't stop me / Did not deter]
  Specific deterrents named by client: "..."
- Reasons for ideation: [End the pain / Get attention / Punish self / Other — quoted]

BEHAVIOR (C-SSRS — lifetime and recent)
- Actual attempts: [Number lifetime; most recent date; method; medical lethality; rescue: planned/interrupted; client's stated intent at time]
- Interrupted attempt: [Yes / No — details]
- Aborted / self-interrupted attempt: [Yes / No — details]
- Preparatory acts or behavior: [Acquiring means / Giving things away / Saying goodbye / Note / Searching methods / Yes-No-details]
- NSSI: [Methods, frequency, function, last episode]

LETHALITY OF PAST ATTEMPT(S)
[For each attempt: Lethality Rating Scale 0–6: 0=no physical damage … 6=death; description; medical attention received; ICU; near-miss circumstances.]

STATIC FACTORS
- Prior attempts: [count, most recent]
- Family suicide history: [...]
- Trauma history: [...]
- Chronic medical illness: [...]
- Demographic context: [age cohort, sex, sexual orientation if disclosed and relevant, military history, race/ethnicity context if relevant to risk]
- Trait hopelessness: [...]

DYNAMIC FACTORS
- Current depression severity: [PHQ-9 = X]
- Anxiety / agitation: [GAD-7 = X; observed agitation]
- State hopelessness: [Beck Hopelessness or quoted statements]
- Substance use: [last use, intoxication today, withdrawal]
- Sleep: [hrs/night, recent change]
- Recent loss / stressor: [type, when]
- Anniversary / date salience: [...]
- Recent ED / discharge: [date, where, follow-up status]
- Psychotic symptoms / command AH: [content if present]
- Sense of burdensomeness / thwarted belongingness: [client-stated]

PROTECTIVE FACTORS
- Reasons for living: [client's own words: "..."]
- Religious / cultural prohibitions: [...]
- Ambivalence / help-seeking: [evidence — coming to appointment, calling crisis line, telling family]
- Family / dependents: [...]
- Treatment engagement: [...]
- Social ties: [specific, named]
- Future-oriented commitments: [...]

ACCESS TO MEANS
- Firearms: [In home / Family member's home / Vehicle / None known] — [storage status]
- Lethal medications: [Current scripts including opioids, benzodiazepines, lithium, TCAs, anticholinergics, beta-blockers, glaucoma drops, OTC acetaminophen quantity]
- Other means: [High places / water / motor vehicle / sharps / other]

MENTAL STATUS (at time of assessment)
[Appearance, behavior, speech, mood (quoted), affect, thought process, thought content (including SI/HI/AH/VH/delusions), cognition, insight, judgment.]

COLLATERAL
[Source, ROI status, content received, impact on assessment.]

RISK STRATIFICATION
Chronic risk: [Low / Moderate / High] — Rationale: [static factors driving chronic risk]
Acute risk: [Low / Moderate / High] — Rationale: [dynamic factors active right now]
Overall stratification: [Low / Moderate / High]

IMMINENCE DECISION
Imminent risk (next hours-to-days): [Yes / No]
Rationale: [Specific factors — plan + intent + means + agitation; or absence thereof]

DISPOSITION
Selected: [Outpatient with safety plan / Outpatient with increased frequency and 24-h check-in / Mobile crisis dispatch / ED for evaluation / Voluntary inpatient / Involuntary hold initiated]
Time of decision: [HH:MM]
Contacts made:
- [Crisis team / On-call psychiatrist / Emergency contact / ED] — [time, content, outcome]
- [Transport: client driven by [self / family / EMS / law enforcement] to [destination]; estimated arrival]

SAFETY PLAN REFERENCE
Stanley-Brown safety plan: [Completed today / Updated today / Existing dated YYYY-MM-DD reviewed / Not completed — rationale]
Lethal-means counseling: [Completed today / Declined / Deferred — rationale]
Means restriction status: [Firearms — removed/secured/declined; Medications — secured/declined]

WHAT WOULD CHANGE THIS STRATIFICATION
Up: [Specific change in dynamic factors that would move risk band up — e.g., "Acquiring firearm; loss of housing; intoxication; cessation of contact with treatment."]
Down: [Specific change that would move risk band down — e.g., "PHQ-9 < 10 sustained 2 weeks; firearm removal verified; consistent attendance; established sobriety."]

CLINICAL REASONING SUMMARY
[3–6 sentences integrating the above into an explicit clinical impression: why this stratification, why this disposition, why now.]

SIGNATURES
Clinician: __________________  Date/Time: ___________
On-call / Supervisor (required for High acute or involuntary hold): __________  Date/Time: ___________
```

## Verification

- [ ] All 19 labeled sections present and in order.
- [ ] Each C-SSRS Ideation Severity item answered (Y/N) with timeframe.
- [ ] Ideation Intensity items present when ideation endorsed.
- [ ] Behavior items walked with dates / methods / lethality.
- [ ] Lethality Rating documented for any actual attempt.
- [ ] Static / dynamic / protective factors are specific, not generic.
- [ ] Access to means documented (firearms, meds, other).
- [ ] Risk stratified separately for chronic and acute, plus overall.
- [ ] Imminence explicitly decided.
- [ ] Disposition selected from fixed set with time and contacts logged.
- [ ] Safety plan and lethal-means status referenced.
- [ ] "What would change this stratification" explicit (up and down).
- [ ] Clinical reasoning summary integrates rather than restates.
- [ ] Supervisor / on-call sign-off present for High acute or involuntary disposition.
- [ ] Client language preserved; no euphemisms.
- [ ] Gaps flagged; nothing fabricated.
