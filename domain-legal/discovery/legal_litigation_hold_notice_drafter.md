---
title: "Litigation Hold Notice Drafter"
category: legal/discovery
description: "Draft a litigation hold package — trigger memo, custodian-specific hold notices, IT/records suspension instructions, acknowledgment form, and a reminder/release schedule — distinct from the custodian interview (which audits compliance after the hold issues) and the enterprise retention schedule (which governs routine disposition)."
techniques:
  - CM-03
  - RP-02
  - DS-33
  - QA-01
difficulty: intermediate
tags:
  - legal
  - litigation-hold
  - preservation
  - ediscovery
  - got-sued-preserve-documents
  - lawsuit-coming-what-to-keep
  - stop-deleting-emails
updated: "2026-09-24"
related_prompts:
  - domain-legal/discovery/legal_ediscovery_custodian_interview.md
  - domain-legal/privacy-data/legal_records_retention_schedule_design.md
  - domain-legal/client-intake-communications/legal_new_matter_intake_summary.md
---

# Litigation Hold Notice Drafter

**Objective:** Produce a defensible hold package the moment the duty to preserve attaches: a short trigger memo that documents *when and why* the hold issued, notices written for each custodian group in language they will actually follow, a separate technical instruction to IT and records staff that suspends auto-deletion, an acknowledgment form, and a schedule for reminders, scope changes, and eventual release.

> **Scope guard — attorney-facing.** For outside counsel, in-house counsel, or legal-operations staff acting at counsel's direction. It drafts the organization's instructions to its own people; it does not decide whether a claim is meritorious. If the user is an individual trying to preserve their own evidence without counsel, route to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_evidence_preservation_and_digital_organizer.md`.

## When to Use

- A complaint, demand letter, government inquiry, subpoena, or credible threat of suit has arrived and no hold has issued yet.
- An existing hold must be expanded (new claims, new custodians, a new date range, a newly discovered data source).
- A hold must be re-issued because the first notice was generic, unacknowledged, or never reached IT.

**Not this prompt if:**
- You need to interview custodians about where their data lives or whether they complied — use `domain-legal/discovery/legal_ediscovery_custodian_interview.md`.
- You are designing routine retention periods and disposition — use `domain-legal/privacy-data/legal_records_retention_schedule_design.md` (it defines the hold *override*; this prompt issues the hold itself).
- You are responding to a government subpoena or CID as a whole — use `domain-legal/regulatory-compliance/legal_subpoena_or_cid_response_strategy.md`, then return here for the notice.

## Inputs

- **Jurisdiction and forum (required):** Court or anticipated forum and the governing preservation rule (e.g., FRCP 37(e) or a state analog). If unknown, the output marks every rule reference `[VERIFY]`.
- **Trigger event:** What happened, on what date, and who at the organization learned of it.
- **Claims and subject matter:** Plain-language description of the dispute, parties, products, transactions, and relevant time period.
- **Custodian list:** Name, role, department, and why each is relevant; include departed employees whose data may still exist.
- **Data map:** Systems in use (email, chat, collaboration tools, file shares, CRM/ERP, mobile devices, personal devices used for work, voicemail, paper), with any known auto-delete settings.
- **Existing retention regime:** Scheduled deletions, device-refresh cycles, departing-employee wipe procedures.
- **Sensitivities:** Whether the hold must avoid revealing strategy, whether custodians include adverse or potentially adverse individuals, privacy or works-council constraints on collection.

## Method

**Ground rules (apply to every step):** Do not invent rule text, case names, or sanction standards; any authority not supplied appears as `[CITE: proposition]` or `[NEED PIN: source]`. Do not state a preservation deadline, limitation period, or retention period that the user did not supply — use `[VERIFY: …]`. Draft only for the jurisdiction stated.

1. **Fix the trigger.** Write two or three sentences recording the date the organization reasonably anticipated litigation and the facts supporting that date. If the facts suggest an earlier anticipation date than the one the user gave (e.g., an internal escalation email predating the demand), flag it — an earlier trigger widens scope and the attorney should decide.
2. **Define scope by subject, time, and source — not by keyword.** State subject matters in words a non-lawyer recognizes ("anything about the Model X battery recall"), a date range with a start before the first relevant event, and every data source type. Keywords belong in later collection, not in the notice; a keyword-scoped hold invites under-preservation.
3. **Segment custodians.** Group them (e.g., key decision-makers, operational staff, executives/assistants, IT/records, departed-employee data owners). For each group decide what they personally must stop doing and what they must do (e.g., "turn off disappearing messages in the team chat app").
4. **Draft the custodian notices.** One notice per group: what the matter is about (high level, no strategy), what to keep, where it might live, what *not* to do (delete, wipe, move to personal accounts, forward to outside parties, create new commentary), how long the hold lasts ("until you receive written release"), whom to call, and the acknowledgment request. Keep each under one page of body text.
5. **Draft the IT/records instruction separately.** Enumerate each system and the concrete action: suspend auto-delete, preserve mailboxes of departing custodians, pull devices from the refresh cycle, preserve backups if they are the only copy, snapshot collaboration spaces. Require written confirmation per system.
6. **Address privilege and tone.** Mark the notice as privileged if the jurisdiction supports it `[VERIFY: whether hold notices are discoverable in this forum, especially if spoliation is alleged]`, and write it assuming a court may later read it — no characterizations of the merits, no instructions that could read as selective preservation.
7. **Build the acknowledgment and escalation path.** Acknowledgment form with custodian attestations; a rule for non-responders (follow-up at a set interval, then manager escalation).
8. **Schedule reminders, updates, and release.** Periodic reminder cadence, triggers for scope updates (new claims, amended pleadings, new custodians), and a release protocol that checks for overlapping holds in other matters before releasing anything.
9. **Self-check** against the Verification list and revise.

## Output Format

```markdown
# Litigation Hold Package — {Matter} — Issued {date}
**Privileged & Confidential — Attorney-Client Communication / Work Product [VERIFY]**

