---
title: "Influence Assessment Write-Up — Publishing Findings With Hedges That Survive"
category: psy-ops/influence-operations
description: "Turn a completed influence assessment into a publishable write-up whose confidence levels survive editing, headlines, social summaries, and retelling. Addresses confidence laundering — where 'low-confidence indicators consistent with' becomes 'linked to' by the third retelling — by building the hedge into the structure of each claim rather than appending it, pre-writing the accurate headline, and testing every sentence against extraction out of context."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - QA-04
  - QA-01
difficulty: advanced
tags:
  - psy-ops
  - reporting
  - confidence-language
  - publication
  - influence-operations
updated: "2026-09-24"
reasoning:
  styles: [evaluative, evidential, adversarial]
  stakes: high
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: team
  output_format: publication_draft_with_extraction_audit
  user_role: [analyst, researcher, journalist, trust_and_safety]
  mode: [document, audit, decide]
related_prompts:
  - domain-psy-ops/influence-operations/psyops_attribution_confidence_assessment.md
  - domain-psy-ops/influence-operations/psyops_influence_operation_analysis.md
  - domain-reasoning-craft/epistemic/epistemic_evidence_quality_score.md
---

# Influence Assessment Write-Up

**Objective:** Turn a completed influence assessment into a publication — a report, article, platform disclosure, or briefing — whose confidence levels **survive what happens to it after release**. The analysis may be careful; the write-up is where that care is usually lost. A finding stated as "low-confidence indicators consistent with coordination, possibly involving actors aligned with X" is edited to "suspected X-linked network," headlined as "X network targets Y," summarized on social media as "X is behind Y," and cited a month later as established fact. Each step is small. Together they are **confidence laundering**, and the analyst who wrote the original is often blamed for a claim they never made.

The craft this prompt teaches is structural. Hedges appended at the end of a paragraph are the first thing cut. Hedges **built into the subject and verb of each claim** — "accounts sharing these three behaviors," not "the network"; "we assess with low confidence," not "suggests" — survive because removing them breaks the sentence. The prompt also pre-writes the **accurate headline and the accurate one-line summary**, since someone will write both, and the analyst's version is the only one that will be correct.

This prompt does not re-run the analysis. It assumes an assessment exists — from `psyops_influence_operation_analysis.md`, with attribution from `psyops_attribution_confidence_assessment.md` — and its first job is to refuse to publish anything stronger than that assessment supports.

**When to use:**
- You have completed an influence assessment and are preparing it for publication or external briefing.
- An editor, communications team, or executive wants a stronger headline than the findings support.
- A previous report of yours was retold as a stronger claim than you made, and you want to prevent it next time.
- You are reviewing someone else's draft for confidence drift before release.

**When NOT to use:**
- The analysis itself is not finished — complete `psyops_influence_operation_analysis.md` first.
- The question is whether attribution is supportable at all — use `psyops_attribution_confidence_assessment.md`.
- You need general evidence grading rather than publication craft — use `domain-reasoning-craft/epistemic/epistemic_evidence_quality_score.md`.
- You are writing a public correction or response rather than publishing research — see `../counter-messaging/`.

**Audience:** Analysts, researchers, journalists, and trust-and-safety teams publishing influence findings.

---

## Inputs / Context

1. **The assessment.** The findings, each with its confidence band and basis, exactly as the analysis concluded them.
2. **The attribution judgment.** Infrastructure, sponsorship, and direction findings with their separate confidences — or "unattributed."
3. **The venue and format.** Report, article, platform disclosure, briefing, thread. Each has its own compression points.
4. **Who will retell it.** Journalists, officials, advocates, opponents. The retellers set the extraction risk.
5. **Named organizations or states.** Any entity the write-up names, and whether it has been offered a right of reply.
6. **Editorial pressure.** What editors or stakeholders want the headline to say, stated plainly so it can be tested.
7. **Outstanding unknowns.** Every `[VERIFY]` item still open from the analysis.

---

## Constraints

### Must
- Publish **nothing stronger than the assessment concluded**. Each published claim maps to a finding and its confidence.
- Build hedges **into the grammar of each claim** — subject, verb, and quantifier — rather than appending them.
- Use a **fixed confidence vocabulary**, define it once in the write-up, and use it identically throughout.
- Pre-write the **accurate headline, the accurate one-sentence summary, and the accurate social post**.
- Run an **extraction test** on every key sentence: read alone, out of context, does it still say what the evidence supports?
- State **what the findings do not show** in a dedicated, prominent passage — not a footnote.
- Offer a **right of reply** to any named organization or state before publication, and record the response or its absence.
- Keep the **three attribution questions separate** in the prose, as the analysis kept them.

