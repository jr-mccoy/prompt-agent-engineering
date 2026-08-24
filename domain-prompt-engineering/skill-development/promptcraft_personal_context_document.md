---
title: "Build a Reusable Personal Context Document"
category: prompt-engineering/skill-development
description: "Produce a single, reusable context document the user pastes into new chats or loads as persistent memory — capturing role, active projects, tools, constraints, vocabulary, and the specific defaults the user doesn't want to re-type every session. Built from evidence of what the user actually explains on every chat, not from an aspirational bio."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - QA-01
difficulty: intermediate
tags:
  - skill-development
  - context-management
  - personal-context
  - reusable
  - persistent-memory
updated: "2026-04-20"
related_prompts:
  - domain-business-strategy/chief-of-staff/cos_memory_scaffold_claude_md.md
  - domain-prompt-engineering/escape-median/escapemedian_bootstrap_instruction_file.md
  - domain-prompt-engineering/skill-development/promptcraft_rewrite_vague_ask.md
  - domain-prompt-engineering/skill-development/promptcraft_constraint_architecture_design.md
---

# Build a Reusable Personal Context Document

**Objective:** Produce a single document — ≤2 pages — that the user can paste into a new chat or load as persistent memory so the model knows who they are, what they work on, what tools they use, what vocabulary they use, and what defaults they don't want to re-specify. The document is built from evidence of what the user actually explains again and again at the start of chats, not from an aspirational self-description.

**When to use:** The user has noticed they start every chat by re-typing the same three paragraphs of background. Or: the user runs AI-assisted work across consistent projects and wants the model to stop asking questions they've already answered ten times.

**Audience:** Individuals doing consistent AI work across a stable role, project set, or workflow. Not for users whose work is highly varied — one context document can't cover wildly different domains.

**Distinction from other context tools:**
- `cos_memory_scaffold_claude_md.md` builds a CLAUDE.md for a *role* or chief-of-staff cadence. It focuses on working rhythm and authority boundaries.
- `escapemedian_bootstrap_instruction_file.md` builds an instruction file from *corrections* — what the user has pushed back on. That's about model preferences.
- This prompt builds a *context* document — who the user is, what they're working on. The three layer together; don't merge them.

---

## Inputs Required

1. **5+ recent chat openers.** Real, pasted. The first 1–3 messages of 5+ recent chats. This is where the user's repeated context shows up.
2. **The user's one-sentence role or working identity.** ("Solo founder, B2B SaaS, 8-person team." "Staff engineer at mid-sized fintech, platform team." "Freelance illustrator specializing in kids' books.")
3. **Active projects (2–6).** Names, one-line descriptions, status.
4. **Tools the user relies on that the model keeps getting wrong.** ("I use Linear, not Jira." "Python 3.11, not 3.9." "Figma Dev Mode, not Zeplin.")
5. **Vocabulary the user uses that the model misreads.** ("When I say 'deal,' I mean 'signed contract,' not 'prospect.'" "We use 'platform' to mean the infra team, not the product.")
6. **Anti-context** — things the model keeps assuming that aren't true of the user. ("I'm not at a FAANG company." "I don't have QA." "I'm not American.")

Refuse to build a context document from a bio or a LinkedIn summary. The value is in the specific, evidence-grounded repetition the user keeps typing. A polished bio has the opposite of what a context document needs.

---

## Instructions

### Step 1 — Extract the repeated pattern

From the 5+ chat openers, list every piece of context the user re-typed more than once. These are the load-bearing elements. If the user re-explained what Linear is every time — that's a candidate. If they only said it once across 5 chats — probably not worth putting in.

Threshold: if it showed up in ≥3 of 5 chats, it's in; if it showed up in 1, it's out; if 2, it's a candidate for confirmation.

### Step 2 — Sort into the four layers

1. **Identity.** One paragraph. Role, company size, domain, a single sentence of what makes the work non-generic.
2. **Active projects.** Up to six, each one line. Name → what it is → status.
3. **Stack and tools.** Bullet list. Name specific tool + version when version matters (Python 3.11). Include things the model gets wrong when it assumes (e.g., user is on macOS, not Linux).
4. **Vocabulary.** Two columns: the term → what the user means by it (when it differs from the default meaning).

A fifth layer, **Anti-context**, sits at the bottom. ("Assume none of the following unless I say so: …")

### Step 3 — Length-check each layer

- Identity: ≤ 5 sentences.
- Projects: ≤ 6 items, one line each.
- Stack: ≤ 15 items. If the list is longer, split by project.
- Vocabulary: ≤ 10 terms. More than that, the document becomes a glossary and the model stops reading it.
- Anti-context: ≤ 5 items.

