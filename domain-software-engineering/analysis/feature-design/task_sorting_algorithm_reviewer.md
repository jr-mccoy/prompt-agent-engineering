---
title: "Task Sorting Algorithm Reviewer"
category: software-engineering/analysis/feature-design
description: "Critically evaluate an existing task-sorting/prioritization algorithm through multi-persona stress testing, adversarial edge cases, bias auditing, and a prioritized, evidence-based improvement roadmap."
techniques:
  - ST-01
  - RT-02
  - QA-02
  - DS-06
  - QA-01
difficulty: advanced
tags:
  - algorithm-review
  - code-review
  - task-prioritization
  - stress-testing
  - edge-cases
updated: "2026-06-07"
related_prompts:
  - domain-software-engineering/analysis/feature-design/task_sorting_algorithm_designer.md
  - domain-software-engineering/analysis/feature-design/task_sorting_kotlin_implementation_verifier.md
  - domain-engineering-workflows/workflows/engineering_post_mortem_root_cause_ladder.md
---

# Task Sorting Algorithm Reviewer

**Objective:** Critically evaluate and improve an existing task-sorting/prioritization algorithm through multi-persona analysis, adversarial edge-case stress testing, a bias/assumption audit, and a prioritized, evidence-based improvement roadmap.

**When to use:**
- Validating a task-prioritization algorithm before scaling to production.
- Auditing an algorithm users are "fighting" or that produces surprising orders.
- Reviewing a design produced by `task_sorting_algorithm_designer.md`.
- Diagnosing edge-case failures (overload, empty attributes, conflicts).

**When NOT to use:**
- Designing a new algorithm from scratch — use `task_sorting_algorithm_designer.md`.
- Verifying a Kotlin implementation's code correctness — use `task_sorting_kotlin_implementation_verifier.md`.

**Audience:** Engineers, product managers, and reviewers auditing a task-prioritization algorithm.

---

## Inputs / Context

The user supplies:
1. **The algorithm specification** — name, purpose, inputs (task attributes, context, settings), logic (pseudocode/flowchart), output. Wrap any pasted pseudocode or code in a `<algorithm>` tag.
2. **Implementation status** — design / prototype / production; platform; any performance data.
3. **Known problems** (optional) — complaints, support tickets, observed failures.
4. **Target user profiles** — who the algorithm serves.

If the spec has gaps, list them and flag the affected analysis as provisional rather than guessing.

---

## Constraints

### Must
- Stress-test from at least three distinct user perspectives with conflicting needs.
- Run adversarial edge cases (overload, empty attributes, impossible schedules, conflicts, overdue avalanche, far-future tasks).
- For every finding: severity, likelihood, impact, and a specific proposed fix.
- Audit implicit assumptions and biases (lifestyle, cognitive/neurodivergent, technical).
- Deliver a prioritized improvement roadmap (Critical → Future).

### Must Not
- Invent benchmark numbers, complexity figures, or user-satisfaction metrics not derivable from the spec — derive complexity from the logic and label estimates.
- Assign blame to "user error" without asking why the algorithm permits the bad outcome.
- Recommend changes without stating regression risk.
- Treat a missing spec detail as a confirmed defect — flag it as a gap.

---

## Instructions

### 1. Algorithm Documentation Review

First, gather and analyze the complete algorithm specification:

**Required Documentation:**
```
Algorithm Name: [Name of algorithm]

Purpose: [What problem does it solve?]

Input Parameters:
- Task attributes used: [list]
- Context variables used: [list]
- User preferences/settings: [list]

Algorithm Logic:
[Pseudocode, flowchart, or detailed description]

Output:
- What is returned (sorted list, scores, rankings, etc.)
- Output format and structure

Current Implementation Status:
- Production/Prototype/Design phase
- Language/Platform: [e.g., Kotlin/Android]
- Performance data: [if available]
```

**Missing Documentation Assessment:**
- Identify gaps in specification
- Flag ambiguous logic
- Note undocumented assumptions
- Request clarification where needed

### 2. Multi-Perspective Stress Testing

Evaluate the algorithm from three distinct user perspectives, each with conflicting priorities:

#### **Perspective 1: The Overwhelmed Parent**
**Profile:**
- 30-50 tasks on list at any time
- Marks 80%+ tasks as "high priority" out of anxiety
- Chronic procrastinator, defers tasks frequently
- Struggles with time estimation (usually underestimates)
- Needs anxiety reduction and realistic daily plans

