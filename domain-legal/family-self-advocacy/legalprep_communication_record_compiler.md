---
title: "Communication Record Compiler (Texts, Emails, Co-Parenting App)"
category: legalprep
description: "Help a self-represented or self-organizing family-law litigant compile message threads (texts, emails, co-parenting-app messages) into a clean, dated, chronological litigation-prep record — verbatim quotes, sender, date/time, and source, with the user's own commentary stripped out and context or screenshot gaps flagged. Organizes the user's own communications only. This is a litigation-prep compilation, not an ongoing logging tool. Not legal advice."
techniques:
  - DS-01
  - ST-03
  - NE-25
  - CM-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - family-law
  - self-represented
  - divorce
  - custody
  - communications
  - messages
  - documentation
  - litigation-prep
updated: "2026-06-05"
related_prompts:
  - domain-legal/family-self-advocacy/legalprep_attorney_handoff_brief.md
  - domain-legal/family-self-advocacy/legalprep_evidence_inventory_organizer.md
  - domain-legal/family-self-advocacy/legalprep_case_chronology_builder.md
  - domain-legal/family-self-advocacy/legalprep_witness_and_source_map.md
  - domain-parenting/caregiver-facing/custody/parenting_custody_communication_log_template.md
---

**Purpose:** Help you compile message threads — texts, emails, co-parenting-app messages — into one clean, dated, chronological record that your attorney can use in litigation preparation. Each row shows the date and time, the sender, the verbatim message content, and the screenshot or export source. Your own commentary, emotional reactions, and interpretations are stripped out so what remains is an accurate factual record. Where a screenshot is missing, the thread is cut, or context is unclear, the gap is flagged rather than filled. This organizes **your own communications** — it does **not** assess what the messages "prove," advise on strategy, or tell you how to respond to the other party.

**When to use this prompt (not the parenting log):** You have an existing body of messages that is already relevant to your case and you need to compile them into a court-ready exhibit for your attorney. This is a **one-time litigation-prep compilation** of messages you already have — organizing a historical record into a clean, sourced document. Use this prompt when you are building an exhibit package, approaching a hearing, or providing materials to counsel.

**When NOT to use this prompt — use `parenting_custody_communication_log_template.md` instead:** You want to log new co-parenting communications going forward on a regular basis. The parenting communication log is an **ongoing tool** designed for day-to-day use. The difference matters: ongoing logging is a habit; this compilation is a one-time exhibit-preparation step. Do not use this prompt as a substitute for maintaining that ongoing record.

**When NOT to use at all:** You want to know what the messages "prove" or how a court will interpret them → that is legal analysis; ask your attorney. You want to draft a response to the other party → do not use any tool in this set for that purpose. There is an active safety emergency → Safety Block first.

---

## Safety Block

Stop and use a different pathway if:
- There is domestic violence, threats, stalking, or a protective/restraining order → National Domestic Violence Hotline 1-800-799-7233 (US). Keep records securely; work through counsel/advocate; do not confront anyone.
- A child is being abused or is unsafe in either home → Childhelp National Child Abuse Hotline 1-800-422-4453 (US); emergencies 911. Report and route to your attorney immediately.
- You or a child is in crisis → 988 Suicide & Crisis Lifeline (US).

This prompt is educational support for organizing your own records. It is not a substitute for legal, safety, or clinical services.

---

## Scope Boundary — Read First

This **compiles a communications record from your own messages**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's family law.** It will **not** assess what messages "prove," advise on litigation strategy, predict how a court will weigh the record, cite or invent evidentiary rules or cases, draft any filing, or tell you how to respond to the other party. Whether messages are admissible, whether they need authentication, and how to use them strategically **vary by state and country and change over time** and are entirely for your attorney. Where a legal concept appears, it is explained in plain language and flagged *confirm with counsel for your jurisdiction.*

---

## Core Principles

