"""``python -m pae_eval`` — the developer command surface.

Deliberately not a ``pae`` subcommand. The Engine's CLI is a read-only,
no-network, no-write runtime; evaluation calls providers, spends money and
writes files. Keeping them in separate commands keeps that boundary visible in
the thing people actually type (spec §8).

Only ``run --execute`` can spend money, it is never the default, and it refuses
to start without an explicit cost ceiling and trial cap.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

from . import canonical
from .constants import FIXTURE_MARKER, HARNESS_VERSION
from .errors import (
    CostCeilingError,
    FrozenPlanError,
    IsolationError,
    PaeEvalError,
    UsageError,
    ValidationError,
)

EXIT_OK = 0
EXIT_FAILED = 1
EXIT_USAGE = 2


# --------------------------------------------------------------------------
# output helpers
# --------------------------------------------------------------------------


def _configure_streams() -> None:
    """Unicode-safe console output on a legacy code page."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="backslashreplace")
            except Exception:  # pragma: no cover
                pass


def _emit(obj: Any, as_json: bool, text: str = "") -> None:
    if as_json:
        print(canonical.canonical_json(obj))
    elif text:
        print(text)


def _problems(title: str, problems: Sequence[str], limit: int = 25) -> str:
    shown = "\n".join(f"  - {p}" for p in problems[:limit])
    more = f"\n  ... and {len(problems) - limit} more" if len(problems) > limit else ""
    return f"{title}\n{shown}{more}"


# --------------------------------------------------------------------------
# shared loading
# --------------------------------------------------------------------------


def _load_benchmark(root: Path):
    from .benchmark import load_benchmark

    return load_benchmark(root)


def _load_plan(path: Path | None):
    from .plan import EvaluationPlan, example_plan

    return EvaluationPlan.load(path) if path else example_plan()


def _load_pricing(path: Path | None):
    from .pricing import PricingSnapshot, example_snapshot

    return PricingSnapshot.load(path) if path else example_snapshot()


def _registry_facts(repo: Path) -> tuple[set[str], set[str]]:
    """Known UIDs and scopes, for label resolution. Empty when unavailable."""
    try:
        from pae_engine import Registry, Repository, SearchEngine
    except ImportError:
        return set(), set()
    try:
        registry = Registry.open(Repository.at(repo))
        engine = SearchEngine(registry)
        index = engine._ensure_index()
        return {doc.uid for doc in index.documents}, set(engine.scopes)
    except Exception:
        return set(), set()


# --------------------------------------------------------------------------
# commands
# --------------------------------------------------------------------------


def cmd_validate_benchmark(args: argparse.Namespace) -> int:
    from .benchmark import composition_report, validate_benchmark
    from .leakage import LeakageCorpus, audit_benchmark

    benchmark = _load_benchmark(Path(args.benchmark_root))
    plan = _load_plan(Path(args.plan) if args.plan else None)

    uids, scopes = _registry_facts(Path(args.repo)) if args.repo else (set(), set())
    problems = validate_benchmark(
        benchmark,
        known_uids=uids or None,
        known_scopes=scopes or None,
        require_provenance=not args.allow_missing_provenance,
    )

    leakage = None
    if args.repo:
        corpus = LeakageCorpus.from_repo(Path(args.repo))
        leakage = audit_benchmark(benchmark.tasks, corpus,
                                  thresholds=plan.leakage_thresholds)
        if leakage.violations and not args.allow_leakage:
            problems.extend(f"leakage gate: {v}" for v in leakage.violations)

    composition = composition_report(benchmark)
    payload = {
        "benchmark_version": benchmark.version,
        "benchmark_sha256": benchmark.sha256,
        "task_count": len(benchmark),
        "valid": not problems,
        "problems": problems,
        "composition": composition,
        "leakage": leakage.to_json_obj() if leakage else None,
    }

    if args.json:
        _emit(payload, True)
    else:
        print(f"benchmark {benchmark.version} — {len(benchmark)} tasks")
        print(f"sha256: {benchmark.sha256}")
        print(f"classes: {composition['class_distribution']}")
        if leakage:
            metrics = leakage.metrics
            print(
                f"leakage: median overlap {metrics['median_target_overlap']}, "
                f"title containment {metrics['title_token_containment_count']}, "
                f"id-tail containment {metrics['id_tail_containment_count']}"
            )
        if problems:
            print(_problems("\nVALIDATION FAILED:", problems))
        else:
            print("\nOK — benchmark is valid")
    return EXIT_OK if not problems else EXIT_FAILED


