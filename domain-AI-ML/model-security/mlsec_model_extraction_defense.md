---
title: "Model Extraction Defense"
category: AI-ML/model-security
description: "Defend a served model against functional stealing by pricing what extraction is worth to an attacker, reducing what each response reveals, budgeting queries against legitimate usage, and accepting that the goal is making extraction uneconomic rather than impossible."
techniques:
  - RT-02
  - DS-02
  - CM-02
  - QA-12
  - AG-44
difficulty: advanced
tags:
  - model-extraction
  - model-stealing
  - query-budget
  - output-granularity
  - api-security
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/model-security/mlsec_secure_inference_endpoint_design.md
  - domain-AI-ML/model-security/mlsec_model_watermarking_provenance.md
  - domain-AI-ML/model-security/mlsec_ml_threat_model.md
  - domain-AI-ML/mlops-infrastructure/mlops_model_serving_architecture.md
---

# Model Extraction Defense

**Objective:** Make functional extraction of a served model uneconomic — by first pricing what a stolen copy is worth against what it costs to obtain, then reducing what each response reveals, budgeting queries against real usage patterns, and stating plainly that every control here raises attacker cost rather than preventing theft.

**When to Use:**
- A model is exposed through an API, a partner integration, or a product surface that returns per-input predictions.
- The model represents a real investment — proprietary training data, expensive labelling, or a capability competitors lack.
- Before loosening rate limits or enriching a response (adding scores, top-k, or explanations), so the cost of that change is visible.

**When NOT to Use:**
- The model has no commercial or strategic value to a copier — the controls cost more than the asset. Say so and stop.
- The concern is what the model reveals about its **training records** rather than its function — use `mlsec_membership_inference_defense.md` or `mlsec_model_inversion_leakage_audit.md`.
- The concern is availability or abuse cost rather than theft — use `mlsec_secure_inference_endpoint_design.md`.

## Inputs / Context

- **Response granularity** — exactly what a caller receives: hard label, top-1 with score, top-k, full probability vector, logits, embeddings, or explanations.
- **Query interface** — authentication, per-caller rate limits, batch endpoints, and whether callers can submit arbitrary inputs or only inputs from a constrained space.
- **Legitimate usage profile** — realistic query volume, distribution, and shape for an honest caller, which is the baseline any budget must not break.
- **Model value** — what it cost to build and what a functional equivalent would be worth to a competitor.
- **Input space** — whether an attacker can generate valid inputs cheaply (images, text) or must obtain scarce real ones (rare medical scans, proprietary telemetry).
- **Contractual and legal position** — terms of service, partner agreements, and whether attribution would ever be acted on.

## Constraints

**Must:**
- Price extraction before designing controls: estimate the query volume a useful copy would need against the response granularity and input-space cost, and compare it to the model's value. Controls are justified only where the ratio is unfavourable.
- State for every control the legitimate-usage cost it imposes, since the binding constraint is nearly always honest callers rather than technical feasibility.
- Treat response granularity as the primary lever — richer outputs reduce the query volume an attacker needs, often by a large factor.
- Declare explicitly that these controls raise cost and do not prevent extraction, and state the resulting attacker cost.
- Include detection and attribution alongside prevention, since a control that cannot be observed cannot be tuned.

**Must Not:**
- Assert query-count figures, extraction-fidelity results, or published attack efficiency numbers from memory; mark any needed figure `[verify against a primary source]`.
- Recommend removing output detail without checking which legitimate consumers depend on it — a downstream calibration or ranking step may need the scores.
- Treat authentication as extraction defense; an attacker with a paid account is authenticated and still extracts.
- Recommend watermarking as prevention — it supports attribution after the fact and belongs in a different column.
- Present rate limiting as sufficient when an attacker can distribute across accounts, without addressing the account-creation cost.

**Instructions:**

1. **Price the theft.** Estimate what a functional copy is worth to a competitor and what it would cost to obtain at the current granularity and rate limit. If obtaining it is cheaper than building it, extraction is rational and the current posture is the finding.

2. **Audit response granularity.** List every field a caller receives and, for each, what it reveals about the decision boundary. Order them by information content: explanations and logits reveal most, full probability vectors next, top-k, top-1 with score, hard label least. This ordering is the menu of available reductions.

