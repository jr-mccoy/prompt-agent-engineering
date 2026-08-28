# Task Sorting System Workflow Guide

**Purpose:** End-to-end guide for using the Task Sorting System prompts to design, review, and implement intelligent task prioritization algorithms.

**Target Audience:** Product managers, algorithm designers, Android/Kotlin developers, QA engineers, and AI agents working on task management applications.

---

## Overview

The Task Sorting System is a collection of three complementary prompts that support the full lifecycle of developing task prioritization algorithms:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        TASK SORTING SYSTEM WORKFLOW                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌──────────────┐     ┌──────────────┐     ┌──────────────────────────┐   │
│   │              │     │              │     │                          │   │
│   │   DESIGNER   │────▶│   REVIEWER   │────▶│  IMPLEMENTATION VERIFIER │   │
│   │              │     │              │     │                          │   │
│   └──────────────┘     └──────────────┘     └──────────────────────────┘   │
│         │                    │                         │                    │
│         ▼                    ▼                         ▼                    │
│   Algorithm Spec       Validated Design          Production Code           │
│   + 3 Approaches      + Improvement Plan        + Quality Assurance        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## When to Use Each Prompt

### Task Sorting Algorithm Designer
**File:** `task_sorting_algorithm_designer.md`

**Use When:**
- Starting a new task management feature from scratch
- Need to explore multiple algorithmic approaches
- Defining requirements for a prioritization system
- Creating an algorithm specification document

**Outputs:**
- Three distinct algorithmic approaches (weighted scoring, rule-based, context-aware)
- Comparative analysis matrix
- Recommended approach with justification
- Pseudocode for implementation
- Edge case documentation

**Typical Users:** Product managers, algorithm designers, senior developers

---

### Task Sorting Algorithm Reviewer
**File:** `task_sorting_algorithm_reviewer.md`

**Use When:**
- Auditing an existing prioritization algorithm
- Validating a proposed algorithm design before implementation
- Investigating user complaints about task sorting
- Preparing for scale or performance optimization
- Conducting pre-launch quality review

**Outputs:**
- Multi-perspective stress test results
- Edge case vulnerability assessment
- Bias and assumption audit
- Performance analysis
- Prioritized improvement roadmap
- Revised algorithm proposal

**Typical Users:** Algorithm designers, tech leads, QA engineers

---

### Task Sorting Kotlin Implementation Verifier
**File:** `task_sorting_kotlin_implementation_verifier.md`

**Use When:**
- Reviewing Kotlin/Android implementation of sorting algorithm
- Conducting code review for task prioritization features
- Debugging unexpected sorting behavior
- Preparing for production deployment
- Onboarding new team members to sorting codebase

**Outputs:**
- Algorithm correctness verification
- Kotlin best practices assessment
- Android integration review
- Performance benchmarks
- Test coverage analysis
- Code quality scorecard

**Typical Users:** Android developers, code reviewers, QA engineers

---

## Complete Workflow Scenarios

### Scenario 1: Building a New Task Sorting Feature

**Context:** Your team is building a family task management app and needs intelligent task prioritization.

**Workflow:**

```
Week 1-2: Design Phase
├── Step 1: Use Algorithm Designer
│   └── Input: App requirements, user personas, technical constraints
│   └── Output: Algorithm specification with 3 approaches
│
├── Step 2: Team reviews spec, selects approach
│
└── Step 3: Use Algorithm Reviewer on selected approach
    └── Input: Selected algorithm specification
    └── Output: Validated design + improvement recommendations

Week 3-4: Implementation Phase
├── Step 4: Developers implement in Kotlin
│
├── Step 5: Use Implementation Verifier for code review
│   └── Input: Kotlin source code + algorithm spec
│   └── Output: Code quality scorecard + issues list
│
└── Step 6: Fix issues, re-verify until passing

Week 5: Launch
└── Step 7: Deploy with confidence
```

---

### Scenario 2: Improving an Existing Algorithm

**Context:** Users complain that task sorting "doesn't make sense" - urgent tasks appear below less urgent ones.

