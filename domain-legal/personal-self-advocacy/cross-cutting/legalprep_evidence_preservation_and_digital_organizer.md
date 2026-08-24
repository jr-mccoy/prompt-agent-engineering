---
title: "Evidence Preservation & Digital Organizer — Save It Right, Index It Cleanly"
category: legalprep
description: "Help a layperson preserve and inventory digital and physical evidence for a personal legal matter — screenshots with full context and URL and timestamp, emails, voicemails, photos, receipts, letters — with basic chain-of-custody hygiene and a lawful-collection flag. Matter-agnostic. Organizes and preserves the user's own evidence only. Does NOT assess what evidence proves, predict outcomes, cite law, advise surveillance/recording/account access, or draft a filing — those route to an attorney and 'confirm what is lawful with counsel'. Not legal advice."
techniques:
  - DS-01
  - DS-21
  - ST-02
  - CM-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - self-represented
  - evidence
  - preservation
  - digital
  - chain-of-custody
  - documentation
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_incident_documentation_organizer.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_personal_legal_chronology_builder.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_handoff_brief.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md
  - domain-legal/ip/legal_dmca_takedown_and_counter_notice.md
---

**Purpose:** Help you **preserve** the evidence for a personal legal matter before it disappears, and **inventory** it into a clean index an attorney or authority can use. The biggest risks with evidence are that it is lost (a post is deleted, a voicemail auto-expires, a phone dies), that it is captured without enough context (a screenshot with no URL, sender, or timestamp), or that it is gathered in a way that later causes problems. This walks you through capturing each item with its full context, storing it safely with basic chain-of-custody hygiene, and listing it in an evidence index — plus flagging anything whose *collection method* needs a lawyer's sign-off. It organizes and preserves **your own evidence** — it does **not** tell you what the evidence proves, predict outcomes, or decide whether any collection method was lawful.

**When to use:** Something happened and you need to save the proof before it is gone; you have scattered screenshots, emails, photos, and receipts and want one clean index; you are preparing materials for an attorney, HR, a platform, or an agency and want them organized and defensibly stored.

**When NOT to use:** You want to know whether your evidence is admissible, strong, or "enough" → that is legal analysis; take the index to an attorney. You are considering recording someone, installing tracking or monitoring software, or accessing an account that is not yours → **stop**; those raise serious legal risk — *confirm what is lawful with counsel before doing anything.* There is an active safety emergency → Safety Block first.

---

## Safety Block

Stop and use a different pathway if:
- You are in immediate danger, or a crime is in progress → **911** (US emergency).
- There is stalking, threats, harassment, or domestic violence → **National Domestic Violence Hotline 1-800-799-7233** (US). Preserve records to a safe location the other person cannot access; do not confront anyone; work through police and counsel.
- A child is unsafe or being abused → **Childhelp National Child Abuse Hotline 1-800-422-4453** (US); emergencies **911**.
- You or someone else is in crisis → **988 Suicide & Crisis Lifeline** (US).
- The matter is identity theft, fraud, or a scam → **IdentityTheft.gov** / **ReportFraud.ftc.gov** / **ic3.gov** (official reporting channels).

This prompt is educational support for organizing and preserving your own evidence. It is not a substitute for legal, safety, or law-enforcement services, and it does not authorize any collection method.

---

## Scope Boundary — Read First

This **helps you preserve and inventory your own evidence**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's law.** It will **not** assess what any piece of evidence proves, judge whether it is admissible or strong, predict outcomes, state a legal conclusion, cite or invent statutes or rules of evidence, or draft a filing. Critically, it will **not** advise or endorse any surveillance, hidden or non-consensual recording, tracking, or access to an account, device, or space that is not yours — those collection methods **vary by state and country and change over time** and can themselves be unlawful. Any such method is flagged *confirm what is lawful with counsel for your jurisdiction before acting.* Whether your evidence helps you is for an attorney or authority.

---

## Core Principles

