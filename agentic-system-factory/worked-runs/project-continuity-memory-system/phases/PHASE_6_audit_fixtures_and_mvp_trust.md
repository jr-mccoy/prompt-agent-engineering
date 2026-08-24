# Phase 6 — `continuity audit`, Full Fixtures & MVP-Trust (19b) 🚩

| | |
|---|---|
| **Phase** | 6 of 10 |
| **Prerequisites** | Phases 1–5 done |
| **Plan sections** | §15 (security/privacy controls), §16 (validation + the audit/heuristic note), §17 (full fixture suite), §19b (MVP-trust acceptance), §20 tasks 12–13 |
| **Ships** | 🚩 **MVP-trust (19b)** — `audit` + the full Fixtures 2–10 in CI. The memory becomes *trustworthy*, not just usable. |
| **Session size** | Medium–large |

---

## Objective

Add the heuristic safety net (`audit`) that `validate`'s determinism intentionally excludes, and complete the evaluation suite so the whole MVP is CI-guarded. After this phase the tool meets the full §19 acceptance list.

## Scope

**In:**
- `continuity audit` (§10, §15, §16 note): stale/unsafe/bloated memory detection — heuristics that **don't** gate `validate`.
- Secret scan (Fixture 6) — token-like strings in memory fail audit / `scan-secrets` (§15, §17.6).
- Instruction-like text heuristic (Fixture 7) — lexical scan for override phrasing ("ignore", "skip", "disable", "always", "never run") → warn (§16 note, §17.7).
- Generated-packet drift (Fixture 8) — source record newer than packet → flag regeneration (§15, §17.8).
- Branch mismatch, missing evidence, invalid status, private-path violation surfaced in audit (§19b.9).
- Fixtures 6–10 + run **all** Fixtures 1–10 in CI (§17, §19b.11).

**Out:**
- Hard CI/pre-commit *enforcement* of high-impact review (plan §22 Q6) — decide policy here; implementing the enforcement mechanism is Phase 9 (hooks/adapters). For now audit *flags* high-impact changes.

## Tasks

