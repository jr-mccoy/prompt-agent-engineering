---
title: "Handoff Communication Structurer"
category: healthcare-clinical/communication
description: "Generate structured clinical handoff communications using standardized frameworks (SBAR, I-PASS) to ensure safe information transfer between providers — active issues, pending results, contingency plans, and clear task ownership — for clinician verification, not autonomous handoff."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-01
  - QA-20
  - CM-02
difficulty: advanced
tags:
  - handoff
  - sbar
  - i-pass
  - care-transitions
  - patient-safety
updated: "2026-06-07"
related_prompts:
  - domain-healthcare-clinical/prompts/workflow/medicine_clinical_documentation.md
  - domain-healthcare-clinical/prompts/reasoning/medicine_clinical_decision_support.md
  - domain-healthcare-clinical/prompts/quality/medicine_adverse_event_analyzer.md
---

# Handoff Communication Structurer

**Objective:** Generate structured clinical handoff communications using standardized frameworks (SBAR, I-PASS) to ensure critical information transfer between providers, including active issues, pending results, contingency plans, and clear task ownership.

**Important Disclaimer:** Handoff communications must be verified by the responsible clinician before transmission. This tool assists with structuring handoffs but does not replace direct clinician-to-clinician communication and professional judgment.

**When to use:**
- Structuring a shift-to-shift, service-to-service, or level-of-care transfer handoff.
- Preparing weekend/holiday coverage summaries or procedure handoffs.
- Ensuring pending results, contingencies, and task ownership are explicit before a transition.
- Teaching standardized handoff frameworks (SBAR, I-PASS) to learners.

**When NOT to use:**
- As a replacement for direct, verbal, two-way clinician-to-clinician handoff.
- For an actively unstable patient requiring immediate escalation rather than a written handoff.
- When the source clinical data is incomplete — gather and verify the facts first.

**Audience:** Licensed clinicians, residents, advanced-practice providers, and nurses responsible for care transitions.

---

## Inputs / Context

Provide the patient and handoff context below. If pasting raw clinical data (vitals, problem list, results), wrap it in a `<handoff_data>` tag so it can be referenced by name; structure only what is supplied and flag any required handoff element that is missing.

---

## Input Required

### Patient Information

**Identifiers:**
- Name/Initials: [Patient identifier]
- Room/Location: [Location]
- MRN: [If applicable]
- Attending: [Responsible physician]

**Current Status:**
- Admission date: [Date]
- Primary diagnosis: [Diagnosis]
- Current clinical status: [Stable/Unstable/Improving/Declining]
- Code status: [Full/DNR/DNI/Comfort]

### Handoff Context

**Handoff Type:**
- [ ] Shift-to-shift (same service)
- [ ] Service-to-service transfer
- [ ] Floor-to-ICU or ICU-to-floor
- [ ] Hospital-to-facility discharge
- [ ] Procedure handoff
- [ ] Weekend/holiday coverage

**Urgency Level:**
- [ ] Routine
- [ ] Requires close monitoring
- [ ] Unstable/High acuity

---

## Constraints

### Must
- Use a single standardized framework (SBAR or I-PASS) consistently, in the same order every time.
- Make **illness severity / stability** explicit and lead with the least stable patients.
- Ensure **every pending result has an action plan** and **every task has a named owner and timing**.
- Provide **contingency ("if/then") plans** for the likely deterioration scenarios.
- Confirm and communicate **code status and allergies** on every handoff.
- Ground all content in the supplied clinical data; flag any required element that is missing or unverified — never fabricate vitals, results, doses, or events.
- Frame output as a draft for clinician verification and direct verbal handoff.

### Must Not
- Do not present the structured handoff as a substitute for direct, two-way verbal handoff.
- Do not invent clinical data, pending results, medications, or contingency thresholds.
- Do not bury critical/unstable items under routine detail, or omit task ownership.
- Do not replace clinician judgment about escalation and disposition.

---

## SBAR Framework

### S - Situation

**Current State:**
```
[Patient name/identifier] in [room/location]

Current situation: [One-sentence summary of why they're in your care]

Immediate concern: [What needs attention now, if anything]

Stability: [Stable / Guarded / Unstable]
```

### B - Background