1. **Preserve first, organize second.** The urgent task is capturing what could vanish (deletable posts, expiring voicemails, cloud items). Save originals before you annotate or index anything.
2. **Context is part of the evidence.** A screenshot without the URL, account name, full thread, date, and time is far weaker. Capture the surrounding context, not just the words.
3. **Keep the original untouched; work from copies.** Store the original file (with its metadata) unaltered; do your highlighting, cropping, or notes on a copy. Note if any item is a copy of an original held elsewhere.
4. **Basic chain-of-custody hygiene.** For each item, record where it came from, when and how you obtained it, and where it is now stored. A consistent, dated trail makes the evidence more useful.
5. **Lawful collection only — flag anything uncertain.** This tool never advises recording, surveillance, tracking, or account access. If a method is even arguably in that zone, stop and flag *confirm what is lawful with counsel.*
6. **Gaps are flagged, not filled.** Missing or not-yet-obtained items are listed as things to preserve — never invented, altered, or reconstructed.
7. **You preserve and index; the professional assesses.** Whether an item is admissible, authenticated, or persuasive is for an attorney or authority — not for this tool to decide.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Type of matter (your best guess):** [workplace / harassment or stalking / something posted / scam or fraud / consumer / other]
- **What evidence you have or can access:** [screenshots, emails, texts, voicemails, photos, receipts, letters, call logs, documents]
- **Where each item currently lives:** [phone, a specific app, email, cloud, paper]
- **What is at risk of being lost soon:** [deletable posts, expiring voicemails, a device you may lose access to]
- **How you obtained each item:** [received it directly / it was sent to me / I photographed my own property / other]
- **Anything you are unsure is OK to collect:** [recording, monitoring, an account/device that is not yours — flag it]
- **Any safety dimension?:** [if yes → Safety Block before anything else]

---

## Constraints

**Must:**
- Require the jurisdiction; work only from the evidence and facts the user supplies.
- Prioritize preservation of at-risk items (deletable/expiring/loss-prone) first.
- For each item, capture full context (source, URL/account, date/time, and where stored).
- Keep originals unaltered; note when an item is a copy and where the original is.
- Record basic chain-of-custody (how and when obtained, current storage).
- Flag any collection method involving recording, surveillance, tracking, or non-owned accounts/devices as *confirm what is lawful with counsel* — and decline to advise how to do it.
- Flag missing items as `[NEED DOCUMENT:]` / `[NEED TO PRESERVE:]`.

**Must Not:**
- Assess what the evidence proves, whether it is admissible, or how strong it is.
- Predict outcomes or state a legal conclusion.
- Cite or invent statutes, rules of evidence, or recording/consent laws.
- Advise, endorse, or explain how to record, surveil, track, or access an account/device/space that is not the user's.
- Advise altering, editing, staging, or fabricating evidence, or backdating anything.
- Characterize the other party or attribute motive.
- Draft any filing, and do not fill gaps with assumptions.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for any safety dimension (route to Safety Block if present). Restate the matter type and jurisdiction. State the boundary: this preserves and indexes your own evidence; whether it helps, and whether any collection method is lawful, is for an attorney.

### Stage 2 — Triage What Is at Risk
Identify items that could disappear soon (deletable posts, expiring voicemails, a device you may lose, cloud items that could be removed). Mark these "preserve now." For each, note the safest capture: full-context screenshot, export, forward-to-a-safe-email, download of the original file.

### Stage 3 — Capture with Full Context
For each item, list what context must accompany it to be useful: source/URL/account/handle, full thread not just one message, sender and recipient, date and time visible in the capture, and the original file where one exists. Flag any item missing context as `[NEED CONTEXT:]`.

### Stage 4 — Preserve Originals and Work from Copies
Note where the untouched original is stored and confirm any annotation happens on a copy. For digital items, prefer keeping the original file (with metadata) rather than only a screenshot where possible.

### Stage 5 — Record Chain-of-Custody and Flag Lawfulness
For each item, record how and when it was obtained and where it now lives. **Screen every item's collection method:** if it involves recording a conversation, monitoring, tracking a person or device, or an account/device/space that is not the user's, stop, do not explain how, and flag *confirm what is lawful with counsel for your jurisdiction.*

### Stage 6 — Build the Evidence Index and Route Out
Assemble the evidence index table and the preservation checklist under the header. Point the user to `legalprep_incident_documentation_organizer.md` to tie items to specific events and `legalprep_professional_handoff_brief.md` to hand the index to a professional. Route admissibility and strength questions to an attorney.

---

## Output Format

