---
title: "Learning Progression Map Designer"
category: education-teaching/program/curriculum-design
description: "Design an evidence-based learning progression for a single concept, skill, or competency — sequencing developmental waypoints from naive understanding through expert performance, with level-discriminating diagnostic probes, misconceptions framed as learner reasoning, and instructional moves at each level."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - DS-01
  - ED-01
  - QA-01
difficulty: advanced
tags:
  - education
  - curriculum-design
  - learning-progression
  - developmental-sequence
  - formative-assessment
  - k12
  - workforce
  - medical-education
updated: "2026-07-18"
related_prompts:
  - domain-education-teaching/program/curriculum-design/program_milestone_alignment_designer.md
  - domain-education-teaching/program/curriculum-design/program_competency_framework_designer.md
  - domain-education-teaching/program/curriculum-design/program_vertical_alignment_auditor.md
  - domain-education-teaching/program/curriculum-design/program_remediation_pathway_designer.md
---

# Learning Progression Map Designer

**Objective:** Design a learning progression for a single concept, skill, or competency: an evidence-based developmental sequence from typical naive understanding through intermediate waypoints to expert performance. Every waypoint must be observable, diagnosable, and instructionally actionable — a teacher reading it should be able to (a) locate a learner on the progression from work samples or probe responses and (b) know what to do next.

## When to Use
- ✅ K-12 standards-based learning progressions (math, science, ELA, reading development)
- ✅ Skill progressions in workforce settings (apprentice → journey → master tradesperson behaviors)
- ✅ Clinical reasoning progression (med-ed: novice schema → illness scripts → expert pattern recognition)
- ✅ Designing formative assessment indicators and diagnostic tools that locate learners on a progression
- ❌ Scope-and-sequence across many topics (use scope-sequence prompts)
- ❌ Credentialing milestones (use `teaching_milestone_alignment_designer.md`)
- ❌ Multiple concepts at once — one progression per concept; if the user names several, do the first and offer the rest as follow-ups

## Inputs Required
- **Concept / skill / competency** the progression targets (must be narrow enough for a single progression — "fractions as quantities," not "mathematics")
- **Domain context** (subject, grade band, professional setting)
- **Learner population**
- **Time horizon** (months, multi-year, career-spanning)
- **Research base or framework reference**, if the user has one (e.g., a specific progressions document, reading-development model, expertise literature)
- **Number of waypoints** (default 5 if unspecified; acceptable range 4-6)

**If inputs are missing:** Ask at most 2 clarifying questions, and only for the concept and learner population — everything else can be defaulted with assumptions stated explicitly in Section 1. Never stall on missing time horizon or waypoint count.

## Constraints

**Must:**
- Anchor each waypoint with observable indicators — verbatim-style examples of what learners *say, do, or produce*, not internal states ("understands," "grasps," "appreciates" are banned as indicators)
- Frame misconceptions as **learner reasoning**, not deficits: state the belief the learner holds and why it is locally sensible ("treats the denominator as a count of pieces, so believes 1/8 > 1/5 because 8 > 5"), never "doesn't know X"
- Make each diagnostic probe **discriminating**: specify the probe task *and* how responses differ between this waypoint and its neighbors — a probe that everyone above level 2 answers the same way cannot locate anyone
- Give each waypoint a **boundary statement**: the specific change in performance that marks the transition to the next level
- Identify the 2-3 **dominant dimensions of growth** for this progression (scope, abstraction, automaticity, integration, autonomy, precision) rather than force-filling all six
- Follow the research-grounding rules below
- Include the assessment caveat: a learner's level is an inference from multiple probes over time; performance regresses under load, in unfamiliar contexts, and in high-stakes conditions, so a single response never fixes a level

**Must Not:**
- Conflate progression with grade level or age (progressions describe development, not curriculum pacing)
- Relabel Bloom's verbs or generic tiers ("basic / intermediate / advanced," "remembers → applies → evaluates") as waypoints — waypoints describe qualitatively different ways of thinking about *this* concept
- Treat the progression as strictly linear — note branches, regressions, and plateaus
- Fabricate citations (see research-grounding rules)
- Write indicators that describe teaching ("has been introduced to X") rather than learner performance

**Research-grounding rules (three tiers — label which applies):**
1. **User-supplied framework:** If the user names a research base, align to it and attribute waypoints to it explicitly.
2. **Established literature:** If drawing on well-known research programs (e.g., CGI for arithmetic, learning-trajectory work in early math, stage models of reading development, novice-expert studies in clinical reasoning), name the research program and its central finding in general terms. Do not invent specific author-year-journal citations from memory; instead state: "Verify exact citations before publication — I can hallucinate references."
3. **Working draft:** If extrapolating beyond available literature, label the progression **"Empirically untested working draft — validate with learner data before high-stakes use"** in both Section 1 and Section 5.

## Instructions

1. **Confirm scope.** Echo concept, domain, learner population, time horizon, framework reference, and waypoint count. State any assumptions filled in for missing inputs. If the concept is too broad for one progression, narrow it and say so.

