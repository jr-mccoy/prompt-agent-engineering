# Technique Analysis: docs-cleaner

**Resource Type:** Skill
**Path:** `claude-code-resources/skills/document-processing/docs-cleaner/`
**Date Analyzed:** 2025-12-22
**Bundled Resources:** 136 lines (1 reference: value_analysis_template.md)
**Complexity:** 4/5 (Structured decision framework with quality gates)

## Overview

The `docs-cleaner` skill provides a systematic framework for consolidating redundant documentation while preserving 100% of valuable content. It uses a four-phase workflow with section-by-section value analysis to reduce documentation sprawl without information loss.

**Key Innovation:** Color-coded value categorization (Keep/Condense/Delete) combined with quantitative before/after metrics and mandatory preservation checklists.

## Identified Techniques

### Technique 1: Critical Evaluation Gate
- **Category:** QA (Quality Assurance)
- **Pattern:** Mandatory analysis before any destructive action
- **Example from resource:** "**Critical evaluation before deletion.** Never blindly delete. Analyze each section's unique value before proposing removal."
- **Maps to existing:** NEW - **QA-23 Critical Evaluation Gate**
- **Effectiveness:** Prevents premature deletion by forcing systematic analysis before action

### Technique 2: Section-by-Section Value Mapping
- **Category:** DS (Domain-Specific - Documentation Engineering)
- **Pattern:** Tabular analysis of each documentation section with value justification
- **Example from resource:**
```markdown
| Section | Lines | Value | Reason |
|---------|-------|-------|--------|
| API Reference | 25 | Keep | Unique endpoint documentation |
| Setup Steps | 40 | Condense | Verbose but essential |
| Test Results | 30 | Delete | One-time record, not reference |
```
- **Maps to existing:** NEW - **DS-97 Section-by-Section Value Mapping**
- **Effectiveness:** Provides granular visibility into what will be kept/deleted, enabling informed decisions

### Technique 3: Three-Tier Value Classification
- **Category:** ST (Structural Techniques)
- **Pattern:** Color-coded classification system (Keep=Green, Condense=Yellow, Delete=Red)
- **Example from resource:**
```markdown
Value categories:
- **Keep**: Unique, essential, frequently referenced
- **Condense**: Valuable but verbose
- **Delete**: Duplicate, one-time, self-evident, outdated
```
- **Maps to existing:** NEW - **ST-36 Three-Tier Value Classification**
- **Effectiveness:** Simple stoplight system provides clear decision criteria for each section

### Technique 4: Quantitative Before/After Metrics
- **Category:** OT (Output Techniques)
- **Pattern:** Explicit metrics showing reduction percentage and value preservation
- **Example from resource:**
```markdown
Before: 726 lines (3 files, high redundancy)
After:  ~100 lines (1 file + reference in CLAUDE.md)
Reduction: 86%
Value preserved: 100%
```
- **Maps to existing:** Extends **OT-02 (Format Specification)** → **OT-13 Quantitative Before/After Metrics**
- **Effectiveness:** Demonstrates concrete impact and builds confidence that nothing was lost

### Technique 5: Mandatory Preservation Checklist
- **Category:** QA (Quality Assurance)
- **Pattern:** Category-specific checklist to verify all essential content types are preserved
- **Example from resource:**
```markdown
Before finalizing, confirm preservation of:
- [ ] Essential procedures (setup, configuration)
- [ ] Key constraints and gotchas
- [ ] Troubleshooting guides
- [ ] Technical debt / roadmap items
- [ ] External links and references
- [ ] Debug tips and code snippets
```
- **Maps to existing:** Extends **QA-01 (Validation Step)** → **QA-24 Mandatory Preservation Checklist**
- **Effectiveness:** Prevents accidental loss of critical content types during consolidation

### Technique 6: Anti-Pattern Table with Solutions
- **Category:** IT (Interaction Techniques)
- **Pattern:** Explicit documentation of common mistakes with corrective actions
- **Example from resource:**
```markdown
| Pattern | Problem | Solution |
|---------|---------|----------|
| Blind deletion | Loses valuable information | Section-by-section analysis first |
| Keeping everything | No reduction achieved | Apply value criteria strictly |
| Multiple sources of truth | Future divergence | Single authoritative location |
| Orphaned references | Broken links | Update all references after consolidation |
```
- **Maps to existing:** NEW - **IT-33 Anti-Pattern Table with Solutions**
- **Effectiveness:** Proactively addresses common failures, accelerating learning curve

