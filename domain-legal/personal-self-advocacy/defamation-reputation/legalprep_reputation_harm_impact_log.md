---
title: "Reputation Harm Impact Log — A Dated, Sourced Record of Concrete Harms You Attribute to the Statements"
category: legalprep
description: "Help a person build a dated, factual log of the concrete harms they attribute to statements published about them — a lost client, a withdrawn offer, specific messages received, documented losses — each sourced, not speculative. Organizes the user's own records for an attorney to assess. Does NOT value the harm, decide causation legally, conclude anything is defamation, or predict recovery — those route to an attorney. Not legal advice."
techniques:
  - DS-01
  - ST-03
  - NE-25
  - CM-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - self-represented
  - defamation
  - reputation
  - harm-log
  - documentation
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/defamation-reputation/legalprep_defamation_concern_documentation_organizer.md
  - domain-legal/personal-self-advocacy/defamation-reputation/legalprep_content_removal_platform_report.md
  - domain-legal/personal-self-advocacy/defamation-reputation/legalprep_correction_retraction_request_preparer.md
  - domain-legal/ip/legal_defamation_publicity_risk_screen.md
---

**Purpose:** Help you build a dated, factual log of the **concrete harms** you attribute to statements published about you — a client who ended a contract, a job offer withdrawn, specific hostile messages you received, a measurable drop you can document. Each entry names the harm, its date, what you say connects it to the statement, and the record that backs it. The discipline this prompt teaches is **sourced, not speculative** — "Client [initials] cancelled on [date]; here is their email referencing the post" is a record; "I've probably lost thousands in business" is a guess. This organizes **your own records** for your attorney. It does **not** put a dollar value on the harm, decide as a legal matter that the statement caused it, conclude anything "is defamation," or predict what you can recover.

**When to use:** Statements you believe are false were published about you, and real-world consequences have followed that you can document; you want to log them factually and contemporaneously, as they happen, so nothing is lost before you meet an attorney.

**When NOT to use:** You want to know what your losses are "worth," whether the statement legally caused the harm, or what you can recover → that is legal and valuation analysis; route to an attorney. You want to capture the statement itself → use `legalprep_defamation_concern_documentation_organizer.md`. The harm is speculative or you have no record for it → note it as a question for the attorney, but do not log it as fact. There is a safety threat → Safety Block first.

---

## Safety Block

Stop and use a different pathway if:
- The harms include threats, stalking, or targeted harassment aimed at you → National Domestic Violence Hotline 1-800-799-7233 (US); emergencies 911. Preserve the messages securely; do not engage; route to law enforcement and counsel. For an online/criminal dimension, `ic3.gov` (FBI Internet Crime Complaint Center).
- The situation is affecting your safety or mental health → 988 Suicide & Crisis Lifeline (US).
- Someone is using the situation to access your identity, accounts, or finances → `IdentityTheft.gov` (FTC).

This prompt is educational support for organizing your own records. It is not a substitute for legal, safety, or clinical services.

---

## Scope Boundary — Read First

This **organizes a dated, factual log of harms you attribute to the statements, from your own records**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's law.** It will **not** value the harm or estimate damages, decide as a legal matter that the statement **caused** any harm (legal causation is a specific question), conclude that any statement "is defamation," predict what you can recover, or cite or invent statutes or cases. **Whether harm is legally compensable and how it is valued vary by state and country and change over time** — those questions are entirely for your attorney. You log what happened and what you attribute it to; the legal significance is the attorney's. *Confirm with counsel for your jurisdiction.*

---

## Core Principles

