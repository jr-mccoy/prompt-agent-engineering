---
title: "Quality Improvement Project Designer"
category: healthcare-clinical/quality
description: "Design healthcare quality-improvement projects with structured methodologies (Model for Improvement/PDSA, Lean, DMAIC) — SMART aim, outcome/process/balancing measures, driver diagram, stakeholder analysis, barrier anticipation, and a control plan — grounded in real baseline data and institutional oversight."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-02
  - QA-01
  - QA-20
difficulty: advanced
tags:
  - quality-improvement
  - pdsa
  - model-for-improvement
  - measurement
  - implementation
updated: "2026-06-07"
related_prompts:
  - domain-healthcare-clinical/prompts/quality/medicine_adverse_event_analyzer.md
  - domain-healthcare-clinical/prompts/communication/medicine_handoff_communication.md
  - domain-healthcare-clinical/prompts/education/medicine_literature_synthesizer.md
---

# Quality Improvement Project Designer

**Objective:** Design quality improvement projects using structured methodologies (PDSA, Lean, Six Sigma), including measure definition, stakeholder identification, intervention planning, barrier anticipation, and monitoring protocols.

**Important Disclaimer:** Quality improvement projects should be conducted under appropriate organizational oversight, with consideration for IRB requirements if applicable, and with engagement of relevant stakeholders. This tool provides a framework but does not replace QI training or institutional processes.

**When to use:**
- Designing a QI project charter with a SMART aim and a balanced measure set.
- Selecting and applying a methodology (Model for Improvement/PDSA, Lean, DMAIC).
- Building a driver diagram, change package, and PDSA test plan.
- Anticipating barriers and designing a sustainability/control plan.

**When NOT to use:**
- As a replacement for formal QI training, IRB determination, or institutional approval processes.
- For projects without access to real baseline data — gather the data first.
- For individual performance management or research masquerading as QI.

**Audience:** Clinicians, QI/quality leaders, project sponsors, frontline improvement teams, and QI learners.

---

## Inputs / Context

Provide the project context below. Paste any baseline data, audit results, or prior-attempt notes wrapped in a `<qi_context>` tag so they can be referenced by name; build the design on the supplied data and flag where real baseline measurement is still required before proceeding.

---

## Input Required

### Project Context

**Identified Problem:**
- Problem statement: [What is the issue?]
- How identified: [Data, events, complaints, audits]
- Current state: [Baseline performance if known]
- Impact: [Who is affected, how much]

**Organizational Context:**
- Setting: [Hospital, clinic, unit, system]
- Scope: [Single unit, multi-site, system-wide]
- Leadership support: [Strong/Moderate/Limited]
- Resources available: [Time, FTE, budget]

**Previous Improvement Attempts:**
- What has been tried: [Past interventions]
- Why it didn't work: [Barriers encountered]

---

## Constraints

### Must
- Anchor the project in **real baseline data**; if baseline is unknown, make collecting it the first step rather than inventing numbers.
- Write a **SMART aim** and define a balanced measure set: **outcome, process, and balancing** measures.
- Ground methodology, driver logic, and intervention choice in established QI science (Model for Improvement, Lean, DMAIC); cite the framework type.
- Test changes via **small PDSA cycles** before spread; include a sustainability/control plan.
- Include **balancing measures** to detect unintended consequences, and engage frontline stakeholders.
- Flag where **IRB/institutional oversight** and stakeholder approval are required; never fabricate baseline values, targets, or measure definitions.

### Must Not
- Do not replace QI training, IRB review, or institutional approval processes.
- Do not invent baseline performance, effect sizes, or measure data to make the charter look complete.
- Do not set vague/over-ambitious aims, or implement at scale before testing.
- Do not omit balancing measures or a sustainability plan.

---

## QI Methodology Selection

### Choose Primary Methodology

**PDSA (Plan-Do-Study-Act) Cycles**
Best for: Small tests of change, iterative improvement, frontline-driven projects

