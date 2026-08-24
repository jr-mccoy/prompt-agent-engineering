---
title: "Unsourced-Claim Disposition — Decide KEEP / SOFTEN / REFRAME / QUOTE / CUT for Claims You Know But Can't Cite"
category: professional-writing/writing
description: "For each factual claim a nonfiction author asserts from experience but has no source for, decide the honest disposition: keep it (a source was found), soften its certainty to match the evidence, reframe it as labeled professional judgment, quote-and-attribute it, or cut it. Prevents tacit expertise from being published as if it were established, cited fact."
techniques:
  - ST-01
  - ST-02
  - QA-04
  - QA-05
  - RT-05
difficulty: intermediate
tags:
  - sourcing
  - claim-disposition
  - certainty-calibration
  - nonfiction
  - attribution
  - tacit-knowledge
updated: "2026-07-06"
related_prompts:
  - domain-professional-writing/writing/writing_original_expression_rewriter.md
  - domain-reasoning-craft/epistemic/epistemic_uncertainty_acknowledgment_audit.md
  - domain-research-academic/research_source_triangulation.md
---

# Unsourced-Claim Disposition

**Objective:** For each factual claim an author asserts but cannot cite, assign one honest disposition — **KEEP**, **SOFTEN**, **REFRAME**, **QUOTE**, or **CUT** — with a reason, so nothing experiential is published as if it were established, sourced fact, and nothing genuinely valuable is thrown away when a citation simply doesn't exist.

**The core move:** A domain expert's knowledge is a mix of (a) verifiable facts they happen not to have cited, (b) their own professional judgment, and (c) things they believe that turn out to be folklore. Publishing all three as flat factual assertions is the failure mode — it's not credible and it's a risk. The fix is not to delete the uncited material; it's to *label it truthfully*. A well-earned professional opinion, clearly marked as the author's judgment, is publishable and honest. The same sentence dressed as established fact is neither.

**When to Use:**
- After claims have been extracted and a source-discovery pass has run, to triage what remains.
- A nonfiction draft (article, book chapter, report, guide) built partly from the author's undocumented experience.
- Any time you must decide "can I say this as fact, and if not, how do I say it honestly?"

**When NOT to use:**
- The claim already has a solid source — it's a KEEP; no disposition needed beyond recording the citation.
- You want to *find* sources — use a source-discovery/triangulation prompt first; this one triages what's left.
- The content is opinion/argument by nature (a review, an op-ed) where everything is understood as the author's view — labeling is lighter there.

**Audience:** Nonfiction authors, editors, ghostwriters, and fact-checkers turning experiential knowledge into publishable prose.

---

## Inputs / Context

1. **The claims** to triage (paste as a list, or wrap the draft in `<draft>...</draft>` and work sentence-by-sentence).
2. **Source-discovery results (if any):** for each claim, what a search found — a supporting source, partial support, contradiction, or nothing. If none was run, treat every claim as "no source found yet."
3. **Claim type (if known):** verifiable-fact / professional-judgment / original-analysis / common-knowledge / experiential-opinion / claim-about-a-named-person. If absent, infer it.
4. **Author's confidence and basis:** how sure the author is and *why* (years of practice, a specific case, a pattern they've seen) — this determines whether REFRAME is honest or overreach.
5. **Stakes:** would a reader act on this claim in a way that could harm them (health, legal, financial, safety)? High stakes raise the bar.

---

## Constraints

### Must
- Assign exactly **one** disposition per claim, with a one-line reason.
- Default to the **most conservative honest option** the evidence supports: if it can't be KEPT as fact, prefer SOFTEN/REFRAME over asserting; prefer CUT over publishing a high-stakes claim with no basis.
- Preserve the author's **genuine expertise** — REFRAME is a first-class, respectable outcome, not a demotion. Well-grounded judgment gets published *as judgment*.
- Make REFRAME wording **explicitly attributive** ("In my experience…", "I've found that…", "In my professional judgment…") so a reader can tell fact from practitioner opinion.
- Match **certainty to basis**: a pattern seen across hundreds of cases warrants stronger language than a hunch from one.
- Raise the bar for **high-stakes** claims (health/legal/financial/safety): these need a real source to KEEP, or they SOFTEN/REFRAME with an explicit "not established" note, or CUT.

