---
title: "Professional & Authority Router — Which Channel Do I Even Need?"
category: legalprep
description: "Help a layperson facing a personal legal problem organize their situation into a routing map of candidate channels — attorney (and what kind), police/911, employer HR, an online platform's reporting/takedown process, a government regulator or agency, or a courthouse self-help/legal-aid office. Organizes the situation into a triage table only. Does NOT tell the user they 'have a case', assess strength, predict outcomes, cite law, or draft anything — those route to an attorney or the relevant authority. Not legal advice."
techniques:
  - DS-01
  - DS-21
  - ST-02
  - CM-01
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - self-represented
  - triage
  - routing
  - referral
  - reporting
  - authority
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_handoff_brief.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_consultation_question_builder.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_incident_documentation_organizer.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_evidence_preservation_and_digital_organizer.md
  - domain-legal/litigation/legal_complaint_drafter.md
---

**Purpose:** Help you figure out **which professional or authority to approach** for a personal legal problem — often more than one — and organize your situation into a clean routing map you can act on. Many problems have several possible channels: an attorney, the police or 911, your employer's HR, an online platform's reporting or takedown process, a government regulator or agency (for example the FTC, your state attorney general, the EEOC, or a labor board), or a courthouse self-help/legal-aid office. This organizes **your situation into candidate channels** — it does **not** tell you that you "have a case," judge how strong your situation is, predict what any channel will do, cite law, or draft anything for you. Whether to pursue a channel — and what it means legally — is for an attorney or that authority.

**When to use:** Something has happened (a harassing message, a workplace incident, a scam, a stalking sighting, something posted about you, a consumer dispute, a housing problem) and you are not sure who to even call. You want to map your options before spending money on a consultation, and separate what is a legal question (route to an attorney) from what is a reporting or self-service channel.

**When NOT to use:** You want to know whether you "have a case," what it is worth, what to file, or which channel will win → that is legal analysis; take your routing map to an attorney (see `legalprep_consultation_question_builder.md`). There is an active safety emergency, threat, or crime in progress → Safety Block first; call 911.

---

## Safety Block

Stop and use a different pathway if:
- You are in immediate danger, or a crime is in progress → **911** (US emergency).
- There is stalking, threats, harassment you fear will escalate, or domestic violence → **National Domestic Violence Hotline 1-800-799-7233** (US). Do not confront the person; preserve records securely; involve police and counsel.
- A child is being abused or is unsafe → **Childhelp National Child Abuse Hotline 1-800-422-4453** (US); emergencies **911**.
- You or someone else is in crisis → **988 Suicide & Crisis Lifeline** (US).
- Identity theft, fraud, or a scam → **IdentityTheft.gov** (FTC), **ReportFraud.ftc.gov**, or the FBI Internet Crime Complaint Center at **ic3.gov**. These are official reporting channels, not legal advice.

This prompt is educational support for organizing your own situation. It is not a substitute for legal, safety, or law-enforcement services.

---

## Scope Boundary — Read First

This **organizes your situation into a map of candidate channels**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's law.** It will **not** tell you that you "have a case," assess how strong your situation is, predict what a channel will do, decide which channel is "right," state legal conclusions (that something "is" harassment, defamation, retaliation, or a crime), cite or invent statutes or standards, or draft any letter or filing. Which channels apply, and what any of them can do, **vary by state and country and change over time.** Every "is this actionable / what do I file / what is it worth" question routes to an attorney or the relevant authority — *confirm with counsel for your jurisdiction.*

---

## Core Principles

1. **Sort the situation, don't judge it.** The output is a triage map of possibilities, not a verdict on whether you will prevail anywhere.
2. **Most real problems have more than one channel.** A workplace incident can be HR *and* an agency *and* an attorney at once. List all candidates rather than picking one for the user.
3. **Separate legal questions from reporting channels.** "Is this illegal / do I have a claim" is an attorney question. "Report this account / file this complaint / request this takedown" is a channel that exists regardless of legal merit.
4. **Name the channel by what it does, not what it will decide.** Describe a channel's function ("HR investigates workplace-policy complaints"; "the platform reviews reports against its rules") without promising an outcome.
5. **Time-sensitivity is a flag, not a deadline.** Some channels have windows (agency filing periods, platform reporting, preservation of evidence). Flag "this may be time-sensitive — *confirm the deadline with counsel or the channel*," never state a specific limitations period.
6. **Use only official, stable resources.** Point to official agency websites and the local bar / legal-aid referral, never an invented phone number or a claim about a specific office's rules.
7. **You map; the professional or authority assesses.** This tool lays out where you *could* go. Whether to go, and what happens there, is for an attorney or that authority.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **What happened, briefly and factually:** [in your own words — who, what, when, where]
- **What kind of matter it feels like:** [workplace / harassment or stalking / something posted about me / scam or fraud / consumer or contract / housing / other — your best guess is fine]
- **Who is involved:** [you; other party by role — employer, stranger, company, landlord, ex, online account]
- **What outcome you are hoping for:** [it to stop / money back / something removed / a record / accountability / just to understand options]
- **Anything already tried:** [reported to anyone? contacted a company? saved evidence?]
- **Any safety dimension (threat, danger, minor, crisis)?:** [if yes → Safety Block before anything else]

