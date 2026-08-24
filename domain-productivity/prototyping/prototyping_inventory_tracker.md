---
title: "Inventory / Asset Tracker — Item CRUD with Filters, Reports, and CSV"
category: productivity/prototyping
description: "Spec a simple inventory/asset tracker: an item data model, a searchable/filterable grid-or-table list, add/edit/detail flows, optional bulk actions, reports/stats, CSV import/export — local-first."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DS-06
  - QA-01
difficulty: beginner
tags:
  - prototyping
  - inventory
  - asset-tracking
  - crud
  - app-spec
updated: "2026-06-07"
related_prompts:
  - domain-productivity/prototyping/prototyping_personal_crm.md
  - domain-productivity/prototyping/prototyping_request_management.md
  - domain-productivity/prototyping/prototyping_habit_tracker.md
---

# Inventory / Asset Tracker

**Objective:** Produce a build-ready spec for a simple inventory/asset tracker — an item data model, a searchable and filterable list (grid or table), add/edit/detail flows, optional bulk actions, a reports/stats section, and CSV import/export — local-first and offline-capable.

**When to use:**
- Tracking office equipment, tools, books, or a small warehouse's stock.
- Personal collections you want searchable with status and location.
- A quick asset register before adopting a heavier inventory system.

**When NOT to use:**
- Real-time multi-location inventory with barcode scanning and POS integration — needs a real system.
- Multi-user concurrent editing — local-first MVP has no sync/locking.
- Regulated asset tracking requiring audit trails and identity — out of MVP scope.

**Audience:** Individuals and small teams generating apps with Lovable, Bolt, v0, or similar AI app builders.

---

## Inputs / Context

Supply the following before generating the spec:

1. **What you're tracking** — item type (equipment, books, stock, etc.).
2. **ID format** — prefix and numbering (e.g., EQ-001).
3. **Categories and locations** — dropdown options (or note they're free-text/dynamic).
4. **Status values** — defaults are Available / In Use / Maintenance / Retired; adjust as needed.
5. **Quantity / value tracking** — whether quantity and price matter (enables low-stock + total-value).
6. **Scale** — expected number of items (informs list performance choices).
7. **Access** — open or a simple password; confirm local-first persistence.

---

## Constraints

### Must
- Define an item model with auto ID (per the given format), required Name, and the requested optional fields.
- Provide search (name/description/ID) and filters (category, location, status).
- Support add, edit, detail, duplicate (new ID), and delete-with-confirmation.
- Provide a reports section (counts, breakdowns; total value and low-stock only if quantity/price are tracked).
- Support CSV export, and CSV import with a downloadable template.
- Be local-first and usable on desktop and mobile.

### Must Not
- Invent categories, locations, statuses, or fields the user didn't provide (offer defaults, marked as such).
- Show total-value or low-stock features when price/quantity aren't tracked.
- Delete without confirmation, or lose data on duplicate.
- Over-scope with barcode scanning, multi-user sync, or POS in an MVP.

---

## Instructions

1. **Confirm scope.** Restate the item type, scale, and that persistence is local-first (flag if a backend is needed).
2. **Specify the data model.** Auto ID format; Name (required); optional fields (description, category, location, status, quantity, assigned-to, purchase date/price, notes, image URL); auto date-added/last-updated.
3. **Specify the main list.** Grid/table toggle; color-code by status; search; filters by category/location/status; sortable columns in table.
4. **Specify add/edit + detail.** Form with all fields and image-URL preview; quick-add; detail view with edit/duplicate/delete(confirm).
5. **Specify bulk actions (optional).** Multi-select; bulk status/location update; bulk delete (confirm).
6. **Specify reports.** Total count; breakdown by category (chart) and status; total value and low-stock alert only when price/quantity are tracked.
7. **Specify import/export + design + technical.** CSV export; CSV import with template; print view; clean functional UI; desktop-focused but mobile-usable; local storage; offline; optional password; tuned for the stated scale.
8. **Self-check before output.** Confirm: ID format applied; search + all filters present; duplicate assigns a new ID; delete confirms; value/low-stock gated on price/quantity; no invented options beyond flagged defaults. Then emit the spec.

---

## False-Positive Prevention

❌ **DON'T:**
- Add barcode scanning, POS, or multi-user sync to an MVP.
- Invent specific categories/locations/statuses the user didn't supply without marking them defaults.
- Show total value or low-stock alerts when price/quantity aren't tracked.
- Allow delete without confirmation or let duplicate reuse an existing ID.
- Build only for desktop when mobile lookups are likely.

✅ **DO:**
- Scope to local-first, single-user CRUD with CSV import/export.
- Apply the given ID format and require only Name.
- Gate value/low-stock features on whether price/quantity exist.
- Confirm destructive actions and assign new IDs on duplicate.
- Offer defaults clearly labeled and easy to replace.

---

## Output Format

```
APP: Inventory / Asset Tracker — [WHAT YOU'RE TRACKING]
SCOPE: [local-first MVP / flag if backend needed]; ~[N] items

DATA MODEL — Item
- ID (auto, [PREFIX]-001); Name (required); Description; Category [opts]; Location [opts];
  Status [Available|In Use|Maintenance|Retired]; Quantity; Assigned To; Purchase Date; Purchase Price;
  Notes; Image URL; Date Added (auto); Last Updated (auto)

MAIN LIST
- Grid/Table toggle; color-code by status
- Search: name/description/ID; Filters: category, location, status; sortable table columns

ADD/EDIT + DETAIL
- Form (all fields, image preview); Quick Add
- Detail: Edit / Duplicate (new ID) / Delete (confirm)

BULK ACTIONS (optional)
- Multi-select; bulk status/location; bulk delete (confirm)

REPORTS
- Total count; by category (chart); by status
- [if price/quantity tracked] total value; low-stock alert (quantity < [THRESHOLD])

IMPORT/EXPORT
- CSV export; CSV import (+ template); print view

DESIGN / TECHNICAL
- Clean functional UI; desktop-focused, mobile-usable; local storage; offline; [optional password]

VERIFICATION NOTES
- [assumptions / defaults flagged]
```

---

## Example Output

```
APP: Inventory / Asset Tracker — Office Equipment
SCOPE: Local-first MVP; ~300 items.

DATA MODEL — Item
- ID: auto, format EQ-001
- Name: required
- Description: optional
- Category: [Laptop, Monitor, Phone, Furniture, Peripheral]
- Location: [HQ-Floor1, HQ-Floor2, Remote, Storage]
- Status: Available | In Use | Maintenance | Retired
- Quantity: number, default 1
- Assigned To: optional (person/department)
- Purchase Date / Purchase Price: optional
- Notes: optional long text
- Image URL: optional (preview on paste)
- Date Added / Last Updated: auto

MAIN LIST
- Grid (cards: image, name, category, status, location) / Table toggle
- Status color-coding: Available green, In Use blue, Maintenance amber, Retired gray
- Search: name/description/ID; Filters: Category, Location, Status; sortable table columns

ADD/EDIT + DETAIL
- Form with all fields + image-URL preview; "Quick Add" from the list
- Detail view: Edit; Duplicate (creates EQ-### with a new ID); Delete (confirm dialog)

BULK ACTIONS
- Multi-select rows; bulk-set Status or Location; bulk delete (confirm)

REPORTS
- Total items: 287
- By category: bar chart; By status: counts
- Total value: sum of Purchase Price where present (price IS tracked → shown)
- Low-stock alert: items with Quantity < 3 (quantity IS tracked → shown)

IMPORT/EXPORT
- Export all to CSV; Import from CSV with a downloadable template; Print view (paper-formatted)

DESIGN / TECHNICAL
- Clean, scannable UI; desktop-focused, mobile-usable; local storage; offline; no password needed

VERIFICATION NOTES
- Categories/locations above are placeholders — user supplies their own.
- Value + low-stock features shown because price and quantity are tracked; they'd be hidden otherwise.
```

---

## Verification

- [ ] Item model uses the given ID format; only Name is required.
- [ ] Search (name/description/ID) and all three filters (category/location/status) present.
- [ ] Add, edit, detail, duplicate (new ID), delete-with-confirm specified.
- [ ] Reports include counts/breakdowns; value + low-stock only when price/quantity tracked.
- [ ] CSV export and CSV import (with template) present.
- [ ] Local-first, offline, desktop + mobile usable.
- [ ] No invented categories/locations/statuses beyond flagged defaults.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Fixes the app to a local-first item-CRUD MVP so scope stays bounded.
- **ST-03 (Output Format Specification):** Locks the model / list / detail / reports / import-export spec into a copy-ready build brief.
- **CM-02 (Constraint Specification):** Encodes Must/Must-Not rules (ID format, confirmed deletes, value features gated on data, no invented options) as constraints.
- **DS-06 (Prioritization and Severity Guidance):** Separates core CRUD from optional bulk actions and conditional reports so the build prioritizes essentials.
- **QA-01 (Self-Verification):** A pre-output check confirms ID format, filters, duplicate/delete behavior, and gated reports before emitting.

---

## Related Prompts

- `domain-productivity/prototyping/prototyping_personal_crm.md` — Same list/filter/detail/export CRUD pattern for people.
- `domain-productivity/prototyping/prototyping_request_management.md` — Intake + admin table with status workflow.
- `domain-productivity/prototyping/prototyping_habit_tracker.md` — Local-first data model + views + stats.
