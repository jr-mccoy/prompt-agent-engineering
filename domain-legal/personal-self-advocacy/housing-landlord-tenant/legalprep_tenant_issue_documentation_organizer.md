---
title: "Tenant Issue Documentation Organizer — Turn a Rental Problem into a Factual Record"
category: legalprep
description: "Help a tenant organize a rental issue — repairs and habitability, landlord entry, deposit, or notices — into a clean, dated, factual record with photos, communications, and the lease provisions at issue described in plain language. For the tenant's own use, legal aid, or an attorney. Does NOT decide whether the landlord violated any law or the lease, predict outcomes, cite landlord-tenant statutes, or draft a filing — those route to legal aid or an attorney. Not legal advice."
techniques:
  - DS-01
  - DS-21
  - ST-03
  - NE-25
  - CM-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - self-represented
  - landlord-tenant
  - housing
  - repairs
  - habitability
  - documentation
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/housing-landlord-tenant/legalprep_landlord_notice_response_preparer.md
  - domain-legal/personal-self-advocacy/housing-landlord-tenant/legalprep_security_deposit_dispute_preparer.md
  - domain-legal/client-intake-communications/legal_demand_letter_drafter.md
  - domain-legal/litigation/legal_complaint_drafter.md
---

**Purpose:** Help you turn a rental problem — a repair the landlord won't make, a habitability concern, an entry without notice, a deposit issue, or a notice you received — into one clean, dated, factual record. It captures what the issue is, when it started and each time it recurred, the photos and other evidence, every communication with your landlord or property manager, and the specific lease provisions involved, described in plain language. This record is reusable: keep it for yourself, bring it to a legal-aid clinic, or hand it to an attorney. It organizes **your own information** — it does **not** tell you whether the landlord broke the lease or the law, predict what a court or agency will do, or claim your records "prove" a habitability violation.

**When to use:** You have an ongoing or one-time issue with your rental and want your facts organized before you write to the landlord, contact a housing agency or legal aid, or talk to a lawyer. Use one copy per distinct issue (repairs, entry, deposit, notice).

**When NOT to use:** You want to know whether the landlord violated the law or the lease, whether you can withhold rent, break the lease, or what your rights are → that is legal analysis; route it to legal aid or an attorney (many areas have free tenant clinics). You need to write back to the landlord → use `legalprep_landlord_notice_response_preparer.md`. Your deposit is being withheld and you want it back → use `legalprep_security_deposit_dispute_preparer.md`. **You have received an eviction or a formal notice with a deadline → Safety Block: contact legal aid immediately; deadlines are strict.**

---

## Safety Block

Act quickly and use the right pathway if:
- **You received an eviction notice, a court summons, a pay-or-quit / cure-or-quit notice, or any notice with a deadline** → contact your **courthouse self-help center / legal aid office** or a **tenant-rights organization immediately**. Eviction and notice deadlines are **strict and short**, and missing one can cost you the case. Do not wait to finish documenting.
- **The unit is unsafe — no heat in freezing weather, no water, gas leak, sewage, fire hazard, exposed wiring, or a condition that threatens health** → contact your local **code-enforcement / housing / health department**; call **911** for immediate danger (gas, fire).
- **There is violence, threats, or a landlord/occupant safety issue** → local police; emergencies **911**; if it involves a household or intimate contact, `National Domestic Violence Hotline 1-800-799-7233`.
- **A child is unsafe in the housing conditions** → `Childhelp National Child Abuse Hotline 1-800-422-4453`.
- **You are in crisis** → `988 Suicide & Crisis Lifeline`.

This prompt is educational support for organizing your own records. It is not a substitute for legal, safety, or housing-agency services.

---

## Scope Boundary — Read First

This **structures a factual tenant-issue record from your own information, photos, and documents**. It is **not legal advice, legal strategy, a legal filing, or a substitute for legal aid, an attorney, or your jurisdiction's landlord-tenant law.** It will **not** decide whether the landlord violated the lease or the law, whether a condition is legally "uninhabitable," or whether you may withhold rent or break the lease; predict what a court or agency will do; assess how strong your position is; cite or invent landlord-tenant statutes, habitability standards, or case law; characterize the landlord's motive; or draft any letter, agency complaint, or court filing. Whether conduct violates the law — and what you may do about it — **varies by state, city, and country and changes over time** and is for legal aid or an attorney. Where a lease term or concept (warranty of habitability, notice period, quiet enjoyment) appears, it is described in plain language and flagged *confirm with legal aid or counsel for your jurisdiction.*

---

## Core Principles

