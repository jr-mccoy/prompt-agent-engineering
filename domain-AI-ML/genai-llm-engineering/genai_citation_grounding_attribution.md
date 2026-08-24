---
title: "Citation Grounding and Attribution"
category: AI-ML/genai-llm-engineering
description: "Make a generated answer verifiably traceable to its sources — distinguishing citation presence from citation correctness, verifying that each cited passage actually supports its claim, and handling the claims no retrieved source supports."
techniques:
  - ST-02
  - DS-02
  - QA-12
  - CM-02
  - RT-05
difficulty: advanced
tags:
  - citation
  - attribution
  - grounding
  - hallucination
  - rag
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_rag_evaluation_harness.md
  - domain-AI-ML/genai-llm-engineering/genai_guardrails_design.md
  - domain-AI-ML/genai-llm-engineering/genai_llm_as_judge_design.md
  - domain-AI-ML/genai-llm-engineering/genai_rag_system_design.md
---

# Citation Grounding and Attribution

**Objective:** Produce answers whose claims can be checked against their sources — separating *citation present* from *citation correct*, verifying that each cited passage genuinely supports the sentence attached to it, and defining what happens to claims no retrieved source supports.

**When to Use:**
- Users must be able to verify an answer, and a plausible citation that does not support its claim is worse than none.
- A RAG system already emits citations and nobody has checked whether they are correct.
- Regulatory, professional, or editorial context makes traceability a requirement rather than a nicety.

**When NOT to Use:**
- The retrieval quality itself is the problem — citations cannot ground an answer on documents that were never retrieved; use `genai_rag_retrieval_quality_debug.md`.
- You need general output guardrails rather than attribution specifically — use `genai_guardrails_design.md`.
- The answer is genuinely generative — a summary, a draft — with no factual claim to attribute.

## Inputs / Context

- **Verification behaviour** — what a user actually does with a citation: click through, spot-check, or never look. This sets how much precision is worth buying.
- **Citation granularity required** — document, section, passage, or sentence level.
- **Answer shape** — extractive, synthesized from several sources, or multi-hop reasoning across them.
- **Consequence of an unsupported claim** — what happens when a confidently cited statement is wrong.
- **Source characteristics** — length, structure, and whether passages are self-contained.
- **Latency and cost budget** for any verification pass.

## Constraints

**Must:**
- Distinguish **citation presence** from **citation correctness** in every measurement. A system that cites on every sentence and attaches the wrong source to a third of them is more dangerous than one that cites nothing, because it manufactures unearned confidence.
- Verify entailment: does the cited passage actually support the specific claim? Presence of a plausible-looking reference is not support.
- Define behaviour for **unsupported claims** — claims the model produced that no retrieved passage backs. Options are to remove, mark as unsupported, or refuse; silently emitting them uncited is the failure mode this prompt exists to prevent.
- Measure at the granularity users verify at; document-level citations on a 40-page document are not verifiable in practice.
- Handle synthesized claims explicitly — a statement combining two sources needs both, and multi-hop claims may be supported by no single passage.

**Must Not:**
- Assert grounding-rate figures, benchmark results, or citation-accuracy norms from memory; mark quantities `[measure on your system]`.
- Report a citation rate as a grounding metric; it counts references, not correctness.
- Use the generating model as the sole judge of its own citations without validating that judge against human labels.
- Allow citation of a source that was retrieved but not actually placed in the generator's context.
- Treat a correct answer with a wrong citation as acceptable; it teaches users to trust an unreliable link.

**Instructions:**

1. **Establish what verification the user performs.** Click-through, spot-check, or none. If users never verify, the value of citations is signalling trust — which makes an incorrect citation actively harmful rather than merely unhelpful, and raises the required precision.

2. **Set the granularity.** Passage or sentence level for genuine verifiability; document level only where documents are short. State the granularity and check it is one a user can actually act on.

3. **Design the generation-side grounding.** Instruct the model to attribute per claim, to cite only from provided context, and to mark claims it cannot support. Include the explicit instruction that not answering is preferable to answering uncited — a permission most prompts fail to give.

