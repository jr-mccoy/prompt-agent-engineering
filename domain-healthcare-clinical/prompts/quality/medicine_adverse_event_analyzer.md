---
title: "Adverse Event Analyzer"
category: healthcare-clinical/quality
description: "Systematically analyze clinical adverse events with root-cause-analysis frameworks (timeline, 5 Whys, multi-level factor classification) to identify system-level root causes over individual blame, and generate impact-and-feasibility-prioritized, intervention-hierarchy-aware action plans — supporting, not replacing, formal incident investigation."
techniques:
  - ST-01
  - RT-02
  - DS-02
  - QA-01
  - QA-20
  - CM-02
difficulty: advanced
tags:
  - patient-safety
  - root-cause-analysis
  - human-factors
  - just-culture
  - quality-improvement
updated: "2026-06-07"
related_prompts:
  - domain-healthcare-clinical/prompts/quality/medicine_quality_improvement.md
  - domain-healthcare-clinical/prompts/communication/medicine_handoff_communication.md
  - domain-healthcare-clinical/prompts/pharmacology/medicine_drug_interaction_checker.md
---

# Adverse Event Analyzer

**Objective:** Systematically analyze clinical adverse events using root cause analysis frameworks, identifying contributing factors at individual, team, system, and organizational levels, and generating actionable recommendations prioritized by impact and feasibility.

**Important Disclaimer:** This tool supports quality improvement and patient safety analysis. It does not replace formal incident investigation processes, legal review, or regulatory compliance requirements. All analyses should be conducted by qualified patient safety professionals.

**When to use:**
- Structuring a root cause analysis of a sentinel event, adverse event, near miss, or precursor event.
- Moving an investigation from individual blame toward system-level root causes.
- Building an intervention-hierarchy-aware, prioritized action plan with owners and measures.
- Teaching RCA method, human factors, and just-culture principles.

**When NOT to use:**
- As a replacement for the organization's formal, multidisciplinary incident-investigation process.
- For legal/peer-review determinations or regulatory reporting decisions.
- Without psychological safety and leadership support for a just-culture review.

**Audience:** Patient safety professionals, quality/risk managers, clinical leaders, RCA teams, and safety-improvement learners.

---

## Inputs / Context

Provide the event data below using de-identified descriptors (roles, not names). Paste source material (chart excerpts, statements, timelines) wrapped in an `<event_data>` tag so it can be referenced by name; analyze only what is supplied and flag information that must be gathered through formal interview/review.

---

## Input Required

### Event Description

**Event Type:**
- [ ] Sentinel event (serious harm or death)
- [ ] Adverse event (harm occurred)
- [ ] Near miss (harm prevented by chance or intervention)
- [ ] Precursor event (unsafe condition identified)

**Event Summary:**
- Date/Time of event: [When]
- Location: [Where - unit, room, area]
- Patient involved: [De-identified descriptor]
- Staff involved: [Roles, not names]
- What happened: [Factual description]
- Outcome: [Patient impact]

### Discovery and Response

**How discovered:** [Who found it and when]
**Immediate actions taken:** [What was done]
**Current patient status:** [If applicable]

---

## Constraints

### Must
- Drive analysis to **system-level root causes**, not "human error" or "failed to follow policy"; apply systems thinking and human-factors principles.
- Ground factor classification and intervention strength in established frameworks (5 Whys, Swiss cheese, action/intervention hierarchy); cite the framework type.
- Prioritize **stronger interventions** (eliminate / substitute / engineering controls) over weak ones (training / policy alone).
- Give each action a **named owner, timeline, and success measure**, and a monitoring plan.
- Use **de-identified, role-based** language; keep the analysis blame-free and just-culture aligned.
- Base findings on the supplied evidence; flag what must still be gathered — never fabricate timeline events, statements, or contributing factors.

### Must Not
- Do not replace the organization's formal incident-investigation, peer-review, or legal processes.
- Do not name or blame individuals, or stop the analysis at proximate cause.
- Do not invent events, quotes, or factors not supported by the supplied data.
- Do not recommend only education/policy when a stronger system fix is feasible.

---

## Root Cause Analysis Framework

### Phase 1: Event Reconstruction

**Timeline Development**

Create detailed chronological sequence:

