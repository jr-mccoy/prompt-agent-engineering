---
title: "Repository Improvement Audit Master Prompt"
category: software-engineering/improvement
description: "Run a full-repository audit for quality, structure, duplication, metadata consistency, discoverability, and maintainability, then produce a phased implementation roadmap executable across future sessions."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - RT-05
  - DS-06
  - QA-01
  - QA-02
difficulty: advanced
tags:
  - repository-audit
  - implementation-roadmap
  - quality-systems
  - metadata-governance
  - maintainability
updated: "2026-04-19"
related_prompts:
  - domain-software-engineering/analysis/repository_analysis_for_improvements.md
  - domain-software-engineering/improvement/improvement_refactoring.md
  - domain-software-engineering/improvement/improvement_best_practice_analysis.md
---

# Repository Improvement Audit Master Prompt

**Objective:** Audit the repository (full or scoped) for quality, structure, duplication, metadata consistency, discoverability, and maintainability, then produce a phased implementation plan that can be executed safely across multiple future sessions.

---

## When to Use

- Use when the repository has grown organically and quality is uneven.
- Use when multiple contributors/agents created overlapping docs or conflicting guidance.
- Use when you need a multi-session implementation backlog instead of one-off recommendations.
- Don't use when you only need a single-file rewrite; use a targeted prompt instead.

---

## Required Inputs

Provide all inputs before beginning:

1. **Repository root path**
   - Example: `/workspace/Prompting-guides`
2. **Target scope**
   - Full repo, or specific directories only
   - Example: `domain-engineering-workflows/` and `techniques/`
3. **Constraints**
   - Access mode: read-only or write-enabled
   - Time budget: e.g., 30 minutes, 2 hours, multi-day
   - Risk tolerance: conservative, balanced, aggressive
4. **Priority preference**
   - Quick wins first, deep refactor first, or balanced sequence

If any required input is missing, stop and request it.

---

## Constraints (Non-Negotiable)

- Every finding **must include evidence** with exact file paths and at least one distinctive string.
- **Do not invent** files, metrics, ownership, dates, or test results.
- Each finding must separate:
  - **Observed issue** (what is directly evidenced)
  - **Inferred risk** (what could happen if unresolved)
- Assign a **confidence level** per finding: High / Medium / Low.
- If uncertainty remains after verification, mark as “Needs Validation” instead of asserting.

---

## Instructions

1. **Inventory current repository information architecture**
   - Map top-level and key nested directories.
   - Identify entry points (`README.md`, index files, master references).
   - Note gaps in navigability (missing index/readme, orphaned sections).

2. **Detect duplication and conflicts**
   - Identify duplicate/near-duplicate technique docs and overlapping workflows.
   - Detect stale or deprecated references (especially index drift).
   - Flag naming anomalies (pattern breaks, inconsistent prefixes/suffixes).
   - For each suspected duplicate/conflict, provide side-by-side evidence strings.

3. **Evaluate prompt quality against Tier criteria**
   - Use `PROMPT_QUALITY_STANDARDS.md` as the benchmark.
   - Assess frontmatter completeness, objective clarity, instruction structure, false-positive prevention, confidence handling, output specification, and example quality.
   - Explicitly mark each audited prompt’s likely tier and why.

4. **Map findings into a prioritized implementation backlog**
   - Convert each verified finding into a concrete task.
   - Include severity, confidence, effort, impact, and dependencies.
   - Group into low-risk quick wins vs structural/systemic changes.

5. **Produce phased implementation plan**
   - **Phase 0: Quick wins** (high-confidence, low-risk, low-effort)
   - **Phase 1: Normalization** (naming, metadata, cross-link consistency)
   - **Phase 2: Systemic improvements** (template upgrades, architecture changes, governance rules)
   - Ensure each phase is independently executable in separate sessions.

6. **Define acceptance criteria and verification checks per task**
   - Each task must include “done when” criteria.
   - Add objective verification checks (commands or deterministic file checks).
   - Include rollback notes for risky changes.

7. **Output session-aware execution guidance**
   - Provide task ordering that minimizes merge conflicts.
   - Mark what can run in parallel and what must be sequential.
   - Include “recommended next session starting point.”

