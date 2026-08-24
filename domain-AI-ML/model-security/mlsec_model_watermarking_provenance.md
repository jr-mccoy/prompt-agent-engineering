---
title: "Model Watermarking and Output Provenance"
category: AI-ML/model-security
description: "Design watermarking, canaries, and output provenance for a model — deciding what claim you actually need to support, whether the evidence would survive an adversary and a dispute, and refusing to present attribution machinery as a deterrent."
techniques:
  - RT-02
  - CM-02
  - QA-12
  - DS-06
  - RT-05
difficulty: advanced
tags:
  - watermarking
  - provenance
  - canary
  - attribution
  - content-authenticity
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/model-security/mlsec_model_extraction_defense.md
  - domain-AI-ML/model-security/mlsec_ml_supply_chain_audit.md
  - domain-AI-ML/responsible-ai-governance/rai_governance_framework_design.md
  - domain-AI-ML/genai-llm-engineering/genai_guardrails_design.md
---

# Model Watermarking and Output Provenance

**Objective:** Decide what provenance claim a deployment actually needs to support — "this model is ours", "this output came from our model", or "this output is synthetic" — then design the mechanism that supports that specific claim, assess whether the evidence survives an adversary and a dispute, and state plainly that none of it prevents misuse.

**When to Use:**
- A model is exposed in a way that makes extraction or unauthorized redistribution plausible, and you want after-the-fact recourse.
- A regulatory, platform, or contractual obligation requires synthetic content to be identifiable.
- You are deciding whether watermarking is worth its cost, and need the case made honestly in both directions.

**When NOT to Use:**
- You want to *stop* extraction or misuse — watermarking is attribution, not prevention; use `mlsec_model_extraction_defense.md`.
- The requirement is disclosure to users that they are interacting with an AI system — that is an interface and governance question, not a watermarking one.
- No one would act on attribution evidence if you had it. Say so, and skip the cost.

## Inputs / Context

- **The claim you need to support** — exactly one of: this model is ours; this output came from our model; this output is machine-generated. Different claims need different mechanisms and are routinely conflated.
- **Who the claim is made to** — an internal team, a platform's trust-and-safety process, a customer, a regulator, or a court. This sets the evidentiary bar.
- **Adversary model** — whether the party you would make the claim against is indifferent, motivated to remove the mark, or expert.
- **Output modality** — text, image, audio, tabular scores, or weights themselves; robustness properties differ sharply.
- **Acceptable quality cost** — how much output degradation the deployment can absorb.
- **Detection access** — whether verification requires a secret key you hold, and who is permitted to run it.

## Constraints

**Must:**
- Fix the claim first and design to it; a mechanism that supports "this output is synthetic" will not support "this model is ours" in a dispute.
- State the evidentiary bar for the audience named, and assess whether the mechanism's output would meet it — including who verifies and whether the verification is reproducible by the other side.
- Assess robustness against the specific adversary: paraphrase, re-encoding, cropping, format conversion, fine-tuning, distillation, or quantization, as applicable to the modality.
- Report false-positive behaviour explicitly, since a provenance claim against an innocent party is a serious harm and the failure mode people forget.
- State the quality cost of any mechanism that alters outputs.

**Must Not:**
- Present watermarking as a deterrent or a control; it supports recourse after the fact and nothing else.
- Assert detection rates, robustness results, or removal-attack efficacy from memory; mark any needed figure `[verify against a primary source]`.
- Recommend a watermark whose verification depends on a secret you would have to disclose to use, without saying so.
- Claim a mark "survives fine-tuning" or "cannot be removed" — state the specific transformations tested and treat the rest as unknown.
- Design canaries that embed real personal data or real secrets as the marker.

**Instructions:**

1. **Fix the claim and the audience.** Write the exact sentence you would need to defend, and to whom. Everything else follows; a vague "we want watermarking" produces a mechanism that supports no specific claim.

2. **Choose the mechanism class for that claim.**
   - *This model is ours* — weight-space marks, or behavioural canaries: rare, deliberately chosen input→output pairs the model reproduces. These survive redistribution of the weights themselves.
   - *This output came from our model* — output-space watermarking at generation time, or logged output hashes for later matching.
   - *This output is machine-generated* — detectable watermarking plus, where applicable, signed content credentials at the file level.