```
EVENT TIMELINE

[Date -X]: [Relevant preceding events/conditions]

[Date, Time 1]: [Event/Action/Decision]
  - Who: [Role]
  - What: [Specific action or inaction]
  - Context: [Circumstances]

[Date, Time 2]: [Event/Action/Decision]
  - Who: [Role]
  - What: [Specific action or inaction]
  - Context: [Circumstances]

[Continue through event...]

[Time of Event]: [The adverse event]

[Post-event Time]: [Discovery and response]
```

**Information Gathered From:**
- [ ] Medical record review
- [ ] Staff interviews
- [ ] Patient/family interviews
- [ ] Witness statements
- [ ] Equipment inspection
- [ ] Environmental assessment
- [ ] Policy/procedure review

### Phase 2: Contributing Factor Analysis

**The "5 Whys" Deep Dive**

For the primary proximate cause:

```
WHY CHAIN ANALYSIS

Event: [The adverse event]

Why 1: Why did this happen?
→ [First-level cause]

Why 2: Why did [first-level cause] occur?
→ [Second-level cause]

Why 3: Why did [second-level cause] occur?
→ [Third-level cause]

Why 4: Why did [third-level cause] occur?
→ [Fourth-level cause]

Why 5: Why did [fourth-level cause] occur?
→ [Root cause - usually system-level]
```

Repeat for additional causal chains if multiple proximate causes identified.

### Phase 3: Multi-Level Factor Classification

**Human Factors Analysis (Individual Level)**

```
INDIVIDUAL FACTORS

Knowledge/Skill Factors:
- [ ] Inadequate training
- [ ] Lack of experience
- [ ] Competency gaps
- [ ] Unfamiliarity with equipment
- Details: [Specific findings]

Cognitive Factors:
- [ ] Fatigue
- [ ] Distraction/interruption
- [ ] Cognitive overload
- [ ] Confirmation bias
- [ ] Fixation error
- Details: [Specific findings]

Physical/Physiological:
- [ ] Fatigue (acute/chronic)
- [ ] Illness
- [ ] Impairment
- Details: [Specific findings]

Behavioral:
- [ ] Deviation from protocol
- [ ] Shortcuts taken
- [ ] Risk normalization
- Details: [Specific findings]
```

**Team Factors**

```
TEAM FACTORS

Communication:
- [ ] Handoff failure
- [ ] Unclear communication
- [ ] Information not shared
- [ ] Language barriers
- [ ] Communication hierarchy barriers
- Details: [Specific findings]

Teamwork:
- [ ] Role confusion
- [ ] Leadership gaps
- [ ] Lack of mutual monitoring
- [ ] Failure to speak up
- [ ] Inadequate briefing/debriefing
- Details: [Specific findings]

Supervision:
- [ ] Inadequate supervision
- [ ] Unavailable supervision
- [ ] Unclear chain of command
- Details: [Specific findings]
```

**Environmental/Equipment Factors**

```
ENVIRONMENTAL FACTORS

Physical Environment:
- [ ] Lighting inadequate
- [ ] Noise excessive
- [ ] Workspace layout
- [ ] Crowding
- [ ] Temperature
- Details: [Specific findings]

Equipment:
- [ ] Equipment malfunction
- [ ] Poor equipment design
- [ ] Look-alike/sound-alike issues
- [ ] Maintenance failure
- [ ] Equipment unavailable
- Details: [Specific findings]

Technology:
- [ ] EHR design issue
- [ ] Alert fatigue
- [ ] System downtime
- [ ] Technology workarounds
- Details: [Specific findings]
```

**Organizational/System Factors**

```
ORGANIZATIONAL FACTORS

Policies & Procedures:
- [ ] Policy absent
- [ ] Policy outdated
- [ ] Policy unclear
- [ ] Policy not followed (why?)
- [ ] Conflicting policies
- Details: [Specific findings]

Staffing:
- [ ] Inadequate staffing levels
- [ ] Skill mix inappropriate
- [ ] High turnover
- [ ] Float/agency staff
- [ ] Excessive workload
- Details: [Specific findings]

Culture:
- [ ] Production pressure
- [ ] Safety not prioritized
- [ ] Fear of reporting
- [ ] Blame culture
- [ ] Poor safety culture scores
- Details: [Specific findings]

Training & Education:
- [ ] Inadequate orientation
- [ ] No ongoing competency verification
- [ ] Simulation training lacking
- [ ] No team training
- Details: [Specific findings]

External Factors:
- [ ] Regulatory requirements
- [ ] Payor pressures
- [ ] Supply chain issues
- [ ] Community/pandemic factors
- Details: [Specific findings]
```

