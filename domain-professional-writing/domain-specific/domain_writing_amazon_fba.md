---
title: "Amazon FBA Seller Listing Copy — Substantiated Claims, Clean Keywords, Bullets That Convert"
category: professional-writing/domain-specific
description: "Write an Amazon product listing (title, five bullets, description, backend search terms) from the seller's spec sheet and evidence: every claim traced to a document, restricted health/antimicrobial/'FDA approved' claims removed or held, keywords placed for accuracy rather than stuffed, and marketplace limits marked for verification. Distinct from scoring a finished description (quality_slop_product_description) and from own-site page copy (copywriting skill)."
techniques:
  - RT-23
  - SV-15
  - DS-32
  - QA-26
difficulty: intermediate
tags:
  - amazon-fba
  - amazon-listing
  - product-listing-copy
  - listing-bullets
  - backend-search-terms
  - claim-substantiation
  - write-my-amazon-listing
updated: "2026-10-06"
related_prompts:
  - domain-professional-writing/content-quality/quality_slop_product_description.md
  - domain-image-generation/ecommerce-product/ecommerce_white_background_product.md
  - domain-agentic-resources/skills/marketing/copywriting/SKILL.md
---

# Amazon FBA Seller Listing Copy

**Objective:** Turn a seller's spec sheet, evidence file, and keyword research into a
publishable Amazon listing in which every claim is backed by a document the seller holds,
no restricted claim slips through, and keywords serve search without degrading the copy.

**When to Use:**
- Launching a new ASIN, or rewriting one whose conversion or return rate is poor.
- The seller's draft (or the supplier's copy) contains claims like "antibacterial",
  "non-toxic", "FDA approved", "#1", or "never breaks" and you need to know which survive.
- You have a keyword list from a research tool and need it placed in title, bullets, and
  backend fields without stuffing.
- Rebranding a private-label product where the supplier's listing cannot be reused.
- **Not this prompt if** the description is already written and you want it scored — use
  `domain-professional-writing/content-quality/quality_slop_product_description.md`, which
  grades a finished draft and returns fixes. For the main image, lifestyle, or variant
  images use `domain-image-generation/ecommerce-product/`. For a product page on your own
  site (no marketplace fields or style guide) use
  `domain-agentic-resources/skills/marketing/copywriting/`.

**Audience:** Two readers. The shopper scanning a mobile search result and the first three
bullets, deciding fit in seconds; and the marketplace's catalogue and compliance review,
which suppresses or removes listings with restricted claims or non-conforming titles.

## Inputs / Context

Paste source material inside named tags and refer to it by tag name:

1. **Product and category** — what it is, the browse category it lists in, variations.
2. **Spec sheet** in `<spec_sheet>` — dimensions, weight, materials, finish, what is in
   the box, care instructions, country of origin if stated.
3. **Evidence file** in `<evidence>` — test reports, certificates (organic, food-contact,
   safety), supplier declarations, warranty terms, review/returns data. A claim with no
   entry here is unsubstantiated.
4. **Target customer** — who buys this and the job they hire it for (keep the stub's
   field; it drives bullet order, not demographic language).
5. **Competitive advantage** — what competing listings emphasize, and the measurable
   difference in yours (thicker, includes X, longer warranty).
6. **Keyword research** in `<keywords>` — terms with search volume, and any the seller
   believes are must-have.
7. **Seller's draft or supplier copy** in `<draft_copy>` (optional) — mined for claims to
   test, not reused.
8. **Category style guide excerpt** in `<style_guide>` (optional) — title pattern,
   character limits, prohibited terms. If absent, every limit is marked `[VERIFY]`.

## Method

1. **Build the claim ledger before writing (RT-23).** Extract every factual or
   comparative claim from `<spec_sheet>`, `<draft_copy>`, and the advantage field. Tag
   each `[doc: <evidence item>]`, `[spec]`, `[seller-belief]`, or `[none]`. Only `[doc]`
   and `[spec]` claims enter the copy as stated.
