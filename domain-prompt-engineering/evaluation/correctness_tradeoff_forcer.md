---
title: "Force Tradeoff Clarity on Competing Quality Dimensions"
category: prompt-engineering/evaluation
description: "Take a task whose quality dimensions pull against each other (brevity vs. completeness, caution vs. decisiveness, precision vs. coverage, refusal vs. best-effort) and force the user to commit to a dominance order with evidence-backed tiebreakers. Returns a tradeoff policy the downstream prompt, eval, and audit can enforce consistently."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - DS-01
  - QA-01
difficulty: intermediate
tags:
  - correctness
  - tradeoffs
  - policy
  - specification
  - prompt-engineering
updated: "2026-04-21"
related_prompts:
  - domain-prompt-engineering/evaluation/correctness_discovery_prompt.md
  - domain-prompt-engineering/evaluation/correctness_vague_requirements_translator.md
  - domain-prompt-engineering/evaluation/correctness_prompt_specification_audit.md
  - domain-prompt-engineering/skill-development/promptcraft_specification_defines_done.md
  - domain-prompt-engineering/skill-development/promptcraft_constraint_architecture_design.md
---

# Force Tradeoff Clarity on Competing Quality Dimensions

**Objective:** Surface the quality dimensions the user implicitly wants from a task, identify the pairs that actually pull against each other in practice, and force an explicit dominance + tiebreaker per pair. The artifact is a tradeoff policy that a downstream prompt, rubric, or audit can cite. Tradeoff denial ("I want both") is not a permitted resolution — the output either picks a dominant dimension or declares that the dimensions are not actually in tension for this task.

**When to use:**
- Outputs feel inconsistent across runs — sometimes terse and missing detail, sometimes long and buried.
- Reviewers disagree about whether an output is good because they're weighting dimensions differently.
- A new consumer (teammate, downstream system) is about to use outputs that were previously only used by the prompt's author, and the author's implicit weighting won't transfer.

**Audience:** Prompt engineers, ML engineers, and developers shipping AI-powered features who have a working prompt whose outputs swing along a quality axis they can name. Not for tasks where dimensions never conflict — if no tension exists, the prompt doesn't need this.

---

## Inputs Required

1. **The task.** One paragraph describing what the prompt produces and for whom.
2. **The quality dimensions the user cares about.** Their list, in their words. Typical ones: brevity, completeness, precision, coverage, caution, decisiveness, readability, auditability, refusal, best-effort. 3–6 dimensions, not 12.
3. **Real past outputs that illustrate the tension.** At minimum: one output the user thought was too far on one dimension and one the user thought was too far on the opposite. If the user can't produce both ends of a tension, the tension may not be real for this task.
4. **The consumer.** Role + decision. If not known, run `correctness_discovery_prompt.md` first.
5. **Stakes.** One paragraph. Stakes determine which dimension dominates on high-ambiguity calls.

**Refuse the tradeoff exercise if:**
- Fewer than 2 real outputs illustrating the tension are provided. Invented examples encode the user's current preference, not the task's real tension.
- The user lists a single dimension. There's no tradeoff to force.
- The user can't name a consumer. Dimensions that serve no one can't be weighted.

---

## Instructions

### Step 1 — Screen the dimensions for real tension

For each pair of dimensions the user listed, ask: does improving one in this task usually cost the other? Mark each pair:

- **Real tension** — improving one demonstrably hurts the other, with at least one real output illustrating the cost.
- **Apparent tension** — the dimensions sound opposed but in this task they don't actually trade off (e.g., "brevity vs. precision" — shorter prose can be more precise when slop is cut).
- **Unrelated** — the dimensions are orthogonal for this task.

Only real tensions move to Step 2. Apparent tensions should be named and dismissed, not resolved — resolving a non-existent tradeoff produces a policy that bites when it shouldn't.

### Step 2 — Rank the real tensions by bite

For each real tension, rank on two dimensions:

- **Frequency.** How often does the task produce an output where the two dimensions conflict? (Estimate from real outputs.)
- **Cost of wrong call.** When the tradeoff is called the wrong way for this consumer, what does it cost? (cosmetic / meaningful / high / critical)

The top 2–3 tensions by (cost, frequency) are where the policy needs explicit rules. Tensions below the top 2–3 are logged but left to model judgment — over-constraining rare tensions produces rigidity without value.

### Step 3 — Force a dominance call per top tension

For each top tension, the user must pick:

- **Dominant dimension.** The one the output should prioritize when they conflict.
- **Subordinate dimension.** The one that yields.
- **Acceptable loss.** How much of the subordinate dimension the user is willing to give up to protect the dominant. Quantified if possible ("up to 50% longer"), qualitative if not ("noticeably longer, not bloated").

"Both equally" is not a permitted answer. If the user insists, probe: on the real outputs that caused the tension, which one did they actually accept? The accepted output encodes the real dominance, whether or not the user can articulate it.

### Step 4 — Write the tiebreaker rule

For each top tension, write a one-sentence tiebreaker rule: what does the output do when both dimensions pull equally? The tiebreaker is not the dominant dimension — the tiebreaker fires only in the narrow band where dominance doesn't decide. Examples:

