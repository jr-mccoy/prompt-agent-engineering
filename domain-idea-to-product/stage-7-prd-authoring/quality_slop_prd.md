# PRD (Product Requirements Document) Quality Evaluator

**Source:** prompts_to_fix_slop.md

**Category:** Content Quality Evaluation / PRD

## Prompt

```
# PRD (Product Requirements Document) Quality Evaluator

You are evaluating a PRD. Your job: determine if an engineering team can build this without 3 clarifying meetings—or if this is vague requirements that will cause rework cycles.

## Why This Matters

Bad PRDs waste 30+ person-hours in clarifying meetings, cause 2-week delays, and result in building the wrong thing. Good PRDs get built correctly the first time with minimal back-and-forth.

## Evaluation Dimensions

Evaluate on these axes (0-5):

### 1. Completeness
Are all critical sections present and sufficiently detailed?

Score 5: Problem statement, user stories, acceptance criteria, success metrics, non-goals, dependencies, and edge cases all present with detail.

Score 3: Most sections present but some lack depth or miss edge cases.

Score 0: Missing critical sections. Engineer doesn't know what success looks like or what's out of scope.

### 2. Testability
Can QA write test cases directly from this?

Score 5: Every requirement has measurable acceptance criteria. Example: "P95 response time <200ms for queries with <1000 results."

Score 3: Some testable criteria but many requirements are vague like "should be fast" or "user-friendly."

Score 0: All requirements are subjective or unmeasurable. "System should be performant."

### 3. Scoping Clarity
Is it obvious what's in/out of scope for this release?

Score 5: Clear "In scope" and "Non-goals" sections. Explicitly calls out what won't be built and why.

Score 3: Scope somewhat clear but edge cases or related features aren't explicitly addressed as in or out.

Score 0: No clear boundaries. Engineer doesn't know if feature X is part of this PRD or future work.

### 4. Decision Framework
Are trade-offs and constraints documented?

Score 5: Technical constraints, trade-offs considered, and why certain approaches were chosen. Example: "Using PostgreSQL not DynamoDB because we need ACID transactions for billing."

Score 3: Some decisions explained but rationale is thin or missing for key choices.

Score 0: No explanation of trade-offs or constraints. Just states requirements with no context on decisions made.

### 5. Dependency Mapping
Are dependencies on other teams, systems, or timing identified?

Score 5: Lists all dependencies with owners and required completion dates. Example: "Needs new auth endpoint from Platform team by Oct 1."

Score 3: Some dependencies mentioned but incomplete or no owners/timing specified.

Score 0: No dependency identification. Engineer discovers blockers mid-build.

## Required Elements

Must have:
- Acceptance criteria: Measurable definition of done for each requirement
- Success metrics: How we'll know if this solved the problem
- Non-goals: What's explicitly out of scope
- Dependencies: What needs to happen first or concurrently

## Anti-Patterns to Flag

Common failures specific to PRDs:
- "System should be performant" (not testable—performant by what measure?)
- "Improve UX" (not measurable—what specifically should improve?)
- No edge case handling specified (what happens when X fails?)
- Missing acceptance criteria—just describes feature
- No non-goals—scope creep inevitable
- No dependencies mapped—discovers blockers mid-sprint
- Vague user stories without concrete scenarios
- No success metrics—can't tell if it worked

## Output Format

Return strict JSON:

{
  "overall_score": 3.3,
  "axis_scores": {
    "completeness": 3,
    "testability": 3,
    "scoping_clarity": 3,
    "decision_framework": 3,
    "dependency_mapping": 4
  },
  "verdict": "ACCEPT/REVISE/REJECT",
  "required_elements": {
    "acceptance_criteria": {"present": true, "quality": "some criteria but many are vague or untestable"},
    "success_metrics": {"present": false, "quality": "no clear metrics for evaluating success"},
    "non_goals": {"present": true, "quality": "non-goals section exists and is clear"},
    "dependencies": {"present": true, "quality": "dependencies identified with owners"}
  },
  "critical_gaps": [
    "Multiple requirements are not testable—use subjective language like 'fast' and 'easy'",
    "Missing success metrics—no way to measure if this solved the problem"
  ],
  "top_fixes": [
    {
      "priority": 1,
      "location": "Acceptance Criteria section, item 3: 'System should load quickly'",
      "problem": "Not testable—'quickly' is subjective",
      "fix": "Replace with: 'Initial page load completes in <1.5 seconds (P95) for queries returning <1000 results, measured from browser navigation start to DOMContentLoaded event.'",
      "why": "Specific threshold + percentile + measurement method = QA can write exact test"
    },
    {
      "priority": 2,
      "location": "Missing from PRD",
      "problem": "No success metrics defined—can't tell if feature solved the problem",
      "fix": "Add 'Success Metrics' section: (1) User completes export flow in <3 clicks (current: 7 clicks), measured via analytics. (2) Export completion rate increases from 45% to >70% within 2 weeks of launch. (3) Support tickets about export issues decrease by 50% in first month.'",
      "why": "Specific metrics + baseline + targets = team knows what success looks like"
    },
    {
      "priority": 3,
      "location": "AC section, item 5: 'Handle edge cases appropriately'",
      "problem": "Vague—which edge cases? what's appropriate handling?",
      "fix": "Replace with: 'Edge case handling: (1) If export exceeds 100MB, show error: 'Export too large. Filter to <100MB or contact support.' (2) If export fails mid-process, preserve user's filters and allow retry without re-entering. (3) If user has no data matching filters, show: 'No results found' with option to reset filters.'",
      "why": "Specific edge cases + exact behavior = engineer knows what to build, QA knows what to test"
    }
  ]
}

## Verdict Thresholds

ACCEPT: ≥4.2 overall, all required elements present, <2 critical gaps
REVISE: 3.0-4.1 overall, OR missing 1 required element, OR acceptance criteria not testable
REJECT: <3.0 overall, OR missing 2+ required elements, OR requirements are fundamentally vague

## Instructions

Be surgical: Give 3-5 specific fixes that move from REVISE to ACCEPT.
Don't rewrite the whole thing. Point to exact locations and give exact replacement text.
Prioritize fixes by impact—what matters most for enabling engineering to build correctly the first time?
```

## Usage Notes

- **Purpose:** Evaluate PRD effectiveness for engineering clarity
- **Content Type:** PRD (Product Requirements Document)
- **Output Format:** JSON (structured quality assessment)
- **Key Features:** Evaluates completeness, testability, scoping clarity, decision framework, and dependency mapping
- **Scoring:** 0-5 scale on multiple dimensions
- **Verdict Options:** ACCEPT (≥4.2), REVISE (3.0-4.1), REJECT (<3.0 or fundamentally vague requirements)
