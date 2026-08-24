# DISCLOSURE MANIFEST — deep-research-fleet

**Version:** 1.0 · **Date:** 2026-06-20

## 1. Product Overview
<!-- DISCLOSURE-DIM-1: complete -->
A deep-research assistant that, given a question, returns a synthesized, fully-cited answer from web sources. Intended for users who need a verifiable sourced first draft. Out of scope: anything behind auth, real-time data, taking external action.

## 2. Company & Accountability
<!-- DISCLOSURE-DIM-2: complete -->
Maintainer: (sample) research-tools team. Incident contact: (sample). Update cadence: monthly.

## 3. Technical Capabilities & System Architecture
<!-- DISCLOSURE-DIM-3: complete -->
Topology TP-06 (orchestrator-workers). Agents: orchestrator, N workers, synthesizer. Tools: read-only search + fetch (MCP-optional). Strong model for orchestrator/synthesizer; mid for workers. External state store for resumable runs.

## 4. Autonomy & Control
<!-- DISCLOSURE-DIM-4: complete -->
Acts (browse/fetch), recommends-only on conclusions. Authority boundary: read-only fetch; no write/exec/spend/message tools exist. Kill switch: `config.halt`. Loop bounds: MAX_WORKERS, MAX_FETCHES, decomposition rounds.

## 5. Ecosystem Interaction
<!-- DISCLOSURE-DIM-5: complete -->
Touches: the public web (read-only) + a search provider. Inter-agent trust: star topology, no peer channel. Identity: per-worker traced identity; no credential caching.

## 6. Safety, Evaluation & Impact
<!-- DISCLOSURE-DIM-6: complete -->
Capability eval (ABC-valid) run on 20 held-out questions with a trivial-agent baseline. Safety eval (real-tool, OpenAgentSafety categories 3/6/8 — the system's real surface) run benign + adversarial: no non-allowlisted action; injected links never surfaced as sources. Residual risk: novel injection phrasings; mitigated by the deterministic allowlist (worst case is a fetch we'd have allowed). Rollback: disable fleet, fall back to single-agent search.

## Completeness check
- [x] No dimension left blank (including #6).
- [x] Safety section reports evals actually run.
- [x] Cross-links to risk register + this run's eval results.
