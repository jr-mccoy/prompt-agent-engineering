---
name: docs-cleaner
description: Consolidates redundant documentation while preserving all valuable content. This skill should be used when users want to clean up documentation bloat, merge redundant docs, reduce documentation sprawl, or consolidate multiple files covering the same topic. Triggers include "clean up docs", "consolidate documentation", "too many doc files", "merge these docs", or when documentation exceeds 500 lines across multiple files covering similar topics.
metadata:
  tags:
    - documentation
    - consolidation
    - deduplication
    - technical-writing
    - docs-cleanup
  updated: "2026-04-11"
---
# Documentation Cleaner

Consolidate redundant documentation while preserving 100% of valuable content.

## Core Principle

**Critical evaluation before deletion.** Never blindly delete. Analyze each section's unique value before proposing removal. The goal is reduction without information loss.

## Workflow

### Phase 1: Discovery

1. Identify all documentation files covering the topic
2. Count total lines across files
3. Map content overlap between documents

### Phase 2: Value Analysis

For each document, create a section-by-section analysis table:

| Section | Lines | Value | Reason |
|---------|-------|-------|--------|
| API Reference | 25 | Keep | Unique endpoint documentation |
| Setup Steps | 40 | Condense | Verbose but essential |
| Test Results | 30 | Delete | One-time record, not reference |

Value categories:
- **Keep**: Unique, essential, frequently referenced
- **Condense**: Valuable but verbose
- **Delete**: Duplicate, one-time, self-evident, outdated

See `references/value_analysis_template.md` for detailed criteria.

### Phase 3: Consolidation Plan

Propose target structure:

```
Before: 726 lines (3 files, high redundancy)
After:  ~100 lines (1 file + reference in CLAUDE.md)
Reduction: 86%
Value preserved: 100%
```

### Phase 4: Execution

1. Create consolidated document with all valuable content
2. Delete redundant source files
3. Update references (CLAUDE.md, README, imports)
4. Verify no broken links

## Value Preservation Checklist

Before finalizing, confirm preservation of:

- [ ] Essential procedures (setup, configuration)
- [ ] Key constraints and gotchas
- [ ] Troubleshooting guides
- [ ] Technical debt / roadmap items
- [ ] External links and references
- [ ] Debug tips and code snippets

## Anti-Patterns

| Pattern | Problem | Solution |
|---------|---------|----------|
| Blind deletion | Loses valuable information | Section-by-section analysis first |
| Keeping everything | No reduction achieved | Apply value criteria strictly |
| Multiple sources of truth | Future divergence | Single authoritative location |
| Orphaned references | Broken links | Update all references after consolidation |

## Output Artifacts

A successful cleanup produces:

1. **Consolidated document** - Single source of truth
2. **Value analysis** - Section-by-section justification
3. **Before/after metrics** - Lines reduced, value preserved
4. **Updated references** - CLAUDE.md or README with pointer to new location

---

## Core Concepts

### Documentation Entropy

Documentation systems naturally drift toward disorder over time. As teams grow, features ship, and contributors rotate, documentation accumulates redundancy, contradiction, and staleness. This phenomenon -- documentation entropy -- is the primary force this skill combats.

Key entropy signals:
- Multiple files covering the same topic with slightly different information
- Contradictory instructions across documents (e.g., different setup steps)
- "Living" docs that stopped being updated months ago
- Copy-pasted sections that diverged after the initial copy
- README files that duplicate CLAUDE.md content or vice versa

### Single Source of Truth Principle

Every piece of information should have exactly one authoritative location. When the same fact appears in multiple places, it will eventually diverge. The consolidation goal is not just fewer files -- it is ensuring each fact lives in exactly one place with clear pointers from everywhere else.

**Rule of thumb:** If changing a fact requires editing more than one file, you have a single-source-of-truth violation.

### Docs-as-Code Philosophy

Treat documentation with the same rigor as source code:
- **Version controlled** - All docs in the repository, not in wikis or external tools
- **Reviewed** - Documentation changes go through pull requests
- **Tested** - Links are validated, formatting is checked
- **Refactored** - Periodically consolidated, just like code

---

## Advanced Consolidation Strategies

### Cross-Reference Merging

When multiple documents reference each other, consolidation often reveals a natural hierarchy:

```
Before:
  SETUP.md (50 lines) -- references TROUBLESHOOTING.md
  TROUBLESHOOTING.md (80 lines) -- references SETUP.md
  FAQ.md (40 lines) -- duplicates content from both

After:
  GUIDE.md (100 lines)
    ## Setup
    ## Troubleshooting
    ## FAQ (deduplicated, unique entries only)
```

### Topic-Based Merging

Group content by topic rather than by original file:

1. **Extract** all sections from all source files
2. **Cluster** sections by topic (setup, configuration, usage, troubleshooting, etc.)
3. **Deduplicate** within each topic cluster -- keep the most complete version
4. **Reorganize** into a logical flow: concept, setup, usage, advanced, troubleshooting
5. **Link** related sections with internal anchors

### Incremental Consolidation

For large doc sets (10+ files, 2000+ lines), consolidate in phases:

| Phase | Focus | Risk |
|-------|-------|------|
| 1 | Delete obviously outdated/duplicate files | Low -- clear redundancy |
| 2 | Merge files covering the same topic | Medium -- need content comparison |
| 3 | Restructure remaining docs into logical hierarchy | High -- requires understanding of information architecture |
| 4 | Add cross-references and navigation | Low -- additive only |

---

## Templates

### Value Analysis Template

