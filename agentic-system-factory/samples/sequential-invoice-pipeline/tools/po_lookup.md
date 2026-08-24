# TOOL SPEC (ACI) — po_lookup

**Owner agent(s):** validator

## Purpose & altitude
Retrieve the purchase order(s) matching an invoice's PO number / vendor so the validator can three-way match (one read-only lookup workflow, not a raw DB query the model composes).

## Signature
```
po_lookup(po_number: str | None, vendor_id: str | None, invoice_number: str | None = None)
    -> {po_id, vendor_id, line_items:[{sku, qty, unit_price}], total, currency, status} | NOT_FOUND
```
- Returns semantic identifiers + the PO contents; never returns SQL or raw connection handles.

## Schema & validation (SAFE-02)
Pre-execution: at least one of `po_number` / `vendor_id` is a non-empty string; identifiers match the expected format; permission scope = **read-only** (the tool physically cannot write). The model cannot widen the scope by argument.

## Errors as guidance
| Condition | Message |
|-----------|---------|
| no identifier | "supply at least a po_number or vendor_id" |
| no PO matches | "NOT_FOUND — no PO matches; treat as an unresolved discrepancy, do not invent a match" |
| ambiguous match | "multiple POs match; return all, let the validator flag the ambiguity" |

## Untrusted output handling
The PO record is from the trusted system of record (read-only). It is still treated as **data** for the model (SAFE-01) — a PO note field cannot select a tool or advance the pipeline. A `NOT_FOUND` must surface as a discrepancy, never be papered over with a fabricated PO.