**Analysis:**
- How does the algorithm handle this user's behavior?
- Does it adapt to reduce overwhelm or exacerbate it?
- Can it identify and correct unrealistic priority inflation?
- Does it provide motivating, achievable daily lists?
- What breaks or frustrates this user?

#### **Perspective 2: The Efficiency Optimizer**
- Small, curated task list (5-15 active tasks)
- Precise about priorities, durations, and contexts
- High completion rate, rarely procrastinates
- Wants maximum productivity optimization
- Values time-blocking and batching opportunities

**Analysis:**
- Does the algorithm leverage detailed input effectively?
- Can it identify efficiency opportunities (batching, routing)?
- Does it respect user's explicit prioritization?
- Are advanced features utilized well?
- What power-user capabilities are missing?

#### **Perspective 3: The Reactive Juggler**
- Mix of urgent and long-term tasks
- Priorities shift constantly due to external factors
- Often interrupted, needs quick context-switching
- Balances work, family, personal demands
- Values flexibility and quick re-planning

**Analysis:**
- How does algorithm handle dynamic reprioritization?
- Can it adapt to context changes quickly?
- Does it support interruption recovery?
- Can user easily override or adjust on-the-fly?
- What happens when external events force changes?

**Comparative Synthesis:**
After analyzing all three perspectives:
- Which user type is best served? Why?
- Which user type struggles most? Why?
- Are trade-offs acceptable or problematic?
- How could algorithm adapt to different user profiles?
- Should there be user-selectable modes or automatic adaptation?

### 3. Adversarial Edge Case Analysis

Systematically stress-test the algorithm with scenarios designed to expose weaknesses:

**Overload Scenarios:**

*Test Case 1: Priority Inflation*
```
Input: 50 tasks, 45 marked "high priority", all due within 3 days
Expected Failure: Cannot meaningfully differentiate
Actual Behavior: [How does algorithm respond?]
Severity: [Critical/High/Medium/Low]
Impact: [User sees unhelpful sorted list]
Proposed Fix: [Specific improvement]
```

*Test Case 2: The Empty Attributes*
```
Input: 20 tasks with minimal info (no due dates, no durations, no priorities set)
Expected Failure: Insufficient data for sorting
Actual Behavior: [How does algorithm respond?]
Severity: [Critical/High/Medium/Low]
Impact: [User sees random or alpha-sorted list]
Proposed Fix: [Specific improvement]
```

*Test Case 3: Impossible Schedule*
```
Input: 15 hours of tasks all due today, user has 4 hours available
Expected Failure: Cannot fit everything, must triage
Actual Behavior: [How does algorithm respond?]
Severity: [Critical/High/Medium/Low]
Impact: [User misses deadlines, loses trust]
Proposed Fix: [Specific improvement]
```

**Conflicting Priorities:**

*Test Case 4: Urgency vs. Importance Matrix Extremes*
```
Input:
- Task A: Very important, not urgent (retirement planning)
- Task B: Not important, very urgent (spam email response)
Expected Challenge: Which ranks higher?
Actual Behavior: [How does algorithm resolve?]
Correctness: [Is this the right prioritization?]
Proposed Fix: [If needed]
```

*Test Case 5: Multi-Person Dependencies*
```
Input: Task requires both parents available, conflicting work schedules
Expected Challenge: Cannot schedule in isolation
Actual Behavior: [How does algorithm handle?]
Proposed Fix: [Specific improvement]
```

**Temporal Edge Cases:**

*Test Case 6: Overdue Avalanche*
```
Input: 30 tasks, all overdue by 1-7 days
Expected Challenge: All equally "past due," need intelligent triage
Actual Behavior: [How does algorithm sort?]
Proposed Fix: [Specific improvement]
```

*Test Case 7: Far Future Tasks*
```
Input: Tasks due in 6 months+ mixed with daily tasks
Expected Challenge: Long-term tasks never surface
Actual Behavior: [How does algorithm balance?]
Proposed Fix: [Specific improvement]
```

**For Each Test Case, Document:**
- **Severity Rating:** How badly does this break user experience?
  - Critical: Algorithm fails, produces wrong output, or crashes
  - High: Produces suboptimal output that frustrates users
  - Medium: Minor usability issue or edge case
  - Low: Theoretical issue unlikely to occur

