---
title: "Diagnose Why Vibe-Coding Has Hit a Wall on a Specific Project"
category: software-engineering/vibe-coding-rescue
description: "When an AI-assisted project has stopped making forward progress — regressions keep appearing, every new feature breaks two old ones, the AI keeps rewriting the same file — classify the wall into a specific failure mode and produce the rescue action that fits. No generic 'add tests' advice."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - RT-07
  - RT-11
  - QA-01
difficulty: intermediate
tags:
  - vibe-coding
  - rescue
  - diagnosis
  - regressions
  - ai-code-debt
updated: "2026-04-21"
related_prompts:
  - domain-software-engineering/vibe-coding-rescue/viberescue_rules_file_design.md
  - domain-software-engineering/vibe-coding-rescue/viberescue_decompose_stuck_task.md
  - domain-software-engineering/vibe-coding-rescue/viberescue_security_audit.md
  - domain-software-engineering/vibe-coding-rescue/viberescue_engineer_handoff_briefing.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_code_footgun_detector.md
  - domain-engineering-workflows/ai-patterns/ai_verification_mental_model_audit.md
---

# Diagnose Why Vibe-Coding Has Hit a Wall on a Specific Project

**Purpose:** "Vibe-coding" — working with an AI coding tool in long, improvisational sessions without strong specification — works until it doesn't. This prompt runs a structured diagnosis when a project has hit a wall: classify the failure into a specific mode, identify the load-bearing cause, and produce the rescue action. Refuses to output generic advice like "add tests" or "clean up your code."

**When to use:**
- A project built largely with AI assistance has stopped making reliable forward progress.
- Each new feature seems to break something previously working.
- The AI keeps rewriting the same file or suggesting changes that revert earlier decisions.
- The human is losing confidence that the codebase matches their mental model.
- A team is evaluating whether to rescue the project in place or hand it to a new engineer (see `viberescue_engineer_handoff_briefing.md`).

**Don't use when:** The project is working fine and the user is looking for preventive advice. Use a rules-file prompt or a code-review prompt instead.

**Audience:** The engineer or builder working on the project. Output is a diagnosis + rescue action, actionable today.

---

## Inputs Required

Ask for all of these. Refuse to diagnose without 1, 2, 3, and 4.

1. **Project shape.** Language, framework, rough LOC, test coverage (rough %; "none" is a valid answer), version control history status (commits frequent? rare? rebased?).
2. **The three most recent "going wrong" sessions.** For each: what the user was trying to do, what the AI did, what broke, what the user did to unstick. Concrete.
3. **The last 5–10 things shipped successfully.** What worked, roughly when, and whether you'd be able to explain each one to a new engineer today.
4. **Map the files.** Rough count of source files. List the 5 files the AI touches most. List any files the user hasn't read in weeks but the AI keeps editing.
5. **The user's current mental model.** In ≤ 5 sentences: what the project does, its main components, where the data flows. Vague is OK — vagueness is itself a signal.
6. **Tooling in use.** Which AI tool, any rules file, any test harness, any CI.
7. **Stakes.** Is this a hobby, a prototype for internal use, a production service, something with customers? Changes the rescue aggressiveness.

---

## Instructions

### Step 1 — Classify into exactly one primary wall mode

Use only this taxonomy. If two plausibly fit, pick the one earliest in the causal chain.

