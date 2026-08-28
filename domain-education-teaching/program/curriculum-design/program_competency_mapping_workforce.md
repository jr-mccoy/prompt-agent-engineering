---
title: "Workforce Competency Mapping (O*NET, Industry Credentials, Apprenticeship)"
category: education-teaching/curriculum-design
description: "Map a workforce-training curriculum to occupational competency sources — O*NET KSAs and work activities, industry credential body-of-knowledge, registered apprenticeship work-process schedule, and stackable credential frameworks — producing a competency × experience matrix and a labor-market alignment audit."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - DS-01
  - QA-01
difficulty: advanced
tags:
  - education
  - curriculum-design
  - workforce
  - onet
  - industry-credentials
  - apprenticeship
  - stackable-credentials
  - cte
  - labor-market-alignment
updated: "2026-07-18"
related_prompts:
  - teaching_scope_sequence_workforce.md
  - teaching_competency_framework_designer.md
  - teaching_milestone_alignment_designer.md
  - teaching_standards_crosswalk_generator.md
---

# Workforce Competency Mapping

**Objective:** Map a workforce-training curriculum to authoritative occupational competency sources — O*NET (Knowledge, Skills, Abilities, Tasks, Work Activities, Tools & Technology), industry credential bodies of knowledge, registered apprenticeship work-process schedules, and stackable-credential ladders — producing a competency × experience matrix, a labor-market alignment audit, and a stackable-credential opportunity map.

## When to Use
- ✅ Aligning a CTE program of study to O*NET for the target occupation
- ✅ Mapping registered apprenticeship work-process schedule to industry credentials
- ✅ Designing stackable-credential ladder for a sector (advanced manufacturing, healthcare support, IT, construction)
- ✅ Auditing existing workforce program for labor-market alignment
- ✅ Building employer-partnered training with shared competency vocabulary
- ❌ Designing the overall scope-and-sequence (use `teaching_scope_sequence_workforce.md`)
- ❌ K-12 standards alignment (use K-12 prompts)
- ❌ Designing the competency framework from scratch (use the framework designer)

## Inputs Required
- **Target occupation(s):** O*NET-SOC code(s) and title(s) (e.g., 51-4041.00 Machinists)
- **O*NET data extract:** pasted or attached KSA/Task/Work Activity/Tools & Technology data from onetonline.org, with version and extraction date. *If not provided, the model must request it or clearly label its own recollection as unverified — see Data Provenance below.*
- **Industry credential(s) the program leads to:** name + awarding body + published body-of-knowledge / exam blueprint (pasted or attached)
- **Apprenticeship status:** if registered, provide the DOL-approved work-process schedule (with hour allocations)
- **Curriculum artifacts:** related-instruction (RI) modules, on-the-job learning (OJL) rotations, courses — each with topics and learning outcomes
- **Stackable credential candidates:** OSHA 10/30, MSSC CPT, NIMS, NCCER Core, CompTIA, NCRC, sector-specific credentials
- **Employer partner inputs:** any employer-specified competency requirements (attribute to the partner)
- **Regional labor market data** (optional): source, date, and high-demand competency clusters

### If Inputs Are Incomplete
Do not silently degrade. Instead:
1. State which sources are missing.
2. Ask the user to paste them, **or**
3. Proceed with available sources only, and mark every affected section "PARTIAL — [source] not provided."
Never substitute invented source data to fill a missing input.

## Data Provenance (read before anything else)

O*NET descriptors, credential blueprints, and work-process schedules are versioned, factual artifacts. A language model can misremember them.

- **Preferred:** work only from user-supplied extracts. Quote descriptor text verbatim from what was provided.
- **If the user asks you to recall O*NET/credential content from memory:** you may draft it, but every recalled item must be flagged `[UNVERIFIED — confirm against O*NET vX.X]` and listed in Section 9. Do not present recalled descriptors as authoritative.
- **Never** invent O*NET-SOC codes, element IDs, importance ratings, credential domain weights, or WPS hour counts.

## Definitions and Conventions

**Depth codes (used in the matrix):**
- **I — Introduced:** competency is named, demonstrated, or explained; learner observes or performs with full support.
- **D — Developed:** learner practices with feedback; partial independence; formative assessment only.
- **M — Mastered:** learner performs independently to the standard implied by the source (credential exam objective, WPS proficiency, or O*NET-level performance) and is summatively assessed.
- **Blank:** no meaningful touch. Do not use I for passing mentions.

**Competency ID scheme (tag every item with its source):**
- `O-K-##` O*NET Knowledge · `O-S-##` Skills · `O-A-##` Abilities · `O-T-##` Tasks · `O-WA-##` Work Activities · `O-TT-##` Tools & Technology
- `CR-<domain>.<sub>` industry-credential body-of-knowledge
- `WPS-Y<year>-##` apprenticeship work-process item
- `EMP-##` employer-specified