## 1. Trigger Memo (file only)
- Anticipation date: {date} — basis: {facts}
- Earlier-trigger flags: {none | facts for attorney decision}
- Governing preservation rule: {rule} [VERIFY]

## 2. Scope
| Subject matter (plain language) | Date range | Data sources | Custodian groups |

## 3. Custodian Notices
### 3.1 Notice to {Group A}
{subject line, body ≤ 1 page, do/don't list, contact, acknowledgment request}
### 3.2 Notice to {Group B} ...

## 4. IT / Records Preservation Instruction
| System | Action required | Owner | Confirmation due | Confirmed (Y/N) |

## 5. Acknowledgment Form
## 6. Non-Response Escalation Path
## 7. Reminder, Update, and Release Schedule
| Event | Timing / trigger | Action | Owner |

## 8. Open Items for Attorney Decision
```

## Verification

- [ ] Jurisdiction lock: preservation rule and any privilege claim for the notice are tied to the stated forum, each marked `[VERIFY]` unless supplied.
- [ ] Citation discipline: no case names, sanction standards, or rule text invented; placeholders used.
- [ ] Scope discipline: the package preserves and instructs; it does not assess merits or collect/review data.
- [ ] Trigger date documented with facts; any earlier plausible trigger flagged.
- [ ] Scope is defined by subject, time, and source type — no keyword-only scoping.
- [ ] Every data source in the data map has a named action in the IT instruction, including ephemeral messaging and personal devices used for work.
- [ ] Departed-employee data and scheduled device refreshes addressed.
- [ ] Each notice is readable by its audience in under two minutes and says the hold lasts until written release.
- [ ] Release protocol checks for overlapping holds.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| One generic notice for everyone | Segment by custodian group; the IT instruction is always separate |
| Keyword-scoped hold ("keep emails containing 'battery'") | Scope by subject matter, date range, and source; keywords are for collection |
| Notice argues the merits or signals strategy | High-level matter description only; assume a court will read it |
| Forgetting ephemeral and off-channel data (disappearing messages, texts, personal phones) | Name each channel and the concrete setting to change |
| Treating issuance as the end of the job | Acknowledgment, escalation, reminders, and release are part of the output |
| Releasing a hold without checking other matters | Release step requires an overlapping-hold check |

## Example

**Input sketch:** Jurisdiction: U.S. district court, FRCP applies. Trigger: demand letter received 2026-08-04 from a fictional distributor, Harbor Supply LLC, alleging our client Kestrel Devices breached an exclusivity clause. Custodians: VP Sales, two regional sales managers, CFO's assistant, IT director; one sales manager left in June. Systems: corporate email, a team chat app with 30-day auto-delete, CRM, company phones.

**Output (abridged):**

> **Trigger memo.** Anticipation date: 2026-08-04 (receipt of demand). *Flag:* user notes the VP Sales emailed Legal on 2026-07-18 that "Harbor is threatening to sue" — attorney to decide whether the trigger is 07-18.
>
> **Notice to Sales group (excerpt).** "Kestrel has received a claim from Harbor Supply about our distribution arrangements. Starting now, keep everything — email, chat, CRM notes, texts on your company phone, and paper notes — that relates to Harbor Supply or to distribution in the Pacific Northwest from January 2024 forward. Do not delete, edit, or move these items, and do not use disappearing-message settings. This instruction stays in effect until Legal releases it in writing. Please confirm by signing the attached form within [internal deadline]."
>
> **IT instruction (row).** Team chat app — disable 30-day auto-delete for listed custodians and relevant channels; export and preserve the departed sales manager's account if still recoverable — Owner: IT director — confirmation due: [date].
>
> **Open item:** whether backups are the only remaining copy of the departed manager's mailbox `[VERIFY: backup rotation schedule]`.