**Lean**
Best for: Waste reduction, process streamlining, efficiency improvement

**Six Sigma (DMAIC)**
Best for: Defect reduction, variation reduction, data-driven process improvement

**Combination Approach**
Many projects benefit from combining elements (e.g., Lean Six Sigma)

---

## Model for Improvement Framework

### The Three Fundamental Questions

```
1. WHAT ARE WE TRYING TO ACCOMPLISH?
   [Clear, specific, measurable aim]

2. HOW WILL WE KNOW THAT A CHANGE IS AN IMPROVEMENT?
   [Measures that will demonstrate improvement]

3. WHAT CHANGES CAN WE MAKE THAT WILL RESULT IN IMPROVEMENT?
   [Specific interventions to test]
```

---

## Project Charter Template

```
═══════════════════════════════════════════════════════════════
QUALITY IMPROVEMENT PROJECT CHARTER
═══════════════════════════════════════════════════════════════

PROJECT TITLE: [Descriptive title]

DATE: [Charter date]
VERSION: [1.0]

───────────────────────────────────────────────────────────────
PROBLEM STATEMENT
───────────────────────────────────────────────────────────────
[Concise description of the problem]

Current State:
- [Metric]: [Current performance]
- [Impact]: [Who/what is affected and how]
- [Trend]: [Getting better/worse/stable]

Root Causes (preliminary):
- [Cause 1]
- [Cause 2]
- [Cause 3]

───────────────────────────────────────────────────────────────
AIM STATEMENT
───────────────────────────────────────────────────────────────
[Follows SMART format]

Specific: [What exactly will improve]
Measurable: [How we will measure]
Achievable: [Realistic target]
Relevant: [Why this matters]
Time-bound: [By when]

AIM: By [date], we will [improve/reduce/increase] [metric] from
[baseline] to [target] for [population] in [setting].

───────────────────────────────────────────────────────────────
SCOPE
───────────────────────────────────────────────────────────────
In Scope:
- [What's included]
- [Population]
- [Processes]

Out of Scope:
- [What's excluded]
- [Adjacent issues not addressed]

───────────────────────────────────────────────────────────────
TEAM
───────────────────────────────────────────────────────────────
Executive Sponsor: [Name, Role]
  Responsibility: Remove barriers, resource allocation

Project Lead: [Name, Role]
  Responsibility: Day-to-day leadership, coordination

Team Members:
| Name | Role | Responsibility | Time Commitment |
|------|------|----------------|-----------------|
| [Name] | [Clinical Champion] | [Subject expertise] | [X hrs/wk] |
| [Name] | [Frontline Staff] | [Implementation] | [X hrs/wk] |
| [Name] | [Data Analyst] | [Measurement] | [X hrs/wk] |
| [Name] | [QI Facilitator] | [Methodology] | [X hrs/wk] |

───────────────────────────────────────────────────────────────
STAKEHOLDER ANALYSIS
───────────────────────────────────────────────────────────────
| Stakeholder | Interest | Influence | Engagement Strategy |
|-------------|----------|-----------|---------------------|
| [Group/Person] | [High/Med/Low] | [High/Med/Low] | [Approach] |
| [Group/Person] | [High/Med/Low] | [High/Med/Low] | [Approach] |

Key stakeholders to engage early:
- [Stakeholder]: [Why and how]

Potential resistors:
- [Stakeholder]: [Concern] → [Mitigation strategy]

───────────────────────────────────────────────────────────────
MEASURES
───────────────────────────────────────────────────────────────

OUTCOME MEASURE (Primary):
  Definition: [Exactly what is being measured]
  Numerator: [Count of events of interest]
  Denominator: [Population at risk]
  Data source: [Where data comes from]
  Collection frequency: [How often]
  Baseline: [Current performance]
  Target: [Goal performance]
  Owner: [Who is responsible]

PROCESS MEASURES:
  Measure 1: [Name]
    Definition: [What it measures]
    Target: [Goal]
    Frequency: [How often collected]

  Measure 2: [Name]
    Definition: [What it measures]
    Target: [Goal]
    Frequency: [How often collected]

BALANCING MEASURES:
  Measure: [Name]
    Definition: [What it measures - unintended consequences]
    Threshold: [When to be concerned]
    Purpose: [What it's checking for]

───────────────────────────────────────────────────────────────
TIMELINE
───────────────────────────────────────────────────────────────
| Phase | Activities | Start | End | Deliverables |
|-------|------------|-------|-----|--------------|
| Planning | Charter, baseline data | [Date] | [Date] | Charter approved |
| Analysis | Root cause, process map | [Date] | [Date] | Driver diagram |
| Design | Intervention development | [Date] | [Date] | Change package |
| Test | PDSA cycles | [Date] | [Date] | Test results |
| Implement | Scale successful changes | [Date] | [Date] | Full deployment |
| Sustain | Monitoring, hardwiring | [Date] | [Date] | Control plan |

───────────────────────────────────────────────────────────────
RESOURCE REQUIREMENTS
───────────────────────────────────────────────────────────────
Personnel: [FTE commitment]
Budget: [$X for specific needs]
Technology: [Systems, tools needed]
Training: [Education required]
Other: [Additional resources]

───────────────────────────────────────────────────────────────
RISKS AND MITIGATION
───────────────────────────────────────────────────────────────
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | [H/M/L] | [H/M/L] | [Strategy] |
| [Risk 2] | [H/M/L] | [H/M/L] | [Strategy] |

───────────────────────────────────────────────────────────────
APPROVALS
───────────────────────────────────────────────────────────────
Executive Sponsor: _________________ Date: _______
Department Leader: _________________ Date: _______
QI Committee: _________________ Date: _______

═══════════════════════════════════════════════════════════════
```