3. **Assess robustness against the transformation set that matters.** For each realistic transformation of the modality — paraphrase and translation for text; crop, re-encode, and rescale for images; fine-tuning, distillation, pruning, and quantization for weights — state whether the mark is expected to survive, and which of these you have actually tested rather than assumed.

4. **Design the detection procedure and its statistics.** Specify what the detector needs (a key, a reference set, the original), the decision threshold, and the false-positive rate at that threshold. Then state the consequence of a false positive in this deployment, because the threshold should be set by that consequence rather than by convenience.

5. **Test the innocent-party case.** Run the detector against content that is genuinely not yours, including content from similar models. A detector that fires on a competitor's honest output is worse than no detector, and this test is the one most often skipped.

6. **Price the quality cost.** Where the mechanism alters outputs, measure the degradation on the metric that matters and check it against tolerance. Where it does not alter outputs (logging, canaries), say so — that is a genuine advantage.

7. **Assess the dispute path.** If you had a positive detection, what happens next? Who verifies, can the other party reproduce the verification, does the mechanism require disclosing a secret to use it in a dispute, and would the organization actually pursue it? A mechanism nobody would act on is a cost with no benefit.

8. **State what it does not do.** Explicitly: does not prevent extraction, does not prevent misuse, does not survive untested transformations, and does not establish intent.

**Output Format:**

A markdown design:
- **Claim & Audience** — the exact sentence, to whom, and the evidentiary bar.
- **Mechanism Selection** — table: Claim | Mechanism class | Why it fits | Quality cost.
- **Robustness Assessment** — table: Transformation | Expected survival | Tested? | Evidence.
- **Detection Procedure** — inputs required, threshold, FPR at threshold, consequence of a false positive.
- **Innocent-Party Test** — what was tested against and the result.
- **Dispute Path** — who verifies, reproducibility, secret-disclosure risk, willingness to act.
- **Explicit Non-Claims** — what this does not do.
- **Recommendation** — adopt, adopt narrowly, or decline, with the reason.

## Verification

- [ ] Exactly one claim is fixed, with its audience and evidentiary bar, before any mechanism is chosen.
- [ ] The mechanism class matches the claim rather than a general desire for watermarking.
- [ ] Robustness is assessed per transformation, with tested and assumed clearly separated.
- [ ] A detection threshold and its false-positive rate are stated.
- [ ] The innocent-party test is run and reported.
- [ ] Quality cost is measured, or its absence is stated.
- [ ] The dispute path names who verifies and whether the organization would act.
- [ ] Non-claims are stated explicitly, including that this is not prevention.
- [ ] No detection rates or removal-attack results are asserted from memory.
- [ ] No canary embeds real personal data or real secrets.

## False-Positive Prevention

❌ **DON'T:**
- Deploy watermarking to "discourage" theft — it changes nothing for an attacker who does not check, and its whole value is after the fact.
- Claim a mark survives fine-tuning or distillation without having tested those specific transformations on this model.
- Set the detection threshold for a good-looking detection rate; set it from the cost of accusing an innocent party.
- Skip testing against content from other models — a detector that cannot distinguish your output from a competitor's supports no claim at all.
- Conflate "this output is synthetic" with "this output is ours"; the second is a much stronger claim and needs a different mechanism.
- Build attribution machinery nobody would act on, and count it as a security control.

✅ **DO:**
- Write the sentence you need to defend and design backwards from it.
- Separate transformations you tested from those you assumed, and label the untested ones unknown.
- Set the threshold from the consequence of a false positive, and report the rate you actually get there.
- Test the detector against honest third-party content before trusting a single positive.
- Prefer mechanisms with no quality cost — logging and canaries — where they support the claim you need.
- State the non-claims prominently, so the mechanism is not later described as prevention.

## Example Output