4. **Build the verification pass — the part that turns citations into evidence.** For each claim–citation pair, check whether the cited passage entails the claim. Options: a natural-language-inference model, an LLM judge with a rubric, or human review on a sample. State the method and its own measured accuracy against human labels, because an unvalidated judge simply relocates the trust problem.

5. **Classify every claim.** *Supported* — cited and entailed. *Miscited* — cited but the passage does not support it. *Unsupported* — no citation and no supporting passage. *Uncited but supported* — a passage supports it but no citation was attached. Report all four; the miscited class is the dangerous one and is invisible in a citation-rate metric.

6. **Decide the handling of unsupported claims.** Remove them, mark them visibly as unsupported, or refuse the answer entirely. This is a product decision with real trade-offs and must be made deliberately rather than defaulted.

7. **Handle synthesis and multi-hop.** A claim combining sources needs all of them cited. A multi-hop conclusion may be supported by no single passage — decide whether to permit it with the chain cited, or to require single-passage support and lose the capability.

8. **Measure and report the four classes**, plus per-claim-type breakdown, on a held-out set with human-labelled ground truth for at least a sample.

9. **Set the user-facing presentation.** How citations appear, how unsupported content is marked, and how a user reaches the source. Precision here matters: a citation that opens a 40-page PDF at page one is technically present and practically useless.

**Output Format:**

A markdown design:
- **Verification Behaviour** — what users do, and the precision implied.
- **Granularity** — level chosen and its verifiability.
- **Generation-Side Grounding** — instructions and permitted behaviours.
- **Verification Method** — mechanism and its accuracy against human labels.
- **Claim Classification** — table: Class | Definition | Rate | Handling.
- **Unsupported-Claim Policy** — remove, mark, or refuse, with the reason.
- **Synthesis & Multi-Hop Policy** — what is permitted and how cited.
- **Measurement** — held-out results by claim type.
- **Presentation** — how citations and unsupported content appear.

## Verification

- [ ] Citation presence and citation correctness are measured separately.
- [ ] Entailment is checked per claim–citation pair.
- [ ] The verification method's own accuracy is measured against human labels.
- [ ] All four claim classes are reported, including miscited.
- [ ] Unsupported-claim handling is decided explicitly.
- [ ] Synthesis and multi-hop claims have a stated policy.
- [ ] Granularity is one a user can act on.
- [ ] Citations are restricted to sources actually placed in context.
- [ ] Presentation lets a user reach the specific supporting text.
- [ ] No grounding rates or benchmark figures are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Report "94% of sentences carry a citation" as a grounding result — that measures the presence of references, and says nothing about whether any of them support what they are attached to.
- Let the generating model grade its own citations without validating that judge against human labels; you have moved the trust problem, not solved it.
- Cite at document level on long documents and call the answer verifiable; a user cannot check a claim against 40 pages.
- Allow citation of a retrieved-but-not-in-context source; the model did not see it, so any apparent support is coincidence.
- Emit unsupported claims silently alongside cited ones — users cannot tell them apart, and the cited ones lend them credibility.
- Accept a correct answer with a wrong citation; it trains users to trust a link that will eventually mislead them.

✅ **DO:**
- Measure the miscited rate specifically; it is the class that does the damage and the one citation-rate metrics conceal.
- Validate the entailment judge against human labels before trusting its numbers.
- Give the model explicit permission to mark a claim unsupported rather than manufacture a citation.
- Decide the unsupported-claim policy as a deliberate product choice.
- Set a policy for synthesized and multi-hop claims rather than letting them fall through.
- Present citations so the user lands on the supporting text, not the document.

## Example Output

