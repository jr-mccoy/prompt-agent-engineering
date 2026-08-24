---
title: "Family Therapy Intake — Systemic (Genogram + Presenting-Problem Mapping)"
category: psychology/populations/cross-population
description: "Systemic family intake that builds a three-generation genogram, maps the presenting problem across the family system, reframes the identified patient, and assesses boundaries and subsystems, producing a CPT 90847/90846 family diagnostic record."
techniques:
  - ST-04
  - RT-02
  - RT-04
  - CM-02
  - QA-04
difficulty: advanced
intended_use: model-testing
tags:
  - family-therapy
  - systemic
  - genogram
  - bowen
  - structural
  - circular-questioning
  - identified-patient
  - cpt-90847
  - cpt-90846
updated: "2026-06-08"
related_prompts:
  - domain-psychology/populations/cross-population/psychology_couples_therapy_intake_eft_or_gottman.md
  - domain-psychology/documentation/psychology_intake_assessment_note.md
  - domain-psychology/diagnostic-formulation/psychology_case_conceptualization_framework.md
  - domain-psychology/treatment-planning/psychology_modality_selection_decision_aid.md
---

# Family Therapy Intake — Systemic (Genogram + Presenting-Problem Mapping)

## Objective

Produce a systemic family-therapy intake record that:

1. Constructs a **three-generation genogram** capturing structure, relationships, repetitive patterns, and transmitted dynamics (Bowen family-systems frame).
2. Maps the **presenting problem across the family system** rather than locating it solely in the identified patient (IP), and reframes the IP language explicitly.
3. Assesses **boundaries and subsystems** (structural family therapy: enmeshment vs. disengagement, hierarchy, alliances, coalitions, triangles).
4. Uses **circular questioning** to elicit differences in perception and reciprocal influence across members.
5. Screens each present member for individual risk and family safety (violence, abuse, neglect, mandated-reporter triggers).
6. Produces a structured family intake note meeting CPT 90847 (with IP present) / 90846 (without IP present) documentation requirements.

## When to Use

- At initial intake when a family presents with a relational or child/adolescent problem framed around an "identified patient."
- When multiple household members are part of the treatment unit and the clinician needs to assess structure and process.
- When prior individual treatment has not resolved a problem maintained by family dynamics.
- When a referral (school, pediatrician, court) names a child's behavior but the system context is unclear.

## When NOT to Use

- For a dyadic couple presentation with no children/other members in the treatment unit (use `psychology_couples_therapy_intake_eft_or_gottman.md`).
- For individual adult or pediatric intake where the unit of treatment is one person.
- For custody evaluations or forensic family assessments, which require different evidence-handling and contact protocols.

## Inputs / Context Required

- **Household and family roster:** Names/initials, ages, roles, who lives in the home, who is present at intake, custody/guardianship if applicable.
- **Referral and presenting concern:** Who initiated, the stated problem, who is named as the IP.
- **Family history across three generations:** Marriages, divorces, deaths, births, cutoffs, significant illnesses, substance use, mental-health history, migration.
- **Relationship qualities:** Close/conflictual/distant/cutoff/enmeshed relationships among members.
- **Developmental/life-cycle stage:** Where the family is in its life cycle (launching, young children, adolescents, later life).
- **Cultural context:** Cultural, religious, and intergenerational norms relevant to structure and roles.
- `[clinician input required: any safety concerns — child abuse/neglect indicators, domestic violence, a member's active SI/HI — disclosed before or during the intake]`

## Constraints

### Must

- Build a three-generation genogram and document its structural facts (births, deaths, marriages, divorces, cutoffs) and relational lines (close, conflictual, distant, enmeshed, cutoff).
- Map the presenting problem systemically: identify how the problem functions in the system, who is involved in maintaining it, and what role it serves.
- Reframe the identified-patient language explicitly: state the IP framing as presented, then offer a systemic reframe that distributes the problem across the system.
- Assess boundaries and subsystems: parental/executive subsystem, sibling subsystem, cross-generational coalitions, triangles, hierarchy, enmeshment vs. disengagement.
- Use at least three circular questions in the assessment and document the differences they surfaced.
- Screen for family safety (IPV, child abuse/neglect) and document the mandated-reporter determination — even when no concerns are found.
- Assess each present member's individual risk (SI/HI/self-harm) at least at a screening level.
- Flag all `[clinician input required: ...]` gaps; do not fabricate genogram facts, history, or relationships.

### Must Not

