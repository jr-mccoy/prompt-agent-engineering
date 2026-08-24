---
title: "Generate a Project Rules File for a Vibe-Coded Android App (Sourced to Audit Evidence)"
category: software-engineering/vibe-coding-rescue/android
description: "Produce a project CLAUDE.md / .cursorrules / equivalent grounded in actual conventions and AI mistakes found in this codebase — not generic Android advice. Sources rules from the codebase audit's good patterns, the security audit's hard don'ts, the wall-diagnosis's primary mode, and any AI patterns repeating across both audits. Output is ≤400 lines and includes hard don'ts, required patterns, vocabulary, lifecycle rules, security gates, and an escalation protocol."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - ST-04
  - CM-02
  - CM-04
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - vibe-coding
  - android
  - rules-file
  - claude-md
  - cursorrules
  - project-memory
updated: "2026-05-17"
related_prompts:
  - domain-software-engineering/vibe-coding-rescue/android/android_viberescue_wall_diagnosis.md
  - domain-software-engineering/vibe-coding-rescue/android/android_viberescue_codebase_audit.md
  - domain-software-engineering/vibe-coding-rescue/android/android_viberescue_security_privacy_audit.md
  - domain-software-engineering/vibe-coding-rescue/viberescue_rules_file_design.md
  - domain-engineering-workflows/ai-native-rollouts/airollout_long_running_project_memory.md
---

# Generate a Project Rules File for a Vibe-Coded Android App

**Purpose:** A rules file (`CLAUDE.md`, `.cursorrules`, `AGENTS.md`, equivalent) is the single most effective preventive against vibe-coding regression — if it's grounded in the actual codebase. Generic Android best-practices files don't work: the AI will follow them only when it remembers to, and they don't address the specific mistakes this codebase keeps making. This prompt generates a project rules file sourced entirely to evidence from the audits and the actual codebase — every rule traces to a positive exemplar, a forbidden pattern, a repeated AI mistake, or a domain vocabulary entry. Generic rules are refused.

**When to use:**
- After running `android_viberescue_codebase_audit.md` AND `android_viberescue_security_privacy_audit.md`. The "AI patterns repeating" sections from both feed the hard don'ts list.
- Wall diagnosis pointed to A12 (context rot) — every session re-negotiates conventions and re-introduces rejected patterns.
- The team is onboarding a new AI tool or new engineer and needs a written contract.
- Periodically as part of a maintenance cadence (~quarterly), to refresh against accumulated changes.

**Don't use when:** The audits haven't been run. Generic rules files are net-negative because they crowd out specific rules.

**Audience:** The engineer (who reviews and commits the rules file) and every future AI session that will read it as project context.

**Agent portability note:** The output file name can be `CLAUDE.md` (Claude Code), `.cursorrules` (Cursor), `AGENTS.md` (Codex / generic), or `.windsurfrules`. The CONTENT is portable. Recommend the user choose the filename their primary agent reads, and add same-content symlinks for the others.

---

## Inputs Required

Refuse to generate without 1, 2, 3, and 5.

1. **Codebase audit output** from `android_viberescue_codebase_audit.md` (especially the "AI patterns repeating" section and the findings list).
2. **Security audit output** from `android_viberescue_security_privacy_audit.md` (same sections).
3. **Three to five "good pattern" files.** Paths to files the engineer considers exemplary — well-architected, idiomatic, what they want more of. The rules file will derive "required patterns" from these.
4. **Optional: wall-diagnosis output.** Primary mode shapes the rules file's emphasis (e.g., A2 lifecycle drift → lifecycle rules get top billing).
5. **Project shape.** UI toolkit, DI framework, async approach, persistence, networking, multi-module yes/no. (Same fields as audit prompts.)
6. **Domain vocabulary, 5–15 terms.** Domain-specific names (entities, screens, flows) that have a canonical spelling and meaning in this codebase. AI tends to invent synonyms; the rules file pins the canonical form.
7. **Optional: existing rules file.** If one exists, it will be refactored and merged rather than overwritten blindly.
8. **Target agent.** Claude Code / Cursor / Codex / Windsurf / generic. Determines the filename and any agent-specific syntax (front-matter, slash commands).

