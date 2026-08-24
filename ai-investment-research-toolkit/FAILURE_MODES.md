*For informational and research purposes only. Not financial, investment, or tax advice.*

# Failure-Mode Analysis — AI Investment Research Toolkit

**Scope:** This applies the framework in `domain-AI-ML/agentic-ai-systems/aiagent_failure_mode_analysis.md`
to *this* loop specifically — the `research-orchestrator` / `pattern-miner` / `monitor-agent`
agents, the 8 stages, and the four gate-enforcing scripts (`build_snapshot.py`,
`validate_pattern.py`, `screen_rank.py`, `brokers.py`, `score_brier.py`, `adapters.py`).
It catalogs how the loop can loop, stall, hallucinate, overspend, or take an unsafe (paper)
action — each with a detection signal, severity (likelihood × consequence), a **bounded**
mitigation, and an explicit note on **what the existing gates/scripts already catch vs. what is
uncovered** (the residual the operator must watch).

The unsafe-action class is treated as highest priority regardless of likelihood, per the framework.

---

## Surface Map

- **Control loop:** `research-orchestrator` (opus) classifies the entry point and routes Stages
  0→7 per `orchestrator_investment_research.md`; reads `mandate.yaml` first for `halt` / `live_enabled` /
  cadence; delegates Stage 3 → `pattern-miner`, Stage 5 → `monitor-agent`. No explicit step/iteration
  cap is specified in the agent contract.
- **Tools (scripts, gate-enforcing, code-not-trust):** `build_snapshot.py` (Stage 1, immutable +
  look-ahead-safe), `validate_pattern.py` (Stage 3, **Gate A**, reports never mutates),
  `screen_rank.py` (Stage 4, **Gate A** at rank time), `brokers.py` (Stage 6, **kill switch** +
  **Gate B** + paper fill + `--report`), `score_brier.py` (Stage 7, Brier + **Gate C** progress),
  `adapters.py` (manual-only PIT reads, `UNAVAILABLE` queueing).
- **Memory tiers:** durable & git-tracked — `knowledge-base/patterns/PATTERN-*.md`,
  `knowledge-base/journal/PRED-*.md`, `INDEX.md`; working & git-ignored — `data/snapshots/<as_of>/`
  (immutable), `data/output/**`, `data/output/portfolio.json` (paper ledger).
- **External actions:** the only state-changing action is a **paper** fill via `PaperBrokerAdapter`
  (`builtin_simulator`). `LiveBrokerAdapter` is a disabled stub raising `NotImplementedError` (Gate C).
  All data reads are read-only and manual-only by default.

---

## Failure-Mode Register

Severity = Likelihood × Consequence. **Coverage** = whether a script/gate already catches it.