def cmd_plan(args: argparse.Namespace) -> int:
    from .plan import EvaluationPlan, example_plan, plan_warnings, validate_plan
    from .snapshot import resolve_commit

    if args.check:
        plan = EvaluationPlan.load(Path(args.plan))
        recomputed = plan.sha256
        sidecar = Path(args.plan).with_suffix(Path(args.plan).suffix + ".sha256")
        recorded = sidecar.read_text(encoding="utf-8").strip() if sidecar.exists() else None
        problems = validate_plan(plan)
        checked_warnings = plan_warnings(plan)
        matches = recorded is None or recorded == recomputed
        if not matches:
            problems.append(
                f"plan digest mismatch: file says {recorded}, content hashes to "
                f"{recomputed}. The plan was edited after it was frozen."
            )
        payload = {"plan_sha256": recomputed, "recorded_sha256": recorded,
                   "valid": not problems, "problems": problems,
                   "warnings": checked_warnings}
        if args.json:
            _emit(payload, True)
        else:
            print(f"plan sha256: {recomputed}")
            if checked_warnings:
                print(_problems("PLAN WARNINGS (not failures — declare these):",
                                checked_warnings))
            print(_problems("PLAN CHECK FAILED:", problems) if problems
                  else "OK — plan is valid and its digest matches")
        return EXIT_OK if not problems else EXIT_FAILED

    benchmark = _load_benchmark(Path(args.benchmark_root))
    pricing = _load_pricing(Path(args.pricing) if args.pricing else None)
    base = _load_plan(Path(args.from_plan) if args.from_plan else None)

    from dataclasses import replace

    plan = replace(
        base,
        mode=args.mode,
        benchmark_version=benchmark.version,
        benchmark_sha256=benchmark.sha256,
        pae_commit=resolve_commit(Path(args.repo)) if args.repo else base.pae_commit,
        pricing_snapshot_sha256=pricing.sha256,
    )
    problems = validate_plan(plan)
    warnings = plan_warnings(plan)

    # Costing is estimated here without any provider call.
    from .statistics import ci_half_width, detectable_effect

    n = len(benchmark)
    participants = max(1, len([m for m in plan.models if m.role != "judge"]))
    repeats_per_task = sum(plan.repeats_for(c) for c in plan.conditions)
    planning = {
        "n_tasks": n,
        "detectable_effect_pp": round(detectable_effect(n) * 100, 2),
        "ci_half_width_pp": round(ci_half_width(n) * 100, 2),
        "planned_trials": n * repeats_per_task * participants,
    }

    if args.out:
        digest = plan.write(Path(args.out))
    else:
        digest = plan.sha256

    payload = {
        "plan_sha256": digest,
        "valid": not problems,
        "problems": problems,
        # Not failures. Limitations the report has to carry — printed here so
        # they are seen while the plan can still be changed, rather than
        # discovered in the write-up after the money is spent.
        "warnings": warnings,
        "planning": planning,
        "written_to": str(args.out) if args.out else None,
    }
    if args.json:
        _emit(payload, True)
    else:
        print(f"plan sha256: {digest}")
        print(f"tasks: {n}  planned trials: {planning['planned_trials']}")
        print(f"detectable effect ~{planning['detectable_effect_pp']} pp; "
              f"CI half-width ~{planning['ci_half_width_pp']} pp")
        if args.out:
            print(f"written: {args.out}")
        if warnings:
            print(_problems("\nPLAN WARNINGS (not failures — declare these):",
                            warnings))
        if problems:
            print(_problems("\nPLAN PROBLEMS:", problems))
    return EXIT_OK if not problems else EXIT_FAILED