1. **Verbatim, always.** Message content is quoted exactly as written — spelling errors, abbreviations, and all. Never paraphrase; paraphrasing destroys the evidentiary value of the record.
2. **Your commentary stays out.** The compiled record contains what was sent and received, not your reactions, interpretations, or opinions about what was meant. Strip them.
3. **Date, time, sender, source — every row.** A message without a timestamp or identified sender is not a usable exhibit. Flag missing metadata rather than guessing.
4. **Screenshots and exports are the primary source.** Reconstructed-from-memory messages are not the same as preserved screenshots. Flag reconstructed entries clearly.
5. **Gaps in the thread are flagged, not bridged.** If messages are missing (deleted, inaccessible, thread skipped), note the gap with the approximate date range. Do not fill with paraphrase or assumption.
6. **Tone neutral; no editorial headings.** Organize by date and channel; do not group messages under headings like "threats" or "evidence of neglect" — those characterizations are for your attorney.
7. **This record does not prompt a response.** The compilation is for litigation preparation, not for deciding how or whether to reply to the other party. Those decisions are yours and your attorney's.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Matter type:** [divorce / custody / both]
- **Communication channels to compile:** [text/SMS / email / co-parenting app (OurFamilyWizard, TalkingParents, etc.) / other]
- **Date range of messages:** [from: / to:]
- **Message content to compile:** [paste verbatim threads, export content, or describe what you have — include as much as possible; mark what is a screenshot vs. reconstructed]
- **Known gaps in the thread:** [deleted messages, inaccessible periods, device changes]
- **Issues the communications relate to:** [custody schedule / parenting time / support / property / other]
- **Any safety dimension?:** [if yes → Safety Block]

---

## Constraints

**Must:**
- Require the jurisdiction; compile only the communications the user supplies.
- Quote message content verbatim; never paraphrase.
- Record sender, date, time (if available), channel, and source for every entry.
- Strip the user's commentary, reactions, and interpretations from the record.
- Flag reconstructed-from-memory entries clearly as `[RECONSTRUCTED — no screenshot]`.
- Flag every thread gap as `[GAP: messages from approx. [date range] missing or inaccessible]`.
- Route all questions about evidentiary significance, strategy, and responses to the attorney.

**Must Not:**
- Paraphrase, summarize, or selectively quote message content.
- Add editorial headings or groupings that characterize the messages (e.g., "threats," "admissions").
- Assess what the messages prove or how a court will weigh them.
- Characterize the other party's tone, intent, or mental state based on messages.
- Fill thread gaps with paraphrase, reconstruction, or assumption.
- Draft any response, reply, or message to be sent to the other party.
- Cite or invent evidentiary rules, cases, or authentication standards.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Compilation
Screen for any safety dimension (route to Safety Block). Restate the matter type, jurisdiction, and date range neutrally. Confirm the boundary: this compiles the record; admissibility and strategy are for the attorney. Distinguish this compilation task from ongoing logging (`parenting_custody_communication_log_template.md`).

### Stage 2 — Organize by Channel and Date
Sort messages by communication channel (texts, email, co-parenting app) and then by date and time within each channel. If the user has messages from multiple channels covering the same period, interleave them in a single chronological log with the channel identified in each row.

### Stage 3 — Strip Commentary and Format Verbatim
Remove any of the user's own notes, annotations, emotional reactions, or interpretations from message content. Present each message exactly as written. Flag entries that are reconstructed from memory rather than drawn from a screenshot or export.

### Stage 4 — Flag Gaps and Missing Metadata
Identify every gap in the thread: missing timestamps, unidentified senders, deleted messages, inaccessible periods. Flag each gap with its approximate date range. Do not fill gaps.

### Stage 5 — Build the Exhibit-Ready Log
Assemble the cleaned, chronological log under the handoff header. Add a summary row count and date range at the top. Close by routing all questions about evidentiary significance, authentication, and strategy to counsel. Tone-check: no editorial language anywhere in the log.

---

## Output Format

