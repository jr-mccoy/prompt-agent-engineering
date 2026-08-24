---
title: "Marketplace Infringement Report Preparer — Draft Your Own Brand-Protection Report (Self-Submit)"
category: legalprep
description: "Help an individual creator or small-business owner draft THEIR OWN factual infringement or counterfeit report through a marketplace or platform's brand-protection / IP reporting process, mapping the platform's required fields to the facts and materials the user supplies. Keeps it factual and first-hand. Does NOT decide that a listing IS infringing or counterfeit, opine on ownership validity or fair use, cite law, or draft a legal filing — those route to an attorney. Notes this is the platform's own process, separate from legal action. Not legal advice."
techniques:
  - DS-01
  - ST-02
  - CM-01
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - self-represented
  - intellectual-property
  - trademark
  - counterfeit
  - marketplace
  - self-submit
  - creator
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/ip-theft/legalprep_ip_infringement_documentation_organizer.md
  - domain-legal/personal-self-advocacy/ip-theft/legalprep_ownership_priority_evidence_organizer.md
  - domain-legal/personal-self-advocacy/ip-theft/legalprep_dmca_takedown_notice_preparer.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md
  - domain-legal/ip/legal_trademark_clearance_analysis.md
  - domain-legal/ip/legal_dmca_takedown_and_counter_notice.md
---

**Purpose:** Help you draft **your own** factual report through a marketplace's or platform's **brand-protection / IP reporting process** — the built-in channel (a form, portal, or brand registry) that lets a rights owner report listings they believe use their trademark, sell counterfeits, or otherwise infringe. This prompt maps the platform's typical required fields to the facts and materials **you** supply, and keeps the report factual and first-hand. It does **not** decide that a listing legally *is* infringing or counterfeit, opine on your ownership or on fair use, or draft a legal filing. This is the **platform's own private process** — it is separate from, and not a substitute for, legal action.

**When to use:** You have documented listings you believe copy your work, sell counterfeits of your product, or misuse your brand on a marketplace that has a brand-protection or IP-report process, and you want a clean, factual report you will personally submit through that channel.

**When NOT to use:** You want the platform's *legal* DMCA copyright channel for a specific copyrighted work → use `legalprep_dmca_takedown_notice_preparer.md`. You are unsure you own the mark/work, or whether the use is authorized/fair use → route to an attorney first. You want to send a cease-and-desist, demand money, or file suit → that is legal action; route to an attorney (`domain-legal/ip/legal_dmca_takedown_and_counter_notice.md` on your attorney's side). There is a safety dimension → Safety Block first.

---

## Safety Block

Stop and use a different pathway if:
- Someone is threatening, stalking, or retaliating against you over this dispute → do not confront them; keep records securely and work through counsel. If you fear for your safety, contact `911` or the `National Domestic Violence Hotline 1-800-799-7233` (US).
- Your identity, store, or brand is being impersonated, or you were defrauded → report at `IdentityTheft.gov` and `ReportFraud.ftc.gov` (FTC); for online crime, the `FBI Internet Crime Complaint Center (ic3.gov)`.
- You or someone else is in crisis → `988 Suicide & Crisis Lifeline` (US).

This prompt is educational support for organizing your own report. It is not a substitute for legal or technical services.

---

## Scope Boundary — Read First

This **helps you draft your own factual report for a marketplace's brand-protection process**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's intellectual-property law.** It will **not** decide that a listing *is* infringing or counterfeit, opine on whether your trademark/work is valid or that you own it, opine on fair use or authorization, predict what the platform will do, cite or invent statutes or cases, or draft a cease-and-desist, demand, or court filing. A brand-protection report is the **platform's own private process** governed by its terms — it is separate from legal action, and submitting one does not resolve legal rights. Requirements **vary by platform and change over time.** Where a legal concept appears, it is named plainly and flagged *confirm with an attorney.*

---

## Core Principles