**Workflow:**

```
Investigation Phase
├── Step 1: Use Algorithm Reviewer
│   └── Input: Current algorithm (code or spec)
│   └── Output: Root cause analysis + improvement roadmap
│
├── Step 2: Review edge case failures
│   └── Identify specific scenarios causing complaints
│
└── Step 3: Generate revised algorithm proposal

Improvement Phase
├── Step 4: Use Algorithm Designer (if major redesign needed)
│   └── Input: Lessons learned + new requirements
│   └── Output: New algorithm approaches
│
├── Step 5: Implement improvements in Kotlin
│
└── Step 6: Use Implementation Verifier
    └── Verify fixes + no regressions
```

---

### Scenario 3: Code Review for Sorting Feature

**Context:** A PR adds a new weighted scoring algorithm for task prioritization.

**Workflow:**

```
Code Review Process
├── Step 1: Standard code review (style, tests, etc.)
│
├── Step 2: Use Implementation Verifier
│   └── Input: PR diff + algorithm specification
│   └── Output: Detailed verification report
│
├── Step 3: Request changes based on findings
│
└── Step 4: Re-verify after fixes
```

---

## Integration with Development Lifecycle

### Agile/Scrum Integration

| Sprint Phase | Prompts to Use | Activity |
|--------------|----------------|----------|
| Backlog Refinement | Designer | Explore approaches for new sorting features |
| Sprint Planning | Reviewer | Validate complexity estimates against analysis |
| Development | Verifier | Code reviews and pair programming |
| QA | Reviewer + Verifier | Edge case testing, performance validation |
| Retrospective | Reviewer | Analyze production issues |

### CI/CD Integration

The prompts can inform automated checks:

```yaml
# Example: Checklist items from Verifier could become CI checks
quality_gates:
  - name: "Null Safety"
    check: "No force unwrapping (!!) without null checks"

  - name: "Performance"
    check: "Sorting 100 tasks completes under 16ms"

  - name: "Test Coverage"
    check: "All edge cases have explicit tests"
```

---

## Common Patterns

### Pattern 1: Iterative Refinement

```
Designer → Reviewer → Designer (refined) → Reviewer (final) → Implementation
```

Use when the problem space is complex or poorly understood. The first Designer pass explores options, Reviewer identifies gaps, second Designer pass addresses them.

### Pattern 2: Direct Implementation

```
Designer → Implementation → Verifier
```

Use when requirements are clear and team has experience with similar algorithms.

### Pattern 3: Rescue Mission

```
Verifier (existing code) → Reviewer → Designer (redesign) → Implementation
```

Use when inheriting problematic code or addressing critical bugs.

---

## Anti-Patterns to Avoid

### ❌ Skipping the Reviewer

**Problem:** Going directly from Designer to Implementation without validation.

**Consequence:** Edge cases and user perspective issues discovered late in development.

**Fix:** Always run the Reviewer on your algorithm design before coding.

---

### ❌ Using Verifier as Primary Design Tool

**Problem:** Trying to use the Implementation Verifier to design the algorithm.

**Consequence:** Focus on code details before algorithm is properly designed.

**Fix:** Use Designer first, then Reviewer, then Verifier.

---

### ❌ One-Time Use Only

**Problem:** Using prompts once at project start, never revisiting.

**Consequence:** Algorithm drifts from spec, issues accumulate.

**Fix:** Re-run Reviewer quarterly or when user feedback indicates problems.

---

### ❌ Ignoring Edge Case Warnings

**Problem:** Reviewer identifies edge cases but they're dismissed as "won't happen."

**Consequence:** Production incidents when edge cases occur.

**Fix:** Document each edge case disposition. If not fixing, explain why with evidence.

---

## Troubleshooting Guide

### Issue: Algorithm Designer produces approaches that don't fit our constraints

**Diagnosis:** Insufficient context provided in the initial prompt.

**Solution:** Provide more detail about:
- Technical constraints (performance requirements, platform limitations)
- User constraints (typical task volumes, user sophistication)
- Business constraints (timeline, resources)

