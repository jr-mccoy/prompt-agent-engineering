# DISCLOSURE MANIFEST — marketing-copy-evaluator-optimizer

**Version:** 1.0 · **Date:** 2026-06-20

## 1. Product Overview
<!-- DISCLOSURE-DIM-1: complete -->
An evaluator-optimizer system that, given a product brief and brand rules, produces marketing copy and iteratively revises it until an independent critic passes it against a fixed three-dimension rubric (on-brand voice, factual-claims-substantiation, length/format) or a round cap is reached. Intended for marketers who want a draft pre-checked against brand and claims constraints. Out of scope: publishing the copy, image generation, sourcing live facts, legal sign-off.

## 2. Company & Accountability
<!-- DISCLOSURE-DIM-2: complete -->
Maintainer: (sample) marketing-tools team. Incident contact: (sample). Update cadence: monthly. Owner of the brand-rules pack and rubric definition is the brand team; changes to either are versioned.

## 3. Technical Capabilities & System Architecture
<!-- DISCLOSURE-DIM-3: complete -->
Topology TP-07 (evaluator-optimizer). Two roles: a generator agent (writes/revises copy) and a critic/evaluator agent (scores against the rubric, emits a deterministic per-dimension verdict). No external tools — both operate purely on in-context content (brief + brand rules + current draft). A loop driver holds the current draft, round counter, and best-scoring draft. Strong model for both roles.

## 4. Autonomy & Control
<!-- DISCLOSURE-DIM-4: complete -->
Acts (rewrites copy across rounds), recommends-only on the final draft (a human ships it). Authority boundary: read-only by construction — no write/exec/fetch/spend/message tools exist. Kill switch: `config.halt`. Loop bounds: MAX_ROUNDS = 4 with a cap-fallback that returns the best-scoring draft flagged `did_not_converge`.

## 5. Ecosystem Interaction
<!-- DISCLOSURE-DIM-5: complete -->
Touches nothing external: no network, no files, no third-party services. Inputs are supplied in-context; output is returned to the caller. Inter-agent trust: generator and critic never message each other; they communicate only via the loop driver's validated state. Identity: per-round traced identities for generator and critic.

## 6. Safety, Evaluation & Impact
<!-- DISCLOSURE-DIM-6: complete -->
Capability eval (ABC-valid) run on a held-out brief set with a round-1-vs-final baseline showing the loop improves rubric scores. Safety eval run benign + adversarial against the real content-risk surface (fabricated claims, injected false claims from untrusted source text, off-brand content): the system ships zero unsubstantiated claims, the critic catches injected false claims, and off-brand drafts are never returned as passed; non-converging briefs are returned flagged, never silently shipped. Residual risk: a subtle on-brand-but-misleading claim that traces to an ambiguous brief line; mitigated by the three-layer claims defense (generator self-check + independent critic + final guardrail) and human ship-time review. Rollback: disable the loop (`config.halt`) and fall back to single-shot generation with a manual editor pass.

## Completeness check
- [x] No dimension left blank (including #6).
- [x] Safety section reports evals actually run against the content-risk surface.
- [x] Cross-links to the eval harness (this run's capability + safety results) and the runbook rollback.