### Phase 4: Root Cause Identification

**Distinguishing Root Causes from Contributing Factors:**

Root causes are:
- System-level (not individual-level)
- Addressable with sustainable interventions
- Fundamental (addressing them prevents recurrence)
- Not simply "human error" or "failed to follow policy"

```
ROOT CAUSE DETERMINATION

Root Cause 1:
[Statement in system terms]

Evidence supporting this root cause:
- [Evidence 1]
- [Evidence 2]

Why this is root (not proximate):
[Explanation of how this is fundamental]

---

Root Cause 2:
[Statement in system terms]

Evidence supporting this root cause:
- [Evidence 1]
- [Evidence 2]

Why this is root (not proximate):
[Explanation of how this is fundamental]
```

### Phase 5: Causal Statement

```
CAUSAL STATEMENT

This [event type] occurred because:

[Root cause 1 statement], which led to [chain of events], resulting in [harm].

Contributing factors included:
- [Factor 1] at the [level] level
- [Factor 2] at the [level] level
- [Factor 3] at the [level] level

The harm could have been prevented if:
- [Prevention point 1]
- [Prevention point 2]
```

---

## Action Planning Framework

### Intervention Hierarchy

**Stronger Interventions (Preferred):**

| Strength | Type | Examples |
|----------|------|----------|
| Strongest | Eliminate hazard | Remove dangerous medication from unit |
| Strong | Substitute | Replace error-prone process with safer one |
| Strong | Engineering controls | Physical barriers, forcing functions, automation |
| Strong | Simplification | Reduce steps, standardize |

**Weaker Interventions (Supplement Only):**

| Strength | Type | Examples |
|----------|------|----------|
| Weak | Administrative controls | Policies, checklists, double-checks |
| Weak | Warnings/labels | Signs, alerts, color coding |
| Weakest | Training/education | Training programs, competencies |

### Action Plan Development

```
ACTION PLAN

For each root cause, develop interventions:

ROOT CAUSE 1: [Statement]

Intervention 1A: [Description]
- Type: [Eliminate/Substitute/Engineering/etc.]
- Strength: [Strong/Moderate/Weak]
- Owner: [Person/Department responsible]
- Timeline: [Target date]
- Resources needed: [Budget, FTE, etc.]
- Success measure: [How we'll know it worked]

Intervention 1B: [Description]
- Type: [Type]
- Strength: [Strength]
- Owner: [Owner]
- Timeline: [Date]
- Resources needed: [Resources]
- Success measure: [Measure]

---

ROOT CAUSE 2: [Statement]

[Repeat intervention format]
```

### Prioritization Matrix

```
ACTION PRIORITIZATION

| Action | Impact on Safety | Feasibility | Strength | Priority |
|--------|-----------------|-------------|----------|----------|
| [A]    | High/Med/Low    | High/Med/Low| Strong   | 1        |
| [B]    | High/Med/Low    | High/Med/Low| Moderate | 2        |
| [C]    | High/Med/Low    | High/Med/Low| Weak     | 3        |

Priority Criteria:
- Impact: How much will this reduce risk?
- Feasibility: Can we actually implement this?
- Strength: Is this a strong or weak intervention?
```

---

## Output Format

### RCA Summary Report

