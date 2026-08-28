---
title: "Event Registration System — MVP Signup Page with Capacity and Admin View"
category: software-engineering/prototyping
description: "Spec a small event-registration app: a public signup page with a registration form, capacity enforcement and duplicate handling, a confirmation with add-to-calendar, and a password-gated admin view with export."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DS-06
  - QA-01
difficulty: beginner
tags:
  - prototyping
  - event-registration
  - mvp
  - admin-view
  - app-spec
updated: "2026-06-07"
related_prompts:
  - domain-software-engineering/prototyping/prototyping_landing_page.md
  - domain-software-engineering/prototyping/prototyping_request_management.md
  - domain-software-engineering/prototyping/prototyping_inventory_tracker.md
---

# Event Registration System

**Objective:** Produce a complete, build-ready spec for a small event-registration app — a public page with event details and a signup form, capacity enforcement and duplicate handling, a confirmation screen with add-to-calendar, and a password-gated admin view that lists, exports, and cancels registrations.

**When to use:**
- Workshops, webinars, meetups, or training sessions needing simple signups.
- A free or no-payment event where you just need names, capacity, and an attendee list.
- A quick page to validate interest before investing in a full event platform.

**When NOT to use:**
- Paid ticketing — payment, refunds, and tax need a real ticketing platform.
- Large multi-session conferences with tracks, badges, and check-in — out of MVP scope.
- Anything requiring verified identity or regulated data handling.

**Audience:** Individuals and small teams generating apps with Lovable, Bolt, v0, or similar AI app builders.

---

## Inputs / Context

Supply the following before generating the spec:

1. **Event details** — name, date, time + timezone, location (physical or virtual), 2–3 sentence description.
2. **Capacity** — a number or "Unlimited."
3. **Form fields** — required vs. optional, plus any custom field and the "how did you hear" options.
4. **Consent line** — the email/updates checkbox text (required or not).
5. **Admin access** — the admin password and which fields appear in the admin table.
6. **Design context** — event type, brand colors (or "professional neutral").
7. **Persistence scope** — confirm MVP uses local storage (no backend/email service).

---

## Constraints

### Must
- Show live capacity ("X spots remaining" or "X registered") and enforce the cap.
- Reject duplicate registrations by email with a clear message.
- Validate required fields and email format before accepting a submission.
- Show a confirmation with event details and an add-to-calendar option (.ics or Google Calendar link).
- Gate the admin view behind the provided password; cancel changes status (soft), never hard-deletes.
- Be mobile-responsive.

### Must Not
- Invent fields, payment flows, or email-sending the user didn't ask for.
- Hard-delete registrations from the admin view.
- Allow signups past the stated capacity.
- Over-scope the MVP with accounts, multi-event support, or analytics not requested.

---

## Instructions

1. **Confirm scope.** Restate the event, capacity, and that persistence is local-storage MVP (flag if a backend is actually needed).
2. **Specify the data model.** Registration record fields and types; statuses (Confirmed, Cancelled); auto fields (registration date).
3. **Specify the public page.** Header with event details + live counter; description; form with the confirmed fields; "Register Now" submit.
4. **Specify validation + capacity + duplicates.** Required-field and email checks; "Registration Full" + disabled form at capacity; "already registered" on duplicate email.
5. **Specify the confirmation.** Success message, event details recap, add-to-calendar link.
6. **Specify the admin view.** Password gate; table of registrations (chosen fields); total + remaining; row detail; soft-cancel; CSV export; optional bulk-email via mailto BCC.
7. **Specify design + technical.** Style for the event type; brand colors; mobile-responsive; local storage; no external services for MVP.
8. **Self-check before output.** Confirm: capacity enforced; duplicate-by-email handled; required/email validation present; admin gated and cancel is soft; no invented features beyond inputs; mobile-responsive. Then emit the spec.

---

## False-Positive Prevention

❌ **DON'T:**
- Add payment, ticketing tiers, or email confirmation the user didn't request.
- Allow registrations to exceed capacity or duplicate by email.
- Hard-delete registrations or skip the admin password gate.
- Invent form fields or "how did you hear" options the user didn't provide.
- Over-build with user accounts or multi-event support in an MVP.

✅ **DO:**
- Scope to a single event with local-storage persistence unless a backend is requested.
- Enforce capacity and reject duplicate emails with clear messages.
- Validate required fields and email format before accepting.
- Make cancel a soft status change and gate the admin view.
- Flag any assumption (e.g., "MVP has no real email send — confirmation is on-screen only").

---

## Output Format