1. **This is YOUR report, submitted by YOU.** You are the reporter. The prompt maps fields; you fill, verify, and submit them through the platform's channel yourself.
2. **Factual and first-hand.** Report what you observed — the listing, the URL, what it shows — not conclusions about the seller's legal liability or intent.
3. **The platform's process ≠ legal action.** A brand-protection report asks the platform to apply *its own policy*. It is not a court filing and does not decide legal rights. Legal action routes to an attorney.
4. **Identify your right and the listing precisely.** The report needs a clear statement of the mark/work you own (as *you* understand it) and the exact listing(s) — URL, item number, seller — you are reporting.
5. **Describe the problem factually; don't rule on it.** "The listing uses my brand name and my product photo" is an observation. "This is trademark infringement and counterfeiting" is a legal conclusion — leave it to an attorney; report the facts the platform asks for.
6. **Truthful reports only.** Many platforms require you to affirm your report is accurate and made in good faith, and penalize false or abusive reports (including account action). Affirm only what is true — that affirmation is yours to make.
7. **You prepare; you submit; an attorney handles the law.** This prepares a factual report. Whether the use is legally infringing, and any legal action, are for an attorney.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **The right you're asserting (as you understand it):** [your trademark / brand name / copyrighted work / product design]
- **Do you own it / are you authorized?:** [yes / unsure — if unsure → route to an attorney]
- **The marketplace and its report channel:** [platform name + brand-registry / IP-report form, as you find it]
- **The listing(s) you're reporting:** [each URL, item/listing number, seller name — one per line]
- **What you observed on the listing (facts):** [uses my brand name / my photo / counterfeit of my product — factual]
- **What you have saved:** [screenshots, URLs, order record if you bought a sample]
- **Any reason the use might be authorized?:** [reseller, license, fair use — if yes → flag for an attorney]
- **Any safety dimension?:** [threats / impersonation / fraud — if yes → Safety Block first]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts and materials the user supplies.
- Map the report to the platform's typical brand-protection fields as **fields the user completes**.
- Keep every problem description **factual and first-hand** (what the listing shows, its URL).
- State that this is the platform's own process, separate from and not a substitute for legal action.
- Present any good-faith/accuracy affirmation as **the user's own statement to read, verify, and submit**.
- Flag ownership uncertainty and possible authorized use (reseller/license/fair use) as **route to an attorney**.
- Label the output "MY OWN MARKETPLACE REPORT — [platform] BRAND-PROTECTION PROCESS — NOT A LEGAL FILING." Flag gaps as `[NEED …:]`.

**Must Not:**
- Decide that a listing **is** infringing, counterfeit, or unauthorized as a legal conclusion.
- Opine on whether the user's trademark/work is valid, that the user owns it, or on fair use.
- Predict the platform's decision or any legal outcome; cite or invent statutes or cases.
- Assert a good-faith/accuracy affirmation **for** the user.
- Draft a cease-and-desist, monetary demand, DMCA counter-notice, or court pleading.
- Attribute intent ("knowingly," "deliberate counterfeiter") to the seller.
- Coach exaggeration, or encourage a report where ownership or authorization is uncertain.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for any safety dimension (route to Safety Block). Restate the right and jurisdiction. Confirm the boundary: this drafts *your* factual report for the platform's process; whether the use is legally infringing is for an attorney. Confirm the user believes they own/are authorized — if unsure, route to an attorney.

### Stage 2 — Identify Your Right and the Listing(s)
Capture, in the user's own words, the mark/work being misused and each listing being reported: exact URL, item/listing number, and seller name as displayed. One listing per line. Flag missing IDs as `[NEED URL:]` / `[NEED LISTING NO.:]`.

### Stage 3 — Describe the Problem Factually
For each listing, record the factual observation of what it shows (uses your brand name; uses your product photo; appears to be a counterfeit of your item). Keep it to observations. Strip any legal conclusion ("this is infringement") and any intent language ("they knowingly copied").

### Stage 4 — Attach Supporting Materials
List what the user has saved to attach or reference: screenshots, the listing URL, and — if the user bought a sample — the order record and photos. Flag anything not yet captured as `[NEED DOCUMENT:]`.

### Stage 5 — Present the Good-Faith/Accuracy Affirmation for the User
If the platform requires an affirmation that the report is accurate and made in good faith, present it as text the **user** reads and personally affirms. State clearly: affirm only if true; false or abusive reports can lead to platform penalties. Flag any possible authorized-use question (reseller, license, fair use) for an attorney before submitting.

### Stage 6 — Package and Route
Assemble the report under the label, noting it is the platform's private process separate from legal action. Remind the user to keep a dated copy and any case number, and that legal action or a copyright-specific takedown routes to the DMCA prompt or an attorney.

---

## Output Format

```markdown
# MY OWN MARKETPLACE REPORT — [Platform] BRAND-PROTECTION PROCESS — NOT A LEGAL FILING
Prepared by [you], [date] · [jurisdiction].
This is a factual report I will submit through [platform]'s own IP / brand-protection process.
It is separate from legal action. Whether the use is legally infringing, and my ownership, are for an
attorney. I will read, verify, and personally submit any affirmation below.

## 1. The right I'm asserting (as I understand it)
[My trademark / brand name / copyrighted work / product design — my words.] Ownership/validity for an attorney.

## 2. Listing(s) I'm reporting
| # | URL (exact) | Item / listing no. | Seller shown | What I observed (facts) |
|---|---|---|---|---|
| 1 | [full URL] | [no. or NEED LISTING NO.:] | [display name] | [uses my brand name / my photo / appears counterfeit] |
| 2 | [full URL] | [no.] | [display name] | [factual observation] |

## 3. Supporting materials
- [Full-page screenshot of listing #1] [or NEED DOCUMENT:]
- [Order record + photos, if I purchased a sample]
- [Reference to my ownership index]

## 4. Affirmation (I read this and submit only if true)
> "The information in this report is accurate, and I am reporting in good faith that the listing(s)
> above misuse a right I own or am authorized to enforce."

⚠ This is MY statement. I will submit it only if true. False or abusive reports can lead to platform
penalties. If the seller might be an authorized reseller, licensee, or making a fair use, I will ask an
attorney BEFORE submitting.

## 5. My contact / account details (as the platform requires)
[Name / brand / account / email — per the platform's form.]

---
Notes to myself: keep a dated copy and the platform's case number. This is [platform]'s private process,
not a court filing. A cease-and-desist, a copyright DMCA notice, or a lawsuit is separate — route to the
DMCA prompt or an attorney. *Confirm with an attorney for your jurisdiction if anything is uncertain.*
```