| # | Wall mode | Signs | Core rescue |
|---|-----------|-------|-------------|
| 1 | **Mental-model drift** | User can't explain parts of the codebase without the AI. "What does this do?" answered only by asking the AI to reread. | Re-ground: narrate and test what exists before adding more. |
| 2 | **Spec-free loop** | AI keeps changing the same file; each session reverses the last. No written spec anywhere for the disputed behavior. | Write the spec for the disputed behavior, then diff current code against it. |
| 3 | **No invariants** | No tests, or tests only assert what just-generated code produces. Regressions land silently. | Add invariant tests that encode contracts, not current behavior. |
| 4 | **Scope bloat without deletion** | Project has grown features by accretion; nothing has been removed; many files have 3+ ways to do the same thing. | Subtraction pass: delete dead paths and consolidate. |
| 5 | **Context rot** | Every new session spends half its time re-explaining context; AI gets forgetful or contradicts itself across sessions. | Install project memory (`airollout_long_running_project_memory.md`). |
| 6 | **Rules-file absence** | No written conventions; every session re-negotiates style, error handling, naming. AI drifts. | Write a rules file (`viberescue_rules_file_design.md`). |
| 7 | **Security / correctness debt** | Code mostly works but has accumulated patterns that look dangerous on inspection (SQL concat, unsanitized input, unverified external calls). | Focused audit (`viberescue_security_audit.md`). |
| 8 | **Wrong architecture for the problem** | Load-bearing architectural choice early on doesn't fit what the project has become. Every feature fights the architecture. | Rescue may not be local — consider partial rewrite with a fresh architectural brief. |
| 9 | **Task too big for the loop** | The AI keeps failing at a specific task because the task is too big per turn, not because the project is broken. | Decompose (`viberescue_decompose_stuck_task.md`). Project itself may be fine. |
| 10 | **Human exhaustion** | User is tired; the project is fine; every session feels frustrating because attention is thin. | Pause. Don't rescue a project that's fine. |

Do not invent new modes. If none fit, state so and ask what's actually happening.

### Step 2 — Justify the classification with the user's own words

Quote or paraphrase from inputs 2, 3, 5, and 4 specifically. One or two sentences. If the user's description spans two modes, name the second and why it was ranked second.

### Step 3 — Check for compounding modes

Some walls stack. Do these cascades apply? If yes, call them out:

- **Mode 1 + Mode 3:** Mental-model drift + no invariants = the user has no way to detect when the code no longer matches intent. Dangerous.
- **Mode 2 + Mode 5:** Spec-free loop + context rot = the AI will literally never converge. Fix both or stop.
- **Mode 4 + Mode 8:** Scope bloat + wrong architecture = the "rescue" is probably a rewrite of a subset. Acknowledge.
- **Mode 6 + Mode 2:** No rules + no spec = everything is negotiated every session. Agree on rules first, spec second.

Cascades change the rescue. Treat them as primary findings, not footnotes.

### Step 4 — Deliver the rescue action

The action must be:

- **Specific.** Named file, named spec, named prompt, named test.
- **Small for the first step.** Under 60 minutes for step 1.
- **Tied to the classified mode.** Mode 3 gets invariant tests; it doesn't get "be more careful."
- **Aware of stakes.** Production service with customers (input 7) blocks certain "just rewrite" rescues.

If mode is 10 (exhaustion), the action is to stop. Say so plainly.

### Step 5 — State the "one-week reality check"

One specific observable state the user should see within a week if the rescue is landing. If that state isn't reached, the diagnosis was probably wrong — re-run the prompt.

### Step 6 — Call out what the rescue does NOT fix

Be explicit: this rescue doesn't fix [other wall modes if also present]. If there's a secondary mode, name it and the follow-up rescue. Do not attempt multi-rescue in one run.

### Step 7 — Handoff consideration

For projects with real stakes (input 7 = production / customers), explicitly answer: is in-place rescue the right posture, or should this be briefed to a different engineer for takeover? Point to `viberescue_engineer_handoff_briefing.md` if takeover is warranted. Giving up gracefully is sometimes the rescue.

### Step 8 — Verify and output

Run the verification checklist.

---

## Constraints

### Must
- Pick exactly one primary wall mode.
- Justify with the user's own words.
- Check the four cascade patterns.
- Deliver one specific rescue action, not a menu.
- State an observable one-week reality check.
- Call out what the rescue does NOT fix.

### Must Not
- Invent new modes.
- Give generic advice ("add tests," "refactor," "be more careful with prompts").
- Pile multiple rescues into one run.
- Shame the vibe-coding approach — it has a real scope.
- Recommend rewrite as default for Modes 1–7. Rewrite is Mode 8 or high-stakes-handoff territory.
- Claim mental model is fine based on the AI's own retelling. That's circular.