### Must Not
- KEEP a claim as fact on the strength of the author's confidence alone — confidence is not a citation.
- REFRAME a claim the author has no real basis for into "in my experience" — that launders a guess into false authority. If there's no basis, CUT.
- CUT genuinely valuable experiential insight just because it can't be cited — REFRAME it instead.
- Silently change a claim's meaning while "softening" — SOFTEN adjusts *certainty*, not *content*.
- Present the author's original analysis as if it were external consensus (or vice versa).

---

## Instructions

1. **Classify the claim.**
   - Is it a *verifiable fact* (in principle citable), a *professional judgment* (the author's earned opinion), *original analysis* (the author's own synthesis), *common knowledge* (needs no cite), or *experiential opinion*? This drives the disposition.

2. **Check what source discovery found.**
   - Solid support → **KEEP** (record the source). Partial/weak support → **SOFTEN** to what the source actually shows. Contradiction → SOFTEN/REFRAME/CUT depending on basis. Nothing found → go to step 3.

3. **For claims with no source, test the basis (CRITICAL).**
   - Ask: *why* does the author believe this, and is that basis real and substantial?
     - **Strong experiential basis** (a pattern seen repeatedly, a defensible professional judgment) → **REFRAME** as labeled judgment, certainty matched to the basis.
     - **It's really an author-original insight** → **REFRAME/KEEP as clearly the author's analysis**, framed as such (not as established fact).
     - **Common knowledge** in the field (uncontroversial, no reader would demand a cite) → **KEEP** unmarked, but sanity-check it isn't actually folklore.
     - **Thin or no basis** (a hunch, hearsay, "everyone says") → **CUT**, or QUOTE a real source if one exists.
     - **Better as someone's exact words** (a definition, a memorable formulation whose value is the phrasing) → **QUOTE** with attribution.

4. **Apply the stakes multiplier.**
   - If a reader could be harmed by acting on the claim, escalate: KEEP needs a real source; otherwise SOFTEN/REFRAME with an explicit "this is my judgment, not established guidance — verify with [appropriate professional]" or CUT.

5. **Write the disposition.**
   - Give the disposition, a ≤12-word reason, and — for SOFTEN/REFRAME/QUOTE — the **rewritten sentence** in honest form.

6. **Flag the residue.**
   - List every REFRAMED and CUT claim so the author sees exactly what could not be stated as fact and why.

---

## False-Positive Prevention (MUST follow)

❌ **DON'T** KEEP a claim as fact because the author is certain — certainty ≠ evidence. High confidence with no source is a REFRAME candidate, not a KEEP.
❌ **DON'T** REFRAME a baseless guess into "in my experience…" — that manufactures authority. No real basis → CUT.
❌ **DON'T** CUT valuable, well-earned insight just because it lacks a citation — REFRAME preserves it honestly.
❌ **DON'T** let "SOFTEN" quietly change what the claim says — soften certainty, never meaning.
❌ **DON'T** treat every field-common statement as needing a cite (over-flagging) — genuine common knowledge can stay, but verify it isn't folklore first.
✅ **DO** default to the most conservative honest label the basis supports.
✅ **DO** make REFRAME wording explicitly first-person/attributive so readers can separate fact from judgment.
✅ **DO** escalate the bar for anything a reader might act on to their harm.
✅ **DO** preserve the author's expertise by publishing judgment *as* judgment.

## Confidence Levels
- **High:** clear source verdict or clear basis (e.g., strong support found → KEEP; no basis at all → CUT).
- **Medium:** basis is real but hard to size (defensible REFRAME, but wording/strength is a judgment call).
- **Low:** genuinely unsure whether the author has a basis, or whether it's common knowledge vs folklore — flag for the author to confirm.

---

## Expected Output

### Output Format

```
## Disposition Table
| # | Claim (short) | Type | Source found? | Disposition | Confidence | Reason |
|---|---------------|------|---------------|-------------|-----------|--------|
| 1 | ...           | verifiable-fact | solid | KEEP | High | source S3 supports directly |
| 2 | ...           | professional-judgment | none | REFRAME | Medium | strong repeated-pattern basis |
| 3 | ...           | experiential-opinion | none | CUT | High | no basis; high-stakes health claim |

## Rewrites (for SOFTEN / REFRAME / QUOTE)
- **Claim 2 (REFRAME):**
  - Was: "X always causes Y."
  - Now: "In my experience across [basis], X very often leads to Y, though I'm not aware of a study establishing it."

## Residue Report
- **Reframed as judgment (not fact):** [list]
- **Cut (could not be stated honestly):** [list, with why]
- **High-stakes items needing professional verification:** [list or "none"]
- **Low-confidence — author, please confirm basis:** [list or "none"]
```

