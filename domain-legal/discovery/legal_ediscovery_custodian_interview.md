---
title: "E-Discovery Custodian Interview Outline"
category: legal/discovery
description: "Run a structured custodian interview to map data sources, devices, communication tools, retention, and behaviors that drive a defensible ESI collection — output is a record-quality interview outline plus a population-and-source map."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - discovery
  - ediscovery
  - custodian-interview
  - esi-collection
  - litigation-hold
updated: "2026-05-08"
related_prompts:
  - domain-legal/discovery/legal_document_request_drafter.md
  - domain-legal/discovery/legal_discovery_response_objections.md
  - domain-legal/discovery/legal_document_review_coding_taxonomy.md
---

**Purpose:** Generate a custodian-interview outline that systematically captures every data source and behavior relevant to a defensible ESI collection, while building a contemporaneous record that supports a Rule 26(g) certification of reasonable inquiry.

**When to use:** Beginning of a matter under litigation hold; expanding a collection after newly identified custodians; verifying completeness before a Rule 30(b)(6) deposition on document preservation.

---

## Your Input

- **Custodian:** [Name, role, tenure, reporting line, work locations]
- **Matter and time period:** [Matter type, key dates, hold start, time period to be searched]
- **Technical environment:** [Email platform, chat platform, file-storage platforms, CRM/ERP/ticketing, BYOD policy, VPN, removable media policy]
- **Retention regime:** [Default retention by system; legal-hold mechanism; auto-deletion settings]
- **Subjects of the matter relevant to this custodian:** [Specific topics, projects, counterparties, transactions]
- **Interviewer:** [Outside counsel / in-house / forensic vendor]
- **Privileged context:** [Yes — interview conducted at direction of counsel for purpose of providing legal advice; should be marked accordingly]

---

## Constraints

**Must:**
- Open with the **privilege framing**: who the lawyer represents, that the interview is for the purpose of providing legal advice, that the custodian's communications with counsel in this interview are confidential and should not be shared with non-privileged third parties.
- Cover, in order: **identifications**, **work environment**, **devices and accounts**, **communication patterns**, **storage habits**, **retention behavior**, **collaboration tools**, **personal-device use**, **prior collections**, **knowledge of relevant subjects**.
- For every system or device, capture: in use during time period, account identifier, location of data, retention default, custodian's typical use, any auto-deletion the custodian configured, last clear-out, any BYOD wiping events.
- Capture **chat** systems by name (Slack, Teams, Webex, Google Chat) and **mobile** messaging (SMS, iMessage, WhatsApp, Signal, Telegram).
- Capture **non-corporate** accounts where the custodian may have transmitted relevant content (personal email, personal phone, personal cloud).
- Capture **departures**: prior custodians who left; treatment of departed custodians' data.
- Capture **destruction events**: re-imaging, hard-drive replacement, account suspension, retention pruning.
- Capture **knowledge of subject matter** and identify **other persons** involved in those subjects, both inside and outside the company.
- Output must include both an **interview outline** (questions in order) and a **completed source map** template the interviewer fills in.

**Must Not:**
- Lead the witness on substantive subject-matter facts. The interview is primarily about ESI architecture and behavior, not the merits.
- Skip personal-device and personal-account questions because they are uncomfortable.
- Treat the interview as a substitute for IT validation. Always cross-check custodian answers with IT for accounts and systems.
- Memorialize answers in a way that disclaims privilege. The interview memorandum should be marked privileged work product.
- Forget to ask about the litigation-hold notice — receipt, understanding, compliance.

---

## Instructions

1. **Open with privilege framing**, hold confirmation, and the matter description (high level).
2. **Custodian context:** role, dates of relevant employment, supervisors, supervisees, department, physical work locations, work hours and patterns.
3. **Devices and accounts:** corporate laptop(s), desktop, mobile phone (corporate / BYOD), tablet, removable media, home office equipment, personal devices used for work, virtual desktops.
4. **Email:** primary corporate, alias addresses, distribution lists membership, archival folders, PST/local archives, retention rules custodian sets, deleted-items behavior.
5. **Chat / collaboration:** every platform; channels relevant to the matter; DM behavior; ephemeral / disappearing-message settings; sharing of files inside chat.
6. **File storage:** corporate share drives, OneDrive/Google Drive/SharePoint, departmental wikis, project folders.
7. **Specialized systems:** CRM, ticketing, ERP, code repos, design tools, financial systems, HR systems — wherever relevant content might live.
8. **Mobile messaging:** SMS, iMessage, WhatsApp, Signal, Telegram, voice memos, mobile email.
9. **Personal accounts:** personal email, personal cloud, personal devices used for work.
10. **Retention behavior:** what does the custodian delete and when; auto-archive rules; PST creation; cleanup events.
11. **Destruction / disruption events:** re-imaging, device replacement, account suspension, departure events, departed colleagues' inboxes.
12. **Litigation hold:** receipt date, understanding, compliance, any difficulty, any inadvertent deletion since hold.
13. **Subject-matter knowledge:** for each relevant subject, custodian's role, who else was involved, where decisions were memorialized.
14. **Other custodians:** who else should be interviewed; who else has relevant data.
15. **Closing:** confirm hold compliance going forward; instruct on preservation of any data sources newly identified; schedule follow-up if needed.

