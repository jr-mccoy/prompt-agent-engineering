---
title: "Rhetorical Deception Scan — Structural Bad Faith, Not Ordinary Fallacy"
category: psy-ops/technique-analysis
description: "Scan an argument for the structural moves that make it unfalsifiable or unanswerable in practice: motte-and-bailey, gish gallop, just-asking-questions, false balance, concern trolling, goalpost shifting, and prebunked criticism. Distinguishes these from honest error, since the same surface can come from confusion or from design. Complements general fallacy detection by focusing on moves whose function is to exhaust or trap a responder rather than to reason badly."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - psy-ops
  - rhetoric
  - bad-faith
  - argumentation
  - analysis
updated: "2026-07-28"
reasoning:
  styles: [analytic, adversarial, dialectical]
  stakes: moderate
  horizon: immediate
  uncertainty: ambiguity
  evidence_quality: strong
  domain_complexity: single_domain
  collaboration: solo_or_pair
  output_format: structural_move_inventory
  user_role: [analyst, moderator, journalist, educator, individual]
  mode: [assess, audit, decide]
related_prompts:
  - domain-psy-ops/technique-analysis/psyops_propaganda_technique_identification.md
  - domain-reasoning-craft/epistemic/epistemic_logical_fallacy_scan.md
  - domain-reasoning-craft/epistemic/epistemic_disagreement_diagnosis.md
---

# Rhetorical Deception Scan

**Objective:** Identify the **structural** moves in an argument whose function is to make it unfalsifiable, unanswerable, or exhausting to engage rather than merely to reason badly. This is a narrower target than general fallacy detection: a non sequitur is an error, while a motte-and-bailey is a structure. The moves in scope — motte-and-bailey, gish gallop, just-asking-questions, false balance, concern trolling, goalpost shifting, prebunked criticism, and the isolated-demand-for-rigor — share a signature: **they cost the responder far more than the arguer**, and they leave the arguer a retreat that costs nothing.

The scan's hard constraint is that identical surface behavior arises from honest confusion. A person can genuinely hold the modest claim and the strong one without noticing they differ. Someone can raise many objections because they have many. A question can be sincere. The scan therefore reports **structure and asymmetry**, and treats bad faith as a hypothesis requiring behavior over time — most reliably, what happens when the move is named.

**When to use:**
- An exchange feels unwinnable and you want to identify the structure rather than conclude you argued badly.
- You are moderating and need to characterize a pattern in terms a participant can check.
- You are preparing to engage a public argument and want to know what you are walking into.
- You suspect your own argument may rest on one of these and want to check before publishing.

**When NOT to use:**
- You want general fallacy coverage — use `domain-reasoning-craft/epistemic/epistemic_logical_fallacy_scan.md`.
- You want to know why a disagreement persists — use `domain-reasoning-craft/epistemic/epistemic_disagreement_diagnosis.md`.
- The content is propagandistic rather than argumentative — use `psyops_propaganda_technique_identification.md`.
- You are deciding whether to respond publicly at all — use `../counter-messaging/psyops_rumor_response_triage.md`.

**Audience:** Analysts, moderators, journalists, educators, debaters, and anyone stuck in an exchange that will not resolve.

---

## Inputs / Context

1. **The argument.** Full text or transcript. For moves that unfold over time, the full exchange in sequence.
2. **The claim at issue.** What is actually being asserted, in your words and theirs — a divergence here is itself diagnostic.
3. **The exchange history.** Prior rounds, if any. Goalpost shifting and motte-and-bailey are only visible across turns.
4. **The forum.** Public, private, moderated, adversarial — this determines cost asymmetry.
5. **Your stake.** Whether you are a participant or an observer.

---

## Constraints

### Must
- Anchor each identified move to **quoted spans**, including both positions for two-position moves like motte-and-bailey.
- Compute the **cost asymmetry**: roughly what it costs to make the move versus to answer it properly.
- Offer the **honest-confusion reading** for every move identified. It is frequently the correct one.
- Distinguish moves visible **within one text** from those requiring **the exchange over time**.
- Note the **name-it test**: what a good-faith arguer does when the structure is pointed out (clarifies which claim they hold) versus what a bad-faith one does (switches again).
- Recommend a **response posture**: engage, engage-with-constraints, decline, or ask one clarifying question first.
- Scan **your own argument** for the same moves before concluding.

### Must Not
- Diagnose bad faith from a single instance. Bad faith is a hypothesis about a pattern, and a costly one to assert wrongly.
- Use the labels as an exit from a hard question. "That's a gish gallop" applied to a person with many genuine objections is itself a deflection.
- Name-call. The finding is about the structure of a move, never about the character of a person.
- Fabricate or paraphrase quotes into a cleaner example of the move than the original supports.
- Treat asking questions as inherently bad-faith. Most questions are questions.
- Conclude that a claim is false because it was defended with one of these moves. Bad advocacy is compatible with a true conclusion.

