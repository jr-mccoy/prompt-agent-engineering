---
title: "Manuscript Fact-Check Reconciler — Reconcile a Finished Draft Against Its Source Set"
category: research-academic
description: "Take a finished nonfiction draft plus the source set it was built from and reconcile them claim-by-claim: confirm every factual statement is actually supported by a cited source, catch orphan claims (asserted, uncited), overreach (claim stronger than its source), misattribution, and citations that don't say what the text implies. Produces a reconciliation report and a fix list."
techniques:
  - ST-01
  - ST-02
  - QA-01
  - QA-05
  - RT-05
difficulty: advanced
tags:
  - fact-checking
  - citation-audit
  - reconciliation
  - nonfiction
  - verification
updated: "2026-07-06"
related_prompts:
  - domain-research-academic/research_source_triangulation.md
  - domain-reasoning-craft/epistemic/epistemic_uncertainty_acknowledgment_audit.md
  - domain-professional-writing/writing/writing_unsourced_claim_disposition.md
---

# Manuscript Fact-Check Reconciler

**Objective:** Given a finished draft and the set of sources it was built from, reconcile the two so that every factual claim in the manuscript is either (a) genuinely supported by a source that says what the text claims, (b) flagged as an orphan (asserted with no source), (c) flagged as overreach (stated more strongly than the source supports), or (d) flagged as misattributed (the cited source doesn't actually support it) — and produce a concrete fix for each problem.

**When to Use:**
- A nonfiction draft is near-final and you need to confirm it and its citations actually agree before publishing.
- The final gate on a claims→sources pipeline: catch anything that drifted during drafting.
- Auditing someone else's cited draft (a contributor's chapter, a report you're signing off on).

**When NOT to use:**
- You haven't gathered sources yet — run source discovery/triangulation first; this reconciles an existing draft against existing sources.
- The piece is opinion/argument where claims aren't meant to be externally sourced.
- You need a legal-risk read (defamation, copyright) — use the risk-screen prompts; this checks factual support and citation integrity.

**Audience:** Fact-checkers, editors, nonfiction authors, and researchers doing final citation reconciliation.

---

## Inputs / Context

1. **The manuscript** (wrap in `<manuscript>...</manuscript>`), ideally with inline citation tokens or markers.
2. **The source set** (wrap in `<sources>...</sources>`): the list of sources with an id each, and — critically — enough of each source's actual content (quote, abstract, data point) to check support. A bare URL list is insufficient to verify support; note where you can only check citation *presence*, not *substance*.
3. **Citation mapping (if available):** which source each claim cites.
4. **Certainty context:** any claims the author intends as their own judgment (should be labeled, not treated as needing a source).

If a source's content isn't provided (only a title/URL), say so and mark those claims `SOURCE-CONTENT-NOT-PROVIDED` rather than assuming support.

---

## Constraints

### Must
- Check every **factual claim** in the manuscript, not a sample.
- For each claim, produce a verdict: **SUPPORTED / PARTIAL / OVERREACH / MISATTRIBUTED / ORPHAN / SOURCE-CONTENT-NOT-PROVIDED / AUTHOR-JUDGMENT (labeled)**.
- Verify **substance, not just presence**: a citation next to a sentence is not support unless the source actually says it. Where you can only confirm a token exists (no source content given), say so explicitly.
- Detect **overreach**: source says "may / in some cases / one study"; manuscript says "does / always / studies show." Flag and propose calibrated wording.
- Detect **misattribution**: the cited source is real but doesn't support the specific claim.
- Propose a **concrete fix** for every non-SUPPORTED claim (add source / soften / reframe / attribute / cut).

### Must Not
- Assume a citation supports a claim without checking the source's actual content.
- Invent, "recall," or assert facts about what a source says beyond what's provided — if content isn't given, mark it unverifiable here.
- Treat the author's labeled judgment as an orphan factual claim (or vice versa — an unlabeled factual assertion is an orphan even if the author "knows" it).
- Pass a claim as SUPPORTED on partial evidence — that's PARTIAL, with the gap named.

---

## Instructions

1. **Enumerate factual claims.**
   - Walk the manuscript and list every statement presented as fact (not clearly-labeled opinion). Assign each a short id.

2. **Bind each claim to its cited source(s).**
   - Use the citation mapping/inline tokens. Claims with no citation → provisional ORPHAN (confirm they're factual, not labeled judgment).

3. **Check substance against the source (CRITICAL).**
   - For each bound claim, compare the manuscript's statement to what the source actually says (from provided content):
     - Says the same thing, same strength → **SUPPORTED**.
     - Supports part / a weaker version → **PARTIAL** (name the gap).
     - Source weaker/narrower than the claim → **OVERREACH**.
     - Source doesn't support this claim → **MISATTRIBUTED**.
     - No source content provided → **SOURCE-CONTENT-NOT-PROVIDED** (can't verify substance).

4. **Resolve orphans.**
   - Is the orphan actually the author's judgment? If unlabeled, it still reads as fact → needs a source, a label, or a cut. Route to the disposition prompt.

5. **Propose fixes.**
   - PARTIAL/OVERREACH → calibrated rewrite matching the source. MISATTRIBUTED → find the right source or reclassify. ORPHAN → add source / label as judgment / cut.

6. **Summarize risk.**
   - Count claims by verdict; list the must-fix items (MISATTRIBUTED, OVERREACH on high-stakes claims, ORPHAN factual claims) before publish.

---

## False-Positive Prevention (MUST follow)

❌ **DON'T** mark a claim SUPPORTED because a citation is *present* — presence ≠ support. Check what the source says.
❌ **DON'T** assert what a source says when its content wasn't provided — mark it SOURCE-CONTENT-NOT-PROVIDED.
❌ **DON'T** flag clearly-labeled author judgment as an orphan factual claim.
❌ **DON'T** miss "quiet overreach" — a source's "associated with" becoming the manuscript's "causes."
❌ **DON'T** pass PARTIAL as SUPPORTED to reduce the fix list.
✅ **DO** compare claim strength to source strength word-for-word on certainty verbs.
✅ **DO** give every non-SUPPORTED claim a concrete, specific fix.
✅ **DO** separate "can't verify (no content)" from "verified unsupported."

## Confidence Levels
- **High:** source content provided and clearly matches or clearly doesn't.
- **Medium:** support is arguable/partial, or hinges on interpretation of the source.
- **Low:** source content thin or not provided — flag for human check with the full source in hand.

---

## Expected Output

### Output Format

```
## Reconciliation Table
| Claim id | Claim (short) | Cited source | Verdict | Confidence | Note |
|----------|---------------|--------------|---------|-----------|------|
| C1 | ... | S3 | SUPPORTED | High | source states directly |
| C2 | ... | S3 | OVERREACH | High | source: "may"; text: "does" |
| C3 | ... | — | ORPHAN | High | factual, uncited |
| C4 | ... | S7 | MISATTRIBUTED | Medium | S7 is about a different population |

## Fix List (must-fix first)
1. [C4 MISATTRIBUTED] → ...
2. [C2 OVERREACH] → soften to "..."
3. [C3 ORPHAN] → add source, label as judgment, or cut.

## Summary
- SUPPORTED: n | PARTIAL: n | OVERREACH: n | MISATTRIBUTED: n | ORPHAN: n | UNVERIFIABLE (no content): n
- Publish blockers: [list]
```

---

## Example Output

## Reconciliation Table
| Claim id | Claim (short) | Cited source | Verdict | Confidence | Note |
|----------|---------------|--------------|---------|-----------|------|
| C1 | "Remote work grew sharply after 2020" | S1 (BLS) | SUPPORTED | High | data series shows the rise |
| C2 | "Remote work makes teams more productive" | S2 | OVERREACH | High | S2 finds mixed/context-dependent effects, not a general gain |
| C3 | "Four-day weeks reduce burnout" | S4 | PARTIAL | Medium | S4 is one 6-month pilot; supports a narrower claim |
| C4 | "Async communication eliminates meeting overload" | — | ORPHAN | High | asserted as fact, no citation |
| C5 | "In my experience, small teams adopt async faster" | (labeled) | AUTHOR-JUDGMENT | High | properly labeled; not an orphan |

## Fix List (must-fix first)
1. **[C2 OVERREACH]** → "Evidence on remote work's productivity effect is mixed and depends on role and management (S2)."
2. **[C4 ORPHAN]** → add a source, or reframe: "In my experience, async practices reduce meeting load" — and label it, or cut.
3. **[C3 PARTIAL]** → narrow to "In one six-month pilot, a four-day week was associated with lower reported burnout (S4)."

## Summary
- SUPPORTED: 1 | PARTIAL: 1 | OVERREACH: 1 | MISATTRIBUTED: 0 | ORPHAN: 1 | UNVERIFIABLE (no content): 0
- Publish blockers: C2 (overreach on a headline claim), C4 (orphan factual claim).

---

## Customization Guide
- **Strict mode:** treat SOURCE-CONTENT-NOT-PROVIDED as a blocker (nothing ships unverified).
- **High-stakes domains:** auto-escalate any OVERREACH/PARTIAL on health/legal/financial claims to publish-blocker.
- **Bulk manuscripts:** reconcile per section and roll up the summary.

## Techniques Used
- **ST-01 (Clear Objective):** one verdict + fix per factual claim.
- **ST-02 (Structured Sequential Instructions):** enumerate → bind → check substance → resolve orphans → fix.
- **QA-01 (Self-Verification / Chain-of-Verification):** the reconciliation *is* a structured verification pass over the draft.
- **QA-05 (Citation Requirements):** substance-level citation checking; distinguishes fact from labeled judgment.
- **RT-05 (Evidence-Based Reasoning):** verdicts cite the specific source content, not impression.

## Related Prompts
- `domain-research-academic/research_source_triangulation.md` — produce/refresh source verdicts per claim.
- `domain-reasoning-craft/epistemic/epistemic_uncertainty_acknowledgment_audit.md` — deeper overreach/certainty calibration.
- `domain-professional-writing/writing/writing_unsourced_claim_disposition.md` — route ORPHANs to a disposition.
