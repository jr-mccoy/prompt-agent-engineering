---
title: "Multi-Format Schedule Export Correctness Audit"
category: algorithms
description: "Verify correctness of multi-format schedule export (PDF, Excel, iCal, CSV) including format-specific pitfalls, round-trip testing, and edge case handling"
tags:
  - algorithms
  - export
  - scheduling
  - pdf
  - excel
  - ical
  - csv
  - data-integrity
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - QA-01  # Chain-of-Verification
  - RT-05  # Evidence-Based Reasoning
  - DS-03  # Tool and Methodology Suggestions
difficulty: intermediate
version: "1.0"
updated: 2026-03-04
related_prompts:
  - algorithms_temporal_logic_scheduling.md
  - testing_schedule_validity_oracle.md
---

# Multi-Format Schedule Export Correctness Audit

**Objective:** Audit the correctness of schedule exports across multiple formats (PDF, Excel, iCal, CSV), identifying format-specific data integrity issues, encoding problems, and layout/semantic errors that produce files that open without error but contain wrong data.

**When to Use:** Use this prompt when a scheduling system exports to multiple formats and you need to verify that the exported data accurately represents the generated schedule. Export bugs are insidious because the file "works" (opens, renders) but contains subtle errors (wrong dates, missing assignments, timezone shifts).

**Instructions:**

### 1. Export Architecture Review

Verify the export pipeline:

```
Ideal Architecture:
Schedule (internal) → Intermediate Representation → Format-Specific Renderer
                                                    ├── PDF Renderer
                                                    ├── Excel Renderer
                                                    ├── iCal Renderer
                                                    └── CSV Renderer

Questions:
├── Is there an intermediate representation, or does each exporter
│   read the internal schedule state directly?
├── If each exporter reads internal state, are they all reading the
│   same data? (Or could one read stale data?)
└── Is the intermediate representation tested independently?
```

**Why this matters:** If each exporter independently traverses the schedule, they may disagree on what "the schedule" contains (e.g., one exporter includes unfilled slots as blank, another omits them).

### 2. PDF Export Correctness

| Check | What to Verify | Common Bug |
|-------|---------------|------------|
| Assignment accuracy | Every cell matches the schedule | Off-by-one in row/column mapping |
| Name truncation | Long names visible or clearly truncated | Name silently cut at column boundary |
| Multi-page pagination | Month boundaries paginate correctly | Last day of month on wrong page |
| Special characters | Accented names render correctly | UTF-8 → Latin-1 encoding loss |
| Print layout | Margins, orientation match specification | Landscape schedule printed in portrait |
| Date headers | Correct day-of-week labels | Header row shifts if week starts on non-Monday |