---

## Instructions

### Step 1 — State the claim in both versions
Write what you understand the claim to be, and what they say it is. If these differ substantially, a motte-and-bailey may already be visible.

### Step 2 — Scan for two-position structures
Look for a strong, contested claim (the bailey) that retreats under pressure to a modest, near-unarguable one (the motte), then reappears. Quote both. Note whether the retreat is ever acknowledged.

### Step 3 — Measure volume asymmetry
Count assertions requiring separate rebuttal. Estimate the time to make them versus the time to answer them. Flag a gish gallop only where the asymmetry is large *and* unanswered points get treated as conceded.

### Step 4 — Check the question layer
Are questions doing assertion's work — planting a claim while preserving deniability? The tell is whether answers change anything: sincere questions have answers that land, rhetorical ones regenerate.

### Step 5 — Check the goalposts
Across the exchange, has the standard of proof moved after being met? Quote the standard before and after. Also check for isolated demands for rigor — a standard applied to your evidence but not theirs.

### Step 6 — Check balance and framing moves
Is false balance presenting a lopsided evidentiary picture as an even dispute? Is criticism prebunked ("they'll call this X, which proves it")? Prebunking is notable because it makes disagreement into evidence for the claim.

### Step 7 — Offer the honest reading for each
For every move, write the version where the arguer is sincere and simply imprecise. Then say what would distinguish the readings — usually the name-it test.

### Step 8 — Scan your own side, then set posture
Run the same scan on your own argument and report anything found. Then recommend a posture and, if engaging, the single clarifying question that collapses the ambiguity.

---

## False-Positive Prevention

1. **Bad faith from one instance.** Structure is observable; intent is not. A single motte-and-bailey is usually imprecision.
2. **Labels as deflection.** Using "gish gallop" to avoid answering someone with many real objections. Check whether the objections are individually substantive before invoking volume.
3. **Questions treated as attacks.** Most questions are sincere. Reserve the finding for questions that regenerate no matter how well answered.
4. **The conclusion contaminating the assessment.** Finding more structural bad faith in arguments you disagree with. Run the scan on your own side; if it comes back clean every time, the scan is broken.
5. **False-balance overreach.** Calling any presentation of two sides false balance. It requires a genuinely lopsided evidence base, which you must establish rather than assume.
6. **Truth inferred from tactics.** Concluding the claim is false because it was badly defended. Poor advocacy and true conclusions coexist routinely.
7. **Ignoring forum cost.** Missing that the asymmetry is created by the venue — a live debate rewards volume regardless of anyone's intent.
8. **Person-directed findings.** Sliding from "this move is unfalsifiable" to "this person is a liar." The finding attaches to the move.

---

## Output Format

```
# Rhetorical structure scan — [argument / exchange]

## The claim, two ways
- As I understand it: [...]
- As they state it: [...]

## Structural moves identified
| Move | Quoted anchor(s) | Visible in | Cost to make | Cost to answer | Honest-confusion reading |
|---|---|---|---|---|---|
| Motte-and-bailey | bailey: "[...]" / motte: "[...]" | exchange | low | high | [sincere version] |

## Goalpost check
| Standard before | Standard after | Was the first standard met? |
|---|---|---|
| "[quote]" | "[quote]" | yes/no |

## Cost asymmetry summary
[Overall: how much cheaper it is to make these than to answer them, and whether unanswered points are being treated as conceded]

## The name-it test
[What a good-faith arguer would do if this structure were pointed out — and what has actually happened, if it has been]

## Scan of my own argument
[Structural moves found on my side, stated plainly — or "none found," with the caveat that self-scans run clean too easily]

## Response posture
[Engage / engage with constraints / decline / ask one question first] — because [one line]
**If engaging, the one clarifying question:** "[question that collapses the ambiguity]"

## Not established
[Anything that looks like a move but is equally consistent with confusion]
```

---

## Verification

- [ ] Every move has quoted anchors, including both positions for two-position structures.
- [ ] Cost asymmetry is estimated for each move.
- [ ] An honest-confusion reading is offered for every single move identified.
- [ ] No bad-faith conclusion rests on a single instance.
- [ ] Findings attach to moves, never to a person's character.
- [ ] The analyst's own argument was scanned and the result reported.
- [ ] The claim's truth is kept entirely separate from the quality of its defense.
- [ ] Moves requiring the exchange over time are distinguished from those visible in one text.
- [ ] A response posture is recommended, with one clarifying question if engaging.
- [ ] Quotes are verbatim; nothing was paraphrased into a cleaner example.
