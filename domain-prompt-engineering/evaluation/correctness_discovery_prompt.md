---
title: "Discover What 'Correct' Actually Means for a Fuzzy Request"
category: prompt-engineering/evaluation
description: "Pin down an operational definition of correctness for a task the user describes loosely. Returns a correctness spec — named consumer, observable must-haves, must-nots, refusal conditions, tiebreakers — grounded in real examples the user has judged rather than in abstract quality heuristics. The output is the input to specification, evaluation, and audit prompts."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - RT-02
  - DS-01
  - QA-01
difficulty: intermediate
tags:
  - correctness
  - specification
  - fuzzy-requirements
  - definition
  - prompt-engineering
updated: "2026-04-21"
related_prompts:
  - domain-prompt-engineering/evaluation/correctness_vague_requirements_translator.md
  - domain-prompt-engineering/evaluation/correctness_tradeoff_forcer.md
  - domain-prompt-engineering/evaluation/correctness_prompt_specification_audit.md
  - domain-prompt-engineering/goal-orientation/goalorientation_right_problem_diagnostic.md
  - domain-prompt-engineering/skill-development/promptcraft_rewrite_vague_ask.md
  - domain-prompt-engineering/skill-development/promptcraft_specification_defines_done.md
---

# Discover What "Correct" Actually Means for a Fuzzy Request

**Objective:** Convert a fuzzy request ("write a good summary," "make this more rigorous," "help me think through this") into an operational definition of correctness that downstream prompts can consume. The output names the consumer, states observable must-haves and must-nots, defines refusal conditions, and resolves the top 2–3 tradeoffs with explicit tiebreakers. Correctness is discovered against the user's own examples of acceptance and rejection, not inferred from generic quality heuristics.

**When to use:**
- The user has asked the model for something vaguely and is not satisfied with the results but can't name why.
- A task is about to be handed to a teammate, an agent, or a pipeline, and "you know what good looks like" will not survive the handoff.
- A specification prompt, eval prompt, or audit prompt wants a correctness definition as input and the user doesn't have one.

**Audience:** Prompt engineers, ML engineers, and developers shipping AI-powered features who need a concrete definition of correct output before investing in measurement, specification, or automation. Not for exploratory one-off chats where the user is still deciding what they want.

---

## Inputs Required

1. **The fuzzy request.** The exact words the user would type or has typed. If they can only describe it abstractly, stop and collect an actual prompt or task framing first.
2. **The consumer of the output.** Named specifically: person, role, downstream system, or the user themselves acting in a specific later role. "Me" is not enough — "me preparing for the Tuesday review meeting" is.
3. **3–5 real past outputs the user accepted.** With the input that produced each one. Real, not reconstructed from memory, not synthetic. If none exist, the user has not run the task enough times to discover what correct means; route them elsewhere.
4. **2–3 real past outputs the user rejected or found wanting.** With one sentence each on what was wrong.
5. **The stakes.** What goes wrong when the output is wrong, to whom, and how reversibly. One paragraph.

**Refuse the discovery if:**
- The task is hypothetical or aspirational. Correctness cannot be discovered from imagined outputs — imagination smuggles in the user's unstated preferences without grounding them.
- Fewer than 2 rejected outputs are provided. Without rejection evidence, the definition will over-index on the accepted outputs and fail to exclude plausible-but-wrong alternatives.
- The user names "me" as consumer without a use-case frame. Output that satisfies the user in one mood may not satisfy them in another; the consumer must be a role, not a person.

---

## Instructions

### Step 1 — Name the consumer and the decision

One sentence: who will read or act on the output, and what decision or action depends on it. "My teammate Paula, deciding whether to escalate the incident to on-call." "Me on Tuesday morning, deciding which three of twenty threads to respond to first." The consumer determines everything downstream; a correctness definition written for a different consumer is wrong.

If the same output has multiple consumers (user + stakeholder + auditor), pick the strictest. Write the definition for them. Note the others.

### Step 2 — Cluster the accepted outputs into behaviors

Across the 3–5 accepted outputs, identify the behaviors that made them acceptable. Cluster into:

- **Content behaviors.** What the output included or concluded (e.g., always named the affected user, always ranked options by a specific criterion).
- **Form behaviors.** Structure, length, register (e.g., always under 200 words, always in a table with three columns).
- **Absence behaviors.** What the output reliably did *not* do (e.g., never speculated past the evidence, never assumed authority it didn't have).

Do not list every commonality — only the ones that a different, plausible output would have violated. A list of "these outputs all used English" is not a correctness behavior; every plausible alternative uses English too.

### Step 3 — Cluster the rejected outputs into violated behaviors

For each rejected output, name which content / form / absence behavior it violated. If a rejection does not map to any behavior identified in Step 2, either the accepted-outputs clustering missed a behavior (go back and add it) or the rejection was for a reason outside the correctness definition (e.g., model capability, off-day user) — flag and park.

Rejections that map cleanly are the most valuable data: each one is a negative case that the correctness definition must now exclude.

### Step 4 — Write the must-haves

From the clustered behaviors, write 3–7 must-have criteria. Each criterion:

- Is observable from the output alone (or from the output + the input; never from the user's mood).
- Rules out at least one rejected output. If it doesn't, it's either redundant or decorative.
- Is specific enough that two independent graders would agree on pass / fail on 9 of 10 cases.

Fewer than 3 and the definition is thin. More than 7 and it's over-specified and will mostly be ignored.

### Step 5 — Write the must-nots

From the absence behaviors and the rejected outputs, write 2–5 must-nots. Each must-not:

- Names a specific failure mode, not a vague anti-quality ("no slop" is not a must-not).
- Is evidence-backed by ≥1 rejected output or a credible near-miss the consumer described.

Must-nots exist because models often produce plausible-but-wrong outputs that no must-have catches. The rejected-outputs pool is the main source of must-nots.

### Step 6 — Set refusal conditions

Name inputs for which the correct output is *not producing an output*. At least one of:
- Input is out of scope (define scope).
- Input requires information the system cannot have (name what).
- Input is ambiguous enough that any output risks misleading the consumer; the correct response is to ask, escalate, or decline.

Refusal conditions exist because "best-effort always" is a policy, not an absence of policy; users who haven't named refusal conditions are implicitly committing to best-effort-always and will be surprised by the consequences.

### Step 7 — Resolve the top 2–3 tradeoffs

Surface the tensions the user will face once the must-haves and must-nots are fixed. Typical ones: brevity vs. completeness; caution vs. decisiveness; precision vs. coverage; refusal vs. best-effort. Pick the top 2–3 that actually bite for this task. For each:

- Name the dominant dimension and the subordinate one.
- State the tiebreaker rule (what the output should do when both pull equally).
- Cite one accepted output and one rejected output that illustrate the rule.

A correctness definition that doesn't resolve tradeoffs is a wish list. The tradeoff resolution is what makes it operational.

### Step 8 — Write the one-paragraph correctness definition

Final artifact: one paragraph that names the consumer + decision, lists the must-haves by tag, names the must-nots by tag, states the refusal policy in one sentence, and names the dominant dimension on the top tradeoff. This paragraph pastes directly into downstream prompts.

---

## Constraints

### Must
- Ground every must-have and must-not in at least one accepted or rejected output.
- Name the consumer as a role + decision, not as a person in the abstract.
- Resolve at least one tradeoff with an explicit tiebreaker.
- Write the final definition in one paragraph that stands alone.

### Must Not
- Include generic quality heuristics ("accurate," "clear," "well-structured") without an observable test attached.
- Invent must-nots from failure modes the user has never experienced on this task.
- Treat the accepted outputs as the full spec — the must-haves must survive cases the user hasn't seen yet.
- Confuse "what the user prefers" with "what the consumer needs." If they diverge, the definition is for the consumer.
- Produce more than 7 must-haves or more than 5 must-nots.

---

## False-Positive Prevention

1. **Heuristics masquerading as criteria.** "Clear," "professional," "thorough" are not testable. Any must-have that doesn't survive the question "how would a grader check this?" is a heuristic; rewrite it or drop it.
2. **Accepted-output over-fit.** A must-have that only rules out outputs the user would never have produced anyway is decorative. Every must-have must rule out at least one plausible alternative — ideally a rejected output.
3. **Refusal conditions skipped.** Users overwhelmingly forget refusal conditions because "always answer" feels like a default rather than a policy. A definition without refusal conditions is implicitly committing to best-effort-always — call that out and force an explicit choice.
4. **Consumer drift.** "Me" as consumer hides the fact that the user wants different outputs in different moods. Force a role-framed consumer; if the task genuinely has multiple consumer modes, write separate definitions.
5. **Tradeoff denial.** Users asked "brevity vs. completeness?" will often answer "both." That's tradeoff denial, not a resolution. Force dominance; if they truly want both, the task either has a bigger context window or needs to be split.
6. **Hypothetical-case contamination.** If the user starts inventing outputs during the session to "make a point," pause. The definition must be grounded in real outputs; invented ones encode the user's current preference instead of the consumer's actual need.
7. **Definition drift across conversations.** A correctness definition produced on a Monday and revisited on a Thursday often drifts. Timestamp it, attach the evidence, and treat changes as explicit revisions with a reason.
8. **Skipping stakes.** A correctness definition without stakes cannot rank its own criteria. High-stakes tasks need tighter refusal conditions and stricter must-nots; low-stakes tasks tolerate more best-effort. Stakes set the temperature.

---

## Output Format

```markdown
## Task
[The fuzzy request, quoted verbatim.]

## Consumer
[Role + decision. "Paula, triage engineer, deciding whether to escalate."]

## Stakes
[One paragraph.]

## Evidence inventory
- Accepted outputs: [N, with labels]
- Rejected outputs: [N, with labels and one-line reasons]

## Must-haves (3–7)
| # | Criterion | Observable test | Rules out rejection # |
|---|---|---|---|
| 1 | [...] | [...] | [N] |
| ... |

## Must-nots (2–5)
| # | Failure mode | Evidence (rejection #) |
|---|---|---|
| 1 | [...] | [N] |
| ... |

## Refusal conditions
- [When to not produce an output, and what to do instead.]

## Tradeoffs resolved
| # | Tension | Dominant | Subordinate | Tiebreaker | Examples (acc / rej) |
|---|---|---|---|---|---|
| 1 | [...] | [...] | [...] | [...] | [...] |
| ... |

## Correctness definition (one paragraph)
[Consumer + decision, must-haves by tag, must-nots by tag, refusal policy, top tradeoff dominance.]

## Date + evidence snapshot
[Timestamp. Names the accepted/rejected output labels used.]
```

---

## Verification

- [ ] Consumer is a role + decision, not a person in the abstract.
- [ ] Every must-have has an observable test and rules out ≥1 real alternative.
- [ ] Every must-not cites ≥1 rejected output or named near-miss.
- [ ] Refusal conditions are explicit.
- [ ] ≥1 tradeoff is resolved with an explicit tiebreaker.
- [ ] The one-paragraph definition stands alone.
- [ ] Heuristic words ("clear," "good," "appropriate") do not appear without an attached test.
- [ ] Evidence labels are timestamped for later drift detection.