2. **Establish waypoint structure.** Name each waypoint with a **content-bearing label** that captures the way of thinking at that level (e.g., "Fractions as counts of pieces," "Fractions as part-whole relations," "Fractions as quantities on a number line") — not a generic tier name. Generic labels (Emergent/Developing/etc.) may appear only as a secondary tag after the content label.

3. **Draft each waypoint** using the Section 2 table. Write indicators first, then derive the probe: ask "what task would make a level-3 learner and a level-4 learner give visibly different responses?" If no such task exists, the two waypoints are not distinct — merge or redefine them.

4. **Specify progression direction.** Identify the 2-3 dominant dimensions of growth and describe concretely what changes along each. Mention non-dominant dimensions in one line only if they matter.

5. **Map branches and regressions.** Where do learners branch into different valid pathways? Regress under cognitive load, stress, or novel contexts? Plateau — and what typically causes the plateau?

6. **Ground in research** per the three-tier rules.

7. **Self-audit before delivering.** Check every item in the Verification Checklist. If any item fails, **revise the progression before output** — do not deliver with a noted failure. Report the completed checklist at the end.

## Output Format

Default to the full format below. If the user asks for a quick or compact version, deliver Sections 1-2 only, with the overview table and abbreviated waypoint entries (indicators, one misconception, one probe each).

### Section 1: Progression Identity
Target concept, domain, learner population, time horizon, research-grounding tier, waypoint count, and any assumptions made for missing inputs.

### Section 2: Waypoint Sequence

**First, an overview table** (one row per waypoint):

| # | Waypoint (content-bearing label) | Core way of thinking | Boundary to next level |
|---|---|---|---|

**Then, for each waypoint:**

**Waypoint [N]: [Content-bearing label]**

| Element | Description |
|---|---|
| Indicators (what learners say / do / produce) | |
| What's coordinated at this level | |
| What's still difficult | |
| Common misconceptions (stated as learner beliefs, with why they're locally sensible) | |
| Diagnostic probe + how responses differ from adjacent levels | |
| Instructional moves to advance | |
| Boundary statement (what marks the transition to N+1) | |

*Calibration example of the expected grain size (fractions, mid-progression):*
> **Waypoint 2: Fractions as counts of pieces.** Indicators: partitions shapes into equal parts and names "3 out of 4"; writes 3/4 for shaded regions; when comparing 1/5 and 1/8, says "1/8 is bigger because 8 is more." Misconception: numerator and denominator are two independent whole numbers, which is locally sensible because all prior number work rewarded counting. Probe: "Which is larger, 1/5 or 1/8? Show me with a drawing." A Waypoint-2 learner picks 1/8 or answers correctly only after drawing; a Waypoint-3 learner answers from the meaning of the denominator without needing the drawing. Boundary: learner begins reasoning about the *size* of parts, not the *count* of parts.

### Section 3: Progression Direction

| Dominant dimension | What changes across the sequence (concrete) |
|---|---|

Plus one line on non-dominant dimensions if relevant.

### Section 4: Branches, Regressions, Plateaus
- Branch points (alternative valid pathways)
- Common regressions and their triggers (load, stress, novel context)
- Plateau patterns and typical causes

### Section 5: Research Base
Grounding tier, named research programs or user framework, and the verification caveat or working-draft flag.

### Section 6: Using This Progression
- Diagnostic assessment design (including the multi-probe caveat)
- Instructional sequencing
- Formative feedback language (what to say to a learner at each level)
- Curriculum-mapping tag

### Section 7: Completed Verification Checklist

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Equating progression with grade level | Learners progress at different rates; grade labels smuggle in pacing assumptions | Describe development; decouple from age/grade |
| Generic or Bloom's-verb waypoints | "Intermediate" or "applies concepts" describes no observable, concept-specific thinking | Content-bearing labels + specific indicators |
| Misconceptions as deficits ("doesn't know X") | Absence of knowledge isn't a misconception and suggests no instructional move | State the belief held and why it's locally sensible |
| Non-discriminating probes | A probe every learner passes (or fails) locates no one | Each probe must produce visibly different responses at adjacent levels |
| Indicators describing teaching or internal states | "Has covered X" / "understands X" cannot be observed | Only what learners say, do, or produce |
| Strictly linear progression | Real progressions branch, regress, and plateau | Section 4 is mandatory |
| Invented citations | Hallucinated references destroy credibility and mislead adopters | Three-tier grounding rules; verify-before-publication caveat |
| Level assignment from one response | Performance is context- and load-dependent | Multi-probe, over-time inference caveat in Section 6 |

## Verification Checklist

- [ ] 4-6 waypoints, each with a content-bearing label and observable indicators (no banned verbs)
- [ ] Misconceptions at each waypoint stated as learner beliefs with their local logic
- [ ] Every probe discriminates between adjacent levels (differing responses specified)
- [ ] Boundary statement at each waypoint
- [ ] Instructional moves to advance at each waypoint
- [ ] Dominant dimensions of growth identified with concrete changes
- [ ] Branches, regressions, and plateaus noted
- [ ] Research-grounding tier labeled; no fabricated citations; caveat included
- [ ] Any failed item was revised before delivery
