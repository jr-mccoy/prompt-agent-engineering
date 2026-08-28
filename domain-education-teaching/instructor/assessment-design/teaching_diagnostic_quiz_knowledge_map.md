---
title: "Diagnostic Quiz + Knowledge Map"
category: education-teaching/instructor/assessment-design
description: "Build a pre-unit diagnostic quiz that outputs not just items but a knowledge map of prerequisite concepts — and an instructional routing guide that translates score patterns into specific starting points."
techniques:
  - ST-01
  - DS-01
  - QA-02
  - RT-02
  - CM-01
difficulty: advanced
tags:
  - assessment
  - diagnostic
  - pre-assessment
  - knowledge-map
  - formative-assessment
  - instructional-routing
  - prerequisite
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/instructor/response-cycle/teaching_preassessment_designer.md
  - domain-education-teaching/instructor/assessment-analysis/teaching_item_analysis_report.md
  - domain-education-teaching/instructor/assessment-analysis/teaching_quiz_to_reteach_plan.md
  - domain-education-teaching/instructor/response-cycle/teaching_misconception_diagnoser.md
---

# Diagnostic Quiz + Knowledge Map

## Objective

Produce a pre-unit diagnostic quiz whose purpose is not a score but a map — a structured representation of which prerequisite concepts students hold, which are shaky, and which are absent, with an instructional routing guide that tells the teacher where to begin.

## When to Use

- At the start of a new unit or course
- Before introducing a concept that builds on prerequisites
- When student starting points are likely to vary significantly
- When you want to group students by readiness rather than treat the class as uniform
- When you're a new teacher to a class and don't know what they actually retained

## When NOT to Use

- For grading purposes — this is diagnostic, not summative
- When the unit has no meaningful prerequisites (introduces entirely new content)
- For mid-unit checks — use `assessment_hinge_question_designer.md` or exit tickets instead

---

## Inputs Needed

- **Unit topic:** [The concept or skill the upcoming unit will teach]
- **Learning objectives for the unit:** [List of SWBAT statements]
- **Grade / course level:** [e.g., Grade 9 Algebra, AP Chemistry]
- **Prior units / courses that feed this one:** [What students should have encountered]
- **Time available for the diagnostic:** [e.g., 15, 20, or 30 minutes]
- **Response format preference:** [MC only / MC + short answer / short answer only]
- **Class profile notes:** [Optional — known gaps from prior teacher, demographics, IEP prevalence]

---

## Instructions

### Step 1: Map the Prerequisites

Identify 6–10 discrete prerequisite knowledge/skill nodes that students need to enter the unit successfully. For each node, write:

```
KNOWLEDGE MAP — NODE LIST
─────────────────────────────────────────────
Node 1: [Concept or skill name]
  Definition: [1 sentence]
  Why it matters: [How it connects to the upcoming unit]
  Evidence of mastery: [What a student who has this looks like]
  Common gap: [Typical way this is missing or broken]

Node 2: [...]
...
```

Draw the relationship structure (as text):

```
PREREQUISITE DEPENDENCY CHAIN
─────────────────────────────────────────────
[Node 1] → [Node 3] → [Unit Entry Point]
[Node 2] → [Node 3]
[Node 4] (parallel prerequisite) → [Unit Entry Point]
─────────────────────────────────────────────
```

Identify which nodes are **gateway prerequisites** (unit cannot proceed without them) vs. **supportive prerequisites** (helpful but not blocking).

### Step 2: Write Diagnostic Items — One Per Node

For each node, write one item that probes exactly that concept. Mix formats based on input preference:

```
DIAGNOSTIC ITEM N  [Node: Name]
─────────────────────────────────────────────
Format:     [MC / Short answer]
Node:       [Name]
Gateway?:   [Yes / No]
Time:       [Estimated seconds to answer]

ITEM:
[Full item text as student would see it]

[If MC: options A, B, C, D with key and distractor labels]
[If short answer: model answer + partial credit threshold]

SCORING GUIDE:
Full credit: [What earns full marks]
Partial credit: [If applicable]
Gap indicator: [What a wrong answer or blank reveals about this specific node]
```

