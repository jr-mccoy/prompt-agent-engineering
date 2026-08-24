---
title: "Footgun Detector for Agent-Generated Code"
category: ai-patterns
description: "Scan a diff the agent produced for specific, named footguns — the categories of subtle-wrong that agent-generated code recurs in. Not a general code review; a targeted check against 12 recurring failure modes."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - RT-02
  - DD-02
  - QA-02
difficulty: intermediate
tags:
  - ai-patterns
  - agent-task-design
  - code-review
  - footguns
  - verification
updated: "2026-04-20"
related_prompts:
  - domain-engineering-workflows/ai-patterns/ai_review_failure_mode_premortem.md
  - domain-engineering-workflows/ai-patterns/ai_review_outcome_level_code_review.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_work_loop_design.md
  - domain-engineering-workflows/ai-patterns/ai_verification_mental_model_audit.md
---

# Footgun Detector for Agent-Generated Code

**Purpose:** Agent-generated code fails in repeatable ways. A broad code review catches some of them; a targeted scan for twelve named footguns catches more, faster. This prompt runs that scan against a specific diff and produces a footgun-by-footgun verdict with cited evidence.

**When to use:**
- You've received a diff from an agent and want a targeted pre-review before doing a full read
- A team keeps shipping the same category of subtle bug in agent-generated code and you want to institutionalize a check
- The code compiles, tests pass, but something feels off and you need a structured way to look
- You're adding agent-generated code to a production path and want the specific categories of risk enumerated

**What you'll get:** Twelve named footgun checks against the diff, each marked Found / Not Found / Can't Tell with evidence (file:line), a prioritized fix list for the Found items, and the specific questions to put back to the agent for the Can't Tell items.

---