3. **Establish the legitimate-usage baseline.** Profile real callers — volume, burstiness, input diversity, and which response fields they actually consume. Every proposed control is measured against breaking this.

4. **Reduce granularity where it is affordable.** For each field, decide: keep, coarsen (round scores, reduce precision), truncate (top-1 instead of top-k), or remove. Name the legitimate consumer affected by each reduction and what they lose.

5. **Budget queries against usage, not against the attack.** Set per-caller limits from the legitimate profile plus headroom. Then address the distribution problem directly: what does it cost an attacker to obtain N accounts, and does account creation carry enough friction to matter? If accounts are free, per-account limits are a speed bump.

6. **Consider input-space friction.** Where valid inputs are scarce or costly to obtain, that scarcity is already a defense — quantify it. Where inputs are trivially generated, it offers nothing and should not be counted.

7. **Design detection.** Extraction traffic differs from legitimate traffic in profile: input diversity out of proportion to a real workload, systematic coverage of the input space, near-boundary querying, or volume without corresponding downstream activity. Specify the signals, their baselines, and the false-positive tolerance — a legitimate batch-integration customer can look exactly like an attacker.

8. **Plan attribution.** If extraction is suspected, what evidence exists — query logs with sufficient retention, watermarking, or canary inputs whose responses would appear in a stolen copy. Attribution changes what recourse is available; note whether the organization would actually act on it.

9. **State the residual.** Say what an attacker with a paid account, patience, and a modest budget can still obtain, and what that means commercially.

**Output Format:**

A markdown defense plan:
- **Extraction Economics** — value of a copy vs cost to obtain at current posture; the resulting verdict.
- **Response Granularity Audit** — table: Field | What it reveals | Legitimate consumer | Reduction option | Cost of reducing.
- **Legitimate Usage Baseline** — volume, burstiness, diversity, fields consumed.
- **Control Plan** — table: Control | Attacker cost added | Legitimate cost imposed | Prevents or raises cost.
- **Account-Distribution Analysis** — cost of N accounts, and whether per-caller limits survive it.
- **Detection Signals** — signal, baseline, false-positive tolerance.
- **Attribution Options** — evidence available and whether it would be acted on.
- **Residual** — what remains obtainable, and the commercial meaning.

## Verification

- [ ] Extraction is priced before any control is proposed.
- [ ] Every response field is audited for what it reveals and who consumes it.
- [ ] Each control states both attacker cost added and legitimate cost imposed.
- [ ] The account-distribution problem is addressed, not assumed away by per-caller limits.
- [ ] Input-space scarcity is quantified where claimed as a defense.
- [ ] Detection signals have baselines and a stated false-positive tolerance.
- [ ] Watermarking, if present, appears under attribution rather than prevention.
- [ ] The plan states plainly that it raises cost rather than preventing extraction.
- [ ] No query counts or extraction-fidelity figures are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Build extraction defenses for a model nobody would want to copy — price the asset first, or the controls are pure legitimate-user tax.
- Strip scores from responses without checking which downstream consumers calibrate, threshold, or rank on them; you can break a paying integration to defend against a hypothetical.
- Treat per-account rate limits as the control when accounts are free to create — the real limit is the cost of an account.
- Count "attacker must send many queries" as a defense without checking whether those queries are cheap and whether inputs are trivially generated.
- Flag a high-volume, high-diversity caller as an extractor when a legitimate batch-integration customer produces exactly that profile.
- Describe the model as protected; every control here is a cost multiplier.

✅ **DO:**
- Compare the cost of extracting against the cost of building from scratch, and let that ratio decide the effort.
- Order response fields by information content and reduce from the top, naming each affected consumer.
- Set query budgets from the legitimate profile, then separately price the account-distribution bypass.
- Quantify input-space scarcity where it genuinely raises cost, and discount it where inputs are synthetic.
- Give every detection signal a baseline and a false-positive tolerance before it gates anything.
- State the residual in commercial terms — what a determined competitor still walks away with.

## Example Output