**Relevant History:**
```
ADMISSION INFORMATION
- Admitted: [Date] for [Reason]
- Working diagnosis: [Diagnosis]

RELEVANT HISTORY
- Key PMH: [Conditions affecting current care]
- Key surgical history: [Relevant procedures]
- Allergies: [Drug allergies with reactions]

HOSPITAL COURSE SUMMARY
[Brief narrative of what has happened during this admission]

KEY EVENTS THIS SHIFT
- [Event 1 with time]
- [Event 2 with time]
```

### A - Assessment

**Current Assessment:**
```
CURRENT CLINICAL STATUS

Vitals trend: [Stable/Improving/Concerning trend]
- Most recent: T[X] HR[X] BP[X/X] RR[X] SpO2[X]%
- Concerning changes: [If any]

System-by-system (abnormals and active issues only):

Neuro: [Status / Changes / Concerns]
Cardiac: [Status / Changes / Concerns]
Pulm: [Status / Changes / Concerns]
GI: [Status / Changes / Concerns]
Renal: [Status / Changes / Concerns]
ID: [Status / Changes / Concerns]
Heme: [Status / Changes / Concerns]
Other: [Status / Changes / Concerns]

ACTIVE PROBLEMS
1. [Problem 1]: [Current status and plan]
2. [Problem 2]: [Current status and plan]
3. [Problem 3]: [Current status and plan]

CLINICAL IMPRESSION
[Your assessment of trajectory - improving, stable, at risk for...]
```

### R - Recommendation

**Action Items:**
```
TASKS REQUIRING ACTION

Immediate:
- [ ] [Task]: [What to do] - [Who owns it]

This shift:
- [ ] [Task]: [What to do] - [Who owns it]
- [ ] [Task]: [What to do] - [Who owns it]

PENDING RESULTS
| Test | Expected Time | Action if Abnormal |
|------|---------------|-------------------|
| [Test 1] | [Time] | [What to do] |
| [Test 2] | [Time] | [What to do] |

CONTINGENCY PLANS
If [Scenario 1]:
  → Do [Action] and notify [Person]

If [Scenario 2]:
  → Do [Action] and notify [Person]

ANTICIPATORY GUIDANCE
- Likely to need: [Anticipated needs]
- Watch for: [Warning signs]
- Contact attending if: [Thresholds for escalation]
```

---

## I-PASS Framework

### I - Illness Severity

```
ILLNESS SEVERITY: [STABLE / WATCHER / UNSTABLE]

STABLE: Routine care, unlikely to change overnight
WATCHER: Not unstable but at risk for deterioration
UNSTABLE: Requires frequent assessment, may decompensate

Rationale: [Why this classification]
```

### P - Patient Summary

```
PATIENT SUMMARY

[Age] year-old [sex] with [relevant PMH]
Admitted [date] for [chief complaint/diagnosis]

One-liner: [Synthesis of current situation]

Hospital course highlights:
- [Key event 1]
- [Key event 2]
- [Current trajectory]
```

### A - Action List

```
ACTION LIST

[ ] TASK 1: [Description]
    Owner: [Who]
    Timing: [When]

[ ] TASK 2: [Description]
    Owner: [Who]
    Timing: [When]

[ ] TASK 3: [Description]
    Owner: [Who]
    Timing: [When]

MUST DO:
- [Non-negotiable task]

SHOULD DO:
- [Important but could wait if emergencies arise]

COULD DO:
- [If time permits]
```

### S - Situation Awareness & Contingency Planning

```
SITUATION AWARENESS

WHAT I'M WORRIED ABOUT:
- [Concern 1]: [Why]
- [Concern 2]: [Why]

WHAT COULD GO WRONG:
- [Risk 1]: [Signs to watch]
- [Risk 2]: [Signs to watch]

CONTINGENCY PLANS:

IF [Trigger condition]:
   THEN [Immediate action]
   NOTIFY [Person/team]
   CONSIDER [Next steps]

IF [Trigger condition]:
   THEN [Immediate action]
   NOTIFY [Person/team]
   CONSIDER [Next steps]
```

### S - Synthesis by Receiver

```
SYNTHESIS CHECK

Receiving provider should confirm:
- [ ] Illness severity understood
- [ ] Active problems clear
- [ ] Action items acknowledged with ownership
- [ ] Contingencies understood
- [ ] Questions asked and answered

Clarifying questions from receiver:
- [Question 1]
- [Question 2]

Read-back of critical items:
- [Critical item 1]
- [Critical item 2]
```

