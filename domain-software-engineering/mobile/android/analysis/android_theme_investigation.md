---
title: "Android Theme Investigation & Documentation"
category: mobile-development
description: "Comprehensive investigation and documentation of Android theme-related code with root cause analysis for persistent styling issues"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - analysis
  - mobile-development
  - themes
  - debugging
  - android
updated: "2025-12-30"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_compose_ui_consistency_audit.md
  - domain-software-engineering/mobile/android/analysis/android_resource_asset_analysis.md
  - domain-software-engineering/mobile/android/analysis/android_compose_ui_analysis.md
---


# Android Theme Investigation & Documentation

**Objective:** Conduct a comprehensive investigation of all theme-related code in an Android application, documenting the complete theme architecture, identifying persistent styling issues (especially stubborn color problems), analyzing UI consistency, and collaborating with the user to create a concrete remediation plan.

**When to Use:** Use this prompt when you have persistent theme issues that resist fixes (colors that keep appearing despite changes, inconsistent styling across screens), need to understand a complex or inherited theme system, want comprehensive documentation of how theming works in your app, or need to audit theme consistency before a major UI update.

---

## Context & Philosophy

This prompt addresses a common pain point: **theme issues that won't stay fixed**. These persistent problems typically stem from:
- Multiple competing sources of truth for colors/styles
- Hardcoded values overriding theme definitions
- Incorrect theme inheritance hierarchies
- Resource qualifier conflicts (night mode, API levels, etc.)
- Legacy code bypassing the theme system
- Compose and XML theme misalignment

**This Is an Investigation-First Process:**
- **Phase 1:** Comprehensive discovery of all theme-related code
- **Phase 2:** Documentation of the theme architecture
- **Phase 3:** Root cause analysis of persistent issues
- **Phase 4:** UI consistency and quality assessment
- **Phase 5:** Collaborative planning with user approval

**Critical Constraint:** Do NOT make any code changes until the investigation is complete, findings are presented, and the user has explicitly approved a remediation plan.

---

## Instructions

### CRITICAL: Verification Requirements

**Before diagnosing ANY theme issue, you MUST:**

1. **Trace actual theme inheritance** - Don't assume issues without mapping the complete theme hierarchy.
2. **Check for intentional overrides** - Search for legitimate reasons why values might differ from defaults.
3. **Understand the context** - Consider whether "inconsistencies" might be intentional design choices.
4. **Confirm actual reproduction** - Can the issue be reproduced consistently across configurations?
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `colors.xml:23`, `Theme.kt:45`).

**Finding a WELL-STRUCTURED theme is an acceptable outcome.** If the theme system is correctly configured, say so with confidence.

### False-Positive Prevention

- ❌ Do NOT flag intentional variations as theme bugs
- ❌ Do NOT assume all hardcoded colors are problems without checking context
- ❌ Do NOT report theoretical issues without demonstrating actual visual problems
- ❌ Do NOT ignore resource qualifiers when analyzing theme values
- ✅ DO trace complete theme inheritance chains before diagnosing
- ✅ DO check both Compose and XML theme layers
- ✅ DO test in both light and dark modes
- ✅ DO consider intentional per-screen customizations

---

### Step 1: Scope Definition

Begin by understanding the specific concerns. Ask the user:

1. **Primary Pain Points:**
   - "What specific theme issues keep recurring despite fixes?"
   - "Are there particular colors that appear where they shouldn't?"
   - "Which screens or components are most problematic?"

2. **Technical Context:**
   - "Is this a Compose-only, XML-only, or hybrid (Compose + XML) app?"
   - "Are you using Material Design 2, Material Design 3, or a custom design system?"
   - "Do you have separate themes for light/dark mode?"

3. **Historical Context:**
   - "Has this theme been migrated or inherited from an older codebase?"
   - "Have multiple developers worked on the theme system?"
   - "Are there known areas of technical debt in the styling?"

4. **Documentation Status:**
   - "Is there existing documentation for the theme system?"
   - "Is there a design system or style guide this should align with?"

---

### Step 2: Comprehensive Theme Discovery

Systematically search and catalog ALL theme-related code:

#### A. Theme Definition Files

Search for and document:

| File Type | Search Patterns | Purpose |
|-----------|-----------------|---------|
| **XML Themes** | `res/values*/themes.xml`, `res/values*/styles.xml` | Base theme definitions |
| **XML Colors** | `res/values*/colors.xml` | Color resource definitions |
| **Compose Theme** | `*Theme.kt`, `*Colors.kt`, `*Typography.kt`, `*Shapes.kt` | Compose theming |
| **Design Tokens** | `*Tokens.kt`, `*DesignSystem.kt` | Design system definitions |
| **Dimension Resources** | `res/values*/dimens.xml` | Spacing and sizing |

#### B. Theme Application Points

Identify where themes are applied:

| Location | What to Find | Why It Matters |
|----------|--------------|----------------|
| **AndroidManifest.xml** | `android:theme` attributes | App-wide and activity-level themes |
| **Activity/Fragment** | `setTheme()` calls | Programmatic theme changes |
| **Compose Entry Points** | `MaterialTheme {}` wrappers | Compose theme application |
| **View Inflation** | `ContextThemeWrapper` usage | Theme overrides at inflation |

#### C. Color/Style Usage Analysis

Search for all places where colors and styles are used:

```
Search Patterns:
├── Hardcoded colors: #[0-9A-Fa-f]{6,8}, Color(0x...), Color.parse
├── Resource references: @color/, R.color., colorResource()
├── Theme attributes: ?attr/, ?android:attr/, MaterialTheme.colorScheme
├── Direct color values: Color.Red, Color.White, Color(red=, Color.rgb
├── Style references: @style/, R.style., style=
└── Legacy patterns: getColor(), ContextCompat.getColor()
```

#### D. Resource Qualifier Analysis

Document all resource qualifier variations:

| Qualifier | Files Found | Potential Conflicts |
|-----------|-------------|---------------------|
| `values/` | [List files] | Base definitions |
| `values-night/` | [List files] | Dark mode overrides |
| `values-v21/` | [List files] | API 21+ overrides |
| `values-v31/` | [List files] | Material You support |
| Other qualifiers | [List files] | [Note any conflicts] |

---

### Step 3: Theme Architecture Documentation

Create a comprehensive map of the theme system:

#### A. Theme Inheritance Tree

```
Document the complete inheritance chain:

AppTheme (Application level)
├── Theme.Material3.DayNight (or parent)
│   └── [Parent theme details]
├── Overrides:
│   ├── colorPrimary → @color/...
│   ├── colorSecondary → @color/...
│   └── [All overrides]
└── Child Themes:
    ├── AppTheme.NoActionBar
    ├── AppTheme.Splash
    └── [Other variants]
```

#### B. Color Source Mapping

For each semantic color, trace its complete source chain:

| Semantic Color | XML Definition | Compose Mapping | Actual Hex Value | Used In |
|----------------|----------------|-----------------|------------------|---------|
| Primary | @color/primary | colorScheme.primary | #XXXXXX | [List locations] |
| Background | @color/background | colorScheme.background | #XXXXXX | [List locations] |
| [Continue for all colors] |

#### C. Compose-XML Bridge Analysis (If Hybrid)

Document how Compose and XML themes interact:

| Aspect | XML Source | Compose Source | Synchronized? |
|--------|------------|----------------|---------------|
| Primary Color | colors.xml | Theme.kt | Yes/No |
| Typography | styles.xml | Typography.kt | Yes/No |
| Shapes | N/A | Shapes.kt | N/A |
| [Continue] |

---

### Step 4: Root Cause Analysis for Persistent Issues

For each persistent issue the user identified, conduct deep analysis:

#### A. Color Tracing Protocol

For problematic colors that "won't go away":

