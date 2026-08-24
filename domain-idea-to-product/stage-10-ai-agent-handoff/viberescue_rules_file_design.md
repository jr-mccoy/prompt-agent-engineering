---
title: "Build a Rules File That Constrains AI Output for a Codebase"
category: software-engineering/vibe-coding-rescue
description: "Produce a rules file (CLAUDE.md, .cursorrules, or equivalent) tuned to a specific codebase — grounded in the conventions the code actually follows and the failures the AI has actually made, not generic 'be a good engineer' guidance."
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
  - rules-file
  - claude-md
  - conventions
  - ai-guardrails
updated: "2026-04-21"
related_prompts:
  - domain-software-engineering/vibe-coding-rescue/viberescue_wall_diagnosis.md
  - domain-software-engineering/vibe-coding-rescue/viberescue_decompose_stuck_task.md
  - domain-engineering-workflows/ai-native-rollouts/airollout_long_running_project_memory.md
  - domain-engineering-workflows/ai-native-rollouts/airollout_delegate_like_parallel_coworker.md
  - domain-prompt-engineering/escape-median/escapemedian_bootstrap_instruction_file.md
---

# Build a Rules File That Constrains AI Output for a Codebase

**Purpose:** Generic AI rules files ("write clean code, handle errors, follow conventions") don't constrain anything. A useful rules file is tuned to one specific codebase: it encodes the conventions the code actually follows, forbids the mistakes the AI has actually made here, and points to the specific files or functions that model good patterns. This prompt produces that file.

**When to use:**
- A codebase has no rules file (or has a stub one) and AI output keeps drifting from conventions.
- The user keeps correcting the AI on the same handful of things — imports, error handling, naming, test style.
- A new rules-file is being drafted or an existing one rewritten after a wall-diagnosis (`viberescue_wall_diagnosis.md`) identified Mode 6.
- A team is moving from individual CLAUDE.md files to a shared, committed one.

**Don't use when:** The project has no consistent conventions yet. Write down the 5 decisions first, then use this prompt.

**Audience:** An engineer or lead authoring a rules file for their team's codebase. Output is a file ready to commit.

---

## Inputs Required

1. **Codebase shape.** Language(s), framework(s), rough LOC, repo layout.
2. **3–5 files that model good patterns.** Files the user considers "how we do things here." These ground the rules in real code.
3. **The last 10 AI mistakes the user corrected.** Concrete: "AI imported from the wrong path," "AI used `snake_case` on a new function in a camelCase file," "AI added a third argument defaulting to None instead of a new overload." Verbatim is best.
4. **Existing conventions, if any.** Style guide, linter config, README snippets. If there is a rules file already, paste it.
5. **Forbidden patterns.** Anything the user has explicitly told the AI not to do and the AI still does: don't wrap everything in try/except, don't add dependencies, don't touch the migrations directory, etc.
6. **Project-specific domain vocabulary.** 5–15 terms that mean something specific in this codebase (a "User" is not a generic user; a "Job" has a specific lifecycle). The AI needs to know these mean THIS, not the textbook thing.
7. **The tool this rules file is for.** Claude Code / Cursor / Copilot / repo-level convention doc for humans + AI. Changes the file name and some structure.

---

## Instructions

### Step 1 — Refuse to write generic rules

Reject entries like "write clean code," "follow best practices," "be consistent," "use good names." They compile to nothing when read by an LLM. If the user's input 4 has generic entries, replace them with specific ones from inputs 2–3 or drop them.

### Step 2 — Ground every rule in evidence

Every rule must be sourced to one of:

- A specific file/pattern in input 2 (positive exemplar).
- A specific AI mistake in input 3 (negative exemplar).
- A specific forbidden pattern in input 5 (constraint).
- A specific domain term in input 6 (vocabulary).

If a rule can't be sourced, it isn't a rule yet — drop it.

### Step 3 — Organize the rules file by what the AI reads first

AI tools read files top-to-bottom and some truncate. Put the highest-value, most-frequently-violated rules at the top. Structure (in this order):

#### 3.1 Project purpose (2–3 sentences)
What the project is, who it's for, what "good" looks like operationally. Brief.

