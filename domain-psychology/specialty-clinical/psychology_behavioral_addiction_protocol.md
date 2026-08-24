---
title: "Behavioral Addiction CBT — Gambling / Gaming / Behavioral-Addiction Protocol"
category: psychology/specialty-clinical
description: "Generate a CBT session/episode plan for behavioral addiction (gambling disorder, gaming disorder, problematic internet use) with functional analysis, cognitive correction of gambling-related distortions, stimulus control, and relapse prevention."
techniques:
  - ST-04
  - RT-02
  - DT-02
  - DS-04
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - behavioral-addiction
  - gambling-disorder
  - gaming-disorder
  - CBT
  - functional-analysis
  - relapse-prevention
  - motivational-interviewing
intended_use: model-testing
updated: "2026-06-08"
related_prompts:
  - domain-psychology/treatment-planning/psychology_relapse_prevention_plan_designer.md
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
  - domain-psychology/modalities/cbt/psychology_cbt_panic_protocol_session_plan.md
---

# Behavioral Addiction CBT — Gambling / Gaming / Behavioral-Addiction Protocol

## Objective

Generate a CBT session/episode plan for a behavioral addiction — gambling disorder (DSM-5-TR), gaming disorder (ICD-11), or problematic internet use — anchored to manualized cognitive-behavioral treatment for gambling (Petry's CBT workbook approach; Ladouceur & Lachance's cognitive correction model) with relapse-prevention scaffolding (Marlatt & Gordon) and motivational interviewing (Miller & Rollnick) for ambivalence. The plan specifies a functional analysis of the target behavior, cognitive correction of behavior-specific distortions (gambler's fallacy, illusion of control, near-miss effect), stimulus control and financial/access safeguards, a collaboratively set abstinence-or-harm-reduction goal, and risk monitoring (behavioral addictions, gambling especially, carry elevated suicide risk).

## When to Use

- DSM-5-TR Gambling Disorder, ICD-11 Gaming Disorder, or clinically significant problematic internet/screen use.
- Client showing chasing losses, escalating stakes/time, withdrawal-like irritability, lying about extent, or jeopardized relationships/finances/work.
- Ambivalent client where MI is needed before action-stage CBT.
- Co-occurring depression, anxiety, or substance use where the behavior functions as escape/regulation.
- Not appropriate as a standalone plan during acute suicidal crisis or unmanaged financial/legal emergency — stabilize and escalate first.

## Inputs / Context

- Target behavior and DSM-5-TR / ICD-11 criteria met (count and which).
- Baseline screen scores: PGSI or SOGS (gambling); IGDS9-SF (gaming); time/money metrics.
- Functional pattern: triggers (internal/external), urge intensity, behavior, short-term relief, long-term consequence.
- Financial picture: debt, recent losses, access to funds, others affected. `[clinician input required: current financial-crisis severity and whether a debt emergency exists]`
- Comorbidity: depression, anxiety, ADHD, SUD, prior behavioral addictions.
- Suicide-risk status (ideation, plan, prior attempt, recent catastrophic loss). `[clinician input required: current SI screen result]`
- Stage of change and goal preference (abstinence vs harm reduction). `[clinician input required: collaboratively negotiated goal]`
- Available environmental controls: self-exclusion programs, blocking software, account closure, financial delegation, supporter.

## Constraints

### Must

- Build an explicit functional analysis of the target behavior (antecedent → urge → behavior → short-term reinforcement → long-term cost).
- Target behavior-specific cognitive distortions by name: gambler's fallacy, illusion of control, near-miss as "almost won," selective recall of wins, superstitious rules, chasing logic.
- Specify stimulus control and access/financial safeguards (self-exclusion enrollment, blocking apps, removing payment methods, delegating finances, deleting accounts) as concrete behavioral steps.
- Screen for suicidal ideation every episode where active behavior, recent loss, or debt crisis is present; behavioral addiction (notably gambling) carries elevated suicide risk.
- Assess for acute financial/debt crisis and route to appropriate resources (financial counseling, debt support) alongside therapy.
- Make the abstinence-vs-harm-reduction goal collaborative and documented, not imposed.
- Use MI strategies (evoke change talk, roll with resistance, develop discrepancy) when ambivalence is present rather than confronting.
- Include a relapse-prevention component: high-risk situations, lapse-vs-relapse distinction, coping/urge-surfing plan.

### Must Not

- Do not treat lapses as catastrophic failure (abstinence violation effect); frame as learning data.
- Do not impose abstinence on an ambivalent client without MI groundwork; premature confrontation increases dropout.
- Do not skip the SI screen because the presenting concern is "just gambling/gaming."
- Do not address cognitions without behavioral access control — distortion work alone is insufficient when funds/accounts remain freely accessible.
- Do not provide financial, legal, or debt-management advice beyond referral.
- Do not fabricate screen scores, debt figures, or loss amounts — these come from client report or records.

## Instructions

1. Open with screen review (PGSI/SOGS or IGDS9-SF) and the week's time/money/behavior data.
2. Conduct or update the functional analysis of the target behavior; identify the dominant function (escape, excitement, social, financial recovery).
3. Run the SI/risk screen; if positive, branch to risk pathway (assessment, safety plan, escalation) before continuing.
4. Assess and document financial-crisis severity; refer to financial counseling/debt support if a crisis exists.
5. Using MI, establish or revisit the goal (abstinence vs harm reduction) and elicit change talk.
6. Select 1–2 behavior-specific cognitive distortions present this week; do cognitive correction (challenge probability/control beliefs, examine near-miss logic).
7. Specify concrete stimulus-control and access safeguards to implement before next session.
8. Build/refresh the relapse-prevention plan: high-risk situations, urge-surfing, coping menu, lapse protocol.
9. Assign homework: self-monitoring log, one access-control action, one cognitive-correction practice.
10. Document outcome metrics, risk status, and coordination needs; co-sign/notify supervisor if SI elevated or financial emergency.

## Output Format

```
=== BEHAVIORAL ADDICTION CBT SESSION PLAN ===
Client: [Initials/MRN]    Session #: [N]    Date: [YYYY-MM-DD]    Modality: [In-office / Telehealth]
Target behavior: [Gambling / Gaming / Internet]    Dx: [DSM-5-TR Gambling Disorder / ICD-11 Gaming Disorder / Other]
Baseline screen: [PGSI / SOGS / IGDS9-SF = N]    This week: [time / money / episodes]

OPENING (5 min)
- Screen/log review: [data]
- Homework review: [access control done? cognitive practice? log kept?]

FUNCTIONAL ANALYSIS
Antecedent/trigger: [internal + external]
Urge intensity (0–100): [N]
Behavior: [what, duration, amount]
Short-term reinforcement: [escape / excitement / chasing / social]
Long-term consequence: [financial / relational / occupational]

RISK SCREEN
SI/HI: [Result; C-SSRS if indicated]    Recent catastrophic loss: [Y/N]
Financial crisis: [None / Moderate / Acute — describe]    Referral made: [financial counseling / debt support]

GOAL (collaborative)
[Abstinence / Harm reduction — specifics]    Stage of change: [...]    Change talk elicited: [...]

COGNITIVE CORRECTION
Distortion(s) this session: [gambler's fallacy / illusion of control / near-miss / selective recall]
Verbatim belief: "[...]"    Correction/evidence work: [...]    Re-rate conviction (0–100): [N]

STIMULUS CONTROL / ACCESS SAFEGUARDS
- [Self-exclusion enrollment / blocking software / remove payment method / delegate finances / close account]

RELAPSE PREVENTION
High-risk situations: [...]    Urge-surfing/coping plan: [...]    Lapse protocol: [...]

HOMEWORK
- Self-monitoring log: [what to track]
- Access-control action: [specific]
- Cognitive practice: [specific]

OUTCOME / RISK / BILLING
- Screen trajectory: [trend]    Goal adherence: [...]
- Risk status: [...]    Supervisor co-sign/notify: [Y/N — why]
- Prescriber coordination: [Y/N]
- CPT: [90834 (45 min) / 90837 (60 min)]    Next focus: [...]
Clinician: ____________________  Supervisor (if high acuity): ____________________
```

## Verification

- [ ] Functional analysis includes antecedent, urge, behavior, short- and long-term consequences.
- [ ] Behavior-specific distortions named and corrected (not generic cognitive work).
- [ ] Stimulus-control/access safeguards specified as concrete steps.
- [ ] SI/risk screen completed; gambling-related suicide risk addressed.
- [ ] Financial-crisis severity assessed; referral made if crisis present.
- [ ] Abstinence-vs-harm-reduction goal is collaborative and documented.
- [ ] MI used where ambivalence present; no premature confrontation.
- [ ] Relapse-prevention plan distinguishes lapse from relapse.
- [ ] CPT code and supervisor co-sign (if high acuity) recorded.
- [ ] No fabricated screen scores, loss amounts, or debt figures — all from client report or records.
