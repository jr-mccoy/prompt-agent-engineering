---
title: "Design a QA Harness for Visually-Delivered Work"
category: presentations/visual-planning
description: "Design a repeatable QA harness for work that ships as visuals — slides, dashboards, diagrams, infographics, deck images — where correctness isn't caught by type-checkers or tests. Produces a per-artifact checklist, a reviewer protocol, and a drift check, not a generic 'have someone else look at it' plan."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - QA-01
  - QA-18
difficulty: intermediate
tags:
  - visual-planning
  - qa-harness
  - review-protocol
  - visualizations
  - quality-control
updated: "2026-04-21"
related_prompts:
  - domain-presentations/visual-planning/visualplan_capability_frontier_map.md
  - domain-presentations/visual-planning/visualplan_modality_router.md
  - domain-presentations/visual-planning/visualplan_cascade_effects_scan.md
  - domain-presentations/powerpoint_deck_assembly_and_validation.md
  - domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md
---

# Design a QA Harness for Visually-Delivered Work

**Objective:** Visuals ship wrong more often than text because the usual safety nets (type checkers, unit tests, grammar checkers) don't catch visual-specific errors: wrong axis scale, mislabeled series, a typo in a category name that makes the whole chart wrong, a legend that contradicts the data, a slide whose claim isn't supported by its chart, a rendered infographic with a swapped number. This prompt designs a QA harness specific to the artifact type the user ships — with a per-artifact checklist, a review protocol, drift checks, and explicit escalation.

**When to use:**
- The user regularly ships visual artifacts (board decks, dashboards, infographics, worksheets, data viz, diagrams, image-generation outputs).
- A visual artifact shipped wrong recently and the user wants a systematic fix.
- A team is standardizing review for visual work and needs a shared harness.
- An IC is setting up their own solo QA pass for visuals before sending them out.

**Don't use when:** The artifact is pure text with no visual structure. Use a text-editing workflow.

**Audience:** The person who owns the visual artifact's quality — IC, designer, analyst, or lead. Output is a checklist + protocol document they use per artifact.

---

## Inputs Required

1. **The artifact type.** Specific: "board decks with ~20 slides and 5–8 charts," "weekly revenue dashboard in Looker," "process infographics rendered by DALL-E," "worksheet PNGs for K-5 math." One type per harness; different types get different harnesses.
2. **A recent example.** Paste or reference a real artifact of this type the user has shipped.
3. **Known past failures.** 3–5 specific errors the user (or their team) has shipped in this artifact type recently. Verbatim where possible: "axis was 0–100% but the data only went to 45%, making the bars look huge" or "I generated 8 badge images and one had the wrong student name."
4. **Audience + stakes.** Who consumes the artifact and what happens when it's wrong. Changes the harness rigor.
5. **Tooling.** How the artifact is produced (PowerPoint, Figma, Tableau, DALL-E, Midjourney, code-generated chart). Affects what automation can do.
6. **Cadence.** How often the artifact ships and who reviews it today.

---

## Instructions

### Step 1 — Enumerate the failure modes this artifact type is prone to

Use inputs 3 and the artifact type. Categorize failures:

| Category | Examples |
|----------|----------|
| **Data-to-visual translation** | Wrong axis, wrong scale, wrong chart type for the claim, missing units, misleading truncation. |
| **Labeling** | Wrong title, wrong legend, category label typo, swapped series, mislabeled cell. |
| **Claim-evidence mismatch** | Slide's narrative claim isn't supported by the chart on the slide. |
| **Rendering** | Text overflow, overlapping elements, transparent backgrounds on opaque-required outputs, image generation producing the wrong count / orientation / layout. |
| **Consistency** | Fonts / colors / date formats drift across the artifact. |
| **Source integrity** | Underlying data changed; artifact not re-rendered. Data reference URLs broken. |
| **Accessibility** | Contrast, text size, alt text, color-blind readability. |

Not every artifact needs every category. Include the ones relevant to the type; drop the rest and note the drops.

### Step 2 — Build the per-artifact checklist

Produce a flat checklist, organized by category, that the author runs before shipping. Rules:

- Each item is observable (inspection or automated).
- Each item has a pass/fail outcome.
- Max ~20 items total. Longer checklists go unread.

Include items sourced directly from input 3 (past failures). Every past failure must map to a checklist item that would have caught it.

### Step 3 — Build the reviewer protocol

If the artifact has a reviewer (a second human), specify what the reviewer does, distinct from the author:

- **Reviewer reads the artifact cold.** They should not have the author's context. Their job is to approach it the way the final audience will.
- **Reviewer answers 3 questions:**
  1. What is this artifact claiming?
  2. Does the visual evidence support the claim?
  3. Is there anything that makes me do a double-take, even if I can't immediately say why?
- **Reviewer flags specific items from the checklist** that they examine.
- **Reviewer's role is not to verify data accuracy.** That's the author's; the reviewer can't re-derive data in review time.

For solo work (no reviewer), specify a "cold re-read" protocol: set the artifact aside for N hours or days, return to it with the reviewer lens.

### Step 4 — Identify what can be automated

For the tooling in input 5, enumerate what can be checked by tool rather than eye:

- For code-generated charts: assert expected data range, expected axis bounds, expected series count.
- For image-generation: assert dimensions, file count, output filename pattern.
- For deck tools: lint checklists exist (spell check, embedded-file integrity, slide numbering).
- For dashboards: data freshness alerts, null-count checks, schema monitors.

Automation replaces checklist items only where reliable; otherwise it supplements. Note the delta.

### Step 5 — Define the ship gate

When does the artifact leave the author? Concrete:

- Author checklist complete.
- Reviewer (if applicable) signed off.
- Automation checks green.
- Known escalation items (e.g., high-stakes numbers) spot-verified against source.

A single missed gate item stops the ship. The escape hatch is a named person authorizing an exception, not a silent bypass.

### Step 6 — Define drift checks

QA harnesses rot. Schedule:

- **Per-artifact:** Any new failure that ships → add a checklist item within one week.
- **Monthly:** Review the last N artifacts against the checklist — any items no longer needed (automation caught them)? Any items that aren't actually catching their target?
- **Quarterly:** Run a pre-mortem: "which failure mode would embarrass us next? Is it covered?"

Name an owner.

### Step 7 — Handle image-generation specifically (if in scope)

Image generation has pathological failure modes the harness must cover:

- **Count and layout:** Output N items, in specified orientation, without hallucinated extras.
- **Text integrity:** Any text in the image reads correctly and matches intent (names, numbers, labels).
- **Physical-world plausibility:** If the image is of something that maps to a real thing (person, product, logo), does it match the real thing?
- **Instruction leakage:** No visible prompt text, no UI chrome artifacts, no placeholder watermarks.

For image-gen, a human eye is required. Automation can partially help (OCR the text; file-count check) but cannot replace the eye for identity or layout.

### Step 8 — Define an escalation path

When a checklist item fails, what happens:

- Auto-fix where trivial (regenerate with clarified prompt; re-export).
- Reviewer note for "likely fine but check" items.
- Hard stop for "can't ship without a fix" items. Name which categories are hard-stop.

### Step 9 — Validate the harness against past failures

For each failure in input 3:

- Would the checklist have caught it?
- Would the reviewer protocol have caught it?
- Would automation have caught it?

If any input-3 failure is not covered, revise.

### Step 10 — Verify and output

Run the verification checklist.

---

## Constraints

### Must
- Produce a per-artifact checklist with ≤ ~20 items.
- Map every past failure (input 3) to a catching item.
- Distinguish author checklist from reviewer protocol.
- Separate automatable checks from eye-check items.
- Schedule drift reviews with an owner.
- Include image-generation-specific failure modes if in scope.

### Must Not
- Produce a generic QA checklist that applies to all artifact types.
- Make the reviewer responsible for re-deriving data accuracy.
- Let the checklist exceed ~20 items; longer lists go unread.
- Rely on automation for identity / layout checks in image generation.
- Leave drift review unscheduled.
- Bypass gates without a named exception authorization.

