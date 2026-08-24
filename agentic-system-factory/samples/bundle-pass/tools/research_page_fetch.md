# TOOL SPEC (ACI) — research_page_fetch

**Owner agent(s):** worker

## Purpose & altitude
Fetch the readable text of one source URL (read-only).

## Signature
```
research_page_fetch(url: str) -> {url, text}
```

## Schema & validation (SAFE-02)
Pre-execution: url matches https scheme allowlist; domain not on denylist. Permission scope: read-only fetch. No write/exec capability.

## Errors as guidance
| Condition | Message |
|-----------|---------|
| non-https url | "url must use https; you passed a non-https scheme" |
| blocked domain | "Domain is on the denylist; choose another source" |

## Safety for state-modifying tools
N/A — read-only, no side effects, idempotent.

## Untrusted output handling
Returns external page content → data only (SAFE-01); the text is wrapped as a document block and never interpreted as instructions.
