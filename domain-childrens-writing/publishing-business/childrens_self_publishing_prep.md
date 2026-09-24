---
title: "Self-Publishing Prep for Children's Books"
category: childrens-writing
description: "Plan the self-publishing path for a children's book: format specs by book type (trim, page count, bleed) confirmed against the chosen printer, ISBN and copyright basics, a print-file handoff checklist for the designer, and honest expectation-setting with no invented sales figures; distinct from the traditional-path synopsis/submission package and from the illustrator-collaboration prompt's production-norms overview."
techniques:
  - ST-02
  - QA-26
  - DD-05
  - NE-20
  - QA-04
difficulty: intermediate
tags:
  - childrens-writing
  - self-publishing
  - print-on-demand
  - publishing
  - kidlit
  - how-to-self-publish-my-kids-book
  - print-ready-files
updated: "2026-09-24"
related_prompts:
  - domain-childrens-writing/publishing-business/childrens_synopsis_submission_package.md
  - domain-childrens-writing/representation-collaboration/childrens_illustrator_collaboration.md
  - domain-image-generation/publishing-covers/cover_fiction_book.md
---

# Self-Publishing Prep for Children's Books

## When to Use

- You have decided (or are deciding) to self-publish a picture book, early reader, chapter book, or middle-grade novel and need a production plan.
- You need to know which format decisions come *before* illustration begins, such as trim size and page count, because changing them later means redrawing art.
- You are about to hand files to a designer or upload to a print-on-demand (POD) service and want a checklist so the proof does not come back wrong.
- You want a realistic view of what self-publishing a children's book involves, without hype or invented numbers.

**Not this prompt if:**
- You are querying agents or publishers. Use `domain-childrens-writing/publishing-business/childrens_synopsis_submission_package.md` and `domain-childrens-writing/publishing-business/childrens_query_letter_kidlit.md`.
- You need art-note discipline or help with the working relationship with an illustrator. Use `domain-childrens-writing/representation-collaboration/childrens_illustrator_collaboration.md`.
- You need a cover or interior *image* generated. Use `domain-image-generation/publishing-covers/cover_fiction_book.md` or `domain-image-generation/coloring-book/coloring_book_kdp_interior.md`.
- You need retailer descriptions, jacket copy, or launch marketing → `childrens_book_marketing_copy.md`. It covers getting a correct, legally tidy book file into print.

## Inputs

- **Book type and age band** (board book, picture book, early reader, chapter book, MG, upper-MG) and word count.
- **Illustration status:** none / spot art / full-color spreads; illustrator hired or not yet.
- **Formats wanted:** paperback, hardcover, ebook (reflowable or fixed-layout), and whether audio is planned later.
- **Printer/distributor candidates** the author is considering (e.g., a POD service, an offset printer, or undecided).
- **Author's country**, because ISBN agencies and copyright registration are national.
- **Budget and timeline** as the author states them. Do not estimate costs for them.

## Method