---

## Root Cause Analysis Tools

### Fishbone (Ishikawa) Diagram

```
FISHBONE DIAGRAM: [Problem Statement]

                    EQUIPMENT          PROCESS
                         \                /
                          \              /
                    [Cause]  \          / [Cause]
                   [Cause]    \        /   [Cause]
                               \      /
                                ======> [PROBLEM]
                               /      \
                   [Cause]    /        \   [Cause]
                    [Cause]  /          \ [Cause]
                          /              \
                         /                \
                    PEOPLE            ENVIRONMENT/POLICY

Categories to explore:
- People: Skills, training, staffing, communication
- Process: Steps, standardization, workflow
- Equipment: Technology, supplies, maintenance
- Environment/Policy: Culture, policies, physical space
```

### Five Whys

```
FIVE WHYS ANALYSIS

Problem: [Statement]

Why 1: Why does [problem] occur?
→ Because [first-level cause]

Why 2: Why does [first-level cause] occur?
→ Because [second-level cause]

Why 3: Why does [second-level cause] occur?
→ Because [third-level cause]

Why 4: Why does [third-level cause] occur?
→ Because [fourth-level cause]

Why 5: Why does [fourth-level cause] occur?
→ Because [root cause]

ROOT CAUSE IDENTIFIED: [Statement]
```

### Driver Diagram

```
DRIVER DIAGRAM

AIM                 PRIMARY DRIVERS         SECONDARY DRIVERS
═══════════════════════════════════════════════════════════════

                    ┌─ [Driver 1.1]
                    │
[AIM      ] ◄──── [Primary Driver 1] ◄──┼─ [Driver 1.2]
 Statement]         │                    │
                    │                    └─ [Driver 1.3]
                    │
                    │                    ┌─ [Driver 2.1]
                    │                    │
                    ├──── [Primary Driver 2] ◄──┼─ [Driver 2.2]
                    │                    │
                    │                    └─ [Driver 2.3]
                    │
                    │                    ┌─ [Driver 3.1]
                    │                    │
                    └──── [Primary Driver 3] ◄──┼─ [Driver 3.2]
                                         │
                                         └─ [Driver 3.3]

CHANGE IDEAS (linked to secondary drivers):
- [Change idea 1] → Tests [Driver X.X]
- [Change idea 2] → Tests [Driver X.X]
```

