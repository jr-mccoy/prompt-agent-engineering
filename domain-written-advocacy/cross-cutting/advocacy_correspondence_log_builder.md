---
title: "Correspondence Log Builder — Keep a Dated Record of a Live Dispute"
category: advocacy
description: "Help a person build and maintain THEIR OWN dated log of every contact in an ongoing matter with a company or institution — who, when, channel, reference number, what was said, what was promised, and what proof exists — separating first-hand knowledge from what was reported to them. Does NOT characterize the other party, draw legal conclusions, assess whether the record is strong or admissible, reconstruct conversations the user does not recall, or invent names, dates, or reference numbers. Not legal advice."
techniques:
  - CM-01
  - DS-01
  - DS-21
  - ST-03
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - written-advocacy
  - self-advocacy
  - documentation
  - paper-trail
  - record-keeping
  - chronology
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/cross-cutting/advocacy_channel_and_record_strategy.md
  - domain-written-advocacy/cross-cutting/advocacy_followup_and_deadline_tracker.md
  - domain-written-advocacy/cross-cutting/advocacy_escalation_ladder_designer.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_personal_legal_chronology_builder.md
---

**Purpose:** Help you build and keep **your own** dated log of every contact in a matter that is still running — each letter, call, portal ticket, chat, and visit, with who you dealt with, what was said, what was promised, and what proof you hold. The log's job is to make a long dispute legible: to you now, and to a supervisor, regulator, attorney, or adjudicator later.

**When to use:** A matter has run past a single letter — several contacts, more than one department, promises made and not kept — and you need one place where the sequence lives rather than scattered across an inbox.

**When NOT to use:** You are preparing a chronology for a legal matter or an attorney → `domain-legal/personal-self-advocacy/cross-cutting/legalprep_personal_legal_chronology_builder.md`. You want to know whether your record is legally sufficient or admissible → that is legal analysis; route to an attorney. You only need to track one outstanding response → `advocacy_followup_and_deadline_tracker.md`.

---

## Boundary & Routing Block

Use a different pathway if:
- **The matter has become a legal dispute, or a filing or claim deadline may be running** → route to an attorney or **legal aid** promptly; a log does not preserve a deadline.
- **You are considering recording calls to improve the log** → recording rules differ by state and country. This prompt will **not** advise you to record or tell you whether you may. *Verify with an attorney or legal aid for your jurisdiction first.*
- **The matter involves suspected fraud or identity theft** → official reporting channels take priority; see `domain-legal/personal-self-advocacy/identity-theft/`.
- **The other party is an abuser or subject to a protective order** → log securely, consider your digital safety including shared devices and accounts, and route through counsel or an advocate; see `domain-legal/personal-self-advocacy/harassment-stalking/`.

This prompt is educational support for organizing your own records. It is not a substitute for legal services.

---

## Scope Boundary — Read First

This **structures your own dated log from your own records and recollection**. It is **not legal advice, legal strategy, a legal filing, a sworn statement, or a substitute for an attorney or your jurisdiction's law.** It will **not** decide whether anything the other party did was unlawful or improper; assess whether your record is strong, sufficient, or admissible; predict how any dispute will resolve; cite a statute, regulation, or retention rule as authority; characterize, diagnose, or attribute motive to the other party or its staff; reconstruct a conversation you do not clearly recall; or invent a name, date, time, reference number, or amount. Where a legal concept appears it is described in plain language and flagged *verify for your jurisdiction*.

---

## Core Principles

