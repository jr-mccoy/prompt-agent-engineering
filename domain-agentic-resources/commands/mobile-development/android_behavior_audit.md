---
name: android_behavior_audit
description: Orchestrate comprehensive Android app behavior audit across survey, deep code tracing, behavioral scrutiny, developer clarification, and fix planning to align actual code behavior with developer intent
version: "1.0.0"
category: mobile-development
tags: [android, audit, behavior, kotlin, compose, firebase, room, intent-alignment, pre-release]
agents_used: [android-app-surveyor, android-behavior-tracer, android-behavior-auditor, android-behavior-fix-planner]
---

Orchestrate a complete Android app behavior audit, coordinating 4 specialized agents across 5 phases to identify and resolve behavioral discrepancies between what the code actually does and what the developer intends:

[Extended thinking: This workflow audits an Android app's actual behavior against developer intent. It is fundamentally different from code review (quality), security audit (vulnerabilities), or architecture review (structure). The key insight is that many pre-production issues are not crashes or security holes — they are subtle behavioral discrepancies where the code does something slightly different from what the developer intended. These issues are nearly invisible to traditional reviews because the code "works" — it just doesn't work correctly.

The workflow uses 4 specialized agents, each optimized for a distinct cognitive mode:
- Surveyor (Sonnet): Breadth-first discovery — fast, structured, comprehensive
- Tracer (Opus): Depth-first analysis — exhaustive code path following
- Auditor (Opus): Critical reasoning — "does this make sense?" evaluation
- Fix Planner (Opus): Surgical implementation — minimal-change fixes with verification

Three user interaction gates ensure the developer stays in control:
1. After survey: Developer selects which areas to audit
2. After audit: Developer clarifies intended behavior for findings
3. After planning: Developer approves fix plan before implementation

The workflow is designed for solo developers preparing apps for Google Play closed/open testing, where behavioral correctness is critical for passing review and maintaining user trust.]

## Configuration

### Supported Flags
- `--scope=all|<feature-name>`: Pre-select scope (skip Phase 1 user interaction)
- `--depth=shallow|deep`: Shallow traces enumerate behaviors only; deep traces include all edge cases (default: deep)
- `--skip-implementation`: Stop after Phase 4 (planning only, do not implement fixes)
- `--focus=bugs|suspicious|all`: Filter scrutiny output to specific finding categories (default: all)

### Parameters
- `$ARGUMENTS`: Path to the Android project root directory

## Phase 1: Survey & Selection

### 1. Codebase Survey
- Use Task tool with subagent_type="android-app-surveyor"
- Prompt: "Survey the Android application at $ARGUMENTS to produce a comprehensive feature map. Load the android-app-survey skill for methodology and templates.

  Perform a 3-pass scan:
  1) Structural scan: Read build.gradle.kts for dependencies and SDK versions, read AndroidManifest.xml for declared components and permissions, identify module structure
  2) Screen & navigation scan: Find all NavHost destinations (Compose) or navigation graph destinations (XML), map navigation structure (bottom nav, drawer, tabs), identify entry points and deep links
  3) Feature & subsystem inventory: Group screens into user-facing feature areas (Auth, Settings, Content, Sync, etc.), identify technical subsystems (Room, Firebase, WorkManager, etc.)

  Use the feature map template from the android-app-survey skill to present results. Include: Tech Stack summary, Screens & Navigation table, Feature Areas with descriptions, Technical Subsystems inventory, and Complexity Indicators.

  End by listing all feature areas as numbered options and asking the developer which areas they want audited in depth."
- Expected output: Categorized feature map with numbered feature areas for developer selection
- Context: This is the first phase — no prior context exists

### USER INTERACTION GATE 1
Present the feature map to the developer and ask:

"Which feature areas would you like to audit? You can select one or more areas by number, or type 'all' to audit everything. I recommend starting with 1-2 areas for a focused audit, then expanding if needed."

**STOP and wait for developer response. Do not proceed to Phase 2 until the developer has specified their selection.**

## Phase 2: Deep Analysis & Behavior Cataloging

### 2. Deep Behavior Tracing
- Use Task tool with subagent_type="android-behavior-tracer"
- Prompt: "Trace all code behavior for the following feature area(s) in the Android application at $ARGUMENTS: [SELECTED AREAS FROM GATE 1]. Load the android-behavior-trace skill for methodology and templates.

  For each feature area, trace every user action through all architectural layers:
  - UI Layer: Click handlers, state observation, navigation triggers, loading/error/empty states
  - ViewModel Layer: State management, coroutine execution, business logic, error mapping
  - Repository Layer: Data source coordination, caching strategy, offline behavior
  - Data Layer: Room queries (exact SQL, conflict strategies, transactions), Firebase operations (read/write paths, listener lifecycle), API calls (request/response, retry logic)
  - Background Layer: WorkManager tasks (constraints, retry, chain dependencies), services, receivers

  For EACH behavior traced, also trace the error path (what happens on failure at each layer) and check edge cases: configuration change, process death, no network, concurrent access.

  Produce a behavior catalog using the cataloging template from the android-behavior-trace skill:
  | # | User Action | Code Behavior | Code Location | Edge Cases |

  Every entry must be factual (what the code does, not what it should do), referenced (file:line locations), and complete (include error and edge case paths).

  Reference existing targeted review prompts for subsystem-specific guidance where relevant (ViewModel state management, Compose recomposition, Room queries, process death recovery, coroutine scopes, sync architecture, offline conflicts, WorkManager, data integrity, Hilt DI scopes, Room migrations)."
