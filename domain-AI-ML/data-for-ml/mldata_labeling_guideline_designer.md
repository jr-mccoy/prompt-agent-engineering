---
title: "ML Labeling Guideline Designer"
category: AI-ML/data-for-ml
description: "Write annotation guidelines that maximize inter-annotator agreement — precise label definitions, decision rules, worked edge cases, and positive/negative examples — before annotation begins."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DT-04
  - QA-16
difficulty: intermediate
tags:
  - data-labeling
  - annotation-guidelines
  - inter-annotator-agreement
  - taxonomy
  - edge-cases
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_annotation_quality_review.md
  - domain-AI-ML/data-for-ml/mldata_dataset_curation_plan.md
  - domain-AI-ML/data-for-ml/mldata_datasheet_authoring.md
---

# ML Labeling Guideline Designer

**Objective:** Produce an annotation guideline document that lets independent annotators apply the same labels to the same data — by fixing precise label definitions, an exhaustive-and-mutually-exclusive (or explicitly multi-label) taxonomy, tie-breaking decision rules, worked edge cases, and labeled positive/negative examples — so inter-annotator agreement is high *by design* rather than fixed after the fact.

**When to Use:**
- Standing up a new labeling effort (in-house, crowd, or vendor) and you need the rulebook before annotation begins.
- Inter-annotator agreement is low and you need to rewrite ambiguous instructions.
- Migrating an informal "we just know it when we see it" label into a documented, auditable standard.

**When NOT to Use:**
- Labels already exist and you need to assess their quality/agreement (use `mldata_annotation_quality_review.md`).
- You are planning what data to collect, not how to label it (use `mldata_dataset_curation_plan.md`).

## Inputs / Context

Provide what you can; the guideline degrades gracefully if some are missing:
- **Task & label schema** — the classes/spans/relations to label, and whether single-label, multi-label, or hierarchical.
- **Modeling intent** — how the labels will be used downstream (what the model must learn), which sets the granularity.
- **Annotator profile** — who labels (domain experts, crowd, internal ops), their expertise and constraints.
- **Sample items** — representative examples, especially confusing or borderline ones.
- **Existing conventions** — any prior label definitions, style guides, or known disagreements.
- **Tooling constraints** — what the annotation tool can and cannot capture.

## Constraints

**Must:**
- Define each label so that the boundary between it and its nearest neighbor is decidable by rule, not vibe.
- Provide a decision procedure for ambiguous items (an ordered tie-breaker, a "when in doubt" rule, or an explicit "uncertain/skip" option).
- Include both positive and negative (near-miss) examples for each label.

**Must Not:**
- Invent domain facts, label semantics, or a taxonomy the user did not intend — surface granularity choices as decisions for the user.
- Write definitions that overlap (two labels both apply with no tie-breaker) or leave gaps (an item fits no label with no "other").
- Assume annotators share the author's context; spell out abbreviations, scope, and exclusions.

**Instructions:**

1. **Fix the labeling unit and schema type.** State exactly what is labeled (document, span, image region, pair) and whether each unit gets one label, many, or a hierarchy. This determines everything else.

2. **Define each label operationally.** For every label give: a one-line definition, inclusion criteria, explicit exclusions, and the nearest confusable label with the rule that separates them.

3. **Make the taxonomy MECE or explicitly not.** Verify labels are mutually exclusive and collectively exhaustive; if not, document overlaps and the multi-label rule, and add an "Other/None" with criteria so nothing is forced.

4. **Write decision rules for ambiguity.** Provide an ordered procedure: check precedence, apply the "when in doubt" default, or route to the uncertain/escalate path. Forbid silent guessing.

5. **Build the edge-case library.** Collect borderline items and resolve each with the rule that decides it, so future annotators inherit the precedent instead of re-deciding.

6. **Add worked examples per label.** For each label, show 1–2 clear positives and 1–2 near-miss negatives, each with a short rationale tied to the definition.

7. **Specify metadata and quality controls.** Define required fields (confidence, comments), how to flag bad/ambiguous items, and the gold/honeypot and adjudication plan that will measure agreement.

8. **Pilot and revise.** Recommend a small dual-labeled pilot, predict where disagreement will cluster, and specify what the pilot must show before scaling.

**Output Format:**