---

## Instructions

### Step 1 — Inventory the evidence base

From inputs 1 and 2, extract:

- **Hard don'ts (forbidden patterns):** From both audits' "AI patterns repeating" sections, plus any Critical or High finding category that's likely to recur. Each don't must trace to ≥1 specific finding (file:line citation in the rules file).
- **Required patterns:** From input 3 (good-pattern files). Read each, identify what makes it good (consistent state hoisting, viewModelScope discipline, EncryptedSharedPreferences usage, proper Hilt scoping, etc.). Each required pattern traces to ≥1 exemplar file.
- **Vocabulary:** From input 6. Each term gets a canonical spelling and a one-sentence definition.
- **Wall-diagnosis emphasis:** From input 4. If primary mode is A2 (lifecycle), the rules file leads with lifecycle. If A7 (security), leads with security gates.

### Step 2 — Detect conflicts

- If a "required pattern" from input 3 conflicts with a "hard don't" from inputs 1/2 (e.g., the exemplar uses an API the audit forbids), flag the conflict for human review BEFORE writing the rules file. The exemplar may be wrong, or the don't may be over-broad.
- If input 7 (existing rules file) has rules that contradict the new evidence, list them with the conflict and a recommendation (keep / drop / modify).

### Step 3 — Structure the rules file

Use this section order. Section headings are fixed; content is sourced to evidence.