---

## PDSA Cycle Template

```
═══════════════════════════════════════════════════════════════
PDSA CYCLE #[Number]
═══════════════════════════════════════════════════════════════

Cycle Date: [Start] - [End]
Change Being Tested: [Specific change]
Driver Addressed: [Which driver from diagram]

───────────────────────────────────────────────────────────────
PLAN
───────────────────────────────────────────────────────────────
Objective: [What we're trying to learn/accomplish]

Questions:
1. [Question we want to answer]
2. [Question we want to answer]

Predictions:
1. [What we expect to happen]
2. [What we expect to happen]

Plan for change:
- Who: [Person responsible]
- What: [Specific intervention]
- When: [Dates]
- Where: [Location/unit]

Plan for data collection:
- What data: [Measures]
- Who collects: [Person]
- How: [Method]
- When: [Frequency]

───────────────────────────────────────────────────────────────
DO
───────────────────────────────────────────────────────────────
What happened: [Describe implementation]

Data collected:
| Date | [Measure] | [Measure] | Notes |
|------|-----------|-----------|-------|
| [Date] | [Value] | [Value] | [Notes] |

Problems encountered: [Issues during test]
Unexpected observations: [Surprises]

───────────────────────────────────────────────────────────────
STUDY
───────────────────────────────────────────────────────────────
Analysis of data:
- [Finding 1]
- [Finding 2]

Compare to predictions:
- Prediction 1: [Met/Not met] - [Explanation]
- Prediction 2: [Met/Not met] - [Explanation]

Summary of learning:
[Key insights from this cycle]

───────────────────────────────────────────────────────────────
ACT
───────────────────────────────────────────────────────────────
Decision: [Adopt / Adapt / Abandon]

If Adopt: [Plan for broader implementation]
If Adapt: [Changes to make for next cycle]
If Abandon: [Rationale and alternative approach]

Next PDSA Cycle:
- Focus: [What to test next]
- Timeline: [When]

═══════════════════════════════════════════════════════════════
```

---

## Implementation Planning

### Change Package

```
CHANGE PACKAGE

INTERVENTION BUNDLE:

Change 1: [Name]
  Description: [What it is]
  Evidence base: [Why we think it will work]
  Resources needed: [Requirements]
  Training required: [Education needs]

Change 2: [Name]
  Description: [What it is]
  Evidence base: [Why we think it will work]
  Resources needed: [Requirements]
  Training required: [Education needs]

Change 3: [Name]
  Description: [What it is]
  Evidence base: [Why we think it will work]
  Resources needed: [Requirements]
  Training required: [Education needs]
```

### Implementation Checklist

```
PRE-IMPLEMENTATION
- [ ] Stakeholders engaged and informed
- [ ] Resources secured
- [ ] Training completed
- [ ] Materials/supplies obtained
- [ ] Data collection system ready
- [ ] Baseline data collected
- [ ] Communication plan executed
- [ ] Go-live date announced

IMPLEMENTATION
- [ ] Change deployed as planned
- [ ] Real-time support available
- [ ] Issues logged and addressed
- [ ] Data collection occurring
- [ ] Huddles/check-ins scheduled

POST-IMPLEMENTATION
- [ ] Data analyzed
- [ ] Results shared with stakeholders
- [ ] Lessons documented
- [ ] Sustainability plan activated
- [ ] Spread opportunities identified
```

### Barrier Anticipation