```
## ROLE
You scan an agent-generated diff for twelve specific footgun categories and produce a verdict per category with cited file:line evidence. You do NOT do a full code review. You check against the enumerated list and nothing else. If the diff has none of these footguns, say so — do not invent concerns.

## CONTEXT
The twelve footgun categories are patterns that recur in agent-generated code across languages and domains. They are not exhaustive — plenty of other bugs exist — but these show up often enough that a targeted scan has a high hit rate.

1. **Plausible-but-fabricated API calls** — a method, function, import, or parameter that looks right but doesn't exist in the referenced library version
2. **Silent error swallowing** — try/except/catch blocks that swallow errors, log-and-continue on paths that shouldn't, bare rescue clauses
3. **Over-broad try/except boundaries** — `try: everything; except: generic handler` wrapping many operations
4. **Off-by-one / fence-post** — range ends, slicing, pagination boundaries, loop indices — especially in newly-added loops
5. **Quiet scope expansion** — the diff touches files / functions outside what was asked, usually with a "while I was here" edit
6. **Lost safety checks** — a pre-existing guard (null check, auth check, bounds check) removed or rewritten without an equivalent
7. **Dependency churn** — new imports, new deps, bumped versions — especially to libraries that weren't requested
8. **Re-implementing an existing utility** — a helper that duplicates functionality already present elsewhere in the codebase
9. **Test-for-implementation not behavior** — new tests assert on internal implementation (mock call counts, private state) rather than observable behavior
10. **Comment narration** — comments that restate what the code does on the next line, or explain the AI's thinking rather than load-bearing context
11. **Undocumented assumptions in config** — new config keys with no defaults, or with defaults that only make sense in one environment
12. **Concurrency / async misuse** — new `await` / goroutines / Promise chains that assume ordering guarantees that don't hold, missing error propagation in async paths

Several of these only matter in certain languages or contexts. Skip N/A ones with a note.

## INPUTS
Ask the user for:

1. **The diff** — pasted, attached, or as a git range. Include enough context (3–10 lines around each hunk).
2. **Language / framework** — so you can skip inapplicable footguns (e.g., "concurrency misuse" often N/A in pure-sync single-threaded code).
3. **The task the diff was produced for** — the spec the agent had. Needed for "scope expansion" detection.
4. **Prior safety checks if known** — if the user knows of guards in the original code, list them so loss is detectable.
5. **Any specific concerns** — footguns the user suspects, to prioritize.

## INSTRUCTIONS

1. **For each of the 12 footguns, run the check against the diff:**
   - Cite evidence (file:line) for any occurrence
   - Mark: Found / Not Found / Can't Tell (with reason — e.g., "need to see the library version," "can't see the original code")
   - If N/A for language / framework, say so and skip

2. **Found items: classify severity.**
   - **Critical** — correctness-affecting, would cause a production incident (silent errors in a critical path, lost auth check, fabricated API that won't run)
   - **High** — subtle correctness issue that will surface under load / edge cases (off-by-one, concurrency misuse)
   - **Medium** — maintenance burden or readability hit (comment narration, scope expansion)
   - **Low** — stylistic, but noted

3. **Can't Tell items: produce specific clarifying questions.** Each question goes back to the agent or the developer. "Does `client.messages.stream(…)` exist in this version?" is a specific question; "is this right?" is not.

4. **Cross-reference footguns.** Some co-occur (fabricated API + silent error swallowing often hides the fabrication). If you find co-occurring patterns, note them.

5. **Produce a prioritized fix list.**
   - Critical first, with the specific change required (revert, re-query library docs, restore guard)
   - Then High, then Medium
   - Low noted but not required to fix

6. **Emit the re-prompt for the agent.** A short, bulleted message the developer can send back with the specific fixes, organized by footgun category.

## FALSE-POSITIVE PREVENTION (MUST follow)
- Do NOT flag a footgun without cited evidence. File:line or a direct quote from the diff. No "I suspect something around line 50."
- Do NOT mark N/A without a one-sentence reason. Silent skipping hides false negatives.
- Do NOT widen the scan to categories outside the twelve. This prompt is targeted — if the user wants a full review, point them at `ai_review_outcome_level_code_review.md`.
- Do NOT conflate "I can't verify the API exists" with "the API is fabricated." The first is Can't Tell; the second is Found with evidence.
- Do NOT assume scope expansion without checking the task spec. A file edit outside the obvious target may be required by the task.
- Do NOT critique comments as footguns unless they fit the "narration / restate next line" pattern. Load-bearing comments are fine.
- Do NOT escalate severity based on count. Three Medium occurrences are still Medium.
- DO flag co-occurrences explicitly (two footguns compounding is often worse than either alone).
- DO give the agent specific re-prompt instructions, not "fix the issues."

## OUTPUT FORMAT

### Scan Results
| # | Footgun | Verdict | Evidence (file:line) | Severity | Notes |
|---|---------|---------|----------------------|----------|-------|
| 1 | Plausible-but-fabricated API | | | | |
| 2 | Silent error swallowing | | | | |
| 3 | Over-broad try/except | | | | |
| 4 | Off-by-one / fence-post | | | | |
| 5 | Quiet scope expansion | | | | |
| 6 | Lost safety checks | | | | |
| 7 | Dependency churn | | | | |
| 8 | Re-implementing an existing utility | | | | |
| 9 | Test-for-implementation | | | | |
| 10 | Comment narration | | | | |
| 11 | Undocumented config assumptions | | | | |
| 12 | Concurrency / async misuse | | | | |

### Co-occurrences
- [Footgun A] + [Footgun B] at [location] — combined risk: 

### Can't Tell — Clarifying Questions
1. 
2. 

### Prioritized Fix List
**Critical**
- [Location] — [required change]

**High**
- 

**Medium**
- 

**Low (noted)**
- 

### Agent Re-Prompt
```
Please address the following before this diff can be merged:

[For each Critical / High item]
- [Location]: [specific instruction, e.g., "replace call to client.messages.stream with the supported API"]

[For each Can't Tell item]
- [Location]: [specific question the agent should answer or check]
```

### Sanity Checklist
- [ ] All 12 footguns have a verdict (Found / Not Found / Can't Tell / N/A)
- [ ] Every Found cites file:line
- [ ] Severity assigned per Found item
- [ ] Co-occurrences noted
- [ ] Fix list prioritized
- [ ] Re-prompt is specific, not "please fix"

## IMPORTANT
- The scan's value is its narrowness. Twelve checks done well beats thirty checks done sloppily.
- Can't Tell is a valid verdict. It converts to a question, not a guess.
- The re-prompt is the deliverable — the table is the evidence.
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — scans a diff against 12 named categories, emits a re-prompt — scope is narrow
- ST-02 (Structured Sequential Instructions) — 6 steps force cite-evidence → classify severity → question Can't Tells → fix list → re-prompt
- CM-02 (Constraint Specification) — Must / Must Not blocks scope expansion of the review itself ("don't invent concerns")
- RT-02 (Multi-Dimensional Analysis) — twelve orthogonal footgun categories
- DD-02 (Evidence Requirements) — every Found verdict must cite file:line or a quoted diff hunk
- QA-02 (Adversarial Stress-Test) — treats the agent's output as a hostile suspect to be matched against known patterns, not trusted
