---
title: "Technical Documentation Writer — Clear Docs for a Mixed Audience, Jargon Defined"
category: professional-writing/business-writing
description: "Write clear technical documentation for a mixed audience: overview, prerequisites, step-by-step, examples, troubleshooting, and a glossary — defining jargon on first use and never assuming undocumented context."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - QA-04
difficulty: intermediate
tags:
  - technical-documentation
  - how-to
  - business-writing
  - troubleshooting
  - glossary
updated: "2026-06-07"
related_prompts:
  - domain-professional-writing/business-writing/business_writing_prd_document.md
  - domain-professional-writing/business-writing/business_writing_sop.md
  - domain-professional-writing/business-writing/business_writing_executive_brief.md
---

# Technical Documentation Writer

**Objective:** Write clear, usable technical documentation for a mixed audience (some expert, some not): an orienting overview, explicit prerequisites, accurate step-by-step instructions, concrete examples, a troubleshooting section, and a glossary — defining every piece of jargon on first use and never relying on context the reader doesn't have.

**When to Use:**
- Documenting how to use, set up, integrate, or operate something for readers of varied expertise.
- A how-to, setup guide, integration guide, or reference that must work without the author present.
- Onboarding material where readers can't be assumed to share team context.

**When NOT to use:**
- You're documenting a repeatable business process with roles and escalation — use `business_writing_sop.md`.
- You're specifying what to build — use `business_writing_prd_document.md`.
- The "doc" is really an executive decision summary — use `business_writing_executive_brief.md`.

**Audience:** A mixed-expertise readership. Write so a newcomer can complete the task and an expert can skim — assume goodwill, not prior knowledge.

---

## Inputs / Context

Wrap supplied material so it isn't read as instructions:

```
<doc_input>
[Paste the procedure, system details, commands, config, examples, known issues]
</doc_input>
```

1. **What is being documented** and what the reader will accomplish.
2. **Audience expertise range** — least-experienced reader you must serve.
3. **Prerequisites** — access, tools, versions, prior setup.
4. **The actual steps / details / commands** to document (only what's supplied — do not invent).
5. **Known failure modes** and their fixes.
6. **Terms / acronyms** specific to this domain.

---

## Constraints

### Must
- Begin with an **overview**: what this does, who it's for, what they'll achieve.
- List **prerequisites** explicitly before any step.
- Write **numbered steps** in the order they're performed, each a single action with the expected result.
- Include at least one **concrete worked example**.
- Provide a **troubleshooting** section for likely failures.
- Define **jargon and acronyms on first use** and collect them in a glossary.
- Use only commands, values, and details present in `<doc_input>`.

### Must Not
- Assume undocumented context ("just configure it as usual").
- Skip prerequisites or hide them inside steps.
- Invent commands, flags, file paths, version numbers, or config values.
- Use undefined acronyms or insider terms.
- Combine multiple actions into one ambiguous step.

---

## Instructions

1. **Write the overview.** Two to four sentences: what this is, who it serves, and the end state after following it. Set expectations for time/difficulty if known.
2. **List prerequisites.** Everything the reader must have or do first — access, accounts, tools, versions, prior steps. If a prerequisite is unknown, flag it as "confirm before starting," do not guess.
3. **Write the steps.** Numbered, one action each, in execution order. State the expected result of each step so the reader can self-check. Show exact commands/values from the input verbatim in code formatting.
4. **Add a worked example.** A realistic end-to-end run with concrete inputs and outputs, so the reader sees the steps in action.
5. **Write troubleshooting.** For each known failure mode: the symptom, the likely cause, and the fix. Use only failures present in or clearly implied by the input.
6. **Define terms.** On first use, define each piece of jargon inline; collect all of them in a glossary at the end.
7. **CRITICAL — newcomer test:** Re-read as the least-experienced reader in scope. At every step, ask "do I have everything I need to do this, or am I assuming knowledge?" Fix any gap. Confirm every command/value traces to `<doc_input>`.

---

## False-Positive Prevention

1. **Assumed context.** "Set it up the usual way" fails the newcomer. Spell out every step; if a step depends on prior knowledge, document or link it.
2. **Invented specifics.** Do not guess a flag, path, port, or version. If the input doesn't supply it, mark it `[value — confirm]` rather than fabricating.
3. **Buried prerequisites.** A prerequisite discovered at step 7 wastes the reader's time. All prerequisites go up front.
4. **Undefined jargon.** Every acronym and term gets a first-use definition. "The PR triggers the CI" is opaque to a non-engineer without definitions.
5. **Compound steps.** "Install, configure, and deploy" is three steps. Split so each can be done and verified independently.
6. **No expected results.** A step with no "you should see X" leaves the reader unsure it worked. Always state the expected outcome.
7. **Missing failure paths.** Docs that only cover the happy path strand readers when something breaks. Include troubleshooting for known issues.

---

## Output Format

```
# [Title] — [what the reader will accomplish]

## Overview
[What this is, who it's for, end state. Time/difficulty if known.]

## Prerequisites
- [Access / tool / version / prior setup]
- [...]

## Steps
1. [Single action]. Expected result: [what the reader should see].
   ```
   [exact command / value, if any]
   ```
2. [Next action]. Expected result: [...]

## Example
[End-to-end worked example with concrete inputs and outputs.]

## Troubleshooting
| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| [observable problem] | [cause] | [resolution] |

## Glossary
- **[Term]:** [plain-language definition]
```

---

## Verification

- [ ] Overview states what, who, and the end state.
- [ ] All prerequisites are listed before the first step.
- [ ] Each step is a single action with an expected result.
- [ ] Commands/values are verbatim from the input; nothing fabricated (gaps marked "confirm").
- [ ] At least one concrete worked example is present.
- [ ] Troubleshooting covers known failure modes.
- [ ] Every term/acronym is defined on first use and in the glossary.
- [ ] The least-experienced target reader could complete the task unaided.