---

## Specialized Handoff Templates

### ICU Handoff (Enhanced Detail)

```
ICU HANDOFF

PATIENT: [ID] | ROOM: [X] | ATTENDING: [Name]
CODE STATUS: [Full/DNR/DNI/Comfort]
ISOLATION: [Type if any]

ILLNESS SEVERITY: [CRITICAL / UNSTABLE / GUARDED]

24-HOUR SUMMARY:
[Concise narrative of past 24 hours]

SYSTEM-BY-SYSTEM:

NEURO: GCS [X] | Pupils [X] | Sedation [Drug/Dose]
- Assessment: [Current status]
- Plan: [Goals and approach]

CARDIOVASCULAR: [Rhythm] | MAP goal [X] | Pressors [If any]
- Lines: [Central, arterial, etc.]
- Assessment: [Current status]
- Plan: [Goals and approach]

PULMONARY: [Vent mode/settings or airway status]
- FiO2: [X] | PEEP: [X] | Current ABG: [Values]
- Assessment: [Current status]
- Plan: [Goals, weaning trajectory]

RENAL/FLUIDS: [UOP trend] | Cr [X] | I/O [X]
- RRT: [If applicable]
- Assessment: [Current status]
- Plan: [Fluid goals, electrolyte repletion]

GI/NUTRITION: [Diet/feeds] | [GI issues]
- Assessment: [Current status]

ID: [Active infections] | [Antibiotics with day #]
- Cultures: [Status]
- Assessment: [Current status]

HEME: [Anticoagulation] | [Blood products]
- Assessment: [Current status]

PENDING STUDIES:
| Study | Ordered | Expected | Action Needed |
|-------|---------|----------|---------------|
| [X]   | [Time]  | [Time]   | [Action]      |

FAMILY/GOALS OF CARE:
- Family contact: [Name/Phone]
- Last family update: [Time/Date]
- GOC status: [Summary]

OVERNIGHT ISSUES:
- [Issue and resolution]

WHAT I'M WORRIED ABOUT:
1. [Concern with specific trigger for action]
2. [Concern with specific trigger for action]
```

### Floor-to-ICU Transfer

```
URGENT TRANSFER HANDOFF

PATIENT: [ID] | FROM: [Location] | CODE STATUS: [Status]

REASON FOR TRANSFER:
[Clear statement of why ICU needed]

CURRENT STATUS:
- Vitals: T[X] HR[X] BP[X/X] RR[X] SpO2[X]% on [O2 support]
- Mental status: [Description]
- Airway: [Stable/At risk/Intubated]

IMMEDIATE CONCERNS:
1. [Concern requiring ICU intervention]
2. [Concern requiring ICU intervention]

BRIEF BACKGROUND:
- Admitted for: [Reason]
- Key PMH: [Relevant conditions]
- Hospital course: [What changed]

WHAT HAS BEEN DONE:
- [Intervention 1 with response]
- [Intervention 2 with response]

WHAT NEEDS TO HAPPEN:
- Immediate: [Next intervention needed]
- Pending: [Tests/consults ordered]

ALLERGIES: [List]
CURRENT DRIPS: [If any]
CODE STATUS CONFIRMED: [Yes/No]
FAMILY NOTIFIED: [Yes/No]
```

### Weekend Coverage Handoff

```
WEEKEND COVERAGE SUMMARY

PATIENT LIST: [Service/Team]
COVERING PROVIDER: [Name/Pager]
PRIMARY ATTENDING: [Name/Contact]

HIGH PRIORITY PATIENTS:

1. [Patient ID] - Room [X]
   Status: [UNSTABLE/WATCHER]
   Key issue: [One-liner]
   Must do: [Critical weekend task]
   Watch for: [Deterioration signs]
   If problems: [Contingency]

2. [Patient ID] - Room [X]
   Status: [WATCHER]
   Key issue: [One-liner]
   Must do: [Critical weekend task]
   Watch for: [Deterioration signs]
   If problems: [Contingency]

ROUTINE PATIENTS:
[Brief list with any specific needs]

PENDING RESULTS TO FOLLOW:
| Patient | Test | Expected | Action if Abnormal |
|---------|------|----------|-------------------|
| [ID]    | [Test]| [Time]  | [Action]          |

DISCHARGES PLANNED:
- [Patient]: [Pending discharge need]

ANTICIPATED ADMISSIONS:
- [Expected admission type]

ESCALATION CONTACTS:
- Non-urgent: [Contact]
- Urgent: [Contact]
- Attending for major decisions: [Contact]
```

