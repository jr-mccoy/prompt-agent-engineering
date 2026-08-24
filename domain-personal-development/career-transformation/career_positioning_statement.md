---
title: "Build a Positioning Statement From Evidence of Past Wins"
category: personal-development/career-transformation
description: "Derive a sharp professional positioning statement — who you help, with what specific problem, and why you over alternatives — from evidence of the user's actual past wins and the pattern in who sought them out. Refuses generic personal-brand language and adjective soup."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DD-02
  - QA-12
difficulty: intermediate
tags:
  - career
  - positioning
  - professional-brand
  - differentiation
  - evidence
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/career-transformation/career_residual_skills_inventory.md
  - domain-personal-development/career-transformation/career_ai_era_skill_moat.md
  - domain-personal-development/career-transformation/career_internal_vs_external_move.md
  - domain-personal-development/prompts/identity/identity_taste_development.md
  - domain-personal-development/major-decisions/personal_career_offer_evaluation.md
---

# Build a Positioning Statement From Evidence of Past Wins

**Objective:** Produce one sharp positioning statement — *who* the user helps, with *what specific problem*, and *why them* over the alternatives — grounded entirely in the pattern across their real past wins and who actually sought them out. Not a personal-brand slogan, not adjective soup.

**When to use:** The user is preparing for a job search, an internal pitch, a consulting/freelance shift, a networking push, or a promotion case, and needs a crisp, defensible answer to "what do you do / why you." Also when the user's current self-description is generic ("I'm a strategic operator who drives impact") and isn't landing. Not for: writing a full resume or LinkedIn profile (this produces the positioning core those hang off of).

**Audience:** An individual positioning themselves. Not for branding a company or product, and not clinical.

---

## Inputs Required

1. **Five to eight real wins from the last 3 years.** Each as: *situation → what the user specifically did → the concrete result.* "Concrete result" means an outcome someone else cared about, not effort. Reject wins with no result.
2. **Who sought the user out, and for what.** The last several times someone came *to* the user — for advice, to hire them, to pull them onto something, to unblock them — who were they and what did they want? This reveals the market's revealed demand.
3. **The problem behind the wins.** In the user's words, what kind of problem keeps recurring across the wins? If they can't name it, that's fine — the prompt derives it.
4. **The alternatives.** Who or what does the audience use *instead* of the user for this kind of problem (other people, agencies, tools, doing nothing)?
5. **The target audience for this statement.** Who is the statement for — a specific hiring market, an internal exec, a client segment? Positioning is audience-relative; a generic statement is a failed statement.

If the user supplies fewer than 4 wins *with concrete results*, refuse and ask for more. Positioning derived from too few data points is just an aspiration.

---

## Instructions

### Step 1 — Extract the win pattern

Read the wins (input 1) and the inbound demand (input 2) together. Find the **repeating problem-type** — the kind of situation the user is pulled into again and again. Name it concretely (e.g., "untangling a stalled cross-team launch," "turning a vague exec ask into a shippable spec," "rescuing a data pipeline nobody understands"). A pattern must appear in at least **three** wins or inbound requests to count. One-offs are noise.

### Step 2 — Name the audience and the stakes

From input 5 and the wins, name *who has this problem* and *why it hurts them* — the cost of the problem going unsolved. Positioning lands on the pain, not on the user's process.

### Step 3 — Establish the "why you"

The differentiator must come from the evidence, not from adjectives. Derive it from one of:
- **A rare combination** the wins prove (e.g., "deep in the domain *and* can ship code" — shown by wins X and Y).
- **A track record** on the specific problem-type (e.g., "did this five times, four landed").
- **A scarce input** the user controls (a relationship, a body of context, a hard-won model).

Test it against input 4: the "why you" is only real if it's a reason to pick the user *over the named alternatives*. If it isn't, it's not a differentiator — discard it and try another.

### Step 4 — Draft the statement in a fixed shape

Fill this frame, then strip every word that isn't load-bearing:

> **I help [specific audience] [solve a specific recurring problem] so they [the concrete stake]. Unlike [the alternative], I [evidence-backed why-you].**

