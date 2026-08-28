---
title: "Personal CRM Application — Contact Cards, Follow-up Urgency, and Tags MVP"
category: software-engineering/prototyping
description: "Spec a personal CRM: a person data model, a color-coded contact-card grid with search and tag/status filters, add/detail/edit flows with 'record contact', and CSV export — local-first."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DS-06
  - QA-01
difficulty: beginner
tags:
  - prototyping
  - personal-crm
  - contacts
  - crud
  - app-spec
updated: "2026-06-07"
related_prompts:
  - domain-software-engineering/prototyping/prototyping_inventory_tracker.md
  - domain-software-engineering/prototyping/prototyping_habit_tracker.md
  - domain-software-engineering/prototyping/prototyping_request_management.md
---

# Personal CRM Application

**Objective:** Produce a build-ready spec for a personal CRM — a person data model, a color-coded contact-card grid with search and tag/status filters, add/detail/edit flows including a one-tap "record contact," and CSV export — local-first, no accounts, mobile-responsive.

**When to use:**
- Tracking professional relationships and follow-ups without a full sales CRM.
- A personal networking tool that nudges you when contact goes stale.
- A quick, no-account app to manage contacts with tags and notes.

**When NOT to use:**
- Team sales pipelines with deals, stages, and reporting — needs a real CRM.
- Multi-user shared contact databases — local-first MVP has no sync.
- Anything requiring email/calendar sync or enrichment at MVP.

**Audience:** Individuals generating apps with Lovable, Bolt, v0, or similar AI app builders.

---

## Inputs / Context

