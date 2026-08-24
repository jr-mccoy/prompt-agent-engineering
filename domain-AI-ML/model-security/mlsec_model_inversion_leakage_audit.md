---
title: "Model Inversion and Memorization Leakage Audit"
category: AI-ML/model-security
description: "Audit what a model reconstructs or regurgitates from its training data — separating genuine memorization from plausible-looking generation, testing extraction against known-planted content, and reporting per-record risk rather than a corpus-level average."
techniques:
  - RT-02
  - QA-12
  - RT-05
  - CM-02
  - DS-06
difficulty: advanced
tags:
  - model-inversion
  - memorization
  - data-extraction
  - attribute-inference
  - canary
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/model-security/mlsec_membership_inference_defense.md
  - domain-AI-ML/responsible-ai-governance/rai_privacy_pii_assessment.md
  - domain-AI-ML/responsible-ai-governance/rai_machine_unlearning_deletion.md
  - domain-AI-ML/data-for-ml/mldata_data_quality_audit.md
---

# Model Inversion and Memorization Leakage Audit

**Objective:** Establish what a model can be induced to reveal about the *content* of its training data — reconstructed inputs, inferred attributes, or verbatim regurgitation — while rigorously separating genuine memorization from output that merely looks like training data, and reporting risk per record rather than as a corpus average.

**When to Use:**
- A generative or high-capacity model was trained on data containing secrets, personal information, or licensed content.
- A deletion, unlearning, or right-to-erasure request needs evidence about what the model still holds.
- Before releasing model weights, since weight release removes every serving-side control at once.

**When NOT to Use:**
- The question is whether a record was *present* rather than what it contained — use `mlsec_membership_inference_defense.md`.
- The training corpus is public and non-sensitive, and regurgitating it harms nobody — record that and stop.
- You need a legal or regulatory determination rather than a technical measurement — route to `domain-legal/` with this audit as input.

## Inputs / Context

- **What would be harmful to reveal** — named categories: credentials, personal identifiers, health or financial details, licensed text, confidential business content. Without this the audit has no target.
- **Model type and access** — generative or discriminative; whether callers see generations, probabilities, embeddings, or weights.
- **Training corpus characteristics** — size, duplication rate, and whether rare high-entropy strings (keys, account numbers) are present.
- **Known-planted content** — any canaries deliberately inserted before training; if none exist, note it, because their absence limits what this audit can conclude.
- **Deduplication history** — what deduplication was applied and at what granularity, since duplication is the strongest driver of memorization.
- **Deployment surface** — prompt-controllable or fixed inputs, and whether callers can iterate.

## Constraints

**Must:**
- Distinguish **verbatim memorization** (exact reproduction), **approximate memorization** (recoverable content with variation), and **plausible generation** (output resembling training data without being it). Only the first two are leakage.
- Verify every suspected leak against the actual training corpus before calling it memorization; an unverified match is a hypothesis.
- Use planted canaries with known entropy where available, because they give a measurable extraction rate that natural-text matching cannot.
- Report **per-record** risk for the sensitive categories, since one extractable credential matters and a corpus-average extraction rate does not.
- State the extraction effort assumed — a leak reachable in one query is a different finding from one requiring a targeted, informed prompt.

**Must Not:**
- Report a model output as leaked training data without corpus verification — high-entropy-looking output is frequently generated, not recalled.
- Quote memorization rates, extraction-success figures, or published corpus-contamination results from memory; mark any needed figure `[verify against a primary source]`.
- Reproduce any actual extracted secret, credential, or personal record in the report; report the finding with the value redacted and a stable reference.
- Conclude that deduplication removed memorization without testing, or that a model "does not memorize" from a null result on a small probe set.
- Provide reusable extraction prompts or a procedure optimized for pulling secrets out of a model.

**Instructions:**

1. **Name the harmful categories.** List what would actually be damaging to reveal, with an example shape for each (a key format, an identifier pattern, a licensed-text signature). Everything downstream targets these.

2. **Inventory the memorization drivers.** Duplication rate, presence of rare high-entropy strings, model capacity relative to corpus size, and training epochs. These predict where leakage will concentrate before any probing.

3. **Design the probe set against the categories, not at random.** For each harmful category, construct probes that a realistic adversary would use: prefix continuation where a format is predictable, structured elicitation for attribute inference, and targeted probing where the attacker holds partial knowledge. State the effort each represents.

4. **Use canaries where they exist.** Planted strings of known entropy inserted before training give a defensible extraction rate. Report the rate against entropy and duplication count. If no canaries were planted, say so and note that the audit can demonstrate leakage but cannot bound it.

