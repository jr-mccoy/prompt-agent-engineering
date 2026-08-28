---
title: "Internal Request Management Tool — Public Intake + Gated Admin Workflow MVP"
category: software-engineering/prototyping
description: "Spec an internal request/ticketing tool: a public submit form, a password-gated admin dashboard with status workflow and filters, a request detail/editor with reply, and optional analytics — local-first."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DS-06
  - QA-01
difficulty: beginner
tags:
  - prototyping
  - request-management
  - ticketing
  - intake
  - app-spec
updated: "2026-06-07"
related_prompts:
  - domain-software-engineering/prototyping/prototyping_event_registration.md
  - domain-software-engineering/prototyping/prototyping_inventory_tracker.md
  - domain-software-engineering/prototyping/prototyping_personal_crm.md
---

# Internal Request Management Tool

**Objective:** Produce a build-ready spec for an internal request/ticketing tool — a public submit form that returns a request ID, a password-gated admin dashboard with a status workflow, filters and search, a request detail/editor with a reply action, and optional analytics — local-first.

**When to use:**
- IT helpdesk, design-request intake, facilities or HR inquiries.
- Any internal service desk that currently lives in scattered emails or a spreadsheet.
- A quick intake-plus-tracking tool before adopting a full ticketing platform.

**When NOT to use:**
- External customer support at scale — needs a real help-desk platform with SLAs and auth.
- Multi-team workflows with approvals and integrations — beyond MVP.
- Anything requiring real user accounts/SSO rather than a shared admin password.

**Audience:** Individuals and small teams generating apps with Lovable, Bolt, v0, or similar AI app builders.

---

## Inputs / Context

Supply the following before generating the spec:

1. **Request type** — what's being requested (IT tickets, design, facilities, etc.).
2. **Use case** — who submits and who handles them.
3. **Categories** — the dropdown options for this use case.
4. **Statuses** — defaults are New / In Progress / Waiting on Requester / Resolved / Closed; adjust as needed.
5. **Priority levels** — defaults Low/Medium/High/Urgent.
6. **Admin access** — the admin password; whether internal notes are hidden from requesters.
7. **Analytics wanted (optional)** — which charts/metrics, if any; confirm local-first persistence.

---

## Constraints

### Must
- Provide a public submit form (no auth) that validates required fields and returns a generated request ID.
- Auto-generate IDs in the given format (e.g., REQ-001) and set Date Submitted automatically.
- Gate the admin dashboard behind the provided password (entered once per session).
- Provide admin table with sort, filter (status/priority/category/assignee), search, and priority color-coding.
- Provide a detail view where status/assignee/notes/priority are editable; set Date Resolved automatically when status → Resolved; "Reply to Requester" opens a mailto draft.
- Keep internal notes out of any requester-facing view.

### Must Not
- Invent categories, statuses, or fields the user didn't provide (offer defaults, marked as such).
- Expose internal notes to requesters.
- Leave the admin dashboard ungated.
- Over-scope with real accounts/SSO, approvals, or external integrations in an MVP.

---

## Instructions

1. **Confirm scope.** Restate the request type, who submits/handles, and that persistence is local-first (flag if a backend is needed).
2. **Specify the data model.** Auto ID (given format); Title; Description; Requester name/email; Priority; Category; Status; Assigned To; Date Submitted (auto); Date Resolved (auto on Resolved); internal Notes (hidden from requester).
3. **Specify the submit view.** Clean form with required fields and dropdowns; submit → confirmation showing the request ID.
4. **Specify the admin dashboard.** Password gate; table with columns incl. Age; sort any column; filter by status/priority/category/assignee; search by ID/title/requester; row color by priority.
5. **Specify the detail view.** All fields; editable status/assignee/notes/priority; status-change timestamps if feasible; "Reply to Requester" via mailto; auto Date Resolved on Resolved; save.
6. **Specify analytics (optional).** Requests by status, average time-to-resolution, by category, over time — only if requested.
7. **Specify design + technical + access.** Functional desktop-first admin, mobile-friendly submit; clear hierarchy; local storage; CSV export; admin password once per session; no external services.
8. **Self-check before output.** Confirm: submit validates + returns ID; ID format applied; admin gated; status workflow incl. auto Date Resolved; notes hidden from requesters; filters/search present; no invented options beyond flagged defaults. Then emit the spec.

---

## False-Positive Prevention

❌ **DON'T:**
- Leave the admin dashboard accessible without the password.
- Expose internal notes in the submit/confirmation (requester-facing) views.
- Invent categories/statuses the user didn't supply without marking them defaults.
- Add real accounts/SSO, approvals, or external integrations to an MVP.
- Forget to auto-set Date Resolved when status moves to Resolved.

✅ **DO:**
- Gate the admin view; keep internal notes admin-only.
- Validate the submit form and return a generated request ID.
- Apply the given ID format and auto-stamp submitted/resolved dates.
- Offer status/category/priority defaults clearly labeled and editable.
- Scope to local-first with CSV export and a shared admin password.