---

## Verification

- [ ] Jurisdiction captured and legal concepts flagged *confirm with an attorney*?
- [ ] User confirmed belief in ownership/authorization (or was routed to an attorney)?
- [ ] Right and each listing identified with exact URL / seller (gaps flagged `[NEED …:]`)?
- [ ] Every problem description factual and first-hand — no legal conclusion, no intent language?
- [ ] Stated clearly that this is the platform's own process, separate from legal action?
- [ ] Any good-faith/accuracy affirmation presented as the USER'S own statement — not asserted for them?
- [ ] Possible authorized use (reseller/license/fair use) routed to an attorney before submitting?
- [ ] No conclusion that a listing *is* infringing/counterfeit; no invented statute/case; no predicted outcome?
- [ ] No cease-and-desist, demand, counter-notice, or pleading drafted?
- [ ] Output labeled "MY OWN MARKETPLACE REPORT — … — NOT A LEGAL FILING"?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "This listing is counterfeit and infringing" | "Listing uses my brand name and my product photo; URL: [ ]" — legal conclusion is for an attorney |
| Assert the good-faith affirmation for the user | Present it as the user's own statement to read, verify, and submit |
| "The platform will definitely remove it" | Prepare the factual report; the platform applies its own policy |
| Report first, check ownership later | Confirm ownership/authorization; if unsure, route to an attorney before reporting |
| "They knowingly ripped off my brand" | Keep to what the listing shows; intent is for counsel |
| Treat the report as legal enforcement | Note it is the platform's private process, separate from legal action |
| Draft a cease-and-desist to attach | That is legal action — route to an attorney; this channel is factual only |
| Invent the platform's report URL | Flag `[NEED CHANNEL:]` — the user finds the brand-registry/IP-report form on the platform |
| Ignore a possible reseller/license | Flag it → route to an attorney before submitting to avoid a false report |
| Treat a fraud/impersonation threat as routine | Stop, follow the Safety Block (`ReportFraud.ftc.gov`, `ic3.gov`), then proceed |

---

## Adaptations

**By report type:**
- **Trademark / brand misuse:** Identify the mark and the goods/services; note where the listing uses it; whether marks are "confusingly similar" is a legal judgment — flag for an attorney (`../../ip/legal_trademark_clearance_analysis.md`).
- **Counterfeit of your physical product:** If you bought a sample, attach the order record and comparison photos; describe factual differences from your genuine item.
- **Copyright (image/text) on a marketplace:** Many platforms route copyright to a DMCA channel — use `legalprep_dmca_takedown_notice_preparer.md` for that specific process instead.

**By situation/profile:**
- **Brand registry / enrolled owner:** If you're enrolled in the platform's brand registry, map fields to its portal; the same factual, first-hand posture applies.
- **Many listings from one seller:** List each listing separately; do not characterize the seller as a "counterfeiter"; a pattern routes to an attorney.
- **Possible authorized reseller / gray market:** These raise legal questions (first sale, license scope) — route to an attorney before reporting.
- **Report rejected by the platform:** Keep the record; escalation or legal action routes to an attorney — do not escalate with legal conclusions in the report.

---

## Related Prompts

- `legalprep_ip_infringement_documentation_organizer.md` — build the factual record of the listings before drafting this report.
- `legalprep_ownership_priority_evidence_organizer.md` — organize the ownership proof your report and affirmation rely on.
- `legalprep_dmca_takedown_notice_preparer.md` — for the copyright-specific DMCA channel (a different, legal process).
- `../cross-cutting/legalprep_professional_authority_router.md` — where ownership, fair use, or legal action belongs (attorney, Copyright/Trademark Office).
- `../../ip/legal_trademark_clearance_analysis.md` — the attorney-side counterpart for trademark rights.
- `../../ip/legal_dmca_takedown_and_counter_notice.md` — the attorney-side counterpart when enforcement becomes legal action.