```
═══════════════════════════════════════════════════════════════
ROOT CAUSE ANALYSIS REPORT
═══════════════════════════════════════════════════════════════

EVENT: [Brief descriptor]
DATE: [Event date]
ANALYSIS DATE: [Report date]
RCA TEAM: [Roles involved - not names]

───────────────────────────────────────────────────────────────
EXECUTIVE SUMMARY
───────────────────────────────────────────────────────────────

Event Description:
[2-3 sentence summary of what happened]

Root Causes Identified:
1. [Root cause 1 - system-level statement]
2. [Root cause 2 - system-level statement]

Priority Actions:
1. [Highest priority intervention]
2. [Second priority intervention]
3. [Third priority intervention]

───────────────────────────────────────────────────────────────
EVENT DETAILS
───────────────────────────────────────────────────────────────

[Detailed timeline and description]

───────────────────────────────────────────────────────────────
ANALYSIS FINDINGS
───────────────────────────────────────────────────────────────

Contributing Factors:

Individual Level:
- [Factor]: [How it contributed]

Team Level:
- [Factor]: [How it contributed]

Environment/Equipment Level:
- [Factor]: [How it contributed]

Organization/System Level:
- [Factor]: [How it contributed]

───────────────────────────────────────────────────────────────
ROOT CAUSES
───────────────────────────────────────────────────────────────

Root Cause 1: [Statement]
Evidence: [Supporting evidence]

Root Cause 2: [Statement]
Evidence: [Supporting evidence]

Causal Statement:
[Integrated causal statement]

───────────────────────────────────────────────────────────────
ACTION PLAN
───────────────────────────────────────────────────────────────

| # | Action | Type | Owner | Due | Measure |
|---|--------|------|-------|-----|---------|
| 1 | [Action]|[Type]|[Owner]|[Date]|[Measure]|
| 2 | [Action]|[Type]|[Owner]|[Date]|[Measure]|

───────────────────────────────────────────────────────────────
MONITORING PLAN
───────────────────────────────────────────────────────────────

Outcome Measures:
- [Measure 1]: [Target] - Monitored [frequency]
- [Measure 2]: [Target] - Monitored [frequency]

Process Measures:
- [Measure 1]: [Target] - Monitored [frequency]

Review Schedule:
- 30-day check: [Date]
- 60-day check: [Date]
- Sustainability review: [Date]

───────────────────────────────────────────────────────────────
SPREAD AND SPREAD ANALYSIS
───────────────────────────────────────────────────────────────

Could this happen elsewhere?
- [Unit/area 1]: Risk assessment [High/Med/Low]
- [Unit/area 2]: Risk assessment [High/Med/Low]

Recommendations for spread:
- [Recommendation]

═══════════════════════════════════════════════════════════════
```

---

## Quality Verification

### RCA Quality Checklist

Before finalizing analysis:

- [ ] Timeline is accurate and complete
- [ ] All data sources reviewed
- [ ] Contributing factors at all levels considered
- [ ] Root causes are truly system-level (not "human error")
- [ ] "5 Whys" completed to sufficient depth
- [ ] Causal statement is logical and evidence-based
- [ ] Actions address root causes (not just proximate causes)
- [ ] Actions include strong interventions (not just education/policy)
- [ ] Each action has owner, timeline, and measure
- [ ] Monitoring plan established

### Common RCA Pitfalls

**Avoid:**
- Stopping at "human error" or "failed to follow policy"
- Accepting proximate causes as root causes
- Blaming individuals instead of systems
- Recommending only training and policy changes
- Creating actions without clear ownership
- No plan to measure effectiveness

**Instead:**
- Ask "Why did the system allow this to happen?"
- Dig deeper with "5 Whys"
- Focus on system redesign
- Prioritize engineering controls and forcing functions
- Assign specific owners with authority
- Define measurable outcomes

---

## Human Factors Principles

### Key Concepts to Apply

**Systems Thinking:**
- Errors are symptoms of system problems
- People do not come to work to make mistakes
- Sharp end (frontline) vs. blunt end (leadership)
- Swiss cheese model - multiple barriers

**Error Types:**
- Slips: Unintentional action (right intention, wrong action)
- Lapses: Memory failure (forgot step)
- Mistakes: Wrong plan (wrong intention, executed correctly)
- Violations: Deliberate deviation (routine, situational, exceptional)

**High Reliability Principles:**
- Preoccupation with failure
- Reluctance to simplify
- Sensitivity to operations
- Commitment to resilience
- Deference to expertise

---

## False-Positive Prevention

❌ **DON'T:**
- Fabricate timeline events, witness statements, or contributing factors not supported by the supplied data.
- Stop at "human error" / "failed to follow policy" and call it a root cause.
- Name or implicitly blame individuals instead of describing the system that allowed the failure.
- Recommend only training and policy reminders when an engineering control or forcing function is feasible.
- Produce a generic "improve communication and education" plan with no owners, measures, or system fix.