---

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Assume automation can catch labeling errors. Automated tools flag structural errors; wrong-but-plausible labels usually pass.
- Treat "it looks right" as a pass. A chart can look right and still be wrong (axis truncation, swapped series).
- Combine the author's checklist and reviewer's checklist. They have different cognitive jobs.
- Let the reviewer skim the artifact. The reviewer's job is cold read; partial skim misses the category it's designed to catch.
- Include items like "artifact is high quality." If a checklist item isn't pass/fail by inspection, it doesn't belong.

✅ **DO:**
- Include one "claim-evidence" item per artifact: what does this assert, and does the visual support it?
- Include one source-check item: is the underlying data still current as of the ship date?
- Include cold-read time in solo-author protocols. An hour of rest or a sleep before review is the equivalent of a reviewer.
- Make reviewer sign-off a named action (comment, approval, initials) so it's auditable.
- For rendered / generated artifacts, require the author to visually inspect every generated output, not a sample — image generation errors don't distribute uniformly.

---

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** Checklist is followed but too generic; specific failure ships; team stops trusting the checklist.

❌ **UNHELPFUL failure:** Harness is so heavy that artifacts ship late or not at all; authors skip the harness; same outcome as no harness.

✅ **Quality check:** An author can run the harness on a typical artifact within a reasonable fraction of total artifact time (e.g., 10–20%). A reviewer can complete their protocol in 5–15 min for a typical artifact.

---

## Output Format

```markdown
# Visual QA Harness — [Artifact Type]

## Scope
- Artifact type: 
- Tooling: 
- Cadence: 
- Audience + stakes: 

## Failure-Mode Inventory
[Categories applicable to this type; categories deliberately dropped]

## Author Checklist (≤ 20 items)
### Data-to-Visual Translation
- [ ] 
### Labeling
- [ ] 
### Claim-Evidence
- [ ] 
### Rendering
- [ ] 
### Consistency
- [ ] 
### Source Integrity
- [ ] 
### Accessibility
- [ ] 
### Image-Generation Specific (if in scope)
- [ ] 

## Reviewer Protocol
1. Read cold (no author context).
2. Answer: (a) what is this claiming? (b) does the evidence support it? (c) anything that makes you double-take?
3. Spot-check flagged checklist items.
4. Sign off with [mechanism].

(For solo work: cold re-read after N hours, with reviewer lens.)

## Automation
- [Automated checks wired into tooling]
- [Items that remain eye-check]

## Ship Gate
- [ ] Author checklist complete.
- [ ] Reviewer sign-off.
- [ ] Automation checks green.
- [ ] High-stakes numbers spot-verified.
- Exception authorization: [named person]

## Drift Checks
- Per-artifact: new failure → checklist item within 1 week.
- Monthly: checklist audit against recent artifacts.
- Quarterly: pre-mortem.
- Owner: 

## Input-Failure Coverage
| Past failure (input 3) | Catching mechanism |
|------------------------|--------------------|
| | Author / Reviewer / Automation |

## Escalation
- Hard-stop categories: [list]
- Fix-and-reship categories: [list]
- "Likely fine, note in review" categories: [list]
```

---

## Verification

- [ ] Checklist is artifact-specific, not generic.
- [ ] ≤ 20 checklist items.
- [ ] Every past failure maps to a catching mechanism.
- [ ] Reviewer protocol distinct from author checklist.
- [ ] Automation vs eye-check explicit.
- [ ] Ship gate lists all required passes.
- [ ] Drift reviews scheduled with owner.
- [ ] Image-gen-specific modes included if in scope.
- [ ] Harness completes in reasonable fraction of artifact production time.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Output is a per-artifact QA harness, not a generic review pitch.
- **ST-02 (Structured Sequential Instructions):** Ten steps enumerate failures → checklist → reviewer → automation → gate → drift → image-gen → escalation → validate → verify.
- **CM-02 (Constraint Specification):** Must Not block forbids generic checklists, over-long checklists, and silent gate bypass.
- **DS-01 (Framework Application):** Seven failure-mode categories are the framework; the harness is the per-type instance.
- **QA-01 (Self-Verification):** Verification checklist + input-failure coverage table validate the harness before it ships.
- **QA-18 (Domain-Specific Smell Tests):** The "does anything make you double-take" reviewer question is the load-bearing catch for the visual errors automation misses.
