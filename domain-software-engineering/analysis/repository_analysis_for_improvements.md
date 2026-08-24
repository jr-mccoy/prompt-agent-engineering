---
title: "Repository Analysis for Strategic Improvements"
category: software-engineering/analysis
description: "Conduct an adaptive-depth, evidence-based audit of any repository — scaling from sampling to exhaustive analysis based on repository size — to identify the single most impactful improvement opportunity and deliver a prioritized action plan with verifiable success criteria"
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - RT-05  # Evidence-Based Reasoning
  - RT-06  # Correlation and Cross-Analysis
  - DS-04  # Pattern Recognition Requests
  - DS-06  # Prioritization Guidance
  - CM-07  # Token-Budget-Aware Progressive Loading
  - DT-05  # Element-by-Element Assessment Matrix
  - QA-08  # Gate-Based Verification
  - DD-07  # Self-Audit Table
difficulty: advanced
tags:
  - repository-audit
  - quality-assessment
  - strategic-improvement
  - content-architecture
  - discoverability
  - technical-debt
  - adaptive-depth
  - exhaustive-analysis
updated: "2026-02-15"
related_prompts:
  - domain-software-engineering/analysis/architecture/architecture_layer_identification.md
  - domain-software-engineering/analysis/evolution/evolution_technical_debt_estimation.md
  - domain-software-engineering/analysis/quality/quality_code_complexity_analysis.md
---

# Repository Analysis for Strategic Improvements

**Objective:** Audit a repository's structure, content quality, and discoverability — adapting analysis depth from sampling to exhaustive based on repository size and available context — to identify exactly one primary bottleneck and deliver a max-5-item action plan where every finding is backed by file paths, metrics, and classified root causes.

---

## When to Use

- **Use when:** You need an evidence-based assessment of a repository's health before investing in improvements
- **Use when:** A content repository has grown organically and you suspect structural or quality issues
- **Use when:** You want to identify the single highest-leverage improvement across structure, quality, and discoverability
- **Don't use when:** You already know the specific problem and need a targeted fix (use the relevant domain-specific analysis prompt instead)

---

## Inputs / Context

**Required:**
- Repository access (file system or clone URL)
- General description of the repository's purpose and intended audience

**Optional:**
- Known pain points or suspected problem areas (to validate or refute)
- Priority weighting: structure vs quality vs discoverability (default: equal weight)
- Specific directories or content types to emphasize

**If any required input is missing:** Ask clarifying questions before proceeding.

---

## Constraints

**Must:**
- Provide specific file paths for every finding (no unsupported claims)
- Include quantitative metrics (counts, percentages, ratios) wherever measurable
- Classify every finding as DRIFT, VIOLATION, MISSING RULE, or ORPHAN
- Identify exactly one primary bottleneck (not two, not five — one)
- Limit the action plan to a maximum of 5 items
- Complete the self-audit verification table before delivering

**Must Not:**
- Report findings without evidence ("seems like" and "might have" are prohibited)
- Conflate aspirational improvements with actual breakage
- Skip phase checkpoints — each phase must produce its checkpoint before the next begins
- Flag patterns without understanding context (e.g., naming deviations that are intentional conventions)
- Recommend actions without measurable success criteria

---

## Adaptive Depth Strategy

Before beginning analysis, assess the repository size and determine the appropriate analysis depth. This prompt scales its thoroughness based on how much of the repository can be loaded into context.

**Determine your analysis tier:**

| Tier | Repository Size | Strategy | Rationale |
|------|----------------|----------|-----------|
| **Exhaustive** | < 200 files | Read every file. Score every file in Phase 2. Check every link in Phase 3. No sampling — full census. | The entire repository fits comfortably in context. Sampling would discard available information. |
| **Expanded** | 200–1,000 files | Read all files for structure (Phase 1). Sample 30–50 files for quality (Phase 2, stratified across all categories). Full link audit in Phase 3. | Most of the repository fits in context. Larger samples produce statistically meaningful quality assessments. |
| **Targeted** | 1,000+ files | Use the original sampling protocol (20 files for naming, 9 for quality). Prioritize reading high-traffic files (READMEs, indexes, guides) and files in suspected problem areas. | Repository exceeds single-pass context. Focus depth on highest-signal files. |