```markdown
## Issue: [Color Description] appears in [Location]

### Expected Behavior
- Expected color: [What should appear]
- Expected source: [Where it should come from]

### Actual Behavior
- Actual color appearing: [Hex value if identifiable]
- Where it appears: [Specific screens/components]

### Source Tracing
1. **Direct Search Results:**
   - Files containing this color value: [List with line numbers]
   - Files referencing this as a resource: [List with line numbers]

2. **Inheritance Check:**
   - Is this color inherited from parent theme? [Yes/No]
   - Parent theme source: [File:Line]

3. **Override Analysis:**
   - Are there multiple definitions? [List all]
   - Which definition wins based on specificity/qualifier?

4. **Hardcoded Usage Check:**
   - Hardcoded instances found: [List with file:line]
   - These bypass theme system: [Explain impact]

5. **Resource Qualifier Conflicts:**
   - Does this color differ across qualifiers?
   - Which qualifier is being selected at runtime?

### Root Cause Determination
- **Primary Cause:** [Identified root cause]
- **Contributing Factors:** [Secondary issues]
- **Why Previous Fixes Failed:** [Analysis of past attempts]

### Recommended Fix
- [Specific fix with rationale]
- [Files to modify]
- [Order of changes]
```

#### B. Common Root Cause Patterns

Check for these known issues:

| Pattern | Symptoms | Detection Method |
|---------|----------|------------------|
| **Hardcoded Override** | Theme changes don't apply to specific views | Search for hex values in layout/code |
| **Wrong Theme Attribute** | Unexpected colors in themed views | Check `?attr/` vs `@color/` usage |
| **Qualifier Precedence** | Colors change unexpectedly by device | Compare all qualifier folders |
| **Compose/XML Mismatch** | Different colors in Compose vs XML views | Compare color definitions in both |
| **Parent Theme Bleed** | Unwanted colors from parent theme | Trace full inheritance chain |
| **Dynamic Color Override** | Material You breaking expected colors | Check `dynamicColor` settings |
| **Context Theme Mismatch** | Wrong theme in inflated views | Check ContextThemeWrapper usage |

---

### Step 5: UI Consistency Assessment

Evaluate theme consistency across the application:

#### A. Cross-Screen Consistency

| Element | Expected | Screen A | Screen B | Screen C | Consistent? |
|---------|----------|----------|----------|----------|-------------|
| Primary button color | #XXXXXX | [Actual] | [Actual] | [Actual] | Yes/No |
| Background color | #XXXXXX | [Actual] | [Actual] | [Actual] | Yes/No |
| Text primary | #XXXXXX | [Actual] | [Actual] | [Actual] | Yes/No |
| [Continue for key elements] |

#### B. Component Consistency

For each component type, verify consistent theming:

| Component | Uses Theme? | Hardcoded Values? | Consistent Styling? |
|-----------|-------------|-------------------|---------------------|
| Buttons | [Yes/Partial/No] | [List any] | [Yes/No - details] |
| Cards | [Yes/Partial/No] | [List any] | [Yes/No - details] |
| Text Fields | [Yes/Partial/No] | [List any] | [Yes/No - details] |
| App Bars | [Yes/Partial/No] | [List any] | [Yes/No - details] |
| Navigation | [Yes/Partial/No] | [List any] | [Yes/No - details] |
| Dialogs | [Yes/Partial/No] | [List any] | [Yes/No - details] |

#### C. State Consistency

Verify theming across different states:

| State | Theme Applied Correctly? | Issues Found |
|-------|--------------------------|--------------|
| Light Mode | [Yes/No] | [Details] |
| Dark Mode | [Yes/No] | [Details] |
| Disabled States | [Yes/No] | [Details] |
| Error States | [Yes/No] | [Details] |
| Loading States | [Yes/No] | [Details] |

---

### Step 6: Present Findings Report

Compile and present comprehensive findings:

```markdown
# Android Theme Investigation Report

## Executive Summary

### Theme System Health
| Aspect | Status | Risk Level |
|--------|--------|------------|
| Theme Architecture | [Clean/Complex/Fragmented] | [Low/Medium/High] |
| Color Consistency | [X]% consistent | [Low/Medium/High] |
| Hardcoded Values | [X] instances found | [Low/Medium/High] |
| XML-Compose Sync | [Synchronized/Partial/Divergent] | [Low/Medium/High] |
| Documentation | [Good/Partial/Missing] | [Low/Medium/High] |

### Key Findings
1. **[Most Critical Finding]** - [Impact statement]
2. **[Second Finding]** - [Impact statement]
3. **[Third Finding]** - [Impact statement]

### Persistent Issue Root Causes
| Issue | Root Cause | Complexity to Fix |
|-------|------------|-------------------|
| [Issue 1] | [Cause] | [Low/Medium/High] |
| [Issue 2] | [Cause] | [Low/Medium/High] |

---

## Theme Architecture Map

### File Inventory
**Theme Definition Files:**
- [File path]: [Purpose] - [Lines of relevant code]

**Color Definition Files:**
- [File path]: [Purpose] - [Number of colors defined]

**Style Definition Files:**
- [File path]: [Purpose] - [Key styles defined]

### Inheritance Diagram
[ASCII diagram of theme inheritance]

### Color Source Chain
[Table mapping each color from definition to usage]

---

## Issue Analysis

### Issue 1: [Persistent Color Problem]

**Problem Statement:** [What the user sees]

**Root Cause:** [Technical explanation]

**Evidence:**
- File: [path], Line [X]: [What was found]
- File: [path], Line [X]: [What was found]

**Why Previous Fixes Failed:** [Explanation]

**Recommended Solution:** [Specific steps]

[Repeat for each issue]

---

## Consistency Analysis

### Inconsistencies Found

| Location | Expected | Actual | Severity | Fix Complexity |
|----------|----------|--------|----------|----------------|
| [File:Line] | [Value] | [Value] | [High/Med/Low] | [High/Med/Low] |

### Hardcoded Values Inventory

| File | Line | Hardcoded Value | Should Reference |
|------|------|-----------------|------------------|
| [Path] | [Line] | [Value] | [Theme attribute] |

---

## Recommendations Summary

### Priority 1: Critical (Resolve Persistent Issues)
1. [Specific recommendation]
   - Files to modify: [List]
   - Estimated changes: [Count]
   - Risk: [Assessment]

### Priority 2: High (Establish Single Source of Truth)
1. [Recommendation]

### Priority 3: Medium (Improve Consistency)
1. [Recommendation]

### Priority 4: Low (Polish & Documentation)
1. [Recommendation]

---

## Questions for Discussion

Before proceeding with any changes:

1. Do these findings accurately explain the persistent issues you've experienced?
2. Are there additional problem areas I should investigate?
3. Do you agree with the root cause analysis for [specific issue]?
4. What is your priority order for addressing these issues?
5. Are there any constraints (timeline, risk tolerance) that should influence the plan?

**Please review this report. I will not make any changes until we've discussed findings and agreed on a remediation plan.**
```

---

### Step 7: Collaborative Planning

After presenting findings, work with the user to create a concrete plan:

#### A. Validate Understanding

- Confirm root cause analysis is accurate
- Discuss any findings that surprise or concern the user
- Identify any missing information

#### B. Prioritize Together

- Review recommended priorities with user
- Adjust based on user's constraints and preferences
- Identify what can be deferred vs. must be fixed

#### C. Build Remediation Plan

```markdown
## Agreed Remediation Plan

### Confirmed Understanding
- [User-validated root cause 1]
- [User-validated root cause 2]

### Phase 1: [Name] (Agreed Priority)
**Goal:** [What this achieves]

**Changes:**
1. File: [path]
   - Change: [Specific modification]
   - Rationale: [Why this fixes the issue]

2. File: [path]
   - Change: [Specific modification]
   - Rationale: [Why this fixes the issue]

**Verification:** [How to confirm the fix worked]

### Phase 2: [Name]
[Same structure]

### Phase 3: [Name]
[Same structure]

### Deferred Items
- [Item]: Reason for deferral
- [Item]: Reason for deferral

### Success Criteria
- [ ] [Specific measurable outcome]
- [ ] [Specific measurable outcome]
- [ ] [Specific measurable outcome]

### Risk Mitigation
- Before changes: [Backup/branch strategy]
- Testing approach: [How to verify]
- Rollback plan: [If issues arise]

---

**Do you approve this remediation plan?**
Reply 'approve' to proceed with implementation, or let me know what adjustments are needed.
```

---

### Step 8: Implementation (Only After Explicit Approval)

Once the user explicitly approves:

1. **Create Working Branch:**
   - Ensure all changes are isolated
   - Document starting state

2. **Execute Phase by Phase:**
   - Make changes according to approved plan
   - Verify each phase before proceeding
   - Document any deviations

3. **Post-Implementation Verification:**
   - Confirm all persistent issues are resolved
   - Verify no regressions introduced
   - Update documentation if created

