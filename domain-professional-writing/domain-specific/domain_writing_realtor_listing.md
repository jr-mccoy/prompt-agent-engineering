---
title: "Realtor Listing Remarks — Record-Sourced Facts, Fair-Housing-Clean Language, MLS-Ready"
category: professional-writing/domain-specific
description: "Write MLS public remarks and portal copy for one residential listing: every square-footage, lot, and year-built figure traced to the public record, the property described instead of the buyer, steering phrases swept and replaced, and MLS field rules marked for local verification. Distinct from setting the price (realestate_comparative_market_analysis) and from listing images (advertising_real_estate_property)."
techniques:
  - RT-23
  - SV-15
  - DP-04
  - QA-18
difficulty: intermediate
tags:
  - realtor-listing
  - mls-public-remarks
  - listing-description
  - fair-housing-language
  - real-estate-agent
  - write-a-home-listing
updated: "2026-10-06"
related_prompts:
  - domain-specialized-fields/real-estate/realestate_comparative_market_analysis.md
  - domain-advertising/advertising_real_estate_property.md
  - domain-specialized-fields/real-estate/realestate_inspection_report_triage.md
---

# Realtor Listing Remarks

**Objective:** Produce MLS public remarks (150–200 words) plus portal bullets and agent-only
remarks for one property, with every figure sourced, no fair-housing steering language,
and nothing in the public field that the MLS reserves for elsewhere.

**When to Use:**
- A listing agreement is signed, the list price is set, and the MLS entry needs remarks.
- The seller's or a team member's draft says who the home is "perfect for" and needs a
  fair-housing sweep before it goes live.
- Seller-stated square footage, lot size, or year built disagrees with the county record.
- Refreshing remarks after a price change or a long time on market.
- **Not this prompt if** you are still deciding the list price — use
  `domain-specialized-fields/real-estate/realestate_comparative_market_analysis.md`, whose
  range this copy consumes (the copy states the price; it never argues it). For listing
  photos or ad imagery use `domain-advertising/advertising_real_estate_property.md`.

**Audience:** Buyers and their agents reading portal and MLS remarks to decide whether to
book a showing; the MLS compliance reviewer; and, if a complaint is ever made, a fair-housing
investigator reading the copy literally. The listing agent and supervising broker own the
advertising and its compliance; this prompt drafts it.

## Inputs / Context

Paste source material inside named tags and refer to it by tag name:

1. **Property record** in `<public_record>` — county assessor/tax record: finished square
   footage, lot size, year built, bed/bath count as recorded.
2. **Property details** in `<property_details>` — the stub's field, sharpened: room list,
   updates with year and evidence (permit, invoice), materials, systems, outbuildings.
   Seller-stated figures that differ from the record go here, labelled as such.
3. **Neighborhood** — area name, amenities with measured distances (map tool, not
   impression), the assigned school district per the district's own boundary lookup.
4. **Best features** — what the agent thinks sells it.
5. **Buyer needs served** — the stub's "Target Buyer", restated: which *needs* the property
   meets (single-level living, garden space, workshop), never *who* the buyer is.
6. **List price** — from the CMA or pricing decision. Comparable sales stay out of public
   copy.
7. **Draft copy** in `<draft_remarks>` (optional) — swept, not reused as is.
8. **MLS rules** in `<mls_rules>` (optional) — public-remarks character limit, prohibited
   content (contact details, showing instructions, URLs), required disclaimers. If absent,
   each is marked `[VERIFY: local MLS rules]`.

## Method

1. **Build the fact sheet with a source per figure (RT-23).**
   - Square footage, lot size, year built, beds/baths: use `<public_record>` and cite it
     ("per county records"). Where the seller's figure differs, use the record in copy and
     list the conflict as an open item.
   - Space that may not count as finished (enclosed porch, basement, conversion): describe
     the room, add no footage, and flag permit status for the agent.
   - Updates carry a year only if a permit or invoice supports it.
