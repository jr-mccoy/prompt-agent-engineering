# Proposed technique cluster — Irreversible / High-Blast-Radius Action Gating

**Provenance:** Session-3 mining (brief-03, T11 irreversible-action gating). Ledger C29–C40.
**Home:** extends the existing **Gate/Approval family**, which today is thin and abstract
(QA-08 gate-based verification, DP-05 stakes-based gate policy, AG-02 skeptical default). This adds
the concrete *prompt-level action-gate* mechanisms that family lacks. Cross-link to the existing
reversibility-assessment aid ("Can this be undone?") and `domain-decision-making/tradeoff_reversibility_stakes_grid.md`.

**Dedup verdict:** cluster is NEW. Adjacent-but-distinct: DP-05 (gate *policy* scales with risk),
AG-02 (skeptical default), the "friction vs capability-removal" *security* control-eval (a different
lens — adversary resistance, not user-experience ceiling). None names these mechanisms.

**Framing principle:**
> *For an action that is trivial to perform and impossible to undo, the design is entirely in the
> safeguards. Uncertainty resolves toward HALT, never toward the action — and the gate specifies its
> **maximum** friction as explicitly as its minimum, so it can neither be fired by accident nor rot
> into uselessness.*

---

## Core mechanisms (catalog-absent; assign real IDs at ingestion)

1. **Phase-gated action cycle** — the consequential call is legal *only* as the final step of a
   fixed sequence (Scope → Preview → Confirm → Recheck → Commit → Verify), never reachable by
   shortcut. *Generalizes to any prompt with a costly action.*
2. **Manifest-bound commit** — act on the *enumerated artifact* the user approved (an explicit ID
   list), never on a re-evaluated query or description. This is the *structural* TOCTOU fix: late
   matches are unreachable because the query is never re-run. *Ex: commit `ids=[...]`, never `filter=...`.*
3. **Nonce-bound confirmation** — each preview issues a short code the confirmation must quote; any
   new preview voids prior codes. CSRF-token thinking applied to conversational approval. *Ex:
   `DELETE 47 PERMANENTLY — CODE Q7XA`. (Anti-replay/anti-confusion within the conversation, not cryptographic.)*
4. **Confirm+modify = modify** — a message that both approves and changes scope counts *only* as a
   change; approval and modification never co-travel. *Ex: "confirmed, also add the drafts" → new cycle, nothing fires.*
5. **Freshness with enumerated disarm events** — approval has a TTL and a *defined list* of voiding
   events (scope change, mutating op, message-count cap, tool error, expressed second thoughts), with
   scope-neutral clarifying questions explicitly exempt. *Prevents both stale-approval firing and question-punishing.*
6. **Pre-commit recheck (TOCTOU guard)** — re-verify the exact target set against live state
   immediately before firing; any drift → back to preview with a diff.
7. **Blast-radius tripwires + comprehension echo** — defined thresholds (count, "all," negation/
   wildcard) add *exactly one* extra check: the user restates the scope in their own words. Tests
   **comprehension, not compliance** — the sharp part. *Ex: N≥100 → "in one sentence, what will this delete?"*
8. **Friction budget / ceiling** — the gate specifies its *maximum* friction as explicitly as its
   minimum: one preview, one confirmation, no re-asks, every HALT names its single unblocking action.
   *Fable's pick for most-worth-stealing, and it directly serves the "don't rot into over-cautious
   uselessness" goal. Also promote as a standards-level tightening (see below).*
9. **Flag-once-then-defer** — the model may voice a concern *exactly once*, before confirmation;
   afterward the informed user's decision governs. *Respects autonomy; anti-relitigation.*
10. **No advance / conditional / scheduled authorization** — blanket or pre-committed approval is
    invalid by definition; approval exists only *after* a preview and *contemporaneous* with commit.
11. **Post-action reconciliation & disclosure** — compare intended vs. actual, lead with any
    discrepancy, never imply undo exists. *Ex: "requested 47, deleted 46, failed r_1082 (locked) — permanent."*

## Overlaps with prior sessions (do NOT double-count)
- **Channel separation for authority** (this session's #10) == **C26 data-instruction quarantine**
  (Session 2). It re-surfaced here — a *recurrence signal* that it's a core cross-cutting technique.
  MERGE into C26; cite it in both the inter-prompt family and this cluster.
- **Verify-not-retry on ambiguity** relates to Session-2 error-propagation + idempotency; cite, don't re-mint.
- **Verbatim-figures / reporting integrity** == house-style evidence-or-drop / source anchoring. MERGE/relate.

## Standards-level promotion (asset type 3)
**Friction ceiling** (#8) generalizes beyond action gates to *every* guardrail/safeguard prompt:
> *A safeguard must specify its maximum friction as explicitly as its minimum. Name the cap (how
> many confirmations, how many flags) and require every halt to name its exit. A gate that specifies
> only its floor ends up either bypassed or unbearable.*
This is the concrete, enforceable form of house-style move 5 (proportionality) + the QA-20 unhelpful-
failure guard, and it directly targets over-cautious output. Add to `PROMPT_QUALITY_STANDARDS.md`.

## Exemplar (asset type 4)
The "Permanent Record Deletion Operator" prompt is a high-quality, honest reference for action-gating
prompts (it even states its residuals: gate forces *exposure* to evidence, not *comprehension*; a
model can't notarize its own fidelity; injection/tool-shape are soft and belong in the tool layer).
Ship as an exemplar under `domain-prompt-engineering/` or the agent-safety area.

## Honest novelty note
Fable again flagged most as ports (state machines, two-phase commit, CSRF tokens, TOCTOU guards,
idempotency, reconciliation) — standard in systems engineering, absent in the prompt catalog. The
nearer-to-novel: nonce-bound conversational confirmation (3), confirm+modify=modify (4), the
comprehension echo (7), and the friction ceiling (8). Novel *for this catalog*.

## Operating-model signal
Second new-shape tension (after T7) to yield a *cluster*, not a technique — the pattern holds.
First **cross-session recurrence** appeared (channel separation, S2→S3): recurrence flags a core
cross-cutting technique AND is an early saturation signal for that specific mechanism. T18
(resumable state) is the remaining new-shape cell; likely another cluster.
