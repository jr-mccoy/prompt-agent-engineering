---
title: "Compound Corrections Across a Session So Preferences Stick"
category: prompt-engineering/escape-median
description: "Turn a stream of ad-hoc corrections the user has made to a model during a working session into a compact, ordered rule set that makes those corrections stick — for the rest of the session and, optionally, for future sessions — so the user stops re-correcting the same defaults."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - escape-median
  - correction-compounding
  - preferences
  - rule-extraction
  - personalization
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/escape-median/escapemedian_instruction_sharpener.md
  - domain-prompt-engineering/escape-median/escapemedian_bootstrap_instruction_file.md
  - domain-prompt-engineering/model-behavior/modelbehavior_active_coaching_in_session.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_rule_extraction_from_decisions.md
---

# Compound Corrections Across a Session So Preferences Stick

**Objective:** Review the corrections a user has made in a working session (to a model's tone, format, level of detail, stance, or scope), extract the underlying preferences, convert each preference into a rule stated in the user's own words, sort the rules so the most load-bearing come first, and produce a short rule block the user can (a) paste back into the current session to compound the corrections, and (b) decide whether to promote into a system prompt or CLAUDE.md for future sessions.

**When to use:** You've been working with a model for a while on a task, and you've noticed yourself making the same kinds of corrections repeatedly ("shorter," "skip the preamble," "don't caveat that"). You want to stop re-correcting and have the model just work the way you want.

**Audience:** Individual users in an active working session with Claude, GPT, or a similar model who have accumulated enough corrections to extract a pattern.

---

## Inputs Required

1. **The session transcript** (or the relevant turns) containing the corrections. Needs to be real — this prompt does not work on imagined preferences.
2. **A rough count** of how many corrections have been made. If fewer than 3, stop: there isn't enough signal yet.
3. **Whether the corrections are task-specific or general.** If general, the rules should go to CLAUDE.md. If task-specific, they stay in the current prompt or a task-scoped instruction.
4. **Any preferences the user has stated outside of corrections** (preferences they've declared rather than corrected into). Optional.

Refuse to run on a session with no corrections. "I'd like to make the model better" without data is not a compounding task — that's instruction design, which lives in `escapemedian_instruction_sharpener.md`.

---

## Instructions

### Step 1 — List every correction verbatim

Go through the session and list each correction as a short item: what the model did, what the user asked it to do instead, quoting both. Don't paraphrase. Paraphrasing is where real preferences get washed out.

### Step 2 — Cluster corrections by underlying preference

Corrections are surface; preferences are the underlying pattern. Typical clusters:

- **Length / verbosity.** Multiple "shorter," "tighter," "just the answer" corrections.
- **Preamble / framing.** Corrections removing restatements, "great question" openers, "let me walk you through" preludes.
- **Hedging / confidence.** Corrections removing "it depends," "consider," "you might want to."
- **Format.** Corrections between prose/bullets/table.
- **Scope.** Corrections cutting off topics the model expanded into.
- **Stance.** Corrections from balanced to committed, or the other way.
- **Level of detail.** Corrections between "don't explain" and "explain more."

A cluster needs at least two corrections pointing the same direction. Single corrections go in a "noise" bucket — they may become clusters later but shouldn't be promoted to rules yet.

### Step 3 — Derive one rule per cluster

Each cluster becomes a rule. Rule shape:
- **Positive action.** Describe what the model should do, not only what to avoid.
- **Testable.** A reviewer should be able to check any single output against it.
- **In the user's voice.** "Cap answers at 150 words unless I ask for more" not "be concise."
- **Names the default being overridden**, where known.

If two corrections in a cluster point opposite directions (the user asked for more detail once and less another time), the rule should be conditional: "When I'm working through a plan, default to short; when I'm drafting for others, expand."

### Step 4 — Rank the rules

Not all rules are equal. Rank by:
1. Rules that address corrections the user made most often.
2. Rules that address corrections made *most emphatically*.
3. Rules that would prevent the most future corrections.

The ranking matters for conflict resolution — rules do conflict in the wild, and the model needs to know which wins.

### Step 5 — Produce the rule block

A rule block is short (aim for 5–10 lines), sits at the top of the prompt, and the model treats as governing. Include:
- The ranked rules, numbered.
- One line naming the overall preference ("I want output that commits, not balances").
- A tie-breaker: what to do when rules conflict (usually "higher number wins" or "ask").

### Step 6 — Apply and verify in-session

Paste the rule block into the current session as a single correction turn. Ask the model to restate the rules in its own words (not paraphrase — operationalize). Observe adherence on the next 2–3 turns. If adherence holds, the rules compounded. If it doesn't, see Step 7.

### Step 7 — Escalate if rules don't hold in-session

If the user keeps correcting for the same thing after pasting the rules:
- The rule may be too vague. Tighten with a specific operational rule and one compliant example.
- The rule may be fighting a strong base-model default. Strengthen the override framing and explicitly name the default.
- The rule may only hold for some task types. Scope it.
- The rule may itself be wrong. The user may have been correcting inconsistently; re-read the clusters.

### Step 8 — Decide whether to promote

For each rule, classify:
- **Session-only.** Useful here, not elsewhere.
- **Task-scoped.** Useful whenever the user is doing this type of task. Promote to a task-specific prompt header.
- **General.** Useful across tasks. Promote to CLAUDE.md or the equivalent persistent-memory file via `escapemedian_bootstrap_instruction_file.md`.

Rules promoted at the wrong scope either over-apply or get forgotten.

---

## Constraints

### Must
- Work from the actual session, not a summary.
- Require at least 3 corrections before proceeding.
- List corrections verbatim before clustering.
- Produce 3–8 rules, ranked.
- Provide a tie-breaker for rule conflicts.
- Verify adherence across 2–3 turns before declaring success.
- Classify each rule by scope for promotion.

### Must Not
- Promote single corrections to rules. Single corrections are noise until they repeat.
- Synthesize rules the user didn't actually correct toward.
- Produce more than 8 rules. Past that, the model averages.
- Use vague rule language ("be clearer," "sound confident"). Replace with operational tests.
- Add a rule to CLAUDE.md or a persistent file without the user's explicit consent.

---

## False-Positive Prevention

1. **Compounding corrections can calcify a bad preference.** If the user has been correcting toward a preference that backfires (too short for the audience, too confident for the context), promoting it makes the problem bigger. Check: would the user actually want this rule next week on a different task?
2. **"The user always wants X" is a claim that needs ≥3 corrections, not 2.** Two corrections could be noise. Three is a pattern.
3. **Negative-only rules produce unintended behavior.** "Don't hedge" with no positive replacement leaves the model hedging in a different shape.
4. **Context affects rules.** A rule derived during a debug session may not apply during a writing session. Scope carefully.
5. **Promoted rules age faster than people think.** A rule that was right six months ago may be wrong now because the work changed. Encourage revisiting promoted rules whenever the task changes.
6. **The model claiming it will follow the rule ≠ following it.** Verify adherence on actual outputs across multiple turns, not on the model's acknowledgment.
7. **If corrections are internally inconsistent,** don't force a rule. Flag the inconsistency. Forcing a rule over inconsistent corrections leads to the model doing the wrong thing confidently.

---

## Output Format

```markdown
## Corrections listed (verbatim)
1. Model did: "[...]". User asked: "[...]".
2. ...

## Clusters
- **[Cluster name]** (count: N): [brief description]. Corrections: [#s from list above].
- ...

## Noise (single-instance corrections, not promoted)
- [...]

## Rules (ranked)
1. **[Rule]** — overrides default: [default, if any]. Test: [how to check a single output].
2. ...

## Tie-breaker
When rules conflict: [higher-numbered wins | ask | closer-to-task wins].

## Rule block (paste into current session)

```
[5–10 lines: ranked rules + tie-breaker, in the user's voice.]
```

## In-session verification
- Paste the block.
- Ask the model to restate each rule as an operational check.
- Observe the next 3 turns.
- Still correcting? → escalate.

## Promotion plan
| Rule | Scope | Promote to |
|------|-------|------------|
| 1 | task-scoped | task-specific prompt header |
| 2 | general | CLAUDE.md via bootstrap-instruction-file prompt |
| 3 | session-only | — |
```

---

## Verification

- [ ] At least 3 corrections were input.
- [ ] Corrections are listed verbatim.
- [ ] Each rule comes from ≥2 corrections in the same cluster.
- [ ] Rules are ranked.
- [ ] A tie-breaker is specified.
- [ ] Adherence is verified on multiple turns, not on acknowledgment.
- [ ] Each rule has a scope decision.