### Must Not
- Use collapsing verbs — "linked to," "behind," "tied to," "orchestrated by" — unless the underlying finding supports that exact relation at high confidence.
- Refer to a set of accounts as "the network" or "the operation" when the finding is that they share behaviors.
- Name private individuals, or publish handles of accounts belonging to identifiable private people as participants.
- Count reports that trace to one original as independent confirmation, or cite prior coverage as corroboration it does not provide.
- Invent figures, account counts, reach estimates, or quotations to strengthen the narrative.
- Let an editor's headline stand without an explicit, recorded decision if it exceeds the findings.
- Publish methods detail that would function as an evasion guide for the behavior described.

---

## Instructions

### Step 1 — Build the claim ledger
List every claim the write-up will make, each mapped to its finding, confidence band, and basis. Any sentence in the draft that does not map to a ledger line is either removed or added to the ledger with its own grade.

### Step 2 — Define the confidence vocabulary once
Choose the terms (for example low / moderate / high assessed confidence), define each in one line, and place the definitions early in the write-up. Then use only those terms. Varying phrasing — "suggests," "indicates," "points to" — reads as varying confidence to every reader.

### Step 3 — Rebuild each claim structurally
Rewrite key claims so the hedge carries the grammar: "Accounts showing these three behaviors posted within the same four-hour windows (moderate confidence)" rather than "A coordinated network posted in bursts." Replace collapsing verbs with the relation actually found.

### Step 4 — Separate the attribution questions in prose
Where attribution appears, state infrastructure, sponsorship, and direction separately with their own confidences. If attribution is unattributed, say so plainly and early; do not let adjacency to a named state imply one.

### Step 5 — Write the "what this does not show" passage
State, prominently, what the findings do not establish: effect on belief or behavior, sponsorship, direction, scale beyond what was observed. This passage is what careful retellers quote, and its absence is what careless ones exploit.

### Step 6 — Pre-write the compressions
Draft the accurate headline, one-sentence summary, and social post. Each must be true when read alone. Offer these to editors and communications staff before they write their own.

### Step 7 — Run the extraction test and right of reply
Pull each key sentence out of context and read it as a stranger would. Fix any that strengthen in isolation. Offer a right of reply to any named organization or state and record the response or its absence.

### Step 8 — Adversarial check
Write the worst accurate-sounding retelling a hostile or over-eager reader could produce from this draft, then close the openings it used. Record any editorial override of the findings as an explicit decision with its owner.

---

## False-Positive Prevention

1. **Collapsing verbs.** "Linked to" and "behind" asserted where the finding is "shares behaviors with" or "consistent with." The single most common source of overstatement.
2. **Nouns that assert.** "The network," "the operation," "the campaign" — each presupposes the coordination the analysis only graded.
3. **Vocabulary drift.** Using several phrasings for the same confidence, which readers decode as several confidences.
4. **Appended hedges.** Caveats placed at paragraph end, which editing and excerpting remove first.
5. **Headline ceded.** Leaving the headline and summary to someone who did not do the analysis and has different incentives.
6. **Attribution by adjacency.** Placing a named state or organization near the findings so readers infer a link the analysis did not make.
7. **Circular corroboration.** Citing prior coverage of the same original finding as independent support.
8. **Silence on limits.** Omitting what the findings do not show, so that retellers fill the gap with the strongest available reading.

---

## Output Format

```
# Write-up package — [assessment]

## Claim ledger
| Claim as it will be published | Finding | Confidence | Basis |
|---|---|---|---|

## Confidence vocabulary (defined once, used identically)
- Low: [...]
- Moderate: [...]
- High: [...]

## Structural rewrites
| Draft sentence | Problem | Rewritten |
|---|---|---|
| [...] | [collapsing verb / asserting noun / appended hedge] | [...] |

## Attribution in prose
Infrastructure: [...] · Sponsorship: [...] · Direction: [...] — or **unattributed**

## What these findings do not show
[Prominent passage: effect, sponsorship, direction, scale beyond observation]

## Pre-written compressions
Headline: "[...]"
One-sentence summary: "[...]"
Social post: "[...]"

## Extraction test
| Sentence | Read alone, does it overstate? | Fix |
|---|---|---|

## Right of reply
| Named entity | Offered on | Response |
|---|---|---|

## Adversarial check
Worst accurate-sounding retelling: "[...]"
Openings closed: [...]

## Editorial overrides (if any)
[What was changed beyond the findings, by whom, with the risk named]
```

---

## Verification

- [ ] Every published claim maps to a finding and its confidence in the ledger.
- [ ] The confidence vocabulary is defined once and used without variation.
- [ ] Hedges are built into the grammar of key claims rather than appended.
- [ ] Attribution questions are kept separate, and "unattributed" is stated plainly where it applies.
- [ ] A prominent "what this does not show" passage exists.
- [ ] Accurate headline, summary, and social post are pre-written and true when read alone.
- [ ] The extraction test was run on every key sentence.
- [ ] Right of reply was offered to named entities and the outcome recorded.
- [ ] No collapsing verb, asserting noun, invented figure, or circular corroboration remains in the draft.
- [ ] No private individual is named, and no evasion-enabling methods detail is published.