### Technique 7: Four-Phase Structured Workflow
- **Category:** DS (Domain-Specific - Documentation Engineering)
- **Pattern:** Sequential phases with clear deliverables: Discovery → Value Analysis → Consolidation Plan → Execution
- **Example from resource:**
```markdown
### Phase 1: Discovery (identify all files, count lines, map overlap)
### Phase 2: Value Analysis (section-by-section table)
### Phase 3: Consolidation Plan (target structure with metrics)
### Phase 4: Execution (consolidate, delete, update references, verify links)
```
- **Maps to existing:** Extends **DS-01 (Multi-Step Breakdown)** → **DS-98 Four-Phase Documentation Workflow**
- **Effectiveness:** Prevents rushing to execution; ensures thorough analysis before changes

### Technique 8: Output Artifacts Specification
- **Category:** OT (Output Techniques)
- **Pattern:** Explicit list of required deliverables for the task
- **Example from resource:**
```markdown
A successful cleanup produces:
1. **Consolidated document** - Single source of truth
2. **Value analysis** - Section-by-section justification
3. **Before/after metrics** - Lines reduced, value preserved
4. **Updated references** - CLAUDE.md or README with pointer to new location
```
- **Maps to existing:** Extends **OT-02 (Format Specification)** → **OT-14 Output Artifacts Specification**
- **Effectiveness:** Defines "done" criteria, preventing incomplete work

### Technique 9: Bundled Template Reference
- **Category:** IT (Interaction Techniques)
- **Pattern:** Progressive disclosure - main skill references detailed template in bundled file
- **Example from resource:** "See `references/value_analysis_template.md` for detailed criteria."
- **Maps to existing:** **IT-14 Progressive Disclosure with Lazy Loading** (already identified)
- **Effectiveness:** Keeps main instructions concise while providing depth on demand

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: Critical Evaluation Gate (QA-23)
- **Description:** Mandatory analysis checkpoint before any destructive action
- **Implementation:**
  - State the core principle at the top: "Critical evaluation before deletion"
  - Require section-by-section analysis with justifications
  - Force explicit value categorization before proposing removal
- **Use case:** Any workflow involving deletion, refactoring, or removal of existing content/code
- **Example:** Documentation cleanup, code deletion, database schema changes
- **Proposed category:** QA (Quality Assurance)
- **Proposed code:** QA-23

### Pattern 2: Section-by-Section Value Mapping (DS-97)
- **Description:** Granular tabular analysis of each component with value justification
- **Implementation:**
  - Create table with columns: Component | Size | Value Decision | Reason
  - Apply value criteria to each row
  - Require explicit justification for every decision
- **Use case:** Documentation consolidation, code refactoring, feature deprecation, database cleanup
- **Example:** Analyzing which API endpoints to deprecate, which database tables to archive
- **Proposed category:** DS (Domain-Specific - Documentation Engineering)
- **Proposed code:** DS-97

### Pattern 3: Three-Tier Value Classification (ST-36)
- **Description:** Stoplight classification system (Keep, Condense, Delete) with clear criteria
- **Implementation:**
  - Define three tiers with color coding (Green, Yellow, Red)
  - Provide explicit criteria for each tier
  - Apply consistently across all sections
- **Use case:** Prioritization, triage, decision-making on existing artifacts
- **Example:** Code review (keep/refactor/delete), feature prioritization, technical debt
- **Proposed category:** ST (Structural Techniques)
- **Proposed code:** ST-36

### Pattern 4: Quantitative Before/After Metrics (OT-13)
- **Description:** Explicit metrics showing reduction percentage and value preservation guarantee
- **Implementation:**
  - Before: [metric] (additional context)
  - After: [metric] (additional context)
  - Reduction: X%
  - Value preserved: 100%
- **Use case:** Any refactoring, consolidation, or optimization task
- **Example:** Code refactoring (LOC reduction), API consolidation (endpoint reduction), database optimization (query reduction)
- **Proposed category:** OT (Output Techniques)
- **Proposed code:** OT-13

### Pattern 5: Mandatory Preservation Checklist (QA-24)
- **Description:** Category-specific checklist to verify all essential content types are preserved
- **Implementation:**
  - Identify critical content types for the domain
  - Create checkbox list for each type
  - Require confirmation before finalization
- **Use case:** Refactoring, migration, consolidation tasks
- **Example:** Database migration (preserve constraints, triggers, indexes), code refactoring (preserve edge cases, error handling)
- **Proposed category:** QA (Quality Assurance)
- **Proposed code:** QA-24

### Pattern 6: Anti-Pattern Table with Solutions (IT-33)
- **Description:** Structured table of common mistakes with corrective actions
- **Implementation:**
  - Column 1: Anti-pattern name
  - Column 2: Problem it causes
  - Column 3: Solution/correction
  - Present early in instructions to prevent failures
- **Use case:** Complex workflows with known failure modes
- **Example:** Code review anti-patterns, API design mistakes, security pitfalls
- **Proposed category:** IT (Interaction Techniques)
- **Proposed code:** IT-33