The statement must be sayable out loud in one breath. If it needs two sentences of qualification, it isn't sharp yet.

### Step 5 — Kill the generic version

Write out the *generic* version the user would otherwise default to (the adjective-soup one), side by side with the sharp one, and name the specific words that were doing no work ("strategic," "results-driven," "passionate," "dynamic"). This makes the sharpening visible and repeatable.

### Step 6 — Attach proof and one deployment action

- Attach the **two strongest wins** as the proof points that back the statement — these are what the user cites when challenged.
- Name **one** place to deploy the statement this week: rewrite a LinkedIn headline, open a specific conversation, lead a specific application with it. Physical and bounded.

---

## Constraints

### Must
- Derive the problem-type from a pattern of ≥ 3 wins/inbound requests.
- State the audience specifically; positioning is audience-relative.
- Back the "why you" with evidence and test it against the named alternatives.
- Produce exactly one statement in the fixed frame, sayable in one breath.
- Attach two proof wins and one deployment action.

### Must Not
- Use adjective-brand language (strategic, results-driven, passionate, visionary, dynamic, thought leader) in the final statement.
- Position the user against "everyone" — require named alternatives.
- Produce three positioning options and let the user choose. Converge on one.
- Invent wins, inflate results, or claim a differentiator the wins don't support.
- Turn this into a values/mission exercise. Positioning is about a buyer's problem, not the user's purpose.

### Must Not (anti-moralizing)
- Congratulate the user on their wins or cheerlead the brand. Extract the pattern and stop.

---

## False-Positive Prevention

1. **Effort is not a win.** "I worked incredibly hard on X" with no outcome someone valued is not evidence for positioning. Require a concrete result.
2. **Inbound demand beats self-perception.** If the user *wants* to be positioned as a strategist but everyone comes to them to fix broken things, the evidence says operator-fixer. Position on the revealed demand, not the aspiration — and name the gap if it exists.
3. **A differentiator that isn't scarce is a table stake.** "I'm reliable and communicate well" differentiates against no one. If the alternatives also have it, it's not a why-you.
4. **Audience-less positioning fails.** A statement that tries to appeal to every possible employer/client appeals to none. If the user resists narrowing the audience, that resistance is the finding.
5. **Don't let the frame hide vagueness.** A statement can fit the template and still be generic ("I help companies grow by driving impact"). Force specificity on each blank; reject filler that survives the frame.
6. **Recency of wins matters.** A brilliant win from 6 years ago in a domain the user left is weak positioning evidence today. Weight recent, relevant wins.

---

## Output Format

```
## The recurring problem you get pulled into
[Named problem-type] — appears in wins/requests: [#, #, #]

## Audience and stakes
- **Audience:** [specific]
- **What it costs them:** [the pain]

## Why you (evidence-backed)
[Differentiator] — proven by [win X], [win Y]. Holds up against the alternative ([named alternative]) because [reason].

## Positioning statement
> I help [audience] [solve specific problem] so they [stake]. Unlike [alternative], I [why-you].

## Generic version (what you'd default to) — and what's dead in it
- Generic: "[the adjective-soup version]"
- Dead words: [list] — doing no work because [why].

## Proof points
1. [Strongest win, one line]
2. [Second win, one line]

## Deploy this week
[One physical action — rewrite headline / open conversation / lead an application], by [date].

Predicted check: when you next say this out loud to [audience], the follow-up question is about your proof, not "what do you mean?"
```

---

## Verification

- [ ] Problem-type is backed by a ≥ 3-win/request pattern, cited.
- [ ] Audience is specific, not "companies" or "everyone."
- [ ] "Why you" is evidence-backed and tested against a named alternative.
- [ ] Exactly one statement, in the frame, sayable in one breath.
- [ ] No adjective-brand words in the final statement.
- [ ] Generic version and its dead words are shown.
- [ ] Two proof wins and one physical deployment action attached.
- [ ] Positioned on revealed demand where it conflicts with the user's aspiration, with the gap named.