---

### Issue: Reviewer stress tests seem unrealistic

**Diagnosis:** User personas may not match your actual user base.

**Solution:** Customize the three perspectives in the Reviewer prompt to match your actual user segments. The default personas (Overwhelmed Parent, Efficiency Optimizer, Reactive Juggler) are starting points.

---

### Issue: Implementation Verifier flags issues that we intentionally designed

**Diagnosis:** Verifier doesn't know about intentional design decisions.

**Solution:** Provide the algorithm specification document to the Verifier. It uses this to distinguish intentional behavior from bugs.

---

### Issue: Team disagrees on which approach to select from Designer output

**Diagnosis:** Normal! The Designer intentionally provides multiple approaches.

**Solution:**
1. Use the comparative analysis matrix as discussion framework
2. Run Reviewer on top 2 candidates to identify differentiating factors
3. Consider hybrid approach combining best elements

---

## Customization Guide

### For Different Platforms

The Implementation Verifier is Kotlin/Android-specific. For other platforms:

| Platform | Adaptation |
|----------|------------|
| iOS/Swift | Replace Kotlin sections with Swift idioms, UIKit/SwiftUI patterns |
| React Native | Replace with TypeScript/JavaScript patterns, React Native performance |
| Flutter | Replace with Dart patterns, Flutter state management |
| Web/TypeScript | Replace with TypeScript patterns, browser performance |

### For Different Domains

The prompts default to family/task management. For other domains:

| Domain | Key Adaptations |
|--------|-----------------|
| Enterprise Project Management | Add team dynamics, approval workflows, resource constraints |
| Health/Wellness Apps | Add habit tracking, motivation psychology, streak mechanics |
| CRM/Sales Tasks | Add deal stages, revenue impact, customer relationship factors |
| Gaming Quest Systems | Add progression mechanics, difficulty balancing, reward timing |

### For Different Team Sizes

| Team Size | Workflow Adaptation |
|-----------|---------------------|
| Solo Developer | Combine Designer+Reviewer in single session, use Verifier for self-review |
| Small Team (2-5) | Full workflow, rotate who runs each prompt |
| Large Team (10+) | Specialize: PM owns Designer, Tech Lead owns Reviewer, Devs own Verifier |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────┐
│                  TASK SORTING QUICK REFERENCE                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  DESIGNER (task_sorting_algorithm_designer.md)                  │
│  ├── When: New feature, exploring approaches                    │
│  ├── Input: Requirements, constraints, user context             │
│  └── Output: 3 approaches + recommendation + pseudocode         │
│                                                                  │
│  REVIEWER (task_sorting_algorithm_reviewer.md)                  │
│  ├── When: Validating design, investigating issues              │
│  ├── Input: Algorithm spec or existing implementation           │
│  └── Output: Stress test results + improvement roadmap          │
│                                                                  │
│  VERIFIER (task_sorting_kotlin_implementation_verifier.md)      │
│  ├── When: Code review, pre-launch QA                           │
│  ├── Input: Kotlin source code + algorithm spec                 │
│  └── Output: Quality scorecard + issue list + fixes             │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│  TYPICAL FLOW: Designer → Reviewer → Code → Verifier → Ship     │
└─────────────────────────────────────────────────────────────────┘
```

---

## Related Prompts

- `product-sprint-prioritizer.md` - Sprint-level task prioritization
- `strategy-feature-prioritization.md` - Feature prioritization for roadmaps
- `testing_unit_test_generation.md` - Generate tests for sorting logic
- `engineering_pre_code_planning_canvas.md` - Project planning before implementation
- `android_architecture_review.md` - Broader Android architecture review

---

## Changelog

### 2025-12-17
- Initial workflow guide created
- Documented all three prompts and their relationships
- Added workflow scenarios, patterns, and anti-patterns
- Created troubleshooting and customization guides

---

*Part of the Task Sorting System. See `docs/SORTING_SYSTEM_OVERHAUL.md` for full roadmap.*
