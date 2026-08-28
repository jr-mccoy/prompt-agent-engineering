---
title: "Remediation Pathway Designer (MTSS/RTI + Competency-Based)"
category: education-teaching/program/curriculum-design
description: "Design a remediation pathway for learners who haven't reached an expected level — K-12 MTSS/RTI tiered intervention, HE/workforce competency-based remediation, or med-ed milestone remediation — with diagnostic logic, intervention dose, monitoring cadence, and exit criteria."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - DS-02
  - QA-01
  - ED-01
difficulty: advanced
tags:
  - education
  - curriculum-design
  - remediation
  - mtss
  - rti
  - competency-based-remediation
  - k12
  - higher-ed
  - workforce
  - medical-education
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/program/curriculum-design/program_milestone_alignment_designer.md
  - domain-education-teaching/program/curriculum-design/program_progression_map_designer.md
  - ../program-outcomes-assessment/teaching_program_gap_analysis.md
  - domain-education-teaching/program/curriculum-design/program_unit_design_advanced.md
---

# Remediation Pathway Designer

**Objective:** Design a remediation pathway for learners who haven't reached an expected level on a standard, competency, milestone, or progression point. Parameterized for K-12 MTSS/RTI tiered intervention, higher-ed/workforce competency-based remediation, or medical-education milestone/EPA remediation. Output: a structured pathway with diagnostic logic, intervention dose, progress monitoring, exit criteria, and decision rules for escalation.

## When to Use
- ✅ K-12: designing MTSS/RTI Tier 1/2/3 protocols for academic or behavioral standards
- ✅ HE: designing competency-based remediation when a student fails an outcome
- ✅ Workforce/apprenticeship: re-skilling pathway after failed competency demonstration
- ✅ Medical education: remediation plan after milestone or EPA not met
- ❌ Designing a complete competency framework (use the framework designer)
- ❌ Diagnosing learning difficulty for an individual (this is a system-level design)

## Inputs Required
- **Sector:** K-12 / HE / Workforce / Med-Ed
- **What's being remediated:** standard / competency / milestone / EPA / skill — with identifier and target level
- **Diagnostic data available:** assessment results, observation notes, prior remediation attempts
- **Tier or stakes:** Tier 1 (universal classroom support) / Tier 2 (small-group targeted) / Tier 3 (individual intensive); or for HE/workforce: informal support / formal remediation plan / probation
- **Available resources:** intervention specialists, tutoring, supplemental materials, simulation, supervised practice opportunities
- **Time constraints:** how long until next checkpoint
- **Regulatory frame:** IDEA/504 implications (K-12), academic integrity (HE), licensure boundaries (med-ed/workforce)

## Constraints

**Must:**
- Tier the response: lighter-touch interventions before intensive
- Specify diagnostic question: what is the hypothesis about why the learner is stuck?
- Specify intervention dose: frequency, duration, group size, materials
- Specify progress-monitoring cadence and measure
- Specify exit criteria (what counts as successful remediation)
- Specify escalation criteria (when to move to higher tier)
- Specify resolution if remediation fails (alternative pathway, repeat attempt, withdrawal — sector-appropriate)
- Honor due-process requirements

**Must Not:**
- Default to "more time on task" without diagnostic basis
- Apply the same intervention regardless of root cause
- Skip progress monitoring (intervention without monitoring is hope, not plan)
- Generate punitive structures without supportive elements
- Skip due-process or accommodation considerations

## Instructions

1. **Confirm inputs.** Echo sector, target, diagnostic data, tier/stakes, resources, time, regulatory frame.

2. **Generate diagnostic hypotheses.**
   - K-12 academic: prerequisite skill gap, attendance/engagement, language, processing, executive function, instructional fit
   - K-12 behavior: skill deficit vs. performance deficit; function of behavior (escape, attention, sensory, tangible)
   - HE/workforce: knowledge gap, skill gap, integration gap, motivation, life circumstances, mismatch
   - Med-ed: knowledge, clinical reasoning, procedural skill, professionalism, communication, system navigation

3. **Match intervention to hypothesis.**
   - Each hypothesis maps to a different intervention class.
   - Pre-skill gap → targeted preteach
   - Engagement → motivational + relational
   - Procedural skill → deliberate practice with feedback
   - Integration → case-based / scenario practice

