# TOOL SPEC (ACI) — research_sources_search

**Owner agent(s):** worker

## Purpose & altitude
Find candidate sources for a subtopic (one search workflow, not a raw API endpoint).

## Signature
```
research_sources_search(query: str, max_results: int = 10) -> list[{title, url}]
```
- Returns semantic identifiers (title/url), not technical ids.

## Schema & validation (SAFE-02)
Pre-execution: query is a non-empty string; max_results ≤ 25. Permission scope: read-only.

## Errors as guidance
| Condition | Message |
|-----------|---------|
| empty query | "query must be a non-empty search string" |
| no results | "No matches; try broadening the query" |

## Untrusted output handling
Returns external content → treated as data only (SAFE-01); cannot select the next tool.