2. **Sort claims into allowed / restricted / forbidden (SV-15, DS-32).**
   - *Restricted — remove or hold:* disease, health, or medical-effect claims;
     "antibacterial", "antimicrobial", "kills germs" (pesticide-type claims that can require
     product registration); "FDA approved" / "FDA certified"; "organic", "BPA-free",
     "non-toxic", "eco-friendly" without a certificate or test in `<evidence>`.
     Mark each `[VERIFY: Amazon restricted-products and claims policy for <category>]`.
   - *Forbidden in copy:* superlatives and rankings ("#1", "best seller", "best on
     Amazon"), competitor brand names, pricing/promotional language, guarantees the
     warranty terms do not state.
   - *Allowed:* measurable specs, construction facts, included items, care, warranty as
     written.
3. **Rewrite seller beliefs as construction facts.** "Never warps" becomes the
   construction that resists warping plus the care condition; "won't hurt your knives"
   becomes nothing unless tested. Keep the benefit, drop the unprovable absolute.
4. **Place keywords by accuracy, then volume.**
   - Drop terms that describe a different product (a face-grain board is not a "butcher
     block"); a wrong-match keyword buys clicks that become returns.
   - Title: brand, product type, the one or two highest-volume accurate terms, key size
     or count. No repetition, no ALL CAPS, no symbols beyond the style guide's allowance.
   - Bullets: one benefit each, led by a short label, with the spec that proves it.
   - Backend search terms: synonyms and use-cases not already in visible copy; no
     competitor brands, no ASINs, no repeated words
     `[VERIFY: current Amazon category style guide — search-term byte limit and rules]`.
5. **Write in shopper order.** Bullet 1 answers the job the target customer hires the
   product for; bullet 5 carries care and warranty. Description expands use and care in
   plain paragraphs; specs repeat exactly as in `<spec_sheet>`.
6. **Verify before output (QA-26).** Read each sentence and find the first fact that is
   not in `<spec_sheet>` or `<evidence>`; fix or cut it, then continue. Count title and
   bullet characters and report the counts beside the limits — limits themselves come
   from `<style_guide>` or stay `[VERIFY]`.

## Output Format

```
## Claim ledger
| # | Claim (as drafted) | Source tag | Disposition | Copy wording |

## Title  ([n] characters; limit [from style guide or VERIFY])

## Bullets
1. [LABEL] — [benefit] + [proving spec]
2–5. …

## Product description

## Backend search terms  ([n] bytes; limit [from style guide or VERIFY])

## Keywords dropped and why

## Held for seller action
- [claim] — needs [document] / [VERIFY item]
```

## Verification

- [ ] Every claim in title, bullets, and description appears in the ledger as `[doc]` or `[spec]`.
- [ ] No disease, antimicrobial, "FDA approved", organic, or toxicity claim without a document in `<evidence>`.
- [ ] Dimensions, weight, and contents match `<spec_sheet>` character for character.
- [ ] No competitor brand, ASIN, superlative, or promotional phrase anywhere, including backend terms.
- [ ] Every keyword describes this exact product; dropped terms are listed with the reason.
- [ ] Character/byte counts are reported; every limit is sourced or marked `[VERIFY]`.
- [ ] Warranty wording matches the seller's written terms, no stronger.

## False-Positive Prevention

1. **Supplier copy as substantiation.** "Antibacterial bamboo" on the factory's
   Alibaba page is not a test report. A claim the supplier made is still the seller's
   claim once it is live, and the seller carries the suppression or removal.
2. **"FDA approved" for a food-contact item.** Kitchenware is generally not something
   the FDA "approves" as a product `[VERIFY: FDA food-contact framework for the material]`;
   at most the seller can say a material or finish meets a named standard, and only if a
   declaration in `<evidence>` says so. Treat the phrase as a red flag, never a feature.
3. **Keyword stuffing that reads as optimisation.** A title carrying every synonym
   ("cutting board chopping board carving board wood board") scores worse with shoppers
   and can breach title rules; one accurate term per concept is the bar.
4. **Accurate-sounding wrong-match keywords.** "Butcher block", "teak", or "end grain"
   on a face-grain bamboo board pulls the wrong shopper and the return reason will say
   "not as described".
5. **Style-guide numbers from memory.** Title, bullet, and search-term limits differ by
   category and change; a confident "200 characters" in the copy plan is an invented
   fact unless `<style_guide>` supplies it.
6. **Absolute durability promises.** "Never warps", "lifetime" or "unbreakable" outrun
   any warranty or returns data the seller holds; state the construction and the care
   condition instead.
7. **Benefit bullets with no spec.** "Premium quality you can feel" passes a tone check
   and fails a shopper comparing two tabs; every bullet must carry a number or a
   checkable fact.

## Example Output

Scenario: Harbor & Pine, a private-label kitchen brand, lists a large bamboo board.
`<spec_sheet>`: 18 x 12 x 0.75 in; 4.2 lb; 3-ply cross-laminated face-grain bamboo; juice
groove on one face, flat reverse; two recessed side handles; finished with food-grade
mineral oil; hand wash only. `<evidence>`: supplier finish declaration (mineral oil, food
grade); 1-year replacement warranty (seller policy); returns log, 12 months.
`<draft_copy>` from the supplier says "naturally antibacterial", "FDA approved",
"organic bamboo", "never warps", "#1 cutting board". `<style_guide>` not supplied.

```
## Claim ledger
| # | Claim (as drafted)          | Source tag      | Disposition | Copy wording |
| 1 | 18 x 12 x 0.75 in, 4.2 lb   | [spec]          | Keep        | as spec |
| 2 | Naturally antibacterial     | [none]          | Remove      | — (antimicrobial claim; [VERIFY: Amazon claims policy, Kitchen]) |
| 3 | FDA approved                | [none]          | Remove      | "finished with food-grade mineral oil" [doc: finish declaration] |
| 4 | Organic bamboo              | [seller-belief] | Hold        | — until a certificate is in <evidence> |
| 5 | Never warps                 | [seller-belief] | Rewrite     | "3-ply cross-laminated build resists warping when hand-washed and oiled" |
| 6 | #1 cutting board            | [none]          | Remove      | — (ranking claim) |
| 7 | Thicker than typical boards | [seller-belief] | Rewrite     | "0.75 in thick" (state the number, drop the comparison) |
| 8 | 1-year replacement          | [doc: warranty] | Keep        | "1-year replacement warranty" |

## Title  (121 characters; limit [VERIFY: current Amazon category style guide, Kitchen & Dining])
Harbor & Pine Large Bamboo Cutting Board with Juice Groove, 18 x 12 x 0.75 in, Reversible Carving Board with Side Handles

## Bullets
1. ROOM FOR A WHOLE ROAST — 18 x 12 in surface with a juice groove on one face that catches drippings while you carve.
2. REVERSIBLE — flat side for bread, cheese, and chopping; grooved side for meat and juicy fruit.
3. STAYS FLAT — 0.75 in, 3-ply cross-laminated bamboo resists warping when hand-washed and oiled.
4. EASY TO MOVE — recessed handles on both short sides; 4.2 lb, steady on the counter.
5. CARE & WARRANTY — hand wash, dry upright, re-oil monthly with food-grade mineral oil; 1-year replacement warranty.

## Product description
Carve a roast, slice a loaf, and set out cheese on one board. The grooved face holds
drippings; the flat face is for everything else. Cross-laminated bamboo, 0.75 in thick,
arrives finished with food-grade mineral oil. Hand wash only; a dishwasher or soaking
can warp wood. Included: one board. 18 x 12 x 0.75 in, 4.2 lb.

## Backend search terms  (105 bytes; limit [VERIFY: Amazon search-term byte limit])
chopping board kitchen wood carving tray meat brisket turkey serving charcuterie thick reversible handles

## Keywords dropped and why
- "butcher block" — face-grain board, not butcher block; wrong-match returns (FPP 4).
- "[competitor brand] cutting board" — competitor brand names not permitted.
- "antibacterial cutting board" — would reintroduce ledger #2.

## Held for seller action
- Organic (ledger #4): add a certificate covering this SKU, or leave it out.
- Confirm Kitchen title rules and limits against the current category style guide.
- Returns log shows 2 warping complaints in 1,140 units: keep "resists", never "never".
```

## Techniques Used

- **RT-23 Input Provenance Tagging** — the claim ledger tags each claim `[doc]`, `[spec]`, `[seller-belief]`, or `[none]` before any copy is written.
- **SV-15 Allowed vs. Forbidden Distinction** — claims are sorted into allowed, restricted (hold), and forbidden (remove) lists that the copy must respect.
- **DS-32 Regulatory Enumeration Pattern** — restricted claim families (health, antimicrobial, "FDA approved", certifications) are enumerated and each marked for policy verification.
- **QA-26 First-Invented-Fact Test** — the pre-output pass finds the first sentence-level fact not in the spec sheet or evidence and fixes it before continuing.

## Related Prompts

- `domain-professional-writing/content-quality/quality_slop_product_description.md` — score the finished listing for vagueness and fit.
- `domain-image-generation/ecommerce-product/ecommerce_white_background_product.md` — the main image the title and bullets sit beside.
- `domain-agentic-resources/skills/marketing/copywriting/SKILL.md` — product-page copy for your own site, outside marketplace rules.