**Importance handling:** O*NET reports importance on a 1–5 scale for KSAs and Work Activities. Treat ≥ 4.0 as **High**, 3.0–3.9 as **Medium**, < 3.0 as **Low** (state this convention in the output). Tasks are listed as Core/Supplemental — treat Core as High. Tools & Technology carries no importance rating; do not fabricate one.

**Scoping rule (keep the matrix usable):** For occupations with large O*NET profiles, include all High items, include Medium items, and summarize Low items in one collapsed row per category ("Low-importance Knowledge: n items, m covered") unless the user requests the full list. Never trim High items.

**Deduplication across sources:** When an O*NET KSA, a credential objective, and a WPS item describe the same competency, keep them as separate rows (they are audited against different sources) but add a `Crosswalk` note linking the IDs. Do not merge rows — coverage percentages must remain computable per source.

## Constraints

**Must:**
- Use O*NET's actual taxonomy (Knowledge / Skills / Abilities / Tasks / Work Activities / Tools & Technology) as provided in the extract
- Use the industry credential body-of-knowledge exactly as published by the awarding body, including domain weights if published
- For registered apprenticeships: use the DOL-approved work-process schedule, preserving hour allocations
- Build a competency × experience matrix using the I/D/M definitions above
- Verify a mastery path for every High-importance and employer-specified item: at least one I or D touch **before** the M touch, in curriculum order
- Identify labor-market alignment: high-demand competencies that are or are not covered
- Identify stackable-credential opportunities: clusters of competencies that align to a separately awardable credential
- Cite version and extraction date for every source