2. **Describe the property, not the people (SV-15, DP-04).** Must-not list for public copy:
   - Familial status or age: "perfect for a young family", "empty nesters", "kid-friendly",
     "adult community" (unless a qualified housing-for-older-persons designation is in the
     inputs `[VERIFY]`).
   - Religion, national origin, race, ethnicity, or proxies: places of worship as selling
     points, ethnic-enclave descriptors, "exclusive", "private community" used for people.
   - Disability: "walking distance", "perfect for the able-bodied"; give the measured
     distance instead. Accessibility *features* (zero-step entry, 36 in doorways) are
     facts and are allowed when the inputs state them.
   - Neighborhood character and safety: "safe", "quiet", "family neighborhood", crime
     references.
   - School quality: "top-rated", "great schools", rankings. Name the assigned district
     with "buyers to verify".
   - Mark the whole list `[VERIFY: HUD and state fair-housing advertising guidance, and your
     brokerage's word list]`; local guidance may be stricter.
3. **Write the remarks in the stub's order.** Hook (the two or three features that
   differentiate, as nouns), key interior features, outdoor and outbuildings, systems and
   updates with years, neighborhood amenities as distances, price, call to action.
4. **Route content to the right field.** Showing instructions, lockbox, commission,
   occupancy, and seller notes go to agent-only remarks. Contact details and URLs stay out
   of public remarks unless `<mls_rules>` allows them.
5. **Smell-test before output (QA-18).**
   - Swap test: does any sentence describe a person rather than the house? Rewrite it.
   - Number test: every figure appears in the fact sheet with a source.
   - Field test: word count is 150–200; character count reported against the MLS limit
     (from `<mls_rules>` or `[VERIFY]`).

## Output Format

```
## Fact sheet
| Item | Value used in copy | Source | Conflict / note |

## Fair-housing sweep
| Draft phrase | Problem | Replacement |

## Public remarks  ([n] words / [n] characters; MLS limit [..])

## Portal bullets (5–7)

## Agent-only remarks

## Open items for the listing agent
```

## Verification

- [ ] Square footage, lot, and year built match `<public_record>` and are attributed.
- [ ] No sentence describes a buyer, a household type, or a group of people.
- [ ] No school-quality, safety, or neighborhood-character claim; district named with "buyers to verify".
- [ ] Distances are measured numbers, not "walking distance" or "minutes from".
- [ ] Every update year traces to a permit or invoice in `<property_details>`.
- [ ] Public remarks contain no showing instructions, contact details, or comps.
- [ ] 150–200 words; character count reported against a sourced or `[VERIFY]` limit.

## False-Positive Prevention

1. **The "target buyer" field leaking into copy.** The intake asks who the home suits; the
   copy must translate that into features. "Ideal for a growing family" reads warm and is
   the textbook familial-status problem.
2. **Seller square footage that includes the sunroom.** A seller's 2,100 sq ft against a
   recorded 1,860 is usually unpermitted or unheated space; publishing the larger number
   invites a misrepresentation claim when the appraisal comes in.
3. **"Walking distance" as a neutral convenience phrase.** It assumes a buyer's mobility;
   "0.3 miles to the trailhead" carries the same information without the assumption.
4. **School names doubling as quality claims.** "Top-rated Westbrook schools" states a
   ranking the agent did not measure and boundaries change; the assigned district plus
   "buyers to verify" is the defensible form.
5. **Landmarks that signal a group.** A church, temple, or cultural centre named as a
   selling point steers by religion or origin even when it is genuinely nearby; use
   parks, transit, and markets with distances.
6. **Update years from the seller's memory.** "New roof" without an invoice or permit
   becomes a dispute at inspection; "roof replaced 2019" needs the document behind it.
7. **MLS limits and prohibited fields assumed.** Character limits, "primary" versus
   "master" policies, and contact-info rules vary by MLS; stated from memory they are
   guesses `[VERIFY: local MLS]`.

## Example Output

Scenario: 412 Alder Lane, Linden Park. `<public_record>`: 3 bed, 2 bath, 1,860 sq ft
finished, 0.23 acre, built 1962. `<property_details>`: kitchen remodel 2021 (permit on file;
quartz, gas range, peninsula); refinished oak floors; primary bedroom with bath and walk-in
shower; enclosed south-facing sunroom (seller says it makes the home "2,100 sq ft"; permit
status unknown); fenced yard, three raised beds, stone patio; detached one-car garage with a
10 x 12 ft workshop with outlets; roof 2019 (invoice), furnace and central air 2022
(invoice). Neighborhood: greenway trailhead 0.3 mi, Elm Street farmers market 1.1 mi (map
tool); district lookup returns Westbrook School District. List price $449,000 (from CMA).
`<draft_remarks>`: "Perfect starter home for a young family in a safe, quiet neighborhood,
walking distance to St. Anne's and top-rated Westbrook schools! Huge master suite, 2,100 sq ft!"