---

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Report a duplicate based only on title similarity.
- Label references as stale without checking current target files.
- Infer missing frontmatter fields without opening the file.
- Treat intentional naming exceptions as defects without documented evidence.
- Claim “repo-wide” impact from a single sampled folder.

✅ **DO:**
- Verify each claim with direct file inspection and exact path references.
- Capture at least one distinctive string per evidence item for reproducibility.
- Check both source and target when evaluating cross-links.
- Distinguish “observed issue” from “inferred risk” in every finding.
- Use “Needs Validation” when evidence is partial or ambiguous.

---

## Dual-Failure Prevention (QA-20 style quality guard)

Evaluate output for both failure directions:

- **Harmful failure:** Overstates findings, invents evidence, or prescribes risky large-scale refactors without dependency mapping.
- **Unhelpful failure:** Gives generic advice without executable tasks, verification checks, or phased sequencing.

A valid output must be both accurate and operationally useful.

---

## Expected Output Format

Return output in this structure:

1. **Executive Summary**
   - Scope audited, overall health snapshot, top bottlenecks, recommended starting phase.

2. **Findings Table**
   - Columns: `Severity | Confidence | Evidence (Path + Distinctive String) | Observed Issue | Inferred Risk | Impact | Recommended Change`

3. **Implementation Roadmap**
   - Organized by Phase 0 / 1 / 2
   - Includes effort/impact matrix and dependency notes

4. **Ordered AI-Agent Task List**
   - Task IDs, file scope, deterministic steps, acceptance criteria, verification checks

5. **First 5 PRs to Open (Low-risk, Scoped)**
   - Each with explicit file set, rationale, and rollback plan

---

## Worked Example Output (Illustrative)