---

## Example Output

_Input: a career-coach's draft claim set, source discovery already run._

## Disposition Table
| # | Claim (short) | Type | Source found? | Disposition | Confidence | Reason |
|---|---------------|------|---------------|-------------|-----------|--------|
| 1 | "The average job search takes about 5 months" | verifiable-fact | solid | KEEP | High | BLS data supports (S1) |
| 2 | "Most roles are filled before they're posted" | verifiable-fact | partial/contested | SOFTEN | Medium | sources vary widely; state as "a large share, by some estimates" |
| 3 | "Candidates who send a same-day thank-you note get more offers" | experiential-opinion | none | REFRAME | Medium | coach has seen the pattern across many clients; no study found |
| 4 | "Recruiters spend exactly 6 seconds on a résumé" | verifiable-fact | contradicted | SOFTEN | High | the "6 seconds" figure traces to one small eye-tracking vendor study — attribute, don't state as law |
| 5 | "Networking is the single most effective job-search tactic for everyone" | professional-judgment | none | REFRAME | Medium | defensible judgment; universal "for everyone" overreaches — narrow it |
| 6 | "You should never take a counteroffer" | experiential-opinion | none | CUT | High | high-stakes career advice, no basis, contested even as opinion |

## Rewrites
- **Claim 2 (SOFTEN):**
  - Was: "Most roles are filled before they're posted."
  - Now: "A meaningful share of roles are filled through referrals and internal moves before a public posting, though estimates vary."
- **Claim 3 (REFRAME):**
  - Was: "Candidates who send a same-day thank-you note get more offers."
  - Now: "In my coaching practice, candidates who send a prompt, specific thank-you note tend to fare better — I haven't found a controlled study on it, so I offer it as a pattern I've observed, not a rule."
- **Claim 4 (SOFTEN/attribute):**
  - Was: "Recruiters spend exactly 6 seconds on a résumé."
  - Now: "One widely-cited eye-tracking study put average initial résumé review at roughly six seconds; treat it as indicative, not precise."
- **Claim 5 (REFRAME + narrow):**
  - Was: "Networking is the single most effective job-search tactic for everyone."
  - Now: "In my experience, networking is the highest-leverage tactic for most mid-career candidates — less so for some early-career or credential-gated roles."

## Residue Report
- **Reframed as judgment (not fact):** 3, 5
- **Cut:** 6 ("never take a counteroffer" — no basis, high-stakes, contested).
- **High-stakes items needing professional verification:** none remaining after CUT.
- **Low-confidence — author, please confirm basis:** none.

---

## Customization Guide
- **Lower the bar** for low-stakes lifestyle/opinion content where readers expect the author's take (lighter REFRAME labeling).
- **Raise the bar** hard for regulated domains (health, legal, financial) — wire in the relevant source-standards profile so KEEP requires a tier-1/2 source.
- **Batch by type** for long manuscripts: triage all verifiable-facts first, then all judgment claims.

## Techniques Used
- **ST-01 (Clear Objective):** one disposition per claim with a defined decision set.
- **ST-02 (Structured Sequential Instructions):** classify → check source → test basis → apply stakes → write disposition.
- **QA-04 (Uncertainty Acknowledgment):** SOFTEN/REFRAME calibrate stated certainty to the actual basis.
- **QA-05 (Citation Requirements):** KEEP-as-fact requires a real source; distinguishes fact from interpretation.
- **RT-05 (Evidence-Based Reasoning):** disposition follows from the source verdict and the basis, not the author's confidence.

## Related Prompts
- `domain-professional-writing/writing/writing_original_expression_rewriter.md` — for QUOTE→paraphrase handling.
- `domain-reasoning-craft/epistemic/epistemic_uncertainty_acknowledgment_audit.md` — deeper certainty calibration.
- `domain-research-academic/research_source_triangulation.md` — run before this to produce the source verdicts.