**Must Not:**
- Invent O*NET codes, KSA descriptors, importance ratings, or work-process items
- Confuse O*NET KSAs with industry-credential objectives (different sources, different conventions — keep both, crosswalk them)
- Claim regional labor-market alignment without a cited data source and date
- Force every curriculum element to map (general-education and some soft-skills content legitimately doesn't map to O*NET)
- Mark M where no summative assessment exists in the curriculum artifact
- Suppress gaps (uncovered high-demand or employer-specified competencies)

## Instructions

1. **Confirm sources.** Echo back: target occupation O*NET-SOC code(s) and title(s), O*NET version/extraction date, credential body-of-knowledge (name, awarding body, version), apprenticeship WPS (registration number if given), employer partners, labor-market data source. List anything missing per *If Inputs Are Incomplete*.

2. **Build the competency inventory** from the supplied sources.
   - O*NET: extract KSAs, Tasks, Work Activities, Tools & Technology; record importance ratings where reported and apply the High/Medium/Low convention; apply the scoping rule.
   - Industry credential: list domains and sub-domains from the published body-of-knowledge; record exam weights if published.
   - Apprenticeship: extract work-process items **with hour allocations** from the registered schedule.
   - Employer-partner additions: list additional competencies, attributed to the naming partner.
   - Add crosswalk notes where items from different sources describe the same competency.

3. **Build the curriculum inventory.** List each RI module, OJL rotation, and course with its topics, learning outcomes, and assessment type (formative/summative) — assessment type is needed to justify M ratings.

4. **Build the competency × curriculum matrix.**
   - Rows: competencies (ID + short label). Columns: curriculum components in delivery order.
   - Cells: I / D / M / blank per the definitions above.
   - Annotate High-importance rows (e.g., ★).
   - For OJL columns mapping WPS items, note allocated hours.

5. **Compute coverage diagnostics.**
   - Coverage by source: % of items with ≥1 touch, and % with an M touch, computed separately for each source.
   - High-importance check: are High items preferentially covered and mastered relative to Medium/Low?
   - Mastery-path check: every M is preceded by I or D in curriculum order; flag "cold masteries."
   - Employer-specified items: 100% coverage expected; flag any shortfall.
   - WPS hours check: curriculum OJL hours vs. WPS-required hours per work-process area.

6. **Identify gaps.** For each: competency, source, importance, gap type (no touch / introduced-never-mastered / cold mastery / hours shortfall), and a concrete recommendation.

7. **Identify stackable-credential opportunities.** Cluster competencies matching a published credential's blueprint; name the curriculum window that completes the cluster; recommend the natural award point; note any delta the curriculum would need to add. Mark blueprint matches from memory as `[UNVERIFIED]`.

8. **Labor-market alignment audit** (only if regional data was supplied). Cite the data source and date. Check coverage of high-demand and emerging (12–24 month) competencies. If no data supplied, state "Not performed — no regional data provided" rather than improvising.

9. **Produce recommendations.** Prioritized: (a) High-importance and employer-specified gaps first, (b) mastery-path repairs, (c) stackable credentials to embed, (d) labor-market additions. Each recommendation names the gap it addresses and a concrete implementation step (which module/rotation, what change).

10. **Write verification notes** (Section 9 of output): every `[UNVERIFIED]` item, every assumption, source versions and dates.

## Output Format

Begin with a **5-line executive summary**: occupation, sources used, headline coverage % per source, count of High-importance gaps, top recommendation.

### Section 1: Mapping Identity
Occupation (O*NET-SOC code + title), O*NET version + extraction date, credential + body-of-knowledge version, apprenticeship status + WPS reference, employer partners, labor-market data source (or "none").

### Section 2: Competency Inventory

| ID | Source | Competency Statement (verbatim) | Importance | Crosswalk |
|---|---|---|---|---|
| O-K-01 | O*NET Knowledge | Knowledge of machines and tools, including their designs, uses, repair, and maintenance. | High (4.2) | CR-1.3, WPS-Y1-04 |
| CR-1.3 | NIMS Level I BOK | [verbatim objective text] | Weight 12% | O-K-01 |
| WPS-Y1-04 | Apprenticeship WPS | [verbatim item] — 250 hrs | — | O-K-01 |
| EMP-3 | Employer: [name] | [text as specified] | — | — |

### Section 3: Competency × Curriculum Matrix

|  | RI-1 | RI-2 | OJL-A | OJL-B | … |
|---|---|---|---|---|---|
| ★ O-K-01 | I | D | D | M | |

Legend: I = Introduced, D = Developed, M = Mastered (summatively assessed), ★ = High importance.

### Section 4: Coverage Diagnostics

| Source | Total | ≥1 Touch | % | With M | % | Notes |
|---|---|---|---|---|---|---|
| O*NET KSAs (High) | | | | | | |
| O*NET KSAs (Med/Low) | | | | | | |
| O*NET Tasks/WAs | | | | | | |
| O*NET Tools & Tech | | | | | | |
| Industry credential | | | | | | |
| Apprenticeship WPS | | | | | | incl. hours vs. required |
| Employer-specified | | | | | | must be 100% |

### Section 5: Gaps

| Competency | Source | Importance | Gap Type | Recommendation |
|---|---|---|---|---|

### Section 6: Stackable Credential Opportunities

| Candidate Credential | Awarding Body | Competencies Covered | Curriculum Window | Award Point | Delta Needed |
|---|---|---|---|---|---|

### Section 7: Labor-Market Alignment
(If data available; otherwise state not performed.)

| Regional High-Demand Competency | Data Source (date) | In Curriculum? | Recommendation |
|---|---|---|---|

### Section 8: Recommendations (prioritized)

| # | Priority | Recommendation | Gap Addressed | Implementation |
|---|---|---|---|---|

### Section 9: Verification Notes
- O*NET version; extraction date; provided vs. recalled
- Credential body-of-knowledge version; provided vs. recalled
- WPS reference and hour totals
- Employer-partner attribution
- All `[UNVERIFIED]` items, listed individually
- Assumptions made where inputs were incomplete

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Inventing O*NET KSAs, IDs, or importance ratings | Damages credibility and downstream alignment | Work from supplied extract; flag any recalled item `[UNVERIFIED]` |
| Merging O*NET KSAs with credential objectives | Different sources, different conventions; breaks per-source coverage math | Separate rows + crosswalk notes |
| Marking M without a summative assessment | Overstates program outcomes | M requires independent performance + summative assessment in the artifact |
| "Cold mastery" (M with no prior I/D) | Implausible learning path; hides sequencing gaps | Mastery-path check in diagnostics |
| Mapping every general-ed element to the occupation | Some content is legitimately general (math, communication) | Leave unmapped; note as general education |
| Suppressing uncovered High-importance KSAs | Damages labor-market alignment | Surface honestly; recommend additions |
| Deprioritizing employer-specified items | Partnership credibility depends on responsiveness | 100% coverage target; flag shortfalls |
| Fabricating labor-market alignment | No source = no audit | Require cited source + date, or state audit not performed |
| Ignoring WPS hour allocations | Registered apprenticeships are hour-audited | Compare curriculum OJL hours to WPS-required hours |
| Drowning the matrix in Low-importance items | Unusable deliverable; High items get lost | Apply the scoping rule; never trim High items |
| No version/date stamp on sources | Data ages; misalignment hidden | Cite version and extraction date for every source |

## Verification Checklist

- [ ] All sources echoed with version/date; missing inputs handled per protocol
- [ ] Competency inventory built from supplied sources; recalled items flagged `[UNVERIFIED]`
- [ ] No invented codes, ratings, weights, or hour counts
- [ ] Crosswalk notes link duplicate competencies across sources; rows not merged
- [ ] Matrix uses defined I/D/M; every M backed by a summative assessment
- [ ] Mastery-path check run; cold masteries flagged
- [ ] Coverage diagnostics computed per source, High-importance broken out
- [ ] WPS hours compared to requirements (if apprenticeship)
- [ ] Gaps surfaced with gap type and recommendation
- [ ] Stackable-credential opportunities include award point and delta
- [ ] Labor-market audit performed only with cited data, or explicitly skipped
- [ ] Section 9 lists every unverified item and assumption