**How to assess:**
1. Count total files (e.g., `find . -type f -name "*.md" | wc -l` or equivalent)
2. Estimate average file size — if files are large (>500 lines average), shift down one tier
3. Record your tier selection in the Phase 0 checkpoint

**Phase 0 Checkpoint — record before proceeding:**
```
Total files: [N]
Average file size: [estimate]
Selected tier: [Exhaustive / Expanded / Targeted]
Rationale: [One sentence if deviating from the size-based default]
```

**Critical:** The tier determines sample sizes throughout all subsequent phases. Each phase specifies how its protocol varies by tier.

---

## Steps

### Phase 1: Structural Reconnaissance

**Goal:** Build a map of repository architecture and surface obvious structural issues.

1. **Map repository architecture**
   - Count top-level directories and measure maximum nesting depth
   - Identify the organizational pattern (by domain, by type, hybrid, or inconsistent)
   - Flag any directories that break the dominant organizational pattern

2. **Assess discoverability infrastructure**
   - Check: Does every directory have a README or index file? Report count: `[N]/[Total]`
   - Check: Is there a master index or entry point? Record its location
   - Check: Are cross-references bidirectional? Sample 5 links, trace both directions

3. **Assess naming conventions** (depth varies by tier)
   - **Exhaustive tier:** Check every file against the repository's dominant naming pattern. Report: `[N]/[Total] compliant ([%])`
   - **Expanded tier:** Check all files in the 5 largest categories plus a random selection of 20 files from remaining categories. Report: `[N]/[checked] compliant ([%])`
   - **Targeted tier:** Sample 20 files across at least 5 categories. Report: `[N]/20 compliant ([%])`
   - For all tiers: List outlier files with their full paths and note whether the deviation appears intentional (e.g., a documented convention for that content type)

**Phase 1 Checkpoint — record before proceeding:**
```
Directories: [N]
Max nesting depth: [N]
READMEs present: [N]/[Total] ([%])
Naming compliance: [N]/[checked] ([%]) — [Tier] depth
Files checked for naming: [N]
Obvious structural issue: [One sentence or "None identified"]
```

---

### Phase 2: Content Quality Assessment

**Goal:** Measure quality variance across categories. Depth scales with analysis tier.

**Assessment protocol (by tier):**

- **Exhaustive tier:** Read and score every content file. Group scores by category. This produces a complete quality census — no statistical uncertainty.
- **Expanded tier:** Score a stratified sample of 30–50 files. Select from every category proportional to category size (minimum 2 per category). Within each category, always include: (a) the oldest file, (b) the newest file, (c) remaining slots filled randomly. Total sample: 30–50 files.
- **Targeted tier:** Select 3 categories: (1) the largest by file count, (2) the smallest, (3) one chosen at random. From each category, read 3 files: (a) the oldest, (b) the newest, (c) one random. Total sample: 9 files.

**CRITICAL: Verify quality assessments against context.** A file that looks sparse may be intentionally minimal. A file with heavy structure may be over-engineered for its purpose. Evaluate fitness for purpose, not raw complexity.

**Score each assessed file on five dimensions (1–5 scale):**

| Dimension | 1 (Poor) | 3 (Adequate) | 5 (Excellent) |
|-----------|----------|--------------|---------------|
| **Objective Clarity** | Vague or missing purpose | Present but broad | Single, measurable goal stated |
| **Structure** | Unformatted wall of text | Some headings and organization | Clear sections, numbered steps, logical flow |
| **Technique Application** | No visible methodology | 1–2 implicit techniques | 3+ techniques, explicitly named or clearly applied |
| **Output Specification** | No definition of expected results | General description of output | Template with format, sections, and example |
| **Actionability** | Cannot be executed as written | Requires significant interpretation | Copy-paste ready with clear instructions |

**Confidence level for each score:** Assign High/Medium/Low based on whether the score reflects clear evidence or subjective judgment. For Exhaustive and Expanded tiers, statistical confidence in category-level conclusions is inherently higher.