- Do not locate the problem solely in the identified patient; a systemic intake that leaves the IP framing unchallenged has not done its job.
- Do not pathologize one member; distribute the formulation across the system.
- Do not omit the safety/mandated-reporter screen because the presentation seems benign.
- Do not fabricate three-generation history (deaths, divorces, cutoffs) the family did not report; mark unknowns as unknown.
- Do not collapse structural and Bowenian language into vague "family dysfunction"; name the specific structures (boundary type, triangle, coalition).

## Systemic Assessment Overlay

| Construct | What to assess | Where it appears in the note |
|-----------|----------------|------------------------------|
| Genogram (Bowen) | 3-gen structure, repetitive patterns, cutoffs, transmitted dynamics | Genogram section |
| Boundaries (structural) | Clear / rigid (disengaged) / diffuse (enmeshed) within and between subsystems | Structure & subsystems |
| Hierarchy (structural) | Is the executive/parental subsystem in charge? Cross-gen coalitions? | Structure & subsystems |
| Triangles (Bowen) | Who is pulled in to stabilize a dyad's tension? | Process & dynamics |
| Circular causality | Reciprocal feedback loops maintaining the problem | Presenting-problem map |
| Life-cycle stage | Transition the family is navigating | Formulation |

## Instructions

1. **Set the frame.** Explain confidentiality and its limits to all members in age-appropriate terms; clarify that the family system — not one person — is the unit of attention. Confirm consent/assent and guardianship for any minors.

2. **Take the presenting concern from multiple members.** Elicit each present member's view of the problem in their own words, including the member named as the IP.

3. **Construct the three-generation genogram.** Capture structure (marriages, divorces, deaths, births, children, cutoffs) and relational quality lines. Note repetitive patterns (substance use, estrangement, mental illness, roles) across generations.

4. **Map the presenting problem systemically.** Identify the sequence around the problem (who does what, when, in response to whom), the circular feedback loop, and what function/role the problem serves in the system.

5. **Reframe the identified patient.** State the IP framing, then offer a systemic reframe distributing the problem across the system.

6. **Assess structure and subsystems.** Boundaries (clear/rigid/diffuse), hierarchy, executive subsystem, sibling subsystem, coalitions, triangles, alliances.

7. **Use circular questioning.** Ask differences and reciprocal-influence questions; document what they revealed.

8. **Safety and individual screening.** Screen for IPV and child abuse/neglect; complete the mandated-reporter determination. Screen each present member for individual risk.

9. **Write the Family Intake Note** using the output format below.

10. **Run verification.**

## Output Format