- Expected output: Complete behavior catalog with file:line references for all traced behaviors
- Context from previous: Feature areas selected by developer in Gate 1, feature map from Phase 1

## Phase 3: Behavioral Scrutiny & Findings

### 3. Behavioral Scrutiny
- Use Task tool with subagent_type="android-behavior-auditor"
- Prompt: "Scrutinize the behavior catalog for the Android application at $ARGUMENTS to identify behavioral discrepancies. Load the android-behavior-audit skill for scrutiny checklists, classification guide, and calibration examples.

  For each behavior in the catalog, evaluate:
  - Does this behavior make sense for the user?
  - Does this behavior match what a reasonable developer would intend?
  - Are error paths handled in a way that keeps the user informed?
  - Are edge cases handled appropriately?

  Apply the scrutiny checklists from the skill, organized by Android subsystem:
  - Compose UI: recomposition side effects, state loss, loading/error/empty completeness, back button behavior
  - ViewModel state: unreachable states, missing transitions, process death restoration, concurrent updates
  - Room database: silent write failures, orphaned records, migration data loss, transaction completeness
  - Firebase: conflict resolution, offline queue, partial sync, auth token expiry, listener leaks
  - Navigation: dead ends, back stack consistency, deep link handling, auth gates
  - Error handling: swallowed exceptions, generic messages, retry mechanisms, crash prevention vs correctness
  - Background work: constraints, interrupted handling, result delivery, periodic overlap

  Check against known anti-patterns from the android_behavior_patterns.md reference.

  Classify each finding into exactly one category:
  - Likely Bug (>80% confidence): Almost certainly unintended behavior
  - Suspicious Pattern (40-80%): Could be intentional but looks wrong
  - Design Question (<40%): Works but intent is ambiguous
  - Confirmed Correct: Reviewed and appears sound

  Use the calibration examples from finding_examples.md to ensure consistent classification.

  Present findings using the audit findings template:
  - Summary with counts per category
  - Likely Bugs: behavior, reasoning, user impact, code location, user scenario
  - Suspicious Patterns: behavior, reasoning, possible intent, code location, question for developer
  - Design Questions: behavior, ambiguity, options, code location, question for developer
  - Confirmed Correct: brief list with rationale

  Order findings within each category by user impact (highest impact first)."
- Expected output: Classified findings with confidence levels, user scenarios, and developer questions
- Context from previous: Behavior catalog from Phase 2

### USER INTERACTION GATE 2
Present all findings to the developer and ask:

"Please review each finding and let me know:

**For Likely Bugs:** Are these confirmed bugs? If any are actually intentional, let me know.