### A. `audit` core (plan §10, §15, §16 note, §20.12)
1. Load all memory + manifest; read tracking policies (don't guess — §7).
2. **Staleness/health flags:** stale handoff (age + commit-distance, reuse Phase 4), aged-unresolved questions/decisions, expired records, low-confidence-without-evidence, oversized `sessions/` growth note (forward-ref §22 Q7 / Phase 10 rollup).
3. **Missing evidence / invalid status / private-path violation:** surface (these also fail `validate`, but audit reports them in the health view — §19b.9).
4. **Bloat:** adapter files duplicating full memory content (§16.13); packet over budget.

### B. Secret scan (plan §15, §17.6, Fixture 6)
5. `scan-secrets` (and as an audit sub-check): regex set for common secret shapes (API keys, tokens, PEM headers, high-entropy strings, `password=`/`secret=` assignments). Memory containing a token-like string → audit **fails** (non-zero) and points to the offending record/line.
6. Document that this must run **before** any "commit memory" recommendation (§2.6, §15).

### C. Instruction-like heuristic (plan §16 note, §17.7, Fixture 7)
7. Lexical scan of `known-traps.md` and record bodies for override-style phrasing → **warning** for human review. This is a *flag*, never a `validate` gate (§16.14). Confirm guard still treats such text as data (Phase 5).

### D. Generated-packet drift (plan §15, §17.8, Fixture 8)
8. Compare the resume packet's source header (Phase 4 stamp) against current record mtimes/commit: if any source record is newer → flag "regeneration needed". Same idea for stale-report/memory-index and (later) index hashes.

### E. Full fixture suite (plan §17, §19b.11)
9. Build remaining fixtures:
   - **6 — Secret leak:** session record with token-like string → `audit`/`scan-secrets` fails.
   - **7 — Poisoned memory text:** record says "ignore tests" → audit flags instruction-like content; guard treats as data.
   - **8 — Generated packet stale:** source newer than packet → audit flags regeneration.
   - **9 — Cloud fallback:** no CLI execution; committed packet + plain files support manual resume (assert files answer the resume questions). *(Builds on Phase 4 step 11.)*
   - **10 — Many sessions:** 100 session records → resume packet stays bounded and prioritizes current/handoff/active decisions over old observations.
10. Wire **all** Fixtures 1–10 into CI (§19b.11). Add `validate` + `audit` to the CI run.

### F. 19b acceptance verification (plan §19b)
11. Confirm: `guard` (Ph5) passes Fixture 3; `audit` flags stale handoff / missing evidence / invalid statuses / private-path violations / branch mismatch / packet drift; `validate` fails on invalid frontmatter / duplicate IDs / id-filename disagreement / invalid statuses / secret-prohibited committed records.

## Files created / modified
- `continuity.py`: add `audit`, `scan-secrets`, drift check, heuristics.
- `fixtures/fixture-06..10/**`
- `tests/test_audit.py`, `tests/test_secrets.py`, `tests/test_fixtures.py`
- CI config: run `validate` + `audit` + Fixtures 1–10.

## Acceptance criteria (this is 19b — verify the full list, §19b)
- [x] `audit` flags stale handoff, missing evidence, invalid statuses, private-path violations, branch mismatch, generated-packet drift. (`run_audit` reuses `compute_staleness` + re-surfaces validate-failing health checks; `tests/test_audit.py::HealthViewTests`, `PacketDriftTests`.)
- [x] `scan-secrets`/audit fails on token-like strings (Fixture 6). (`scan_secrets` + `audit` secret sub-check, exit 1; `tests/test_secrets.py::Fixture6Tests`.)
- [x] Audit flags instruction-like text (Fixture 7); guard treats it as data. (`scan_instruction_like` warns; `guard` next-action never lifts the imperative; `tests/test_audit.py::InstructionLikeTests`.)
- [x] Audit flags packet regeneration needed (Fixture 8). (`detect_packet_drift` via stamped-vs-current `inputs_hash`; `tests/test_audit.py::PacketDriftTests`.)
- [x] `validate` fails on invalid frontmatter, duplicate IDs, id↔filename disagreement, invalid statuses, secret-prohibited committed records. (Phase 2 checks unchanged; `tests/test_validate.py`.)
- [x] Fixtures 2–10 (and 1) all run in CI and pass. (`validate` over all 10 + `audit` over all 10 in `ci.yml`; `tests/test_fixtures.py`.)
- [x] Cloud fallback (Fixture 9) and bounded-at-scale resume (Fixture 10) verified. (`tests/test_fixtures.py::CloudFallbackTests`, `ManySessionsTests`.)

## Implementation tracker

| # | Task | Status | Notes |
|---|---|---|---|
| 1 | audit core (load + policy-aware) | ☑ | `run_audit`/`cmd_audit`; reads manifest+loaders, never guesses policy |
| 2 | staleness/health flags | ☑ | reuses Phase 4 `compute_staleness` (age+distance, branch mismatch, aged/expired/low-conf) |
| 3 | missing-evidence/invalid-status/private-path in audit | ☑ | re-surfaces validate-fail findings (`_AUDIT_HEALTH_CHECKS`) as warnings |
| 4 | bloat checks | ☑ | `_audit_bloat`: over-budget packet, adapter duplication/size, sessions-growth note |
| 5 | scan-secrets regex set + audit subcheck | ☑ | `SECRET_PATTERNS` + high-entropy; `scan_secrets`, `cmd_scan_secrets`, audit `fail` |
| 6 | instruction-like heuristic (warn only) | ☑ | `scan_instruction_like`; warn-only, never gates validate/guard |
| 7 | generated-packet drift check | ☑ | `detect_packet_drift` compares stamped vs current `inputs_hash` (mtime-independent) |
| 8 | fixture-06 secret leak | ☑ | session record with AWS-key-id + `password=`; validate clean, audit/scan-secrets block |
| 9 | fixture-07 poisoned text | ☑ | trap + attempt with override phrasing; audit flags, guard treats as data |
| 10 | fixture-08 packet stale | ☑ | committed packet with wrong `inputs_hash` (gitignore negation) |
| 11 | fixture-09 cloud fallback | ☑ | accurate committed packet + plain files; no CLI; `inputs_hash` matches (no drift) |
| 12 | fixture-10 many sessions (bounded) | ☑ | 100 session records; packet ≤5k tokens, no transcript leak; sessions-growth note |
| 13 | CI: validate + audit + Fixtures 1–10 | ☑ | `ci.yml`: validate(1–10) + audit(1–10, only F6 blocks) + drift/instruction spot checks |
| 14 | **19b acceptance list all green** | ☑ | full list verified above; 138 tests pass (44 new) |

## Decisions resolved this phase
- **High-impact review enforcement (§22 Q6):** **Flag-only for now.** `audit` surfaces high-impact / unsafe conditions as warnings (and a secret as the one hard block), but does not *enforce* high-impact review at CI/pre-commit time. The enforcement mechanism (pre-commit hook / CI gate / adapter) is deferred to **Phase 9** (hooks & adapters), consistent with the Scope "Out" note. The one exception is the secret gate, which blocks today (`audit`/`scan-secrets` exit non-zero) because committing a credential is irreversible.
- **Secret-scan regex set scope (covered / known gaps):**
  - *Covered shapes:* AWS access-key id (`AKIA…`), GitHub tokens (`gh[pousr]_…`), Slack tokens (`xox[baprs]-…`), Google API keys (`AIza…`), OpenAI-style keys (`sk-…`), JWTs (`eyJ….….…`), PEM private-key headers, bearer tokens, and `api_key/secret/token/access_token/password/…`-style assignments with a ≥16-char value. Plus a conservative high-entropy detector (≥32-char base64-ish tokens requiring mixed upper/lower/digit and Shannon entropy ≥3.5 bits/char).
  - *Deliberate non-goals / known gaps:* pure-hex strings (git shas, the 12-char `inputs_hash`) and lowercase-only record ids are intentionally NOT flagged (the high-entropy charset excludes `_`/`-` and requires class-mix), so the scanner stays quiet on normal memory. Short/exotic provider tokens, secrets split across lines, and base32/url-encoded secrets may be missed. Scope is **committed memory only** — `private/`, `index/`, `generated/` are skipped (private is gitignored; generated is checked for drift, not secrets). Bias is toward low false-positives over exhaustive recall; widen the set if dogfood surfaces a real miss.

## Handoff to post-MVP (Phases 7–10)
- **MVP complete.** Capture, resume, guard, audit, validate, scan-secrets all CI-guarded; Fixtures 1–10 all run in CI (only the secret fixture blocks `audit`).
- Re-run the dogfood loop with the full trust toolchain; collect remaining §22 answers before packaging/MCP/hooks/index.
- **High-impact-review enforcement** is the natural first post-MVP follow-up that Phase 6 explicitly deferred → **Phase 9** (hooks/adapters) is the home for turning the flag into a gate. Packaging (Phase 7) is the lowest-risk next step to make the tool installable for wider dogfood; record which the dogfood feedback most argues for first: _______