### Pattern 7: Four-Phase Documentation Workflow (DS-98)
- **Description:** Sequential phases for documentation work: Discovery → Analysis → Planning → Execution
- **Implementation:**
  - Phase 1 (Discovery): Inventory all artifacts
  - Phase 2 (Value Analysis): Assess each component
  - Phase 3 (Consolidation Plan): Design target state
  - Phase 4 (Execution): Implement with verification
- **Use case:** Documentation consolidation, content migration, knowledge base restructuring
- **Example:** Confluence to Notion migration, API documentation consolidation
- **Proposed category:** DS (Domain-Specific - Documentation Engineering)
- **Proposed code:** DS-98

### Pattern 8: Output Artifacts Specification (OT-14)
- **Description:** Explicit enumeration of required deliverables with descriptions
- **Implementation:**
  - List each artifact by name
  - Provide 1-sentence description of each
  - Use this as "definition of done"
- **Use case:** Complex tasks with multiple deliverables
- **Example:** Architecture review (diagram + analysis + recommendations), security audit (findings + remediation plan + compliance report)
- **Proposed category:** OT (Output Techniques)
- **Proposed code:** OT-14

## Multi-Technique Combinations

The `docs-cleaner` skill demonstrates sophisticated combination of techniques:

1. **Quality Gates + Value Analysis:**
   - Critical Evaluation Gate (QA-23) prevents action
   - Section-by-Section Value Mapping (DS-97) provides granular analysis
   - Result: No deletion without justification

2. **Classification + Metrics:**
   - Three-Tier Value Classification (ST-36) categorizes content
   - Quantitative Before/After Metrics (OT-13) measures impact
   - Result: Clear decision criteria with measurable outcomes

3. **Workflow + Checklists:**
   - Four-Phase Documentation Workflow (DS-98) structures process
   - Mandatory Preservation Checklist (QA-24) validates completeness
   - Result: Systematic process with validation at end

4. **Anti-Patterns + Templates:**
   - Anti-Pattern Table (IT-33) warns of common mistakes
   - Bundled Template Reference (IT-14) provides detailed guidance
   - Result: Learn from others' mistakes, deep-dive when needed

5. **Output Artifacts + Progressive Disclosure:**
   - Output Artifacts Specification (OT-14) defines deliverables
   - Progressive Disclosure (IT-14) provides template details
   - Result: Clear expectations with depth on demand

## Integration Notes

### For MASTER_TECHNIQUE_INDEX.md:
1. **Add 8 new techniques:**
   - QA-23: Critical Evaluation Gate
   - DS-97: Section-by-Section Value Mapping
   - ST-36: Three-Tier Value Classification
   - OT-13: Quantitative Before/After Metrics
   - QA-24: Mandatory Preservation Checklist
   - IT-33: Anti-Pattern Table with Solutions
   - DS-98: Four-Phase Documentation Workflow
   - OT-14: Output Artifacts Specification

2. **Create new category if needed:**
   - "Documentation Engineering" as DS subcategory (DS-97, DS-98)

3. **Cross-reference existing techniques:**
   - QA-24 extends QA-01 (Validation Step)
   - OT-13 and OT-14 extend OT-02 (Format Specification)
   - DS-98 extends DS-01 (Multi-Step Breakdown)

### For USE_CASE_LOOKUP.md:
- Add "Documentation Consolidation" use case
- Recommended techniques: QA-23, DS-97, ST-36, OT-13, QA-24, DS-98

### For AI_AGENT_QUICK_START.md:
- Add example in Section 4: "Documentation cleanup workflow"
- Demonstrate Critical Evaluation Gate + Value Mapping combination

## Summary

**Complexity Rating:** 4/5

The `docs-cleaner` skill is a **quality-gated documentation consolidation framework** that demonstrates sophisticated use of safety mechanisms (critical evaluation gates, preservation checklists) combined with value analysis tools (section mapping, three-tier classification).

**Key Strengths:**
1. **Safety-first approach:** Multiple gates prevent accidental information loss
2. **Granular visibility:** Section-by-section analysis enables informed decisions
3. **Measurable outcomes:** Quantitative metrics demonstrate value
4. **Progressive disclosure:** Main instructions concise, template provides depth

**Novel Contributions:**
- Critical Evaluation Gate pattern applicable to any destructive workflow
- Three-tier classification system (Keep/Condense/Delete) with clear criteria
- Preservation checklists for domain-specific content types
- Anti-pattern tables to accelerate learning curve

**Recommended Integration Priority:** HIGH
- Critical Evaluation Gate (QA-23): Broadly applicable to refactoring, migration, deletion workflows
- Three-Tier Value Classification (ST-36): Useful for prioritization and triage tasks
- Quantitative Before/After Metrics (OT-13): Standard for any optimization or consolidation work

**Lines of Bundled Knowledge:** 136 lines
- SKILL.md: 85 lines
- references/value_analysis_template.md: 51 lines
