"""The ``pae`` command.

This module owns argument parsing and human formatting, and nothing else.
Every policy decision — discovery precedence, serving policy, path containment,
integrity, validation — lives below the CLI in the library, so a future MCP
server can reach the same behaviour without importing a line of this file.

Two output rules are absolute:

* stdout carries the answer and nothing else; a failing command leaves it empty;
* under ``--json`` an agent gets one machine-readable object and never has to
  parse prose to find out what happened.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Optional, Sequence, TextIO

from ._lexical import DEFAULT_LIMIT, MAX_LIMIT
from ._version import __version__
from .errors import PaeError, UsageError
from .models import RECORD_SCHEMA, SUMMARY_SCHEMA
from .registry import Registry
from .repository import REPO_ENV_VAR, Repository
from .routing import DEFAULT_ROUTE_LIMIT, MAX_ROUTE_LIMIT, Router
from .search import KINDS, SearchEngine
from .validate import raise_if_invalid, validate_registry

__all__ = ["main"]

CONSOLE_NAME = "pae"
DISTRIBUTION_NAME = "prompt-agent-engineering"
IMPORT_NAME = "pae_engine"

_SUPPRESS = argparse.SUPPRESS


def _emit_json(obj: Any, stream: TextIO) -> None:
    """One compact line, UTF-8, stable key order, nothing decorative."""
    stream.write(json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    stream.write("\n")


class _Parser(argparse.ArgumentParser):
    """An ArgumentParser whose own errors honour ``--json``.

    argparse fails before the parsed flags exist, so the raw argv is consulted.
    Without this, a malformed invocation would be the one failure mode that
    broke the machine-readable contract.
    """

    def error(self, message: str) -> "None":  # type: ignore[override]
        if "--json" in sys.argv[1:]:
            _emit_json(
                {
                    "error": "usage_error",
                    "exit_code": 2,
                    "message": message,
                    "command": self.prog,
                },
                sys.stderr,
            )
        else:
            sys.stderr.write(f"{self.prog}: error: {message}\n")
            sys.stderr.write(f"try `{CONSOLE_NAME} --help`\n")
        raise SystemExit(2)


def _build_parser() -> argparse.ArgumentParser:
    parser = _Parser(
        prog=CONSOLE_NAME,
        description=(
            "Read-only runtime for the PAE Registry. Resolves, inspects and serves "
            "governed resources from a local PAE checkout."
        ),
        epilog=(
            f"The checkout is found by --repo, then ${REPO_ENV_VAR}, then the working "
            "directory and its ancestors. Nothing is downloaded and nothing is written."
        ),
    )
    parser.add_argument(
        "--version", action="store_true", help="print engine and registry contract versions"
    )
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument(
        "--repo", metavar="PATH", default=None, help="path to a PAE checkout"
    )

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument(
        "--repo", metavar="PATH", default=_SUPPRESS, help="path to a PAE checkout"
    )
    common.add_argument(
        "--json", action="store_true", default=_SUPPRESS, help="machine-readable output"
    )

    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND")

    subparsers.add_parser(
        "where",
        parents=[common],
        help="report the resolved checkout and how it was found",
        description="Report the resolved checkout. Reads no registry records.",
    )

    stats = subparsers.add_parser(
        "stats",
        parents=[common],
        help="summarize the registry",
        description=(
            "Summarize the registry from its generated summary. Records are counted by "
            "lifecycle, kind, maturity, serving policy and metadata completeness — there "
            "is no single 'prompt count', because the registry holds six kinds."
        ),
    )
    stats.add_argument(
        "--verify",
        action="store_true",
        help="recount the records and fail if the summary disagrees",
    )

    get = subparsers.add_parser(
        "get",
        parents=[common],
        help="resolve a reference and return its record or body",
        description=(
            "Resolve a UID, current public ID or retired alias. Returns metadata by "
            "default; --content returns the whole verified body or nothing."
        ),
    )
    get.add_argument("ref", help="UID (pae_...) or public ID (scope:path)")
    get.add_argument(
        "--content",
        action="store_true",
        help="return the verified source body instead of metadata",
    )

    search = subparsers.add_parser(
        "search",
        parents=[common],
        help="rank resources against a natural-language query",
        description=(
            "Deterministic lexical search over registry metadata. Resource bodies are "
            "never read, so what a resource says cannot affect where it ranks. Scores "
            "order results within one query and are not confidence values."
        ),
    )
    search.add_argument("query", help="natural-language query, or an exact UID / public ID")
    search.add_argument(
        "--kind",
        action="append",
        dest="kinds",
        metavar="KIND",
        help=f"restrict to a kind ({', '.join(KINDS)}); repeatable",
    )
    search.add_argument(
        "--scope",
        action="append",
        dest="scopes",
        metavar="SCOPE",
        help="restrict to a scope; repeatable",
    )
    search.add_argument(
        "--limit",
        type=int,
        default=DEFAULT_LIMIT,
        metavar="N",
        help=f"maximum results (default {DEFAULT_LIMIT}, max {MAX_LIMIT})",
    )
    search.add_argument(
        "--include-deprecated", action="store_true", help="include deprecated resources"
    )
    search.add_argument(
        "--include-tombstones", action="store_true", help="include tombstoned identities"
    )
    search.add_argument(
        "--include-copies",
        action="store_true",
        help="return every physical copy instead of one result per canonical cluster",
    )

    route = subparsers.add_parser(
        "route",
        parents=[common],
        help="decide which scope and kind should handle a task",
        description=(
            "Route a task to a scope and resource kind, with candidate resources. "
            "Reports 'ambiguous', 'weak' or 'no_route' rather than forcing a confident "
            "answer out of thin evidence. Never executes a resource."
        ),
    )
    route.add_argument("task", help="natural-language description of the task")
    route.add_argument(
        "--kind",
        action="append",
        dest="kinds",
        metavar="KIND",
        help=f"restrict candidates to a kind ({', '.join(KINDS)}); repeatable",
    )
    route.add_argument(
        "--limit",
        type=int,
        default=DEFAULT_ROUTE_LIMIT,
        metavar="N",
        help=f"candidate resources to return (default {DEFAULT_ROUTE_LIMIT}, "
        f"max {MAX_ROUTE_LIMIT})",
    )

    validate = subparsers.add_parser(
        "validate-registry",
        parents=[common],
        help="check the registry against consumer trust assumptions",
        description=(
            "Check that this checkout's registry is safe to serve from: identity shape "
            "and uniqueness, alias disjointness, relationship targets, source-path "
            "containment, and summary consistency."
        ),
    )
    validate.add_argument(
        "--verify-checksums",
        action="store_true",
        help="also hash every addressable live source file",
    )
    return parser


# --------------------------------------------------------------------------
# commands
# --------------------------------------------------------------------------


def _cmd_version(as_json: bool, out: TextIO) -> int:
    if as_json:
        _emit_json(
            {
                "console": CONSOLE_NAME,
                "distribution": DISTRIBUTION_NAME,
                "engine_version": __version__,
                "import": IMPORT_NAME,
                "record_schema": RECORD_SCHEMA,
                "summary_schema": SUMMARY_SCHEMA,
            },
            out,
        )
    else:
        out.write(f"{CONSOLE_NAME} {__version__} (registry contract {RECORD_SCHEMA})\n")
    return 0


def _cmd_where(repository: Repository, as_json: bool, out: TextIO) -> int:
    if as_json:
        _emit_json(repository.to_json_obj(), out)
        return 0
    out.write(f"root:   {repository.root}\n")
    out.write(f"source: {repository.discovery_source}\n")
    if repository.search_start is not None:
        out.write(f"from:   {repository.search_start}\n")
    return 0


def _cmd_stats(repository: Repository, verify: bool, as_json: bool, out: TextIO) -> int:
    summary = Registry.open(repository).stats(verify=verify)
    if as_json:
        _emit_json(
            {
                "repository": str(repository.root),
                "summary": summary.to_json_obj(),
                "verified": summary.verified,
            },
            out,
        )
        return 0

    live = summary.by_lifecycle.get("live", 0)
    tombstone = summary.by_lifecycle.get("tombstone", 0)
    out.write(f"repository: {repository.root}\n")
    out.write(f"schema:     {summary.schema}\n")
    out.write(
        f"records:    {summary.total_records} "
        f"(live {live}, tombstone {tombstone})\n"
    )
    out.write(f"recounted:  {'yes' if summary.verified else 'no'}\n")

    out.write("\nby kind (live / total)\n")
    for kind in sorted(summary.by_kind):
        live_n = summary.by_kind_live.get(kind, 0)
        out.write(f"  {kind:<12} {live_n:>6} / {summary.by_kind[kind]}\n")

    if summary.by_kind_tombstone:
        out.write("\ntombstones by kind\n")
        for kind in sorted(summary.by_kind_tombstone):
            out.write(f"  {kind:<12} {summary.by_kind_tombstone[kind]:>6}\n")

    _write_counter(out, "by maturity", summary.by_maturity)
    _write_counter(out, "by serving policy", summary.by_serving_policy)
    _write_counter(out, "by metadata completeness", summary.by_metadata_completeness)
    return 0


def _write_counter(out: TextIO, heading: str, counts: Any) -> None:
    if not counts:
        return
    out.write(f"\n{heading}\n")
    for key in sorted(counts):
        out.write(f"  {key:<22} {counts[key]:>6}\n")


def _cmd_get(
    repository: Repository, ref: str, want_content: bool, as_json: bool, out: TextIO
) -> int:
    registry = Registry.open(repository)

    if want_content:
        content = registry.content(ref)
        if as_json:
            _emit_json(content.to_json_obj(), out)
            return 0
        # Byte-exact. No header, no footer, no added newline: the caller asked
        # for the file, and a resource whose guards must survive intact cannot
        # afford the Engine decorating it.
        buffer = getattr(out, "buffer", None)
        if buffer is None:  # pragma: no cover - only when stdout is redirected in-process
            out.write(content.text())
        else:
            buffer.write(content.data)
            buffer.flush()
        return 0

    resolution, record = registry.lookup(ref)
    if as_json:
        _emit_json(
            {
                "record": record.to_json_obj(),
                "resolution": resolution.to_json_obj(),
                "serving": record.serving_json_obj(),
            },
            out,
        )
        return 0

    _write_record_human(out, record, resolution)
    return 0


def _write_record_human(out: TextIO, record: Any, resolution: Any) -> None:
    out.write(f"uid:           {record.uid}\n")
    out.write(f"id:            {record.id}\n")
    out.write(f"kind:          {record.kind}\n")
    out.write(f"lifecycle:     {record.lifecycle}\n")
    out.write(f"title:         {record.title}\n")
    if record.description:
        out.write(f"description:   {record.description}\n")
    out.write(f"maturity:      {record.maturity}\n")
    out.write(f"review:        {record.review_status}\n")
    out.write(f"eval:          {record.eval_status}\n")
    out.write(f"metadata:      {record.metadata_completeness}\n")

    policy_line = record.serving_policy
    if not record.serving_policy_recognized:
        policy_line += (
            f"  (declared {record.serving_policy_declared!r}; unrecognized, failed closed)"
        )
    out.write(f"serving:       {policy_line}\n")
    if record.guard_preservation:
        note = record.guard_preservation.get("note")
        out.write(
            "guards:        must not truncate"
            + (f" — {note}" if note else "")
            + "\n"
        )

    if record.has_body:
        out.write(f"source:        {record.source_path}\n")
        out.write(f"checksum:      {record.content_sha256}\n")
        out.write(
            "content:       "
            + ("available (pass --content)\n" if record.content_available else "withheld by policy\n")
        )
    elif record.lifecycle == "tombstone":
        out.write("content:       none — this identity is a tombstone; the body no longer exists\n")
    else:
        out.write("content:       none — no independently addressable body\n")
        if record.defined_in:
            out.write(f"defined in:    {record.defined_in}\n")

    if record.aliases:
        out.write(f"aliases:       {', '.join(record.aliases)}\n")
    if resolution.ref_kind == "alias":
        out.write(
            f"resolved via:  retired alias {resolution.matched_alias} -> "
            f"{resolution.current_id}\n"
        )
    if resolution.replacement:
        refs = ", ".join(
            str(edge.get("ref")) for edge in resolution.replacement.get("edges", [])
        )
        out.write(f"replacement:   {resolution.replacement['relation']} -> {refs}\n")


def _cmd_search(repository: Repository, args: Any, as_json: bool, out: TextIO) -> int:
    engine = SearchEngine(
        Registry.open(repository),
        include_deprecated=bool(args.include_deprecated),
        include_tombstones=bool(args.include_tombstones),
    )
    results = engine.search(
        args.query,
        kinds=args.kinds,
        scopes=args.scopes,
        limit=args.limit,
        include_copies=bool(args.include_copies),
    )
    if as_json:
        _emit_json(results.to_json_obj(), out)
        return 0

    for notice in results.notices:
        out.write(f"note: {notice}\n")
    if not results.hits:
        out.write(f"no results for {results.query!r}\n")
        out.write(f"terms: {' '.join(results.normalized_terms)}\n")
        return 0

    shown = len(results.hits)
    out.write(f"{results.total_matched} result(s); showing {shown}\n")
    out.write(f"terms: {' '.join(results.normalized_terms)}\n\n")
    for hit in results.hits:
        out.write(f"{hit.rank:>2}. {hit.id}\n")
        out.write(
            f"    {hit.kind} · {hit.scope} · score {hit.score:.3f}\n"
            if hit.matched_fields != ("exact_reference",)
            else f"    {hit.kind} · {hit.scope} · exact reference\n"
        )
        out.write(f"    {hit.title}\n")
        for field in hit.matched_fields:
            out.write(f"    {field}: {' '.join(hit.match_terms[field])}\n")
        if hit.copy_uids:
            out.write(f"    copies: {len(hit.copy_uids)} other member(s) of this cluster\n")
        out.write("\n")
    return 0


def _cmd_route(repository: Repository, args: Any, as_json: bool, out: TextIO) -> int:
    engine = SearchEngine(Registry.open(repository))
    decision = Router(engine).route(args.task, kinds=args.kinds, limit=args.limit)
    if as_json:
        _emit_json(decision.to_json_obj(), out)
        return 0

    out.write(f"status:   {decision.status}\n")
    out.write(f"scope:    {decision.selected_scope or '— none selected'}\n")
    out.write(f"kind:     {decision.selected_kind or '— none selected'}\n")
    out.write(f"coverage: {decision.coverage:.2f}   margin: {decision.margin:.2f}\n")

    if decision.candidate_scopes:
        out.write("\ncandidate scopes\n")
        for candidate in decision.candidate_scopes[:5]:
            out.write(
                f"  {candidate.name:<34} {candidate.score:>8.3f}  "
                f"({candidate.hit_count} hit(s))\n"
            )
    if decision.candidate_kinds:
        out.write("\ncandidate kinds\n")
        for candidate in decision.candidate_kinds:
            out.write(
                f"  {candidate.name:<34} {candidate.score:>8.3f}  "
                f"({candidate.hit_count} hit(s))\n"
            )
    if decision.resources:
        out.write("\nstart from\n")
        for hit in decision.resources:
            out.write(f"  {hit.id}\n      {hit.title}\n")
    out.write("\nwhy\n")
    for reason in decision.reasons:
        out.write(f"  - {reason}\n")
    return 0


def _cmd_validate(
    repository: Repository, verify_checksums: bool, as_json: bool, out: TextIO
) -> int:
    report = validate_registry(repository, verify_checksums=verify_checksums)
    raise_if_invalid(report)
    if as_json:
        _emit_json(report.to_json_obj(), out)
        return 0
    for key in sorted(report.checked):
        out.write(f"{key + ':':<20}{report.checked[key]}\n")
    out.write(
        f"{'checksums:':<20}{'verified' if report.checksums_verified else 'not verified'}\n"
    )
    out.write(f"{'result:':<20}ok — no problems found\n")
    return 0


# --------------------------------------------------------------------------
# entry point
# --------------------------------------------------------------------------


def _report_error(exc: PaeError, as_json: bool, err: TextIO) -> int:
    if as_json:
        _emit_json(exc.to_json_obj(), err)
        return exc.exit_code
    err.write(f"{CONSOLE_NAME}: {exc.error}: {exc.message}\n")
    issues = exc.details.get("issues")
    if isinstance(issues, list):
        for issue in issues:
            err.write(f"  [{issue.get('code')}] {issue.get('message')}\n")
    return exc.exit_code


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(list(sys.argv[1:] if argv is None else argv))
    as_json = bool(getattr(args, "json", False))
    out = sys.stdout
    err = sys.stderr

    try:
        if args.command is None:
            if args.version:
                return _cmd_version(as_json, out)
            parser.print_help(err)
            raise UsageError("no command given")

        repository = Repository.discover(getattr(args, "repo", None))

        if args.command == "where":
            return _cmd_where(repository, as_json, out)
        if args.command == "stats":
            return _cmd_stats(repository, bool(args.verify), as_json, out)
        if args.command == "get":
            return _cmd_get(repository, args.ref, bool(args.content), as_json, out)
        if args.command == "search":
            return _cmd_search(repository, args, as_json, out)
        if args.command == "route":
            return _cmd_route(repository, args, as_json, out)
        if args.command == "validate-registry":
            return _cmd_validate(repository, bool(args.verify_checksums), as_json, out)

        raise UsageError(f"unknown command: {args.command}")
    except PaeError as exc:
        return _report_error(exc, as_json, err)
    except BrokenPipeError:  # pragma: no cover - depends on the consumer
        return 0
    except KeyboardInterrupt:  # pragma: no cover - interactive only
        err.write("\ninterrupted\n")
        return 130
    except Exception as exc:  # noqa: BLE001 - the last line of defence
        wrapped = PaeError(f"unhandled engine error: {exc.__class__.__name__}: {exc}")
        return _report_error(wrapped, as_json, err)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