def cmd_run(args: argparse.Namespace) -> int:
    from .providers import get_adapter
    from .runner import dry_run, execute, prepare

    if args.execute and args.dry_run:
        raise UsageError("choose exactly one of --dry-run and --execute")
    # Neither flag means dry-run. Spending money is never the default, and it
    # is never what you get by forgetting an argument.
    executing = bool(args.execute)

    benchmark = _load_benchmark(Path(args.benchmark_root))
    plan = _load_plan(Path(args.plan) if args.plan else None)
    pricing = _load_pricing(Path(args.pricing) if args.pricing else None)

    context = prepare(
        plan=plan, benchmark=benchmark, repo=Path(args.repo),
        output_dir=Path(args.output_dir), benchmark_root=Path(args.benchmark_root),
        pricing=pricing, snapshot_dir=Path(args.snapshot_dir) if args.snapshot_dir else None,
        mode=args.mode,
    )

    if not executing:
        report = dry_run(
            context, max_cost_usd=args.max_cost_usd,
            require_ripgrep=args.require_ripgrep,
        )
        if args.json:
            _emit(report.to_json_obj(), True)
        else:
            print(f"run id           : {context.run_id}")
            print(f"planned trials   : {report.trial_count}")
            print(f"estimated cost   : ${report.estimated_cost_usd:.2f} "
                  f"(no cache hits assumed — size the ceiling from this)")
            print(f"  with caching   : ${report.estimated_cached_cost_usd:.2f} "
                  f"(same tokens, tool loops priced as cache reads)")
            print(f"snapshot         : {report.snapshot_sha256}")
            print(f"schedule         : {report.schedule_sha256}")
            print(f"isolation        : "
                  f"{'PASS' if report.isolation.passed else 'FAIL'} "
                  f"({len(report.isolation.checks)} checks)")
            for check in report.isolation.failures:
                print(f"  ✗ {check.name}: {check.detail}")
            for warning in report.warnings:
                print(f"  ! {warning}")
            print("\nno provider call was made")
        return EXIT_OK if report.isolation.passed else EXIT_FAILED

    if args.max_cost_usd is None or args.max_trials is None:
        raise UsageError(
            "--execute requires both --max-cost-usd and --max-trials with "
            "explicit positive values. The harness does not choose a spending "
            "ceiling on your behalf."
        )

    adapters: dict[str, Any] = {}
    if args.fake_quality:
        # A credential-free end-to-end run. Every provider in the plan is
        # served by the same behavioural fake, so the full pipeline — snapshot,
        # isolation, tool loops, trial records, resume — is exercised exactly as
        # a paid run would exercise it.
        from .providers.fake import BehaviouralFake

        shared = BehaviouralFake(quality=args.fake_quality)
        for model in plan.models:
            if model.role != "judge":
                adapters[model.provider] = shared
    else:
        # Prompt caching is on unless the plan turns it off. It changes the
        # bill and the latency, never a token the model sees, so it is a
        # default rather than a decision — but it is recorded in the plan hash
        # and in the manifest either way.
        caching = bool(plan.limits.get("prompt_caching", True))
        for model in plan.models:
            if model.role == "judge":
                continue
            if model.provider not in adapters:
                kwargs: dict[str, Any] = {}
                if model.provider == "anthropic":
                    kwargs["cache_prompts"] = caching
                adapters[model.provider] = get_adapter(model.provider, **kwargs)

    summary = execute(
        context, adapters=adapters, max_cost_usd=args.max_cost_usd,
        max_trials=args.max_trials, resume=not args.no_resume,
        require_ripgrep=args.require_ripgrep,
    )
    if args.json:
        _emit(summary.to_json_obj(), True)
    else:
        print(f"run id     : {summary.run_id}")
        print(f"attempted  : {summary.attempted} of {summary.planned}")
        print(f"completed  : {summary.completed}")
        print(f"skipped    : {summary.skipped_resume} (resume)")
        print(f"spent      : ${summary.spent_usd:.4f}")
        if summary.failures_by_class:
            print(f"failures   : {summary.failures_by_class}")
        if summary.ceiling_reached:
            print("stopped early: cost ceiling reached")
    return EXIT_OK


def cmd_judge(args: argparse.Namespace) -> int:
    """Deterministic scoring, plus an LLM judge when one is configured."""
    from .judging import score_task
    from .trials import TrialStore

    benchmark = _load_benchmark(Path(args.benchmark_root))
    plan = _load_plan(Path(args.plan) if args.plan else None)
    store = TrialStore(Path(args.output_dir) / "trials.jsonl")
    scores_path = Path(args.output_dir) / "scores.jsonl"

    written = 0
    seen: set[str] = set()
    with open(scores_path, "a", encoding="utf-8", newline="\n") as handle:
        for row in store.read():
            trial = str(row.get("trial_id"))
            if trial in seen or row.get("state") != "completed":
                continue
            seen.add(trial)
            task = benchmark.by_id(str(row.get("task_id")))
            if task is None:
                continue
            score = score_task(task, trial=row, judge_payload=None)
            handle.write(canonical.canonical_json(score.to_json_obj()) + "\n")
            written += 1

    payload = {"scores_written": written, "scores_path": str(scores_path),
               "llm_judging": "deterministic-only in this invocation"}
    if args.json:
        _emit(payload, True)
    else:
        print(f"scored {written} trial(s) -> {scores_path}")
        print("deterministic criteria only; pass --with-llm-judge to add a judge model")
    return EXIT_OK


