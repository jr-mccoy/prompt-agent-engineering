---
title: "Logical Fallacy Scan — Detect Named Fallacies With Cited Evidence"
category: reasoning-craft/epistemic
description: "Scan a passage against a catalog of ~15 named logical fallacies, quoting the offending sentence for each candidate and distinguishing the mere rhetorical use of a fallacy from genuine commission (where the argument's conclusion actually depends on the bad inference). Counters the failure mode of fallacy-spotting as a debate weapon — labeling without quoting, and treating every rhetorical flourish as a load-bearing logical error."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - epistemic
  - logical-fallacy
  - argument-analysis
  - critical-thinking
  - audit
updated: "2026-05-21"
reasoning:
  styles: [analytical, diagnostic, adversarial]
  stakes: variable
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: per_fallacy_verdict_table
  user_role: [analyst, researcher, editor, individual, executive]
  mode: [audit, diagnose]
related_prompts:
  - domain-reasoning-craft/epistemic/epistemic_claim_inference_separator.md
  - domain-reasoning-craft/reasoning-moves/reasoning_argument_map_toulmin.md
  - domain-reasoning-craft/reasoning-moves/reasoning_premise_audit.md
---

# Logical Fallacy Scan

**Objective:** Scan a passage for named logical fallacies. For each candidate fallacy, check whether its diagnostic signature is present, quote the exact offending sentence, and classify it as either a rhetorical *use* (a stylistic move that doesn't undermine the argument's logic) or a genuine *commission* (the conclusion actually depends on the bad inference). Output a per-fallacy verdict with severity and a repair suggestion if the author wants to keep the conclusion. The discipline of quoting and distinguishing use from commission is what separates this from fallacy-spotting as a rhetorical weapon.

**When to use:**
- Auditing a persuasive piece — op-ed, position paper, pitch, expert testimony, marketing claim — for logical soundness.
- Reviewing your own argument before publishing, to find where the logic is doing less work than the rhetoric.
- A claim feels persuasive but you can't articulate what's wrong; the catalog helps name it.
- Teaching or feedback contexts where naming the specific fallacy is more useful than "this is weak."

**When NOT to use:**
- You want to dismiss an argument you dislike by hunting for any label to attach — that's the anti-pattern this prompt guards against.
- The disagreement is about facts or values, not reasoning structure — a fallacy scan won't resolve it (use `epistemic_disagreement_diagnosis.md`).
- You need the full argument structure (claims, evidence, warrants) — use `reasoning_argument_map_toulmin.md` or `epistemic_claim_inference_separator.md`.

**Audience:** Analysts, editors, researchers, and anyone evaluating or sharpening a persuasive argument.

---

## Inputs / Context

1. **The passage.** The text to scan (the argument, op-ed, claim, transcript excerpt). Provide it verbatim so sentences can be quoted.
2. **The author's conclusion.** What the passage is trying to establish — needed to judge whether a fallacy is load-bearing.
3. **Purpose of the scan.** Self-audit, review of someone else's work, or teaching — affects tone of the repair suggestions.
4. **Specific fallacies to prioritize (optional).** If the user suspects particular ones.

---

## Fallacy catalog (with diagnostic signature)

- **Ad hominem** — attacks the arguer instead of the argument. Signature: a claim is rebutted by a fact about its source's character/motive rather than its content.
- **Straw man** — refutes a weakened or distorted version of the opponent's position. Signature: the rebutted claim is not the claim actually made.
- **False dichotomy** — presents two options as exhaustive when more exist. Signature: "either X or Y" where Z is available.
- **Slippery slope** — asserts a chain of consequences without justifying each link. Signature: "A leads to Z" skipping B–Y.
- **Appeal to authority (illegitimate)** — cites authority outside its domain or against consensus. Signature: expertise invoked where it doesn't apply, or one authority vs the field.
- **Appeal to nature** — treats "natural" as "good/correct." Signature: naturalness substituted for an argument about value or effect.
- **Equivocation** — a key term shifts meaning across the argument. Signature: the same word carries two senses, and the conclusion needs both.
- **Hasty generalization** — broad conclusion from a small or biased sample. Signature: "n=few" → universal claim.
- **No true Scotsman** — redefines a category to exclude counterexamples. Signature: a counterexample is dismissed by redefining the term.
- **Post hoc** — treats sequence as causation. Signature: "B followed A, so A caused B" with no mechanism or control.
- **Motte and bailey** — defends a modest claim (motte) but uses it to assert a stronger one (bailey). Signature: retreat to the defensible claim under challenge, then re-advance the strong one.
- **Gish gallop** — overwhelms with many weak claims so none can be addressed. Signature: volume substituting for weight.
- **Weak analogy** — an analogy whose relevant structure doesn't transfer. Signature: surface similarity carrying an inference the deep structure doesn't support.
- **Sunk cost** — justifies continuing by past investment. Signature: "we've already put in X" as a forward-looking reason.
- **Base-rate neglect** — case features dominate the base rate. Signature: a high posterior with no reference to how common the phenomenon is.