```markdown
## Citation Design: Clinical Guideline Assistant
Answers clinician questions from an internal guideline corpus.

### Verification Behaviour
Clinicians **do** click through — the professional context requires it, and answers are used to
support decisions they are accountable for. High click-through raises the cost of a miscitation
sharply: a wrong link is discovered, and it costs trust in every other answer the system gives.

### Granularity
**Passage level with anchor links** to the specific paragraph. Document-level citation to a
120-page guideline would be technically present and practically useless — the clinician would
have to search the document to check a single claim, which is the work the citation was meant
to remove.

### Generation-Side Grounding
Instructions to the generator:
- Attribute **each factual claim** to a specific provided passage.
- Cite **only** from the provided context; never from parametric knowledge.
- **Explicitly permitted:** mark a claim `[unsupported by provided sources]` rather than
  producing a citation for it. Without this permission the model will manufacture a plausible
  citation, because answering fully reads as the more helpful behaviour.
- Where a claim synthesizes two passages, cite both.

### Verification Method
Separate entailment check per claim–citation pair, using an LLM judge with a rubric.
**The judge's own accuracy is measured against 200 human-labelled pairs** `[measure]`. An
unvalidated judge would simply relocate the trust question from the generator to the judge, and
report a confident number about nothing.

### Claim Classification
| Class | Definition | Rate | Handling |
|---|---|---|---|
| Supported | cited, and the passage entails the claim | `[measure]` | show normally |
| **Miscited** | cited, passage does **not** entail | `[measure]` | **blocking — must be near zero** |
| Unsupported | no citation, no supporting passage | `[measure]` | mark visibly (see policy) |
| Uncited but supported | a passage supports it, no citation attached | `[measure]` | attach citation in post-processing |

The **miscited** rate is the metric this whole design exists to control. A system with 95%
citation coverage and a 6% miscitation rate is worse in this setting than one that cites half as
often and is never wrong, because clinicians will find the wrong ones.

### Unsupported-Claim Policy
**Mark visibly, do not remove.** Clinical questions frequently have no guideline answer, and
silence is misleading in a different way — the clinician needs to know the guidelines are silent,
which is itself clinically relevant. Unsupported content is rendered in a visually distinct block
with the label "not covered by the guideline corpus". Removal was rejected because it would make
guideline gaps invisible.

### Synthesis & Multi-Hop Policy
Synthesized claims are permitted with **all** contributing passages cited. **Multi-hop
conclusions are not permitted** — where a conclusion follows from two passages but is stated in
neither, the system presents both passages and lets the clinician draw the inference. This
deliberately gives up a capability, and in this setting that is the right trade: an inference the
system makes is an inference the clinician did not, in a decision they carry.

### Measurement
Held-out set with human-labelled ground truth, reported by claim type:
| Claim type | Supported | Miscited | Unsupported | Uncited-but-supported |
|---|---|---|---|---|
| Dosing | `[measure]` | `[measure]` | `[measure]` | `[measure]` |
| Contraindication | `[measure]` | `[measure]` | `[measure]` | `[measure]` |
| Procedural | `[measure]` | `[measure]` | `[measure]` | `[measure]` |
| Definitional | `[measure]` | `[measure]` | `[measure]` | `[measure]` |

Contraindication claims warrant the tightest miscitation bar, since that is where a wrong link
maps most directly onto patient harm.

### Presentation
Each claim carries an inline marker linking to the **specific paragraph**, with the guideline
name and section visible without clicking. Unsupported blocks are visually distinct and labelled.
Hovering shows the supporting sentence, so the common case — a quick check — needs no navigation
at all.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** generation-side grounding precedes verification, which precedes classification and handling.
- **DS-02 (Metric Specification):** the four claim classes are defined as distinct measured quantities, with miscitation as the controlling one.
- **QA-12 (False Positives Identification):** separates citation presence from correctness, which is the central confusion in grounding work.
- **CM-02 (Constraint Specification):** the cite-only-from-context and permission-to-abstain rules bound the generator.
- **RT-05 (Evidence-Based Reasoning):** entailment, not plausibility, is the standard a citation must meet.

**Related Prompts:**
- `genai_rag_evaluation_harness.md` — where these grounding metrics live alongside retrieval and answer quality.
- `genai_llm_as_judge_design.md` — designing and validating the entailment judge.
- `genai_guardrails_design.md` — the wider output-control layer.
- `genai_rag_system_design.md` — the pipeline this attribution sits inside.
