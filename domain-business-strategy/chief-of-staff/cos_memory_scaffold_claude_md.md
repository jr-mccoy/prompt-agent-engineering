---
title: "Author a Personal / Role CLAUDE.md Memory Scaffold"
category: business-strategy/chief-of-staff
description: "Draft a CLAUDE.md (or equivalent persistent-memory file) that captures the user's role, priorities, working style, standing preferences, and authority boundaries — so an AI agent stops re-asking the same context every session."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - ST-03
  - QA-01
difficulty: intermediate
tags:
  - chief-of-staff
  - claude-md
  - memory-scaffold
  - personal-context
  - ai-configuration
updated: "2026-04-20"
related_prompts:
  - domain-engineering-workflows/ai-patterns/ai_pattern_rule_extraction_from_decisions.md
  - domain-business-strategy/chief-of-staff/cos_authority_boundaries.md
  - domain-business-strategy/chief-of-staff/cos_specify_subagent_task.md
---

# Author a Personal / Role CLAUDE.md Memory Scaffold

**Objective:** Produce a concise CLAUDE.md (or equivalent persistent-memory file for another AI tool) that gives an agent the baseline context to work with the user effectively from the first turn: who they are, what they work on, how they like to work, what decisions they've already made, and what the agent is and isn't authorized to do. The scaffold should cut repeated re-contextualizing across sessions.

**When to use:** Setting up a new workspace or project with an AI agent. When the user notices they're re-explaining the same context every session. Rewriting an existing scaffold that has drifted or bloated.

**Audience:** Individual knowledge worker or executive who works alongside an AI agent (Claude Code, ChatGPT, Cursor, custom). The scaffold is authored for the agent to read; the user is the source of truth.

---

## Inputs Required

1. **Role and scope.** Title, function, the specific domain of work this scaffold covers.
2. **Current top 3 priorities**, stated as outcomes not activities.
3. **Standing preferences** the user has noticed themselves repeating to AI agents — format, tone, level of detail, what to do when unsure, when to ask vs proceed.
4. **Known pet peeves and anti-patterns.** Specific AI behaviors the user has had to correct more than twice.
5. **Authority boundaries** — what the agent may do on its own, what requires confirmation, what it must refuse. If the user doesn't know yet, run `cos_authority_boundaries.md` first.
6. **Frequent collaborators / systems** the agent will encounter (names, tools, repos) — only those actually relevant to this scaffold's scope.

Refuse to produce a generic scaffold from inputs 1 and 3 alone. Without 4 and 5, the file becomes ambient advice and stops being enforceable.

---

## Instructions

### Step 1 — Scope the file

One sentence at the top of the draft: what this file is for and what is out of scope. Examples:
- "For work on the customer analytics roadmap. Not for personal scheduling or unrelated projects."
- "For all personal coding projects. Not for work at [Company]."

A scaffold that tries to cover everything becomes ignored. Scope is the constraint that keeps it used.

### Step 2 — Role and current priorities

Three short paragraphs:
- **Role.** One line. Title + scope + decision-making authority in the relevant domain.
- **Priorities right now.** Three outcome statements. Dated. These are the most likely to drift — the scaffold should signal when to update them.
- **What I'm explicitly not prioritizing.** Two or three things the agent might otherwise pull the user into.

### Step 3 — Working preferences

A short list of how the user wants to work with the agent. Keep each bullet operational, not aspirational:
- Output length defaults (terse, thorough, table, prose).
- When to ask clarifying questions vs proceed with an assumption.
- How to handle uncertainty (flag, caveat, or guess and label).
- Reading level / technical depth expected.
- Preferred output format defaults.

If a preference cannot be tested against agent behavior, rewrite it until it can.

### Step 4 — Anti-patterns (specific to the user's experience)

List 3–7 specific behaviors the agent should avoid, each with a one-line reason. These come from the user's actual experience, not a generic checklist. Examples:
- "Don't open with 'Great question.' The user will not read past the salutation."
- "Don't output a multi-page plan when the user asked for a decision."
- "Don't invent company names or product names. If a name is needed, use a placeholder."

Vague anti-patterns become invisible. Specific ones bind.

### Step 5 — Authority boundaries

Short table (or prose if the user prefers) with three columns: **Can do**, **Ask first**, **Never**. Pull directly from the user's answers in `cos_authority_boundaries.md`. Do not invent boundaries.

### Step 6 — Collaborators and systems

List only names/tools/repos the agent will actually encounter in scope. For each:
- Who / what they are, one line.
- What the agent should do when it sees a reference to them (e.g., "check [repo] first for convention before proposing changes").

### Step 7 — Revision plan

Two lines at the bottom:
- **Last updated:** [date].
- **Trigger to revise:** a specific signal that tells the user this file needs updating (e.g., "when priorities change," "after any conversation that ended with 'you should have this in your CLAUDE.md'").

Without a revision trigger, the scaffold drifts silently and gets worse.

---

## Constraints

### Must
- Scope the file explicitly at the top.
- Include dated priorities.
- Keep working preferences operational (testable against agent behavior).
- Ground anti-patterns in the user's real experience.
- Populate authority boundaries from the user's actual answers, not defaults.
- Include a revision trigger.

### Must Not
- Produce a generic "how to use AI" document.
- Exceed 2 pages. A CLAUDE.md that's too long stops being read — by the agent and by the user.
- Include sensitive credentials, PII, or contents that shouldn't live in a repo file.
- Include aspirational preferences the user hasn't actually tested ("I like concise responses" when they keep asking for more detail).
- Add rules the user didn't ask for; flag any optional addition as a question.

---

## False-Positive Prevention

1. **Don't confuse length with rigor.** A one-page scaffold that actually changes agent behavior beats a three-page one the agent averages over.
2. **Don't write preferences the user hasn't verified.** "Use bullet points by default" is only a real preference if they've corrected the agent when it didn't.
3. **Don't bury authority boundaries in prose.** They need to be scannable — the agent reads this file fast.
4. **Don't make the scope too broad.** "Everything I do" is not a scope; it's an opt-out.
5. **Don't skip the revision trigger.** CLAUDE.md files rot fastest at the priorities section.
6. **If the user has no anti-patterns yet,** say so and propose running the scaffold for two weeks before filling in that section. Don't invent.

---

## Output Format

```markdown
# CLAUDE.md — [scope label]

**Scope:** [What this file governs. What it doesn't.]

## Role
[One line: title, function, decision authority in scope.]

## Priorities (as of [date])
1. [Outcome]
2. [Outcome]
3. [Outcome]

**Not prioritizing right now:** [2–3 things.]

## Working preferences
- [Operational preference.]
- [Operational preference.]
- [Operational preference.]

## Anti-patterns to avoid
- **Don't [specific behavior].** [One-line reason.]
- **Don't [specific behavior].** [One-line reason.]

## Authority boundaries
| Can do on its own      | Ask first               | Never                   |
|------------------------|-------------------------|-------------------------|
| [Item]                 | [Item]                  | [Item]                  |

## Collaborators / systems in scope
- **[Name/tool]** — [one-line description]. When you see this: [instruction].

## Revision
- Last updated: [date]
- Revise when: [specific trigger]
```

---

## Verification

- [ ] Scope is stated at the top.
- [ ] Priorities are dated and stated as outcomes.
- [ ] Every preference is testable against agent behavior.
- [ ] Anti-patterns are specific, not generic.
- [ ] Authority boundaries come from the user's input, not defaults.
- [ ] A revision trigger is set.
- [ ] Total length ≤ 2 pages.