A markdown guideline document:
- **Task & Labeling Unit** — what is labeled and schema type.
- **Label Definitions** — table: Label | Definition | Include | Exclude | Confusable-with → tie-breaker.
- **Decision Rules** — ordered ambiguity procedure + uncertain/escalate path.
- **Edge-Case Library** — borderline item → resolution + rule.
- **Worked Examples** — per label: positives and near-miss negatives with rationale.
- **Metadata & Quality Controls** — required fields, flags, gold/adjudication plan.
- **Pilot Plan** — dual-labeling step + expected disagreement hotspots.

## Verification

- [ ] Every label has explicit include AND exclude criteria and a named nearest-confusable with a tie-breaker.
- [ ] The taxonomy is MECE, or its overlaps/gaps are documented with an Other/None and multi-label rule.
- [ ] An ambiguity procedure exists and "guess silently" is explicitly disallowed.
- [ ] Each label has at least one positive and one near-miss negative example.
- [ ] A gold/adjudication and pilot plan is specified to measure agreement before scaling.

## False-Positive Prevention

❌ **DON'T:**
- Write definitions that read clearly to the author but rely on unstated domain context annotators lack.
- Leave two labels that can both legitimately apply with no precedence rule — this guarantees disagreement.
- Force every item into a label by omitting an "Other/None," producing noisy labels on out-of-scope items.
- Provide only positive examples; without near-misses, annotators over-apply broad labels.

✅ **DO:**
- Pin each label boundary against its nearest neighbor with an explicit tie-breaker.
- Give an ordered "when in doubt" procedure and an uncertain/skip option so ambiguity is captured, not hidden.
- Include near-miss negatives so the *edge* of each label is taught, not just the center.
- Pilot on dual-labeled data and rewrite the definitions that disagreement exposes before scaling up.

## Example Output

```markdown
## Annotation Guidelines: Support Ticket Intent (v1)

### Task & Labeling Unit
- Unit: one inbound support message. Schema: single-label (pick exactly one intent).

### Label Definitions
| Label | Definition | Include | Exclude | Confusable-with → tie-breaker |
|---|---|---|---|---|
| Billing | Question/dispute about charges | refunds, invoices, plan price | "how do I upgrade" (→ Account) | Account: if money is disputed → Billing |
| Account | Access/settings/plan changes | password, upgrade, seats | charge disputes (→ Billing) | Billing: non-monetary change → Account |
| Bug | Product not working as designed | errors, crashes, wrong output | "how do I X" (→ How-to) | How-to: if user expected it to work → Bug |
| How-to | Usage/guidance request | "where is", "how do I" | broken behavior (→ Bug) | Bug: feature works, user unsure → How-to |
| Other/None | Fits no intent above | spam, greetings only | anything matching above | — |

### Decision Rules
1. If multiple intents appear, label the *primary ask* (the action the user wants resolved).
2. If money is disputed, Billing wins over Account.
3. If genuinely undecidable after rules 1–2, mark `uncertain=true` and add a comment. Never guess silently.

### Edge-Case Library
- "I was charged but the upgrade didn't apply" → Billing (rule 2: money disputed).
- "App crashes when I open settings" → Bug, not Account (broken behavior > settings topic).

### Worked Examples
- Billing ✅ "Why was I charged twice in March?" — disputes a charge.
- Billing ❌ (near-miss) "How do I add a payment method?" → How-to (no dispute).

### Metadata & Quality Controls
- Required: intent, uncertain (bool), comment (if uncertain). 5% gold items per batch; adjudicate items where κ-flagged.

### Pilot Plan
- 200 items dual-labeled; expect disagreement on Bug↔How-to. Require κ ≥ 0.70 before scaling; else revise that boundary.
```

**Techniques Used:**
- **ST-01 (Clear Objective Statement):** the guideline opens by fixing the labeling unit and schema type.
- **ST-02 (Structured Sequential Instructions):** definitions → MECE check → decision rules → edge cases → pilot.
- **CM-02 (Constraint Specification):** label boundaries and the no-silent-guess rule are governing constraints.
- **DT-04 (Decision Criteria Specification):** explicit tie-breakers and ordered ambiguity procedure.
- **QA-16 (Edge Case Handling):** the edge-case library and near-miss examples teach the label boundaries.

**Related Prompts:**
- `mldata_annotation_quality_review.md` — measure whether the guideline actually produced agreement.
- `mldata_dataset_curation_plan.md` — plan what data the guideline will be applied to.
- `mldata_datasheet_authoring.md` — record the labeling process in the dataset's documentation.