✅ **DO:**
- Analyze only the supplied evidence; flag what must still be gathered through formal interview/review.
- Drive each causal chain to a system-level root cause using the 5 Whys.
- Keep language de-identified, role-based, and just-culture aligned.
- Prioritize stronger interventions and attach owner, timeline, and measure to each action.
- Stay genuinely useful: deliver a concrete, prioritized action plan with a monitoring plan.

---

## Dual-Failure Prevention (QA-20)

This prompt must avoid **both** failure modes:

- **Failure of commission (harmful):** fabricating events/factors, assigning individual blame, or asserting a root cause the evidence does not support — which can produce wrong fixes and unjust outcomes.
- **Failure of omission (useless):** producing a blame-free but vacuous analysis ("communication broke down; re-educate staff") with no system-level root cause, no strong interventions, and no measurable actions.

The correct output is rigorous *and* fair: evidence-grounded system-level root causes, strong-intervention-weighted actions with owners/measures, and explicitly flagged information gaps — framed as support for, not a replacement of, the formal investigation.

---

## Example Output

```
ROOT CAUSE ANALYSIS REPORT (decision support — supplements formal investigation)

EVENT: Wrong-dose insulin administered (near miss, caught before harm)
ANALYSIS DATE: 06/07
RCA TEAM: Nursing, pharmacy, informatics, safety (roles only)

EXECUTIVE SUMMARY
A nurse drew up a 10x insulin dose; a second nurse caught it pre-administration.
Root causes are system-level, not individual.

ROOT CAUSES
1. Look-alike vial concentrations stored adjacently with no forcing function.
   Evidence: timeline + storage layout (supplied). System-level: design allows the error.
2. Independent double-check policy existed but workflow made it easy to bypass.
   Evidence: staff statements (supplied). Why root: policy relied on memory, not design.

ACTION PLAN (intervention-hierarchy weighted)
| # | Action | Type | Owner | Due | Measure |
| 1 | Remove high-concentration vial from floor stock (eliminate) | Strong | Pharmacy mgr | 30d | Vial absent on audit |
| 2 | Barcode-scan hard stop for insulin (engineering) | Strong | Informatics | 90d | % scanned doses |
| 3 | Reinforce independent double-check (administrative) | Weak | Nurse educator | 30d | Audit compliance |

MONITORING: weekly insulin-error reports; 30/60/sustainability reviews.

INFORMATION GAPS (flag for formal review): staffing levels at time of event not supplied.
```

---

## Verification

- [ ] Timeline and factors are evidence-based; gaps for formal review are flagged (nothing fabricated).
- [ ] Root causes are system-level, reached via 5 Whys (not "human error").
- [ ] Language is de-identified, role-based, and blame-free.
- [ ] Action plan prioritizes stronger interventions over education/policy alone.
- [ ] Each action has owner, timeline, and success measure; monitoring plan present.
- [ ] Framed as support for the formal investigation, not a replacement.
- [ ] Avoids both fabrication/individual blame and a vacuous, action-free plan (QA-20).

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Opens with a single-sentence objective scoping the tool to system-level RCA supporting formal investigation.
- **RT-02 (Multi-Dimensional Reasoning):** Classifies factors across individual, team, environment/equipment, and organizational levels.
- **DS-02 (Evidence-Based Standards):** Applies established RCA, human-factors, and intervention-hierarchy frameworks to ground findings.
- **QA-01 (Self-Verification):** RCA quality checklist and pitfall list before finalizing.
- **QA-20 (Dual-Failure Prevention):** Guards against both fabrication/individual blame and vacuous, action-free analysis.
- **CM-02 (Constraint / Safety Framing):** Hard constraints on just-culture, de-identification, no fabrication, and formal-process framing.

---

## Related Prompts

- `domain-healthcare-clinical/prompts/quality/medicine_quality_improvement.md` — turns RCA root causes into a structured QI project with PDSA cycles.
- `domain-healthcare-clinical/prompts/communication/medicine_handoff_communication.md` — addresses handoff failures frequently implicated in adverse events.
- `domain-healthcare-clinical/prompts/pharmacology/medicine_drug_interaction_checker.md` — supports analysis of medication-related adverse events.

---

**Critical Reminder:** Effective RCA requires psychological safety, commitment to just culture, and leadership support. This tool provides structure but cannot replace the organizational commitment to learning rather than blaming. All analyses should be conducted with appropriate quality and risk management oversight.