---

## Quality Verification

### Handoff Safety Checklist

Before completing handoff, verify:

**Essential Elements:**
- [ ] Patient correctly identified
- [ ] Code status confirmed and communicated
- [ ] Allergies stated
- [ ] Current medications and drips reviewed
- [ ] Active problems listed
- [ ] All pending results identified with action plans
- [ ] Contingency plans for likely scenarios
- [ ] Clear task ownership established

**Communication Quality:**
- [ ] Verbal handoff completed (not just written)
- [ ] Receiver had opportunity to ask questions
- [ ] Critical items read back
- [ ] Contact information exchanged

**Safety Priorities:**
- [ ] Unstable patients highlighted
- [ ] Time-sensitive tasks flagged
- [ ] Warning signs to watch specified
- [ ] Escalation pathway clear

### Common Handoff Failures to Avoid

**Information Gaps:**
- Missing pending test results
- Incomplete medication reconciliation
- Unclear code status
- Missing allergies

**Communication Failures:**
- No verbal handoff
- No opportunity for questions
- Too much irrelevant detail obscuring critical info
- Using jargon or abbreviations unclear to receiver

**Responsibility Gaps:**
- Tasks without clear ownership
- No contingency plans
- Unclear escalation pathway
- Ambiguous timing expectations

---

## Output Formats

### Quick Verbal Handoff Script

```
"This is [Patient ID] in room [X], a [age] year-old with [key PMH] admitted for [reason].

Current status: [Stable/Watcher/Unstable] because [reason].

Key overnight events: [Brief summary].

Active problems: [Problem 1], [Problem 2].

To do list: [Task 1 - timing], [Task 2 - timing].

Pending: [Test] - if abnormal, [action].

I'm worried about: [Concern] - if [trigger], then [action].

Code status: [Status]. Allergies: [List].

Questions?"
```

### Written Handoff Note

```
═══════════════════════════════════════════════
HANDOFF: [Patient ID] | Room [X] | [Date/Time]
Covering: [Name] | Pager: [Number]
═══════════════════════════════════════════════

STATUS: [STABLE / WATCHER / UNSTABLE]
CODE: [Full/DNR/DNI] | ALLERGIES: [List]

SUMMARY:
[One-liner clinical summary]

ACTIVE ISSUES:
1. [Issue]: [Status] → [Plan]
2. [Issue]: [Status] → [Plan]

TO DO:
□ [Task] - [Timing] - Owner: [Name]
□ [Task] - [Timing] - Owner: [Name]

PENDING:
• [Test] expected [time]: If [result], then [action]

IF/THEN:
• IF [condition] → THEN [action]
• IF [condition] → THEN [action]

CONTACT IF:
• [Threshold for notification]
═══════════════════════════════════════════════
```

---

## Process Guidelines

### Structured Communication
- Use consistent frameworks (SBAR or I-PASS)
- Same order every time
- Complete all sections even if "nothing to report"

### Prioritize by Risk
- Lead with unstable patients
- Highlight time-sensitive items
- Make high-risk issues unmissable

### Enable Questions
- Pause for questions
- Create psychologically safe environment
- Don't rush

### Confirm Understanding
- Read back critical items
- Verify task ownership accepted
- Confirm contact information

---

## False-Positive Prevention

❌ **DON'T:**
- Fabricate vital signs, pending results, medication doses, drips, or events that were not supplied.
- Invent contingency thresholds or escalation criteria not grounded in the clinical picture.
- Omit code status, allergies, or task ownership to make the handoff shorter.
- Bury an unstable patient or time-sensitive task under routine detail.
- Reduce the handoff to vague phrases ("doing fine, follow labs") that give the receiver nothing actionable.