```
=== SYSTEMIC FAMILY THERAPY INTAKE NOTE ===

Family identifier: [Surname initial]    Members present: [List, role, age]
Identified patient (as presented): [Member]    Household: [Who lives in home]
Date of Service: [YYYY-MM-DD]    Time: [HH:MM–HH:MM]
Clinician: [Name, credentials]
CPT: [90847 (family WITH patient present) | 90846 (family WITHOUT patient present)]    Duration: [N minutes]
Consent / assent / guardianship for minors: [Documented — details]
Confidentiality and its limits explained to all members: [Yes]

─────────────────────────────────────────
PRESENTING CONCERN (MULTIPLE PERSPECTIVES)
─────────────────────────────────────────
Referral source: [...]    Who initiated: [...]
Member views of the problem (each in their own words):
  [Member A]: "[...]"
  [Member B]: "[...]"
  [Identified patient]: "[...]"
Recent precipitant: [...]

─────────────────────────────────────────
THREE-GENERATION GENOGRAM
─────────────────────────────────────────
Generation 1 (grandparents): [Names/initials, status (living/deceased + year), marriages/divorces, notable history: substance use, mental illness, cutoffs]
Generation 2 (parents + their siblings): [Same fields; including the identified patient's parents]
Generation 3 (children / identified patient's generation): [Same fields]

Relational lines noted:
  Close: [Pairs]
  Conflictual: [Pairs]
  Distant / cutoff: [Pairs]
  Enmeshed: [Pairs]

Repetitive multigenerational patterns: [e.g., paternal-line estrangement; transmitted substance use; over-responsible eldest-child role]
Unknown / not reported: [Mark gaps — do not fabricate]

─────────────────────────────────────────
PRESENTING-PROBLEM SYSTEMIC MAP
─────────────────────────────────────────
Problem sequence (circular): [Who does what → who responds how → feedback loop]
Function/role the problem serves in the system: [e.g., detours marital conflict; maintains parental alliance; regulates distance]
Triangles involved: [Dyad in tension + third member pulled in]
IDENTIFIED-PATIENT REFRAME:
  As presented: "[The problem is X's behavior.]"
  Systemic reframe: "[The problem is better understood as ... — distribute across the system]"

─────────────────────────────────────────
STRUCTURE AND SUBSYSTEMS (STRUCTURAL FRAME)
─────────────────────────────────────────
Executive / parental subsystem: [In charge / undermined / absent — describe; cross-generational coalition: Yes/No]
Sibling subsystem: [Cohesive / conflictual / parentified child present: ...]
Boundaries:
  Within parental subsystem: [Clear / rigid / diffuse]
  Parent–child: [Clear / rigid (disengaged) / diffuse (enmeshed)]
  Family–outside world: [Open / rigid / diffuse]
Hierarchy: [Appropriate / inverted / contested]
Coalitions / alliances: [Describe]

─────────────────────────────────────────
CIRCULAR QUESTIONING — DIFFERENCES SURFACED
─────────────────────────────────────────
Q1: [Question asked] → [Difference revealed]
Q2: [Question asked] → [Difference revealed]
Q3: [Question asked] → [Difference revealed]

─────────────────────────────────────────
FAMILY LIFE CYCLE AND CULTURAL CONTEXT
─────────────────────────────────────────
Life-cycle stage / transition: [Launching / adolescents / young children / later life — and the strain it creates]
Cultural / religious / intergenerational norms relevant to structure and roles: [...]

─────────────────────────────────────────
SAFETY AND MANDATED-REPORTER SCREEN
─────────────────────────────────────────
Intimate-partner violence in home: [None / Disclosed — describe]
Child abuse / neglect indicators: [None / Present — describe]
Member individual risk (SI / HI / self-harm), per present member: [Member — finding]
MANDATED-REPORTER DETERMINATION: [No report indicated — basis / Report filed — agency, date/time, report #]

─────────────────────────────────────────
SYSTEMIC FORMULATION
─────────────────────────────────────────
[Narrative integrating genogram patterns, structural findings (boundaries/hierarchy/coalitions), the circular maintenance loop, the function of the problem, life-cycle strain, and family strengths. Avoid pathologizing a single member.]

Strengths and resources: [Relational, cultural, community]

─────────────────────────────────────────
DIAGNOSTIC AND PROBLEM CODING
─────────────────────────────────────────
Relational Z-codes: [Z63.8 Other specified problems related to primary support group / Z62.820 Parent-child relational problem / Z63.0 — as applicable]
Individual diagnoses (any member, if warranted): [F##.## — note systemic context]

─────────────────────────────────────────
TREATMENT RECOMMENDATIONS
─────────────────────────────────────────
Modality: [Structural / Bowenian / Strategic / integrative family therapy — rationale]
Unit of treatment: [Whole family / parental subsystem / specific dyad — sequence]
Initial systemic targets: [Restructure a boundary / detriangulate / strengthen executive subsystem / interrupt the loop]
Frequency: [...]    Adjunct individual treatment for any member: [...]
School/medical coordination if minor involved: [...]

─────────────────────────────────────────
BILLING NOTE
─────────────────────────────────────────
CPT: [90847 when the identified patient is present in the family session; 90846 when family is seen WITHOUT the identified patient present, for treatment of the patient]. Do not bill both for the same session; choose based on IP presence.
Payer: [...]    Authorization: [Not required / Auth # ___]
```

## Verification

- [ ] Three-generation genogram constructed with structural facts and relational lines; unknowns marked, not fabricated.
- [ ] Presenting problem mapped systemically (circular sequence + function in the system), not located solely in the IP.
- [ ] Identified-patient framing stated AND reframed across the system.
- [ ] Boundaries, hierarchy, subsystems, coalitions, and triangles assessed using structural/Bowenian language.
- [ ] At least three circular questions documented with the differences they surfaced.
- [ ] IPV and child abuse/neglect screen completed; mandated-reporter determination documented even when negative.
- [ ] Each present member screened for individual risk (SI/HI/self-harm).
- [ ] Formulation distributes the problem across the system and does not pathologize one member.
- [ ] Relational Z-codes and any individual diagnoses recorded.
- [ ] CPT 90847 vs. 90846 selected by IP presence; billing note included.
- [ ] Gaps flagged with `[clinician input required: ...]`; no fabricated history.