**Phase 2 Checkpoint — record before proceeding:**
```
Analysis tier: [Exhaustive / Expanded / Targeted]
Files assessed: [N] (of [Total])
Quality range: [lowest]-[highest] (mean: [X.X])
Highest-quality category: [name] (avg: [X.X])
Lowest-quality category: [name] (avg: [X.X])
Quality variance: [High/Medium/Low]
Cross-category consistency: [Consistent/Moderate/Fragmented]
Categories with 100% coverage: [N] (Exhaustive/Expanded only)
```

---

### Phase 3: Gap Analysis

**Goal:** Identify gaps that hurt usability — not theoretical completeness gaps.

**3.1 Critical Path Analysis**

Map the user journey for the 3 most common use cases:
1. "Help me with [task relevant to repo]"
2. "Create a new [content type] for [purpose]"
3. "Find an existing [content type] for [purpose]"

For each path, document:
- Entry point (where does the user start?)
- Steps to reach the target resource (count the hops)
- Friction points (where does the user likely get lost or give up?)

**3.2 Broken Reference Audit** (depth varies by tier)

- **Exhaustive / Expanded tier:** Scan all markdown files for internal links (`[text](path)` patterns). Report every broken link with source file, line number, and target. Report every orphaned file (not linked from any other file). This is a complete audit — no sampling.
- **Targeted tier:** Scan all markdown files for internal links. Report broken links: `[N] broken` (list top 10 with source file and target). Report orphaned files: `[N] orphaned`.

For all tiers:
- Verify broken links are actually broken (not relative paths that resolve in a different context)
- Classify orphaned files: truly orphaned vs. intentionally standalone (templates, archives, entrypoints)

**3.3 Coverage and Utilization Assessment** (depth varies by tier)

- **Exhaustive tier:** If a technique/pattern index exists, cross-reference every indexed item against every content file to produce a complete utilization matrix. Report: `[N]/[Total] techniques referenced ([%])`. List unreferenced techniques.
- **Expanded tier:** Cross-reference all indexed items against the 30–50 files already read in Phase 2, plus all READMEs and guides. Report: `[N]/[Total] techniques referenced ([%])`.
- **Targeted tier:** Sample 10 content files. Report: how many reference their methodology or cite their sources? Calculate documentation-to-usage gap: `[N]%`.

**Phase 3 Checkpoint — record before proceeding:**
```
Analysis tier: [Exhaustive / Expanded / Targeted]
Critical path friction: [High/Medium/Low] for each of 3 paths
Broken references: [N] (of [Total links checked])
Orphaned files: [N] (of which [N] intentionally standalone)
Documentation-to-usage gap: [N]%
Technique utilization rate: [N]% (if technique index exists)
Highest-friction user journey: [Which of the 3 paths]
```

---

### Phase 3.5: Cross-Repository Pattern Analysis (Exhaustive and Expanded tiers only)

**Goal:** Identify systemic patterns that only become visible when analyzing many files together. Skip this phase for Targeted tier.

This phase exploits the ability to hold large portions of the repository in context simultaneously — something that sampling-based analysis cannot achieve.

**3.5.1 Structural Pattern Correlation**
- Correlate quality scores (Phase 2) with file age, directory depth, and category
- Identify: Do older files consistently score lower? Do deeply nested files get orphaned more often?
- Report any statistically meaningful correlations: "[Dimension] correlates with [factor] (r=[value] or qualitative strength)"

**3.5.2 Content Evolution Patterns**
- Compare the oldest and newest files within each category
- Identify: Has quality improved, degraded, or stayed flat over time?
- Report: Which categories show active improvement vs. stagnation?

**3.5.3 Cross-Category Inconsistency Detection**
- With many files loaded, identify patterns that repeat inconsistently:
  - Sections present in some files but not others within the same category (e.g., "Constraints" section in 60% of analysis prompts)
  - Structural templates followed partially (e.g., frontmatter present but incomplete)
  - Terminology drift (same concept referred to by different names across files)
- Report: List the top 3–5 inconsistencies with file counts and specific examples

**3.5.4 Duplication and Overlap Detection**
- Identify files with substantially overlapping content or purpose
- Report: `[N] potential duplicates or near-duplicates` with file pairs and overlap description
- Distinguish: true duplication (should be merged) vs. intentional variation (different audience, different depth)