---

## Constraints

**Must:**
- Require the jurisdiction; build the map only from the facts the user supplies.
- Present **multiple candidate channels** where they exist, each with its function and what to bring.
- Distinguish legal-question channels (attorney) from reporting/self-service channels (agency, platform, HR, police).
- Point to official resources by name/website; flag any phone number you are not certain is current as `[VERIFY: current number for <resource>]`.
- Flag time-sensitivity generically as "may be time-sensitive — *confirm with counsel or the channel.*"
- Close every channel row with a *confirm with counsel / the authority* note.

**Must Not:**
- Tell the user they "have a case," a claim, or a valid complaint, or assess how strong the situation is.
- State a legal conclusion (that something "is" harassment, defamation, retaliation, fraud, or a crime).
- Predict what any channel will do or which channel is "best."
- Cite or invent statutes, agencies' rules, limitations periods, or filing standards.
- Attribute motive to, diagnose, or label the other party.
- Draft a complaint, report, letter, or filing (route those out).
- Invent a phone number, office, or agency, or fill factual gaps.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for any safety dimension (route to Safety Block if present — danger, threats, a minor, crisis, identity theft/fraud). Restate the situation neutrally and the jurisdiction. State the boundary: this maps candidate channels; whether to use any of them, and what they will do, is for an attorney or that authority.

### Stage 2 — Clarify What the User Wants
Reflect back the user's goal (make it stop / recover money / remove content / create a record / understand options). Different goals point to different channels; capture the goal without promising it is achievable anywhere.

### Stage 3 — Identify Candidate Channels
From the facts, list every channel that *could* apply, using the categories: attorney (and what kind — for example employment, family, consumer, IP/media, general civil litigation), police / 911, employer HR or ethics line, an online platform's reporting/takedown process, a government regulator or agency (FTC, state attorney general consumer-protection office, EEOC, state labor board, etc.), and courthouse self-help / legal-aid / bar-referral. Do not narrow to one.

### Stage 4 — Describe Each Channel Factually
For each candidate, note in plain language what that channel *does* (its function), what to bring to it, and one honest limit (for example "HR enforces company policy, not the law"; "an agency intake is not the same as suing"; "a platform applies its own rules, not a court's"). Flag time-sensitivity generically.

### Stage 5 — Separate Legal Questions from Reporting Steps
Split the map into "questions only an attorney can answer" (is this actionable, what to file, what it is worth) and "channels you can approach directly" (report/file/request). Make clear the two are independent — a reporting channel exists whether or not a claim is strong.

### Stage 6 — Assemble the Routing Map and Route Out
Assemble the routing table under the header. Point the user to `legalprep_professional_handoff_brief.md` to prepare for whichever channel(s) they choose, and to `legalprep_consultation_question_builder.md` for the attorney conversation. Close by routing all legal questions to counsel and all reporting to the official channel.

---

## Output Format