> **Routing note:** Sunk cost and base-rate neglect are cognitive biases that surface in written arguments, which is why they appear in this catalog; to audit your own reasoning *process* for them, use `epistemic_bias_specific_audit.md`.

---

## Constraints

### Must
- For each candidate fallacy flagged, **quote the exact sentence(s)** that triggered the flag. No quote, no flag. Exception: passage-level patterns (gish gallop) have no single triggering sentence — flag them by citing the claim count/density across the passage instead.
- Classify each as **use** (rhetorical, conclusion survives without it) or **commission** (the conclusion genuinely depends on the bad inference). Only commissions threaten the argument.
- Rate **severity**: how much the conclusion's support degrades if the fallacy is removed.
- Offer a **repair**: how the author could re-support the conclusion legitimately, if it can be saved.
- Cover only fallacies actually present. A clean scan that finds nothing is a valid and important result.

### Must Not
- Label a fallacy without quoting the offending text.
- Treat every rhetorical move as a logical failure. A vivid analogy or a sharp characterization is not automatically a fallacy.
- Use fallacy names as a way to dismiss a conclusion you simply disagree with on other grounds.
- Confuse "the argument contains a fallacy" with "the conclusion is false." A badly argued claim can still be true (it's just unsupported by *this* argument).
- Pile on — if the same fallacy appears five times, note the pattern once, don't inflate the count.

---

## Instructions

### Step 1 — Restate the author's conclusion
One sentence. Everything downstream judges whether a fallacy is load-bearing for *this* conclusion.

### Step 2 — Pass through the catalog
For each fallacy, ask: is the diagnostic signature present anywhere in the passage? Where it is, capture the sentence.

### Step 3 — Quote and locate
For each flagged candidate, quote the triggering sentence(s) verbatim.

### Step 4 — Use vs commission
Decide: if you deleted this move, would the conclusion still be supported? If yes → **use** (rhetorical). If no → **commission** (the conclusion rests on it). Only commissions are serious.

### Step 5 — Severity
Rate how much support the conclusion loses if the commission is removed: cosmetic / moderate / load-bearing.

### Step 6 — Repair
For each commission, suggest how the author could legitimately re-establish the conclusion (gather the missing evidence, restate without the equivocal term, narrow the generalization) — or note that the conclusion can't be saved by this argument.

### Step 7 — Summary verdict
State whether the argument's conclusion is adequately supported once the fallacies are accounted for, and which one or two commissions matter most.

---

## False-Positive Prevention

1. **Label without quote.** Naming a fallacy without citing the sentence is fallacy-spotting theater. Always quote.
2. **Use/commission conflation.** Treating a rhetorical flourish as a logical defect. A colorful straw-manning aside that the argument doesn't actually rely on is a *use*, not a *commission*.
3. **Fallacy-as-dismissal.** Using "that's a slippery slope!" to avoid engaging the actual claim. The scan is a diagnostic, not a rebuttal generator.
4. **Fallacy-fallacy.** Inferring the conclusion is false because the argument is fallacious. The conclusion may be true on better grounds; the scan judges *this* argument's support only.
5. **Over-detection.** Forcing a fallacy onto every sentence. Reasonable arguments contain few or no commissions; a clean result is legitimate.
6. **Pattern inflation.** Counting the same repeated fallacy as many separate findings. Note the pattern once.
7. **Domain blindness on authority.** Flagging "appeal to authority" when the authority is genuinely on-domain and consensus-aligned — that's legitimate evidence, not a fallacy.
8. **Repair omission.** Diagnosing without offering a path to legitimately support the conclusion, where one exists.

---

## Output Format

```
# Logical fallacy scan — [source]

## Author's conclusion
[One sentence]

## Findings
| # | Fallacy | Quoted text | Use or commission | Severity | Repair |
|---|---------|-------------|-------------------|----------|--------|
| 1 | [name]  | "[verbatim]"| commission        | load-bearing | [how to re-support] |
| 2 | [name]  | "[verbatim]"| use               | cosmetic | n/a |
| … |         |             |                   |          |        |

## Pattern notes
[Any fallacy that recurs, noted once]

## Verdict
- Conclusion adequately supported after accounting for fallacies? [yes / no / partially]
- The 1–2 commissions that matter most: [which, and why]
- Reminder: a fallacious argument does not make the conclusion false — it makes it unsupported by this argument.
```

---

## Verification

- [ ] Author's conclusion restated before scanning.
- [ ] Every flagged fallacy has a verbatim quote.
- [ ] Each flag classified as use or commission.
- [ ] Severity rated for each commission.
- [ ] Repair offered for each commission (or "not salvageable by this argument").
- [ ] No fallacy labeled purely to dismiss a disliked conclusion.
- [ ] Fallacy-fallacy explicitly avoided (fallacious ≠ false).
- [ ] Clean findings reported honestly where the argument is sound.