1. **Project context** (≤8 sentences): what this app is, primary toolkit choices, where to find the canonical structure.
2. **Hard don'ts** (forbidden patterns): The AI must never do these. Each has a one-line rule + a one-line "seen in [file:line]" or "audit flagged [N] instances" trace. 10–25 items max.
3. **Required patterns:** What the AI must do for each common task. Each has a rule + a "see [exemplar file]" pointer. 8–20 items.
4. **Lifecycle rules** (Android-specific): scope discipline, observer cleanup, state survival on rotation / process death. Cite the canonical lifecycle helper if the codebase has one.
5. **Security gates:** Things that must be checked before any networking, persistence, or component-export change. Each gate is a yes/no question the AI must answer before producing code.
6. **DI / Hilt rules** (if Hilt): scope assignments, module boundaries, what `@Singleton` vs `@ViewModelScoped` means here.
7. **Compose rules** (if Compose): state hoisting, side-effect discipline, Modifier rules, derivedStateOf / remember discipline.
8. **Coroutines / async rules:** scope source, exception handling expectation, Dispatchers usage.
9. **Vocabulary:** the 5–15 terms with canonical spelling and definitions.
10. **Testing rules:** what kinds of tests are required for what kinds of changes (e.g., "lifecycle changes require an instrumentation rotation test").
11. **Escalation protocol:** when the AI must stop and ask the human. Examples: "before changing a Room schema", "before modifying signing config", "before adding a permission to the manifest".
12. **Out of scope:** what this rules file does NOT cover (so the AI doesn't infer the absence of a rule means the area is free).

### Step 4 — Write each rule with discipline

Every rule must:

- Be **specific.** "Use viewModelScope for ViewModel-launched coroutines" — not "use coroutines correctly."
- Be **observable.** A reader can decide in <30 seconds whether a code change violates it.
- Be **traced** (for don'ts and required patterns) to an audit finding or an exemplar file.
- Be **terse.** One sentence per rule, occasionally two. The file will be re-read every session by an AI — long prose is friction.

Forbidden rule shapes:
- "Follow Android best practices."
- "Write clean code."
- "Be careful with [X]."
- "Consider [X]."
- Any rule that doesn't trace to evidence in this codebase.

### Step 5 — Honor the size budget

Total rules file: ≤400 lines including section headers and blank lines. If the inventory is bigger, prioritize: every Critical-finding-driven don't makes it in; every High-finding-driven don't makes it in; lower-severity findings get summarized or dropped. The rules file is a high-leverage artifact, not a bug tracker.

### Step 6 — Sanity check against the wall diagnosis

If input 4 (wall diagnosis) was provided:

- The primary mode's rescue should be reflected in the rules file. (A2 lifecycle → lifecycle section is prominent. A8 WebView/Intent → security gates include WebView config check. A12 context rot → vocabulary and required-patterns sections are exhaustive.)
- If the rules file doesn't visibly address the primary mode, the inventory was incomplete. Revise.

### Step 7 — Generate the agent-specific front matter (if applicable)

- **Claude Code:** No required front matter; saved as `CLAUDE.md` at project root or in `.claude/` for global.
- **Cursor:** `.cursorrules` is plain text, no front matter.
- **Codex / generic:** `AGENTS.md` is plain text.
- **Windsurf:** `.windsurfrules`, plain text.

If the agent supports slash commands, suggest 2–3 the team should add (one per common workflow: "/audit", "/fix", "/onboard").

### Step 8 — Emit conflict report and rules file

Two outputs:

1. The rules file itself, ready to commit to the project root.
2. A short conflict / decision log: what was dropped for size, what conflicted with the existing rules file, what was deferred for human decision.

### Step 9 — Verify and output

Run the verification checklist.

---

## Constraints

### Must
- Every hard don't traces to an audit finding (file:line or summary).
- Every required pattern traces to an exemplar file.
- Vocabulary section uses the user's input 6 verbatim for canonical spellings.
- File is ≤400 lines.
- All twelve sections present (in order); empty sections explicitly marked "N/A — codebase does not use [X]".
- Conflicts (audit vs exemplar, new vs existing rules file) flagged before generation.
- Output filename matches input 8's target agent.

### Must Not
- Include generic rules ("follow best practices," "write clean code," "be careful").
- Include rules without a trace to evidence in this codebase.
- Exceed 400 lines.
- Silently drop rules due to size — surface what was dropped.
- Reference Claude-Code-specific tool names inside the rules file unless the target agent IS Claude Code.
- Recommend a rule that contradicts the wall diagnosis's primary mode's rescue.
- Include placeholder text ("fill in here," "[TODO: example]") in the final file.

---

## False-Positive Prevention (MUST follow)

DON'T:
- Derive required patterns from a single exemplar without checking whether the exemplar is itself audit-clean.
- Inflate vocabulary with terms that don't recur in the codebase — pinning a non-recurring term wastes section budget.
- Add a hard don't from a Low-severity finding — those don't justify rules-file weight.
- Recommend a slash command that the project hasn't agreed to maintain.
- Output the rules file before resolving conflicts from step 2.

DO:
- Cap hard don'ts at 25 — beyond that, agents stop reading.
- Cap required patterns at 20.
- Lead each section with the highest-leverage rule.
- When the user's existing rules file (input 7) has good content, preserve it and merge rather than replacing.
- Make the escalation protocol section concrete — name the human(s) or channels to escalate to if the team has them.

---

## Dual-Failure Prevention (QA-20)

HARMFUL failure: Rules file recommends a pattern the audits flagged as risky (because the exemplar was wrong); future AI follows the rule and re-introduces the issue.

UNHELPFUL failure: Rules file is 400 lines of generic Android advice; AI ignores it in practice; vibe-coding wall returns.

Quality check: A senior Android engineer reads the rules file in <5 minutes, agrees every rule is grounded in this codebase, and can predict that an AI following these rules would not produce the patterns the audits found.

---

## Output Format

### Output 1 — Conflict / Decision Log

```markdown
# Rules File Generation Log — [App name] — [Date]

## Inputs Used
- Codebase audit findings: [N]
- Security audit findings: [N]
- Exemplar files: [paths]
- Wall-diagnosis primary mode: [A# / "not provided"]
- Existing rules file: [present + path / absent]
- Vocabulary terms: [N]

## Conflicts Surfaced
- [Conflict 1: exemplar A vs hard don't X — recommendation]
- [Conflict 2: existing rules vs new evidence — recommendation]
- [...]

## Dropped for Size Budget
- [Rule 1 — dropped because: rule N was higher leverage]
- [...]

## Deferred for Human Decision
- [Decision 1: should we forbid pattern Y given a single exemplar uses it?]
- [...]

## Suggested Slash Commands (if applicable)
- /[name] — [purpose]
- [...]
```

### Output 2 — The Rules File

Save to project root as `CLAUDE.md` / `.cursorrules` / `AGENTS.md` / `.windsurfrules` based on input 8.

```markdown
# [App name] — Project Rules

## 1. Project context
[≤8 sentences: what this app is, toolkit, structure pointer.]

## 2. Hard don'ts
- DO NOT [rule]. — _Seen in [file:line] / audit flagged [N] instances._
- DO NOT [rule]. — _Seen in [file:line]._
- [10–25 items.]

## 3. Required patterns
- For [task], use [pattern]. — _See exemplar: [file]._
- For [task], use [pattern]. — _See exemplar: [file]._
- [8–20 items.]

## 4. Lifecycle rules
- Collect Flows with `repeatOnLifecycle(STARTED)`. — _See: [file]._
- Cancel coroutines via `viewModelScope` / `lifecycleScope`; never construct ad-hoc scopes. — _Audit found [N] violations._
- [...]

## 5. Security gates
Before writing code that does X, answer:
- [ ] Does this component need `android:exported="true"`? If yes, what protects it?
- [ ] Is this data sensitive enough to require `EncryptedSharedPreferences`?
- [ ] Does this PendingIntent need `FLAG_IMMUTABLE`? (Always yes on API 31+.)
- [...]

## 6. DI / Hilt rules
[If Hilt; else "N/A — codebase does not use Hilt."]
- `@Singleton` is for [defined scope]; do not bind ViewModels or session data as `@Singleton`.
- [...]

## 7. Compose rules
[If Compose; else "N/A — codebase does not use Compose."]
- State that two composables need to share is hoisted to a ViewModel, not duplicated.
- Side effects use `LaunchedEffect` keyed on the inputs they depend on; never `Unit`.
- [...]

## 8. Coroutines / async rules
- `GlobalScope` is forbidden.
- Top-level coroutines have a `CoroutineExceptionHandler` or explicit `try/catch`.
- I/O uses `Dispatchers.IO`; main-thread I/O is a build-break.
- [...]

## 9. Vocabulary
- **[CanonicalTerm]** — [one-sentence definition].
- **[CanonicalTerm]** — [one-sentence definition].
- [5–15 terms.]

## 10. Testing rules
- Lifecycle changes require an instrumentation rotation + process-death test.
- New permissions require a manifest-assertion test.
- Compose screens with non-trivial state require a Compose UI test.
- [...]

## 11. Escalation protocol
STOP and ask before:
- Changing a Room schema (migration path must be reviewed).
- Modifying signing config or release build configuration.
- Adding a new manifest permission.
- Changing auth or session behavior.
- Touching `network_security_config.xml`.

## 12. Out of scope
This file does not cover:
- [topic — where to look instead]
- [...]
```

---

## Verification

- [ ] Every hard don't traces to an audit finding.
- [ ] Every required pattern traces to an exemplar file.
- [ ] Vocabulary uses input 6 verbatim.
- [ ] File ≤400 lines.
- [ ] All 12 sections present (N/A explicitly noted for unused).
- [ ] Conflicts surfaced in the log BEFORE the rules file.
- [ ] Dropped rules listed in the log.
- [ ] Filename matches target agent (input 8).
- [ ] No generic or placeholder content.

---

## Techniques Used

- **ST-01 (Clear Objective):** Output is a project rules file grounded in this codebase, not a generic Android style guide.
- **ST-02 (Structured Sequential Instructions):** Nine steps drive inventory → conflict detection → structure → discipline → size → sanity → front-matter → emit → verify.
- **ST-03 (Output Format Specification):** Twelve-section fixed structure; the rules file format is the contract for downstream AI sessions.
- **ST-04 (Grounded-in-Evidence):** Every rule traces to a finding, an exemplar, or a vocabulary entry. Generic rules are explicitly refused.
- **CM-02 (Constraint Specification):** Must Not block forbids generic advice and exceeding size budget.
- **CM-04 (Forbidden Patterns Explicit):** Hard don'ts section is a named, prominent block — not buried.
- **RT-05 (Evidence-Based Reasoning):** Step 1 inventory and step 4 discipline force evidence citations for every rule.
- **QA-01 (Self-Verification):** Verification checklist + dual-failure prevention ensures the file is high-leverage rather than aspirational.