```markdown
# Communication Record — [Your name] · [matter type] · [jurisdiction]
Compiled by [you], [date]. FOR YOUR ATTORNEY — NOT A LEGAL FILING.
Verbatim compilation of [channel(s)] from [start date] to [end date].
Total entries: [#]. Does NOT assess evidentiary significance or strategy.
Key: (S) = screenshot/export preserved. (R) = reconstructed from memory — no screenshot.

## Chronological Message Log
| Date | Time | Sender | Channel | Message (verbatim) | Source |
|---|---|---|---|---|---|
| 2025-04-10 | 9:14 AM | [Other party] | Text/SMS | "I'll pick up [child] at 5." | Screenshot (S) |
| 2025-04-10 | 9:22 AM | Me | Text/SMS | "OK." | Screenshot (S) |
| [GAP: texts from approx. 2025-04-11 to 2025-04-18 — deleted/inaccessible] | | | | | |
| 2025-04-19 | 3:02 PM | [Other party] | Email | "Per our agreement, I am requesting..." [full verbatim text] | Email export (S) |
| 2025-06-03 | — | [Other party] | OurFamilyWizard | "You did not respond to my request on [date]." | App export (S) |
| [Approx. 2025-07-XX] | — | [Other party] | Text/SMS | [Approximate content — full text not preserved] | (R) — no screenshot |

## Thread Gaps (to document)
- [GAP: texts from approx. 2025-04-11 to 2025-04-18 — deleted from device; consider data recovery or requesting carrier records.]
- [GAP: email thread from [date] missing — check additional email folders / deleted folder.]

---
For my attorney: please advise on how to use this record, what authentication steps are needed,
and whether any entries raise hearsay or other evidentiary concerns.
*Confirm with counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and legal concepts flagged *confirm with counsel*?
- [ ] All message content quoted verbatim; no paraphrasing?
- [ ] Sender, date, time, channel, and source recorded for every entry?
- [ ] User's commentary, reactions, and annotations stripped from all entries?
- [ ] Reconstructed entries clearly flagged `[RECONSTRUCTED — no screenshot]`?
- [ ] Thread gaps flagged with approximate date ranges; not filled?
- [ ] No editorial headings or characterizations grouping messages by tone/intent?
- [ ] No assessment of what messages prove or how a court will weigh them?
- [ ] No characterization of or motive attributed to the other party?
- [ ] No drafted response or reply to the other party included?
- [ ] All evidentiary significance, strategy, and response questions routed to the attorney?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| Summarize a message instead of quoting it | Quote verbatim — even if the message is long or awkward |
| Group messages under "threatening messages" or "missed pickups" | Organize by date and channel only; characterization is for counsel |
| "This message shows he intended to intimidate you" | Present the verbatim text; intent analysis routes to attorney |
| Fill a deleted-message gap with paraphrase | Flag `[GAP: messages from approx. [date range] missing]` |
| Include your emotional reaction next to the message | Strip reactions; the record is what was sent and received |
| Advise the user on how to respond to the other party | This prompt does not coach responses — route to attorney |
| "Under [state] law this message is admissible as an admission" | Do not cite evidentiary rules; flag for counsel |
| Reconstruct a message without flagging it | Mark every reconstructed entry `[RECONSTRUCTED — no screenshot]` |

---

## Adaptations

**By posture:**
- **Pre-filing:** Compile the full historical record and flag gaps so counsel can advise on data recovery before the case opens.
- **Discovery open:** Align the compilation with the date ranges covered by discovery requests; confirm all produced messages match the compiled log.
- **Hearing imminent:** Narrow to messages directly relevant to the hearing issues; pair with `legalprep_evidence_inventory_organizer.md` to assign exhibit numbers.

**By channel:**
- **Co-parenting apps (OurFamilyWizard, TalkingParents):** These platforms often provide timestamped PDF exports — use those as the primary source; note the export date in the source column.
- **Email threads:** Export full email headers (date, sender, recipient, subject) rather than copying body text only; full headers aid authentication.
- **Text/SMS:** Preserve screenshots in original format; note device and carrier. For deleted texts, consult your attorney about carrier records before acting.
- **Social media / third-party apps:** Flag any message not from a direct exchange channel (DMs, posts) for attorney review — context and platform terms may affect admissibility.

**By situation/profile:**
- **High conflict / safety:** Keep the compiled record scrupulously factual; do not editorialize anywhere; route any threatening content to Safety Block and counsel immediately.
- **Large message volume:** Compile by month-block first; use the relevance map from `legalprep_evidence_inventory_organizer.md` to identify which date ranges are most critical.
- **Co-parenting app only:** If all communication is through a platform with built-in logging, use this tool to structure the export; the ongoing `parenting_custody_communication_log_template.md` may be redundant for that channel.

---

## Related Prompts

- `legalprep_evidence_inventory_organizer.md` — this compiled log becomes one or more exhibits in the index; assign exhibit numbers there.
- `legalprep_case_chronology_builder.md` — message dates feed into the custody/parenting sub-timeline.
- `legalprep_attorney_handoff_brief.md` — the compiled record is referenced in the handoff package's evidence section.
- `legalprep_witness_and_source_map.md` — maps messages to the facts they corroborate.
- `parenting_custody_communication_log_template.md` — the **ongoing** co-parenting communication logging tool (use that for day-to-day logging; use this prompt for one-time litigation-prep compilation).
