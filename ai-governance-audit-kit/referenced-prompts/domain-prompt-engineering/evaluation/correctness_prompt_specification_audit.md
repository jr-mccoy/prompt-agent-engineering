---
title: "Audit an Existing Prompt for Specification Gaps"
category: prompt-engineering/evaluation
description: "Audit a prompt the user is already running in the wild against a specification-coverage checklist. Surfaces the unstated assumptions, undefined success criteria, ambiguous audience, and missing refusal conditions that let the model wander. Returns a ranked list of gaps, evidence from real outputs, and the specific prompt edits that would close each gap."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - RT-02
  - DS-01
  - QA-01
difficulty: advanced
tags:
  - correctness
  - prompt-audit
  - specification
  - gap-analysis
  - prompt-engineering
updated: "2026-04-21"
related_prompts:
  - domain-prompt-engineering/evaluation/correctness_discovery_prompt.md
  - domain-prompt-engineering/evaluation/correctness_vague_requirements_translator.md
  - domain-prompt-engineering/evaluation/correctness_pre_mortem.md
  - domain-prompt-engineering/skill-development/promptcraft_specification_defines_done.md
  - domain-prompt-engineering/skill-development/promptcraft_eval_harness.md
  - domain-prompt-engineering/prompt-improvement/engineering_prompt_improver.md
---

# Audit an Existing Prompt for Specification Gaps

**Objective:** Take an existing prompt the user is running in production (or running often enough to care about output quality) and audit it against a fixed specification-coverage checklist. Produce a ranked list of specification gaps, with concrete evidence drawn from the user's actual past outputs, and one specific prompt edit per gap that would close it. The audit is diagnostic, not a rewrite — the user decides which gaps to close and owns the edit.

**When to use:**
- A prompt "mostly works" but the user can't articulate why some outputs miss.
- Outputs drift over time or across runs in ways that feel arbitrary.
- The user is about to hand the prompt to someone else (teammate, agent, production pipeline) and wants to pressure-test it before it breaks on their behalf.
- The user has run the prompt enough times to have a library of good and bad outputs but hasn't formalized what separates them.

**Audience:** Prompt engineers, ML engineers, and developers shipping AI-powered features who own a prompt and can supply real outputs it has produced. Not for first drafts — first drafts should go through `promptcraft_specification_defines_done.md` instead.

---

## Inputs Required

1. **The exact prompt text being audited.** Copy-paste, not paraphrased. Include the system prompt, any templated sections, and any tool / function schemas the prompt references. Redact secrets; keep structure.
2. **3–5 real past outputs the user judged "good."** With the input that produced each one. Real, not reconstructed from memory.
3. **3–5 real past outputs the user judged "bad" or "surprising."** With the input that produced each one, and one sentence per output on *why* it was bad (missed a constraint, wrong audience, hallucinated, refused inappropriately, etc.).
4. **The user's informal mental model of what the prompt should do.** One paragraph. The audit will compare this mental model against what the prompt actually says.
5. **The deployment context.** Who runs the prompt (user, teammate, automated pipeline), how often, with what downstream consumer.

**Refuse the audit if:**
- The prompt is hypothetical, aspirational, or "what I'm thinking of writing." The audit depends on real outputs; without them, gap-finding becomes gap-invention.
- Fewer than 2 bad outputs are provided. A single bad output could be a one-off; the audit needs a pattern to distinguish systematic gaps from noise.
- The user cannot say why the bad outputs were bad. The audit cannot recover a specification the user hasn't formed — route them to `correctness_discovery_prompt.md` first.
- Outputs were produced by a different prompt than the one being audited. Spec gaps must be diagnosed against the text responsible for them.

---

## Instructions

### Step 1 — Read the prompt against the 10-slot coverage checklist

