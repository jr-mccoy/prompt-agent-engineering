---
title: "Ad Copy Variant Matrix — Angle × Audience × Format, One Variable Per Cell"
category: advertising/campaign
description: "Design the copy test grid before writing at volume: choose which angle × audience × format cells deserve to exist, state what each cell isolates and why, draft one tight variant per cell, and mark every character limit as [VERIFY current platform spec] rather than asserting it. Produces a launch-ready matrix with a hypothesis per row and a kill list of cells deliberately not built. Distinct from the ad-creative skill (bulk headline generation and iteration from performance data), the ab-test-setup skill (statistical design and sample size), and quality_slop_ad_copy (scoring finished copy)."
techniques:
  - RT-02
  - CM-02
  - OC-03
  - QA-01
difficulty: intermediate
tags:
  - advertising
  - ad-copy
  - creative-testing
  - paid-media
  - campaign
  - messaging
  - too-many-versions
  - which-ad-works
  - limited-test-budget
updated: "2026-09-24"
related_prompts:
  - domain-agentic-resources/skills/marketing/ad-creative/SKILL.md
  - domain-agentic-resources/skills/marketing/ab-test-setup/SKILL.md
  - domain-professional-writing/content-quality/quality_slop_ad_copy.md
---

# Ad Copy Variant Matrix

**Objective:** Turn a product, a set of audiences, and a set of placements into a
deliberately small copy matrix — every cell justified, every cell testing one thing,
every character limit left for verification — so that the first flight of ads
produces a readable result instead of forty variants that differ in everything.

**When to Use:**
- You are about to launch a campaign and have more angles, audiences, and formats
  than budget to test them all.
- A previous flight "tested" many ads and nobody could say what won or why.
- Stakeholders each want their message in the launch and you need a principled way
  to decide which cells ship.

**When NOT to use:**
- You need dozens of headline variants for an angle you already chose, or you are
  iterating from performance data — `domain-agentic-resources/skills/marketing/ad-creative/`.
- You need sample size, significance, or test duration —
  `domain-agentic-resources/skills/marketing/ab-test-setup/`.
- You have finished copy and want it scored —
  `domain-professional-writing/content-quality/quality_slop_ad_copy.md`.
- You need landing-page copy — `skills/marketing/copywriting/`.
- The claims in the copy have not been checked — run
  `adcampaign_claims_compliance_review.md` on the finished matrix before launch.

## Inputs / Context

1. **Product and offer**, in one sentence each, with the proof you actually hold
   (numbers, reviews, awards — sourced).
2. **Audiences** (2–4), each with the one problem they have that this solves.
3. **Placements** you will run (platform + format), from the media plan.
4. **Candidate angles** — the reasons someone would click (pain, outcome, proof,
   identity, comparison, curiosity).
5. **Budget and time available for the first flight**, so the matrix fits it.
6. **Mandatory elements** — brand name, disclaimers, trademark marks.

## Method

1. **Write the full cross-product, then cut it.** List angle × audience × format.
   Most cells should not exist. Cut a cell when the angle does not fit the
   audience's problem, the format cannot carry the angle (a proof angle with no
   room for the proof), or the budget cannot give it enough delivery to read.
2. **Pick the test axis.** Decide which dimension this flight is about — usually
   angle, because it moves results most. Hold the other two constant within each
   comparison group. A group varies one thing.
3. **Write a hypothesis per group.** "For [audience], a [angle] message will
   outperform [other angle] on [metric] because [reason from research]."
4. **Mark every limit as unverified.** For each placement, list the text fields
   (headline, primary text, description, overlay, CTA) with the limit column set
   to `[VERIFY current platform spec]`. Do not supply numbers from memory; specs
   change and differ by placement. Hand the field list to
   `adcampaign_placement_spec_checklist.md` to fill.
5. **Draft one variant per cell.** Short enough to survive the likely limit
   (write tight; you can expand after verification), leading with the angle in the
   first words, with every factual claim traceable to the proof list.
6. **Flag claims.** Tag any cell making a comparative, numerical, health, financial,
   or "free/guaranteed" claim `[CLAIM — review]` for the compliance pass.
7. **Write the kill list.** The cells you cut, and why. This is what stops them
   being added back in the review meeting.
8. **Define the read.** For each group: primary metric, what counts as a winner,
   and what happens to the loser. Statistical thresholds come from ab-test-setup,
   not from here.

## Output Format