```markdown
## Extraction Defense: Product-Categorization API (partner-facing, paid tier)
Classifies retail product listings into a 1,400-node taxonomy. The taxonomy and its labelled
training set are the asset; the architecture is unremarkable.

### Extraction Economics
Building an equivalent requires the taxonomy plus ~1.4M labelled listings — the labelling
alone was the dominant cost. Current responses return the **full 1,400-way probability
vector**, which reveals far more per query than a label would. At the current 10k queries/day
per key, a competitor with a handful of paid keys plausibly reaches a useful copy well inside
a year for the price of the subscriptions. `[verify: run the query-count estimate against your
own model rather than from a published figure.]`
**Verdict:** extraction is currently cheaper than building. This is the finding.

### Response Granularity Audit
| Field | Reveals | Legitimate consumer | Reduction option | Cost of reducing |
|---|---|---|---|---|
| Full 1,400-way probability vector | near-complete boundary per query | 2 of 31 partners (re-rank top-20) | truncate to top-20 | those 2 partners re-integrate |
| Confidence score (float64) | boundary distance | most partners threshold on it | round to 2 dp | none observed |
| Predicted node ID | the answer | all | keep | n/a |
| Sibling-node explanation | local boundary shape | 0 partners (added, never adopted) | **remove** | none |

### Legitimate Usage Baseline
Median partner: 900 queries/day, bursty at catalogue-sync times, input diversity tracking
their own catalogue (narrow). Largest partner: 8.2k/day. **No** legitimate partner queries
uniformly across the taxonomy — every real caller's traffic clusters in their own categories.

### Control Plan
| Control | Attacker cost added | Legitimate cost imposed | Prevents / raises cost |
|---|---|---|---|
| Remove sibling-node explanation | moderate — removes cheapest boundary probe | **none** — unused | raises cost |
| Truncate vector to top-20 | **large** — most of the per-query information | 2 partners re-integrate | raises cost |
| Round score to 2 dp | small | none | raises cost |
| Per-key limit 12k/day | small alone | none (above largest partner) | raises cost |
| Paid key required, KYC on signup | **large** — this is the real limiter | signup friction | raises cost |

### Account-Distribution Analysis
Per-key limits are only as strong as the cost of a key. Keys are currently self-service at a
low monthly price, so 20 keys is an affordable line item and per-key limits contribute little.
Adding business verification at signup is the single highest-leverage control here — it moves
the bypass from a budget item to an operational effort. Without it, the other limits are speed
bumps.

### Detection Signals
| Signal | Baseline | FP tolerance |
|---|---|---|
| Taxonomy coverage entropy per key | real partners cluster; near-uniform is anomalous | low — no legitimate caller is uniform |
| Query volume without catalogue-sync correlation | partners burst on sync | **high** — a new partner mid-onboarding looks like this |
| Near-boundary query concentration | legitimate inputs are not boundary-seeking | medium |
| Input novelty vs partner's known catalogue | partners query their own products | medium — catalogue expansion is legitimate |

Coverage entropy is the strongest signal precisely because no honest integration needs uniform
taxonomy coverage.

### Attribution Options
Query logs retained 90 days with per-key input hashes. Canary listings — synthetic products
with a deliberate, stable classification — would appear in any copy trained on our responses.
Commercially, partner agreements prohibit derivative model training, and legal has confirmed
they would act on clear evidence, which makes canaries worth the small cost.

### Residual
A competitor willing to pass business verification, pay for several keys, and query patiently
within limits over ~18 months can still obtain a serviceable copy. The controls change the
economics from "a cheap subscription" to "a funded, sustained, attributable project" — and the
canaries mean the outcome is contestable rather than silent. That is the intended end state;
it is not prevention.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** response granularity × query budget × input-space cost is the analysis grid.
- **DS-02 (Metric Specification):** extraction cost and legitimate-usage baselines are defined as measurable quantities rather than intuitions.
- **CM-02 (Constraint Specification):** the price-first rule and the raises-cost-not-prevents declaration bound what may be claimed.
- **QA-12 (False Positives Identification):** separates extraction traffic from the legitimate batch integration that resembles it.
- **AG-44 (Impossible-vs-Tedious Control Test):** every control declares the cost it adds rather than implying prevention.

**Related Prompts:**
- `mlsec_secure_inference_endpoint_design.md` — implements the rate limiting, response shaping, and logging this plan specifies.
- `mlsec_model_watermarking_provenance.md` — the attribution side, including canary design.
- `mlsec_ml_threat_model.md` — decides whether extraction is worth defending against at all.
- `../mlops-infrastructure/mlops_model_serving_architecture.md` — where these controls physically live.