1. **The issue and its timeline are the anchor.** What the problem is, when it started, and each date it recurred or you reported it. A dated history beats "it's been broken forever."
2. **Describe the condition; do not legally label it.** "Kitchen ceiling has an active leak; water pooling since [date]; photographed [date]" — not "the unit is uninhabitable" or "the landlord violated the warranty of habitability." Facts are what legal aid and agencies act on.
3. **Reports and communications are the spine.** Every time you told the landlord — date, channel, what you said, what they said or did — shows what you asked for and how they responded.
4. **Photos and dates carry the weight.** Time-stamped photos and videos of a condition, and dated messages reporting it, anchor the record far more than memory.
5. **Quote the lease; don't interpret it.** Point to the specific lease section by number and quote its words. What it legally requires is for legal aid — you record what it says.
6. **Separate what you observed from what you were told.** "I saw water on the floor" is first-hand; "the neighbor said the pipe's been leaking for months" is second-hand — label both.
7. **You document and prepare; the professional assesses.** You assemble the record; whether it is a legal violation and what remedy applies is for legal aid or an attorney. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/city/country):** [required]
- **Type of issue:** [repair/habitability / landlord entry / deposit / notice received / other]
- **What the issue is:** [in your own words — describe the condition or event factually]
- **When it started and key dates:** [first occurrence, each recurrence, each report — as precise as possible]
- **How and when you reported it:** [date, channel, what you asked, landlord's response]
- **Lease provisions involved:** [section number(s) and the exact words — described, not interpreted]
- **Evidence you have:** [photos/videos with dates, texts/emails, repair requests, receipts, inspection reports]
- **Rent and tenancy basics:** [monthly rent, lease start/end, whether rent is current]
- **Any notice with a deadline, or safety/habitability emergency?:** [if yes → Safety Block before anything else]

---

## Constraints

**Must:**
- Require the jurisdiction; build the record only from facts the user supplies.
- Anchor to the specific issue and a dated timeline of occurrence, recurrence, and reporting.
- Log every landlord/property-manager communication with date, channel, and content.
- Quote the relevant lease section by number and words; describe, do not interpret.
- List photos and evidence with dates and storage locations; flag missing items as `[NEED DOCUMENT:]`.
- Label first-hand observation vs. what others told the user.
- Route all questions about violation, remedies, rent-withholding, and lease-breaking to legal aid or an attorney.

**Must Not:**
- State a legal conclusion ("this violates the warranty of habitability / the lease / the law").
- Decide a condition is legally "uninhabitable" or that the tenant may withhold rent or break the lease.
- Predict what a court or agency will do, or assess how strong the tenant's position is.
- Cite or invent landlord-tenant statutes, habitability standards, or case law.
- Characterize the landlord or attribute motive ("they're retaliating," "they're slumlords").
- Draft a letter, agency complaint, or court filing (route to the appropriate prompt or legal aid).
- Fill factual or date gaps with assumption (flag `[NEED …:]`).
- Coach the user to exaggerate the condition or the landlord's conduct.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for any notice-with-a-deadline or unsafe-condition dimension (route to Safety Block — legal aid immediately if a deadline exists; code enforcement / 911 if the unit is dangerous). Restate the issue type and jurisdiction. Confirm the boundary: this organizes the facts; whether it is a legal violation is for legal aid or an attorney.

### Stage 2 — Anchor the Issue and Build the Timeline
Capture the condition or event and lay a dated timeline: when it started, each recurrence, and each time it was reported. Flag imprecise dates as `[APPROX:]` / `[NEED DATE:]`.

### Stage 3 — Describe the Condition (Facts, Not Labels)
Have the user describe the condition or event observably. Rewrite any legal label ("uninhabitable," "illegal entry," "retaliation") or motive claim into factual description: what is wrong, since when, what is visible.

### Stage 4 — Log Reports and Communications
Lay every contact with the landlord/manager in date order: date, channel, what was asked, what they said or did, and whether any promised repair happened. Flag gaps as `[NEED DATE:]`.

### Stage 5 — Pull the Lease Provisions and Evidence
Quote the specific lease section(s) by number and words, described not interpreted. Index photos, videos, messages, repair requests, receipts, and any inspection report with dates and storage locations; flag missing items as `[NEED DOCUMENT:]`. Label first-hand vs. heard-from-others.

### Stage 6 — Package and Close
Assemble the record under the header. Note it can feed a written request to the landlord, a housing-agency complaint, or a legal-aid/attorney handoff. Route violation, remedy, and rent questions out.

---

## Output Format

```markdown
# Tenant Issue Record — [Your name] · [issue type] · [jurisdiction]
Address: [unit]. Issue first noted: [date]. Compiled by [you], [date].
FOR MY OWN USE / LEGAL AID / MY ATTORNEY — NOT A LEGAL FILING.
Does NOT decide any legal violation, predict outcomes, or state that the law or lease was broken.
Key: (F) = I observed it first-hand. (H) = someone else told me — labeled.

## Issue Summary (facts only)
[What the condition/event is, described observably. No labels like "uninhabitable" or "illegal."]

## Timeline
| Date | What happened (facts only) | Source |
|---|---|---|
| [YYYY-MM-DD] | (F) Leak first appeared in [room]. | Photo [file] |
| [YYYY-MM-DD] | Reported to [landlord] by [channel]. | [message] |

## Reports & Communications with Landlord/Manager
| Date | Channel | What I asked | What they said / did | Repair happened? |
|---|---|---|---|---|
| [YYYY-MM-DD] | [text/email/call/portal] | [fix the leak] | [quote or summary] | [Yes/No/Pending] |

## Lease Provisions Involved (quoted, not interpreted)
- Section [#] ("[exact words from the lease]"). *What this requires legally: for legal aid/counsel.*

## Evidence Index
| Item | Date | What it shows | Storage location | Status |
|---|---|---|---|---|
| Photo of [condition] | [date/EXIF] | [what is visible] | [photos folder] | Have it |
| Repair request | [date] | [what I asked] | [email/portal] | Have it |
| Inspection / code report | [date] | [findings, factual] | [location] | [NEED DOCUMENT:] |

## Rent & Tenancy Basics
- Monthly rent: [$X] · Lease term: [start]–[end] · Rent current? [Yes/No]

## Gaps to Address
- [NEED DATE: date of first report]
- [NEED DOCUMENT: lease copy / inspection report / dated photo]

---
For legal aid or my attorney: please advise whether any of this is a legal violation,
what remedies or deadlines apply, and my options (including any rent question).
*Confirm with legal aid or counsel for your jurisdiction — landlord-tenant law varies by state and city.*
```

---

## Verification

- [ ] Jurisdiction captured and legal concepts flagged *confirm with legal aid/counsel*?
- [ ] Issue anchored with a dated timeline of occurrence, recurrence, and reporting?
- [ ] Condition described observably — no "uninhabitable," "illegal," or other legal labels?
- [ ] Every landlord communication logged with date, channel, and content?
- [ ] Lease provisions quoted by section and words, described not interpreted?
- [ ] Evidence indexed with dates and storage; first-hand vs. heard-from-others labeled?
- [ ] Gaps flagged `[NEED …:]`, not filled?
- [ ] No conclusion that the landlord violated the lease or the law?
- [ ] No advice to withhold rent or break the lease?
- [ ] No characterization of the landlord or motive attribution?
- [ ] Notice-deadline or unsafe-condition dimension screened and routed (legal aid / code enforcement / 911)?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "The landlord violated the warranty of habitability" | "Ceiling leaking since [date]; reported [dates]; not repaired" — the legal question is for legal aid |
| "This is an illegal entry / retaliation" | "Landlord entered on [date] without prior notice per lease §[#]" — no legal label |
| "You can legally withhold rent until it's fixed" | Do not advise rent action; route to legal aid/attorney |
| "Cite the state habitability statute" | Do not cite law; quote the lease and route the legal question |
| "They're slumlords who don't care" | Log the dated reports and responses; no motive |
| Draft the letter or agency complaint here | Organize the record; use `legalprep_landlord_notice_response_preparer.md` or legal aid |
| Fill in a report date you don't remember | Flag `[NEED DATE:]` or `[APPROX:]` |
| Treat an eviction notice as routine documentation | Stop, Safety Block, contact legal aid immediately — deadlines are strict |

---

## Adaptations

**By issue type:**
- **Repairs / habitability:** Center on the condition, dated photos, the reporting history, and the lease repair clause; describe the condition observably, never as "uninhabitable."
- **Landlord entry:** Record each entry date/time, whether notice was given and how far in advance, and quote the lease notice clause — do not label it "illegal."
- **Deposit:** Pair with `legalprep_security_deposit_dispute_preparer.md`; anchor to move-in/out condition and the deposit amount.
- **Notice received (rent increase, cure/quit, non-renewal, eviction):** Safety Block first — record the notice date, type, and stated deadline exactly; route to legal aid immediately.

**By situation/profile:**
- **Ongoing / recurring problem:** Keep every recurrence dated; a clean recurrence log is stronger — but its significance is for legal aid.
- **Multiple issues at once:** Use one record per issue; note they are related so counsel can see the whole picture.
- **Habitability emergency (no heat/water, gas, sewage):** Safety Block — code enforcement / 911 first; document after safety is addressed.
- **Possible retaliation or discrimination concern:** Record the facts and dates only; whether it is legally retaliation/discrimination is entirely for legal aid or an attorney.

---

## Related Prompts

- `legalprep_landlord_notice_response_preparer.md` — to turn this record into your own factual written response or request to the landlord.
- `legalprep_security_deposit_dispute_preparer.md` — for a deposit-specific demand or dispute.
- `../../client-intake-communications/legal_demand_letter_drafter.md` — the attorney-side demand-letter counterpart legal aid or a lawyer may use.
- `../../litigation/legal_complaint_drafter.md` — the attorney-side pleading counterpart if the matter proceeds to court.
