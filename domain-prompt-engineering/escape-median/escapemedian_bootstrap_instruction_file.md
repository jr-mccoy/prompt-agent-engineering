---
title: "Bootstrap a Personal Instruction File from Observed Preferences"
category: prompt-engineering/escape-median
description: "Build a first-draft personal instruction file (CLAUDE.md, custom-instructions block, or equivalent) from evidence — corrections the user has accumulated, rules they've compounded in-session, maps of model defaults they've pushed against — instead of from a blank page full of aspirational preferences."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - QA-01
difficulty: intermediate
tags:
  - escape-median
  - claude-md
  - instruction-file
  - personalization
  - bootstrap
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/escape-median/escapemedian_correction_compounder.md
  - domain-prompt-engineering/escape-median/escapemedian_default_position_mapper.md
  - domain-prompt-engineering/escape-median/escapemedian_instruction_sharpener.md
  - domain-business-strategy/chief-of-staff/cos_memory_scaffold_claude_md.md
---

# Bootstrap a Personal Instruction File from Observed Preferences

**Objective:** Produce a first-draft personal instruction file (a CLAUDE.md, a ChatGPT "custom instructions" block, a Gemini system prompt, or equivalent persistent-memory file) seeded entirely from the user's *observed* preferences — corrections they've made, rules they've compounded, defaults they've pushed against — rather than from a blank page of guesses. The bootstrap is deliberately minimal; it prefers leaving sections empty to filling them with preferences the user hasn't actually tested.

**When to use:** The user has worked with a model long enough to have real corrections and real preferences, and wants to stop re-typing them each session. Especially useful right after running `escapemedian_correction_compounder.md` across a few sessions, or after mapping defaults on 2–3 topics via `escapemedian_default_position_mapper.md`.

**Audience:** Individual users setting up persistent memory for Claude Code, ChatGPT, Cursor, or similar tools. Not for teams — team-level instruction files need extra governance and live under `goal-orientation/`.

---

## Inputs Required

1. **Correction clusters** — rules that have already been extracted from at least two sessions via `escapemedian_correction_compounder.md` (or an equivalent summary). Ideally 5–15 rules.
2. **Default maps** for 1–3 topics the user repeatedly works on (optional but strongly useful).
3. **The model(s)** the instruction file will govern. Different tools load instruction files differently.
4. **Scope of the file.** One of: general across all work, role-scoped, project-scoped, or task-scoped. If the user can't pick, start narrow.
5. **Any non-negotiables** the user wants enforced regardless of task.

Refuse to generate an instruction file from aspirational preferences alone ("I'd like concise answers, I'd like it to be proactive"). An instruction file built from what the user *wishes* they wanted produces drift the first time real work tests it. Use corrections and observed behavior.

---

## Instructions

### Step 1 — Verify there's enough evidence

Count:
- Correction-derived rules: should be ≥5. Below that, the file will be too thin to matter.
- Default maps: at least one, preferably three.
- Sessions represented: at least two. A single session over-specifies to one task.

If evidence is thin, stop. Recommend two more weeks of active work with `escapemedian_correction_compounder.md` at the end of each session before bootstrapping.

### Step 2 — Scope the file

Write one sentence at the top of the draft answering: what does this file govern, and what is explicitly out of scope? Scoping examples:
- "For all my personal AI coding work. Not for work at [company], which has separate instructions."
- "For research-and-writing sessions. Not for quick fact lookups."

Without scope, instruction files get pulled in where they don't fit and the user ends up deleting them. Narrow scope = long-lived file.

### Step 3 — Translate rules into the instruction file sections

Group the rules into the file's standard sections. Suggested minimal structure:

- **Role / who I am.** One paragraph, only if the user's work has a clear role.
- **Working preferences.** The rules from correction clusters — length defaults, format defaults, hedge suppression, stance preference, etc.
- **Stances on topics I return to.** Derived from default maps: "On X, my prior is Y — don't balance, argue against Y." Only include topics where the user has a real, tested prior.
- **Anti-patterns.** Specific model behaviors the user has corrected more than twice. Name them explicitly.
- **Non-negotiables.** User-supplied. Kept verbatim.
- **Authority / when to ask.** How the model should handle uncertainty — flag, caveat, guess-and-label, proceed.

Every section is optional except scope and revision trigger. Better an empty section than a filler one.

### Step 4 — Translate each rule into testable form

A rule the model can't check doesn't belong in the file. Rewrite each rule so a single output could be judged against it. Examples of transformations:

- "Be concise" → "Cap answers at 150 words unless I ask for more."
- "Don't hedge" → "Don't include the phrases 'it depends,' 'consider your,' or 'there's no one right answer.' If you genuinely don't know, say 'I don't know' and stop."
- "Be proactive" → "After answering, if you see something the question missed, flag it in one line. No full extra section."
- "Know my context" → [Delete. Replace with specific rules that encode the context, not a meta-rule to know it.]

