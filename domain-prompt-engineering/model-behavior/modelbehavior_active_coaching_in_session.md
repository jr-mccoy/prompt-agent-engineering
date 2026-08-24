---
title: "Active Coaching Inside a Running Conversation to Correct Behavior"
category: prompt-engineering/model-behavior
description: "Mid-conversation coaching pattern that corrects a model's behavior in the current session without starting over — name the specific deviation, supply the rule that replaces the default, check adherence, and capture what should move into the system prompt for next time."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - RT-09
  - QA-01
difficulty: intermediate
tags:
  - model-behavior
  - in-session-coaching
  - corrective-instruction
  - prompt-debugging
  - claude-code
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/model-behavior/modelbehavior_instruction_deviation_diagnostic.md
  - domain-prompt-engineering/escape-median/escapemedian_correction_compounder.md
  - domain-prompt-engineering/escape-median/escapemedian_instruction_sharpener.md
---

# Active Coaching Inside a Running Conversation to Correct Behavior

**Objective:** When a model in an ongoing conversation is behaving in a way you don't want, use a structured correction turn that (1) names the specific deviation, (2) supplies the rule that should replace the model's current default, (3) asks the model to restate the rule in its own words to confirm it understood, and (4) captures the rule as a candidate for the system prompt so the correction doesn't have to be repeated in the next session.

**When to use:** You're in a live chat or agentic session. The model has drifted — it's adding preambles, hedging, using a format you didn't ask for, mis-prioritizing goals, or otherwise deviating. Restarting the session would lose useful context. You want to correct behavior *now* and also preserve the correction.

**Audience:** Prompt engineers, developers, and power users who run long sessions with Claude, GPT, or similar models and want to correct behavior without losing the session state.

---

## Inputs Required

1. **The current conversation or the relevant turn(s).** You need to point at real output, not a hypothetical.
2. **The specific behavior you want changed.** One sentence. "It's adding three-paragraph preambles before every answer," not "it's being too verbose."
3. **The replacement rule.** One sentence that, if followed, would prevent the deviation. If the user doesn't have this yet, help them derive it in Step 1.
4. **Whether the rule should persist** (add to system prompt / CLAUDE.md) or is session-only.

Refuse to produce a coaching turn if no real deviation has occurred. "Coach the model to be better in general" is not a correction — it's a rewrite. Redirect to the instruction-sharpening prompt for that case.

---

## Instructions

### Step 1 — Name the deviation precisely

Write one sentence that both of these are true for:
- The sentence is falsifiable ("it adds a preamble" can be checked against the output).
- The model's recent output contradicts the sentence.

If the user's complaint is vague ("it's bad," "it's missing the point"), push for specificity before continuing. The coaching turn only works if the deviation is nameable.

### Step 2 — Identify what default the model is executing

Before writing the correction, name what the model *is* doing and why that's its default. Common defaults include:

- Opening with a restatement of the question.
- Adding safety hedges or disclaimers when none were requested.
- Defaulting to bullet points when prose was expected (or vice versa).
- Offering multiple options when a decision was requested.
- Ending with "let me know if you'd like more detail."
- Giving the balanced view when a stance was requested.
- Explaining what it's about to do before doing it.

Naming the default explicitly is what lets the correction override it. A correction that doesn't name the default ("please be more direct") usually fails because the default stays stronger than the correction.

### Step 3 — Write the correction turn

Structure:

```
[1] Name the deviation. "You just did X. I don't want X."
[2] Name the default. "The default here is probably Y. Please override it."
[3] State the replacement rule in one sentence.
[4] Give one concrete example of compliant output (optional but strongly recommended).
[5] Ask the model to restate the rule in its own words.
[6] Ask the model to apply the rule to the previous turn and regenerate.
```

Keep the correction turn short. Long correction turns compete for attention with the original task. The rule is the asset, not the explanation around it.

### Step 4 — Check adherence on the next two turns