**Phase 3.5 Checkpoint — record before proceeding:**
```
Quality-age correlation: [Positive/Negative/None] (strength: [Strong/Moderate/Weak])
Categories improving over time: [list]
Categories stagnating: [list]
Cross-category inconsistencies: [N] identified
Potential duplicates: [N] pairs
Most significant systemic pattern: [One sentence]
```

---

### Phase 4: Root Cause Classification

**Goal:** Classify root causes — not just symptoms.

For every significant finding from Phases 1–3.5, assign one root cause:

| Root Cause Type | Definition | Typical Fix |
|-----------------|------------|-------------|
| **DRIFT** | Gradual degradation — standards exist but compliance has eroded over time | Re-establish standards, add automated checks |
| **VIOLATION** | Explicit breakage of a documented rule or convention | Fix specific instances, reinforce the rule |
| **MISSING RULE** | No standard exists to violate — the gap is in governance, not compliance | Define and document the rule, then enforce |
| **ORPHAN** | Content exists but is not integrated into navigation, indexes, or cross-references | Add to indexes, link from relevant locations |

**CRITICAL: Verify root cause classification before assigning.** Check whether:
- A "VIOLATION" is actually a "MISSING RULE" (the supposed rule may not be documented)
- A "DRIFT" is actually intentional evolution (the repository's conventions may have changed)
- An "ORPHAN" is actually deprecated content that should be archived, not linked

**Confidence level:** Assign High/Medium/Low to each classification based on strength of evidence.

---

### Phase 5: Bottleneck Identification and Action Plan

**Goal:** Converge all evidence into one primary bottleneck and a focused action plan.

**5.1 Identify the Single Primary Bottleneck**

Select exactly one from these categories:

| Bottleneck Category | Signal |
|---------------------|--------|
| **Discoverability** | Users can't find what already exists |
| **Quality Variance** | Inconsistent quality undermines trust in the whole repository |
| **Coverage Gap** | Important use cases have no content |
| **Structural Debt** | Organization fights against usability |
| **Maintenance Burden** | Content exists but can't be kept current at scale |

Support your selection with at least 3 pieces of evidence from earlier phases. Explain why this bottleneck has more downstream impact than the alternatives you considered.

**5.2 Build the Action Plan (Max 5 Items)**

Prioritize actions using this framework:
- **Priority 1:** Directly addresses the primary bottleneck
- **Priorities 2–3:** High impact, low effort (quick wins)
- **Priorities 4–5:** High impact, higher effort (scheduled work)
- **Everything else:** Explicitly listed as "not prioritized this cycle" with a one-line reason

Every action must have a measurable success criterion that can be verified without subjective judgment.

---

## False-Positive Prevention (MUST follow)

**DON'T:**
- Flag naming inconsistencies that are intentional conventions for specific content types
- Report quality variance as a problem when different categories serve fundamentally different audiences or purposes
- Count orphaned files without checking if they are intentionally standalone (e.g., templates, archives)
- Classify as DRIFT what is actually intentional evolution — check commit history or changelogs
- Recommend structural changes without considering the migration cost to existing users and links
- Flag low scores on "Technique Application" for content types where formal techniques are not applicable

**DO:**
- Trace naming patterns across multiple directories before declaring a convention violation
- Verify that quality differences actually cause user problems, not just aesthetic inconsistency
- Check whether orphaned files are referenced via search, imports, or external links before flagging
- Confirm that broken links are actually broken (not relative paths that resolve in a different context)
- Consider the repository's stage of maturity — early-stage repos have different standards than mature ones
- Validate that recommended actions are feasible given the repository's size and contributor base

---

## Expected Output

Deliver a structured report with the following sections in order.

### Section 1: Executive Summary

```
REPOSITORY HEALTH: [Score]/100

PRIMARY BOTTLENECK: [Category name]
  [One sentence: what the core issue is]
  [One sentence: downstream impact if not addressed]

TOP ACTION: [Specific, concrete action]
  Impact: [What measurably improves]
```

### Section 2: Evidence Dashboard

```
Analysis tier: [Exhaustive / Expanded / Targeted]
Files read: [N] of [Total] ([%])
```

| Metric | Value | Status | Coverage |
|--------|-------|--------|----------|
| Total files/resources | [N] | — | — |
| README/index coverage | [N]% | [GOOD/WARN/POOR] | [N] checked |
| Naming convention compliance | [N]% | [GOOD/WARN/POOR] | [N] checked |
| Broken references | [N] | [GOOD/WARN/POOR] | [N] links checked |
| Orphaned files | [N] | [GOOD/WARN/POOR] | [N] files checked |
| Quality score range | [X]–[Y] (mean: [Z]) | [GOOD/WARN/POOR] | [N] files scored |
| Documentation-to-usage gap | [N]% | [GOOD/WARN/POOR] | [N] items checked |
| Potential duplicates | [N] pairs | [GOOD/WARN/POOR] | Exhaustive/Expanded only |

**Thresholds:** GOOD >80% | WARN 50–80% | POOR <50%

### Section 3: Detailed Findings

For each finding, use this format. Finding count scales with analysis depth:
- **Exhaustive tier:** Up to 20 findings (full evidence available to support more)
- **Expanded tier:** Up to 15 findings
- **Targeted tier:** Up to 10 findings

```
## Finding [N]: [Short Title]

Type: [DRIFT | VIOLATION | MISSING RULE | ORPHAN]
Location: [Specific file paths]
Evidence: [Concrete observation with numbers]
Impact: [Who is affected and how]
Severity: [CRITICAL | HIGH | MEDIUM | LOW]
Confidence: [High | Medium | Low]
```

### Section 3.5: Cross-Repository Patterns (Exhaustive and Expanded tiers only)

```
SYSTEMIC PATTERNS IDENTIFIED: [N]

Pattern 1: [Short title]
  Scope: [N] files across [N] categories
  Description: [What the pattern is]
  Evidence: [Specific files, metrics, or correlations]
  Implication: [What this means for repository health]

Pattern 2: ...
```

Include: quality-age correlations, stagnating categories, terminology drift, structural template inconsistencies, and duplicate/overlapping content.

---

### Section 4: Bottleneck Analysis

```
PRIMARY BOTTLENECK: [Category]

Evidence:
1. [Finding with file path or metric]
2. [Finding with file path or metric]
3. [Finding with file path or metric]

Why this matters most:
[2–3 sentences on downstream impact]

What this is NOT about:
[1 sentence naming what you explicitly deprioritized and why]
```

### Section 5: Prioritized Action Plan

| Priority | Action | Type | Impact | Success Criterion |
|----------|--------|------|--------|-------------------|
| 1 | [Specific action] | [Fix/Create/Restructure] | [HIGH/MED/LOW] | [Measurable outcome] |
| 2 | ... | ... | ... | ... |

**Not prioritized this cycle:**
- [Action]: [One-line reason for deferral]

### Section 6: Self-Audit Verification

| Requirement | Met? | Evidence Location |
|-------------|------|-------------------|
| Analysis tier selected and justified | [Y/N] | Phase 0 Checkpoint |
| Analysis depth matches selected tier | [Y/N] | Phases 1–3.5 |
| Every finding cites specific file paths | [Y/N] | Section 3 |
| Quantitative metrics included | [Y/N] | Section 2 |
| Exactly one primary bottleneck identified | [Y/N] | Section 4 |
| Max 5 actions in plan | [Y/N] | Section 5 |
| No hedging language ("seems like", "might have") | [Y/N] | Full report |
| Every finding classified as DRIFT/VIOLATION/MISSING RULE/ORPHAN | [Y/N] | Section 3 |
| Every action has a measurable success criterion | [Y/N] | Section 5 |
| Phase checkpoints completed before advancing | [Y/N] | Phases 0–3.5 |
| Cross-repository patterns analyzed (if Exhaustive/Expanded) | [Y/N/NA] | Section 3.5 |
| False-positive prevention rules applied | [Y/N] | Findings |

**If any row is "N", revise the report before delivering.**

---

## Example Output

```markdown
# Repository Improvement Analysis Report

## Phase 0: Adaptive Depth

Total files: 1,247
Average file size: ~120 lines
Selected tier: Expanded
Rationale: 1,247 files exceeds Exhaustive threshold; Expanded tier provides
stratified sampling of 42 files for quality and full link audit.

## Executive Summary

REPOSITORY HEALTH: 72/100

PRIMARY BOTTLENECK: Quality Variance
  Content quality ranges from 1.8 to 4.6 across categories, with 3 of 8 categories
  below the 3.0 threshold, concentrated in the oldest content directories.
  New contributors distrust the entire repository when they encounter low-quality
  files, reducing adoption of even the strong categories.

TOP ACTION: Add output specification and verification sections to the 22 files
in domain-productivity/ and domain-decision-making/ currently missing them.
  Impact: Raises 2 category averages from 2.1 to 3.5+, measurable via re-scoring

## Evidence Dashboard

Analysis tier: Expanded
Files read: 312 of 1,247 (25%)

| Metric | Value | Status | Coverage |
|--------|-------|--------|----------|
| Total files/resources | 1,247 | — | — |
| README/index coverage | 85% | GOOD | 47 dirs checked |
| Naming convention compliance | 78% | WARN | 187 files checked |
| Broken references | 14 | WARN | 892 links checked |
| Orphaned files | 31 | WARN | 1,247 files checked |
| Quality score range | 1.8–4.6 (mean: 3.4) | WARN | 42 files scored |
| Documentation-to-usage gap | 38% | POOR | 250 techniques checked |
| Potential duplicates | 4 pairs | WARN | Expanded analysis |

## Detailed Findings

## Finding 1: Quality Cliff Between Technical and Non-Technical Categories

Type: DRIFT
Location: domain-software-engineering/analysis/ vs domain-productivity/validation/
Evidence:
- Analysis prompts (n=8 scored): average quality 4.3/5.0
- Productivity prompts (n=6 scored): average quality 2.1/5.0
- 7 of 9 productivity prompts lack an output specification section
- 0 of 9 productivity prompts include false-positive prevention
Impact: Contributors using productivity prompts produce inconsistent results;
they may abandon the repository for those use cases entirely.
Severity: HIGH
Confidence: High — scoring methodology applied consistently across 42 files, gap is 2+ points

## Finding 2: Orphaned Content in Legacy Directories

Type: ORPHAN
Location: prompts/archived/ (31 files), domain-presentations/visual-planning/ (8 files)
Evidence:
- 31 files in prompts/archived/ are not linked from any README, index, or guide
- 8 files in visual-planning/ are not referenced in the presentations README
- Full link audit: 0 of 39 orphans found in any navigation path (892 links checked)
Impact: Useful content is invisible to users who navigate via indexes and READMEs.
Severity: MEDIUM
Confidence: High — verified via full link audit of all markdown files

## Finding 3: Naming Convention Divergence in Newer Directories

Type: MISSING RULE
Location: domain-image-generation/worksheet-generators/ (12 files),
domain-agentic-resources/skills/ (6 files)
Evidence:
- Repository convention: {domain}_{function}.md
- Worksheet generators use: worksheet_{subject}_{grade}.md (12/45 files)
- Skills use directory-based naming: {skill-name}/SKILL.md (6 directories)
- No documented exception policy for these naming patterns
- Naming audit checked 187 files across all categories
Impact: Automated tooling and search scripts built for the standard pattern
miss these files. Manual discovery requires directory browsing.
Severity: LOW
Confidence: Medium — the naming deviations may be intentional but are undocumented

## Finding 4: Broken Cross-References in Guide Documents

Type: VIOLATION
Location: AI_AGENT_QUICK_START.md (3 broken links),
domain-agentic-resources/README.md (2 broken links)
Evidence:
- AI_AGENT_QUICK_START.md:47 links to "prompts/" which was renamed to "domain-*/"
- AI_AGENT_QUICK_START.md:128 links to a deleted file
- domain-agentic-resources/README.md:89 references a moved skill directory
Impact: Users following the primary guide encounter dead ends on critical paths.
Severity: HIGH
Confidence: High — links verified via filesystem check, all return 404

## Finding 5: Low Technique Utilization Rate

Type: DRIFT
Location: techniques/MASTER_TECHNIQUE_INDEX.md vs content files across repository
Evidence:
- 250 techniques documented in master index
- Of 42 scored files, only 9 reference any techniques (21%)
- Of the 9 that reference techniques, only 3 use the canonical IDs
- Cross-reference against full index: 38 of 250 techniques (15%) appear anywhere
Impact: The technique library — a major differentiator — provides limited value
because most content was written without consulting it.
Severity: MEDIUM
Confidence: High — Expanded tier cross-referenced all 250 techniques against 312 read files

## Cross-Repository Patterns (Expanded Tier)

SYSTEMIC PATTERNS IDENTIFIED: 3

Pattern 1: Quality degrades with file age
  Scope: 42 scored files across 8 categories
  Description: Files older than 6 months average 2.4/5.0; files newer than 3 months
  average 4.1/5.0. The gap is consistent across categories.
  Evidence: domain-productivity/ (oldest files: 1.8 avg) vs domain-software-engineering/
  analysis/ (newest files: 4.5 avg). Correlation between file age and quality score
  is strong negative.
  Implication: Quality standards have improved but have not been backported.
  Upgrading old files is higher leverage than writing new ones.

Pattern 2: Structural template adoption is partial
  Scope: 312 files read, 187 checked for structure
  Description: 68% of files have frontmatter, but only 41% have complete frontmatter
  (all required fields). "When to Use" section present in 52% of files. "False-Positive
  Prevention" present in 11%.
  Evidence: domain-software-engineering/ has 89% complete frontmatter; domain-productivity/
  has 23%. No category achieves 100%.
  Implication: Templates exist but adoption is inconsistent. Automated validation
  could enforce completeness at commit time.

Pattern 3: Two near-duplicate prompt pairs detected
  Scope: 4 files across 2 categories
  Description: validation_adversarial_mini_check.md and validation_am_i_being_nuts.md
  share ~70% structural overlap. Two prompts in domain-decision-making/ cover
  identical frameworks with different formatting.
  Evidence: Side-by-side comparison shows shared sections, reworded identically.
  Implication: Merge candidates. Reducing duplication improves maintainability
  and reduces user confusion about which prompt to use.

## Bottleneck Analysis

PRIMARY BOTTLENECK: Quality Variance

Evidence:
1. Quality scores range from 1.8 to 4.6 across categories (Finding 1)
2. 3 of 8 categories fall below the 3.0 threshold for "adequate"
3. 0% of files outside domain-software-engineering/ include false-positive
   prevention sections, the single highest quality differentiator (PROMPT_QUALITY_STANDARDS.md)

Why this matters most:
Quality variance is the bottleneck because it compounds. When users encounter
a low-quality prompt, they lose confidence in the repository as a whole —
including categories that are genuinely excellent. Fixing discoverability or
structure won't help if users discover content they don't trust. Quality
variance also blocks contribution: potential contributors don't know what
standard to target because the repository demonstrates contradictory standards.

What this is NOT about:
This is not about structural organization, which is coherent and well-indexed.
Structure scored GOOD or WARN on all metrics; quality is where trust breaks down.

## Prioritized Action Plan

| Priority | Action | Type | Impact | Success Criterion |
|----------|--------|------|--------|-------------------|
| 1 | Add output specification + false-positive prevention to 22 files in domain-productivity/ and domain-decision-making/ | Fix | HIGH | 100% of files in both categories score >= 3.0 on all 5 quality dimensions |
| 2 | Fix 5 broken links in AI_AGENT_QUICK_START.md and domain-agentic-resources/README.md | Fix | HIGH | 0 broken links in primary guide documents |
| 3 | Link or archive 31 orphaned files in prompts/archived/ | Restructure | MED | 0 orphaned files in prompts/ directory |
| 4 | Document naming exception policy for worksheet generators and skills directories | Create | MED | Exception policy exists in CONTRIBUTING.md or equivalent, referenced from README |
| 5 | Add technique references (canonical IDs) to 20 highest-traffic content files | Fix | MED | >= 50% of top-20 files reference techniques by ID |

**Not prioritized this cycle:**
- Full technique utilization audit: Requires repository-wide effort; address after quality baseline is raised
- README coverage for remaining 15% of directories: Low-traffic directories; diminishing returns

## Self-Audit Verification

| Requirement | Met? | Evidence Location |
|-------------|------|-------------------|
| Analysis tier selected and justified | Y | Phase 0 (Expanded, 1,247 files) |
| Analysis depth matches selected tier | Y | 42 files scored, 892 links checked, 187 naming checks |
| Every finding cites specific file paths | Y | Findings 1–5 |
| Quantitative metrics included | Y | Evidence Dashboard |
| Exactly one primary bottleneck identified | Y | Bottleneck Analysis |
| Max 5 actions in plan | Y | Action Plan (5 items) |
| No hedging language | Y | Full report reviewed |
| Every finding classified | Y | Findings 1–5 (DRIFT x2, ORPHAN, MISSING RULE, VIOLATION) |
| Every action has measurable success criterion | Y | Action Plan, column 5 |
| Phase checkpoints completed | Y | Phases 0–3.5 |
| Cross-repository patterns analyzed | Y | 3 patterns identified (Section 3.5) |
| False-positive prevention applied | Y | Finding 3 notes intentionality uncertainty |
```

---

## Customization Guide

- **For code repositories** (not content/docs): Replace the Phase 2 quality scoring dimensions with code-specific metrics (test coverage, linting compliance, documentation coverage). Swap "Technique Application" for "Test Coverage" and "Actionability" for "CI/CD Integration."
- **For monorepos with multiple teams:** Run Phase 2 assessment per team/ownership boundary rather than per directory. Add a dimension: "Cross-Team Consistency." Phase 3.5 cross-repository patterns are especially valuable here — correlate quality with team ownership.
- **For time-constrained audits:** Run Phases 1 and 3 only (structure + gaps). Skip Phases 2 and 3.5. Note in the report that quality assessment and pattern analysis were deferred.
- **Overriding the tier selection:** If you have specific reasons to use a different tier than the size-based default (e.g., you know certain directories are irrelevant, or you want to deeply audit only a subset), document your rationale in the Phase 0 checkpoint and adjust subsequent sample sizes accordingly.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Single-sentence objective anchors the entire analysis to one measurable goal
- **ST-02 (Structured Sequential Instructions):** Six-phase workflow (0–5) with explicit ordering, dependencies, and tier-adaptive depth
- **RT-02 (Multi-Dimensional Analysis):** Each finding analyzed across type, location, evidence, impact, severity, and confidence
- **RT-05 (Evidence-Based Reasoning):** File paths, metrics, and counts required for every claim — no unsupported assertions
- **RT-06 (Correlation and Cross-Analysis):** Phase 3.5 correlates quality scores with file age, directory depth, and category to surface systemic patterns invisible to sampling
- **DS-04 (Pattern Recognition Requests):** Phase 3.5 explicitly directs identification of cross-category inconsistencies, terminology drift, and duplication patterns
- **DS-06 (Prioritization Guidance):** Max 5 actions, explicit deprioritization with reasons, severity ranking
- **CM-07 (Token-Budget-Aware Progressive Loading):** Adaptive Depth Strategy (Phase 0) scales analysis from sampling to exhaustive based on repository size and available context capacity
- **DT-05 (Element-by-Element Assessment Matrix):** Exhaustive tier enables file-by-file quality census rather than statistical sampling
- **QA-08 (Gate-Based Verification):** Phase checkpoints must be recorded before advancing to the next phase
- **DD-07 (Self-Audit Table):** Final verification table ensures all quality requirements are met before delivery
- **DP-09 (Single Primary Constraint):** Forces identification of exactly one bottleneck, preventing diffuse recommendations
- **QS-04 (Drift vs Violation Distinction):** Four-way root cause classification prevents treating symptoms as causes
- **CM-02 (Constraint Specification):** Explicit Must/Must-Not boundaries prevent common failure modes
- **DT-04 (Multi-Layer Analysis):** Phase 2 (micro: individual file scoring), Phase 3.5 (meso: cross-file patterns), and Phase 5 (macro: cross-category bottleneck)
- **RP-01 (Expert Role Assignment):** Repository Quality Architect framing establishes appropriate expertise and skepticism

---

## Related Prompts

- [architecture_layer_identification.md](architecture/architecture_layer_identification.md) — For deeper analysis of a repository's architectural layers
- [evolution_technical_debt_estimation.md](evolution/evolution_technical_debt_estimation.md) — For quantifying technical debt within the codebase
- [quality_code_complexity_analysis.md](quality/quality_code_complexity_analysis.md) — For focused code complexity analysis at the file/function level
- evolution_code_churn_analysis.md — For identifying hotspots via change frequency analysis

---

**Version:** 4.0
**Last Updated:** 2026-02-15
