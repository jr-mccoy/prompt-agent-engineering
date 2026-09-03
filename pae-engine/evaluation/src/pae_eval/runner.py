"""Execution: dry-run planning and the real trial loop.

``--dry-run`` is the default and does everything except talk to a provider:
validates the plan and benchmark, builds the snapshot, constructs every
condition, runs the full isolation gate, materializes the schedule, and prices
the run. It needs no API key. That means the expensive failure modes — a broken
condition, a leaked label, an unaffordable plan — are all discovered for free.

``--execute`` requires explicit ``--max-cost-usd`` and ``--max-trials``. There
is no default ceiling, because a default ceiling is a number nobody chose.
"""

from __future__ import annotations

import datetime as _dt
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from . import canonical
from .benchmark import Benchmark, Task
from .conditions import (
    ConditionContext,
    build_condition_a,
    build_condition_b,
    build_condition_c,
    build_condition_d,
    render_system_prompt,
)
from .constants import (
    CONDITION_A,
    CONDITION_B,
    CONDITION_C,
    CONDITION_D,
    HARNESS_VERSION,
)
from .errors import (
    CostCeilingError,
    InfrastructureFailure,
    IsolationError,
    UsageError,
)
from .isolation import IsolationReport, preflight
from .manifest import (
    RunManifest,
    TrialSchedule,
    build_schedule,
    dependency_inventory,
    engine_version,
    environment_summary,
)
from .participant import HostLoop, LoopLimits, RetryPolicy
from .plan import EvaluationPlan
from .pricing import CostGuard, PricingSnapshot, cost_usd, estimate_trial_cost
from .providers import get_adapter
from .snapshot import (
    Snapshot,
    build_snapshot,
    load_snapshot,
    resolve_commit,
)
from .snapshot import write_manifest as write_snapshot_manifest
from .trials import TrialRecord, TrialStore, model_config_hash, new_run_id, trial_id


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="milliseconds")


@dataclass
class RunContext:
    """Everything resolved once for a run."""

    plan: EvaluationPlan
    benchmark: Benchmark
    snapshot: Snapshot
    schedule: TrialSchedule
    pricing: PricingSnapshot
    output_dir: Path
    run_id: str
    benchmark_root: Path | None
    mode: str
    ripgrep_version: str | None = None
    mcp_sdk_version: str | None = None

    @property
    def trials_path(self) -> Path:
        return self.output_dir / "trials.jsonl"


@dataclass
class DryRunReport:
    trial_count: int
    estimated_cost_usd: float
    #: The same token volume re-priced as a cached tool loop. Useful for
    #: sizing a budget; never used to enforce the ceiling, because a ceiling
    #: that assumes cache hits stops being a ceiling the moment one expires.
    estimated_cached_cost_usd: float
    per_condition: Mapping[str, int]
    isolation: IsolationReport
    schedule_sha256: str
    snapshot_sha256: str
    plan_sha256: str
    benchmark_sha256: str
    warnings: tuple[str, ...] = ()
    within_ceiling: bool | None = None
    max_cost_usd: float | None = None

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "trial_count": self.trial_count,
            "estimated_cost_usd": round(self.estimated_cost_usd, 4),
            "estimated_cached_cost_usd": round(self.estimated_cached_cost_usd, 4),
            "per_condition": dict(self.per_condition),
            "isolation": self.isolation.to_json_obj(),
            "schedule_sha256": self.schedule_sha256,
            "participant_snapshot_sha256": self.snapshot_sha256,
            "plan_sha256": self.plan_sha256,
            "benchmark_sha256": self.benchmark_sha256,
            "warnings": list(self.warnings),
            "within_ceiling": self.within_ceiling,
            "max_cost_usd": self.max_cost_usd,
        }


# --------------------------------------------------------------------------
# preparation shared by dry-run and execute
# --------------------------------------------------------------------------


