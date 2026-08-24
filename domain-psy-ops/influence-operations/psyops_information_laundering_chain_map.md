---
title: "Information Laundering Chain Map — How a Claim Becomes Citable"
category: psy-ops/influence-operations
description: "Map the hops by which an unsourced claim acquires citability: placement in a low-scrutiny outlet, citation by a marginally more credible one, aggregation, and finally reference by an institution that treats the chain as sourcing. Locates the citation loop where outlets cite each other in a circle with no original evidence, and identifies the hop where the hedge was dropped."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - psy-ops
  - information-laundering
  - sourcing
  - media-analysis
  - verification
updated: "2026-07-28"
reasoning:
  styles: [analytic, evidential, systems]
  stakes: high
  horizon: months
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: cross_domain
  collaboration: solo_or_team
  output_format: citation_chain_map
  user_role: [analyst, journalist, researcher, fact_checker]
  mode: [assess, document, audit]
related_prompts:
  - domain-psy-ops/technique-analysis/psyops_provenance_and_transmission_trace.md
  - domain-psy-ops/influence-operations/psyops_narrative_lifecycle_tracker.md
  - domain-reasoning-craft/epistemic/epistemic_source_credibility_triangulation.md
---

# Information Laundering Chain Map

**Objective:** Map how a claim with no original evidence acquired the appearance of being sourced. The mechanism is a chain of citations in which each hop borrows credibility from the last: a claim is placed somewhere with low editorial scrutiny, cited by something marginally more credible, picked up by an aggregator, and eventually referenced by an institution — a court filing, a policy paper, a broadsheet, a legislative record — that treats the accumulated chain as sourcing. **No hop adds evidence. Every hop adds authority.** The final citation looks impeccable and rests on nothing.

Two things are being located. First, the **citation loop**: outlets citing each other in a circle, where following any reference eventually returns to where you started without ever reaching an observation. Second, the **hedge-drop hop**: the specific transition where "alleged," "reportedly," or "according to an unnamed source" became a statement of fact. That hop is usually identifiable, is usually a single article, and is where the laundering actually happens.

**When to use:**
- A claim is widely cited and you cannot find anyone who established it.
- A reputable source has stated something as fact and you want to check its sourcing chain.
- You are fact-checking something that everyone seems to know.
- You are documenting how a false claim entered the record.

**When NOT to use:**
- You are tracing a single image or artifact — use `../technique-analysis/psyops_provenance_and_transmission_trace.md`.
- You are tracking a narrative's spread through communities rather than outlets — use `psyops_narrative_lifecycle_tracker.md`.
- You want to weigh sources against each other on general credibility — use `domain-reasoning-craft/epistemic/epistemic_source_credibility_triangulation.md`.

**Audience:** Fact-checkers, journalists, researchers, and analysts trying to find the bottom of a citation chain.

---

## Inputs / Context

1. **The claim.** Stated precisely, in the form now being cited.
2. **The most authoritative current citation.** Where you encountered it in its most credible form.
3. **Each source's stated basis.** What each one says its evidence is — quoted, not summarized.
4. **What you have already followed.** Hops already traced, so the chain does not double back invisibly.
5. **The claim's current status.** Whether it is now treated as established, contested, or debunked.

---

## Constraints

### Must
- Follow each citation to **what it actually cites**, not what it appears to. A footnote to a reputable outlet often points to that outlet citing someone else.
- Record each hop's **stated basis verbatim**, including hedges, attributions, and qualifiers.
- Identify the **hedge-drop hop** precisely: where a qualified statement became an unqualified one.
- Detect and map **citation loops**, showing the cycle explicitly.
- Identify the **terminal node**: the earliest source that either presents original evidence or presents none. Say which.
- Distinguish **laundering from ordinary aggregation**. Reporting that accurately attributes and preserves hedges is normal journalism, not laundering.
- Note where the chain **crosses a credibility threshold** — into peer review, a court record, a government document, an encyclopedia.

### Must Not
- Assume laundering because a chain is long. Long accurate citation chains are normal in any well-covered subject.
- Conclude the claim is false because its sourcing is circular. Poorly sourced claims are sometimes true; the finding is about evidentiary basis, not truth.
- Fabricate an intermediate hop, a citation, an outlet, or a publication date to close a gap.
- Attribute intent to any outlet in the chain. Most hops are ordinary aggregation under deadline by people who assumed the previous outlet had checked.
- Treat an outlet's general reputation as evidence about this specific chain. Reputable outlets launder claims regularly, usually inadvertently.
- Present a partial trace as complete. Untraced branches must be shown as untraced.