---

## Output Format

### Part A — Interview Outline (use during interview)

```markdown
CUSTODIAN INTERVIEW — {Name} — {Date} — Privileged & Confidential — Attorney Work Product

1. Privilege framing
   - "I represent {entity} in {matter}. I'm here to gather facts at the direction of counsel for the purpose of providing legal advice. Our conversation is privileged. Please don't discuss what we cover here with anyone other than counsel."

2. Hold confirmation
   - When did you receive the litigation hold notice in this matter?
   - Have you preserved everything called for since then?
   - Has anything been deleted, transferred, or modified inadvertently since the hold?

3. Role and dates
   - Title; reporting structure; team; tenure within the time period; physical and remote work locations.

4. Devices
   - For each device used during the time period:
     - Type, model, year, identifier (if known)
     - Used for work? Used for personal too?
     - Backup behavior
     - Replacement events during the period
     - Currently in your possession?

5. Email
   - Primary corporate address; aliases; distribution lists you were on
   - Archival behavior; PST or local archives
   - Auto-delete rules
   - Personal email used for work?

6. Chat
   - For each platform: in use during period? Channels relevant to {subjects}? DMs to which colleagues? Disappearing-message settings? Files shared inside chat?

7. File storage
   - Corporate file shares; cloud storage (OneDrive, Google Drive, SharePoint); project folders; wikis

8. Specialized systems
   - CRM; ticketing; ERP; design; code; finance; HR — relevant to subjects?

9. Mobile messaging
   - SMS, iMessage, WhatsApp, Signal, Telegram — used for work? With whom?

10. Personal accounts and devices
    - Used for work content during period? When?

11. Retention behavior
    - What do you delete and when? PSTs? Archives? Cleanups?

12. Disruption events
    - Re-imaging, device replacement, account suspension, role change, departure events of colleagues whose data we may need

13. Subject knowledge — {subject 1}
    - Your role, dates of involvement, others involved, where decisions and discussion are memorialized

14. Subject knowledge — {subject 2}
    {repeat}

15. Other people we should interview
    - Names, roles, why

16. Anything else
```

### Part B — Source Map (fill during interview)

```markdown
| Source / system | Account or location | In use {dates} | Retention default | Custodian behavior | Last cleanup | Notes |
|------------------|----------------------|------------------|---------------------|----------------------|----------------|--------|
| Outlook (corporate) | {address} | {dates} | {retention} | {behavior} | {date} | ... |
| Slack | {handle} | {dates} | {retention} | DMs / channels listed | {date} | ... |
| Personal iPhone | n/a | {dates} | n/a | iMessage with {persons} | n/a | BYOD; cooperate with collection? |
| OneDrive | {URL} | {dates} | {retention} | Active project folders | n/a | ... |
| ... | ... | ... | ... | ... | ... | ... |
```

### Part C — Interview Memorandum Header (for the write-up)

```markdown
PRIVILEGED & CONFIDENTIAL — ATTORNEY WORK PRODUCT
Prepared at the direction of counsel for the purpose of providing legal advice.

INTERVIEW MEMORANDUM
Custodian: {name, title}
Date: {date}
Interviewers: {names, roles}
Location / format: {in person / Zoom}
Time period covered: {dates}

[Body summarizes the source map and substantive responses; flags follow-ups; closes with hold-compliance confirmation.]
```

---

## Verification

- [ ] Privilege framing delivered at the open and reflected in the memo header.
- [ ] Litigation-hold receipt and compliance confirmed.
- [ ] Every device, account, and system listed with retention, behavior, and identifier.
- [ ] Personal devices and accounts addressed, not skipped.
- [ ] Chat and mobile messaging covered platform-by-platform.
- [ ] Retention defaults for each system distinguished from custodian-set behaviors.
- [ ] Disruption / destruction events captured.
- [ ] Subject-matter knowledge captured neutrally without leading.
- [ ] Other-custodian leads captured.
- [ ] Source map populated; gaps flagged for IT confirmation.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Skipping personal-device questions because they are uncomfortable | Ask explicitly; BYOD content is a frequent source of relevant ESI and a frequent spoliation flashpoint |
| Accepting "I don't really use Slack" without channel-by-channel review | Ask about specific channels and DMs by counterpart |
| Forgetting ephemeral / disappearing-message settings | These can implicate spoliation and Rule 37(e) analysis |
| Conflating retention default with custodian behavior | Distinguish: the system default and what the custodian actually does |
| Trusting custodian recall over IT records | Always reconcile with IT for accounts, devices, and dates |
| Memorializing in a way that does not assert privilege | Mark the memo as privileged work product prepared at direction of counsel |
| Skipping departed-colleague data treatment | Departed custodians' mailboxes are a common ESI gap |
| Leading the witness on substantive merits | Keep the interview ESI-architectural; substantive interviews come later |
| No follow-up plan for sources newly identified | End every interview with a written follow-up list and dates |