```markdown
# Routing Map — [Your name] · [matter, in plain words] · [jurisdiction]
Prepared by [you], [date]. FOR MY OWN PLANNING — NOT LEGAL ADVICE.
Maps candidate channels only. Does NOT say I "have a case," assess strength, predict
outcomes, or decide which channel is right — those are for an attorney or the authority.

## What Happened (facts only)
[Brief, neutral summary — who, what, when, where.]

## What I'm Hoping For
[Make it stop / money back / content removed / a record / understand options.]

## Candidate Channels
| Channel | What this channel does | What to bring | Honest limit | Time-sensitive? |
|---|---|---|---|---|
| Attorney — [type, e.g. employment] | Assesses whether you have a claim, options, what to file, and value | Handoff brief; timeline; evidence index | Costs money; consultation may be paid | May be — *confirm with counsel* |
| Police / 911 | Takes reports of crimes; 911 for emergencies | Incident record; evidence; ID | Handles crimes, not civil disputes | If a crime/threat is ongoing → now |
| Employer HR / ethics line | Investigates workplace-policy complaints | Dated incident records; witnesses | Enforces company policy, not the law | May be — *confirm internally* |
| Online platform reporting/takedown | Reviews reports against the platform's own rules | Links/URLs; screenshots with context | Applies its rules, not a court's | Preserve evidence first |
| Government agency/regulator — [e.g. FTC, state AG, EEOC, labor board] | Takes complaints; may investigate patterns | The relevant facts/records; account info | Intake is not the same as suing | Some have filing windows — *confirm* |
| Courthouse self-help / legal aid / bar referral | Explains process; refers to low-cost/free counsel | Your situation summary | Cannot give case-specific legal advice at intake | — |

## Legal Questions (attorney only — do not answer these yourself)
- Is what happened actionable? / Do I have a claim?
- What, if anything, would I file — and where?
- What is this worth / what could I recover?
- Which of the channels above is actually worth my time?

## Reporting Steps I Can Take Directly (independent of the legal questions)
- [e.g. Report the account to the platform] — via [official channel]
- [e.g. File a complaint with the FTC] — via ReportFraud.ftc.gov / IdentityTheft.gov
- [e.g. Report to my state attorney general's consumer-protection office]

## Official Resources (verify before relying)
- FTC fraud/scams: ReportFraud.ftc.gov · Identity theft: IdentityTheft.gov
- FBI Internet Crime Complaint Center: ic3.gov · Government services: usa.gov
- Your state attorney general's consumer-protection office
- Your state/local bar association lawyer-referral service
- Your courthouse self-help center / legal-aid office
- [VERIFY: current phone number for any office before calling]

---
Next: prepare a handoff package (legalprep_professional_handoff_brief.md) and consultation
questions (legalprep_consultation_question_builder.md) for whichever channel(s) I choose.
*Confirm with counsel or the relevant authority for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and legal concepts flagged *confirm with counsel*?
- [ ] Multiple candidate channels presented where they exist (not narrowed to one)?
- [ ] Each channel described by its function, what to bring, and an honest limit?
- [ ] No statement that the user "has a case," a claim, or a strong situation?
- [ ] No legal conclusion (that something "is" harassment/defamation/retaliation/a crime)?
- [ ] No outcome prediction or "best channel" recommendation?
- [ ] No cited/invented statute, agency rule, or limitations period?
- [ ] Legal questions separated from reporting channels?
- [ ] Only official resources named; uncertain phone numbers flagged `[VERIFY:]`?
- [ ] All "is this actionable / what to file / what is it worth" routed to an attorney?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "You have a strong harassment claim — sue" | List candidate channels; route the "do I have a claim" question to an attorney |
| "This is clearly defamation" | Describe the media/IP-attorney channel; legal conclusions are for counsel |
| "The EEOC will rule in your favor" | "An agency takes complaints and may investigate" — no outcome prediction |
| "Just go to HR, that's the right move" | List HR *and* other channels with each one's function and limits |
| "You must file within 180 days" | "May be time-sensitive — *confirm the deadline with counsel or the channel*" |
| Invent a hotline number | Name the official website; flag `[VERIFY: current number]` |
| "He did this to intimidate you" | Strip motive; describe channels, not the other party |
| Treat a threat or crime-in-progress as routing | Stop, follow the Safety Block, call 911 |

---

## Adaptations

**By matter type:**
- **Workplace:** Candidates usually include HR/ethics line, a government agency (EEOC or a state labor board), and an employment attorney. Pair with `../workplace-harassment/` sets where present and the attorney-side `../../employment-labor/legal_workplace_investigation_plan_and_report.md`.
- **Harassment / stalking:** Emphasize the Safety Block, police/911, platform reporting, and do-not-confront; preserve evidence via `legalprep_evidence_preservation_and_digital_organizer.md`.
- **Something posted about you (defamation/IP):** Candidates include the platform's reporting/takedown process, a media/IP attorney, and (for copyright) a DMCA process. Route legal characterization to counsel.
- **Scam / fraud / identity theft:** Center IdentityTheft.gov, ReportFraud.ftc.gov, ic3.gov, and your state attorney general; a consumer attorney is a parallel channel.
- **Consumer / housing:** Candidates include the state attorney general consumer-protection office, a relevant regulator, small-claims self-help, and a consumer/housing attorney or legal aid.

**By situation/profile:**
- **Cost-constrained:** Foreground legal aid, bar-referral, and courthouse self-help before paid counsel.
- **Unsure of matter type:** Keep the map broad; a bar-referral or legal-aid intake can help identify the right kind of attorney.
- **Safety-sensitive:** Safety Block first; do not list any channel that requires confronting the other party.

---

## Related Prompts

- `legalprep_professional_handoff_brief.md` — once you pick a channel, prepare the package to bring to it.
- `legalprep_consultation_question_builder.md` — build the questions for the attorney channel.
- `legalprep_incident_documentation_organizer.md` — document the underlying event before routing it anywhere.
- `legalprep_evidence_preservation_and_digital_organizer.md` — preserve evidence before you report to any channel.
- `../../litigation/legal_complaint_drafter.md` — the attorney-side counterpart if a matter proceeds to court.