```markdown
## Documentation Value Analysis

**Scope:** [Repository/directory being analyzed]
**Date:** [Analysis date]
**Analyst:** [Who performed the analysis]

### Files Analyzed

| # | File | Lines | Last Updated | Status |
|---|------|-------|-------------|--------|
| 1 | README.md | 120 | 2026-03-15 | Active |
| 2 | SETUP.md | 85 | 2025-11-02 | Stale |
| 3 | CONTRIBUTING.md | 45 | 2026-01-20 | Active |

### Overlap Matrix

|  | README | SETUP | CONTRIBUTING |
|--|--------|-------|-------------|
| **README** | - | 40% overlap | 10% overlap |
| **SETUP** | 40% overlap | - | 5% overlap |
| **CONTRIBUTING** | 10% overlap | 5% overlap | - |

### Consolidation Recommendation

**Target structure:** [Proposed file organization]
**Expected reduction:** [X lines -> Y lines (Z%)]
**Risk assessment:** [Low/Medium/High]
```

### Consolidation Proposal Template

```markdown
## Consolidation Proposal

### Current State
- **Files:** [count]
- **Total lines:** [count]
- **Redundancy score:** [percentage of duplicated content]

### Proposed Changes

| Action | Source | Destination | Rationale |
|--------|--------|-------------|-----------|
| Merge | SETUP.md sections 1-3 | GUIDE.md ## Setup | Unique content preserved |
| Delete | FAQ.md entries 1-5 | N/A | Duplicates GUIDE.md |
| Keep | ARCHITECTURE.md | ARCHITECTURE.md | No overlap, unique value |
| Condense | CHANGELOG.md (200 lines) | CHANGELOG.md (50 lines) | Keep last 6 months only |

### After State
- **Files:** [count]
- **Total lines:** [count]
- **Reduction:** [percentage]
- **Information preserved:** 100%
```

---

## Best Practices for Maintaining Consolidated Docs

### Prevention Over Cure

After consolidation, establish practices that prevent re-accumulation:

1. **Define documentation ownership** - Each doc file has an owner who reviews changes
2. **Add "source of truth" headers** - Mark which file is authoritative for each topic
3. **Review docs in PRs** - If a PR adds a new doc file, ask whether it belongs in an existing file
4. **Quarterly doc audits** - Schedule periodic review to catch drift early
5. **Use pointers, not copies** - Link to the authoritative source rather than duplicating content

### Documentation Lifecycle

```
CREATE -> MAINTAIN -> REVIEW -> CONSOLIDATE or ARCHIVE
  |         |          |            |
  |         |          |            +-- Remove if obsolete
  |         |          +-- Quarterly audit
  |         +-- Update with code changes
  +-- New feature = new section in existing doc (preferred)
      or new doc file (only if truly distinct topic)
```

### Consolidation Cadence

| Repository Size | Recommended Cadence | Signs It Is Overdue |
|----------------|--------------------|--------------------|
| Small (< 10 docs) | Every 6 months | Any duplicate file |
| Medium (10-50 docs) | Every 3 months | 3+ files on same topic |
| Large (50+ docs) | Monthly spot-checks | Contradictory instructions found |

---

## Common Pitfalls

| Pitfall | Symptom | Solution |
|---------|---------|----------|
| Blind deletion without analysis | Users report missing information weeks later | Always perform section-by-section value analysis first |
| Keeping everything "just in case" | No meaningful reduction achieved | Apply strict value criteria: if not referenced in 6 months, archive |
| Multiple sources of truth remain | Information diverges again within weeks | Ensure each fact has exactly one authoritative location |
| Orphaned references after cleanup | Broken links in README, CLAUDE.md, or code comments | Search the entire repo for references before deleting any file |
| Consolidating without understanding | Merged docs are incoherent or poorly organized | Read all source docs fully before proposing a structure |
| Skipping the redirect step | Users cannot find content at its new location | Leave a one-line pointer file or update all known references |
| No post-consolidation ownership | Consolidated doc drifts and becomes stale | Assign an owner and add a "last reviewed" date to the doc |
| Over-consolidating into a mega-file | Single file becomes too long to navigate | Cap consolidated files at 300-400 lines; split by topic if larger |

---

## Example: Before/After Consolidation

### Before (3 files, 380 total lines, high redundancy)

**SETUP.md** (120 lines):
```markdown
# Project Setup
## Prerequisites (duplicated in README)
## Installation Steps (unique)
## Configuration (partially duplicated in CONFIG.md)
## Troubleshooting (duplicated in README)
```

**README.md** (180 lines):
```markdown
# Project Name
## Overview (unique)
## Prerequisites (duplicated in SETUP.md)
## Quick Start (condensed version of SETUP.md installation)
## Usage Examples (unique)
## Troubleshooting (duplicated in SETUP.md)
## Contributing (unique)
```

**CONFIG.md** (80 lines):
```markdown
# Configuration Guide
## Environment Variables (partially in SETUP.md)
## Advanced Configuration (unique)
## Configuration Examples (unique)
```

### After (1 file, 150 total lines, no redundancy)

**README.md** (150 lines):
```markdown
# Project Name
## Overview (from original README)
## Prerequisites (single authoritative version)
## Quick Start (consolidated from SETUP + README)
## Configuration
  ### Environment Variables (from CONFIG.md)
  ### Advanced Configuration (from CONFIG.md)
  ### Examples (from CONFIG.md)
## Usage Examples (from original README)
## Troubleshooting (single authoritative version)
## Contributing (from original README)
```

**SETUP.md** -- deleted (all unique content merged into README)
**CONFIG.md** -- deleted (all unique content merged into README)

**Metrics:**
- Files: 3 to 1 (67% reduction)
- Lines: 380 to 150 (61% reduction)
- Unique information preserved: 100%
- Redirects added: SETUP.md and CONFIG.md references updated in codebase