```
## Fact sheet
| Item          | Value used in copy | Source            | Conflict / note |
| Finished area | 1,860 sq ft        | county record     | Seller: 2,100 incl. sunroom — open item 1 |
| Lot           | 0.23 acre          | county record     | — |
| Year built    | 1962               | county record     | — |
| Kitchen       | remodeled 2021     | permit            | — |
| Roof / HVAC   | 2019 / 2022        | invoices          | — |
| Distances     | 0.3 mi / 1.1 mi    | map tool          | — |
| District      | Westbrook SD       | district lookup   | "buyers to verify" [VERIFY: boundary current] |

## Fair-housing sweep
| Draft phrase                     | Problem                                | Replacement |
| Perfect starter home for a young family | familial status / age          | "three bedrooms, fenced garden yard" |
| safe, quiet neighborhood         | character/safety claim, unmeasured     | deleted; distances to amenities instead |
| walking distance to St. Anne's   | disability assumption + religious landmark | "greenway trailhead is 0.3 miles away" |
| top-rated Westbrook schools      | unmeasured quality claim               | "Assigned to Westbrook School District; buyers to verify" |
| master suite                     | term restricted by some MLSs/brokerages | "primary bedroom" [VERIFY: local MLS] |
| 2,100 sq ft                      | not the recorded figure                | "1,860 square feet per county records" |

## Public remarks  (161 words / 962 characters; MLS limit [VERIFY: local MLS])
A remodeled kitchen, a fenced garden yard and a detached workshop, all on one level. This
1962 ranch sits on a 0.23-acre lot in Linden Park, with three bedrooms, two full baths and
1,860 square feet per county records. The 2021 kitchen has quartz counters, a gas range and
a peninsula. Refinished oak floors run through the living and dining rooms. The primary
bedroom has its own bath with a walk-in shower. Off the kitchen, an enclosed sunroom with
south-facing windows opens to the fully fenced backyard, with three raised garden beds and a
stone patio. The detached one-car garage includes a 10 x 12 ft workshop with its own
electrical outlets. Roof replaced 2019; furnace and central air replaced 2022. The Linden
Park greenway trailhead is 0.3 miles away, and the Elm Street farmers market is 1.1 miles.
Assigned to Westbrook School District; buyers to verify school assignment. Offered at
$449,000. Contact the listing agent to schedule a private showing.

## Portal bullets
- Single-level ranch, 3 bed / 2 bath, 1,860 sq ft (county records), 0.23 acre
- Kitchen remodeled 2021: quartz, gas range, peninsula
- Primary bedroom with private bath and walk-in shower
- Enclosed south-facing sunroom opening to a fenced yard with raised beds and patio
- Detached one-car garage with 10 x 12 ft workshop
- Roof 2019; furnace and central air 2022

## Agent-only remarks
Sunroom permit status unconfirmed; footage excluded from listing. Showings by appointment
[seller's notice window]. Roof and HVAC invoices available on request.

## Open items for the listing agent
1. Sunroom: obtain permit history; whether and how to disclose is a broker and
   state-disclosure-form question [VERIFY: state seller disclosure requirements].
2. Confirm public-remarks limit and the "primary"/"master" policy with the local MLS.
3. Re-run the district lookup the week of listing; boundaries are set by the district.
```

## Techniques Used

- **RT-23 Input Provenance Tagging** — the fact sheet gives every figure a source and records seller/record conflicts instead of resolving them silently.
- **SV-15 Allowed vs. Forbidden Distinction** — property features and accessibility facts are allowed; descriptions of people, safety, and school quality are not.
- **DP-04 Must-Not Constraints** — the steering vocabulary is an explicit must-not list applied to public copy and portal bullets alike.
- **QA-18 Domain-Specific Smell Tests** — the swap, number, and field tests run before output.

## Related Prompts

- `domain-specialized-fields/real-estate/realestate_comparative_market_analysis.md` — sets the list price these remarks state.
- `domain-advertising/advertising_real_estate_property.md` — image prompts for the same listing.
- `domain-specialized-fields/real-estate/realestate_inspection_report_triage.md` — when buyer inspection findings bear on what the remarks claim about systems.