| # | Failure | Origin | Detection signal | Likelihood | Consequence | Severity | Bounded mitigation | Coverage |
|---|---|---|---|---|---|---|---|---|
| F1 | Orchestrator oscillates between stages (e.g. Stage 4 fails verification → re-run Stage 2/3 → re-fail) without converging | control loop | same stage re-entered N× with no new `data/output` artifact | Med | wasted cost, stalled run | **High** | `mandate.yaml` `run_limits.max_stage_reentries` sets an explicit per-run stage-visit cap → abort with partial report and the failing Verification item | Partial — config-level bound now in `mandate.yaml run_limits`; **orchestrator-enforced (contract), not a runtime harness** |
| F2 | Orchestrator stalls waiting on an `UNAVAILABLE` input it keeps re-querying (manual-only seam never gets the file) | Stage 1/2 + loop | identical `UNAVAILABLE` queue entry across passes; no progress | Med | run never completes | Med | Queue-and-continue is the design (`adapters.py` returns `UNAVAILABLE`); `run_limits.max_unavailable_retries` bounds retries, then mark queued and advance read-only | Partial — `adapters.py` queues + `run_limits` bounds retries (orchestrator-enforced, not a runtime harness) |
| F3 | Runaway cost on the **weekly Stage 2 deep-research fan-out** (one dossier per universe candidate × reused `domain-finance` prompts) | Stage 1→2 fan-out | candidate count × per-dossier token cost; wall-clock/$ over budget | Med | large token bill | **High** | `run_limits.max_dossiers_per_run` caps the fan-out (degrade to "top-N ranked candidates only"); Stage 1 universe filter caps candidate count upstream | Partial — config-level ceiling now in `mandate.yaml run_limits` (orchestrator-enforced, not a runtime/token circuit-breaker) |
| F4 | Context-window exhaustion mid-run (opus orchestrator holding all dossiers + KB + journal) | control loop | context near limit; truncated reasoning | Med | dropped state, bad routing | Med | Stages write to `data/output/**` and KB files (durable), so re-entry reloads from disk, not context; bound by processing candidates in batches, not all-in-context | Partial — file-based state helps; no explicit batch bound |
| F5 | Hallucinated ticker / price / fill — agent invents a candidate, a quote, or claims an order filled | Stage 1/2/6 + agent | value with no provenance to a `data/input/` file or snapshot; fill not in `portfolio.json` | Med | corrupt dossier, fake position | **High** | `adapters.py` returns only PIT records or `UNAVAILABLE`; `brokers.py` only emits a `Fill` it actually computed and persists to ledger; agent "Must Not invent" rules; verify any claimed fill against `portfolio.json` | **Mostly covered** — fabricated *fills* blocked by `brokers.py`; fabricated *narrative numbers in a dossier* (Stage 2 markdown) are **uncovered** by code |
| F6 | Hallucinated / malformed **tool call** — agent runs a script with bad args or treats a script error as success | tool interaction | script exit code / `REJECTED`/`HALTED`/`FAIL` ignored; non-zero exit not branched on | Low | acts on a failed gate as if passed | **High** | Scripts return structured PASS/FAIL + reasons and non-zero exits; `run_limits.nonzero_exit_is_hard_stop` makes "any non-zero script exit = hard stop" a contract rule the orchestrator must honor | Partial — scripts *report* correctly; `run_limits` codifies the hard-stop rule but enforcement is orchestrator discipline, not a runtime harness |
| F7 | `pattern-miner` promotes an **overfit** pattern past Gate A | Stage 3 / KB | `validate_pattern.py` PASS but with leakage the checker can't see (e.g. holdout not truly disjoint, look-ahead in feature) | Med | a fake "edge" scores in Stage 4 → sizes a paper trade | **High** | `validate_pattern.py` enforces OOS-`n` ≥ min + positive lift + required fields; `screen_rank.py` re-runs it at rank time so only `validated` patterns score. **Residual the checker cannot verify:** that the holdout is genuinely disjoint and feature is point-in-time — relies on `pattern-miner` discipline + multiple-comparisons note | Partial — Gate A catches *in-sample-only / under-n*; **leakage/disjointness is UNCOVERED by code** |
| F8 | `pattern-miner` backfills `registered_on` and dresses a post-hoc story as pre-registered | Stage 3 / KB | `registered_on` near/after first outcome inspection; git history of the PATTERN file | Low | post-hoc pattern validated | **High** | Agent "Must Not backfill"; bound by committing PATTERN records to git so `registered_on` vs. file/commit date is auditable | **UNCOVERED by `validate_pattern.py`** (it checks fields exist, not their honesty) — git-history audit is the only check |
| F9 | `monitor-agent` **misses** a tripwire (reads missing data as "nothing tripped") | Stage 5 | a name with `UNAVAILABLE` inputs but no FIRED/queued entry in `alerts/<as_of>.md` | Med | undetected thesis-break on a paper position | **High** | Agent contract: classify every tripwire `FIRED`/`ARMED`/`UNAVAILABLE` and **queue** every `UNAVAILABLE` — never silent. Bound: alert file must account for every watched name | Partial — enforced by *prompt discipline*, not a script; no code asserts completeness |
| F10 | `monitor-agent` **spams** tripwires (over-fires, alert fatigue) | Stage 5 | high FIRED-rate, repeated identical alerts across daily sweeps | Low | operator ignores alerts | Med | Tripwires are concrete thresholds from the dossier, not vibes; bound by per-name de-dup (don't re-FIRE an already-open alert) and daily snapshot evaluation | **UNCOVERED** — no de-dup logic specified |
| F11 | Monitor uses a value dated **after** the sweep `as_of` (look-ahead in monitoring) | Stage 5 | snapshot record `as_of` > sweep `as_of` | Low | false tripwire / false all-clear | Med | Contract: evaluate against "latest point-in-time snapshot only"; `adapters.py`/`build_snapshot.py` enforce PIT on reads | Mostly covered for snapshot reads; monitor-side discipline is residual |
| F12 | Journal/calibration **corruption** — `probability` edited after outcome known, or running Brier computed over a favorable subset | Stage 7 / journal | `probability` changed vs `lock_hash`; resolved-count in report ≠ files on disk | Med | Gate C track record is a lie | **Critical** | `journal_integrity.py` stamps a `lock_hash` at open; `--verify` detects a `probability` edited after the fact; `score_brier.py` folds it in so `gate_c.integrity_clean` is required for `unlock_ready` | **Now caught in code (tamper-evident)** — `journal_integrity.py` detects a post-lock `probability` edit; git history remains the backstop for pre-lock tampering |
| F13 | Invented resolution — a `PRED-*` marked resolved with no real outcome to inflate the track record | Stage 7 / journal | `resolution` set but no `realized_return`/`resolved_on`; horizon not yet reached | Low | premature/false Gate C progress | **Critical** | `journal_integrity.py` enforces resolution honesty: a resolved record needs `realized_return` + `resolved_on` at/after the horizon, else `integrity_clean` fails and Gate C cannot show ready | **Now caught in code** — premature/empty resolutions fail the integrity check (`gate_c.integrity_clean`) |
| F14 | **Gate / kill-switch bypass** — a stage advances on a failed gate, or `halt`/`live_enabled` is flipped mid-run | all gates / config | a placed order with `REJECTED`; an action stage running while `halt: true`; diff to `mandate.yaml` | Low | unsafe action escapes its gate | **Critical** | Gates enforced in scripts (`brokers.py check_halt` + `check_risk_limits`, `screen_rank.py` Gate A); orchestrator "Must Not flip `halt`/`live_enabled` or loosen/skip/reorder a gate." Bound: gate decisions are script return codes, not agent assertions | **Mostly covered** — scripts enforce; residual is the orchestrator choosing to honor them (no external enforcer above the agent) |
| F15 | **Snapshot look-ahead contamination** — a backtest/pattern peeks at future data | Stage 1 / snapshots | record `as_of` > snapshot date; snapshot mutated after write | Low | inflated, fake edge | **Critical** | `build_snapshot.py` writes **immutable** `data/snapshots/<as_of>/`, **refuses to overwrite** (exit 2), and **skips candidates with no PIT price** (no back-fill); `adapters.py` returns nothing dated after `as_of` | **Covered for snapshot construction** — residual is leakage *inside* a pattern's own feature definition (see F7) |
| F16 | Unsafe (paper) order generation — order sized over caps, no stop/sizing/pre-mortem, or self-trading the ledger to look good | Stage 6 / `brokers.py` | `check_risk_limits` → `REJECTED`; missing `stop`/`sizing_ref`/`premortem_ref` | Low–Med | bad paper decision pollutes track record | **High** | **Gate B** in `brokers.py`: rejects unless stop + sizing + pre-mortem present AND ≤2%/position, ≤20%/class, ≤60% deployed; HALTED/REJECTED orders do **not** mutate `portfolio.json` | **Covered** — Gate B + kill switch enforced in code; thresholds read from `risk_limits.yaml` |
| F17 | Real-money action via `LiveBrokerAdapter` | Stage 6 | any call path reaching `LiveBrokerAdapter.place_order` | **Low** | **irreversible real loss** | **Critical** | Disabled stub raises `NotImplementedError`; Gate C requires ≥100 resolved + Brier ≤0.18 + manual `live_enabled: true`; orchestrator "Must Not reach/enable/simulate Live" | **Covered** — hard-locked; residual is a human deliberately enabling it |
| F18 | Memory drift — `INDEX.md` status disagrees with the `PATTERN-*.md` record (a `retired` pattern still listed `validated`) | Stage 3 / KB | INDEX status ≠ record `status` | Med | retired/overfit pattern still scores | Med | `validate_pattern.py --reconcile` asserts INDEX/record agreement and reports drift before any Stage 4 run | **Now caught in code** — `validate_pattern.py --reconcile` flags INDEX/record status mismatches |

---

## Highest-Priority (Unsafe / Irreversible) Actions

Per the framework, consequence dominates likelihood for these:

- **F17 real-money order** → hard-locked: `LiveBrokerAdapter` raises `NotImplementedError`, Gate C
  (100 resolved + Brier ≤0.18 + manual enable). The only path through is a deliberate human edit.
- **F14 gate/kill-switch bypass** & **F16 over-cap paper order** → `brokers.py` enforces the kill
  switch and Gate B in code; HALTED/REJECTED orders never touch the ledger.
- **F12/F13 journal corruption** → these are unsafe because they are the **input to Gate C**: a
  tampered track record is what would eventually unlock real money. They are now **caught in code**:
  `journal_integrity.py` stamps a `lock_hash` at open (detecting a post-resolution `probability` edit)
  and enforces resolution honesty (`realized_return` + `resolved_on` at/after horizon); `score_brier.py`
  requires `gate_c.integrity_clean` for `unlock_ready`. Git-history audit remains the backstop for
  pre-lock tampering.

---

## Monitoring & Alert Thresholds (recommended)

- **Loop/stall (F1, F2):** alert if any stage is re-entered >2× in one run, or wall-clock exceeds a
  per-run cap → auto-abort with partial report.
- **Cost (F3, F4):** alert at a soft token budget; auto-degrade to top-N candidates and abort the
  fan-out at a hard ceiling.
- **Tool integrity (F6):** treat any non-zero script exit as a hard stop, not a retry.
- **Gate integrity (F14):** log every `git diff` to `config/mandate.yaml` and any order whose status
  is not `FILLED`; alert on a `FILLED` order that was preceded by a `REJECTED` reason.
- **Calibration integrity (F12, F13):** alert on any post-resolution edit to a `PRED-*` `probability`
  field; reconcile `score_brier.py` resolved-count against files on disk before reporting Gate C.
- **Memory drift (F18):** reconcile `INDEX.md` against `PATTERN-*` statuses before each Stage 4.

---

## Residual Risk Summary — Covered vs. Uncovered

**Already caught in code (high confidence):**
- Gate A under-`n` / in-sample-only promotion (`validate_pattern.py`, `screen_rank.py`).
- Gate B cap/discipline breaches and the kill switch (`brokers.py`).
- Gate C real-money lock (`LiveBrokerAdapter` disabled stub).
- Snapshot immutability + point-in-time reads, fabricated-fill prevention (`build_snapshot.py`,
  `adapters.py`, `brokers.py`).
- **Journal/calibration tampering (F12/F13)** — `journal_integrity.py` provides tamper-evidence
  (`lock_hash` detects a post-resolution `probability` edit) and resolution honesty (resolved records
  need `realized_return` + `resolved_on` at/after horizon); folded into `score_brier.py` so
  `gate_c.integrity_clean` is required for `unlock_ready`. Git history remains the backstop for pre-lock edits.
- **Memory drift (F18)** — `validate_pattern.py --reconcile` asserts INDEX/record status agreement.
- **Loop/stall + fan-out cost (F1/F2/F3/F6)** — now have **config-level `run_limits` bounds** in
  `mandate.yaml` (`max_stage_reentries`, `max_unavailable_retries`, `max_dossiers_per_run`,
  `nonzero_exit_is_hard_stop`). These are **orchestrator-enforced contract limits, not a runtime
  harness** — they bound the loop by agent discipline reading the config, not by an external supervisor.

**Top uncovered residuals (operator/agent-discipline only — harden these next):**
1. **Pattern-leakage past Gate A (F7/F8)** — `validate_pattern.py` checks fields and OOS-`n`/lift (and
   now emits non-blocking advisory warnings on high multiple-comparisons counts and missing
   point-in-time/survivorship language) but **cannot verify substance**: that the holdout is genuinely
   disjoint, the feature is point-in-time, or `registered_on` was honest. Relies on `pattern-miner`
   discipline + git history + the leakage audit.
2. **Runaway weekly Stage 2 fan-out / orchestrator loop & stall (F3/F1/F2)** — now bounded by
   `mandate.yaml run_limits` at the **contract** level, but there is still no runtime token circuit-breaker
   or external supervisor; enforcement depends on the orchestrator honoring the config.

The leakage-substance residual (F7/F8) is the catastrophic-but-uncovered case that survives: it corrupts
exactly the evidence the gates trust and no code can verify it. It is accepted today only because the
system is **paper-only** (no real capital at risk) and **git-tracked** (tampering is detectable after the
fact) — and must stay under human audit before Gate C is ever approached.