4. **Specify intervention dose.**
   - K-12 Tier 2: typically 20-30 min, 3-5x/week, 8-12 weeks, small group
   - K-12 Tier 3: 30-45 min, 5x/week, individual or very small group
   - HE/workforce: defined contact hours per week, defined duration
   - Med-ed: defined supervised practice sessions, specific learning activities

5. **Specify progress monitoring.**
   - Measure (CBM, brief probe, work sample, OSCE, supervisor rating)
   - Cadence (weekly for K-12 Tier 2/3; biweekly to monthly for HE/med-ed)
   - Decision rule (data trend lines, percentage of target met)

6. **Specify exit and escalation.**
   - Exit criteria: success threshold over multiple data points
   - Escalation criteria: insufficient progress after defined window; what does next tier look like?
   - Maintenance plan: how is gain consolidated post-exit?

7. **Specify failure resolution.**
   - K-12: special education referral, IEP team meeting
   - HE: course repeat, program adjustment, withdrawal options
   - Workforce: alternative credential pathway, withdrawal
   - Med-ed: extended training, alternative role, performance improvement plan, termination per program policy

8. **Embed due process and equity.**
   - Notification to learner/family
   - Documentation requirements
   - Appeal/review
   - Accommodations integration
   - Equity audit (do remediation rates vary systematically by demographics?)

## Output Format

### Section 1: Pathway Identity
- Sector, target, tier/stakes, resources, time, regulatory frame

### Section 2: Diagnostic Logic

| Hypothesis | Diagnostic Probe | If Confirmed → Intervention Class |
|---|---|---|

### Section 3: Intervention Specifications

For the selected intervention(s):

| Element | Specification |
|---|---|
| Intervention name/type | |
| Dose (frequency × duration × weeks) | |
| Group size | |
| Materials | |
| Instructor/provider | |
| Setting | |
| Hypothesis it addresses | |

### Section 4: Progress Monitoring

| Measure | Cadence | Decision Rule | Who Reviews |
|---|---|---|---|

### Section 5: Exit, Escalation, Failure Resolution

| Outcome | Criteria | Next Step |
|---|---|---|
| Exit (success) | | Maintenance plan |
| Escalation | | Next tier or modification |
| Failure resolution | | [sector-appropriate] |

### Section 6: Due Process & Equity

| Element | Specification |
|---|---|
| Notification | |
| Documentation | |
| Appeal/review | |
| Accommodations integration | |
| Equity monitoring | |

### Section 7: Pathway Audit

| Audit Question | Result |
|---|---|
| Tiered response (lighter before intensive) | Pass / Fail |
| Diagnostic basis for intervention | Pass / Fail |
| Dose specified | Pass / Fail |
| Progress monitoring with decision rule | Pass / Fail |
| Exit and escalation criteria | Pass / Fail |
| Failure resolution pathway | Pass / Fail |
| Due process embedded | Pass / Fail |
| Equity monitoring | Pass / Fail |

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Generic "extra practice" | Without diagnostic basis, often misdirected | Match intervention to hypothesized cause |
| Same intervention regardless of root cause | Wastes time and demoralizes learners | Differential diagnosis → differential intervention |
| No progress monitoring | Intervention is hope, not plan | Build measure + cadence + decision rule |
| Skipping due process | Legal and ethical exposure | Notification, documentation, appeal |
| Punitive without support | Worsens outcomes; equity harm | Pair accountability with structured support |
| Indefinite remediation | Learners trapped in loops | Time-bounded with explicit escalation/exit |
| Ignoring demographic patterns | Disproportionate remediation hides systemic issues | Equity monitoring built in |
| Generic K-12 plan that doesn't honor IDEA/504 | Violates federal law | Honor MTSS/RTI procedures and special-education referral logic |

## Verification Checklist

- [ ] Tiered response with lighter before intensive
- [ ] Diagnostic hypotheses generated
- [ ] Intervention matches hypothesis
- [ ] Dose specified
- [ ] Progress monitoring with decision rule
- [ ] Exit and escalation criteria
- [ ] Failure resolution pathway
- [ ] Due process embedded
- [ ] Equity monitoring built in
- [ ] Regulatory frame honored