```markdown
# Evidence Index & Preservation Log — [Your name] · [matter] · [jurisdiction]
Prepared by [you], [date]. FOR MY ATTORNEY / THE RELEVANT AUTHORITY — NOT A LEGAL FILING.
Preserves and indexes my own evidence. Does NOT assess what it proves, admissibility, or outcome.
Does NOT advise recording, surveillance, tracking, or accessing accounts/devices not mine.

## Preserve-Now Checklist (at-risk items)
- [ ] [Deletable post] — capture full-context screenshot (URL + account + date/time) AND save original link
- [ ] [Voicemail expiring] — export/record the audio file to safe storage
- [ ] [Device I may lose access to] — back up relevant items to [safe location]
- [ ] [NEED TO PRESERVE: item + why at risk]

## Evidence Index
| # | Item | Source / URL / account | Date & time | How obtained | Original stored at | Copy for markup | Lawful-collection flag |
|---|---|---|---|---|---|---|---|
| 1 | Screenshot of [post/message] | [URL / handle] | [date/time in capture] | Received / public post I viewed | [device/folder] | [copy folder] | OK — I received/viewed it |
| 2 | Voicemail from [number] | [caller number] | [date/time] | Left on my phone | [export file] | [transcript copy] | OK — left for me |
| 3 | Email thread with [party] | [my inbox] | [date range] | Sent to/from me | [.eml export] | [PDF copy] | OK — I am a party |
| 4 | [Recording / monitoring item] | [source] | [date] | [method] | [location] | — | ⚠ CONFIRM WHAT IS LAWFUL WITH COUNSEL |

## Chain-of-Custody Notes
- Originals kept unaltered at [location]; all highlighting/notes done on copies.
- [Item #] obtained on [date] by [how]; moved to [storage] on [date].

## Context Gaps to Fix
- [NEED CONTEXT: URL/account for screenshot #_]
- [NEED DOCUMENT: original file for item #_ rather than a screenshot]

## Items I'm Unsure Are OK to Collect (do not act until cleared)
- [Method] — ⚠ *Confirm what is lawful with counsel for my jurisdiction before doing this.*

---
For my attorney / the authority: please advise on admissibility, authentication, what else to
preserve, and whether any collection method above is lawful. *Confirm with counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and legal concepts flagged *confirm with counsel*?
- [ ] At-risk items triaged and prioritized for preservation first?
- [ ] Each item captured with full context (source/URL/account/date/time)?
- [ ] Originals kept unaltered; markup done on copies; copies noted?
- [ ] Chain-of-custody (how/when obtained, current storage) recorded per item?
- [ ] Every collection method screened; recording/surveillance/tracking/non-owned access flagged *confirm what is lawful*?
- [ ] No instruction on how to record, surveil, track, or access someone else's account/device?
- [ ] No assessment of what the evidence proves, admissibility, or strength?
- [ ] No cited/invented statute or recording/consent law?
- [ ] Gaps flagged `[NEED ...]`, not filled or fabricated; nothing altered or backdated?
- [ ] Admissibility/strength questions routed to an attorney?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "This screenshot proves he harassed you" | Index the item; what it proves is for an attorney |
| "Just record your next call with him" | ⚠ Recording law varies — *confirm what is lawful with counsel*; do not advise the method |
| "Install a tracker / check his phone / log into the account" | Decline; flag *confirm what is lawful with counsel*; never explain how |
| Screenshot with just the words | Capture URL, account, full thread, and date/time |
| Edit or crop the original to "clean it up" | Keep the original unaltered; annotate a copy |
| Backdate or reconstruct a missing timestamp | Flag `[NEED CONTEXT:]`; never fabricate metadata |
| "This evidence is admissible" | Preserve and index; admissibility is for an attorney |
| Treat a safety emergency as an evidence task | Stop, follow the Safety Block, call 911 / report, preserve to safe storage |

---

## Adaptations

**By matter type:**
- **Something posted about you:** Preserve the live URL, the account handle, and a full-context screenshot before it is deleted; for copyright, the attorney-side `../../ip/legal_dmca_takedown_and_counter_notice.md` may apply.
- **Harassment / stalking:** Preserve to storage the other person cannot access; keep message originals with sender info; do **not** record or track — flag *confirm what is lawful with counsel*; Safety Block first.
- **Scam / fraud / identity theft:** Preserve transaction records, emails, and numbers; report to IdentityTheft.gov / ReportFraud.ftc.gov / ic3.gov, which may want the originals.
- **Workplace:** Preserve messages and documents you already have lawful access to; do not download or take material you are not authorized to access — flag *confirm with counsel.*
- **Consumer / housing:** Preserve receipts, contracts, letters, and dated photos of the goods/premises.

**By situation/profile:**
- **Everything is digital:** Prioritize exporting original files (with metadata), not just screenshots; keep a second backup.
- **Device at risk:** Back up to a safe location immediately (Stage 2) before anything else.
- **Safety-sensitive:** Store where the other person has no access; Safety Block first; never a method that requires confrontation or non-consensual collection.

---

## Related Prompts

- `legalprep_incident_documentation_organizer.md` — ties each preserved item to the specific event it supports.
- `legalprep_personal_legal_chronology_builder.md` — dated evidence items anchor rows in the master timeline.
- `legalprep_professional_handoff_brief.md` — the evidence index feeds the handoff package's evidence section.
- `legalprep_professional_authority_router.md` — decide which channel(s) should receive the preserved evidence.
- `../../ip/legal_dmca_takedown_and_counter_notice.md` — attorney-side counterpart for copyright takedowns.
