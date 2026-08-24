---
title: "Standards Crosswalk Generator (Two-Framework Alignment)"
category: education-teaching/curriculum-design
description: "Generate a crosswalk between two standards frameworks — e.g., state standards ↔ CCSS, CCSS ↔ AP, NGSS ↔ state science, O*NET ↔ industry credential, ACGME ↔ AAMC EPAs — showing matches, partial fits, gaps, and conflicts."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - DS-01
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - education
  - curriculum-design
  - standards-crosswalk
  - alignment
  - common-core
  - state-standards
  - ngss
  - ap
  - ib
  - acgme
  - aamc-epa
  - onet
  - k12
  - higher-ed
  - workforce
  - medical-education
updated: "2026-05-15"
related_prompts:
  - teaching_standards_alignment_audit.md
  - teaching_competency_mapping_workforce.md
  - teaching_curriculum_map_builder.md
---

# Standards Crosswalk Generator

**Objective:** Generate a crosswalk between two standards or competency frameworks — for each element of Framework A, identify the matching element(s) in Framework B; assess fit (Full / Partial / None); flag conflicts (same content, different cognitive level or depth); and produce a directional summary of what each framework requires that the other does not.

## When to Use
- ✅ State standards ↔ CCSS or NGSS alignment
- ✅ CCSS ↔ AP / IB framework alignment
- ✅ Old standards ↔ new standards (post-revision crosswalks)
- ✅ Industry credential ↔ O*NET KSAs
- ✅ ACGME Core Competencies ↔ CanMEDS ↔ AAMC EPAs
- ✅ Program-specific competencies ↔ accreditor competencies
- ❌ Auditing curriculum against one framework (use `teaching_standards_alignment_audit.md`)
- ❌ Building a curriculum map (use `teaching_curriculum_map_builder.md`)

## Inputs Required
- **Framework A:** name, version, source, and the subset to crosswalk (specify codes)
- **Framework B:** name, version, source, and the subset to crosswalk
- **Direction:** A → B (default) or bidirectional
- **Granularity:** strand-to-strand / standard-to-standard / sub-standard-to-sub-standard
- **Purpose:** state-adoption alignment / curriculum-portability / accreditation evidence / credential-pathway design
- **Standards text:** verbatim text of both frameworks' elements (request if not provided; do not invent)

## Constraints

**Must:**
- Use both frameworks' native codes verbatim
- For every element of Framework A, identify Framework B element(s) using the fit codes: **Full match / Partial match / None / Conflict**
- For Partial matches, specify *what is shared* and *what differs* (content scope, cognitive level, depth, context, audience)
- For Conflicts, flag explicitly — same content area but different cognitive demand, depth, or interpretation
- If bidirectional, repeat the analysis B → A
- Produce a summary of A-only and B-only elements
- Flag any element where verbatim text was not supplied (do not invent text)