def prepare(
    *,
    plan: EvaluationPlan,
    benchmark: Benchmark,
    repo: Path,
    output_dir: Path,
    benchmark_root: Path | None,
    pricing: PricingSnapshot,
    snapshot_dir: Path | None = None,
    mode: str = "development",
) -> RunContext:
    """Build the snapshot and schedule, and derive the run identity."""
    output_dir = Path(output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    snapshot_root = Path(snapshot_dir) if snapshot_dir else output_dir / "snapshot"
    manifest_path = output_dir / "participant-snapshot.json"
    commit = plan.pae_commit or resolve_commit(Path(repo))

    if snapshot_root.exists() and any(snapshot_root.iterdir()):
        # A populated snapshot directory is either a resume or a mistake. It is
        # a resume when a manifest sits beside it describing this very tree at
        # this very commit — in which case reusing it is not just allowed but
        # required, since a resumed run must bind to the same participant bytes
        # as the run it continues. Anything else is refused: a snapshot is
        # content-addressed, and inheriting whatever was left in a directory
        # would make the run depend on it.
        if not manifest_path.exists():
            raise UsageError(
                f"snapshot directory is not empty and has no manifest beside it: "
                f"{snapshot_root}. Point --snapshot-dir at a fresh path, or "
                "delete it."
            )
        snapshot = load_snapshot(snapshot_root, manifest_path)
        if snapshot.commit != commit:
            raise UsageError(
                f"existing snapshot is at commit {snapshot.commit[:12]} but this "
                f"run targets {commit[:12]}. A different commit is a different "
                "experiment — use a fresh --output-dir."
            )
    else:
        snapshot = build_snapshot(
            Path(repo), snapshot_root, commit=commit,
            require_clean=(mode == "sealed"),
        )
        write_snapshot_manifest(snapshot, manifest_path)

    plan_hash = plan.sha256
    schedule = build_schedule(
        task_ids=[t.task_id for t in benchmark.tasks],
        plan=plan,
        trial_id_for=lambda *, task_id, condition, repeat_index, model_config_sha256:
            trial_id(
                evaluation_version=plan.evaluation_version,
                benchmark_sha256=benchmark.sha256,
                task_id=task_id,
                condition=condition,
                model_config_sha256=model_config_sha256,
                repeat_index=repeat_index,
                plan_sha256=plan_hash,
            ),
    )

    run_id = new_run_id(
        plan_sha256=plan_hash,
        benchmark_sha256=benchmark.sha256,
        snapshot_sha256=snapshot.aggregate_sha256,
        label=mode,
    )
    if mode != "sealed":
        # A development run must never be mistaken for a sealed one, in a
        # filename or in a report.
        run_id = f"{run_id}-dev"

    return RunContext(
        plan=plan, benchmark=benchmark, snapshot=snapshot, schedule=schedule,
        pricing=pricing, output_dir=output_dir, run_id=run_id,
        benchmark_root=benchmark_root, mode=mode,
    )


def _failed_record(*, scheduled: Any, task: Any, model: Any, context: RunContext,
                   plan: EvaluationPlan, benchmark: Benchmark, state: str,
                   error_class: str, detail: str, started_at: str,
                   ended_at: str) -> TrialRecord:
    """A trial record for a failure that happened before the model was reached.

    Written rather than skipped: §81 requires every planned trial to be
    accounted for, and a silently absent trial is indistinguishable from one
    that was never scheduled.
    """
    from .pae_conditions import mcp_sdk_version

    return TrialRecord(
        trial_id=scheduled.trial_id, run_id=context.run_id,
        task_id=task.task_id, condition=scheduled.condition,
        repeat_index=scheduled.repeat_index, attempt_no=1,
        evaluation_version=plan.evaluation_version,
        benchmark_version=benchmark.version,
        benchmark_sha256=benchmark.sha256, plan_sha256=plan.sha256,
        participant_provider=scheduled.provider,
        participant_model=scheduled.model,
        model_parameters=model.to_json_obj(),
        model_parameters_sha256=model.sha256,
        system_prompt_sha256="", task_sha256=task.sha256,
        pae_commit=context.snapshot.commit, pae_dirty=False,
        engine_version=engine_version(), mcp_sdk_version=mcp_sdk_version(),
        tool_catalog_sha256="",
        participant_snapshot_sha256=context.snapshot.aggregate_sha256,
        pricing_snapshot_sha256=context.pricing.sha256,
        started_at=started_at, ended_at=ended_at, latency_ms=0.0,
        state=state, stop_reason=error_class, final_answer="",
        observable_tool_calls=[], usage={}, error_class=error_class,
        retry_state={"detail": detail[:500]}, estimated_cost_usd=0.0,
    )


# --------------------------------------------------------------------------
# condition construction for one task
# --------------------------------------------------------------------------


class ConditionFactory:
    """Builds the four conditions for a task, holding shared resources open."""

    def __init__(self, context: RunContext, *, require_ripgrep: bool = True,
                 mcp_executable: Sequence[str] | None = None) -> None:
        self.context = context
        self._require_ripgrep = require_ripgrep
        self._mcp_executable = mcp_executable
        self._bundle_compiler: Any = None
        self._raw_files = tuple(f.path for f in context.snapshot.files)

    def bundle_compiler(self) -> Any:
        if self._bundle_compiler is None:
            from .pae_conditions import BundleCompiler

            budget = self.context.plan.bundle_budget or {}
            self._bundle_compiler = BundleCompiler(
                self.context.snapshot.root,
                budget_estimated_tokens=int(budget.get("estimated_tokens", 8000)),
                budget_bytes=budget.get("bytes"),
                max_resources=int(budget.get("max_resources", 25)),
            )
        return self._bundle_compiler

    def raw_tools(self) -> Any:
        from .raw_repo import RawRepoTools

        return RawRepoTools(
            self.context.snapshot.root,
            files=self._raw_files,
            require_ripgrep=self._require_ripgrep,
        )

    def mcp_session(self) -> Any:
        from .pae_conditions import McpSession

        return McpSession(
            self.context.snapshot.root, executable=self._mcp_executable,
            timeout_s=float(self.context.plan.limits.get("tool_call_timeout_s", 30)),
        )

    def build(self, task: Task, model: Any, condition: str,
              *, mcp_session: Any = None, raw_tools: Any = None) -> ConditionContext:
        common = dict(
            model=model.model, task_query=task.query, deliverable=task.deliverable,
            max_output_tokens=model.max_output_tokens, effort=model.effort,
            extra=model.extra,
        )
        if condition == CONDITION_A:
            return build_condition_a(**common)
        if condition == CONDITION_B:
            return build_condition_b(raw_tools=raw_tools or self.raw_tools(), **common)
        if condition == CONDITION_C:
            return build_condition_c(
                bundle_result=self.bundle_compiler().compile_for(task.query), **common)
        if condition == CONDITION_D:
            if mcp_session is None:
                raise UsageError("condition D requires a live MCP session")
            return build_condition_d(mcp_session=mcp_session, **common)
        raise UsageError(f"unknown condition {condition!r}")


def _sealed_requires_ripgrep(plan: EvaluationPlan, requested: bool) -> bool:
    """A sealed run that includes condition B may not start without ripgrep.

    Condition B *is* ripgrep-backed search (ADR-0036). Without the binary,
    `RawRepoTools` still constructs when `require_ripgrep` is false and only
    fails when the participant first calls `repo_search` — which is partway
    into a paid run, after money is spent, on the baseline half of the primary
    comparison. Opting out is a development convenience; in sealed mode it is
    just a way to discover the problem expensively.
    """
    if requested or not plan.is_sealed or CONDITION_B not in plan.conditions:
        return requested
    return True


# --------------------------------------------------------------------------
# dry run
# --------------------------------------------------------------------------


def dry_run(
    context: RunContext,
    *,
    max_cost_usd: float | None = None,
    require_ripgrep: bool = False,
    mcp_executable: Sequence[str] | None = None,
    sample_tasks: int = 3,
) -> DryRunReport:
    """Validate everything and price the run without contacting a provider."""
    plan, benchmark = context.plan, context.benchmark
    require_ripgrep = _sealed_requires_ripgrep(plan, require_ripgrep)
    warnings: list[str] = []

    per_condition = {
        condition: len(benchmark.tasks)
        * plan.repeats_for(condition)
        * max(1, len([m for m in plan.models if m.role != "judge"]))
        for condition in plan.conditions
    }
    trial_count = len(context.schedule.trials)

    # -- price the run -----------------------------------------------------
    # Two figures on the same token volume. `estimated` assumes nothing is
    # cached and is what the ceiling is checked against; `cached` re-prices the
    # tool loops as cache reads and is what a budget should be sized from.
    estimated = 0.0
    cached = 0.0
    for scheduled in context.schedule.trials:
        price = context.pricing.get(scheduled.provider, scheduled.model)
        if price is None:
            warnings.append(
                f"no pricing entry for {scheduled.provider}/{scheduled.model}; "
                "its trials are priced at zero and the estimate is therefore low"
            )
            continue
        model = next(
            (m for m in plan.models if m.model == scheduled.model), None
        )
        turns = (
            int(plan.limits.get("max_tool_turns", 40))
            if scheduled.condition in (CONDITION_B, CONDITION_D) else 0
        )
        shape = {
            "expected_input_tokens": (
                3000 if scheduled.condition != CONDITION_C else 9000
            ),
            "max_output_tokens": model.max_output_tokens if model else 4096,
            # A worst case assuming the full turn budget would be wildly
            # pessimistic; a quarter of it is a realistic upper-middle case and
            # is documented as such.
            "tool_turns": turns // 4,
        }
        estimated += estimate_trial_cost(price, **shape)
        cached += estimate_trial_cost(price, **shape, cache_reads=True)
    estimated = round(estimated, 4)
    cached = round(cached, 4)

    if cached > estimated:
        # Only reachable if a snapshot priced cache writes above plain input by
        # more than the reads save, which means the snapshot is wrong or
        # caching is a false economy for this model. Say so either way.
        warnings.append(
            f"the cached estimate (${cached:.2f}) exceeds the uncached one "
            f"(${estimated:.2f}); check the cache rates in the pricing snapshot"
        )

    # A missing binary is reported even when the caller opted out of requiring
    # it. Building condition B without ripgrep succeeds and only fails on the
    # first `repo_search`, so silence here would mean the dry run passes and
    # the paid run dies partway through the baseline arm.
    from .raw_repo import ripgrep_version as _rg_version  # noqa: PLC0415

    if CONDITION_B in plan.conditions and _rg_version() is None:
        warnings.append(
            "ripgrep (rg) is not on PATH. Condition B is defined as "
            "ripgrep-backed search, so it will fail at the participant's first "
            "repo_search call — partway into the run, not now. Install "
            "ripgrep, or drop condition B from the plan. A sealed run refuses "
            "to start without it."
        )

    # -- isolation, on a sample of real tasks ------------------------------
    factory = ConditionFactory(context, require_ripgrep=require_ripgrep,
                               mcp_executable=mcp_executable)
    isolation_checks: list[Any] = []
    sample = list(benchmark.tasks)[:max(1, sample_tasks)]
    primary_model = plan.model_for("primary") or plan.models[0]

    for task in sample:
        contexts: list[ConditionContext] = []
        for condition in plan.conditions:
            if condition == CONDITION_D:
                # Building D needs a live server; the tool-catalog assertion is
                # exercised separately by the isolation tests. Skipping it here
                # keeps --dry-run usable without the MCP extra installed.
                warnings.append(
                    "condition D isolation is not exercised in --dry-run because "
                    "it needs a live MCP server; run the isolation tests or an "
                    "--execute fake run to cover it"
                ) if task is sample[0] else None
                continue
            if condition == CONDITION_B and not require_ripgrep:
                try:
                    contexts.append(factory.build(task, primary_model, condition,
                                                  raw_tools=factory.raw_tools()))
                except UsageError as exc:
                    warnings.append(f"condition B unavailable: {exc}")
                continue
            contexts.append(factory.build(task, primary_model, condition))

        report = preflight(
            contexts, task=task, benchmark_root=context.benchmark_root,
            snapshot_root=context.snapshot.root, output_dir=context.output_dir,
        )
        isolation_checks.extend(report.checks)

    isolation = IsolationReport(checks=tuple(isolation_checks))

    within: bool | None = None
    if max_cost_usd is not None:
        within = estimated <= max_cost_usd
        if not within:
            warnings.append(
                f"estimated ${estimated:.2f} exceeds the ceiling ${max_cost_usd:.2f}; "
                "--execute would refuse before sending anything"
            )

    return DryRunReport(
        trial_count=trial_count,
        estimated_cost_usd=estimated,
        estimated_cached_cost_usd=cached,
        per_condition=per_condition,
        isolation=isolation,
        schedule_sha256=context.schedule.sha256,
        snapshot_sha256=context.snapshot.aggregate_sha256,
        plan_sha256=plan.sha256,
        benchmark_sha256=benchmark.sha256,
        warnings=tuple(dict.fromkeys(w for w in warnings if w)),
        within_ceiling=within,
        max_cost_usd=max_cost_usd,
    )


# --------------------------------------------------------------------------
# execute
# --------------------------------------------------------------------------


@dataclass
class ExecutionSummary:
    run_id: str
    planned: int
    attempted: int
    completed: int
    skipped_resume: int
    failures_by_class: dict[str, int] = field(default_factory=dict)
    spent_usd: float = 0.0
    ceiling_reached: bool = False

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "planned_trials": self.planned,
            "attempted_trials": self.attempted,
            "completed_trials": self.completed,
            "skipped_by_resume": self.skipped_resume,
            "failures_by_class": dict(self.failures_by_class),
            "spent_usd": round(self.spent_usd, 6),
            "cost_ceiling_reached": self.ceiling_reached,
        }