def cmd_analyze(args: argparse.Namespace) -> int:
    from .analysis import AnalysisInputs, analyze
    from .trials import TrialStore

    plan = _load_plan(Path(args.plan) if args.plan else None)
    output = Path(args.output_dir)
    trials = list(TrialStore(output / "trials.jsonl").read())
    scores_path = output / "scores.jsonl"
    scores = [
        json.loads(line)
        for line in (scores_path.read_text(encoding="utf-8").splitlines()
                     if scores_path.exists() else [])
        if line.strip()
    ]

    retrieval = None
    retrieval_path = output / "retrieval.json"
    if retrieval_path.exists():
        retrieval = json.loads(retrieval_path.read_text(encoding="utf-8"))

    result = analyze(
        AnalysisInputs(trials=trials, scores=scores, plan=plan, retrieval=retrieval),
        planned_trials=args.planned_trials,
    )
    destination = output / "analysis.json"
    canonical.write_canonical(destination, result)

    if args.json:
        _emit(result, True)
    else:
        primary = result["primary"]
        first, second = primary["primary_contrast"]
        print(f"primary: {first} vs {second} on {primary['n_tasks']} tasks")
        print(f"  {first} pass rate: {primary[f'{first}_pass_rate']:.3f}")
        print(f"  {second} pass rate: {primary[f'{second}_pass_rate']:.3f}")
        print(f"  difference: {primary['absolute_difference']:+.3f}")
        print(f"  95% CI: [{primary['ci']['ci_lower']:+.3f}, "
              f"{primary['ci']['ci_upper']:+.3f}]")
        print(f"  McNemar p: {primary['mcnemar']['p_value']:.4g}")
        print(f"\nwritten: {destination}")
    return EXIT_OK


def cmd_report(args: argparse.Namespace) -> int:
    from .benchmark import composition_report
    from .report import claim_sentence, render_markdown

    output = Path(args.output_dir)
    plan = _load_plan(Path(args.plan) if args.plan else None)
    analysis = json.loads((output / "analysis.json").read_text(encoding="utf-8"))
    manifest_path = output / "run-manifest.json"
    manifest = (
        json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest_path.exists() else {}
    )
    composition = None
    if args.benchmark_root:
        composition = composition_report(_load_benchmark(Path(args.benchmark_root)))

    markdown = render_markdown(
        analysis, plan=plan, manifest=manifest,
        benchmark_composition=composition, is_fixture=args.fixture,
    )
    destination = Path(args.out) if args.out else output / "report.md"
    destination.write_text(markdown, encoding="utf-8", newline="\n")

    claim = claim_sentence(analysis, plan=plan, manifest=manifest)
    if args.json:
        _emit({"report_path": str(destination), "claim_sentence": claim}, True)
    else:
        print(f"report written: {destination}")
        print(f"claim sentence: {claim or '(none — the numbers do not support one)'}")
    return EXIT_OK


def cmd_layer_a(args: argparse.Namespace) -> int:
    from .retrieval import LayerAScorer

    benchmark = _load_benchmark(Path(args.benchmark_root))
    scorer = LayerAScorer(Path(args.snapshot or args.repo))
    report = scorer.score(benchmark, disclosure=args.disclosure)
    destination = Path(args.output_dir) / "retrieval.json" if args.output_dir else None
    if destination:
        destination.parent.mkdir(parents=True, exist_ok=True)
        canonical.write_canonical(destination, report.to_json_obj())
    if args.json:
        _emit(report.to_json_obj(), True)
    else:
        metrics = report.metrics
        print(f"layer A over {metrics['n']} tasks")
        for key in ("recall_at_1", "recall_at_5", "mrr", "scope_at_1", "kind_at_1",
                    "route_status_accuracy", "false_confident_rate"):
            value = metrics.get(key)
            print(f"  {key:24s} {'n/a' if value is None else f'{value:.3f}'}")
        if destination:
            print(f"written: {destination}")
    return EXIT_OK