```markdown
# Repository Improvement Audit Report

## Executive Summary

- **Repository Root:** /workspace/Prompting-guides
- **Scope:** Full repository with emphasis on workflow and technique governance artifacts
- **Mode:** Read-only analysis
- **Time Budget:** 2-hour diagnostic pass
- **Risk Tolerance:** Conservative
- **Priority Preference:** Quick wins first

### Headline Assessment

- Repository has strong content volume but uneven standardization.
- Quality and discoverability issues are concentrated in indexing, naming consistency, and metadata completeness.
- Most immediate leverage is from cross-link and frontmatter normalization before deep refactor.

### Top Bottlenecks

1. Duplicate/near-duplicate workflow and technique-adjacent docs create routing ambiguity.
2. Some index/README guidance appears stale relative to current file inventory.
3. Naming conventions vary across similarly purposed files, reducing scanability.
4. Frontmatter coverage and completeness are inconsistent in legacy documents.

### Recommended Starting Point

- Start with **Phase 0** to reduce confusion fast and create stable baselines for deeper changes.

---

## Findings Table

| Severity | Confidence | Evidence (Path + Distinctive String) | Observed Issue | Inferred Risk | Impact | Recommended Change |
|---|---|---|---|---|---|---|
| High | High | `domain-engineering-workflows/workflows/workflow_engineering_incident_root_cause_analysis.md` + "incident root cause" and `domain-engineering-workflows/workflows/workflow_engineering_incident_root_cause_analysis.md` + "incident rca" | Near-duplicate workflow intent likely exists in two files with overlapping purpose. | Users and agents may pick different prompts for same job, fragmenting quality and updates. | Reduced consistency and duplicated maintenance effort. | Run a side-by-side diff, select canonical file, and convert the other into a redirect/deprecation stub. |
| High | Medium | `domain-engineering-workflows/workflows/workflow_engineering_api_design_review.md` + "api review" and `domain-engineering-workflows/workflows/workflow_engineering_api_design_review.md` + "api design review" | Overlapping workflow scope without explicit boundary guidance. | Duplicate evolution creates conflicting standards over time. | Slower prompt selection and drift in output quality. | Add explicit “use when / don’t use when” disambiguation and link both files bidirectionally. |
| Medium | High | `domain-engineering-workflows/README.md` + "improvement/ # Refactoring and improvement guidance" | Improvement section summary is broad and may under-index new specialized prompts. | New assets remain under-discovered, reducing reuse. | Discoverability debt and repeated reinvention. | Add a curated improvement workflow list with one-line intent summaries. |
| Medium | Medium | Legacy `work_better_*` prefixed files compared with domain-prefixed replacements | Naming anomaly suggests legacy or accidental divergence from dominant prefix pattern. | Searchability and alphabetical grouping degrade; scripts may miss files by prefix pattern. | Increased cognitive load and indexing complexity. | Rename or document intentional exception in naming conventions reference. |
| High | Medium | Multiple legacy prompts lacking full Tier-1 frontmatter fields, validated by spot checks against `PROMPT_QUALITY_STANDARDS.md` required template | Frontmatter and quality structure not consistently aligned with Tier-1 standard. | Harder automation, lower consistency, and reduced quality assurance coverage. | Quality variance persists and scaling maintenance is harder. | Introduce staged frontmatter backfill plan plus lint-like verification checklist. |

---

## Effort/Impact Matrix

| Impact \ Effort | Low Effort | Medium Effort | High Effort |
|---|---|---|---|
| High Impact | Link fixes, disambiguation notes, README indexing updates | Naming normalization pass with redirects | Cross-repo tier uplift program with review gates |
| Medium Impact | Metadata field backfills for critical directories | Deprecation map generation | Automated consistency audit tooling |
| Low Impact | Cosmetic heading consistency | Optional tag expansion | Full historical archival restructuring |

---

## Implementation Roadmap

### Phase 0 — Quick Wins (1-2 sessions)

**Goal:** Improve discoverability and reduce confusion without risky structural edits.

1. Add missing cross-links between overlapping workflow files.
2. Add “canonical vs related” notes where near-duplicates exist.
3. Update domain improvement index section with direct links to active prompts.
4. Add deprecation warning blocks to clearly superseded files (no deletion yet).

**Acceptance Criteria:**
- Every overlapping pair has explicit routing guidance.
- Improvement workflows are discoverable from domain index in <=2 clicks.
- No file removals; all changes reversible.

**Verification Checks:**
- Link-check internal markdown references for modified files.
- Confirm each deprecated file points to canonical replacement.

---

### Phase 1 — Normalization (2-4 sessions)

**Goal:** Normalize metadata and naming to improve consistency and machine-processability.

1. Define naming convention policy for workflow files and edge-case exceptions.
2. Rename clear anomalies (or document intentional exceptions).
3. Backfill full frontmatter fields for priority directories.
4. Add standardized “When to Use / Don’t Use” sections where missing.

**Acceptance Criteria:**
- Naming compliance baseline documented and improved.
- Priority directory frontmatter coverage reaches agreed threshold (e.g., 95%+).
- Each normalized file has deterministic before/after diff scope.

**Verification Checks:**
- Run file-name pattern audit script.
- Run frontmatter completeness check against Tier-1 required fields.
- Spot-review 10 normalized files for semantic integrity.

---

### Phase 2 — Systemic Improvements (multi-session)

**Goal:** Create durable quality governance mechanisms.

1. Establish reusable Tier-1 prompt template and migration playbook.
2. Add repository-level QA checklist for new prompt submissions.
3. Introduce periodic audit cadence (monthly drift + quarterly deep audit).
4. Define ownership model for index and taxonomy governance.

**Acceptance Criteria:**
- New prompts follow template by default.
- Drift reports identify regressions before accumulation.
- Ownership and escalation paths are documented.

**Verification Checks:**
- Validate template adoption in newly added prompts.
- Confirm scheduled audit documents exist and are linked from root governance docs.

---

## Ordered Task List (AI-Agent Executable)

1. **TASK-001: Overlap Pair Inventory**
   - Scope: `domain-engineering-workflows/workflows/`
   - Steps: enumerate likely duplicates by title similarity + manual semantic check.
   - Done when: each pair labeled as `duplicate`, `related`, or `distinct` with evidence.
   - Verify: review evidence table includes file path + distinctive string for both files.

2. **TASK-002: Deprecation Routing Notes**
   - Scope: confirmed duplicate or superseded files
   - Steps: add standardized deprecation note pointing to canonical doc.
   - Done when: deprecated files contain explicit replacement link.
   - Verify: open each deprecated file and confirm link resolves.

3. **TASK-003: Improvement Index Strengthening**
   - Scope: domain-level README and improvement subsection
   - Steps: add link list with one-line intent summaries.
   - Done when: all active improvement prompts listed and reachable.
   - Verify: click-through validation from domain README.

4. **TASK-004: Naming Conventions Audit + Action**
   - Scope: workflow and improvement directories
   - Steps: detect outliers; rename or annotate exceptions.
   - Done when: each outlier has disposition (`renamed` or `intentional`).
   - Verify: naming pattern report and changed-file list.

5. **TASK-005: Frontmatter Coverage Backfill (Priority Set)**
   - Scope: highest-traffic directories first
   - Steps: add missing Tier-1 fields without changing semantic behavior.
   - Done when: required frontmatter keys present for priority set.
   - Verify: frontmatter checker returns pass for scoped directories.

6. **TASK-006: Tier Evaluation Notes**
   - Scope: sampled prompts across directories
   - Steps: assign likely tier with rationale tied to standards.
   - Done when: each sampled file has tier label + gap notes.
   - Verify: each tier label references concrete criteria.

7. **TASK-007: Session Sequencing Plan**
   - Scope: roadmap artifact
   - Steps: sequence tasks by dependency and conflict risk.
   - Done when: next-session queue and parallelizable bundles are explicit.
   - Verify: no task depends on future undefined artifact.

---

## First 5 PRs to Open

### PR-1: Improvement README Link Map
- **Scope:** Add/expand improvement links in domain README.
- **Risk:** Low
- **Why first:** Immediate discoverability gain, minimal coupling.

### PR-2: Duplicate Workflow Disambiguation Notes
- **Scope:** Add “use when / don’t use when” and related links for overlapping workflow pairs.
- **Risk:** Low
- **Why second:** Reduces user selection errors quickly.

### PR-3: Deprecation Stubs for Confirmed Superseded Docs
- **Scope:** Mark superseded files, preserve content history.
- **Risk:** Low-Medium
- **Why third:** Prevents accidental use of obsolete guidance.

### PR-4: Naming Anomaly Cleanup Batch
- **Scope:** Normalize clear outlier filenames; update inbound links.
- **Risk:** Medium
- **Why fourth:** Improves long-term discoverability and tooling reliability.

### PR-5: Frontmatter Backfill (Priority Directories)
- **Scope:** Add required metadata fields and consistent tags.
- **Risk:** Medium
- **Why fifth:** Enables scalable QA and indexing automation.

---

## Confidence Legend

- **High:** Direct evidence confirmed in multiple files/links with explicit string matches.
- **Medium:** Strong evidence with minor contextual uncertainty.
- **Low:** Early signal requiring additional validation before action.

## Notes on Evidence Discipline

- Every finding above separates what was observed from what is inferred.
- No test results were claimed unless explicitly run and recorded.
- No file was claimed missing unless path checks confirmed absence.
```

---

## Techniques Used (Canonical IDs)

- **ST-01 (Clear Objective Statement):** Defines a precise audit goal and deliverable.
- **ST-02 (Structured Sequential Instructions):** Provides a deterministic, numbered workflow.
- **ST-03 (Output Format Specification):** Enforces standardized report and roadmap outputs.
- **RT-02 (Multi-Dimensional Analysis):** Covers quality, structure, duplication, metadata, discoverability, and maintainability.
- **RT-05 (Evidence-Based Reasoning):** Requires path-level evidence and distinctive strings.
- **DS-06 (Prioritization Guidance):** Forces phased backlog and effort/impact sequencing.
- **QA-01 (Constraint Specification):** Adds hard boundaries against fabricated claims.
- **QA-02 (Adversarial Thinking):** Includes false-positive and dual-failure prevention guards.

---

## Customization Guide

- For **read-only audits**, suppress all direct edit recommendations and emit PR-ready task scopes only.
- For **write-enabled mode**, include patch sequencing and branch/commit guidance per phase.
- For **time-boxed audits**, run Phase 0 fully, sample Phase 1, and defer Phase 2 architecture work.