✅ **DO:**
- Structure only the data provided; mark missing required elements (code status, allergies, pending results) as gaps to verify.
- Lead with illness severity and the least stable patients.
- Attach an explicit action plan to every pending result and a named owner + timing to every task.
- State each contingency as a concrete if/then with whom to notify.
- Stay genuinely useful: produce a complete, scannable handoff the receiver can act on, framed for verbal confirmation.

---

## Dual-Failure Prevention (QA-20)

This prompt must avoid **both** failure modes:

- **Failure of commission (harmful):** asserting fabricated results, doses, or contingency thresholds, or misstating code status/allergies — any of which can directly cause patient harm at a transition of care.
- **Failure of omission (useless):** producing a vague, incomplete handoff with no ownership, no pending-result actions, and no contingencies, leaving the receiver unprepared.

The correct output is complete *and* bounded: a fully structured handoff with explicit ownership, pending-result actions, contingencies, and flagged gaps — framed as a draft for direct verbal, two-way clinician handoff, never as a replacement for it.

---

## Example Output

```
═══════════════════════════════════════════════
HANDOFF: Mr. K (Bed 4B) | Room 412 | 06/07 19:00
Covering: Dr. Lee | Pager: 5521
═══════════════════════════════════════════════

STATUS: WATCHER
CODE: Full | ALLERGIES: Penicillin (hives)

SUMMARY:
68 y/o M, COPD + HFrEF, admitted 06/05 for COPD exacerbation,
improving on steroids/nebs but borderline volume status.

ACTIVE ISSUES:
1. COPD exacerbation: Day 3 prednisone, weaning O2 → wean as tolerated, keep SpO2 ≥ 88%.
2. HFrEF: net even today; watch for fluid overload from IV abx volume.

TO DO:
□ Recheck BMP at 22:00 - Owner: night RN/Dr. Lee
□ Reassess O2 requirement at 06:00 - Owner: Dr. Lee

PENDING:
• Blood cultures (drawn 06/06) expected final 06/08: if positive, notify primary team + start/adjust abx per ID.

IF/THEN:
• IF SpO2 < 88% on current O2 → THEN increase O2, get ABG, call covering MD.
• IF SBP < 90 or new crackles/weight jump → THEN hold further IV fluids, reassess diuresis, notify MD.

CONTACT IF:
• Any respiratory deterioration, new chest pain, or SBP < 90.

[Verify all values against the chart and confirm verbally with the receiving provider.]
═══════════════════════════════════════════════
```

---

## Verification

- [ ] A single framework (SBAR or I-PASS) used consistently, same order.
- [ ] Illness severity / stability stated; unstable patients led with.
- [ ] Every pending result has an action plan; every task has an owner and timing.
- [ ] Contingency if/then plans present for likely scenarios.
- [ ] Code status and allergies confirmed and communicated.
- [ ] No fabricated vitals, results, doses, or events; missing elements flagged.
- [ ] Output framed for direct verbal, two-way handoff with read-back.
- [ ] Avoids both fabrication/omission of critical data and uselessly vague content (QA-20).

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Opens with a single-sentence objective scoping the tool to structuring safe handoffs for verification.
- **ST-02 (Structured Sequential Instructions):** Standardized framework sections (SBAR / I-PASS) applied in fixed order.
- **RT-02 (Multi-Dimensional Reasoning):** Integrates severity, active problems, pending results, contingencies, and ownership dimensions.
- **QA-01 (Self-Verification):** Handoff safety checklist and read-back/synthesis step before completion.
- **QA-20 (Dual-Failure Prevention):** Guards against both harmful fabrication/misstatement and uselessly vague handoffs.
- **CM-02 (Constraint / Safety Framing):** Hard constraints on ownership, contingencies, code status/allergies, no fabrication, and verbal-handoff framing.

---

## Related Prompts

- `domain-healthcare-clinical/prompts/workflow/medicine_clinical_documentation.md` — formats the underlying clinical record the handoff draws from.
- `domain-healthcare-clinical/prompts/reasoning/medicine_clinical_decision_support.md` — supports the management decisions behind the handoff's contingency plans.
- `domain-healthcare-clinical/prompts/quality/medicine_adverse_event_analyzer.md` — analyzes handoff-related safety events when transitions fail.

---

**Critical Reminder:** Handoffs are high-risk moments for patient safety. This tool helps structure communication but cannot replace the professional judgment, direct communication, and situational awareness that safe handoffs require.