---

## Instructions

### Step 1 — Fix the claim in its current authoritative form
Quote it exactly as the most credible current source states it, with that source's attribution language.

### Step 2 — Follow the citation one hop and record verbatim
Go to what it cites. Record what that source says its basis is, word for word, preserving every hedge.

### Step 3 — Repeat until you reach a terminal node or a loop
Continue hop by hop. Stop when you reach original evidence, an explicit absence of evidence, a dead end, or a source you have already visited — which means a loop.

### Step 4 — Map any loop explicitly
If sources cite each other in a cycle, draw it. A citation loop with no original evidence anywhere in it is the strongest possible finding here.

### Step 5 — Locate the hedge-drop hop
Compare attribution language across hops. Find the exact transition where qualification disappeared: "sources say X is possible" becoming "X, according to [outlet]."

### Step 6 — Mark credibility threshold crossings
Note where the claim entered a venue that confers durable authority — peer-reviewed literature, a court filing, a legislative record, an encyclopedia. These are hard to reverse and are where laundering pays off.

### Step 7 — Classify the terminal node
Original evidence / explicit absence of evidence / anonymous assertion / dead link / untraceable. State which and how confident you are that nothing earlier exists.

### Step 8 — Adversarial check and characterization
Argue that this is normal aggregation, that the original evidence exists somewhere you have not looked, and that the hedge-drop was ordinary editorial compression. Then characterize the chain.

---

## False-Positive Prevention

1. **Length as evidence.** A long chain is normal for a well-covered topic. Circularity and absence of a terminal evidence node are the findings, not hop count.
2. **Circularity read as falsity.** Poor sourcing means the claim is unestablished, not that it is false. Keep evidentiary basis and truth separate.
3. **Search limits mistaken for absence.** Concluding no original source exists when you searched one language, one archive, or only online sources. State your search bounds.
4. **Intent attributed to outlets.** Nearly every hop is a deadline-pressed writer assuming the prior outlet checked. Laundering is usually emergent, not designed.
5. **Reputation transferred to the chain.** Assuming a reputable outlet verified independently. Check what it actually cites; it is frequently the same upstream node.
6. **Aggregation mislabeled.** Accurate attribution with hedges preserved is normal journalism. Laundering requires hedges lost or basis misrepresented.
7. **Partial trace presented as complete.** Following one branch of a multi-branch chain and reporting a terminal node. Show untraced branches.
8. **Fabricated closure.** Inventing a plausible intermediate source to complete an otherwise unsatisfying map.

---

## Output Format

```
# Laundering chain — [claim]

## The claim, as currently cited
"[verbatim]" — [most authoritative source, date, its attribution language]

## Chain (authoritative → earliest)
| Hop | Source | Date | Stated basis (verbatim) | Hedges present | Cites |
|---|---|---|---|---|---|
| 1 | [outlet] | [date] | "according to [outlet 2]" | none | hop 2 |
| 2 | [outlet 2] | [date] | "sources reportedly indicate" | reportedly | hop 3 |

## Citation loop
[Cycle drawn explicitly, or "none detected"]

## Hedge-drop hop
**At hop [n]:** "[hedged version]" → "[unhedged version]"
[The single transition where qualification was lost]

## Credibility threshold crossings
| Hop | Venue | Why this is durable |
|---|---|---|

## Terminal node
[Original evidence / explicit absence / anonymous assertion / dead link / untraceable]
Search bounds: [languages, archives, date ranges, offline sources not checked]

## Untraced branches
[Any citation not followed, shown as untraced]

## Characterization
[Laundered — no original evidence / poorly sourced but traceable to evidence / normal aggregation]

## Truth status (separate question)
[Whether the claim is true, assessed independently of its sourcing — or "not assessed"]

## Adversarial check
[The case that this is normal aggregation and the evidence exists where I have not looked]
```

---

## Verification

- [ ] Every hop's stated basis is recorded verbatim with hedges preserved.
- [ ] Each citation was followed to what it actually cites, not what it appears to cite.
- [ ] Any citation loop is drawn explicitly.
- [ ] The hedge-drop hop is located precisely, with both versions quoted.
- [ ] The terminal node is classified, and search bounds are stated so absence is not overclaimed.
- [ ] Untraced branches are shown as untraced; no partial trace is presented as complete.
- [ ] The claim's truth is assessed separately from its sourcing, or explicitly not assessed.
- [ ] No intent is attributed to any outlet in the chain.
- [ ] Normal accurate aggregation is distinguished from laundering.
- [ ] No hop, citation, outlet, or date was invented to close a gap.