- **Likelihood:** How often will users encounter this?
  - High: Common user behavior or data state
  - Medium: Occasional but realistic scenario
  - Low: Rare edge case

- **Impact Assessment:** What is the consequence?
  - User frustration level
  - Loss of trust in algorithm
  - Task completion degradation
  - Potential data loss or errors

- **Proposed Solution:** Specific, actionable fix
  - Code-level changes needed
  - Algorithm logic adjustments
  - Fallback strategies
  - User-facing mitigations

### 4. Bias and Assumption Audit

Identify implicit biases and assumptions in the algorithm:

**Cultural and Lifestyle Assumptions:**
- Does algorithm assume 9-5 work schedule?
- Does it assume nuclear family structure?
- Does it favor individual vs. collaborative tasks?
- Does it assume smartphone/computer access?
- Does it assume consistent daily routines?

**Cognitive and Neurological Assumptions:**
- Does it assume users have good time estimation skills?
- Does it assume users can handle cognitive load of complex sorting?
- Does it assume users understand priority concepts consistently?
- Does it account for ADHD, executive function challenges?
- Does it consider anxiety or decision paralysis?

**Technical Assumptions:**
- Does it assume reliable connectivity?
- Does it assume accurate device time/location?
- Does it assume users will input complete data?
- Does it assume consistent user engagement?

**Value Judgments:**
- What does algorithm implicitly value? (productivity, balance, perfection, speed)
- Are those values aligned with stated user goals?
- Do value hierarchies match diverse user needs?

**For Each Assumption/Bias:**
- Is it necessary or avoidable?
- What users are excluded or disadvantaged?
- How could algorithm be more inclusive?
- What configuration or adaptation is needed?

### 5. Performance and Scalability Analysis

**Computational Performance:**

Analyze algorithm complexity:
```
Time Complexity: O(?)
- Best case: [scenario and complexity]
- Average case: [scenario and complexity]
- Worst case: [scenario and complexity]

Space Complexity: O(?)

Benchmarking:
- Time to sort 10 tasks: [estimate/measurement]
- Time to sort 100 tasks: [estimate/measurement]
- Time to sort 1000 tasks: [estimate/measurement]
- Mobile device performance: [considerations]
```

**Performance Issues Identified:**
- Bottlenecks: [specific computational steps]
- Redundant operations: [inefficiencies]
- Optimization opportunities: [specific improvements]

**Scalability Concerns:**
- At what task count does performance degrade?
- What happens with thousands of historical tasks?
- How does algorithm scale with users (multi-user lists)?
- Database query efficiency for data retrieval

**Recommendations:**
- Caching strategies
- Incremental sorting
- Background processing
- Pagination or windowing
- Algorithm optimizations

### 6. User Experience and Transparency Evaluation

**Explainability:**
- Can users understand WHY tasks are sorted as they are?
- Is there "show your work" capability for the algorithm?
- Can users see what factors influenced each task's position?

**Predictability:**
- Do small input changes cause large output changes?
- Is sort order stable for similar tasks?
- Can users predict how changes will affect sorting?

**User Control:**
- Can users override algorithm decisions?
- Can users adjust weights or preferences?
- Is there a "manual mode" fallback?
- Can users provide feedback on sort quality?

**Friction Points:**
- Does algorithm require too much data input?
- Are surprises in sort order frustrating?
- Do users fight the algorithm frequently?
- Does it create decision fatigue?

**Recommendations:**
Rate user experience on 1-5 scale:
- Transparency: [rating + explanation]
- Predictability: [rating + explanation]
- User Control: [rating + explanation]
- Friction: [rating + explanation]

**Improvement Suggestions:**
[Specific UX enhancements]

### 7. Comparative Benchmarking

Compare this algorithm against standard approaches:

**Baseline 1: Simple Due Date Sort**
- Sort by due date ascending, then priority
- How does reviewed algorithm compare?
- What value does additional complexity provide?

**Baseline 2: User Priority Only**
- Trust user's explicit priority setting
- How does reviewed algorithm compare?
- Does algorithmic override add or remove value?

**Baseline 3: Popular App Approaches**
- How does Todoist/Things/TickTick handle similar scenarios?
- What can be learned from established solutions?
- Where does this algorithm innovate?

**Value Justification:**
- Is added complexity justified by improved outcomes?
- What measurable improvements does it provide?
- How to validate effectiveness?

### 8. Comprehensive Findings Report

Synthesize all analysis into actionable report:

**Executive Summary:**
- Overall Algorithm Quality: [Excellent/Good/Fair/Poor]
- Primary Strengths: [3-5 bullet points]
- Critical Weaknesses: [3-5 bullet points]
- Recommendation: [Ship/Iterate/Redesign]

**Detailed Findings by Category:**

**1. Logic Correctness**
- Status: [Correct/Has Issues]
- Issues Found: [list with severity]
- Edge Cases Handled: [X/Y documented cases pass]

**2. User Experience**
- Multi-Perspective Assessment: [summary from Section 2]
- Best Served Users: [profile]
- Underserved Users: [profile]
- UX Rating: [X/5]

**3. Robustness**
- Edge Case Pass Rate: [X/Y test cases pass]
- Critical Failures: [count and list]
- High-Severity Issues: [count and list]
- Fail-Safe Mechanisms: [present/missing]

**4. Performance**
- Computational Efficiency: [rating]
- Scalability: [rating]
- Bottlenecks: [identified issues]

**5. Bias and Inclusivity**
- Assumptions Audit: [X assumptions identified]
- Excluded User Groups: [list]
- Inclusivity Rating: [X/5]

**6. Transparency and Control**
- Explainability: [X/5]
- User Override Capability: [X/5]
- Predictability: [X/5]

### 9. Prioritized Improvement Roadmap

**Critical Fixes (Must Address Before Launch):**

Priority 1: [Issue Name]
- Severity: Critical
- Impact: [specific user impact]
- Current Behavior: [what happens now]
- Proposed Fix: [detailed solution]
- Implementation Effort: [hours/days]
- Testing Requirements: [how to validate]

Priority 2: [Issue Name]
[Same format]

**High-Priority Improvements (This Quarter):**

[List 3-5 most important improvements with same format as above]

**Medium-Priority Enhancements (Next Quarter):**

[List 5-8 valuable improvements with briefer descriptions]

**Future Considerations (Backlog):**

[List nice-to-have features or long-term improvements]

### 10. Revised Algorithm Proposal

Based on all findings, provide improved algorithm specification:

**Algorithm Name:** [Original or New Name v2.0]

**Key Changes from Original:**
1. [Change description with rationale]
2. [Change description with rationale]
3. [Change description with rationale]

**Improved Logic:**
```
[Pseudocode or detailed description of revised algorithm]
[Highlight what changed and why]
```

**Edge Case Handling:**
[Document how each identified edge case is now handled]

**Fallback Strategies:**
[When algorithm cannot make confident decision, what happens?]

**Configuration Options:**
[User-tunable parameters to adapt to different profiles]

### 11. Validation and Testing Plan

**Test Cases for Validation:**

Create comprehensive test suite covering:
- All identified edge cases
- All three user perspectives
- Performance benchmarks
- Regression tests for previous issues

**Success Metrics:**

Define measurable criteria:
- Task completion rate increase: [target %]
- User satisfaction score: [target rating]
- Sort quality rating: [target %]
- Edge case pass rate: [target %]
- Performance benchmarks: [target ms]

**A/B Testing Recommendation:**

If applicable, design experiment:
- Control: [current algorithm or baseline]
- Treatment: [improved algorithm]
- Sample size: [users needed]
- Duration: [days/weeks]
- Metrics to track: [list]
- Success criteria: [statistical significance threshold]

**User Feedback Collection:**

- In-app surveys: [specific questions]
- Usage analytics: [events to track]
- Qualitative interviews: [discussion guide]
- Iteration cadence: [how often to review and improve]

## Expected Output

Your comprehensive algorithm review should include:

1. **Executive Summary (1 page)**
   - Overall quality assessment
   - Ship/iterate/redesign recommendation
   - Top 3 strengths and top 3 weaknesses
   - Key metrics if available

2. **Multi-Perspective Analysis**
   - Three detailed user perspective evaluations
   - Comparative synthesis
   - User profile fit assessment

3. **Edge Case Test Results**
   - 10-15 documented test cases
   - Pass/fail for each
   - Severity and likelihood ratings
   - Proposed fixes for failures

4. **Bias and Assumption Audit**
   - Identified assumptions with implications
   - Inclusivity assessment
   - Mitigation recommendations

5. **Performance Analysis**
   - Complexity analysis
   - Benchmarking results
   - Optimization recommendations

6. **UX Evaluation**
   - Transparency, predictability, control ratings
   - Friction point identification
   - Enhancement suggestions