Testability is what makes the file actually govern behavior.

### Step 5 — Draft the file

Compose the instruction file. Target length: ~1 page for ChatGPT custom instructions, ≤2 pages for CLAUDE.md. Longer files average over themselves.

### Step 6 — Add the revision trigger

One line: what signal tells the user to revisit the file. Examples:
- "When I correct the same thing twice in one session."
- "After any model version change."
- "Quarterly."

Without a trigger, files rot silently.

### Step 7 — Flag gaps for future filling

If certain sections have weak evidence (e.g., no default map yet for a topic the user works on constantly), mark them as gaps with a pointer to the right next step:
- "No default map yet for [topic]. Run `escapemedian_default_position_mapper.md` next time this topic comes up."
- "Authority / when-to-ask is empty. Run `cos_authority_boundaries.md` if this matters."

Gaps are better than invented content.

### Step 8 — Prescribe the first two weeks of use

An instruction file isn't finished at first draft. It's finished when two weeks of real use hasn't produced a correction the file didn't cover. State this to the user so they don't treat the bootstrap as final.

---

## Constraints

### Must
- Require ≥5 correction-derived rules and ≥1 default map before generating.
- Scope the file at the top.
- Rewrite every rule into testable form.
- Keep non-negotiables verbatim from user input.
- Leave sections empty rather than fill with aspirational content.
- Include a revision trigger.
- Flag gaps with pointers to the right prompt for filling them.

### Must Not
- Invent preferences from generic "good AI defaults."
- Exceed 2 pages. Length is the enemy of adherence.
- Include credentials, PII, or anything sensitive — this file may live in a repo.
- Copy language from CLAUDE.md examples you've seen; use the user's own correction language.
- Treat the bootstrap as final. It's a first draft.

---

## False-Positive Prevention

1. **Aspirational preferences are the #1 failure mode.** "I like concise answers" from a user who keeps asking follow-ups for more detail is aspirational, not real. Cross-check stated preferences against corrections.
2. **A file full of rules is not a file that governs behavior.** Past ~12 rules, the model averages across them. Cut aggressively. The five most load-bearing rules outperform fifteen mediocre ones.
3. **Stance-on-topic entries age quickly.** Priors change. Date them and mark the revision trigger accordingly.
4. **Don't encode anti-patterns that only happened once.** Anti-patterns need evidence of repetition. Put single-instance corrections in a "watch" list, not the file.
5. **Scope creep kills files.** If the user has 25 rules for general work and 15 more for one specific project, don't merge them. Use a task-scoped or project-scoped file for the 15.
6. **If the user has no corrections to draw from,** they aren't ready for this prompt. They're ready for `escapemedian_instruction_sharpener.md` on specific prompts.
7. **Promoting a rule the user didn't want promoted is a trust break.** For each rule, confirm the user wants it in the file before including it.

---

## Output Format

```markdown
## Evidence audit
- Correction-derived rules supplied: [N] (threshold: 5)
- Default maps supplied: [N] (threshold: 1)
- Sessions represented: [N] (threshold: 2)
- [Proceed / stop and gather more evidence.]

## Scope
[One sentence. What this file governs, what it doesn't.]

## Rule translations (from correction clusters → testable rules)
| Original correction pattern | Testable rule in file |
|-----------------------------|-----------------------|
| [...] | [...] |

---

## Instruction file (first draft)

```markdown
# [CLAUDE.md | Custom Instructions] — [scope label]

**Scope:** [one sentence]

## Role
[One paragraph, only if the user's work has a clear role.]

## Working preferences
- [Testable rule from corrections.]
- [Testable rule from corrections.]

## Stances on topics I return to
- **[Topic]:** My prior is [...]. Don't balance; argue against it.

## Anti-patterns
- **Don't [specific corrected behavior].** [One-line reason.]

## Non-negotiables
- [User-supplied, verbatim.]

## When you don't have enough information
[Ask / flag / proceed with labeled assumption — one rule.]

## Revision
- Last updated: [date]
- Revise when: [specific signal]
```

## Gaps flagged for future filling
- [Section / topic]: [pointer to the right next prompt].

## First two weeks
Treat this as a first draft. For the next two weeks, run
`escapemedian_correction_compounder.md` at the end of each working
session. If a correction wasn't already covered by this file, update
the file. The file is "done" when two clean weeks pass without
updates.
```

---

## Verification

- [ ] Evidence thresholds were checked before drafting.
- [ ] Scope is stated at the top.
- [ ] Every rule is testable against a single output.
- [ ] File length ≤ 2 pages.
- [ ] Non-negotiables are verbatim from user input.
- [ ] Empty sections were left empty rather than filled.
- [ ] Gaps are flagged with pointers to the right follow-up prompt.
- [ ] A revision trigger is set.