#### 3.2 Hard don'ts (5–10 bullets, max)
The most important forbidden patterns. These are the ones the AI will otherwise violate. Sourced from input 5 and input 3 (where corrections are repeat offenders).

#### 3.3 Conventions (grouped, concrete)
Organized by area. Each entry points to a file in input 2 or cites a rule with reasoning.

- **Imports + module structure:** How imports are organized (alphabetical? grouped? absolute vs relative?). Cite a file.
- **Naming:** Case conventions per identifier type. Cite specific examples.
- **Error handling:** When to raise, when to log, when to return. Cite a handler file.
- **Logging:** Format, levels, what to include / exclude.
- **Testing style:** Test runner, naming, fixture patterns. Cite a test file.
- **Function / class shape:** Length limits (soft guidance), argument style, defaults.
- **File organization:** Where things go. Name the directory map.

#### 3.4 Domain vocabulary (glossary)
From input 6. One short sentence per term. "In this codebase, a `Job` is …" — force the AI out of generic priors.

#### 3.5 Pointers, not content
Short list pointing to: architecture doc, state doc, decisions directory (see `airollout_long_running_project_memory.md`). Rules file stays short; detail lives elsewhere.

#### 3.6 Recent AI mistakes (rotating list)
A section where recent recurring AI mistakes get written down. Small. Updated as new ones appear. This is the "teach the AI what it just got wrong" surface.

### Step 4 — Size the file for the tool

- Claude Code / CLAUDE.md: target ≤ 400 lines. If longer, split and use pointers.
- Cursor / .cursorrules: shorter; aim for ≤ 150 lines of concrete rules.
- Copilot / GitHub rules: see the tool's current size and format limits; apply accordingly.

A rules file longer than the tool reads well is worse than a shorter one.

### Step 5 — Make each rule self-contained and LLM-friendly

Rules should:

- Be phrased as an imperative or a constraint, not a philosophy.
- State both the DO and the DON'T where ambiguous.
- Include the concrete thing the rule is about, not just the category. ("Use `logger.info()` for request logs and `logger.exception()` inside except blocks; do not use `print()` or bare `logger.error()`.")

Avoid phrasing like "prefer X." LLMs downweight soft preferences.

### Step 6 — Add a "when in doubt" protocol

At the end of the file, a short section:

- If unsure about naming: look at [file].
- If unsure about error handling: look at [file].
- If a required decision isn't in this file: ask the user before writing code; don't guess.

This converts rules-file gaps into explicit escalation rather than silent AI defaults.

### Step 7 — Run the "one-week repeat" test

For each of input 3 (last 10 AI mistakes), walk through: does the file as drafted prevent this mistake when the AI reads it at the top of a new session? If not, revise. The file exists to stop the repeats.

### Step 8 — Define how the rules file is maintained

Name:

- **Owner:** Who updates it.
- **Update trigger:** Any AI mistake corrected twice within a week gets a rule.
- **Prune trigger:** Every quarter, remove rules that no longer fire (the behavior is now automatic or the convention has changed).
- **Drift check:** On a schedule (monthly), sample 5 recent AI outputs — are they actually following the file?

### Step 9 — Verify and output

Run the verification checklist.

---

## Constraints

### Must
- Every rule is sourced to inputs 2, 3, 5, or 6.
- Hard don'ts section is at the top.
- Domain vocabulary is included.
- File includes pointers to architecture / state / decisions rather than embedding them.
- A "when in doubt" escalation section is present.
- Each of input 3's AI mistakes is prevented by a rule in the file.

### Must Not
- Include generic rules ("write clean code," "follow best practices").
- Grow the file past the tool's effective read size.
- Embed long architecture or state — use pointers.
- Use soft-preference phrasing ("prefer," "try to") for rules that should be firm.
- Repeat the same rule in multiple sections.
- Include commented-out or aspirational rules. If it's not the rule now, it doesn't belong.