def cmd_snapshot(args: argparse.Namespace) -> int:
    from .snapshot import (
        assert_no_evaluation_infrastructure,
        assert_product_present,
        build_snapshot,
        write_manifest,
    )

    snapshot = build_snapshot(
        Path(args.repo), Path(args.dest), commit=args.commit,
        require_clean=args.require_clean,
    )
    assert_no_evaluation_infrastructure(snapshot)
    assert_product_present(snapshot)
    digest = write_manifest(snapshot, Path(args.dest).parent
                            / "participant-snapshot.json")
    payload = {
        "commit": snapshot.commit,
        "files": snapshot.file_count,
        "excluded": snapshot.excluded_count,
        "aggregate_sha256": snapshot.aggregate_sha256,
        "manifest_sha256": digest,
    }
    if args.json:
        _emit(payload, True)
    else:
        print(f"commit    : {snapshot.commit}")
        print(f"files     : {snapshot.file_count} included, "
              f"{snapshot.excluded_count} excluded")
        print(f"aggregate : {snapshot.aggregate_sha256}")
    return EXIT_OK


# --------------------------------------------------------------------------
# authoring firewall (Phase 8A)
# --------------------------------------------------------------------------


def cmd_prepare_authoring(args: argparse.Namespace) -> int:
    """Select, mask, export, manifest and audit — in that order, once.

    A single command on purpose. Splitting selection from export would let the
    two drift apart between runs, and "which selection produced this packet?"
    is exactly the question a provenance chain must never have to guess at.
    """
    from datetime import datetime, timezone

    from .authoring import audit, packets, selection as sel

    repo = Path(args.repo)
    out_dir = Path(args.out_dir)
    created_at = args.created_at or datetime.now(timezone.utc).replace(
        microsecond=0).isoformat()

    exclusions = (sel.DevelopmentExclusions.load(Path(args.development_exclusions))
                  if args.development_exclusions else sel.DevelopmentExclusions.empty())

    records = sel.load_registry_records(repo)
    result = sel.select_targets(
        records, repo,
        target_pae_commit=args.commit,
        excluded_clusters=exclusions.clusters,
        excluded_uids=exclusions.uids,
        development_exclusion_sha256=exclusions.sha256,
    )
    if not result.ok:
        print(_problems("SELECTION FAILED:", list(result.problems)), file=sys.stderr)
        return EXIT_FAILED

    by_uid = {str(r.get("uid")): r for r in records}
    mappings, problems = packets.build_mappings(result, by_uid, repo)
    if problems:
        print(_problems("MASKING FAILED:", problems), file=sys.stderr)
        return EXIT_FAILED

    author_root = out_dir / packets.AUTHOR_PACKET_NAME
    reviewer_root = out_dir / packets.REVIEWER_PACKET_NAME
    author_digests = packets.build_author_packet(author_root, mappings)
    reviewer_digests = packets.build_reviewer_packet(reviewer_root, mappings, result)

    author_manifest = packets.author_manifest(
        repo=repo, selection=result, mappings=mappings,
        digests=author_digests, created_at=created_at,
    )
    reviewer_manifest = packets.reviewer_manifest(
        repo=repo, selection=result, mappings=mappings,
        digests=reviewer_digests, created_at=created_at,
    )
    author_manifest_sha = packets.write_manifest(
        out_dir / "author-packet-manifest.json", author_manifest)
    reviewer_manifest_sha = packets.write_manifest(
        out_dir / "reviewer-private-manifest.json", reviewer_manifest)

    # The audit runs against the files as written, not against the objects that
    # wrote them. Auditing the intention would prove nothing about the export.
    forbidden = {digest: path for path, digest in reviewer_digests.items()}
    report = audit.audit_export(
        author_root,
        audit.target_identities(m.to_json_obj() for m in mappings),
        forbidden_digests=forbidden,
    )
    disjoint = audit.assert_disjoint(author_root, reviewer_root)

    payload = {
        "created_at": created_at,
        "pae_commit": result.target_pae_commit,
        "selection": result.public_summary(),
        "author_packet": str(author_root),
        "reviewer_packet": str(reviewer_root),
        "author_manifest_sha256": author_manifest_sha,
        "reviewer_private_manifest_sha256": reviewer_manifest_sha,
        "audit": report.to_json_obj(),
        "export_disjointness_problems": disjoint,
        "readiness": (report.readiness if not disjoint
                      else "NOT READY FOR INDEPENDENT TASK AUTHORING"),
    }
    ok = report.passed and not disjoint

    if args.json:
        _emit(payload, True)
    else:
        composition = result.public_summary()["composition"]
        print(f"selected {composition['selected']} masked targets "
              f"across {composition['distinct_scopes']} scopes")
        print(f"kinds:   {composition['kind_distribution']}")
        print(f"classes: {composition['class_distribution']}")
        print(f"\nauthor packet:   {author_root}")
        print(f"reviewer packet: {reviewer_root}")
        print("\nleakage audit:")
        for line in report.summary_lines():
            print(f"  {line}")
        if report.problems:
            print(_problems("\nAUDIT PROBLEMS:", list(report.problems)))
        if disjoint:
            print(_problems("\nEXPORTS ARE NOT DISJOINT:", disjoint))
        print(f"\n{payload['readiness']}")
    return EXIT_OK if ok else EXIT_FAILED


