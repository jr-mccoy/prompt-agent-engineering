---
title: "Propaganda Technique Identification — Name the Move, Quote the Evidence"
category: psy-ops/technique-analysis
description: "Dissect a single artifact — a post, ad, speech, article, or video script — into the specific persuasion and propaganda techniques it uses, each named and anchored to a quoted span. Separates technique presence from intent and from falsity, since ordinary honest communication uses many of the same moves. Counters the failure mode of labeling any disagreeable message 'propaganda' without being able to point at what in it does the work."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - psy-ops
  - propaganda
  - rhetoric
  - media-literacy
  - analysis
updated: "2026-07-28"
reasoning:
  styles: [analytic, evaluative, evidential]
  stakes: moderate
  horizon: immediate
  uncertainty: ambiguity
  evidence_quality: strong
  domain_complexity: single_domain
  collaboration: solo_or_pair
  output_format: annotated_technique_inventory
  user_role: [analyst, educator, journalist, individual]
  mode: [assess, audit, teach]
related_prompts:
  - domain-psy-ops/technique-analysis/psyops_emotional_manipulation_decoder.md
  - domain-psy-ops/technique-analysis/psyops_framing_and_narrative_analysis.md
  - domain-psy-ops/case-studies-taxonomies/psyops_technique_taxonomy_reference.md
---

# Propaganda Technique Identification

**Objective:** Take one artifact and produce an evidenced inventory of the persuasion techniques operating in it — each technique named, each anchored to a specific quoted span, each rated for how load-bearing it is to the piece. The discipline is that **naming requires pointing**: if you cannot quote the words doing the work, the technique is not established. The analysis holds three things apart that are routinely collapsed: whether a technique is *present*, whether the content is *true*, and whether the author *intended* to deceive. All three can vary independently, and only the first is directly observable in the text.

This matters because most persuasion techniques are not inherently illegitimate. Emotional appeal, repetition, vivid anecdote, authority citation, and in-group language appear in public health messaging, closing arguments, sermons, and safety warnings. What distinguishes propaganda is usually density, deception, and the absence of anything that would let the audience check — not the presence of any single move.

**When to use:**
- You have one artifact in hand and want a rigorous account of how it works on a reader.
- You are teaching media literacy and need a worked example rather than an abstract list.
- You want to explain to someone else why a piece felt manipulative, in terms they can verify themselves.
- You are building the per-artifact layer of a larger influence-operations assessment.

**When NOT to use:**
- You are assessing a pattern across many accounts or weeks — use `../influence-operations/psyops_influence_operation_analysis.md`.
- The question is specifically about emotional levers — use `psyops_emotional_manipulation_decoder.md`.
- The question is about statistical or chart distortion — use `psyops_statistical_and_visual_distortion_scan.md`.
- You want general logical fallacy detection with no influence framing — use `domain-reasoning-craft/epistemic/epistemic_logical_fallacy_scan.md`.

**Audience:** Analysts, educators, journalists, moderators, and individuals who want to understand a specific piece of persuasive content.

---

## Inputs / Context

1. **The artifact.** The full text, transcript, or description. Partial excerpts limit the analysis and must be flagged as partial.
2. **Its context.** Where it appeared, who published it, when, and to whom. Say if unknown.
3. **The apparent audience.** Who it seems built for — which is often not who is reading it now.
4. **What you already know about the claims.** Which assertions you can independently verify true or false, and which you cannot.
5. **Your relationship to the content.** Whether you agree, disagree, or are neutral. This is an input because it predicts your errors.

---

## Constraints

### Must
- Anchor every named technique to a **quoted span** from the artifact. No quote, no finding.
- Rate each technique's **load** — is the piece's persuasive work resting on it, or is it incidental?
- Keep **technique presence, factual accuracy, and authorial intent** in separate columns. Never infer one from another.
- Note the **legitimate uses** of any technique you flag, so the reader can calibrate.
- Identify what the piece **does not give the audience** — sourcing, counterarguments, uncertainty, a way to check.
- Assess **density and convergence**: many techniques pointing the same direction is more diagnostic than any single one.
- Give an overall characterization that distinguishes **ordinary persuasion / aggressive advocacy / manipulative content / deceptive content**.

### Must Not
- Assert the author's intent. You can observe technique and effect; you cannot read minds from a text. Say "the effect is X," not "the author wanted X."
- Call something propaganda because you disagree with its conclusion. Run the substitution test: would this analysis survive if the same techniques argued the opposite side?
- Fabricate a quote, misquote, or trim a quotation so it changes meaning. Quote spans must be verbatim and long enough to be fair.
- Invent technique names or attribute a taxonomy to a source you have not verified. Use established names, or describe the move plainly.
- Treat the presence of emotion as evidence of manipulation. Grief, fear, and anger are appropriate responses to real things.
- Produce a rewritten, "more effective" version of the artifact. This prompt analyzes; it does not optimize persuasion.