---

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Assume the user's listed good-pattern files (input 2) actually agree with each other. Check — if two cited files disagree on a convention, flag it and ask which is canonical.
- Paste a linter config into the rules file. The rules file complements the linter; it doesn't duplicate it. Reference the linter, don't inline it.
- Include rules the linter or formatter already enforces. The rules file is for decisions tools can't enforce automatically.
- Cram domain vocabulary entries with philosophy. One short sentence per term.
- Leave "ask the user when in doubt" out. Without an escalation path, AI silently defaults.

✅ **DO:**
- Check the input 2 files for consistency. If input 2 files disagree, the project has a convention conflict — name it.
- Keep the hard don'ts section tight (5–10). Long don't-lists become noise.
- Include at least one positive exemplar pointer per convention section ("see `src/api/handler.py` for the error-handling shape").
- Phrase vocabulary entries for an LLM prior: "A Job in this codebase is [specific thing with lifecycle]; this is NOT the generic sense of the word."
- Version the rules file (comment at top with "last meaningful update: YYYY-MM-DD").

---

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** File is long and contradictory; AI silently picks whichever rule is closer to its prior, produces wrong-looking code that the user approves because "it looked right."

❌ **UNHELPFUL failure:** File is short, generic, and the AI's behavior doesn't change; user concludes rules files don't work.

✅ **Quality check:** A senior engineer on the project, reading the file cold, could predict 80% of the conventions the codebase actually follows.

---

## Output Format

```markdown
# [Tool-appropriate filename, e.g., CLAUDE.md / .cursorrules]

## Project
[2–3 sentences.]

## Hard Don'ts
- [Specific forbidden pattern, sourced from input 5 or repeat-offender from input 3]
- [...]

## Conventions

### Imports + Module Structure
[Rule; cite file from input 2.]

### Naming
[Rule; examples.]

### Error Handling
[Rule; cite handler file.]

### Logging
[Rule; format.]

### Testing
[Rule; cite test file.]

### Function / Class Shape
[Rule; soft guidance with specifics.]

### File Organization
[Directory map or pointer.]

## Domain Vocabulary
- **Term:** short specific definition.
- [...]

## Pointers
- Architecture: [file]
- Current state: [file]
- Decisions: [directory]

## Recent AI Mistakes
- [Latest correction, with the rule that now covers it.]

## When in Doubt
- Naming: look at [file].
- Error handling: look at [file].
- Anything else: ask before writing code.

## Maintenance
- Owner: [role]
- Update trigger: AI mistake corrected ≥ 2x in a week.
- Prune cadence: quarterly.
- Drift check: monthly sample of AI outputs.

<!-- Last meaningful update: YYYY-MM-DD -->
```

(Include a separate small artifact after the file:)

```markdown
## Input-Mistake Coverage Table
| AI mistake (input 3) | Rule in file that prevents it |
|----------------------|-------------------------------|
| | |
```

---

## Verification

- [ ] Every rule is sourced to inputs 2, 3, 5, or 6.
- [ ] File size is within the tool's effective read range.
- [ ] Hard don'ts section sits at the top.
- [ ] Each input-3 mistake is covered by a rule (coverage table).
- [ ] Domain vocabulary present.
- [ ] Pointers, not embedded architecture/state.
- [ ] "When in doubt" escalation section present.
- [ ] Maintenance protocol named.
- [ ] No generic "write clean code" entries.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Output is a rules file for a specific codebase, tied to evidence, not a generic engineering manifesto.
- **ST-02 (Structured Sequential Instructions):** Nine steps force refuse-generics → ground-in-evidence → ordered sections → size → phrasing → escalation → repeat-test → maintenance → verify.
- **CM-02 (Constraint Specification):** Must Not block forbids generic rules, inlined architecture, and soft-preference phrasing.
- **DS-01 (Framework Application):** Ordered section structure (purpose → don'ts → conventions → vocab → pointers → mistakes → escalation → maintenance) is the load-bearing framework.
- **RT-07 (Cascade Effect Analysis):** Input-mistake coverage table catches the cascade where a "rules file" exists but doesn't actually stop the repeats.
- **RT-11 (Error Recovery):** "When in doubt" section converts rules-file gaps into explicit escalation rather than silent defaults.
- **QA-01 (Self-Verification):** One-week repeat test plus coverage table verify the file fights the actual failures.