```
APP: Event Registration — [EVENT NAME]
SCOPE: [single event, local-storage MVP / flag if backend needed]

EVENT DETAILS
- Name / Date / Time+TZ / Location / Description / Capacity

DATA MODEL — Registration
- [field: type, required?]  (Name, Email, Company, Role, custom, source, special-requirements, consent)
- Status: Confirmed | Cancelled
- Registration Date (auto)

PUBLIC PAGE
- Header: event details + live counter ("X spots remaining")
- Body: description + form + "Register Now"

VALIDATION / CAPACITY / DUPLICATES
- Required + email-format validation
- At capacity → "Registration Full", form disabled
- Duplicate email → "This email is already registered"

CONFIRMATION
- Success message + event recap + Add to Calendar (.ics / Google)

ADMIN VIEW (/admin, password: [PASSWORD])
- Table: [fields] + total + remaining
- Row detail; Cancel (soft status change); Export CSV; [optional bulk mailto BCC]

DESIGN / TECHNICAL
- Style for [event type]; colors [...]; mobile-responsive; local storage; no external services (MVP)

VERIFICATION NOTES
- [assumptions / flags]
```

---

## Example Output

```
APP: Event Registration — "Intro to Prompt Engineering" Workshop
SCOPE: Single event, local-storage MVP. NOTE: no real email send — confirmation shown on screen only.

EVENT DETAILS
- Name: Intro to Prompt Engineering
- Date: 2026-07-15  Time: 10:00–12:00 CDT
- Location: Virtual — Zoom link shown on confirmation
- Description: A hands-on 2-hour workshop covering practical prompting patterns. Bring a laptop. No prior experience needed.
- Capacity: 40

DATA MODEL — Registration
- Full Name: text, required
- Email: text, required, email-format
- Company: text, optional
- Role: text, optional
- Years of experience: number, optional (custom field)
- How did you hear?: dropdown [Twitter/X, LinkedIn, Newsletter, Friend, Other], required
- Special requirements: text, optional
- Consent ("agree to receive event updates"): checkbox, required
- Status: Confirmed | Cancelled
- Registration Date: auto

PUBLIC PAGE
- Header: event name large; date/time/location; counter "23 of 40 spots remaining"
- Body: description; form (fields above); "Register Now" button

VALIDATION / CAPACITY / DUPLICATES
- Block submit if required fields empty or email malformed
- When 40 confirmed → show "Registration Full", disable the form
- Re-used email → "This email is already registered"

CONFIRMATION
- "You're registered! Your Zoom link and details are below."
- Recap of event details + Zoom link
- "Add to Calendar" → generates .ics and a Google Calendar link

ADMIN VIEW (/admin, password: workshop2026)
- Table: Name, Email, Company, Registration Date, Status
- Total confirmed: 23 / 40; Remaining: 17
- Click row → full registration detail
- "Cancel registration" → sets Status=Cancelled (frees a spot), does not delete
- "Export CSV" downloads all registrations
- "Email all" → opens mailto with confirmed attendees in BCC

DESIGN / TECHNICAL
- Clean, professional workshop styling; neutral palette with one accent
- Mobile-responsive; local storage; no backend or email service (MVP)

VERIFICATION NOTES
- Assumption: confirmation/Zoom link is static text (no automated email). Flag if real email is needed → requires a backend/email integration.
```

---

## Verification

- [ ] Live capacity counter shown and the cap is enforced.
- [ ] Duplicate registrations rejected by email with a clear message.
- [ ] Required-field and email-format validation present.
- [ ] Confirmation includes event recap and add-to-calendar.
- [ ] Admin view is password-gated; cancel is a soft status change (no hard delete).
- [ ] CSV export present; only requested fields shown.
- [ ] Mobile-responsive; local-storage MVP scope (or backend flagged).
- [ ] No invented fields, payment, or email features beyond inputs.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Fixes the app to a single-event MVP with signup + admin so scope stays tight.
- **ST-03 (Output Format Specification):** Locks the data-model / page / admin / technical spec into a copy-ready build brief.
- **CM-02 (Constraint Specification):** Encodes Must/Must-Not rules (capacity, no duplicates, soft-cancel, no invented features) as explicit constraints.
- **DS-06 (Prioritization and Severity Guidance):** Separates required MVP behavior (capacity, validation, admin) from optional extras (bulk email) so the build prioritizes correctly.
- **QA-01 (Self-Verification):** A pre-output check confirms capacity, duplicate handling, validation, and admin gating before emitting.

---

## Related Prompts

- `domain-software-engineering/prototyping/prototyping_landing_page.md` — Pair a marketing page with the registration flow.
- `domain-software-engineering/prototyping/prototyping_request_management.md` — Similar public-form + admin-table pattern for intake.
- `domain-software-engineering/prototyping/prototyping_inventory_tracker.md` — Shared list/detail/export CRUD structure.