**For Suspicious Patterns:** For each one, is this:
- A confirmed bug that needs fixing
- Intentional behavior (I'll close the finding)
- Something you're not sure about (I can investigate further)

**For Design Questions:** Please indicate your intended behavior for each question.

Take your time — this is the most important step for ensuring the fixes are correct."

**STOP and wait for developer response. Do not proceed to Phase 4 until the developer has reviewed all findings and provided clarifications.**

## Phase 4: Clarification & Fix Planning

### 4. Fix Planning
- Use Task tool with subagent_type="android-behavior-fix-planner"
- Prompt: "Plan fixes for the confirmed behavioral issues in the Android application at $ARGUMENTS based on the developer's clarifications. Load the android-behavior-fix-planning skill for methodology, blast radius estimation, and fix patterns.

  Step 1: Integrate developer clarifications
  - Confirmed bugs → move to fix list with intended behavior
  - Intentional behavior → close finding, document intent
  - Deferred items → move to backlog
  - Unclear items → flag for follow-up

  Step 2: For each confirmed fix, plan the change:
  - Define the specific code change needed (which files, which functions, what changes)
  - Estimate blast radius: Contained (single function), Local (1-3 files), Cross-cutting (multiple features), Architectural (fundamental change)
  - Estimate complexity: Trivial (<15 min), Simple (15-60 min), Moderate (1-3 hr), Complex (3-8 hr)
  - Apply fix patterns from fix_pattern_library.md where applicable

  Step 3: Order fixes by dependency:
  - Build dependency graph (which fixes depend on others)
  - Apply ordering: dependencies first → data integrity → lowest blast radius → highest confidence
  - Identify fixes that can be applied independently

  Present the fix plan using the template:
  | Order | Fix ID | Title | Blast Radius | Complexity | Dependencies |

  Include risk assessment (low/medium/high risk groups) and total estimated effort.

  Reference existing skills for implementation patterns: android-room-database, android-hilt-di, android-testing-patterns."
- Expected output: Ordered fix plan with blast radius, complexity, dependencies, and risk assessment
- Context from previous: Audit findings from Phase 3, developer clarifications from Gate 2

### USER INTERACTION GATE 3
Present the fix plan to the developer and ask:

"Here is the proposed fix plan. Please review and let me know:

1. **Which fixes to implement now?** (You can approve all, or select specific ones)
2. **Is the implementation order acceptable?** (I've ordered by dependency and risk — lowest risk first)
3. **Any fixes you want to defer?** (They'll stay on the backlog for a future audit)

I'll implement each approved fix one at a time, verify it, then move to the next."

**STOP and wait for developer response. Do not proceed to Phase 5 until the developer has approved the fix plan.**

## Phase 5: Implementation & Verification

### 5. Fix Implementation
- Use Task tool with subagent_type="android-behavior-fix-planner"
- Prompt: "Implement the approved fixes for the Android application at $ARGUMENTS in the approved order. Load the android-behavior-fix-planning skill for implementation protocol and verification methodology.

  For EACH fix (one at a time):

  Before coding:
  1. Re-read the current code at the fix location
  2. Verify the behavior catalog entry is still accurate
  3. Understand the full calling context

  During coding:
  4. Make the MINIMAL change that resolves the finding
  5. Do NOT refactor surrounding code
  6. Do NOT fix other issues you notice (log them for future audit)
  7. Preserve existing behavior for all non-affected code paths

  After coding:
  8. Run existing tests if available (./gradlew test, ./gradlew connectedAndroidTest)
  9. Add or update tests for the fixed behavior where practical
  10. Verify the fix against the specific user scenario from the finding

  Report status after each fix:
  - What was changed (files, functions, lines)
  - How it was verified
  - Any new observations or concerns

  After ALL fixes are applied, provide a complete fix verification report using the template from the skill."
- Expected output: Fix verification report with applied fixes, regression check status, and any new issues
- Context from previous: Approved fix plan from Gate 3, all prior phase context
- GATE: If any fix introduces test failures, STOP and report to the developer before continuing

### 6. Re-Audit Verification (Optional)
- Use Task tool with subagent_type="android-behavior-auditor"
- Prompt: "Re-audit the modified code areas in the Android application at $ARGUMENTS to verify fixes resolved the identified issues. Load the android-behavior-audit skill.

  Focus on:
  1. Each fix location — confirm the specific finding is resolved
  2. Adjacent code — check if fixes introduced any new behavioral issues
  3. Previously 'Confirmed Correct' behaviors — verify they are still correct

  Report any new findings using the same classification system."
- Expected output: Verification audit confirming fixes or identifying new issues
- Context from previous: Fix verification report from Step 5, original audit findings from Phase 3

## Success Criteria

### Behavioral Criteria
- ✅ All selected feature areas have been surveyed and traced
- ✅ Every behavior in the catalog has been scrutinized
- ✅ All findings have been classified with confidence levels
- ✅ Developer has reviewed and clarified all findings
- ✅ Confirmed bugs have fix plans with blast radius estimates

### Process Criteria
- ✅ Developer was consulted at all three interaction gates
- ✅ No fixes were implemented without developer approval
- ✅ Each fix was verified individually before proceeding to the next
- ✅ The behavior catalog provides a complete record of what was traced and audited

### Quality Criteria (if Phase 5 was executed)
- ✅ All approved fixes have been implemented
- ✅ Existing tests still pass after fixes
- ✅ New tests cover fixed behaviors
- ✅ Re-audit confirms fixes resolved the original findings
- ✅ No new Likely Bug findings introduced by fixes

## Coordination Notes

- **Phase ordering is strict:** Survey → Trace → Audit → Plan → Implement. Each phase depends on the previous phase's output.
- **User gates are non-negotiable:** Never proceed past a gate without developer input. The developer's clarification of intent is what makes this workflow valuable — without it, the audit is just another code review.
- **One fix at a time:** Phase 5 implements fixes individually, not in batches. This makes regression identification straightforward.
- **Context passing:** Each agent receives the output of previous phases. The behavior catalog from Phase 2 is the central artifact that Phase 3 evaluates and Phase 4 plans fixes against.
- **Existing resources:** This workflow references 22+ existing targeted Android review prompts and 12+ existing Android skills. It does not duplicate their analysis — it orchestrates them within the behavioral audit framework.
- **Scope management:** If the developer selects many feature areas in Gate 1, process them sequentially (complete all 5 phases for area 1, then area 2) rather than tracing everything before auditing. This keeps the context manageable and delivers value incrementally.

Target: $ARGUMENTS