4. **Summary Report:**
   - List all changes made
   - Note any issues encountered
   - Provide testing recommendations

---

## Search Patterns Reference

Use these patterns during investigation:

### Color Detection
```
# XML colors
grep -rn "#[0-9A-Fa-f]\{6,8\}" --include="*.xml"
grep -rn "@color/" --include="*.xml"
grep -rn "?attr/color" --include="*.xml"

# Kotlin/Compose colors
grep -rn "Color(0x" --include="*.kt"
grep -rn "Color\." --include="*.kt"
grep -rn "colorResource" --include="*.kt"
grep -rn "MaterialTheme.colorScheme" --include="*.kt"

# Java colors
grep -rn "Color.parseColor" --include="*.java"
grep -rn "getColor(" --include="*.java"
grep -rn "ContextCompat.getColor" --include="*.java"
```

### Theme Detection
```
# Theme definitions
find . -name "themes.xml" -o -name "styles.xml"
grep -rn "Theme.Material" --include="*.xml"
grep -rn "@style/" --include="*.xml"

# Compose themes
find . -name "*Theme.kt" -o -name "*Colors.kt"
grep -rn "MaterialTheme" --include="*.kt"
grep -rn "isSystemInDarkTheme" --include="*.kt"
```

### Manifest Theme Usage
```
grep -n "android:theme" AndroidManifest.xml
grep -rn "setTheme(" --include="*.kt" --include="*.java"
```

---

## Guardrails & Quality Standards

### Investigation Principles
- **Be Exhaustive:** Don't miss any theme-related files
- **Follow the Chain:** Trace every color to its ultimate source
- **Document Everything:** Create clear audit trail
- **Question Assumptions:** Verify, don't assume, inheritance works as expected
- **Consider Qualifiers:** Always check for qualifier-specific overrides

### What NOT to Do
- Do not make "quick fixes" without understanding root cause
- Do not assume the most obvious definition is the active one
- Do not ignore legacy XML when app uses Compose (if hybrid)
- Do not skip dark mode / night qualifier analysis
- Do not implement changes without user approval

### Quality Thresholds for Resolution
- All persistent issues have identified root causes with evidence
- No hardcoded colors remain in UI code (moved to theme)
- Single source of truth for each semantic color
- XML and Compose themes synchronized (if hybrid)
- Documentation exists for theme architecture

---

## Techniques Used

- **ST-01** (Clear Objective): Explicit investigation and documentation objective
- **ST-02** (Structured Sequential Instructions): 8-phase process with clear progression
- **RT-01** (Chain-of-Thought): Step-by-step root cause analysis protocol
- **RT-02** (Multi-Dimensional Analysis): Multiple investigation dimensions (files, inheritance, usage)
- **RT-05** (Evidence-Based Reasoning): All findings require file paths, line numbers, specific values
- **DT-01** (Hierarchical Task Breakdown): Systematic search and categorization approach
- **DS-06** (Prioritization Guidance): Critical/High/Medium/Low classification
- **ST-03** (Output Format Templates): Comprehensive report structure with tables
- **NE-02** (Phased Workflow Architecture): Clear phase separation with handoffs
- **NE-07** (Discussion Before Action): Explicit requirement for approval before changes
- **AG-01** (Skeptical Default Stance): Verify rather than assume about theme behavior

---

## Related Prompts

- `android_compose_ui_analysis.md` - For comprehensive UI consistency assessment
- `android_compose_ui_polish.md` - For targeted UI refinement after theme fixes
- `android_kotlin_best_practices.md` - For code quality beyond theming
- `quality_code_style_consistency_analysis.md` - For broader code consistency review
- `android_kotlin_compose_debugging_audit.md` - For debugging Compose-specific issues

---

## Customization Guide

- **For Compose-only apps:** Skip XML theme sections, focus on Compose color scheme and typography
- **For XML-only apps:** Skip Compose sections, emphasize styles.xml and theme inheritance
- **For Material You / Dynamic Color issues:** Add section on `dynamicColor` configuration and overrides
- **For multi-module apps:** Expand investigation to trace theme definitions across module boundaries
- **For design system migration:** Add comparison section between old and new design tokens
- **For dark mode specific issues:** Emphasize qualifier analysis and `isSystemInDarkTheme` usage