5. **Verify every candidate against the corpus.** For each suspected leak, search the training data for an exact or near match. Classify as verbatim, approximate, or unverified. **Unverified candidates are not findings** — this step is what separates an audit from an anecdote.

6. **Assess attribute inference separately.** Beyond reconstruction, test whether a sensitive attribute can be inferred for a record from model behaviour. This leaks without any verbatim reproduction and is missed by matching-based methods entirely.

7. **Score per record and per category.** For each harmful category: how many distinct records are extractable, at what effort, with what confidence. Lead with the highest-severity single extraction rather than an average.

8. **Recommend mitigations against the observed driver.** Corpus-side deduplication and secret scrubbing before training; training-side capacity, epoch, and DP choices; serving-side output filtering and rate limits. Note that **weight release removes every serving-side control**, so a model destined for release must be mitigated upstream.

9. **State the limits of the audit.** Which categories were probed, at what effort, and what a stronger or better-informed adversary might reach. A null result under weak probing is not evidence of absence.

**Output Format:**

A markdown audit:
- **Harmful Categories** — what would be damaging, with example shapes.
- **Memorization Drivers** — duplication, entropy, capacity, epochs.
- **Probe Design** — table: Category | Probe type | Effort assumed | Realistic adversary?
- **Canary Results** — extraction rate by entropy and duplication count, or a statement that none were planted.
- **Verified Findings** — table: Category | Classification (verbatim/approximate) | Records affected | Effort | Corpus-verified? | Redacted reference.
- **Attribute Inference** — attributes recoverable without reproduction.
- **Per-Record Risk** — the worst single extraction, led with.
- **Mitigations** — mapped to the observed driver, with the weight-release caveat.
- **Audit Limits** — what was not probed and what a stronger adversary might reach.
- **INSUFFICIENT EVIDENCE** — the correct classification for any output that looks like training data but could not be checked against the corpus. A model producing a plausible-looking record and a model reproducing a real one are different findings with different consequences, and only corpus verification separates them. Name the unblocking datum: corpus search access, or planted canaries if the corpus cannot be searched.

## Verification

- [ ] Harmful categories are named before probing, and probes target them.
- [ ] Every finding is classified verbatim / approximate / plausible-generation.
- [ ] Every claimed leak is verified against the training corpus; unverified candidates are excluded from findings.
- [ ] Canary results are reported with entropy and duplication count, or their absence is stated as a limit.
- [ ] Attribute inference is assessed separately from reconstruction.
- [ ] Risk is reported per record for sensitive categories, and the worst case leads.
- [ ] No actual secret, credential, or personal record is reproduced in the report.
- [ ] Mitigations address the observed driver; the weight-release caveat is stated where relevant.
- [ ] The audit's own limits are stated, including that a null result is not absence.
- [ ] No memorization or extraction rates are asserted from memory.
- [ ] Outputs resembling training data that could not be checked against the corpus are classified INSUFFICIENT EVIDENCE — neither confirmed as extraction nor dismissed as plausible generation.

## False-Positive Prevention

❌ **DON'T:**
- Report a plausible-looking credential the model generated as a leak — high-entropy output is generated far more often than recalled, and this is the single most common error in memorization audits.
- Skip corpus verification because a match "obviously" came from training; obviousness is not verification.
- Report a corpus-level extraction rate when the concern is one credential — the average is irrelevant to the record that matters.
- Conclude no memorization from a small random probe set; probes must target the harmful categories or they test nothing.
- Paste the extracted secret into the report to demonstrate the finding — the report then becomes the disclosure.
- Recommend only serving-side filtering for a model whose weights will be published.

✅ **DO:**
- Verify every candidate against the corpus and label the ones you could not verify as unverified.
- Separate verbatim from approximate from plausible, and count only the first two as leakage.
- Use planted canaries where they exist, and state the audit's weakened conclusions where they do not.
- Report the worst single extraction with its effort, and let the average be secondary.
- Redact values and use stable references so a finding can be re-checked without republishing the secret.
- Match mitigations to the driver you measured — duplication, capacity, or epochs — and put them upstream of any weight release.

## Example Output

