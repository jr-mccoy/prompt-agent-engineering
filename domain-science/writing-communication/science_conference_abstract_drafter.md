---
title: "Conference Abstract Drafter"
category: science/writing-communication
description: "Draft an oral, poster, or lightning-talk conference abstract to the target submission portal's exact structure and word/character limit, with a results line that carries a real finding."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - conference-abstract
  - oral-presentation
  - poster
  - submission-portal
  - word-limit
  - encore-policy
  - keywords
  - calibrated-claims
updated: "2026-06-26"
related_prompts:
  - domain-science/writing-communication/science_poster_designer.md
  - domain-science/writing-communication/science_preprint_release_plan.md
---

# Conference Abstract Drafter

**Objective:** Draft a submission-ready conference abstract that conforms to the specific portal's required structure (structured Background/Methods/Results/Conclusions or unstructured single block) and its word/character limit, tuned to the presentation type (oral, poster, or lightning talk). The draft must report an actual user-supplied finding in its Results line, select category and keywords, and pass an encore/embargo check. Every venue requirement is treated as user-supplied or verify-on-site.

**When to use:** You have a completed or near-complete piece of work, a target conference and submission portal, and need an abstract that fits that portal's structure and limit on the first pass.

**Required inputs:**
- **Discipline.** The field and subfield (steers terminology, reporting conventions, what a reviewer expects in the Results line).
- **Finding / work context.** The user-supplied background, methods, the headline result with its direction and magnitude, and the take-home conclusion. Never invented.
- **Target venue or audience.** Conference name, presentation type (oral / poster / lightning / symposium), and the audience's specialization level.
- **Portal structure and limit.** `[user-supplied]` — structured vs unstructured; required section headers if structured; the word or character cap. Verify on the submission site; do not assume a standard 250-word limit.

**Optional inputs:**
- Required keyword count and any controlled vocabulary/category taxonomy the portal enforces.
- Funding/acknowledgment line rules (some portals count these toward the limit; some exclude them).
- Encore/embargo status: has this work been presented or published elsewhere; is there a press or journal embargo date.
- Confirmatory vs exploratory framing for the work; preregistration status; trial registration number if applicable.
- Data/code availability status.