A single passing turn is not evidence the correction took. Check the next two turns for adherence. If the behavior returns by turn three, the correction didn't compound — escalate to Step 5.

### Step 5 — Escalate if coaching fails

If the behavior returns within three turns:
- The rule is probably fighting a strong base-model prior. Make the rule stronger (more specific, more negative-framed, with a compliant example) and reapply.
- Or move the rule into the system prompt / CLAUDE.md. In-session coaching has a half-life; persistent instructions don't.
- Or the rule itself may be wrong — re-run the diagnostic (`modelbehavior_instruction_deviation_diagnostic.md`) to confirm you're correcting the right thing.

### Step 6 — Capture the rule for next session

If the correction stuck, propose the exact sentence to add to the system prompt or CLAUDE.md. Format it so it can be pasted without editing. Flag whether the rule is:
- **General** (applies to any task with this model).
- **Role-scoped** (applies when working in this project / repo / role).
- **Task-scoped** (applies only to a specific task type).

Rules captured at the wrong scope either over-apply or get forgotten.

---

## Constraints

### Must
- Start from a real deviation in the current conversation, not a general complaint.
- Name the default the model was executing, not just the deviation.
- State the replacement rule in one sentence.
- Ask the model to restate the rule (self-check).
- Check adherence on the following two turns before declaring success.
- Produce the rule-as-persistent-instruction in the final output, with scope labeled.

### Must Not
- Write a multi-paragraph correction. Long corrections dilute themselves.
- Layer a new correction on top of a failed one without diagnosing. Corrections don't stack cleanly.
- Use vague replacement rules ("be more direct," "be more thorough") — replace them with concrete rules.
- Treat one passing turn as proof the correction took.
- Add the rule to a system prompt without the user's confirmation.

---

## False-Positive Prevention

1. **In-session coaching decays.** A rule that works for five turns may not survive a long context or a tool call that resets attention weighting. If the rule matters, persist it.
2. **"Please be more X" almost never works.** X has to be replaced with a concrete behavior the model can check itself against. "Please be more concise" is weaker than "cap your answer at 120 words."
3. **The model will often *claim* it understood** (including a convincing restatement) and then not apply the rule. Restatement is a useful signal, not proof. Adherence on the next two turns is proof.
4. **Don't coach away capabilities you'll want back.** A rule that says "never add context" may backfire when you actually need context on a later turn. Scope the rule.
5. **If the same coaching has failed twice in this session,** stop coaching and restart with the rule in the system prompt. Repeated failed corrections poison the attention and make future corrections harder.
6. **If the deviation is from a user instruction the model never saw** (e.g., buried three turns back), the fix is re-surfacing, not coaching. Re-state the original instruction before coaching.

---

## Output Format

```markdown
## Deviation
- **What the model did (quoted):** "[...]"
- **What I wanted instead:** "[...]"

## Default being executed
[One line naming the model's base-mode behavior that produced the deviation.]

## Correction turn (paste into the chat)
> You just did [X]. I don't want [X]. The default here is probably [Y]; override it.
>
> Rule: [one sentence].
>
> Example of compliant output: [short example].
>
> Restate the rule in your own words, then regenerate the previous turn under it.

## Adherence check
Turn after correction: [ ] compliant   [ ] deviated
Second turn after: [ ] compliant   [ ] deviated

If either deviated → escalate (see below).

## Escalation (only if coaching failed)
- Stronger rule to try: [...]
- Or: move to system prompt / CLAUDE.md as: "[exact sentence to paste]"

## Persist the rule (if coaching stuck)
**Scope:** [general / role-scoped / task-scoped]
**Sentence to add to [system prompt | CLAUDE.md | project memory]:**
> [...]
```

---

## Verification

- [ ] A real deviation was quoted (not a general complaint).
- [ ] The default behavior was named explicitly.
- [ ] The replacement rule is one sentence and falsifiable.
- [ ] The correction turn asks the model to restate the rule.
- [ ] Adherence was checked on two turns, not one.
- [ ] A persist-or-drop decision was made with scope labeled.
