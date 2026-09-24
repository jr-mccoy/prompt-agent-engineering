---
title: "Placement Spec Verification Checklist — Build It From the Campaign, Fill It From the Source"
category: advertising/campaign
description: "Produce a per-placement verification checklist for every asset a campaign needs — dimensions, aspect ratio, file type and size, duration, text-field limits, safe zones, caption and audio requirements, and policy-sensitive elements — with every value left blank for the operator to fill from the platform's current official documentation, a source and check date per row, and a pre-upload QA gate. Never asserts a spec from memory. Distinct from the ad-creative skill's platform-specs reference (a static spec table), the paid-ads skill's platform-setup-checklists (account, tracking, and audience setup), and the image prompts in this domain (which generate the images)."
techniques:
  - QA-04
  - QA-05
  - OC-03
  - QA-08
difficulty: beginner
tags:
  - advertising
  - ad-specs
  - placements
  - checklist
  - campaign
  - trafficking
updated: "2026-09-24"
related_prompts:
  - domain-agentic-resources/skills/marketing/ad-creative/references/platform-specs.md
  - domain-agentic-resources/skills/marketing/paid-ads/references/platform-setup-checklists.md
  - domain-advertising/campaign/adcampaign_copy_variant_matrix.md
---

# Placement Spec Verification Checklist

**Objective:** Turn a campaign's placement list and asset list into a checklist of
every spec that must be true before upload — each one blank, sourced, and dated when
filled — so that nothing goes live on a remembered number.

**When to Use:**
- Assets are about to be produced or trafficked and nobody has checked current specs.
- A previous launch was rejected, cropped, or had text covered by interface overlays.
- The same creative is going to several placements and you need to know which
  versions to cut.
- A reference table exists but nobody knows when it was last checked.

**When NOT to use:**
- You need account structure, pixels, conversion tracking, or audiences —
  `skills/marketing/paid-ads/references/platform-setup-checklists.md`.
- You need to generate the images — this domain's `advertising_*.md` image prompts.
- You need a quick reference and accept the risk of staleness —
  `skills/marketing/ad-creative/references/platform-specs.md`; use this checklist to
  re-verify it.

## Inputs / Context

