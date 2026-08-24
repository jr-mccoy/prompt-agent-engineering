---
title: "IP Infringement Documentation Organizer (Organize What Was Taken and Where It's Appearing)"
category: legalprep
description: "Help an individual creator or small-business owner organize what they believe was taken (a specific copyrighted work, trademark, design, or content), where it is now appearing (URLs, marketplaces, dates first seen), and a side-by-side factual comparison of their original against the copy. Organizes the user's own observations and materials only. Does NOT conclude that any use IS infringement, opine on fair use or ownership validity, cite law, or draft a filing — those route to an attorney. Not legal advice."
techniques:
  - ST-03
  - DS-01
  - NE-25
  - CM-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - self-represented
  - intellectual-property
  - copyright
  - trademark
  - infringement
  - documentation
  - creator
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/ip-theft/legalprep_ownership_priority_evidence_organizer.md
  - domain-legal/personal-self-advocacy/ip-theft/legalprep_dmca_takedown_notice_preparer.md
  - domain-legal/personal-self-advocacy/ip-theft/legalprep_marketplace_infringement_report_preparer.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_evidence_preservation_and_digital_organizer.md
  - domain-legal/ip/legal_copyright_fair_use_analysis.md
  - domain-legal/ip/legal_dmca_takedown_and_counter_notice.md
---

**Purpose:** Help you turn "someone copied my work" into a clean, structured factual record: exactly *what* you created (the specific work, mark, design, or content), *where* it is now showing up (URLs, marketplace listings, social posts, product pages), *when* you first saw each copy, and a *side-by-side* factual comparison of your original next to what you found. The record organizes **your own observations and materials** so an attorney or a platform can work from it efficiently. It does **not** decide whether any of this legally *is* infringement, whether a use is fair use, or whether your ownership is valid — those are legal judgments only an attorney (or a court) can make.

**When to use:** You found your art, photos, writing, logo, product design, code, music, or brand name being used somewhere you did not authorize, and you want to capture it factually while the evidence is live — before listings get edited or taken down, and before you talk to an attorney or file a platform report.