def cmd_audit_author_packet(args: argparse.Namespace) -> int:
    """Re-audit an export that already exists, from its mapping file."""
    from .authoring import audit

    author_root = Path(args.author_root)
    mapping = json.loads(Path(args.map).read_text(encoding="utf-8"))
    targets = audit.target_identities(mapping.get("packets") or [])

    forbidden: dict[str, str] = {}
    disjoint: list[str] = []
    if args.reviewer_root:
        reviewer_root = Path(args.reviewer_root)
        for path in sorted(reviewer_root.rglob("*")):
            if path.is_file():
                forbidden[canonical.sha256_file(path)] = \
                    path.relative_to(reviewer_root).as_posix()
        disjoint = audit.assert_disjoint(author_root, reviewer_root)

    report = audit.audit_export(author_root, targets, forbidden_digests=forbidden)
    ok = report.passed and not disjoint
    payload = report.to_json_obj()
    payload["export_disjointness_problems"] = disjoint
    payload["readiness"] = (report.readiness if not disjoint
                            else "NOT READY FOR INDEPENDENT TASK AUTHORING")

    if args.json:
        _emit(payload, True)
    else:
        print(f"audited {report.files_scanned} files under {author_root}")
        for line in report.summary_lines():
            print(f"  {line}")
        if report.findings:
            print(_problems("\nFINDINGS:",
                            [f"{f.category}: {f.file}: {f.detail}"
                             for f in report.findings]))
        if disjoint:
            print(_problems("\nEXPORTS ARE NOT DISJOINT:", disjoint))
        print(f"\n{payload['readiness']}")
    return EXIT_OK if ok else EXIT_FAILED


def cmd_review_candidates(args: argparse.Namespace) -> int:
    """Raw, non-PAE candidate discovery for a reviewer."""
    from .authoring import candidates

    result = candidates.discover(
        Path(args.snapshot), args.query,
        repo=Path(args.repo) if args.repo else None,
        max_candidates=args.max_candidates,
        registered_only=not args.include_unregistered,
    )
    if args.json:
        _emit(result.to_json_obj(), True)
    else:
        print(f"query tokens: {', '.join(result.tokens) or '(none)'}")
        print(f"files with at least one hit: {result.files_considered}")
        if result.unregistered_files_outranked:
            print(f"higher-ranked non-resource files hidden: "
                  f"{result.unregistered_files_outranked} "
                  f"(pass --include-unregistered to see them)")
        print(f"ordering: {candidates.RANKING_BASIS}\n")
        for candidate in result.candidates:
            identity = candidate.identity
            label = (f"{identity.kind}/{identity.scope}: {identity.title}"
                     if identity else "(not a registered resource)")
            print(f"{candidate.rank:>3}. {label}")
            print(f"     tokens {len(candidate.matched_tokens)}, "
                  f"hits {candidate.total_hits}")
            if candidate.excerpt_withheld_reason:
                print(f"     excerpt withheld — {candidate.excerpt_withheld_reason}")
        print(f"\nalways available: {', '.join(candidates.REVIEWER_ESCAPE_OPTIONS)}")
    return EXIT_OK