1. **Choose the path shape before any specs.** Lay out the options (POD only; POD plus wider distribution; short offset print run; ebook only) against the author's goals: gifting and local sales, online retail, bookstores and libraries, or school visits. List what each option makes easy and hard. Do **not** attach prices, royalty rates, or discounts. Write each as `[VERIFY: current terms on the service's own pricing page]`.
2. **Lock format decisions that constrain the art.** For the chosen printer, fill a spec sheet from *their current published specs*. Do not use memory:
   - Trim size: `[VERIFY: printer's supported trim list]`. Note that landscape vs. portrait trims change the whole spread composition.
   - Page count: picture books are conventionally planned around 32 pages (see README). Confirm the printer's minimum page count and required page-count multiple `[VERIFY]`.
   - Bleed, safe margin, and gutter allowance: `[VERIFY: printer's file-prep guide]`. Explain *why* each matters (art to the page edge; text kept away from trim and spine).
   - Color: full-color vs. black-and-white interior, and paper options `[VERIFY]`.
   - Binding: paperback vs. hardcover (case laminate, dust jacket). For board books and novelty formats, first confirm whether the service offers them at all `[VERIFY]`.
3. **Flag young-child product-safety questions.** Board books, bath books, and books with attachments aimed at very young children can raise children's-product safety and testing questions that ordinary paper books may not. Name the question. Do not answer it with a rule: `[VERIFY: applicable children's-product rules in your sales countries, with the printer]`.
4. **Plan identifiers and metadata.**
   - ISBN: one per format (paperback, hardcover, and ebook are separate editions). ISBNs come from the author's national ISBN agency `[VERIFY: agency and cost for your country]`. Explain the trade-off between a free printer-assigned ISBN (if offered) and an author-owned one: who is listed as publisher, and portability to other printers `[VERIFY terms]`.
   - Imprint name: optional; check it does not collide with an existing publisher's name.
   - Subject/age metadata: juvenile categories and an age range that matches the README band. Never pick a band just to widen the audience.
   - AI-use disclosure: some platforms ask whether text or art was AI-generated `[VERIFY: platform's current policy]`.
5. **Copyright basics, stated carefully.** Copyright generally arises when the work is created; registration is a separate, optional step in some countries that can matter if you ever need to enforce `[VERIFY: your country's registration process and fees]`. The illustrator's contract must say who owns or licenses the art and for which formats, including audio, ebook, and merchandise. This is not legal advice; route contract questions to a qualified professional.
6. **Build the print-file handoff checklist** for the designer: final proofread text locked, art delivered at the printer's required resolution and color mode `[VERIFY]`, fonts licensed for print/ebook embedding, copyright page contents, barcode placement, spine width calculated from the printer's calculator for the final page count and paper `[VERIFY]`, and one physical proof ordered and read aloud before approval.
7. **Set honest expectations.** State plainly that uploading a book does not bring readers to it. Discovery, reviews, and library or school purchasing all take separate effort. Do not quote typical sales, conversion, or income figures. If the author asks "how many will I sell?", say that no reliable figure can be given for their book, and list what they can measure after launch instead.
8. **Produce the decision log.** Every choice (printer, trim, ISBN source, formats) goes into a dated table with its reason and what would have to change to reverse it.

## Output Format

```markdown
## Path Recommendation
| Option | Suits goals… | Makes hard… | Terms to verify |

## Format Spec Sheet (for [printer], confirm every row on their site)
| Spec | Value | Source / [VERIFY] | Constrains the art? (Y/N) |

## Safety & Rights Flags
- [Product-safety question, if any] [VERIFY]
- [Art/licensing ownership questions for the illustrator contract]

## Identifiers & Metadata Plan
| Format | ISBN source | Publisher of record | Age band | Notes |

## Copyright Basics (not legal advice)

## Designer Handoff Checklist
- [ ] ...

## Honest Expectations
[Plain statements; no figures]

## Decision Log
| Date | Decision | Reason | Reversal cost |

## Verify List (anti-fabrication)
- [ ] ...
```

## Verification

- [ ] No price, royalty, discount, ISBN fee, registration fee, or sales figure appears without `[VERIFY]`.
- [ ] Every spec-sheet row names its source or carries `[VERIFY]`; none is stated as universal.
- [ ] Specs that constrain the art (trim, page count, bleed, orientation) are flagged for settling *before* illustration begins.
- [ ] One ISBN per format is explained; the free-vs-owned trade-off is framed as terms to check.
- [ ] Board/novelty/very-young formats trigger the product-safety flag.
- [ ] The copyright section says it is not legal advice and covers art ownership across formats.
- [ ] The age band in the metadata matches the README band for the book type.

## False-Positive Prevention

- **Reciting printer specs from memory.** Trim lists, bleed sizes, page minimums, and spine formulas change and differ by printer. Every figure is `[VERIFY]` against the printer's current guide, even when the model "knows" a common value.
- **Invented economics.** Do not produce royalty math, "typical" sales, or break-even claims. The author supplies real quotes; the prompt structures them.
- **Legal certainty.** ISBN, copyright, and product-safety rules are national and change. Name the question and the authority to ask; never give a jurisdiction-specific rule as fact.
- **Treating self-pub as submission prep.** Do not add query letters, comps, or agent language. This path has no gatekeeper, which is why the checklist has to be thorough.
- **Stretching the age band for reach.** Labelling a picture book "ages 2–10" hurts discovery and misleads buyers. Keep to the README band.

## Example

**Input sketch:** Fictional author Rosalind Pereira-Hart (UK) has a 480-word picture book about a hedgehog who is afraid of puddles. The illustrator is hired but has not started. She wants a paperback and a hardcover and hopes to sell at local markets and online.

**Abbreviated output:**

> **Path:** POD paperback + hardcover suits online availability and small-batch market stock. It makes bookstore consignment harder (returns/discount terms `[VERIFY]`).
>
> **Spec sheet:** Trim: square vs. landscape `[VERIFY printer list]`. *Constrains art: Y. Decide before the illustrator's first sketch.* Pages: 32 planned (README convention); printer minimum and multiple `[VERIFY]`. Bleed/safe zone `[VERIFY file-prep guide]`.
>
> **Identifiers:** Two ISBNs (paperback, hardcover) from the UK national ISBN agency `[VERIFY agency + cost]`, or printer-assigned `[VERIFY: who is listed as publisher]`.
>
> **Rights flag:** The illustrator contract must state whether ebook and any future audio or merchandise use of the art is licensed.
>
> **Honest expectations:** Listing the book online does not make it visible. Plan market-stall read-alouds as the main sales channel. No sales forecast is possible.