**Constraints — Must:**
- Open with discipline, finding context, and target venue before drafting.
- Draft to the portal's stated structure exactly: if structured, use the portal's literal section headers; if unstructured, produce one continuous block.
- Keep the draft within the user-supplied limit and report the exact count (words or characters, matching the portal's unit). If the limit is unknown, draft to a stated assumed limit and flag it `[verify on the submission site]`.
- Put a real, user-supplied finding in the Results line, with direction and magnitude where the user provided them.
- Use calibrated language; preserve confirmatory-vs-exploratory honesty (label exploratory findings as exploratory).
- Surface data/code availability and (if applicable) trial/preregistration identifiers when the user supplied them.
- Select keywords/category only from the user-supplied taxonomy when one exists; otherwise propose candidates and mark them for the user to confirm against the portal list.

**Constraints — Must Not:**
- Do not invent results, citations, DOIs, conference requirements, or server policies. Draft only from user-supplied content; mark gaps `[user-supplied]` / "verify on the venue/server site".
- Do not write "results will be discussed" or "data will be presented" unless the user confirms data is genuinely pending — and even then flag this as a weak abstract that many committees down-rank.
- Do not use "novel", "groundbreaking", "first-ever", "unprecedented", or "paradigm-shifting" in drafted text.
- Do not exceed the limit to fit more content; cut instead.
- Do not assert a portal's structure or limit from memory.

**Instructions:**

1. **Confirm the frame.** Restate discipline, finding context, target venue, presentation type, and the portal's structure + limit (or flag them `[user-supplied]` / verify-on-site). State the limit unit (words vs characters).
2. **Extract the four moves.** From the user content, isolate: the gap/question (Background), what was done (Methods), the headline result with direction and magnitude (Results), and the take-home (Conclusions). Flag any of the four that the user did not supply.
3. **Tune to presentation type.** An oral abstract can carry slightly more methods nuance; a poster abstract front-loads the visual/figure-able result; a lightning abstract compresses to one question + one finding + one implication.
4. **Draft the Results line first.** Write the single most important sentence — the actual finding — and check it carries a concrete result, not a placeholder. If the user only has pending data, draft the line honestly and warn it weakens the submission.
5. **Build the rest around it.** Draft Background (1–2 sentences of gap), Methods (design, sample/n, key measure), and Conclusions (implication + one honest limitation or scope boundary), in the portal's structure.
6. **Calibrate and de-hype.** Replace banned hype terms; match claim strength to evidence; label exploratory findings as exploratory; preserve preregistration/confirmatory status.
7. **Fit the limit.** Count words/characters in the portal's unit. If over, cut method detail and qualifiers before cutting the result. Report the exact count vs the cap.
8. **Select keywords/category and run the encore/embargo check.** Propose keywords (from the portal taxonomy if supplied), flag category choices for confirmation, and check whether prior presentation/publication or an embargo affects eligibility.
9. **Produce variants.** Deliver the within-limit draft plus a long variant (if a longer venue is targeted) and a short/lightning variant, each labeled with its count.

**Output format (locked):**

```
## Frame
- Discipline | Venue | Presentation type | Structure (structured/unstructured) | Limit + unit [user-supplied / verify on site]

## Abstract — within limit (count: X / Y [unit])
[Structured headers as required by the portal, OR one unstructured block]
Background: ...
Methods: ...
Results: [carries the actual user-supplied finding]
Conclusions: ...

## Long variant (count: X / Y)
[...]

## Short / lightning variant (count: X / Y)
[...]

## Keywords & category
- Keywords: [...]  (source: portal taxonomy [user-supplied] / proposed — confirm)
- Category: [...]  (confirm against portal list)

## Encore / embargo check
- Prior presentation/publication: [user-supplied] → eligibility note
- Embargo / press hold: [user-supplied] → note

## Open-science surfacing
- Data availability: [user-supplied]
- Code availability: [user-supplied]
- Preregistration / trial registration: [user-supplied]

## Flags & gaps
- [items marked user-supplied or verify-on-site]
```

**Reporting-standard / convention alignment:** Structured-abstract conventions (e.g., Background/Methods/Results/Conclusions); discipline reporting guidelines where they constrain abstracts (e.g., CONSORT for trials, PRISMA for reviews, ARRIVE for animal studies) — named for the user to apply; conference encore and embargo policies (verify on the venue site).

**Verification checklist (before delivering):**
- [ ] Discipline, finding context, and target venue were captured before drafting.
- [ ] Portal structure and limit are stated, with unknowns flagged `[user-supplied]` / verify-on-site.
- [ ] The Results line carries an actual user-supplied finding (not a placeholder), or the placeholder is explicitly flagged as weak.
- [ ] Word/character count is reported against the cap in the correct unit.
- [ ] No banned hype terms appear in drafted text.
- [ ] Confirmatory vs exploratory status is preserved; exploratory findings are labeled.
- [ ] Keywords/category are tied to the portal taxonomy or flagged for confirmation.
- [ ] Encore/embargo check and data/code availability are surfaced.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Placeholder result | "Results will be discussed" reads as polished but signals no finding | Force a real finding in the Results line; flag pending-data abstracts as weak |
| Wrong limit assumed | A clean 250-word abstract that the portal actually caps at 200 chars | Treat the limit as `[user-supplied]`; report count + unit; tell user to verify |
| Hype masquerading as significance | "Novel, first-ever method" feels strong to a writer | Ban hype terms; require claim strength to match evidence |
| Structure mismatch | Unstructured prose submitted to a structured-only portal | Confirm structure before drafting; use the portal's literal headers |
| Exploratory dressed as confirmatory | A post-hoc finding stated as a tested hypothesis | Preserve confirmatory/exploratory labels; require preregistration status |
| Encore violation | Re-submitting previously presented work where the venue forbids it | Run the encore/embargo check; flag prior presentation/publication |