```markdown
## Provenance Design: Licensed Image-Generation Model (partner distribution)
Weights are licensed to three partners under terms prohibiting redistribution and derivative
training.

### Claim & Audience
**Claim:** "The model producing these images is a derivative of our licensed weights."
**Audience:** contract dispute with a named partner; evidentiary bar is what our counsel would
put in front of an arbitrator — reproducible by a neutral expert, and by the other side.
Note this is *not* the claim "this image is AI-generated", which we do not need and which a
different mechanism would serve.

### Mechanism Selection
| Claim | Mechanism | Why it fits | Quality cost |
|---|---|---|---|
| Model is ours | **Behavioural canaries** — 40 rare prompt→output pairs fixed during fine-tuning | Survives redistribution *and* further fine-tuning better than output marks; needs only black-box access to test | None at inference |
| Model is ours (secondary) | Weight-space mark | Strong if weights are obtainable in a dispute | None |
| Output is ours | Output watermark | **Not selected** — partners legitimately post-process; marks would not survive, and the claim we need is about the model |

### Robustness Assessment
| Transformation | Expected survival | Tested? | Evidence |
|---|---|---|---|
| Redistribution unchanged | Yes | **Yes** | 40/40 canaries reproduce |
| Further fine-tuning, small dataset | Likely partial | **Yes** | 31/40 after 2k-step fine-tune |
| Further fine-tuning, large dataset | Degrades | **Yes** | 12/40 after 50k-step fine-tune |
| Distillation to a smaller model | Unknown | **No** | not tested — treat as unknown, not as survival |
| Quantization to 8-bit | Likely | **Yes** | 38/40 |
| Pruning | Unknown | **No** | not tested |

Twelve of forty surviving a large fine-tune is still far above chance for canaries chosen at
this rarity, but the claim weakens as the derivative moves further from the original — and
that should be said plainly rather than papered over.

### Detection Procedure
Query the suspect model with all 40 canary prompts; count matches under a fixed similarity
threshold. Requires only black-box API access — no key, no weights, no original.
**Threshold:** ≥8 of 40 matches. **FPR at that threshold:** measured at <0.1% against the
control set below. The threshold is set high because the consequence of a false positive is
a formal accusation against a commercial partner, not a dashboard alert.

### Innocent-Party Test
Ran the detector against: 4 open-weight image models we have no relationship with; 2 partner
models trained from a *different* base; and 1 internally trained model from a different
lineage. **Maximum matches: 2 of 40**, against a threshold of 8. The detector separates our
lineage from unrelated models with margin — without this test the threshold would have been
guesswork and a positive would have meant nothing.

### Dispute Path
Verification runs black-box, so a neutral expert **and the partner** can both reproduce it —
which is what makes it usable in arbitration rather than merely internally convincing. The
canary prompts must be disclosed to do so, which burns them for future disputes; they are
therefore treated as single-use evidence, and a second reserved set of 40 is held back and not
disclosed. Legal has confirmed they would pursue a clear result under the licence terms.

### Explicit Non-Claims
- Does **not** prevent redistribution, extraction, or derivative training.
- Does **not** establish intent — a positive shows lineage, not that anyone knowingly breached.
- Does **not** cover distillation or pruning; those are untested and must be treated as unknown.
- Does **not** identify individual generated images as ours; that is a different claim we chose
  not to pursue.

### Recommendation
**Adopt** behavioural canaries with the reserved second set. Decline output watermarking — it
does not support the claim we actually need and would be destroyed by legitimate partner
post-processing. Add distillation and pruning to the test backlog before the next licence
renewal, since both are plausible evasion routes and both are currently unknown.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** claim × mechanism × transformation × audience is the design grid.
- **CM-02 (Constraint Specification):** the fix-the-claim-first rule and the non-claims section bound what the mechanism may be said to do.
- **QA-12 (False Positives Identification):** the innocent-party test and threshold-from-consequence rule guard the failure mode that matters most here.
- **DS-06 (Prioritization and Severity Guidance):** mechanisms are ranked by the claim they support and the cost they carry.
- **RT-05 (Evidence-Based Reasoning):** tested and assumed transformations are held apart throughout.

**Related Prompts:**
- `mlsec_model_extraction_defense.md` — the prevention-side controls this complements but does not replace.
- `mlsec_ml_supply_chain_audit.md` — provenance of what goes *into* the model rather than what comes out.
- `../responsible-ai-governance/rai_governance_framework_design.md` — where a provenance obligation is recorded and owned.
- `../genai-llm-engineering/genai_guardrails_design.md` — runtime controls on generated content.