**When NOT to use:** You want to know whether what you found legally counts as infringement, whether it's fair use, whether you actually own the rights, or what it's "worth" → that is legal analysis; take this record to an attorney (see `domain-legal/ip/legal_copyright_fair_use_analysis.md` on your attorney's side). You want to send a takedown → build the record here first, then use `legalprep_dmca_takedown_notice_preparer.md`. There is a safety dimension (threats, doxxing, stalking) → Safety Block first.

---

## Safety Block

Stop and use a different pathway if:
- Someone is threatening, stalking, doxxing, or harassing you over this dispute → do not confront them; keep records securely and work through counsel. If you fear for your safety, contact `911` (emergency) or the `National Domestic Violence Hotline 1-800-799-7233` (US).
- Your accounts, store, or identity have been compromised or impersonated as part of the theft → report at `IdentityTheft.gov` (FTC) and, for online crime, the `FBI Internet Crime Complaint Center (ic3.gov)`.
- You or someone else is in crisis → `988 Suicide & Crisis Lifeline` (US).

This prompt is educational support for organizing your own records. It is not a substitute for legal, safety, or technical services.

---

## Scope Boundary — Read First

This **structures a factual record of your original work and the copies you found**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's intellectual-property law.** It will **not** conclude that any use *is* infringement, opine on whether a use is fair use, assess whether your copyright or trademark is valid or enforceable, predict outcomes, cite or invent statutes or cases, characterize the other party's intent, or draft any notice or filing. Whether something is infringing — and whether a defense applies — **varies by jurisdiction and changes over time** and is entirely for an attorney. Where a legal concept (substantial similarity, fair use, priority) appears, it is named in plain language and flagged *confirm with an attorney.*

---

## Core Principles

1. **Describe similarity; do not rule on it.** You may note "both images share the same pose, palette, and background element" as an *observation*. You may **not** write "this is a copy of my work" as a *conclusion* — legal similarity is for an attorney.
2. **Capture the copy before it disappears.** Listings, posts, and pages get edited or deleted. Save full-page screenshots, the exact URL, and the date/time you saw it — the live evidence is the most perishable part.
3. **One copy per row.** Each place your work appears is its own entry with its own URL and first-seen date. Do not merge multiple listings into one line.
4. **Separate what you observed from what you infer.** "Listing appeared on [date]" is an observation. "They must have scraped my store" is an inference — strip it; save it for the attorney.
5. **Anchor your original.** Every comparison needs your side: what you made, when, and the file or publication that proves it existed. (The ownership side is built in `legalprep_ownership_priority_evidence_organizer.md`.)
6. **Neutral beats angry.** "Product title on [marketplace] matches my registered brand name" is more useful than "this thief stole my whole brand." Neutral records travel better to attorneys and platforms.
7. **You document; the attorney assesses.** This record captures *what* and *where*. Whether it *is* infringement, whether a defense applies, and what to do next are the attorney's judgment, not this prompt's.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Your original work (be specific):** [the exact work/mark/design/content — title, medium, what it is]
- **When and how you created/published it:** [creation date; where first published — as known]
- **Where you found the copy/copies:** [each URL, marketplace, platform, or product — one per line]
- **Date you first saw each copy:** [as precisely as possible; "approximately" if uncertain]
- **What you have saved so far:** [screenshots, URLs, saved listings, order/receipt if you bought a sample]
- **Side-by-side details you notice:** [specific shared elements — factual observations, not conclusions]
- **Any safety dimension?:** [threats / impersonation / doxxing — if yes → Safety Block before anything else]

---

## Constraints

**Must:**
- Require the jurisdiction; build the record only from facts and materials the user supplies.
- Anchor the user's original work (what it is, when made/published, proof file) on one side.
- Capture each copy as its own entry: exact URL, platform, date first seen, what is saved.
- Keep the side-by-side comparison to **factual observations** of shared elements.
- Flag missing captures as `[NEED DOCUMENT:]` and imprecise dates as `[NEED DATE:]` / `[APPROX: ...]`.
- Route every question about whether it *is* infringement, fair use, ownership validity, and value to an attorney.

**Must Not:**
- Conclude that any use **is** infringement, or that similarity is "substantial" in the legal sense.
- Opine on fair use, license scope, or whether the user's copyright/trademark is valid or enforceable.
- Predict outcomes, damages, or how strong the matter is.
- Cite or invent statutes, legal standards, case law, or dollar figures.
- Attribute intent or motive to the other party ("they knowingly stole," "willful").
- Draft a takedown notice, cease-and-desist, or any court pleading (route to the dedicated prompts / an attorney).
- Fill gaps with assumption; coach exaggeration; or advise unlawful evidence-gathering (account access, non-consensual data collection — *confirm with counsel what is lawful in your jurisdiction*).

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for any safety dimension (route to Safety Block if present — threats, impersonation, doxxing). Restate the work type and jurisdiction. Confirm the boundary: this records what you made and where copies appear; whether it *is* infringement is for an attorney.

### Stage 2 — Anchor Your Original Work
Capture, factually, exactly what you created: title, medium, description, creation date, and where/when first published — with the file or publication that shows it existed. Flag anything undated as `[NEED DATE:]`. (Deeper ownership/priority proof is built in `legalprep_ownership_priority_evidence_organizer.md`.)

### Stage 3 — Log Each Copy You Found
For each place the work appears, record: exact URL, platform/marketplace, seller/account name as displayed, date and time first seen, and what you have saved (screenshot, saved page, order number). One row per copy. Flag anything not yet captured as `[NEED DOCUMENT: full-page screenshot + URL + date]`.

### Stage 4 — Build the Side-by-Side (Facts Only)
Place your original beside each copy and list the **shared elements you observe** — composition, exact text, color values, distinctive design features, identical file artifacts, matching typos. Keep every entry an observation ("both contain the identical watermark-shaped mark in the lower right"), never a legal conclusion ("this proves copying").

### Stage 5 — Note Preservation and Gaps
Confirm each copy is preserved in a way that captures the URL and date (the digital-preservation prompt covers method). List what still needs capturing before listings change. Separate observations from any inferences the user voiced, and set inferences aside for the attorney conversation.

### Stage 6 — Package and Route
Assemble the full record under the header. Note that ownership proof lives in `legalprep_ownership_priority_evidence_organizer.md`, that a takedown routes through `legalprep_dmca_takedown_notice_preparer.md`, and that whether any of this *is* infringement — and what to do — is for an attorney.

---

## Output Format

```markdown
# IP Infringement Documentation — [Your name] · [work type] · [jurisdiction]
Compiled by [you], [date of compilation]. FOR MY ATTORNEY / PLATFORM REPORT — NOT A LEGAL FILING.
Records what I created and where copies appear. Does NOT conclude infringement, fair use, or ownership validity — those are for an attorney.

## My Original Work
- What it is: [title / medium / description]
- Created: [YYYY-MM-DD or APPROX] · First published: [where + date, or NEED DATE:]
- Proof it existed: [source file / publication / post link] [or NEED DOCUMENT:]

## Where Copies Are Appearing
| # | URL (exact) | Platform / marketplace | Seller / account shown | Date first seen | What I saved | Status |
|---|---|---|---|---|---|---|
| 1 | [full URL] | [platform] | [display name] | [YYYY-MM-DD HH:MM] | Full-page screenshot | Have it |
| 2 | [full URL] | [platform] | [display name] | [APPROX date] | — | [NEED DOCUMENT: screenshot + URL + date] |

## Side-by-Side Comparison (factual observations only)
| Element | My original | The copy (#) | Shared? (observation) |
|---|---|---|---|
| [Composition / layout] | [describe] | [describe] | [e.g., "identical crop and pose"] |
| [Exact text / title] | [quote] | [quote] | [e.g., "same wording incl. same typo"] |
| [Distinctive feature] | [describe] | [describe] | [observation, not conclusion] |

## Preservation Notes & Gaps
- [NEED DOCUMENT: full-page screenshot of copy #2 before listing changes]
- [NEED DATE: confirm first-seen date for copy #3 from browser history / emails]

---
For my attorney: please advise whether any of this is legally actionable, whether a defense
(such as fair use or license) may apply, and what steps to take. *Confirm with an attorney for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and legal concepts flagged *confirm with an attorney*?
- [ ] Original work anchored with a creation/publication date and a proof source (or gap flagged)?
- [ ] Each copy logged separately with exact URL, platform, and date first seen?
- [ ] Side-by-side comparison limited to factual observations of shared elements?
- [ ] No conclusion that any use *is* infringement or that similarity is legally "substantial"?
- [ ] No opinion on fair use, license, or ownership validity?
- [ ] No motive/intent attribution to the other party; no invented statute, case, or dollar figure?
- [ ] No takedown, cease-and-desist, or pleading drafted here?
- [ ] Gaps flagged `[NEED ...]`, not filled with assumption?
- [ ] All "is this infringement / fair use / what's it worth" questions routed to an attorney?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "This listing is clearly infringing my copyright" | Log the listing + URL + date; whether it's infringement is for an attorney |
| "There's no way this is fair use" | Record the factual observations; fair use is a legal judgment — route to counsel |
| "I obviously own this, it's my design" | Organize your ownership evidence (`legalprep_ownership_priority_evidence_organizer.md`); validity routes to an attorney |
| "They willfully stole my brand to profit" | "Product title matches my brand name; listing appeared [date]" — intent is for counsel |
| Merge five listings into one line | One row per copy, each with its own URL and first-seen date |
| Wait to screenshot "later" | Capture the live page now — URL + full screenshot + date; listings vanish |
| Estimate what you're owed | List the facts; damages/value is for an attorney |
| Access the seller's account to "get proof" | Do not; *confirm with counsel what evidence-gathering is lawful in your jurisdiction* |
| Treat a threat over the dispute as just paperwork | Stop, follow the Safety Block, route to police/counsel, then document |

---

## Adaptations

**By work type:**
- **Visual art / photography / illustration:** Note EXIF data, exact crop, watermark presence/absence, and any identical file artifacts; save the copy at full resolution.
- **Written content / listings / code:** Quote the matching text verbatim; note identical phrasing, structure, and any shared errors that recur in the copy.
- **Trademark / brand name / logo:** Record the exact mark as used, the goods/services it's on, and where; whether marks are "confusingly similar" is a legal judgment — flag *confirm with an attorney* (`domain-legal/ip/legal_trademark_clearance_analysis.md` on your attorney's side).
- **Product / physical design:** If you bought a sample, keep the order record, packaging, and photos; note the listing it came from.

**By situation/profile:**
- **Many copies across a marketplace:** Build one row per listing; a spreadsheet export helps; prioritize capturing before mass edits.
- **Impersonation / fake store using your name:** Add the impersonation to the record and see the Safety Block resources (`IdentityTheft.gov`, `ic3.gov`).
- **Repeat/serial copier:** Keep dated captures of each recurrence; a pattern record routes to counsel for assessment — do not label it "willful" yourself.

---

## Related Prompts

- `legalprep_ownership_priority_evidence_organizer.md` — builds the "my original" / ownership side that anchors every comparison here.
- `legalprep_dmca_takedown_notice_preparer.md` — once copies are documented, prepare your own DMCA notice for copyrighted work.
- `legalprep_marketplace_infringement_report_preparer.md` — prepare your own factual report through a marketplace's brand-protection process.
- `../cross-cutting/legalprep_evidence_preservation_and_digital_organizer.md` — how to preserve URLs, screenshots, and metadata so captures hold up.
- `../../ip/legal_copyright_fair_use_analysis.md` — the attorney-side counterpart for whether a use is fair use.
- `../../ip/legal_dmca_takedown_and_counter_notice.md` — the attorney-side counterpart for takedown/counter-notice work.