```markdown
## Memorization Audit: Internal Code-Assistant Model (fine-tuned on company repositories)
Fine-tuned on ~4.1M files from internal repos. Weight release to a partner is under discussion,
which is what makes this audit blocking rather than advisory.

### Harmful Categories
| Category | Example shape |
|---|---|
| Cloud credentials | provider-prefixed key strings |
| Internal hostnames & endpoints | `*.internal.<company>` |
| Customer identifiers | 12-char alphanumeric account refs |
| Licensed third-party source | vendor SDK files under a non-redistribution licence |

### Memorization Drivers
Duplication is the dominant driver here: config templates appear in **~2,800 near-identical
copies** across repos, and secret-bearing files were **not** excluded before fine-tuning.
3 epochs at high capacity relative to corpus size. Deduplication was applied at whole-file
granularity only, which leaves near-duplicates and repeated fragments intact.

### Probe Design
| Category | Probe type | Effort assumed | Realistic adversary? |
|---|---|---|---|
| Cloud credentials | prefix continuation from known key prefixes | Low — one query | Yes — prefix format is public |
| Hostnames | prefix continuation from domain suffix | Low | Yes |
| Customer identifiers | structured elicitation with partial ref | Medium — attacker holds a partial | Yes — partner would |
| Licensed source | filename + header continuation | Low | Yes |

### Canary Results
Twelve canaries (high-entropy, format-matched to credentials) were planted before fine-tuning
at duplication counts 1, 4, 16, and 64.
| Duplication count | Canaries extracted |
|---|---|
| 1 | 0 / 3 |
| 4 | 0 / 3 |
| 16 | **2 / 3** |
| 64 | **3 / 3** |

Extraction turns on at roughly 16 duplicates in this setup. This is the audit's most useful
number because it converts a vague worry into a corpus-side threshold we can act on.

### Verified Findings
| Category | Classification | Records | Effort | Corpus-verified | Reference |
|---|---|---|---|---|---|
| Cloud credentials | **verbatim** | 4 distinct keys | 1 query | Yes — exact match, 22–41 dupes each | `FIND-001..004` (values redacted) |
| Internal hostnames | verbatim | 61 distinct | 1 query | Yes | `FIND-005` |
| Customer identifiers | approximate | 0 confirmed | medium | — | see below |
| Licensed source | verbatim | 2 files, ~40 lines each | 1 query | Yes | `FIND-006..007` |

**Excluded as plausible generation:** 37 further credential-shaped strings were produced that
matched *no* corpus entry. Reporting those as leaks would have inflated the finding roughly
tenfold and sent the team hunting for keys that were never in the training data.

### Attribute Inference
Given a partial customer reference, the model completes the internal environment and region
for that customer at a rate well above chance, without reproducing any full identifier. This
leaks customer-to-environment mapping with **no verbatim reproduction at all**, so a
matching-based audit alone would have reported this category clean.

### Per-Record Risk
The worst single finding is a **live-format cloud credential recoverable in one query from a
public prefix**. One extractable credential is the finding; the corpus-level rate is not the
story and should not be quoted as reassurance.

### Mitigations
- **Corpus-side (required before any release):** secret-scan and scrub before fine-tuning;
  deduplicate at fragment rather than whole-file granularity, targeting the ~16-duplicate
  threshold the canaries identified; exclude the non-redistributable vendor SDK.
- **Training-side:** reduce epochs; re-run canaries after each change to confirm the threshold moved.
- **Serving-side:** output filters for credential and hostname patterns — **note this does
  nothing for the partner weight release**, which removes every serving-side control at once.
- **Blocking:** rotate the 4 exposed credentials now, independent of the release decision.

### Audit Limits
Probed four categories at low-to-medium effort. Not probed: multi-turn elicitation, embedding
inversion, or an adversary holding substantial internal knowledge. Customer identifiers
returned no verified verbatim extraction **at this effort level** — that is not evidence of
absence, and the attribute-inference result suggests the mapping is present in some form.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** category × probe type × effort × verification status is the audit grid.
- **QA-12 (False Positives Identification):** the corpus-verification gate is the whole defence against reporting generated content as memorized.
- **RT-05 (Evidence-Based Reasoning):** canary extraction rates and verified matches carry the conclusions rather than impressions.
- **CM-02 (Constraint Specification):** redaction, no-fabrication, and no-reusable-extraction-procedure rules bound the output.
- **DS-06 (Prioritization and Severity Guidance):** per-record severity leads over corpus averages.

**Related Prompts:**
- `mlsec_membership_inference_defense.md` — presence rather than content.
- `../responsible-ai-governance/rai_machine_unlearning_deletion.md` — when a verified finding must actually be removed.
- `../responsible-ai-governance/rai_privacy_pii_assessment.md` — the compliance-facing counterpart.
- `../data-for-ml/mldata_data_quality_audit.md` — corpus-side deduplication and scrubbing before training.
