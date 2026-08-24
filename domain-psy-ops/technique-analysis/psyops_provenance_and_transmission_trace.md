---
title: "Provenance and Transmission Trace — Where Did This Actually Come From"
category: psy-ops/technique-analysis
description: "Trace a claim, image, video, or document backwards through its chain of transmission toward first appearance, recording what changed at each hop: added captions, lost context, altered dates, shifted attribution, and upgraded certainty. Separates the provenance question (where did it come from) from the truth question (is it accurate), since old, recontextualized, and misattributed material is frequently authentic."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - psy-ops
  - provenance
  - osint
  - verification
  - analysis
updated: "2026-07-28"
reasoning:
  styles: [analytic, evidential, abductive]
  stakes: moderate
  horizon: immediate
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: single_domain
  collaboration: solo_or_pair
  output_format: transmission_chain_with_mutations
  user_role: [analyst, journalist, moderator, researcher, individual]
  mode: [assess, document, audit]
related_prompts:
  - domain-psy-ops/influence-operations/psyops_information_laundering_chain_map.md
  - domain-psy-ops/technique-analysis/psyops_statistical_and_visual_distortion_scan.md
  - domain-reasoning-craft/epistemic/epistemic_source_credibility_triangulation.md
---

# Provenance and Transmission Trace

**Objective:** Trace a specific artifact — a claim, photograph, video, screenshot, quote, or document — backwards toward its first appearance, recording **what changed at each hop**. Transmission is not lossless. Captions get added, context gets stripped, dates drift, attribution shifts from "an unnamed source said" to "officials confirmed," hedges disappear, and a photograph from one country and decade arrives as breaking news from another. The trace records those mutations as data.

The central discipline is separating **provenance from truth**. They are different questions with different answers, and conflating them produces error in both directions: authentic material is dismissed because it spread through disreputable channels, and fabricated material is accepted because a reputable outlet repeated it. A photograph can be entirely real and entirely misrepresented. That combination is the single most common pattern in visual misinformation, and it is invisible unless the two questions are kept apart.

**When to use:**
- Something is circulating and you need to establish where it came from before deciding what to do about it.
- An image or clip looks authentic but feels wrong for its stated context.
- You are checking a claim that everyone cites and no one sources.
- You are documenting a chain for a correction, a moderation decision, or a research write-up.

**When NOT to use:**
- You are mapping how a claim gained institutional legitimacy across outlets — use `../influence-operations/psyops_information_laundering_chain_map.md`.
- The question is whether a statistic or chart is distorted — use `psyops_statistical_and_visual_distortion_scan.md`.
- You want to weigh several sources against each other on credibility — use `domain-reasoning-craft/epistemic/epistemic_source_credibility_triangulation.md`.

**Audience:** Journalists, moderators, researchers, analysts, and individuals trying to establish where something came from before passing it on.

---

## Inputs / Context

1. **The artifact.** The specific claim, image, clip, quote, or document, exactly as you received it.
2. **How you received it.** Channel, sender, date, and the surrounding context it arrived in.
3. **The stated provenance.** What the artifact claims about itself: when, where, who, and from what source.
4. **What you have already checked.** Searches run, archives consulted, tools used — so the trace does not repeat work or double-count a single check.
5. **Time pressure.** Whether this needs a fast triage or a complete chain, since the honest depth of the trace depends on it.

---

## Constraints

### Must
- Record the chain as **discrete hops**, each with what was added, lost, or altered relative to the previous one.
- Keep the **provenance question and the truth question in separate sections** throughout. Never let one answer the other.
- Mark the **earliest instance you actually found**, and state plainly that it is the earliest *found*, not the origin.
- Log **mutations explicitly**: caption changes, crops, date shifts, attribution upgrades, hedge removal, translation drift.
- Preserve evidence by **archiving** each hop before it disappears, and note which hops are already dead links.
- Distinguish **authentic-but-recontextualized** from **fabricated** as separate outcomes, because they call for different responses.
- State the **residual uncertainty**: what you could not establish and what tool or access would settle it.

### Must Not
- Assert an origin. You found an earliest instance; origin is a much stronger claim and is usually unavailable.
- Treat "I could not find it earlier" as evidence of origination. Absence in searchable sources is not absence.
- Conclude the content is false because the chain is disreputable, or true because it is reputable. Provenance does not settle truth.
- Fabricate any timestamp, URL, account, outlet, or archive link. Unavailable hops are `[VERIFY]` or "not found."
- Name the individual who first posted something as a bad actor. Early posting is not authorship, and first sharers are usually recipients themselves.
- Assert technical manipulation of an image or video without the analysis to support it. "Looks off" is not a finding.

---