def cmd_check_composition(args: argparse.Namespace) -> int:
    """Plan reconciliation now; acceptance and firewall checks when tasks exist."""
    from .authoring import composition

    payload: dict[str, Any] = {"plan": composition.plan_reconciliation()}
    problems: list[str] = list(payload["plan"]["problems"])

    if args.benchmark_root:
        benchmark = _load_benchmark(Path(args.benchmark_root))
        records = None
        if args.repo:
            from .authoring.selection import load_registry_records

            records = {str(r.get("uid")): r
                       for r in load_registry_records(Path(args.repo))}
        checks = composition.acceptance_checks(benchmark.tasks, records)
        payload["acceptance"] = [c.to_json_obj() for c in checks]
        problems.extend(
            f"acceptance {c.name}: observed {c.observed}, required {c.required}"
            for c in checks if not c.passed
        )
        if args.development_root:
            development = _load_benchmark(Path(args.development_root))
            firewall = composition.firewall_checks(development.tasks, benchmark.tasks)
            payload["firewall"] = [c.to_json_obj() for c in firewall]
            problems.extend(
                f"firewall {c.name}: observed {c.observed}, required {c.required}"
                for c in firewall if not c.passed
            )

    payload["problems"] = problems
    payload["passed"] = not problems
    if args.json:
        _emit(payload, True)
    else:
        plan = payload["plan"]
        print(f"sealed plan: {plan['sealed_total']} = "
              f"{plan['masked_total']} masked + {plan['natural_total']} natural")
        print(f"reconciled: {plan['reconciled']}")
        for key in ("acceptance", "firewall"):
            for check in payload.get(key, []):
                mark = "ok  " if check["passed"] else "FAIL"
                print(f"  {mark} {check['name']}: {check['observed']} "
                      f"(need {check['required']})")
        if problems:
            print(_problems("\nPROBLEMS:", problems))
    return EXIT_OK if not problems else EXIT_FAILED