```
ANTICIPATED BARRIERS AND MITIGATION

Technical Barriers:
| Barrier | Likelihood | Impact | Mitigation |
|---------|------------|--------|------------|
| [IT system limitations] | [H/M/L] | [H/M/L] | [Workaround] |
| [Equipment issues] | [H/M/L] | [H/M/L] | [Solution] |

People Barriers:
| Barrier | Likelihood | Impact | Mitigation |
|---------|------------|--------|------------|
| [Staff resistance] | [H/M/L] | [H/M/L] | [Engagement strategy] |
| [Training gaps] | [H/M/L] | [H/M/L] | [Education plan] |

Process Barriers:
| Barrier | Likelihood | Impact | Mitigation |
|---------|------------|--------|------------|
| [Workflow conflicts] | [H/M/L] | [H/M/L] | [Redesign approach] |
| [Competing priorities] | [H/M/L] | [H/M/L] | [Leadership support] |

Resource Barriers:
| Barrier | Likelihood | Impact | Mitigation |
|---------|------------|--------|------------|
| [Budget constraints] | [H/M/L] | [H/M/L] | [Alternative funding] |
| [Time constraints] | [H/M/L] | [H/M/L] | [Phased approach] |
```

---

## Monitoring and Sustainability

### Control Plan

```
CONTROL PLAN

ONGOING MONITORING:

| Measure | Target | Frequency | Owner | Response if Off-Target |
|---------|--------|-----------|-------|----------------------|
| [Outcome] | [Goal] | [Weekly] | [Name] | [Action plan] |
| [Process] | [Goal] | [Daily] | [Name] | [Action plan] |

SUSTAINABILITY MECHANISMS:

Hard-wiring strategies:
- [ ] Built into EHR/technology
- [ ] Added to policies/procedures
- [ ] Included in orientation/training
- [ ] Part of performance metrics
- [ ] Leadership rounding includes

Monitoring triggers:
- If [measure] drops below [threshold]: [Escalation plan]
- Monthly review by: [Person/Committee]
- Quarterly report to: [Leadership]

Course correction protocol:
- Minor deviation: [Frontline response]
- Major deviation: [Escalation to leadership]
- Sustained decline: [Re-activate improvement team]
```

### Run Chart Template

```
RUN CHART: [Measure Name]

Y-axis: [Metric]
X-axis: [Time period]

Target: ─ ─ ─ [Target line]
Median: ───── [Median line]

        |
[Value] |    *
        |      *  *
        | *        * *     *
        |             * *
        |_________________________
          [Time periods]

Annotations:
↓ [Date]: [Intervention/Event]
↓ [Date]: [Intervention/Event]

Rules for detecting improvement:
- Shift: 6+ consecutive points above/below median
- Trend: 5+ consecutive points going up or down
- Run: Points on one side of median (too many or too few)
```

---

## Quality Verification

### Project Quality Checklist

- [ ] Problem clearly defined with data
- [ ] Aim is SMART
- [ ] Team includes frontline representation
- [ ] Stakeholders identified and engaged
- [ ] Root cause analysis completed
- [ ] Measures defined (outcome, process, balancing)
- [ ] Driver diagram created
- [ ] Changes linked to drivers
- [ ] PDSA cycles documented
- [ ] Data displayed over time
- [ ] Sustainability plan in place

### Common QI Pitfalls to Avoid

- Starting without baseline data
- Aim too vague or too ambitious
- Testing too much at once
- Not involving frontline staff
- Declaring success too early
- No sustainability plan
- Ignoring balancing measures
- Implementing before testing

---

## False-Positive Prevention

❌ **DON'T:**
- Invent baseline performance, targets, or measure values to complete the charter.
- Write a vague aim ("improve patient satisfaction") with no number, population, or deadline.
- Define an outcome measure with no clear numerator/denominator or data source.
- Skip balancing measures, masking harm caused by the intervention.
- Recommend only education/policy and call it an improvement, or plan full rollout before any PDSA test.

✅ **DO:**
- Build on supplied baseline data; make baseline collection step one when it's missing.
- Write a SMART aim and a balanced outcome/process/balancing measure set with explicit definitions.
- Link change ideas to drivers and test them in small PDSA cycles first.
- Include balancing measures and a control/sustainability plan.
- Stay genuinely useful: produce an actionable charter plus a concrete first PDSA cycle.