For each of the ten specification slots below, mark the prompt as: `explicit` (stated directly), `implicit` (the model can infer from context but it isn't stated), or `missing` (no coverage at all). Cite the line or section in the prompt that justifies each mark.

1. **Task.** What the model is being asked to produce.
2. **Audience.** Who will read / use / act on the output.
3. **Inputs.** What the prompt consumes and what shape it expects.
4. **Output format.** Structure, length, required fields, tone.
5. **Must-haves.** Non-negotiable content or properties of the output.
6. **Must-nots.** Content, claims, or formats the output must not contain.
7. **Success criteria.** How the user (or a checker) decides the output is good.
8. **Handling uncertainty.** What the model should do when it doesn't know (guess, hedge, refuse, ask).
9. **Refusal / escalation conditions.** Situations where producing an output is itself a failure.
10. **Scope boundaries.** What is out of scope and how the model should handle out-of-scope requests.

A prompt with every slot `explicit` is over-specified for most tasks. A prompt with most slots `missing` or `implicit` is under-specified and is probably producing the variance the user is complaining about. The pattern of `missing` and `implicit` marks is what drives the rest of the audit.

### Step 2 — Map bad outputs to missing / implicit slots

For each bad output provided, identify which slot(s) the failure maps to. Example mappings:

- Output too long → `output format` is `implicit`.
- Output used jargon the consumer doesn't understand → `audience` is `missing`.
- Output confidently stated a fact the user knows is wrong → `handling uncertainty` and `must-nots` are `missing`.
- Output answered a question the user never meant to ask → `scope boundaries` are `missing`.
- Output refused to answer when the user wanted a best-effort attempt → `refusal / escalation conditions` are `implicit` and misaligned with intent.

A bad output that doesn't map cleanly to any slot means either (a) the checklist is missing something task-specific — flag it and name what's missing — or (b) the output was bad for a reason that isn't a spec gap (model capability, bad input, bad luck). Do not force-fit.

### Step 3 — Map good outputs to slots that are carrying weight

For each good output, identify which slots in the prompt earned the good behavior. This matters because some prompts work only because the model is inferring from a thin cue the user would lose if they rewrote the prompt. Name the cue. Example: a good output stayed terse because the prompt opens with "Answer in one sentence." That line is carrying the weight of the `output format` slot; a rewrite that removes it will regress.

This step protects against audits that delete load-bearing lines thinking they're decorative.

### Step 4 — Rank the gaps

Score each `missing` or `implicit` slot on two dimensions:

- **Failure rate.** How many of the bad outputs trace back to this slot (count).
- **Severity.** What happens when it fails? Choose one: *cosmetic* (user corrects quickly, no downstream harm), *meaningful* (wasted work, trust erosion), *high* (wrong decision, bad data, user action taken on bad output), *critical* (regulatory, safety, or reputational exposure).

Rank slots by (severity, failure rate). The top 3 are the audit's focus. Gaps below the top 3 are logged but not in the edit plan — this is a diagnostic, not a rewrite.

### Step 5 — Propose one specific prompt edit per top gap

For each of the top 3 gaps, propose one specific edit. Each edit must:

- Be a diff-sized change (a sentence, a section, a list), not a rewrite.
- Name exactly where in the prompt the edit goes (after which line, inside which section).
- Be phrased in the voice and register of the existing prompt, so it doesn't introduce tonal inconsistency.
- Include an explicit prediction of which past bad output(s) this edit would have prevented, and which good outputs it risks changing.

Edits that "move the whole prompt in a better direction" without a predicted change in outputs are vibes, not audits. Every edit must tie back to evidence.

### Step 6 — Flag unverifiable gaps

Some specification gaps cannot be confirmed with the outputs provided. Example: a `refusal / escalation conditions` gap might only surface in out-of-scope inputs the user has never sent. Flag these as *unverifiable-from-current-evidence* and recommend one of:

- Run the prompt against a targeted new case designed to expose the gap.
- Send to `correctness_pre_mortem.md` to enumerate failure modes not yet observed.
- Accept the gap as latent and log it for quarterly review.

Do not rank unverifiable gaps against the evidenced ones.

### Step 7 — Write a one-paragraph audit summary

One paragraph. What the prompt specifies well, what it leaves to inference, what the top 3 gaps are, and what the user should do first. This is the artifact a teammate can read in 90 seconds.

---

## Constraints

### Must
- Audit an actual prompt against actual outputs the user supplies.
- Cite specific lines / sections of the prompt for every `explicit` and `implicit` mark.
- Map every claimed gap to at least one real bad output, unless flagged *unverifiable-from-current-evidence*.
- Propose edits as diff-sized changes, not rewrites.
- Predict per edit which past bad output(s) it would have prevented.
- Preserve load-bearing cues from good outputs.

### Must Not
- Invent hypothetical failure modes not present in the evidence.
- Recommend generic "best-practice" rewrites not tied to a specific bad output.
- Produce a full rewrite of the prompt. The audit is diagnostic; the user owns the edit.
- Assume the user's mental model is correct when it conflicts with the prompt text — flag the conflict.
- Rank a gap that has no evidence against gaps that do.
- Conflate "model capability limit" with "specification gap." Some bad outputs are not fixable in the prompt.
- Critique style, tone, or formatting preferences that don't map to a real output failure.

---

## False-Positive Prevention

1. **Inventing gaps from the checklist.** Every slot has *something* implicit in every prompt. A gap is only a gap if a real bad output traces back to it. Reject audit items that read like "the prompt doesn't explicitly say X" with no linked failure.
2. **Generic rewrite disguised as audit.** If the proposed edits don't cite which bad output they would have prevented, they are style preferences, not audit findings. Reject them.
3. **Deleting load-bearing cues.** A terse prompt that "works" often has one line doing the heavy lifting. Step 3 exists to protect those lines. An audit that silently removes a cue the model was relying on will regress good outputs.
4. **Over-ranking cosmetic severity.** Formatting nits are rarely top-3 gaps unless the downstream consumer is a parser that breaks on them. Severity is about consequence, not discomfort.
5. **Confusing the user's mental model with the spec.** The user says "I want concise answers." The prompt says nothing about length. Both the mental model and the prompt are evidence; the gap is the divergence between them, not the winner of the two.
6. **Model-capability gaps mislabeled as spec gaps.** If the bad output is "the model made up a citation," no amount of prompt specification eliminates hallucination risk — the spec can raise the bar (cite-or-refuse) but can't eliminate the failure mode. Call this out, don't promise a fix.
7. **Under-ranking unverifiable gaps by ignoring them.** Flag them separately, don't pretend they don't exist. A latent refusal-condition gap discovered in production costs more than one surfaced in audit.
8. **Audits on prompts the user doesn't own.** If the prompt is part of a vendor product or a framework the user can't edit, the edit proposals are decorative. Either stop at diagnosis or redirect the audit to the wrapper the user *can* edit.

---

## Output Format

```markdown
## Prompt under audit
[Reference / version / length.]

## Deployment context
- Operator: [user / teammate / pipeline]
- Frequency: [runs per week/month]
- Downstream consumer: [...]

## Coverage checklist (10 slots)
| # | Slot | Status | Evidence (line / section) |
|---|---|---|---|
| 1 | Task | explicit / implicit / missing | [...] |
| 2 | Audience | [...] | [...] |
| ... |

## Bad outputs → slot mapping
| Bad output # | What went wrong | Slot(s) involved |
|---|---|---|
| 1 | [...] | [...] |
| ... |

## Good outputs → load-bearing slots
| Good output # | What worked | Cue earning it |
|---|---|---|
| 1 | [...] | [line in prompt] |
| ... |

## Ranked gaps (top 3)
1. **Slot:** [...] | **Severity:** [cosmetic/meaningful/high/critical] | **Failure rate:** [N of M] | **Evidence:** [bad outputs #]
2. [...]
3. [...]

## Proposed edits (one per top gap)
### Edit 1 — closes gap on [slot]
- **Where:** [after line / inside section]
- **Text:** [the exact sentence / list / section to add]
- **Prevents:** [bad output #]
- **Risks changing:** [good output #, if any]

### Edit 2 — [...]
### Edit 3 — [...]

## Unverifiable gaps (flagged, not ranked)
- [slot] — [why unverifiable] — [recommendation: targeted test / pre-mortem / accept-and-log]

## Model-capability items (not spec gaps)
- [bad output #] — [failure mode] — [why spec can raise the bar but not eliminate]

## Audit summary
[One paragraph a teammate can read in 90 seconds.]
```

---

## Verification

- [ ] Every slot in the 10-slot checklist has a status and cited evidence from the prompt text.
- [ ] Every ranked gap is mapped to ≥1 real bad output (or flagged unverifiable).
- [ ] Every proposed edit is diff-sized and cites the bad output it would have prevented.
- [ ] Load-bearing cues from good outputs are called out so the edits don't delete them.
- [ ] Unverifiable gaps are flagged separately, not mixed into the ranked list.
- [ ] Model-capability items are separated from spec gaps.
- [ ] No generic "best-practice" recommendations appear without evidence.
- [ ] The summary paragraph is short enough to hand off without a walkthrough.