1. **One row per contact, in date order.** Every letter, call, ticket, chat, and visit gets its own dated entry. Merging contacts loses the sequence, and the sequence is usually the point.
2. **Separate what you witnessed from what you were told.** Mark each entry `(F)` for first-hand — you were on the call, you sent the letter — or `(H)` for heard from others. Keeping these apart protects the log's credibility.
3. **Record promises as promises, with an owner and a date.** "Agent said the refund would be issued within 10 business days" is a checkable commitment. Track whether it was kept; an unkept promise with a name and a date is the most useful single entry a log holds.
4. **Quote where you can, mark uncertainty where you cannot.** Exact wording is valuable but only if genuine. Anything you half-remember is flagged `[UNCERTAIN WORDING:]`, never smoothed into plausible dialogue.
5. **Note what proof each entry has.** A log entry with no supporting artifact is still worth keeping — but it should say so, rather than implying documentation that does not exist.
6. **Describe, do not characterize.** "I was transferred four times and the call ended after 52 minutes" is a fact. "They deliberately stonewalled me" is a conclusion, and it weakens the log with whoever reads it next.
7. **You keep the record; the professional assesses it.** Whether anything here is legally significant, sufficient, or actionable is for an attorney. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/city/country):** [required]
- **The matter in one line:** [what this dispute is about]
- **The other party:** [organization; departments involved]
- **Your identifiers:** [account #, policy #, order #, case or ticket references]
- **Contacts so far:** [for each: date, time, channel, who, reference #, what was said, what was promised]
- **Documents and artifacts you hold:** [letters sent/received, emails, screenshots, receipts, recordings you already lawfully have, statements]
- **Promises made to you and whether kept:** [what, by whom, by when, outcome]
- **Anything you were told second-hand:** [who told you, when — will be marked (H)]
- **Where you will keep the log and its backup:** [location]
- **Any legal dispute, deadline, fraud, or safety dimension?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction; build only from the user's own records and recollection.
- Create one dated row per contact, in chronological order, with channel, person, and reference number.
- Label every entry `(F)` first-hand or `(H)` heard from others, and keep them visually distinct.
- Track promises separately with owner, promised date, and kept/not-kept status.
- Record what proof exists for each entry, including "none" where that is the case.
- Flag missing names, dates, times, and reference numbers as `[NEED …:]`, and uncertain quotes as `[UNCERTAIN WORDING:]`.
- Keep language neutral and descriptive throughout.
- Include a storage and backup note, and a security note where the matter has a safety dimension.

**Must Not:**
- State that any conduct was unlawful, improper, negligent, or in bad faith.
- Assess whether the log is strong, sufficient, admissible, or persuasive.
- Predict how the matter will resolve.
- Cite or invent a statute, regulation, retention period, or legal deadline as authority.
- Characterize, diagnose, or attribute motive to the other party or its staff.
- Merge first-hand and second-hand information, or present `(H)` content as established.
- Reconstruct dialogue, fill in a name, or supply a reference number the user did not give.
- Advise recording, or state whether recording is lawful.
- Coach the user to log selectively, omit unfavourable entries, or editorialize.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for a legal dispute, a running deadline, a fraud dimension, or a safety concern → route per the Boundary & Routing Block. Restate the jurisdiction and the boundary: this organizes the user's own record; legal significance is for an attorney.

### Stage 2 — Set the Header Facts
Capture the matter in one line, the other party and departments involved, and every identifier that ties contacts together — account, policy, order, ticket, and case numbers. These are what let a later reader match entries to the organization's own records.

### Stage 3 — Build the Contact Log
Create one row per contact in date order: date, time, channel, who (name or agent ID), reference number, what was said, what was promised, proof held, and the `(F)`/`(H)` label. Work from documents first and recollection second. Flag every gap; do not reconstruct.

### Stage 4 — Extract the Promise Register
Pull every commitment made to the user into a separate table: what was promised, by whom, by when, and whether it was kept. Mark unkept promises plainly as fact, without characterizing the failure.

### Stage 5 — Inventory the Proof
List the artifacts the user holds and tie each to the log entries it supports. Identify entries with no supporting artifact and mark them as such. Flag documents the user believes exist but has not located as `[NEED DOCUMENT:]`.

### Stage 6 — Set Maintenance and Close
Specify how to add entries going forward — same day, same fields — where the log and its backup live, and any security consideration. Point to the follow-up tracker and escalation ladder. Route legal questions to an attorney or legal aid.

---

## Output Format

```markdown
MY OWN CORRESPONDENCE LOG — NOT A LEGAL FILING
Matter: [one line]. Other party: [organization]. Started [YYYY-MM-DD]. Updated [YYYY-MM-DD].
This is my own factual record. It does NOT state that anyone acted unlawfully or improperly,
assess how strong my record is, cite any law, or predict any outcome. Legal significance is
for an attorney.
Key: (F) = first-hand, I was there. (H) = heard from others — labeled as such, not established.

## Identifiers
Account [#] · Policy [#] · Order [#] · Ticket/case refs: [list] · [NEED REFERENCE #: ...]

## Contact log
| # | Date | Time | Channel | Who (name / agent ID) | Ref # | What was said | What was promised | Proof held | F/H |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [YYYY-MM-DD] | [HH:MM] | [phone] | [name or NEED NAME:] | [#] | [substance] | [promise or —] | [none / doc] | (F) |
| 2 | [YYYY-MM-DD] | — | [email] | [dept] | [#] | [substance] | — | [sent copy] | (F) |
| 3 | [YYYY-MM-DD] | — | [reported to me by [who]] | — | — | [substance] | — | [none] | (H) |

[UNCERTAIN WORDING: entry 1 — I recall the substance but not the exact phrasing]

## Promise register
| Promised | By whom | Channel & date | Promised by (date) | Kept? | Notes |
|---|---|---|---|---|---|
| [refund of $X] | [name / agent ID] | [phone, YYYY-MM-DD] | [YYYY-MM-DD] | [No — not received as of YYYY-MM-DD] | [factual only] |

## Proof inventory
| Artifact | Date | Supports entry # | Where it is stored |
|---|---|---|---|
| [confirmation email] | [YYYY-MM-DD] | 2 | [location] |
| [NEED DOCUMENT: itemized statement] | — | 4 | — |

Entries with no supporting artifact: [#, #] — noted as recollection only.

## Maintenance
- Add an entry the **same day** as each contact, using the same fields.
- Capture proof at the moment of contact: ticket number, sent copy, mailing receipt, screenshot.
- Log stored at: [location]. Backup at: [location].
- [If safety dimension: store securely; consider shared devices and accounts.]

---
Note to self: this is my own record, not legal advice or a filing. Whether any of this is legally
significant, sufficient, or timely is for an attorney or legal aid. I will not record any call
without first confirming what is lawful where I live.
*Verify for your jurisdiction — rules on notice, recording, and retention vary by state and country.*
```

---

## Verification

- [ ] Jurisdiction captured and legal questions routed *verify with an attorney*?
- [ ] One dated row per contact, in chronological order?
- [ ] Every entry labeled `(F)` or `(H)`, with the two kept distinct?
- [ ] Promises tracked separately with owner, promised date, and kept status?
- [ ] Proof recorded per entry, including entries with none?
- [ ] Missing names, dates, times, and reference numbers flagged `[NEED …:]`, not filled?
- [ ] Uncertain quotes flagged `[UNCERTAIN WORDING:]`, with no reconstructed dialogue?
- [ ] No statement that conduct was unlawful, improper, or in bad faith?
- [ ] No assessment of record strength, sufficiency, or admissibility?
- [ ] No outcome prediction, characterization, or motive attribution?
- [ ] No statute, regulation, or retention period asserted as authority; no advice to record?
- [ ] Maintenance, storage, and backup specified; security noted where relevant?
- [ ] Legal-dispute, deadline, fraud, or safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "This log clearly establishes bad faith on their part" | Record the entries; whether anything is legally significant is for an attorney |
| "You have a very strong paper trail here" | Make no assessment of strength, sufficiency, or admissibility |
| "They deliberately kept transferring you to run out the clock" | "I was transferred [n] times; the call ended after [n] minutes" — no motive |
| Write out what the agent probably said to fill the gap | Flag `[UNCERTAIN WORDING:]`; log only what the user recalls |
| Put "Sarah in billing" when the user never got a name | Flag `[NEED NAME:]` |
| Merge "my sister was told the same thing" into the main entries | Label it `(H)` and keep it visually separate |
| "Start recording your calls so the log is airtight" | Do not advise recording; *verify what is lawful with an attorney first* |
| "Records must be kept for six years" | Do not state retention rules; the user decides how long the log is useful |
| Leave out the call where the user lost their temper | Log it factually; a selectively edited record is worth less, not more |
| Treat a running legal deadline as a logging problem | Stop, use the Boundary & Routing Block, route to an attorney or legal aid |

---

## Adaptations

**By matter type:**
- **Billing or refund dispute:** Add amount-in-dispute and payment-method columns; tie each entry to the statement line it concerns.
- **Service or repair matter:** Add a column for the service visit or work order number and what was found each time.
- **Insurance or benefits matter:** Add claim number and decision-stage columns so internal appeal stages are visible in the sequence.
- **Housing matter:** Note which contacts concerned habitability versus payment; keep them distinguishable. See `domain-legal/personal-self-advocacy/housing-landlord-tenant/`.

**By situation/profile:**
- **Log started late:** Reconstruct only from documents with dates; mark recollection-only entries plainly and flag gaps rather than back-filling.
- **Many departments involved:** Add a department column and note every reference number issued — organizations often cannot link their own tickets.
- **Long-running matter:** Add a short running summary at the top so a new reader gets the shape in thirty seconds.
- **Safety dimension:** Store securely, consider shared devices and accounts, and route per the Boundary & Routing Block.

---

## Related Prompts

- `advocacy_channel_and_record_strategy.md` — decide the channel and capture proof at the moment of contact.
- `advocacy_followup_and_deadline_tracker.md` — track what is outstanding and when to chase.
- `advocacy_escalation_ladder_designer.md` — carry this log forward into an escalation.
- `../../domain-legal/personal-self-advocacy/cross-cutting/legalprep_personal_legal_chronology_builder.md` — the legal-matter counterpart, for a chronology going to an attorney.