def execute(
    context: RunContext,
    *,
    adapters: Mapping[str, Any],
    max_cost_usd: float,
    max_trials: int,
    resume: bool = True,
    require_ripgrep: bool = True,
    mcp_executable: Sequence[str] | None = None,
    manifest_notes: str = "",
) -> ExecutionSummary:
    """Run the schedule, appending one record per attempt."""
    plan, benchmark = context.plan, context.benchmark
    require_ripgrep = _sealed_requires_ripgrep(plan, require_ripgrep)
    store = TrialStore(context.trials_path)

    if resume:
        store.assert_resumable(
            plan_sha256=plan.sha256,
            benchmark_sha256=benchmark.sha256,
            snapshot_sha256=context.snapshot.aggregate_sha256,
        )
    already = store.completed_trial_ids(
        terminal_states={"completed", *(plan.exclusion_policy.get("terminal_states") or ())}
    ) if resume else set()

    guard = CostGuard(max_cost_usd=max_cost_usd, snapshot=context.pricing)
    factory = ConditionFactory(context, require_ripgrep=require_ripgrep,
                               mcp_executable=mcp_executable)

    summary = ExecutionSummary(
        run_id=context.run_id, planned=len(context.schedule.trials),
        attempted=0, completed=0, skipped_resume=0,
    )

    # -- manifest, written before the first request ------------------------
    env = environment_summary()
    from .raw_repo import ripgrep_version as _rg_version
    from .pae_conditions import mcp_sdk_version as _mcp_version

    manifest = RunManifest(
        run_id=context.run_id, mode=context.mode, plan_sha256=plan.sha256,
        benchmark_sha256=benchmark.sha256, benchmark_version=benchmark.version,
        participant_snapshot_sha256=context.snapshot.aggregate_sha256,
        schedule_sha256=context.schedule.sha256, pae_commit=context.snapshot.commit,
        pae_dirty=False, engine_version=engine_version(),
        harness_version=HARNESS_VERSION, python_version=env["python_version"],
        platform=env["platform"], dependency_inventory=dependency_inventory(),
        provider_models=[m.to_json_obj() for m in plan.models],
        provider_adapters=[a.describe() for a in adapters.values()],
        mcp_sdk_version=_mcp_version(),
        ripgrep_version=_rg_version() if require_ripgrep else None,
        tool_catalog_sha256=dict(plan.tool_catalog_sha256),
        system_prompt_sha256={
            "tooled": canonical.sha256_text(render_system_prompt(has_tools=True)),
            "bare": canonical.sha256_text(render_system_prompt(has_tools=False)),
        },
        judge_prompt_sha256=_judge_prompt_hashes(),
        randomization_seed=plan.randomization_seed,
        retry_policy=dict(plan.retry_policy),
        pricing_snapshot_sha256=context.pricing.sha256,
        output_dir=str(context.output_dir),
        credential_env_names=env["credential_env_names"],
        started_at=_utc_now(), notes=manifest_notes,
    )
    manifest.write(context.output_dir / "run-manifest.json")
    context.schedule.write(context.output_dir / "trial-schedule.json")
    # participant-snapshot.json was written by prepare(), which is also what
    # lets a resumed run rebind to the same bytes rather than rebuilding.

    limits = LoopLimits(
        max_tool_turns=int(plan.limits.get("max_tool_turns", 40)),
        tool_loop_timeout_s=float(plan.limits.get("tool_loop_timeout_s", 600)),
        model_call_timeout_s=float(plan.limits.get("model_call_timeout_s", 120)),
        tool_call_timeout_s=float(plan.limits.get("tool_call_timeout_s", 30)),
    )
    retry = RetryPolicy(
        max_attempts=int(plan.retry_policy.get("infrastructure_max_attempts", 3)),
        base_delay_s=float(plan.retry_policy.get("base_delay_s", 1.0)),
        max_delay_s=float(plan.retry_policy.get("max_delay_s", 30.0)),
        jitter=bool(plan.retry_policy.get("jitter", True)),
    )

    mcp_sessions: dict[str, Any] = {}
    try:
        for scheduled in context.schedule.trials:
            if summary.attempted >= max_trials:
                break
            if scheduled.trial_id in already:
                summary.skipped_resume += 1
                continue

            task = benchmark.by_id(scheduled.task_id)
            if task is None:
                continue
            model = next((m for m in plan.models
                          if m.model == scheduled.model
                          and m.provider == scheduled.provider), None)
            if model is None:
                continue
            adapter = adapters.get(scheduled.provider)
            if adapter is None:
                raise UsageError(
                    f"no adapter supplied for provider {scheduled.provider!r}"
                )

            session = None
            raw_tools = None
            if scheduled.condition == CONDITION_D:
                # One process per trial: a server that died mid-task must not
                # carry state into the next one.
                #
                # A server that fails to start is one trial's infrastructure
                # failure, not the end of the run. Letting it propagate would
                # abandon every remaining trial — including the other three
                # conditions, which do not need MCP at all — over a problem
                # confined to this arm.
                session = factory.mcp_session()
                try:
                    session.start()
                    session.assert_expected_tools()
                except (InfrastructureFailure, IsolationError, UsageError) as exc:
                    session.close()
                    summary.attempted += 1
                    error_class = getattr(exc, "error_class", "mcp_process_died")
                    summary.failures_by_class[error_class] = (
                        summary.failures_by_class.get(error_class, 0) + 1
                    )
                    now = _utc_now()
                    store.append(_failed_record(
                        scheduled=scheduled, task=task, model=model,
                        context=context, plan=plan, benchmark=benchmark,
                        state="infrastructure_failed", error_class=error_class,
                        detail=str(exc), started_at=now, ended_at=now,
                    ))
                    continue
            elif scheduled.condition == CONDITION_B:
                raw_tools = factory.raw_tools()

            try:
                condition_context = factory.build(
                    task, model, scheduled.condition,
                    mcp_session=session, raw_tools=raw_tools,
                )
                report = preflight(
                    [condition_context], task=task,
                    benchmark_root=context.benchmark_root,
                    snapshot_root=context.snapshot.root,
                    output_dir=context.output_dir,
                    expected_mcp_catalog=plan.tool_catalog_sha256.get("D"),
                )
                report.raise_if_failed()

                price = context.pricing.get(scheduled.provider, scheduled.model)
                worst_case = estimate_trial_cost(
                    price, expected_input_tokens=4000,
                    max_output_tokens=model.max_output_tokens,
                    tool_turns=limits.max_tool_turns // 4,
                ) if price else 0.0

                loop = HostLoop(
                    adapter, limits=limits, retry=retry,
                    cost_guard=lambda: guard.check(
                        worst_case, label=scheduled.trial_id),
                )
                summary.attempted += 1
                started = _utc_now()
                result = loop.run(
                    condition_context.request,
                    dispatcher=condition_context.dispatcher,
                    tools=condition_context.tools,
                )
                ended = _utc_now()
            except CostCeilingError:
                summary.ceiling_reached = True
                break
            finally:
                if session is not None:
                    session.close()

            amount = guard.record(result.usage, scheduled.provider, scheduled.model)
            state = "completed" if result.ok else (
                "infrastructure_failed" if result.error_class == "infrastructure_failed"
                else result.error_class or "failed"
            )
            if result.ok:
                summary.completed += 1
            else:
                key = result.error_class or "unknown"
                summary.failures_by_class[key] = summary.failures_by_class.get(key, 0) + 1

            observability = dict(condition_context.observability)
            if raw_tools is not None:
                observability["raw_repo_usage"] = raw_tools.log.summary()
            if session is not None:
                observability["mcp_usage"] = session.log.summary()

            store.append(TrialRecord(
                trial_id=scheduled.trial_id, run_id=context.run_id,
                task_id=task.task_id, condition=scheduled.condition,
                repeat_index=scheduled.repeat_index,
                attempt_no=len(result.attempts),
                evaluation_version=plan.evaluation_version,
                benchmark_version=benchmark.version,
                benchmark_sha256=benchmark.sha256, plan_sha256=plan.sha256,
                participant_provider=scheduled.provider,
                participant_model=scheduled.model,
                model_parameters=model.to_json_obj(),
                model_parameters_sha256=model.sha256,
                system_prompt_sha256=condition_context.system_prompt_sha256,
                task_sha256=task.sha256, pae_commit=context.snapshot.commit,
                pae_dirty=False, engine_version=engine_version(),
                mcp_sdk_version=_mcp_version(),
                tool_catalog_sha256=condition_context.tool_catalog_sha256,
                participant_snapshot_sha256=context.snapshot.aggregate_sha256,
                pricing_snapshot_sha256=context.pricing.sha256,
                started_at=started, ended_at=ended, latency_ms=result.latency_ms,
                state=state, stop_reason=result.stop_reason,
                final_answer=result.final_answer,
                observable_tool_calls=result.tool_calls,
                usage=result.usage.to_json_obj(), error_class=result.error_class,
                retry_state={"attempts": [a.to_json_obj() for a in result.attempts]},
                estimated_cost_usd=amount,
                reported_model=result.reported_model,
                provider_response_id=result.provider_response_id,
                route_bundle=condition_context.bundle,
                condition_observability=observability,
                raw_provider_payload=result.raw_final or None,
            ))
    finally:
        for session in mcp_sessions.values():
            session.close()

    summary.spent_usd = guard.spent_usd
    summary.ceiling_reached = summary.ceiling_reached or guard.ceiling_reached
    return summary


def _judge_prompt_hashes() -> dict[str, str]:
    from .judging.llm import ABSOLUTE_JUDGE_PROMPT, PAIRWISE_JUDGE_PROMPT

    return {
        "absolute": canonical.sha256_text(ABSOLUTE_JUDGE_PROMPT),
        "pairwise": canonical.sha256_text(PAIRWISE_JUDGE_PROMPT),
    }