---

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Default to Mode 3 (no invariants) because tests are absent. Many Mode 1 or Mode 2 projects will grow tests naturally once the mental model or spec is restored — tests alone without those prerequisites produce brittle, AI-shaped tests.
- Classify as Mode 8 (wrong architecture) without a concrete "every feature fights X" example. Architectural rewrites are expensive; require evidence.
- Confuse Mode 9 (task too big) with project-level wall. Mode 9 is a task-level problem inside a mostly-fine project.
- Miss Mode 10 (exhaustion). If the user is describing the project neutrally but sounds depleted, the project isn't broken — rest is the move.
- Accept "the AI keeps doing X" as evidence without checking whether the user has written down "the AI should do Y." Without a written spec or rules, the AI is doing its best.

✅ **DO:**
- When the user's mental model (input 5) is vague, lean toward Mode 1.
- When the same file keeps getting rewritten (input 4), lean toward Mode 2.
- When successful shipments (input 3) are explainable but recent work is not, the wall is recent, not total.
- When the wall showed up after scope grew (input 3, 4), consider Mode 4.
- Check whether the user has a rules file before assigning any mode. Rules-file absence (Mode 6) underlies a lot of apparent other modes.

---

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** Diagnosis is confident but wrong; user follows the rescue for a week, it doesn't help, they conclude AI-assisted development doesn't work.

❌ **UNHELPFUL failure:** Diagnosis hedges across five modes and produces no action; user ends with the same vibe-coded wall they started with.

✅ **Quality check:** A senior engineer who knew this project could read the diagnosis, agree with the classification, and expect the one-week reality check to fire.

---

## Output Format

```markdown
# Vibe-Coding Wall Diagnosis — [Project]

## Primary Mode
**Mode:** [# + name]

**Justification:** [One to two sentences grounded in the user's words / evidence from inputs 2–5.]

**Secondary candidate:** [Mode + one-line reason, or "none"]

## Cascade Check
- Mode 1 + 3: [present? impact]
- Mode 2 + 5: [present? impact]
- Mode 4 + 8: [present? impact]
- Mode 6 + 2: [present? impact]

## Rescue Action
[Specific, small first step. Named files / specs / prompts / tests.]

## Stakes Check
- Current stakes: [input 7]
- In-place rescue appropriate: [yes / consider handoff]
- If handoff: [`viberescue_engineer_handoff_briefing.md` + why]

## One-Week Reality Check
[Specific observable state. If not reached by [date], re-run this prompt.]

## What This Rescue Doesn't Fix
- [Other modes present that this rescue ignores, and pointer to follow-up.]
```

---

## Verification

- [ ] Exactly one primary mode chosen.
- [ ] Justification cites user's own words / evidence.
- [ ] Cascade check run on all four pairs.
- [ ] Rescue action is specific, small, tied to the mode.
- [ ] One-week reality check is observable.
- [ ] What-this-doesn't-fix section exists.
- [ ] Stakes check performed; handoff considered where warranted.
- [ ] No generic "add tests / refactor / be careful" advice.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Output is a single-mode diagnosis + one specific rescue action, not a menu of advice.
- **ST-02 (Structured Sequential Instructions):** Eight steps force classification → justification → cascade check → rescue → reality check → unfixed → handoff → verify.
- **CM-02 (Constraint Specification):** Must Not block forbids generic advice and multi-rescue.
- **DS-01 (Framework Application):** Ten-mode taxonomy; disallowing invention keeps it load-bearing.
- **RT-07 (Cascade Effect Analysis):** Four named cascade pairs catch the compounding failures one-mode diagnosis misses.
- **RT-11 (Error Recovery):** One-week reality check + handoff pointer handle the "diagnosis was wrong" and "rescue too late" cases.
- **QA-01 (Self-Verification):** Verification checklist and dual-failure test block confident-but-wrong diagnoses.