1. **Placements**: platform, placement, and ad format, from the media plan.
2. **Assets**: every image, video, and text field planned for each placement (the
   copy matrix's field list and the UGC deliverables).
3. **Category**: whether the product falls in a category platforms treat as
   restricted or sensitive (for the policy rows).
4. **Who fills it and by when**: the person with access to current documentation.

## Method

1. **Enumerate placement × asset.** One block per placement; within it, one row per
   asset or text field that placement accepts.
2. **Attach the spec rows.** For each asset, the attributes that can cause rejection
   or bad rendering: dimensions, aspect ratio, file type, maximum file size, duration
   range, frame rate or bitrate where relevant, text-field character limits, number
   of variants accepted, safe zones, captions, audio. Leave every value blank.
3. **Add source and date columns.** Each value is filled only from the platform's own
   current documentation or ad-manager interface; the filler records the URL or
   screen and the date checked. A value without a source fails the gate.
4. **Add policy-sensitive rows.** Text-in-image, before/after imagery, personal
   attributes, landing-page requirements, and category restrictions — each as a
   question to check in the platform's current policy, not as a rule stated here.
5. **Derive the cut list.** Once filled, group placements that share a spec so the
   minimum set of asset versions is produced.
6. **Write the pre-upload gate.** Binary checks per asset: matches verified spec,
   text inside safe zone, captions burned or supplied, file named per convention,
   policy rows cleared.
7. **Set a re-verify trigger.** Record when the checklist expires (a date, or "next
   campaign"), because specs change.

## Output Format

```
# Placement spec checklist — [campaign]   Filled by: [name]   Expires: [date]

## [Platform — placement — format]
| Asset / field | Attribute | Verified value | Source (URL / screen) | Date checked | ✓ |
|---|---|---|---|---|---|
| [video] | Aspect ratio | [ ] | [ ] | [ ] | [ ] |
| [video] | Duration range | [ ] | [ ] | [ ] | [ ] |
| [headline] | Character limit | [ ] | [ ] | [ ] | [ ] |
| [video] | Safe zone | [ ] | [ ] | [ ] | [ ] |

## Policy checks (verify in the platform's current policy)
| Question | Answer | Source | Date |
|---|---|---|---|

## Cut list (after filling)
| Asset version | Serves placements |
|---|---|

## Pre-upload gate (per asset)
- [ ] Matches every verified value above
- [ ] Text and faces inside the verified safe zone
- [ ] Captions present
- [ ] Policy rows cleared
- [ ] Named per convention
```

## Verification

- [ ] Every placement in the media plan has a block.
- [ ] Every asset and text field in the copy matrix and UGC deliverables has rows.
- [ ] No row contains a value without a source and a date.
- [ ] Policy items are phrased as questions to check, not as rules.
- [ ] An expiry date is set.

## False-Positive Prevention

1. **Never pre-fill from memory.** A plausible number is the failure this prompt
   exists to prevent; even a correct one teaches the team to skip the check.
2. **An old reference table is not a source.** Internal tables — including the
   ad-creative skill's — are starting points to re-verify, not citations.
3. **"Recommended" and "required" differ.** Record which one the documentation
   states; a recommended ratio can still be rejected in another placement.
4. **Policy rows are questions.** "Is before/after imagery permitted for this
   category?" — not "before/after is banned."
5. **One asset rarely fits everything.** The cut list exists because a single
   export stretched across placements is how text ends up under a button.
6. **Specs expire.** A checklist without an expiry is a stale spec table.

## Example

**Input:** Campaign with one social feed image, one vertical short-video placement,
and one search ad; assets from the copy matrix (C1, C3) and one UGC video.

```
# Placement spec checklist — Q4 meal-kit   Filled by: J. Ortiz   Expires: 2026-12-31

## Social — feed — single image
| C1 image | Aspect ratio | [ ] | [ ] | [ ] | [ ] |
| C1 image | Max file size | [ ] | [ ] | [ ] | [ ] |
| C1 headline | Character limit | [ ] | [ ] | [ ] | [ ] |
| C1 primary text | Truncation point | [ ] | [ ] | [ ] | [ ] |

## Social — vertical short video
| UGC video | Duration range | [ ] | [ ] | [ ] | [ ] |
| UGC video | Safe zone (top/bottom) | [ ] | [ ] | [ ] | [ ] |
| UGC video | Captions supported / required | [ ] | [ ] | [ ] | [ ] |

## Search — text ad
| C3 headline | Character limit | [ ] | [ ] | [ ] | [ ] |
| C3 description | Character limit | [ ] | [ ] | [ ] | [ ] |

## Policy checks
| Is "half price" a pricing claim with landing-page requirements? | [ ] | [ ] | [ ] |
| Are star-rating claims permitted in ad text, and with what sourcing? | [ ] | [ ] | [ ] |

## Cut list (after filling)
| [to derive once values are in] | |
```

The star-rating row links back to the copy matrix's C2/C4 flags: the same claim
needs both platform policy clearance here and substantiation in the claims review.

## Techniques Used

- **QA-04 Uncertainty Acknowledgment** — every value starts unknown and says so.
- **QA-05 Citation Requirements** — source and date per filled value.
- **OC-03 Markdown Table Specification** — one fixed table per placement.
- **QA-08 Gate-Based Verification** — the binary pre-upload gate.

## Related Prompts

- `domain-agentic-resources/skills/marketing/ad-creative/references/platform-specs.md` — a reference to re-verify.
- `domain-agentic-resources/skills/marketing/paid-ads/references/platform-setup-checklists.md` — account and tracking setup.
- `adcampaign_copy_variant_matrix.md` — the field list this checklist fills.