**Testing approach:**
- Generate a PDF for a known schedule, extract text with `pdfplumber` or `PyMuPDF`, and compare to expected assignments
- Include workers with non-ASCII names (Müller, O'Brien, García)
- Test with schedules spanning 1, 2, and 3+ months

### 3. Excel Export Correctness

| Check | What to Verify | Common Bug |
|-------|---------------|------------|
| Date cell types | Dates stored as date serial numbers | Dates stored as strings (no date formatting) |
| 1900 date bug | Excel's false Feb 29, 1900 | Off-by-one on all dates before Mar 1, 1900 |
| Sheet structure | Header row, data rows, summary | Missing headers or extra blank rows |
| Conditional formatting | Weekend highlighting, role colors | Formatting lost on save/reopen |
| Cell references | Formulas reference correct cells | Formulas break with varying row counts |
| Special characters | Worker names with commas, quotes | Broken cell content or CSV-like escaping |

```python
# Verification: Read back with openpyxl and compare
import openpyxl

def verify_excel_export(excel_path, expected_schedule):
    wb = openpyxl.load_workbook(excel_path)
    ws = wb.active

    for row in range(2, ws.max_row + 1):  # Skip header
        date_cell = ws.cell(row, 1).value
        assert isinstance(date_cell, datetime), f"Row {row}: date is string, not datetime"

        for col, role in enumerate(expected_schedule.roles, start=2):
            expected_worker = expected_schedule.get(date_cell.date(), role)
            actual_worker = ws.cell(row, col).value
            assert actual_worker == expected_worker, (
                f"Mismatch at {date_cell.date()}/{role}: "
                f"expected '{expected_worker}', got '{actual_worker}'"
            )
```

### 4. iCal Export Correctness

| Check | What to Verify | Common Bug |
|-------|---------------|------------|
| DTSTART format | Correct timezone (UTC `Z` suffix or `TZID`) | Timezone-naive dates shift by offset |
| VTIMEZONE block | Included when TZID is used | Missing → clients guess timezone |
| Event duration | Multi-day events use DTEND, not multiple events | Separate events for each day of a block |
| UID stability | Same schedule → same UIDs on re-export | New UIDs → duplicate events on reimport |
| RRULE absence | On-call shifts are NOT recurring events | RRULE would create phantom future shifts |
| SUMMARY format | Readable: "Main On-Call: Alice" | Cryptic: "MAIN_Alice_2025-01-06" |
| RFC 5545 compliance | Valid iCal structure | Missing `VCALENDAR`, wrong line endings |

```python
# Verification: Parse with icalendar library and compare
from icalendar import Calendar

def verify_ical_export(ical_path, expected_schedule):
    with open(ical_path, 'rb') as f:
        cal = Calendar.from_ical(f.read())

    events = [c for c in cal.walk() if c.name == 'VEVENT']

    # Check event count matches assignment count
    assert len(events) == expected_schedule.total_assignments

    # Check each event maps to a valid assignment
    for event in events:
        dtstart = event.get('dtstart').dt
        summary = str(event.get('summary'))
        # Parse role and worker from summary
        # Verify against expected_schedule
```

**Critical iCal edge cases:**
- Export a schedule spanning a DST transition — verify DTSTART is correct on both sides
- Export with timezone set to UTC vs local — verify events appear at correct times in a calendar client
- Re-export the same schedule — verify UIDs don't change (prevents duplicates)

### 5. CSV Export Correctness

| Check | What to Verify | Common Bug |
|-------|---------------|------------|
| Encoding | UTF-8 with BOM for Windows Excel | UTF-8 without BOM → garbled accented names in Excel |
| Quoting | Fields with commas/newlines quoted | Unquoted comma breaks column alignment |
| NULL handling | Empty assignments represented consistently | Some rows use `""`, others use `N/A`, others omit |
| Header row | Always present, matches data columns | Missing header or header/data column mismatch |
| Date format | ISO 8601 (YYYY-MM-DD) | Locale-dependent format (MM/DD/YYYY) |
| Line endings | Consistent (CRLF for Windows, LF for Unix) | Mixed line endings |

```python
import csv

def verify_csv_export(csv_path, expected_schedule):
    with open(csv_path, 'r', encoding='utf-8-sig') as f:  # utf-8-sig handles BOM
        reader = csv.DictReader(f)

        for row in reader:
            date = datetime.strptime(row['Date'], '%Y-%m-%d').date()
            for role in expected_schedule.roles:
                expected = expected_schedule.get(date, role)
                actual = row.get(role, '').strip()
                if expected is None:
                    assert actual in ('', 'N/A', '-'), f"Expected empty, got '{actual}'"
                else:
                    assert actual == expected, f"{date}/{role}: expected '{expected}', got '{actual}'"
```

### 6. Round-Trip Validation

For each format that supports reimport:

```
Round-Trip Test:
Schedule → Export to Format → Reimport from Format → Compare to Original

Format     Reimportable?   How to Reimport
CSV        Yes             csv.DictReader
Excel      Yes             openpyxl
iCal       Yes             icalendar library
PDF        Partially       pdfplumber text extraction (lossy)
```

```python
def test_csv_round_trip():
    schedule = generate_test_schedule()
    export_csv(schedule, "test_output.csv")
    reimported = import_csv("test_output.csv")

    for day in schedule.days:
        for role in schedule.roles:
            assert schedule.get(day, role) == reimported.get(day, role)
```

### 7. Format-Specific Edge Cases

| Edge Case | PDF | Excel | iCal | CSV |
|-----------|-----|-------|------|-----|
| Empty schedule (0 assignments) | Blank calendar | Empty sheet | Empty VCALENDAR | Header only |
| 100+ workers | Page overflow | Column limit (16384) | Many VEVENTs | Large file |
| Worker name: `O'Brien, Jr.` | Quote rendering | Cell content | SUMMARY escaping | CSV quoting |
| Worker name: `José García` | Font support | Cell encoding | UTF-8 in SUMMARY | BOM + UTF-8 |
| Schedule spans DST transition | Date labels correct | Date serials correct | DTSTART timezone | Date strings correct |
| Single-day schedule | One row/cell | One data row | One VEVENT | One data row |

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag the absence of round-trip testing for PDF as a gap — PDF is a presentation format, not a data format; lossy round-trip is expected
- Report "dates stored as strings in Excel" as always wrong — if the Excel file is read-only reference material, string dates are acceptable
- Flag CSV without BOM as a bug if the system targets Unix/Mac users — BOM is only needed for Windows Excel
- Assume all iCal clients handle VTIMEZONE correctly — test with specific target clients (Google Calendar, Outlook, Apple Calendar)

✅ **DO:**
- Verify that exported data matches the internal schedule for at least 3 spot-check dates
- Test with non-ASCII worker names in every format
- Verify round-trip for CSV and Excel (the two reimportable formats)
- Check that the export produces the same output for the same input (deterministic)

## Expected Output

1. **Architecture Assessment** — Intermediate representation usage and data consistency
2. **Per-Format Audit** — Findings table for each format with specific code references
3. **Round-Trip Results** — Pass/fail for CSV and Excel round-trips
4. **Edge Case Matrix** — Results for each edge case across all formats
5. **Recommendations** — Prioritized fixes with estimated effort

## Quality Checklist

- [ ] Each format tested with non-ASCII worker names
- [ ] CSV and Excel round-trip tests pass
- [ ] iCal exports validated against RFC 5545
- [ ] At least one multi-month schedule tested in PDF
- [ ] Export determinism verified (same input → same output)

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focuses on export correctness across formats
- **ST-02** (Structured Sequential Instructions) — Systematic per-format audit
- **RT-02** (Multi-Dimensional Analysis) — Covers PDF, Excel, iCal, CSV, and cross-format concerns
- **QA-01** (Chain-of-Verification) — Round-trip validation as self-check
- **RT-05** (Evidence-Based Reasoning) — Requires specific code paths and comparison data
- **DS-03** (Tool and Methodology Suggestions) — Recommends verification libraries per format

## Related Prompts

- `algorithms_temporal_logic_scheduling.md` — Date/timezone handling that affects exports
- `testing_schedule_validity_oracle.md` — Validates the schedule before export
- `quality_yaml_configuration_schema_validation.md` — Config that drives export format options