# --------------------------------------------------------------------------
# parser
# --------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m pae_eval",
        description=(
            "PAE independent evaluation harness. Developer tooling: this is not "
            "part of the installed Engine and is never reachable from `pae`."
        ),
    )
    parser.add_argument("--version", action="version",
                        version=f"pae-eval {HARNESS_VERSION}")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    sub = parser.add_subparsers(dest="command", metavar="COMMAND")

    p = sub.add_parser("validate-benchmark", help="schema, labels, leakage gates")
    p.add_argument("--benchmark-root", required=True)
    p.add_argument("--repo", help="PAE checkout, for label resolution and leakage")
    p.add_argument("--plan", help="plan supplying leakage thresholds")
    p.add_argument("--allow-missing-provenance", action="store_true")
    p.add_argument("--allow-leakage", action="store_true",
                   help="report leakage without failing (fixtures only)")
    p.set_defaults(func=cmd_validate_benchmark)

    p = sub.add_parser("plan", help="render and hash an evaluation plan")
    p.add_argument("--benchmark-root")
    p.add_argument("--repo")
    p.add_argument("--from-plan", help="base plan to extend")
    p.add_argument("--plan", help="plan to verify with --check")
    p.add_argument("--pricing")
    p.add_argument("--out")
    p.add_argument("--mode", choices=("development", "sealed"), default="development")
    p.add_argument("--check", action="store_true",
                   help="recompute and verify a frozen plan")
    p.set_defaults(func=cmd_plan)

    p = sub.add_parser("run", help="dry-run or execute trials")
    p.add_argument("--benchmark-root", required=True)
    p.add_argument("--repo", required=True)
    p.add_argument("--output-dir", required=True)
    p.add_argument("--plan")
    p.add_argument("--pricing")
    p.add_argument("--snapshot-dir")
    p.add_argument("--mode", choices=("development", "sealed"), default="development")
    p.add_argument("--dry-run", action="store_true",
                   help="validate and price without contacting a provider (default)")
    p.add_argument("--execute", action="store_true",
                   help="make real provider calls (requires ceilings)")
    p.add_argument("--max-cost-usd", type=float)
    p.add_argument("--max-trials", type=int)
    p.add_argument("--require-ripgrep", action="store_true", default=False)
    p.add_argument("--no-resume", action="store_true")
    p.add_argument(
        "--fake-quality",
        choices=("pass", "fail", "by_condition", "by_condition_inverted"),
        help=("serve every provider from the deterministic fake instead of a "
              "real one; makes zero network calls and needs no credential"),
    )
    p.set_defaults(func=cmd_run)

    p = sub.add_parser("judge", help="score completed trials")
    p.add_argument("--output-dir", required=True)
    p.add_argument("--benchmark-root", required=True)
    p.add_argument("--plan")
    p.add_argument("--with-llm-judge", action="store_true")
    p.set_defaults(func=cmd_judge)

    p = sub.add_parser("analyze", help="compute the analysis object")
    p.add_argument("--output-dir", required=True)
    p.add_argument("--benchmark-root")
    p.add_argument("--plan")
    p.add_argument("--planned-trials", type=int)
    p.set_defaults(func=cmd_analyze)

    p = sub.add_parser("report", help="render the Markdown report")
    p.add_argument("--output-dir", required=True)
    p.add_argument("--benchmark-root")
    p.add_argument("--plan")
    p.add_argument("--out")
    p.add_argument("--fixture", action="store_true",
                   help=f"stamp the report with: {FIXTURE_MARKER}")
    p.set_defaults(func=cmd_report)

    p = sub.add_parser("layer-a", help="model-free retrieval/routing scoring")
    p.add_argument("--benchmark-root", required=True)
    p.add_argument("--repo")
    p.add_argument("--snapshot")
    p.add_argument("--output-dir")
    p.add_argument("--disclosure")
    p.set_defaults(func=cmd_layer_a)

    p = sub.add_parser("snapshot", help="build a participant snapshot")
    p.add_argument("--repo", required=True)
    p.add_argument("--dest", required=True)
    p.add_argument("--commit", default="HEAD")
    p.add_argument("--require-clean", action="store_true")
    p.set_defaults(func=cmd_snapshot)

    p = sub.add_parser(
        "prepare-authoring",
        help="select masked targets, mask them, and export author + reviewer packets",
    )
    p.add_argument("--repo", required=True)
    p.add_argument("--out-dir", required=True,
                   help="private workspace; never inside the PAE checkout")
    p.add_argument("--commit", required=True,
                   help="the PAE commit the selection is bound to")
    p.add_argument("--development-exclusions",
                   help="development/target-exclusions.json")
    p.add_argument("--created-at", help="ISO timestamp; defaults to now (UTC)")
    p.set_defaults(func=cmd_prepare_authoring)

    p = sub.add_parser("audit-author-packet",
                       help="re-run the leakage audit on an existing export")
    p.add_argument("--author-root", required=True)
    p.add_argument("--map", required=True,
                   help="reviewer-private target-map/packet-target-map.json")
    p.add_argument("--reviewer-root",
                   help="also prove the two exports are disjoint")
    p.set_defaults(func=cmd_audit_author_packet)

    p = sub.add_parser("review-candidates",
                       help="raw non-PAE candidate discovery for a reviewer")
    p.add_argument("--snapshot", required=True)
    p.add_argument("--repo", help="PAE checkout, for identity mapping only")
    p.add_argument("--query", required=True)
    p.add_argument("--max-candidates", type=int, default=12)
    p.add_argument("--include-unregistered", action="store_true",
                   help="also show files with no Registry identity "
                        "(indexes and READMEs outrank everything on raw hits)")
    p.set_defaults(func=cmd_review_candidates)

    p = sub.add_parser("check-composition",
                       help="sealed plan reconciliation, acceptance and firewall")
    p.add_argument("--benchmark-root", help="a completed benchmark to check")
    p.add_argument("--development-root", help="development benchmark, for the firewall")
    p.add_argument("--repo")
    p.set_defaults(func=cmd_check_composition)

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    _configure_streams()
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    if not getattr(args, "func", None):
        parser.print_help()
        return EXIT_USAGE
    try:
        return int(args.func(args))
    except (UsageError, ValidationError) as exc:
        print(f"pae_eval: {exc}", file=sys.stderr)
        return EXIT_USAGE
    except (IsolationError, FrozenPlanError, CostCeilingError) as exc:
        print(f"pae_eval: {exc}", file=sys.stderr)
        return EXIT_FAILED
    except PaeEvalError as exc:
        print(f"pae_eval: {exc}", file=sys.stderr)
        return EXIT_FAILED