1. **Sourced, not speculative.** Every harm entry points to a record — an email, a cancelled invoice, a screenshot of a message, a booking history. "I probably lost work" is not an entry; a cancellation with a reason is.
2. **"Attributed to," not "caused by."** You record what you believe connects a harm to the statement; you do **not** assert legal causation. Use "I attribute this to…" language; legal cause is for counsel.
3. **One harm per dated entry.** Each consequence — a specific cancellation, a specific message, a specific withdrawn opportunity — is its own row with its own date and source.
4. **Separate documented loss from feeling and guess.** Real distress and worry are valid, but the log is for concrete, sourced harms. Note non-quantifiable impacts separately and plainly, without inflating them into figures.
5. **No numbers you cannot source.** Do not total up or estimate "lost business." If a specific contract was lost, record its actual documented value from the contract; do not extrapolate.
6. **Contemporaneous is stronger.** Log harms as they happen, with the record captured at the time. A message screenshotted the day it arrived beats one described from memory months later.
7. **You log; the attorney assesses and values.** You assemble dated, sourced harms and what you attribute them to. Whether they are legally compensable, and what they are worth, is the attorney's judgment — never this log's.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **The statement(s) at issue:** [pointer to your statement record — `legalprep_defamation_concern_documentation_organizer.md`]
- **Concrete harms, each with a date:** [what happened, when — one per item]
- **What connects each harm to the statement:** [the fact you point to — e.g., the client's email named the post]
- **The record that backs each harm:** [email, cancelled invoice, message screenshot, booking log]
- **Specific messages you received:** [who, when, what — as saved]
- **Non-quantifiable impacts (noted separately):** [stress, lost sleep — described plainly, not valued]
- **Any safety dimension (threats, harassment)?:** [if yes → Safety Block before anything else]

---

## Constraints

**Must:**
- Require the jurisdiction; build the log only from harms the user can source.
- Date each harm and tie it to the specific record that backs it.
- Use "attributed to" language; keep the statement-to-harm link as the user's account, not a legal finding.
- Flag any harm the user cannot yet source as `[NEED DOCUMENT:]` or move it to a "to confirm" note.
- Record actual, documented values only (e.g., a lost contract's stated amount); never extrapolate.
- Keep non-quantifiable impacts in a separate, plainly described section — not converted to figures.
- Route valuation, causation, and recovery questions to an attorney.

**Must Not:**
- Value the harm, total losses, or estimate damages / lost business.
- Assert that the statement legally caused any harm (legal causation is for counsel).
- Conclude that any statement "is defamation, libel, or slander."
- Predict what the user can recover, or assess how strong the harm evidence is.
- Cite or invent statutes, legal standards, or case law.
- Characterize or attribute motive to anyone beyond the sourced facts.
- Log speculative, unsourced, or "probable" losses as if they were fact.
- Fill gaps with assumption — flag them instead.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for threats, harassment, or identity misuse among the harms and route to the Safety Block if present. Restate the jurisdiction and the boundary: this logs dated, sourced harms and what the user attributes them to; **valuation, legal causation, and recovery are for an attorney**, and this log concludes nothing is defamation.

### Stage 2 — List Each Harm with Its Date
Work through the harms one at a time. For each: what concretely happened and when. Keep each to a documentable event — a cancellation, a withdrawn offer, a received message, a lost opportunity. Flag imprecise dates as `[NEED DATE:]`.

### Stage 3 — Source Each Harm
For each harm, identify the record that backs it (email, invoice, screenshot, booking log) and where it is stored. If a harm has no record yet, flag `[NEED DOCUMENT:]` and note where the record might be obtained. A harm with no source is a question for the attorney, not a log entry.

### Stage 4 — Record What Connects It (attributed, not proven)
For each harm, record the specific fact the user points to as connecting it to the statement — e.g., "the client's cancellation email referenced the review." Frame it as the user's attribution ("I attribute this to…"), not a proven cause. Do not assert legal causation.

### Stage 5 — Separate Non-Quantifiable Impacts
Capture stress, reputational worry, and other non-measurable effects in a separate, plainly worded section. Do not convert them into figures or inflate them; note them as impacts for the attorney to consider.

### Stage 6 — Package and Close
Assemble the dated log under the handoff header. Note that documented values are actual figures from records, never estimates. Route all valuation, causation, and recovery questions to the attorney.

---

## Output Format

```markdown
# Reputation Harm Impact Log — [Your name] · [jurisdiction]
Compiled by [you], updated [date]. FOR YOUR ATTORNEY — NOT A LEGAL FILING.
Records dated, sourced harms I ATTRIBUTE to the statement(s). Does NOT value the harm,
assert legal causation, conclude anything is defamation, or predict recovery — those are
for the attorney. Statement(s) at issue: see my statement concern record.

## Documented Harms (one per dated entry)
| Date | What happened (factual) | What I attribute it to | Backing record | Storage | Status |
|---|---|---|---|---|---|
| 2026-07-10 | Client [initials] ended our contract. | Their email cited the [platform] post. | Client email dated 2026-07-10 | [mail folder] | Have it |
| 2026-07-12 | Speaking invitation from [org] withdrawn. | Organizer referenced "the article." | [email / message] | [folder] | [NEED DOCUMENT: request written confirmation] |

## Specific Messages I Received
| Date | From (as known) | What it said (verbatim / summary) | Saved copy |
|---|---|---|---|
| 2026-07-11 | [handle / unknown] | "[Quote or brief factual summary]" | [screenshot location] |

## Documented Values (actual figures from records only — not estimates)
- Lost contract [initials]: stated contract amount [$ from the contract document], per [document].
- [Do NOT total or estimate. Each figure comes from a record.]

## Non-Quantifiable Impacts (plainly described, not valued)
- [Stress / sleep disruption / reputational worry — described factually, not converted to a dollar figure.]

## Gaps to Address
- [NEED DOCUMENT: written confirmation of the withdrawn invitation]
- [NEED DATE: exact date the client raised the post]

---
For my attorney: please advise whether any of these harms may be legally relevant or
compensable, how causation and valuation work in [jurisdiction], and next steps.
*Confirm with counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and valuation/causation/recovery routed to an attorney?
- [ ] Each harm dated and tied to a specific backing record; unsourced harms flagged `[NEED DOCUMENT:]`?
- [ ] Statement-to-harm link framed as the user's attribution, not asserted legal causation?
- [ ] No conclusion that any statement "is defamation," and no legal conclusion?
- [ ] No damages estimate, no totaling, no extrapolated "lost business"?
- [ ] Documented values taken only from actual records (e.g., a contract amount)?
- [ ] Non-quantifiable impacts kept separate and not converted to figures?
- [ ] No statute/case citation; no motive attribution beyond sourced facts?
- [ ] No speculative or "probable" loss logged as fact?
- [ ] Output labeled "FOR YOUR ATTORNEY — NOT A LEGAL FILING"?
- [ ] Any safety dimension (threats, harassment, identity misuse) screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "You've lost about $50,000 in business" | Record only documented, sourced amounts; no totals or estimates |
| "The post caused you to lose the client" | "Client cancelled on [date]; their email cited the post — I attribute it to that" |
| "This proves defamation damaged you" | Log the dated, sourced harm; legal significance is for counsel |
| Log "probably lost several clients" | Log only cancellations you can source; flag the rest as questions for the attorney |
| Convert stress into a dollar figure | Describe non-quantifiable impacts plainly, separately |
| Extrapolate a monthly loss from one cancellation | Record the one documented loss; no projection |
| "They did this to destroy my livelihood" | Record the harm and its source; motive is for counsel |
| Assume a record exists for a harm | Flag `[NEED DOCUMENT:]` and note where to obtain it |
| Treat threatening messages as routine log entries | Stop, follow the Safety Block, preserve and route to law enforcement/counsel |

---

## Adaptations

**By harm type:**
- **Lost client / contract:** Anchor to the contract or the cancellation communication; record the actual stated value from the document, not a projection.
- **Withdrawn job / offer / opportunity:** Get the withdrawal in writing if possible; note who and when; flag `[NEED DOCUMENT:]` if only verbal.
- **Hostile messages received:** Save each with its date and sender as known; keep them in a dedicated folder; if threatening → Safety Block.
- **Business / booking decline you can measure:** Record only figures you can pull from actual booking or sales records for specific dates; do not model or estimate a trend.

**By situation/profile:**
- **Self-employed / small business:** Your records (invoices, booking logs, client emails) are the sources — keep them organized by date; resist the urge to estimate aggregate loss.
- **Employee / professional reputation:** Log specific workplace consequences (a rescinded assignment, a documented HR conversation) with their records; keep it factual.
- **Ongoing harm:** Update the log contemporaneously as new harms occur; contemporaneous, dated entries with captured records are strongest.
- **Safety dimension:** Safety Block first; preserve threatening messages securely; route to law enforcement and counsel before responding.

---

## Related Prompts

- `legalprep_defamation_concern_documentation_organizer.md` — the statement record this harm log is tied to.
- `legalprep_content_removal_platform_report.md` — to report the content to the platform under its policies.
- `legalprep_correction_retraction_request_preparer.md` — to ask the publisher directly for a correction or retraction.
- `../../ip/legal_defamation_publicity_risk_screen.md` — the attorney-side screen your lawyer may use to assess the matter and any harm.