Supply the following (or accept the spec's defaults):

1. **Fields wanted** — beyond Name (required): company, role, email, phone, LinkedIn, how-we-met, notes.
2. **Tags** — the relationship categories (defaults: Friend, Colleague, Client, Prospect, Investor, Mentor, Mentee, Other).
3. **Follow-up urgency thresholds** — the day bands for color-coding (defaults: ≤30 green, 31–60 yellow, 61+ red, none gray).
4. **Sort/filter needs** — sort options and which filters matter.
5. **Theme** — light default with dark toggle; mobile-responsive confirmed.
6. **Persistence scope** — confirm local-first with CSV export (no backend/API).

---

## Constraints

### Must
- Define a person model with required Name and the requested optional fields (email format-validated).
- Color-code cards by days-since-last-contact using the defined thresholds (incl. a "never contacted" state).
- Provide search (name/company), tag filter, and a follow-up/contact-status filter.
- Provide add (modal), detail, edit, "record contact" (sets last-contact to today), and delete-with-confirm.
- Provide CSV export; be mobile-responsive with a dark-mode toggle.

### Must Not
- Invent fields or tags the user didn't request (offer defaults, marked as such).
- Make external API calls or imply email/calendar sync at MVP.
- Delete a contact without confirmation.
- Over-scope with deals/pipelines, accounts, or multi-user sync.

---

## Instructions

1. **Confirm scope.** Restate it as a local-first, single-user CRM MVP with CSV export (flag if sync/backend is needed).
2. **Specify the data model.** Person fields and types; email format validation; auto created-date; last-contact and next-follow-up dates.
3. **Specify the main view.** Card grid; each card shows name/company/role/tag pills/days-since-contact; color-code by thresholds; sort options; real-time search.
4. **Specify filters.** By tag (match any), by "needs follow-up" (next-follow-up ≤ today), by contact status (recent/overdue/never).
5. **Specify add + detail/edit.** Floating "+" → modal with all fields; detail view shows everything; edit toggle; "Record Contact" sets last-contact = today; delete confirms.
6. **Specify design + technical.** Clean modern; light default + dark toggle; mobile cards stack single-column; CSV export; local storage; no external APIs.
7. **Specify nice-to-haves** (only if straightforward): CSV import, custom sort, bulk tag edit — clearly marked optional.
8. **Self-check before output.** Confirm: Name required + email validated; color thresholds incl. "never"; search + both filters present; "record contact" updates the date; delete confirms; CSV export; no external calls; no invented fields beyond flagged defaults. Then emit the spec.

---

## False-Positive Prevention

❌ **DON'T:**
- Add deals/pipelines, accounts, or multi-user sync to an MVP.
- Invent fields or tags the user didn't ask for without marking them defaults.
- Make external API calls or imply email/calendar integration.
- Skip the "never contacted" color state or delete without confirmation.
- Build desktop-only when contacts are checked on the phone.

✅ **DO:**
- Scope to local-first, single-user with CSV export.
- Require only Name; validate email format; offer tags/thresholds as labeled defaults.
- Color-code urgency including a distinct "never contacted" state.
- Make "Record Contact" a one-tap update and confirm deletes.
- Design mobile-responsive with a dark-mode toggle.

---

## Output Format

```
APP: Personal CRM
SCOPE: [local-first, single-user MVP, CSV export / flag if sync needed]

DATA MODEL — Person
- Name (required); Company; Role; Email (format-validated); Phone; LinkedIn URL; How We Met;
  Tags (multi-select [...]); Last Contact Date; Next Follow-up Date; Notes; Created Date (auto)

MAIN VIEW
- Card grid: Name, Company, Role, Tag pills, days since last contact
- Color-code: ≤[a] green / [a+1]–[b] yellow / [b+1]+ red / none gray
- Sort: Name / Last Contact (recent|oldest) / Company; real-time search (name/company)

FILTERS
- By Tag (match ANY); Needs Follow-up (next ≤ today); Contact status (Recent/Overdue/Never)

ADD / DETAIL / EDIT
- Floating "+" → modal (all fields); Detail view (all fields + full notes)
- Edit toggle; "Record Contact" → Last Contact = today; Delete (confirm)

DESIGN / TECHNICAL
- Clean modern; light default + dark toggle; mobile single-column; CSV export; local storage; no external APIs

NICE TO HAVE (optional)
- CSV import; custom sort; bulk tag edit

VERIFICATION NOTES
- [assumptions / defaults flagged]
```

---

## Example Output

```
APP: Personal CRM
SCOPE: Local-first, single-user MVP with CSV export. No accounts/sync.

DATA MODEL — Person
- Name: required
- Company / Role: optional text
- Email: optional, validated format
- Phone / LinkedIn URL / How We Met: optional text
- Tags: multi-select [Friend, Colleague, Client, Prospect, Investor, Mentor, Mentee, Other]
- Last Contact Date / Next Follow-up Date: date pickers
- Notes: long text; Created Date: auto

MAIN VIEW
- Card grid; each card: Name · Company · Role · tag pills · "12 days since contact"
- Border color: ≤30d green / 31–60d yellow / 61+ red / no date gray
- Sort: Name A–Z, Last Contact (recent/oldest), Company
- Search bar filters by Name or Company as you type

FILTERS
- By Tag (shows people matching ANY selected tag)
- "Needs Follow-up" (Next Follow-up Date today or past)
- Contact status: Recent / Overdue / Never Contacted

ADD / DETAIL / EDIT
- Floating "+" bottom-right → modal with all fields; Save / Cancel
- Click a card → detail view with all fields + full notes
- "Edit" makes fields editable (Save/Cancel)
- "Record Contact" sets Last Contact Date = today
- "Delete" with a confirmation prompt

DESIGN / TECHNICAL
- Modern, clean; light mode default + dark toggle in header
- Mobile: cards stack single-column; Inter font; neutral grays + one accent
- "Export CSV" in header; local browser storage; no external API calls

NICE TO HAVE
- CSV import; sort by custom fields; bulk tag editing (if straightforward)

VERIFICATION NOTES
- Tags and color thresholds shown are defaults — user can adjust.
- Assumption: single device, no sync; flag if cross-device is needed (requires backend).
```

---

## Verification

- [ ] Person model: Name required, email format-validated, optional fields as requested.
- [ ] Cards color-coded by days-since-contact thresholds incl. a "never contacted" state.
- [ ] Search (name/company) plus tag filter and contact-status/follow-up filter present.
- [ ] Add (modal), detail, edit, "Record Contact" (sets date), and delete-with-confirm specified.
- [ ] CSV export; mobile-responsive; dark-mode toggle.
- [ ] No external API calls or implied email/calendar sync.
- [ ] No invented fields/tags beyond flagged defaults; no pipeline/account over-scope.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Fixes the app to a local-first personal CRM MVP so scope stays bounded.
- **ST-03 (Output Format Specification):** Locks the model / views / filters / technical spec into a copy-ready build brief.
- **CM-02 (Constraint Specification):** Encodes Must/Must-Not rules (no external calls, confirmed deletes, no invented fields) as explicit constraints.
- **DS-06 (Prioritization and Severity Guidance):** Color-coded urgency and follow-up filters surface the contacts that need attention first; nice-to-haves are explicitly deprioritized.
- **QA-01 (Self-Verification):** A pre-output check confirms required/validated fields, urgency states, filters, and local-first scope before emitting.

---

## Related Prompts

- `domain-software-engineering/prototyping/prototyping_inventory_tracker.md` — Same list/filter/detail/export CRUD pattern for items.
- `domain-software-engineering/prototyping/prototyping_habit_tracker.md` — Local-first data model + views + stats.
- `domain-software-engineering/prototyping/prototyping_request_management.md` — Intake + admin table with status workflow.