### Step 3: Node-Level Interpretation Guide

For each node, define what different results mean:

```
NODE INTERPRETATION GUIDE
─────────────────────────────────────────────

NODE: [Name]
Full credit → Strong: [What the teacher can assume this student has]
Partial / Incorrect → Gap: [Specific description of what is missing]
Blank / No attempt → Absent: [This concept appears not to have been encountered or was not retained]
```

### Step 4: Instructional Routing Guide

After scoring by node, route students based on their profile:

```
INSTRUCTIONAL ROUTING GUIDE
─────────────────────────────────────────────

PROFILE A: Strong on all gateway nodes (≥ threshold%)
→ START: [Recommended entry point — what lesson or concept to begin with]
→ SKIP: [Prerequisites that don't need revisiting]
→ STRETCH: [Optional enrichment or acceleration suggestion]

PROFILE B: Gap in [specific gateway node(s)]
→ START: [Required reteach or activation activity for those nodes]
→ TIME ESTIMATE: [How long before they're ready for the unit entry point]
→ MATERIALS: [Suggest a specific activity or resource type]

PROFILE C: Gaps in [multiple nodes / foundational gaps]
→ START: [Foundational concept — further back than the unit normally goes]
→ FLAG: [Whether this student may need additional support beyond classroom intervention]

PROFILE D: All nodes absent / no prior exposure
→ START: [Beginning of prerequisite sequence]
→ NOTE: [This student may need a modified path through the unit — flag for planning]
```

### Step 5: Whole-Class Summary View

Produce a class-level summary template the teacher can fill in from scored diagnostics:

```
CLASS SUMMARY TEMPLATE
─────────────────────────────────────────────
Node                  | # Strong | # Gap | # Absent | Gateway? | Action needed?
─────────────────────────────────────────────
[Node 1]              |          |       |          |   Y/N    |
[Node 2]              |          |       |          |   Y/N    |
...
─────────────────────────────────────────────
Most common gap: [Fill in after scoring]
Starting point for majority: [Fill in]
Students needing modified path: [Fill in]
```

---

## Output Format

1. Knowledge map — node list (6–10 nodes with definitions, connections, gaps)
2. Prerequisite dependency chain (text diagram)
3. Diagnostic items (one per node, with scoring guide)
4. Node-level interpretation guide
5. Instructional routing guide (Profiles A–D)
6. Class summary template

---

## False-Positive Prevention

❌ **DON'T:**
- Design items that test the upcoming unit content — this diagnostic tests prerequisites, not the new material
- Create a single total score as the output — the diagnostic is useful only at the node level
- Write items with vocabulary from the upcoming unit that students haven't encountered yet
- Assume "got it right" = fully understands — one item per node is an indicator, not proof
- Use this as a grade — penalizing students for not knowing prerequisites discourages honesty

✅ **DO:**
- Test prerequisites, not unit content
- Report results by node, not by total score
- Include a routing guide so teachers have a concrete response, not just data
- Design items that a student with genuine mastery of the prerequisite would answer correctly — not tricky items
- Build the routing guide to address the most common real-world gap combinations

---

## Quality Indicators

- [ ] 6–10 nodes identified with clear definitions and dependency relationships
- [ ] One item per node, explicitly labeled
- [ ] Gateway prerequisites are clearly distinguished from supportive ones
- [ ] Scoring guide for each item specifies what wrong answers reveal
- [ ] Routing guide addresses ≥ 3 distinct student profiles
- [ ] Class summary template is formatted for actual teacher use (fillable)

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **ST-01** | Knowledge map nodes and routing guide anchor the design. |
| **DS-01** | Prerequisites structured as a dependency chain using explicit frameworks. |
| **QA-02** | Each item includes a gap indicator — what wrong answers reveal about the specific node. |
| **RT-02** | Multi-dimensional analysis across 6–10 prerequisite nodes, not a single score. |
| **CM-01** | Unit topic, grade, time, and class profile frame the entire diagnostic design. |