---

## Output Format

```
APP: Internal Request Management — [REQUEST TYPE]
SCOPE: [local-first MVP / flag if backend needed]; submitters: [...]; handlers: [...]

DATA MODEL — Request
- ID (auto, REQ-001); Title (req); Description (req); Requester Name (req); Requester Email (req);
  Priority [Low|Medium|High|Urgent]; Category [opts]; Status [New|In Progress|Waiting on Requester|Resolved|Closed];
  Assigned To; Date Submitted (auto); Date Resolved (auto on Resolved); Notes (internal, hidden from requester)

VIEW 1 — Submit (public, /submit)
- Required fields + Priority/Category dropdowns; submit → "Your request REQ-XXX has been submitted"

VIEW 2 — Admin Dashboard (password: [PASSWORD], once/session)
- Table: ID, Title, Requester, Priority, Category, Status, Assigned To, Age
- Sort any column; Filter: Status/Priority/Category/Assignee; Search: ID/Title/Requester
- Row color by priority (Urgent red, High orange, Medium default, Low gray)

VIEW 3 — Request Detail
- All fields; editable Status/Assigned To/Notes/Priority; status-change timestamps (if feasible)
- "Reply to Requester" → mailto draft; auto Date Resolved on Resolved; Save

VIEW 4 — Analytics (optional)
- By status; avg time-to-resolution; by category; over time

DESIGN / TECHNICAL
- Functional; desktop-first admin, mobile-friendly submit; local storage; CSV export; no external services

VERIFICATION NOTES
- [assumptions / defaults flagged]
```

---

## Example Output

```
APP: Internal Request Management — IT Support Tickets
SCOPE: Local-first MVP. Submitters: all staff. Handlers: 3-person IT team.

DATA MODEL — Request
- ID: auto, REQ-001
- Title: required; Description: required (long text)
- Requester Name: required; Requester Email: required
- Priority: Low | Medium | High | Urgent
- Category: [Hardware, Software, Access/Account, Network, Other]
- Status: New | In Progress | Waiting on Requester | Resolved | Closed
- Assigned To: optional
- Date Submitted: auto; Date Resolved: auto when Status → Resolved
- Notes: internal, hidden from requester

VIEW 1 — Submit (public, homepage)
- Form: Title, Description, Requester Name, Requester Email, Priority, Category
- Submit → "Your request REQ-042 has been submitted. We'll follow up by email."

VIEW 2 — Admin Dashboard (password: ithelp2026, once per session)
- Table: ID, Title, Requester, Priority, Category, Status, Assigned To, Age (days)
- Sort any column; Filter by Status/Priority/Category/Assigned To; Search by ID/Title/Requester
- Row color: Urgent red, High orange, Medium default, Low gray

VIEW 3 — Request Detail
- All fields visible; editable: Status, Assigned To, Notes, Priority
- Status-change timestamps logged where feasible
- "Reply to Requester" opens a mailto draft to the requester's email
- Moving Status to Resolved auto-sets Date Resolved; Save persists changes

VIEW 4 — Analytics
- Requests by status (bar); average time-to-resolution; by category; volume over time

DESIGN / TECHNICAL
- Clean, usability-first; desktop admin, mobile-friendly submit form; clear CTAs
- Local storage; "Export CSV" in admin; no external services

VERIFICATION NOTES
- Categories above are placeholders — user supplies their own.
- Admin uses a shared password (not real accounts); flag if per-user auth is needed (requires backend).
```

---

## Verification

- [ ] Public submit validates required fields and returns a generated request ID.
- [ ] IDs use the given format; Date Submitted auto-set; Date Resolved auto-set on Resolved.
- [ ] Admin dashboard is password-gated (once per session).
- [ ] Admin table has sort, status/priority/category/assignee filters, search, and priority color-coding.
- [ ] Detail view edits status/assignee/notes/priority and offers reply via mailto.
- [ ] Internal notes are hidden from requester-facing views.
- [ ] Local-first with CSV export; no invented categories/statuses beyond flagged defaults.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Fixes the tool to a local-first intake-plus-tracking MVP so scope stays bounded.
- **ST-03 (Output Format Specification):** Locks the data-model / four-view / technical spec into a copy-ready build brief.
- **CM-02 (Constraint Specification):** Encodes Must/Must-Not rules (gated admin, hidden notes, ID format, no invented options) as explicit constraints.
- **DS-06 (Prioritization and Severity Guidance):** Priority levels and color-coding plus status filters triage which requests handlers see first.
- **QA-01 (Self-Verification):** A pre-output check confirms submit validation, admin gating, status workflow, and note privacy before emitting.

---

## Related Prompts

- `domain-software-engineering/prototyping/prototyping_event_registration.md` — Same public-form + gated-admin pattern.
- `domain-software-engineering/prototyping/prototyping_inventory_tracker.md` — Shared list/detail/filter/export CRUD structure.
- `domain-software-engineering/prototyping/prototyping_personal_crm.md` — Local-first record management with status/urgency views.