**Must Not:**
- Invent codes or text from either framework
- Force matches across structurally different frameworks (a competency in Framework A may have no analog in Framework B — that's a valid result)
- Conflate identical-sounding labels that mean different things across frameworks
- Treat keyword overlap as Full match (e.g., "communication" in two frameworks may mean very different things)
- Suppress conflicts — the value of a crosswalk is surfacing them

## Instructions

1. **Confirm both frameworks.**
   - Echo back: Framework A name + version + source + subset; same for B.
   - If either is missing text, request it or proceed with a "user-supplied codes only" caveat.

2. **Establish a common structural view.**
   - Note structural parallels and differences: does Framework A use grade-band organization while B uses course-band? Does A use "standards/sub-standards" while B uses "competencies/milestones"?
   - Decide what unit is being crosswalked (standard-to-standard, sub-element to sub-element, etc.).

3. **For each Framework A element, search Framework B for candidate matches.**
   - Match on: content scope, cognitive demand, performance context, and intended performance level.
   - Score the fit:
     - **Full match:** Same content, same cognitive level, same context, same depth
     - **Partial match:** Shared content area; differences in scope, cognitive level, context, or depth
     - **None:** No element in B addresses this content
     - **Conflict:** B addresses the same content but requires a different cognitive level, depth, or interpretation that cannot be reconciled

4. **For each Partial or Conflict, write a difference statement.**
   - "Framework A requires [X] at [cognitive level Y] in [context Z]; Framework B requires [X'] at [cognitive level Y'] in [context Z']. Difference: [specific gap]."

5. **Compute the directional summary.**
   - **A-only elements:** elements in A with No fit in B
   - **B-only elements:** elements in B with No fit in A (requires reverse search)
   - **Conflict register:** all conflicts with specific descriptions

6. **Diagnose patterns.**
   - Where do A-only elements cluster? (B doesn't reach into this domain)
   - Where do B-only elements cluster? (A doesn't reach into this domain)
   - Are conflicts concentrated in specific strands? (Frameworks disagree philosophically here)

7. **Produce implementation guidance.**
   - If A is the implementation framework and B is the reference (e.g., implementing CCSS in a state with state standards), guide what to add or modify.
   - If both are reference frameworks (e.g., crosswalking ACGME and CanMEDS for a med-ed program), guide how to satisfy both.

## Output Format

### Section 1: Crosswalk Identity
- Framework A (name, version, source, subset), Framework B (same), direction, granularity, purpose

### Section 2: Element-by-Element Crosswalk (A → B)

| A Code | A Text (verbatim) | B Match(es) | B Text (verbatim) | Fit | Difference Notes |
|---|---|---|---|---|---|
| [A code] | [A text] | [B code(s)] | [B text] | Full / Partial / None / Conflict | [if Partial/Conflict, what differs] |

### Section 3: Element-by-Element Crosswalk (B → A) [if bidirectional]

[same structure]

### Section 4: Directional Summary

**A-only (not addressed by B):**

| A Code | Content Area | Implication |
|---|---|---|

**B-only (not addressed by A):**

| B Code | Content Area | Implication |
|---|---|---|

**Conflicts:**

| A Code | B Code | Content Area | Nature of Conflict | Resolution Suggestion |
|---|---|---|---|---|

### Section 5: Pattern Diagnostics
- Where A reaches but B doesn't (and why this might be)
- Where B reaches but A doesn't
- Where the two frameworks disagree philosophically (conflicts clustered in a domain)

### Section 6: Implementation Guidance
- If implementing A while referencing B: what to add, modify, or supplement
- If satisfying both: where double-coverage is needed
- Verification notes for unverified codes or text

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Matching on label keyword | "Communication" in K-12 SEL ≠ "Communication" in ACGME milestones | Match on content scope, cognitive demand, and context — not labels |
| Treating "Partial" as the default | Inflates apparent alignment; obscures gaps | Reserve Partial for genuine partial overlap; use None when there is no overlap |
| Hiding conflicts | The crosswalk's value is surfacing them | Always include conflicts; resolution is a downstream decision |
| Inventing framework text | Standards bodies have specific language; fabricated text undermines the crosswalk | Request verbatim text; flag unverified codes |
| Forcing 1:1 mapping | Frameworks have different granularity; 1:many and many:1 are normal | Allow each A element to map to multiple B elements (and vice versa) |
| Skipping reverse search | A → B only misses B-only content | Bidirectional search surfaces both directions of gap |
| Confusing similar codes across versions | CCSS 2010 ≠ CCSS 2025 if a revision occurred | Always cite version and date |
| Producing the matrix without difference statements | "Partial match" alone is unactionable | Specify what is shared and what differs for every Partial and Conflict |

## Verification Checklist

- [ ] Both frameworks cited with name, version, source
- [ ] Every Framework A element in scope appears in the A→B crosswalk
- [ ] Every linkage coded Full / Partial / None / Conflict
- [ ] Partial and Conflict entries have specific difference statements
- [ ] If bidirectional, B → A crosswalk also complete
- [ ] A-only and B-only elements listed with implications
- [ ] All conflicts surfaced (not suppressed)
- [ ] No invented codes or text; unverified items flagged
- [ ] Pattern diagnostics identify structural divergences
- [ ] Implementation guidance is specific to the user's purpose