- *Dominance: caution over decisiveness. Tiebreaker: when caution and decisiveness pull equally, produce a decisive output with an explicit uncertainty paragraph attached.*
- *Dominance: brevity over completeness. Tiebreaker: when brevity and completeness pull equally, drop the least-load-bearing section of the template rather than trimming within every section.*

Tiebreakers are where a policy becomes executable rather than a vibe.

### Step 5 — Stress-test against real outputs

For each top tension, pick one accepted output and one rejected output. Walk through: would the policy have accepted the accepted output? Would it have rejected the rejected one? If no, revise the policy until yes. If the accepted and rejected outputs are indistinguishable under the policy, the policy is too coarse — refine dominance or tiebreaker until it discriminates.

A policy that doesn't predict the user's own past judgments is already wrong.

### Step 6 — Name the conditions that flip the policy

Most tradeoffs have conditions that change which dimension dominates. High-stakes inputs might flip caution to dominant even in a task where decisiveness usually wins. Name 0–2 flip conditions per top tension:

- The condition (observable from the input).
- The flipped dominance.
- The reason.

If more than 2 flip conditions are needed, the task is probably two tasks; run the exercise separately on each.

### Step 7 — Write the tradeoff policy

Final artifact: a structured list the downstream prompt, rubric, or audit can cite. One block per top tension, containing task, dominant, subordinate, acceptable loss, tiebreaker, flip conditions, and one example each of the policy accepting and rejecting an output.

The policy is the user's standing answer. Future runs should not re-litigate these tradeoffs unless the task, consumer, or stakes change.

---

## Constraints

### Must
- Screen for real vs. apparent tension before forcing any resolution.
- Ground every dominance call in at least one real accepted and one real rejected output.
- Produce a one-sentence tiebreaker per top tension.
- Stress-test the policy against real outputs; revise until it predicts the user's past judgments.

### Must Not
- Resolve tensions that aren't real for this task.
- Accept "both equally" as a resolution.
- Produce more than 3 top-tension policies — more than that and the user will ignore the policy in practice.
- Invent flip conditions the user has never observed.
- Conflate the user's personal preference with the consumer's need — the policy is for the consumer.

---

## False-Positive Prevention

1. **Solving apparent tensions.** Users list opposed-sounding dimensions that aren't really opposed for their task (brevity vs. precision often collapses). Step 1 screens these out; forcing a resolution on an apparent tension produces a policy that bites on non-existent conflicts.
2. **Dominance without evidence.** A dominance call the user can articulate but can't back with real outputs is a preference, not a policy. It won't survive real outputs. Force the evidence check.
3. **Tiebreaker omitted.** Users happy with dominance often skip the tiebreaker because "it's obvious." It isn't; the tiebreaker is where the policy lives in the narrow band where dominance doesn't decide.
4. **Policy that can't discriminate real cases.** If the accepted and rejected outputs are indistinguishable under the policy, the policy is too coarse. Refine or discard.
5. **Too many tensions.** Users want to resolve every tension they can name. Three is already a lot of policy for a downstream prompt to honor. Stop at the top 2–3 by (cost, frequency).
6. **Flip-condition bloat.** Every flip condition adds a branch the model has to navigate. Two is the ceiling; more and the task is two tasks.
7. **Preference smuggling.** The user's mood is not a flip condition. If the policy changes based on the user's mood, the user is the consumer — name that, or the policy will diverge from the nominal consumer's need.
8. **Policy rot.** Tradeoff policies go stale when the consumer, stakes, or task shifts. Date-stamp the policy and name the revisit condition ("revisit if the consumer changes or if stakes shift").

---

## Output Format

```markdown
## Task
[One paragraph.]

## Consumer
[Role + decision.]

## Stakes
[One paragraph.]

## Dimensions listed
[User's original list.]

## Tension screen
| Pair | Status | Evidence |
|---|---|---|
| [A vs. B] | real / apparent / unrelated | [output # or reason] |
| ... |

## Tensions ranked (top 3 advance)
| # | Tension | Frequency | Cost of wrong call | Advance? |
|---|---|---|---|---|
| 1 | [...] | [...] | [...] | yes / no |
| ... |

## Tradeoff policies (one block per advanced tension)

### Policy 1 — [tension]
- **Dominant:** [...]
- **Subordinate:** [...]
- **Acceptable loss on subordinate:** [...]
- **Tiebreaker:** [one sentence]
- **Flip conditions:** [0–2]
- **Example — policy accepts:** [accepted output #]
- **Example — policy rejects:** [rejected output #]

### Policy 2 — [...]
### Policy 3 — [...]

## Dismissed tensions (apparent / unrelated)
- [pair] — [why dismissed]

## Revisit condition
[What change to the task, consumer, or stakes triggers a rewrite.]

## Policy date
[Timestamp.]
```

---

## Verification

- [ ] All user-listed dimension pairs are screened as real / apparent / unrelated.
- [ ] Only real tensions received policies.
- [ ] Each policy names dominant, subordinate, acceptable loss, and a one-sentence tiebreaker.
- [ ] Each policy is grounded in ≥1 accepted and ≥1 rejected real output.
- [ ] Each policy correctly predicts the user's past judgment on the paired examples.
- [ ] No more than 3 policies are active.
- [ ] Flip conditions are observable from the input, not the user's mood.
- [ ] The policy is dated with a named revisit condition.