```
# Copy matrix — [campaign]

## Test design
Axis tested this flight: [angle | audience | format]
Held constant: [...]
Groups: [n]   Cells: [n]   Budget per cell: [from media plan]

## Field limits (unverified)
| Placement | Field | Limit | Source / date checked |
|---|---|---|---|
| [placement] | [headline] | [VERIFY current platform spec] | [ ] |

## Matrix
| Cell | Group | Audience | Angle | Format | Headline | Body | CTA | Claim flag |
|---|---|---|---|---|---|---|---|---|

## Hypotheses
| Group | Hypothesis | Primary metric | Winner rule | Loser fate |
|---|---|---|---|---|

## Kill list
| Cut cell | Reason |
|---|---|

## Open items
- [claims to substantiate, specs to verify, proof to source]
```

## Verification

- [ ] Each comparison group varies exactly one dimension.
- [ ] Every cell traces to an audience problem and a proof item.
- [ ] No character limit appears as a number without a source and a check date.
- [ ] Every claim-bearing cell is flagged for the compliance review.
- [ ] Cell count × budget per cell fits the flight budget.
- [ ] The kill list is non-empty and each cut has a reason.

## False-Positive Prevention

1. **More variants is not more learning.** Forty ads that differ in angle, image,
   and CTA at once teach nothing; the matrix exists to prevent that.
2. **Do not assert character limits.** "Headlines are 30 characters" may be right
   today for one placement and wrong for another; mark it and verify.
3. **A winner in a starved cell is noise.** If budget per cell is too thin to
   read, cut cells rather than declaring results.
4. **Proof, not puffery.** A numerical or comparative line with no source in the
   proof list is removed or flagged — never softened into vagueness to dodge review.
5. **Do not let the kill list be silently reversed.** Re-adding a cut cell needs a
   reason written into the matrix.
6. **This is not the stats plan.** Do not invent significance thresholds or run
   lengths here; hand them to ab-test-setup.

## Example

**Input:** Meal-kit brand, offer "first box half price." Audiences: new parents
(no time), fitness trainees (macros). Placements: one social feed format, one
short-video format. Angles: time-saved, macro-precision, social proof ("4.6★ from
12,400 reviews" — sourced to review platform export, 2026-09-01). Flight: two weeks.

```
## Test design
Axis tested this flight: angle. Held constant: audience within group, feed format.
Groups: 2   Cells: 4   Budget per cell: [from media plan]

## Field limits (unverified)
| Placement | Field | Limit | Source / date checked |
| Social feed | Headline | [VERIFY current platform spec] | [ ] |
| Social feed | Primary text | [VERIFY current platform spec] | [ ] |

## Matrix
| C1 | G1 | Parents | Time-saved | Feed | Dinner in 20 minutes | Recipes + portioned ingredients at your door. | Get half off | — |
| C2 | G1 | Parents | Social proof | Feed | 12,400 families rate us 4.6★ | See why parents stay. | Get half off | CLAIM — review |
| C3 | G2 | Trainees | Macro-precision | Feed | Macros printed on every recipe | Hit targets without weighing. | Get half off | CLAIM — review |
| C4 | G2 | Trainees | Social proof | Feed | 4.6★ from 12,400 reviews | Rated by people who track. | Get half off | CLAIM — review |

## Hypotheses
| G1 | For parents, time-saved beats social proof on CTR because research interviews named time first | CTR | per ab-test-setup | paused |
| G2 | For trainees, macro-precision beats social proof on CTR because the need is precision | CTR | per ab-test-setup | paused |

## Kill list
| Parents × macro-precision | Angle does not match the audience's stated problem |
| Any × short video | Held for flight 2; budget cannot read four more cells |

## Open items
- C2/C4: "families" vs "reviews" — the export counts reviews, not families; C2 wording to fix.
- C3: confirm macros are printed on every recipe (ops to verify).
```

The open-items check caught that C2 turned a review count into a family count —
exactly the substitution the compliance review exists to stop.

## Techniques Used

- **RT-02 Multi-Dimensional Analysis Framework** — the angle × audience × format
  cross-product, analysed and cut per dimension.
- **CM-02 Constraint Specification** — one variable per group, and limits held as
  `[VERIFY]` constraints rather than facts.
- **OC-03 Markdown Table Specification** — the matrix, hypotheses, and kill list as
  fixed tables a media buyer can load.
- **QA-01 Self-Verification** — the checklist, and the open-items pass that caught
  the review-count substitution.

## Related Prompts

- `domain-agentic-resources/skills/marketing/ad-creative/` — volume variants per
  chosen angle, and iteration from performance data.
- `domain-agentic-resources/skills/marketing/ab-test-setup/` — sample size, run
  length, and significance for the winner rule.
- `adcampaign_placement_spec_checklist.md` — fills the limit column.
- `adcampaign_claims_compliance_review.md` — clears the flagged cells.