---

## Dual-Failure Prevention (QA-20)

This prompt must avoid **both** failure modes:

- **Failure of commission (harmful):** fabricating baseline numbers or targets, ignoring balancing measures (so a "win" hides patient harm), or scaling an untested change broadly.
- **Failure of omission (useless):** producing a generic, number-free plan ("engage stakeholders, educate staff, monitor") with no measurable aim, no driver logic, and no test.

The correct output is measurable *and* safe: a SMART aim grounded in real baseline data, a balanced measure set including balancing measures, driver-linked change ideas tested via PDSA, and a sustainability plan — flagged for institutional oversight.

---

## Example Output

```
QI PROJECT CHARTER (excerpt) — Reduce CAUTI on Unit 5West

PROBLEM: Baseline CAUTI rate 3.1/1000 catheter-days (supplied Q1 data),
above system target of 1.5. Driven by prolonged catheter days.

AIM (SMART): By Dec 31, reduce CAUTI rate on 5West from 3.1 to ≤1.5/1000
catheter-days by cutting unnecessary catheter days.

MEASURES:
- Outcome: CAUTI rate (NHSN-defined infections / 1000 catheter-days). Source: IP surveillance. Monthly.
- Process: % catheters with a documented daily necessity review. Source: chart audit. Weekly.
- Balancing: # of unplanned re-catheterizations + CAUDI/skin breakdown reports. Weekly.

DRIVER → CHANGE IDEA:
- Primary driver: timely catheter removal → Change: nurse-driven removal protocol (PDSA #1).

PDSA #1: Test nurse-driven removal on 5 patients × 1 week; measure % reviewed.
Decision: adopt / adapt / abandon based on results.

CONTROL PLAN: hard-wire daily necessity review into EHR rounding checklist;
monthly run-chart review by unit council. [Confirm IRB-exempt QI status with institution.]
```

---

## Verification

- [ ] Project anchored in real baseline data (or baseline collection is step one).
- [ ] Aim is SMART; measure set includes outcome, process, and balancing measures with definitions.
- [ ] Methodology and driver logic grounded in established QI science.
- [ ] Change ideas linked to drivers and tested via small PDSA cycles before spread.
- [ ] Sustainability/control plan present; frontline stakeholders engaged.
- [ ] No fabricated baselines, targets, or measure data; IRB/oversight flagged.
- [ ] Avoids both fabrication/ignored-balancing-measures and a vague, number-free plan (QA-20).

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Opens with a single-sentence objective scoping the tool to data-grounded QI design.
- **ST-02 (Structured Sequential Instructions):** Charter → measures → driver diagram → PDSA → control plan flow.
- **RT-02 (Multi-Dimensional Reasoning):** Reasons across aim, measurement, stakeholders, barriers, and sustainability dimensions.
- **DS-02 (Evidence-Based Standards):** Applies Model for Improvement, Lean, and DMAIC frameworks and balanced measurement.
- **QA-01 (Self-Verification):** Project quality checklist and pitfall list before finalizing.
- **QA-20 (Dual-Failure Prevention):** Guards against both fabricated/balancing-blind plans and vague, unmeasurable ones.

---

## Related Prompts

- `domain-healthcare-clinical/prompts/quality/medicine_adverse_event_analyzer.md` — supplies the root causes a QI project is designed to address.
- `domain-healthcare-clinical/prompts/communication/medicine_handoff_communication.md` — a common QI target area (transition safety).
- `domain-healthcare-clinical/prompts/education/medicine_literature_synthesizer.md` — grounds change ideas in the evidence base.

---

**Critical Reminder:** Quality improvement is a team sport requiring engagement, iteration, and persistence. This framework provides structure but success depends on leadership support, frontline engagement, and commitment to data-driven decision making. All QI projects should align with organizational priorities and follow institutional processes for approval and oversight.