7. **Prioritized Improvement Roadmap**
   - Critical fixes (detailed)
   - High-priority improvements
   - Medium-priority enhancements
   - Future considerations

8. **Revised Algorithm Specification**
   - Complete improved algorithm
   - Change documentation
   - Edge case handling

9. **Validation Plan**
   - Test cases
   - Success metrics
   - A/B testing design
   - Feedback collection approach

## Quality Checklist

Before finalizing your review, verify:

- [ ] All three user perspectives analyzed with equal rigor
- [ ] At least 10 adversarial edge cases tested
- [ ] Each finding includes severity + likelihood + impact
- [ ] Every identified issue has a proposed solution
- [ ] Performance analysis includes concrete complexity metrics
- [ ] Bias audit considers diverse user populations
- [ ] UX evaluation covers explainability and control
- [ ] Recommendations are prioritized and actionable
- [ ] Revised algorithm addresses critical findings
- [ ] Validation plan includes measurable success criteria

## Advanced Analysis Techniques

### Chain-of-Verification
For each major claim or finding:
1. State the finding clearly
2. List evidence supporting it
3. Identify potential counter-evidence
4. Verify conclusion is warranted

### Comparative Stress Testing
Run same edge case through:
- Current algorithm
- Baseline simple algorithm
- Revised algorithm
Compare outcomes to validate improvement

### Regression Risk Assessment
For each proposed change:
- What could break?
- What existing functionality might degrade?
- What testing is needed to prevent regression?

## False-Positive Prevention

❌ **DON'T:**
- Don't report benchmark times or satisfaction scores you didn't measure — derive complexity from the logic and label any runtime as an estimate.
- Don't conclude an algorithm "fails" on a scenario when the spec is simply silent — flag it as an undocumented case.
- Don't blame "the user marks everything urgent" without asking why the algorithm can't de-conflict inflated priorities.
- Don't recommend a fix without naming its regression risk.

✅ **DO:**
- Quote the spec/logic line your finding rests on; flag spec gaps as gaps.
- Give every finding severity + likelihood + impact + a concrete fix.
- Run each edge case against current vs. proposed behavior to validate improvement.
- State what could break for each proposed change.

---

## Verification

- [ ] At least three user perspectives analyzed with equal rigor.
- [ ] At least 10 adversarial edge cases documented with severity/likelihood/impact.
- [ ] Every finding has a specific proposed fix.
- [ ] Assumption/bias audit covers lifestyle, cognitive/neurodivergent, and technical assumptions.
- [ ] Complexity derived from logic; no fabricated benchmark or satisfaction numbers.
- [ ] Roadmap is prioritized (Critical → Future) and each change states regression risk.
- [ ] Spec gaps flagged as gaps, not asserted as defects.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the evidence-based evaluation and improvement goal.
- **RT-02 (Multi-Dimensional Analysis):** Reviews correctness, UX, robustness, performance, bias, and transparency.
- **QA-02 (Adversarial Self-Critique):** Multi-persona and adversarial edge-case stress testing surface failures.
- **DS-06 (Prioritization and Severity Guidance):** Severity/likelihood ranking drives the improvement roadmap.
- **QA-01 (Self-Verification):** Chain-of-verification check blocks fabricated metrics and unsupported claims.

---

## Related Prompts

- `domain-software-engineering/analysis/feature-design/task_sorting_algorithm_designer.md` — Design a new or revised algorithm.
- `domain-software-engineering/analysis/feature-design/task_sorting_kotlin_implementation_verifier.md` — Verify the implementation of the revised design.
- `domain-engineering-workflows/workflows/engineering_post_mortem_root_cause_ladder.md` — Analyze incidents if the algorithm fails in production.

## Customization Guide

**For Production Algorithms:**
- Add performance profiling data
- Include real user metrics if available
- Emphasize A/B testing and validation
- Focus on regression prevention

**For Prototype Algorithms:**
- Focus on logic correctness and edge cases
- Emphasize user perspective analysis
- Lighter on performance optimization
- More exploratory in recommendations

**For Established Apps:**
- Include competitive analysis vs. similar apps
- Reference user feedback and support tickets
- Consider migration path from existing algorithm
- Assess backward compatibility

**For Research/Academic:**
- Add theoretical analysis and proofs
- Include literature review of sorting algorithms
- Emphasize novelty and contribution
- Provide formal complexity analysis