## Instructions

### Step 1 — Freeze and archive the artifact as received
Capture it exactly, with its surrounding context, before anything changes or is deleted. Record how it reached you.

### Step 2 — Extract every provenance claim it makes
List what the artifact asserts about itself — date, place, people, source — as claims to be tested rather than facts.

### Step 3 — Walk backwards hop by hop
Work from your copy toward earlier instances: reverse image search, quote search on distinctive phrasing, archive lookups, platform search by date range. Record each hop with its timestamp and archive it.

### Step 4 — Log the mutation at each hop
For each step, note precisely what changed: caption added or altered, image cropped, clip trimmed, date restated, attribution upgraded, hedge dropped, numbers rounded up. This log is the trace's main product.

### Step 5 — Identify the earliest instance found
State it as "earliest found," with the date and the search methods that would have surfaced anything earlier. Note the limits of those methods.

### Step 6 — Test the stated provenance against the earliest instance
Does the original context match the claim now attached? Mismatches between original context and current caption are the characteristic finding.

### Step 7 — Assess truth separately
Only now, in its own section, address whether the underlying content is accurate — and answer independently of how it traveled.

### Step 8 — Adversarial check and classification
Argue that the artifact is what it claims and your trace missed the earlier context. Then classify: authentic and correctly contextualized / authentic but recontextualized / altered / fabricated / undetermined.

---

## False-Positive Prevention

1. **Earliest-found read as origin.** The most common error. Your search covers indexed, public, still-live, language-accessible sources — a small slice of where things start.
2. **Provenance-truth conflation.** Dismissing accurate content for traveling through low-quality channels, or accepting false content because a broadsheet repeated it.
3. **Recontextualization missed.** Verifying that an image is genuine and stopping there, when the deception is entirely in the caption. Authenticity of the file is not authenticity of the claim.
4. **First-poster blamed.** Treating the earliest account you found as the originator or a bad actor. They are usually a recipient too, and naming them can direct harassment at an uninvolved person.
5. **Manipulation asserted on vibes.** Calling an image altered from compression artifacts, odd lighting, or unfamiliar rendering. Artifacts of re-encoding are not evidence of editing.
6. **Chain gaps papered over.** Presenting a smooth chain when several hops are inferred. Inferred hops must be marked inferred.
7. **Single-language search.** Concluding origin from English-language sources when the material began elsewhere. State the languages searched.
8. **Dead-link amnesia.** Failing to archive, then losing the evidence mid-analysis and reconstructing from memory.

---

## Output Format

```
# Provenance trace — [artifact]

## As received
[Exact artifact, channel, sender, date, surrounding context] — archived: [link or "archived locally"]

## Provenance claims made by the artifact
| Claim about itself | Status |
|---|---|
| [date / place / source] | untested / supported / contradicted |

## Transmission chain (latest → earliest found)
| Hop | Date | Where | Archived? | Mutation at this hop |
|---|---|---|---|---|
| 1 | [date] | [platform/outlet] | yes | caption added: "[...]" |
| 2 | [date] | [platform/outlet] | dead link | hedge removed; "reportedly" → "confirmed" |

**Inferred hops:** [any step not directly observed, marked as inferred]

## Earliest instance found
[Date, location, original context] — **earliest found, not origin.**
Search methods used: [reverse image, phrase search, archives, date-bounded platform search]
Languages searched: [...]
What could still be earlier: [what these methods would miss]

## Original context vs. current claim
[Side by side — the characteristic finding lives here]

## Truth assessment (separate question)
[Is the underlying content accurate, assessed independently of transmission]

## Classification
[Authentic + correctly contextualized / authentic but recontextualized / altered / fabricated / undetermined]

## Adversarial check
[The case that the artifact is what it claims and my trace missed context]

## Residual uncertainty
[What could not be established, and what access or tool would settle it]
```

---

## Verification

- [ ] The earliest instance is labeled "earliest found" and never described as the origin.
- [ ] The provenance question and the truth question are answered in separate sections, neither used to settle the other.
- [ ] Every hop logs its specific mutation; inferred hops are marked inferred.
- [ ] Hops are archived where possible, and dead links are recorded as dead rather than omitted.
- [ ] Authentic-but-recontextualized is available as a classification and was actively considered.
- [ ] No individual is named as an originator or bad actor on the basis of early posting.
- [ ] No manipulation is asserted without supporting analysis; re-encoding artifacts are not treated as editing.
- [ ] Languages and search methods are stated, with their blind spots.
- [ ] No timestamp, URL, outlet, or archive link was invented; unavailable items are marked `[VERIFY]`.
- [ ] Residual uncertainty is stated rather than resolved by assumption.