If any layer busts its cap, cut. The context document is competing for the model's attention against the actual task; a bloated document gets skimmed.

### Step 4 — Add a version + expiry

Projects change. Stacks change. A context document without a "last updated" and a revision trigger silently rots. Include:
- `Last updated: [date]`
- `Revise when: [specific trigger — e.g., end of a project, tool migration, role change]`

### Step 5 — Mark the load-path

Two usage modes:
- **Paste mode.** User pastes the document at the top of a new chat. Mark sections the user can trim if the task only needs some of them.
- **Persistent mode.** User loads this into CLAUDE.md, ChatGPT custom instructions, or a project-level context. Note any sensitive content that shouldn't live in a persistent file (e.g., client names if the file syncs to a public repo).

### Step 6 — Flag gaps

If the evidence didn't produce content for a layer, don't invent it. Leave the layer empty with a note: "No repeated pattern in the 5 openers; revisit after 5 more chats."

### Step 7 — Compose and stop

Target length: 1–2 pages. If the draft exceeds 2 pages, cut the lowest-signal layer first (usually Stack or Vocabulary, whichever is longer).

---

## Constraints

### Must
- Be built from ≥5 real chat openers, not from a bio.
- Include a `last updated` and a revision trigger.
- Respect per-layer length caps.
- Flag candidate-but-uncertain items separately from confirmed items.
- Note sensitive content if the doc will live in persistent memory.

### Must Not
- Exceed 2 pages.
- Include information the model can infer from the task itself. (If every task names the company, don't add it to context — it's duplication.)
- Invent projects, tools, or vocabulary the user didn't supply.
- Copy from a LinkedIn bio or resume. Those optimize for impressiveness; context documents optimize for usability.
- Merge with an instruction-file (preferences) or CLAUDE.md (role + authority). Layer; don't merge.

---

## False-Positive Prevention

1. **Bio drift.** Context documents drift toward bios because bios are what users are used to writing. A bio says what the user is good at; a context document says what the model needs to know to work with them. Check: does every line help the model produce better output, or does it just describe the user?
2. **Stale project list.** Projects change every few weeks. If the revision trigger is "quarterly," the projects section will be 80% stale at month 2. Tighten the trigger for projects specifically to "when a project ends or a new one starts."
3. **Aspirational vocabulary.** Adding terms the user wishes the model would use, rather than terms the user actually uses, makes the document a style guide for imagined work. Cut anything that didn't show up in the 5 openers.
4. **Sensitive info in persistent mode.** Client names, internal project codenames, and financial details shouldn't live in a CLAUDE.md committed to a repo. Separate paste-mode and persistent-mode versions if needed.
5. **Over-specification of stack.** Listing 40 tools produces skimming. Keep only tools the model has been wrong about or that matter to nearly every task.
6. **Anti-context inflation.** Anti-context is powerful but loses force if it's a dozen items. Cap at 5.
7. **No evidence pass.** A context document written from memory (rather than from 5 real openers) captures what the user *thinks* they explain, not what they actually explain. Always run Step 1.

---

## Output Format

```markdown
## Evidence audit
- Chat openers reviewed: [N] (floor: 5)
- Repeated elements (≥3 of 5): [...]
- Candidate elements (2 of 5): [...]
- Load mode: [paste | persistent | both]

---

## Personal context document — first draft

```markdown
# Personal context — [user label]

**Last updated:** [date]
**Revise when:** [specific trigger]

## Identity
[≤ 5 sentences.]

## Active projects
- **[Name]** — [one line: what + status]
- **[Name]** — [one line: what + status]

## Stack and tools (where defaults get it wrong)
- [Tool + version or specifier]
- [...]

## Vocabulary
| Term | What I mean by it |
|---|---|
| [...] | [...] |

## Anti-context (assume none of these unless I say so)
- [...]
```

---

## Gaps flagged
- [Layer / element] — no evidence yet. Revisit after [N] more chats.

## Usage notes
- Paste mode: trim [sections] for tasks that don't need them.
- Persistent mode: [sensitive content warnings, if any].
```

---

## Verification

- [ ] ≥5 real chat openers were reviewed.
- [ ] Repeated elements (≥3 of 5) were promoted; 1-of-5 elements were dropped.
- [ ] Every line serves the model, not the user's self-description.
- [ ] Document is ≤ 2 pages.
- [ ] `Last updated` and revision trigger are present.
- [ ] Sensitive-content warnings are present for persistent mode, if applicable.
- [ ] No merger with instruction-file or role-scaffold content.
