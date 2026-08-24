---
title: "Define Authority Boundaries (Can Do / Ask First / Never)"
category: business-strategy/chief-of-staff
description: "Produce an explicit three-column authority map for a sub-agent (AI, assistant, junior) that names what it may do on its own, what requires confirmation, and what it must refuse — with the reasoning behind each line so edge cases are resolvable."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - QA-01
difficulty: intermediate
tags:
  - chief-of-staff
  - authority
  - delegation
  - guardrails
  - subagent
updated: "2026-04-20"
related_prompts:
  - domain-business-strategy/chief-of-staff/cos_specify_subagent_task.md
  - domain-business-strategy/chief-of-staff/cos_memory_scaffold_claude_md.md
  - domain-prompt-engineering/delegation/delegation_tool_vs_colleague_decision.md
---

# Define Authority Boundaries (Can Do / Ask First / Never)

**Objective:** Produce a crisp three-column authority map for a specific sub-agent (AI agent, executive assistant, junior, contractor) that answers: what may it do on its own, what must it ask about first, and what must it refuse. Each line is written with enough reasoning that a gray-zone case — something the sub-agent didn't see before — can be resolved by the user and the sub-agent applying the same logic.

**When to use:** When bringing on a new sub-agent. When an existing sub-agent has made a move that felt out of scope (even if it ended well). When a CLAUDE.md or role doc is being drafted and the authority section needs real content, not boilerplate.

**Audience:** Individual knowledge worker or executive who delegates to a sub-agent. Applies equally to AI agents and human sub-agents — the frame is the same; the concrete rules will differ.

---

## Inputs Required

1. **The sub-agent.** AI (which tool and tool access) or a named human role.
2. **The scope of their work.** Specific domain, not "everything."
3. **Known incidents.** Any past events where authority felt ambiguous — what happened, what outcome, what the user wished had happened instead.
4. **Reversibility map.** For the domain, what actions are reversible in under a day, what takes longer, what is not practically reversible.
5. **External constraints.** Legal, compliance, relationship stakes (e.g., anything touching a specific customer, an auditor, a regulator).

If the user cannot provide inputs 2 and 4, refuse to produce the map. Authority questions are answered by reversibility — without that, rules become arbitrary.

---

## Instructions

### Step 1 — Enumerate action types in scope

List the kinds of actions the sub-agent might realistically take in their domain. Categories to consider:
- Communicating externally (who, on what channels).
- Committing resources (time, money, other people's attention).
- Changing state in systems (files, databases, calendars, tickets).
- Making representations on the user's behalf (opinions, promises, signatures).
- Surfacing vs resolving ambiguity.

Aim for 10–20 concrete action types, not abstract categories.

### Step 2 — Score each action by reversibility and blast radius

For each action, note two things:
- **Reversibility:** instant / hours / days / not practically reversible.
- **Blast radius:** self only / team / customer / company-wide / external public.

These two together drive column placement.

### Step 3 — Assign to column

Default rules:
- **Can do on its own:** reversible in under a day and blast radius ≤ team.
- **Ask first:** either harder-than-a-day to reverse or blast radius beyond team.
- **Never:** not practically reversible, or against policy / legal / relationship stakes, or requires a human signature.

These are defaults — the user can override. Every override should be explained in one line.

### Step 4 — Write the rule with reasoning

For each line, write:
- The rule (verb-first).
- The reason (reversibility, blast radius, policy, or user preference).
- The gray-zone test: "If unsure whether a case fits this rule, apply [this heuristic]."

The gray-zone test is the part that makes the map useful in practice. Without it, the sub-agent guesses on every edge case.

### Step 5 — Handle escalation paths

For the **Ask first** column, specify how the sub-agent asks:
- Channel (synchronous DM, email, task comment, new chat).
- What information to include (action proposed, reason, reversibility, alternatives).
- Expected response time.
- What to do if the user is unavailable (wait vs proceed vs default action).

### Step 6 — Pressure-test with past incidents

Take each input-3 incident and walk it through the map. Does the map's rule cover it? If not, the map has a gap — add a rule or sharpen an existing one. Do not write a rule targeted at a single incident; generalize.

### Step 7 — Expiry and review

Set a review date. Authority maps drift — the sub-agent gets more capable (especially AI sub-agents), the domain changes, new action types emerge. Default: 90 days. Name the trigger that would move the review earlier.

---

## Constraints

### Must
- Ground column assignments in reversibility and blast radius.
- Include reasoning and a gray-zone test for every line.
- Specify how the sub-agent asks when in the middle column.
- Walk past incidents through the map.
- Set a review date.

### Must Not
- Write columns as pure lists without reasoning.
- Use vague rules ("be careful with money"). Specify the threshold.
- Invent incidents or policy constraints the user didn't supply.
- Recommend a sub-agent have authority the user doesn't have.
- Default the middle column to "ask about everything" — that eliminates the point of delegation.

---

## False-Positive Prevention

1. **Don't conflate capability with authority.** An AI agent may be capable of sending emails; the question is whether it should. Capability is upstream of authority, not a substitute.
2. **Don't let "Never" bloat.** Every line in Never should be traceable to reversibility, policy, or signature. Boilerplate in Never makes the useful rules harder to find.
3. **Don't write rules targeted at one incident.** Generalize, or the map doesn't cover the next edge case.
4. **Don't skip the gray-zone test.** The test is more valuable than the rule itself over time.
5. **Don't forget the escalation path.** A rule that says "ask first" with no "how to ask" becomes a rule that says "don't do this" in practice.
6. **If the user wants broad authority but low reversibility,** flag it rather than write the rule. Broad authority on irreversible actions is the most common delegation failure.

---

## Output Format

```
# Authority map — [sub-agent] in scope: [domain]

## Can do on its own
| Rule (verb-first) | Reason (reversibility / blast radius / preference) | Gray-zone test |
|-------------------|----------------------------------------------------|----------------|
| [Rule]            | [Reason]                                           | [Heuristic]    |

## Ask first
| Rule | Reason | Gray-zone test | How to ask (channel, info, timeout, default-if-no-answer) |
|------|--------|----------------|-----------------------------------------------------------|
| [Rule] | [Reason] | [Heuristic] | [Specifics] |

## Never
| Rule | Reason (irreversible / policy / signature / other) |
|------|----------------------------------------------------|
| [Rule] | [Reason] |

## Incidents walked through
- [Past incident] → Rule that applies: [which] → Expected outcome under map: [what would happen now].

## Review
- Next review date: [date, default +90 days]
- Earlier-review trigger: [specific signal]
```

---

## Verification

- [ ] Every line has a reason tied to reversibility, blast radius, policy, or stated preference.
- [ ] Every line has a gray-zone test.
- [ ] Ask-first rules specify channel, info required, timeout, and default-if-no-answer.
- [ ] Past incidents have been walked through.
- [ ] Review date is set with an earlier-trigger specified.
- [ ] Map is scannable on one page.
