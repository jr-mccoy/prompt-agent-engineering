---
title: "Run a Pre-Mortem on Correctness Before Shipping"
category: prompt-engineering/evaluation
description: "Imagine the prompt or system has shipped and is producing wrong outputs three months later. Walk the user backward from plausible failure modes to the spec, prompt, or monitoring gap that would have let each failure through. Returns a ranked list of likely failures with preventive edits and detection signals, grounded in the user's actual deployment context rather than generic AI-risk catalogs."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-09
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - correctness
  - pre-mortem
  - failure-modes
  - risk-assessment
  - prompt-engineering
updated: "2026-04-21"
related_prompts:
  - domain-prompt-engineering/evaluation/correctness_discovery_prompt.md
  - domain-prompt-engineering/evaluation/correctness_prompt_specification_audit.md
  - domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md
  - domain-prompt-engineering/evaluation/correctness_production_monitoring_setup.md
  - domain-prompt-engineering/skill-development/promptcraft_specification_defines_done.md
---

# Run a Pre-Mortem on Correctness Before Shipping

**Objective:** Before shipping a prompt or AI system, imagine it has been running for three months and is producing wrong outputs. Walk backward from each plausible failure to the spec, prompt, eval, or monitoring gap that let it through. Produce a ranked list of failure modes with preventive edits and detection signals — each one tied to the actual deployment context, not to a generic AI-risk catalog. The artifact is a pre-ship checklist the user works through before deployment.

**When to use:**
- A prompt is moving from personal experimentation to a shared workflow, agent pipeline, or production feature.
- Stakes have risen — the downstream consumer is now acting on outputs rather than treating them as drafts.
- A previous incident exposed a failure the user wants to systematically avoid next time.

**Audience:** Prompt engineers, ML engineers, and developers shipping AI-powered features who own a prompt or system at the edge of shipping. Not useful upstream of a correctness definition — run `correctness_discovery_prompt.md` first if no spec exists.

---

## Inputs Required

1. **The prompt or system about to ship.** The exact text, configuration, and any tool / function schemas it uses.
2. **The correctness definition.** Produced by `correctness_discovery_prompt.md` or equivalent. If none exists, stop — a pre-mortem against an unnamed spec will invent failures the user doesn't actually care about.
3. **Deployment context.** Who runs the prompt (user / teammate / pipeline / end user), on what traffic volume, at what decision stakes, with what downstream consumer.
4. **At least 5 real past outputs of the prompt across varied inputs.** Good ones and bad ones. Shipping a pre-mortem on a prompt the user hasn't run is speculation.
5. **Known prior incidents or near-misses on this or adjacent tasks.** One paragraph each. If none exist, name that explicitly — the pre-mortem will lean harder on imagined failures and should be marked lower-confidence.

**Refuse the pre-mortem if:**
- No correctness definition exists. The pre-mortem is a coverage test of the spec; without a spec it's free-form worrying.
- The prompt has not been run against real inputs. Speculative pre-mortems on untested prompts invent failures that may not be real for this prompt.
- The deployment context is unnamed. Failure modes depend on who is acting on outputs; without a named consumer, severity can't be ranked.

---

## Instructions

### Step 1 — Imagine the headline three months out

One sentence. The most uncomfortable plausible headline about this system three months after shipping. "Incident review: automated summary told on-call the wrong customer was affected for 45 minutes." "Compliance flagged: output cited a regulation that didn't exist." "Users stopped trusting the digest because it quietly dropped items for a week."

The headline anchors the pre-mortem in the user's real threat model. It is not a generic AI-risk bullet.

### Step 2 — Walk backward from the headline to the gap

For the headline, ask: what specifically produced that outcome? Trace the chain from headline to gap:

- **Headline** (what the world saw).
- **Wrong output** (the specific output type that caused it).
- **Missing or weak specification** (which must-have, must-not, refusal condition, or tradeoff rule would have prevented it).
- **Missing or weak detection** (what signal, if monitored, would have caught it before 45 minutes passed).
- **Missing or weak recovery** (what control would have shortened the impact window).

This is the root-cause ladder: headline → output → spec gap → detection gap → recovery gap. Pre-mortems that stop at "the output was wrong" are not actionable.

### Step 3 — Generate 5–10 additional failure modes

Beyond the headline, generate 5–10 failure modes the prompt could produce. Source them from:

- **Spec gaps surfaced by `correctness_prompt_specification_audit.md`** (if run). These are evidence-grounded.
- **Adjacent-task incidents** the user has seen. Near-miss memory is high-signal.
- **Known model-capability failure modes** that apply to this task type (hallucinated citations for research tasks, over-refusal for medical, length drift for summaries, format drift for structured outputs). Drawn narrowly — do not enumerate the universe of AI failure modes.
- **The inverse of each must-have.** If a must-have is "names the affected user," the inverse failure mode is "names the wrong user" or "omits the user." Both should be tested.

Stop at 10. Pre-mortems that list 40 failure modes get ignored; ones with 5–10 get worked.

### Step 4 — Rank failure modes on severity × likelihood

For each failure mode, score:

- **Severity.** cosmetic / meaningful / high / critical. Based on the named consumer's decision and the downstream effect.
- **Likelihood.** unlikely / possible / likely / already observed. Grounded in the user's real past outputs or adjacent-task incidents.

Rank by (severity, likelihood). The top 3–5 are the pre-mortem's focus. The rest are logged as residual risk.

### Step 5 — Design preventive edits

For each top failure mode, propose one preventive edit. Each edit:

- Targets the spec, prompt, or architecture — name which.
- Is diff-sized, not a rewrite.
- Names which must-have, must-not, refusal condition, or tradeoff rule it adds or strengthens.
- Includes an explicit prediction: after this edit, on what share of cases does the failure mode still fire?

A preventive edit that claims to eliminate a failure mode is usually over-claiming. Models retain residual failure risk on most tasks; name the remaining share honestly.

### Step 6 — Design detection signals

For each top failure mode, propose one detection signal the user can actually monitor. Each signal:

- Is observable from data the user will actually have in production (outputs, user feedback, downstream telemetry, sampling review).
- Has a threshold for "investigate" and a threshold for "act."
- Names the response playbook (pause the system, route to human, log and continue).

Signals that require telemetry the user doesn't have are wishes, not controls. Stay within the user's actual observability.

### Step 7 — Design the dress rehearsal

Pick the top 1–2 failure modes. Design a test case that would have fired each failure in a pre-ship run. Run it before shipping:

- The input that should expose the failure.
- The expected wrong output pattern.
- The preventive edit applied.
- The expected corrected output.

A pre-mortem that isn't tested against at least one rehearsed case is a hope. The rehearsal converts it into evidence.

### Step 8 — Write the pre-ship checklist

Final artifact: a checklist the user works through before flipping the switch. Each item is a yes/no the user can verify in under 10 minutes. If any item is no, the ship is blocked until addressed or explicitly risk-accepted.

---

## Constraints

### Must
- Ground the pre-mortem in a named correctness definition and real past outputs.
- Trace every top failure mode through the full root-cause ladder (headline → output → spec gap → detection gap → recovery gap).
- Propose preventive edits as diff-sized changes tied to the spec.
- Design detection signals within the user's actual observability.
- Run at least one dress rehearsal before shipping.

### Must Not
- Generate generic AI-risk bullets that don't apply to this deployment.
- Claim a preventive edit eliminates a failure mode — name the residual share.
- Propose detection signals that depend on telemetry the user doesn't have.
- Produce more than 10 failure modes in the main list; top 3–5 get full treatment.
- Substitute the pre-mortem for the spec — the pre-mortem tests the spec's coverage, not the other way around.

---

## False-Positive Prevention

1. **Generic risk cataloging.** Importing the full AI-risk taxonomy produces a long list of irrelevant failures. Every failure mode must tie to the user's spec, deployment, or near-miss history.
2. **Un-actionable failure modes.** "The model might hallucinate" is not a failure mode — it's a category. The failure mode is what specifically the hallucination would look like in this output type and what decision it would corrupt.
3. **Over-claiming prevention.** Preventive edits rarely drop failure rates to zero. Requiring a named residual share per edit forces honesty and ensures the detection signal still has something to catch.
4. **Detection on telemetry the user doesn't have.** Proposing "monitor user trust" when the user has no trust signal in their pipeline is theatrical. Constrain signals to the user's actual observability.
5. **Severity inflation.** Everything feels critical before shipping. Forcing the severity scale (cosmetic / meaningful / high / critical) tied to the named consumer's decision calibrates the rank.
6. **Likelihood denial.** Failures the user finds uncomfortable feel "unlikely." Grounding likelihood in past outputs or adjacent incidents protects against this. If the failure has already been observed, it's not "unlikely."
7. **Pre-mortem without rehearsal.** A pre-mortem whose top failure mode has not been rehearsed is not tested. Skipping Step 7 turns the pre-mortem into a document exercise.
8. **Pre-mortem without ship block.** If the pre-ship checklist has no item that can block shipping, the pre-mortem is advisory at best. At least one checklist item must be a hard gate.

---

## Output Format

```markdown
## System under pre-mortem
[Prompt / system reference.]

## Correctness definition in use
[Reference / inline.]

## Deployment context
- Operator: [...]
- Traffic: [...]
- Consumer + decision: [...]
- Stakes: [...]

## Headline (three months out)
[One sentence.]

## Headline failure — root-cause ladder
- Headline: [...]
- Wrong output: [...]
- Spec gap: [...]
- Detection gap: [...]
- Recovery gap: [...]

## Failure-mode inventory (5–10)
| # | Failure mode | Source | Severity | Likelihood | Advances to top? |
|---|---|---|---|---|---|
| 1 | [...] | spec audit / prior incident / inverse must-have | [...] | [...] | yes / no |
| ... |

## Top failure modes (3–5) — full treatment

### Failure 1 — [name]
- **Root-cause ladder:** [...]
- **Preventive edit:** [where / what / residual share after edit]
- **Detection signal:** [signal / investigate threshold / act threshold / playbook]
- **Rehearsal:** [test input / expected wrong output / expected corrected output]

### Failure 2 — [...]
### ...

## Residual risks (logged, not treated)
- [failure mode] — [severity × likelihood] — [reason not advanced]

## Pre-ship checklist (hard gates marked *)
- [ ] * Correctness definition is current and signed off by the consumer.
- [ ] * Preventive edits for top failure modes are in the prompt / system.
- [ ] * Detection signals are wired into actual telemetry.
- [ ] * At least one rehearsal was run and passed.
- [ ] Residual risks are logged with revisit dates.
- [ ] Rollback / pause mechanism is tested.

## Date
[Timestamp.]
```

---

## Verification

- [ ] Correctness definition is in hand before the pre-mortem runs.
- [ ] Headline is specific to this deployment, not generic.
- [ ] Every top failure mode walks the full root-cause ladder.
- [ ] Every preventive edit names a residual share.
- [ ] Every detection signal is within the user's actual observability.
- [ ] At least one failure mode has been rehearsed against a real input.
- [ ] Pre-ship checklist has at least one hard gate.
- [ ] The main failure list has 5–10 items, not 40.