---

## Instructions

### Step 1 — Read once for effect, before analyzing
Note your own reaction: what did it make you feel, believe, or want to do? Record this now; it is data about the artifact and it will be contaminated by analysis later.

### Step 2 — Segment the artifact
Break it into functional parts: hook, framing, evidence, emotional turn, in-group signal, call to action. Not every piece has all of them; note which are missing.

### Step 3 — Inventory techniques with quoted anchors
Work through the artifact and name each technique you can anchor: loaded language, glittering generalities, name-calling, transfer/association, testimonial, plain-folks, bandwagon, card-stacking, false dilemma, repetition, scapegoating, urgency, in-group/out-group construction, prebunking of critics ("they will tell you…"). Quote the span for each.

### Step 4 — Score truth separately
For each factual assertion, mark verified true, verified false, misleading-but-technically-true, or unverified. Most will be unverified; say so rather than guessing.

### Step 5 — Assess what is withheld
What would a reader need to evaluate this independently — sources, base rates, the counterargument, the author's interest — and which of those are absent?

### Step 6 — Rate load and density
Which techniques carry the piece, and how many converge on the same conclusion? Note whether removing the top two techniques would leave an argument standing.

### Step 7 — Run the substitution test
Rewrite your characterization as though the identical techniques were deployed for the position you hold. Does the analysis still read as fair? If not, revise until it does.

### Step 8 — Adversarial check
Argue that this is ordinary, legitimate advocacy and you are over-reading craft as manipulation. Then give the overall characterization and say what evidence would move it.

---

## False-Positive Prevention

1. **Disagreement mistaken for propaganda.** Flagging technique density in content you oppose and calling the same density "good writing" elsewhere. The substitution test is mandatory, not optional.
2. **Intent asserted from text.** Concluding the author meant to deceive. Effects are observable; intentions are not. Write in effect language.
3. **Emotion treated as manipulation.** Marking any emotional appeal as illegitimate. Appropriate emotion about real stakes is honest communication; the question is whether the emotion is earned by the facts.
4. **Technique inflation.** Listing fifteen techniques where two are doing the work, which inflates the appearance of manipulation. Rate load; report the load-bearing ones first.
5. **Quote trimming.** Cutting a span so it demonstrates the technique better than the full passage does. Quote fairly and long enough.
6. **Taxonomy fabrication.** Inventing official-sounding technique names or citing a framework you have not checked. Plain description beats a fabricated label.
7. **Single-technique verdicts.** Declaring propaganda on one move. Almost every persuasive text contains several; density and deception distinguish, not presence.
8. **Ignoring the honest reading.** Failing to consider that the author believes what they wrote and is arguing sincerely — which is the most common case even for content that is false.

---

## Output Format

```
# Technique analysis — [artifact]

## Source and completeness
[Where from, when, to whom, and whether the artifact is complete or excerpted]

## First-read effect (recorded before analysis)
[What it made me feel / believe / want to do]

## Technique inventory
| Technique | Quoted anchor | Load (high/med/low) | Legitimate use of this move |
|---|---|---|---|
| [name] | "[verbatim span]" | high | [where this move is honest] |

## Factual assertions (scored separately)
| Assertion | Status | Basis |
|---|---|---|
| [claim] | true / false / misleading / unverified | [how known, or "not checked"] |

## What is withheld from the reader
[Sourcing, counterarguments, uncertainty, author's interest — what is absent]

## Density and convergence
[How many techniques, pointing the same way; what remains if the top two are removed]

## Substitution test
[The same analysis with the techniques arguing my own position — does it still read as fair?]

## Characterization
[Ordinary persuasion / aggressive advocacy / manipulative / deceptive] — because [one line]

## Adversarial check
[The case that this is legitimate advocacy and I am over-reading]

## Unknowns
[Everything unverified, left unresolved]
```

---

## Verification

- [ ] Every named technique has a verbatim quoted anchor of fair length.
- [ ] Technique presence, factual accuracy, and intent are reported in separate places and never inferred from each other.
- [ ] No claim is made about what the author wanted; findings are stated as effects.
- [ ] The substitution test was run and the characterization survives it.
- [ ] Legitimate uses are noted for each flagged technique.
- [ ] Load is rated, and the analysis leads with load-bearing techniques rather than a long thin list.
- [ ] Unverified claims are labeled unverified rather than assumed false.
- [ ] No quote was trimmed to strengthen a finding, and no technique name or taxonomy was invented.
- [ ] The honest-author reading was considered explicitly.
- [ ] No rewritten or improved version of the artifact was produced.
