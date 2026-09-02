"""Pre-run contamination scan and the isolation gate.

Every check here fails closed and runs before the first paid request. That
ordering is the whole point: an isolation problem discovered from the results is
not a finding to note in the limitations, it is a run that has to be thrown
away.

The scan inspects the *serialized request* each condition is about to send —
not the intent behind it — because a contamination bug is almost always a
plumbing accident, and plumbing is exactly what a serialized payload shows.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from . import canonical
from .constants import CONDITION_A, CONDITION_B, CONDITION_C, CONDITION_D
from .errors import IsolationError


@dataclass
class IsolationCheck:
    name: str
    passed: bool
    detail: str = ""

    def to_json_obj(self) -> dict[str, Any]:
        return {"name": self.name, "passed": self.passed, "detail": self.detail}


@dataclass
class IsolationReport:
    checks: tuple[IsolationCheck, ...]

    @property
    def passed(self) -> bool:
        return all(c.passed for c in self.checks)

    @property
    def failures(self) -> tuple[IsolationCheck, ...]:
        return tuple(c for c in self.checks if not c.passed)

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "passed": self.passed,
            "checks": [c.to_json_obj() for c in self.checks],
        }

    def raise_if_failed(self) -> None:
        if self.passed:
            return
        detail = "\n  ".join(f"{c.name}: {c.detail}" for c in self.failures)
        raise IsolationError(
            "condition isolation failed; refusing to run:\n  " + detail
        )


# --------------------------------------------------------------------------
# request contamination scan (spec §41)
# --------------------------------------------------------------------------


def gold_markers_for(task: Any) -> list[str]:
    """Strings that could only appear in a request if gold data leaked in.

    Deliberately *not* included: ``acceptable_scopes`` and
    ``acceptable_route_statuses``. Those are short, generic vocabulary —
    ``software-engineering`` is a directory name that legitimately appears
    inside the corpus material Condition C injects, and ``weak`` is an English
    word. Treating them as secrets produces constant false positives, and a
    contamination alarm that cries wolf is one that gets switched off.

    What is actually the answer key: the resource UIDs, the label rationale
    written by the benchmark author, and the label field names themselves —
    whose presence means a raw label object was serialized into a prompt.
    """
    markers: list[str] = []
    markers += [r.uid for r in getattr(task, "acceptable_resource_uids", ())]
    if getattr(task, "label_rationale", ""):
        markers.append(task.label_rationale)
    markers += [
        "acceptable_resource_uids", "acceptable_route_statuses",
        "acceptable_scopes", "acceptable_kinds",
        "label_rationale", "label_provenance", "scored_dimensions",
        "leakage_audit", "canonical_policy",
    ]
    return [m for m in markers if m and len(str(m)) >= 8]


def serialize_request(request: Any) -> str:
    """Flatten a ModelRequest to the text that will cross the wire."""
    parts = [request.system]
    for message in request.messages:
        parts.append(message.content or "")
        for call in getattr(message, "tool_calls", ()):
            parts.append(canonical.canonical_json(call.to_json_obj()))
        for result in getattr(message, "tool_results", ()):
            parts.append(result.content or "")
    for spec in request.tools:
        parts.append(spec.name)
        parts.append(spec.description)
        parts.append(canonical.canonical_json(dict(spec.input_schema)))
    return "\n".join(p for p in parts if p)


def scan_request(
    context: Any,
    task: Any,
    *,
    benchmark_root: Path | None = None,
    other_condition_outputs: Iterable[str] = (),
) -> list[IsolationCheck]:
    """Check one built condition's outgoing request for contamination."""
    payload = serialize_request(context.request)
    checks: list[IsolationCheck] = []

    # Condition C legitimately carries resource bodies, and a body may mention
    # its own identifiers. What must never appear is the *label* — the answer
    # key — so uid markers are exempted only for the arm that was handed the
    # bundle on purpose, and the label-field names are checked everywhere.
    label_markers = [
        m for m in gold_markers_for(task)
        if not (context.condition == CONDITION_C and m.startswith("pae_"))
    ]
    hits = [m for m in label_markers if str(m) in payload]
    checks.append(IsolationCheck(
        name=f"{context.condition}: no gold labels in request",
        passed=not hits,
        detail="" if not hits else f"found {hits[:3]}",
    ))

    if benchmark_root is not None:
        root = str(Path(benchmark_root).resolve())
        leaked = root in payload
        checks.append(IsolationCheck(
            name=f"{context.condition}: benchmark path absent from request",
            passed=not leaked,
            detail="" if not leaked else "the benchmark filesystem path appears",
        ))

    foreign = [out for out in other_condition_outputs if out and out in payload]
    checks.append(IsolationCheck(
        name=f"{context.condition}: no other-condition output in request",
        passed=not foreign,
        detail="" if not foreign else "another condition's answer appears",
    ))

    # Condition names are operationally meaningless to the participant and
    # would tell it which arm it is in.
    named = [
        label for label in ("condition A", "condition B", "condition C", "condition D")
        if label in payload
    ]
    checks.append(IsolationCheck(
        name=f"{context.condition}: request does not name a condition",
        passed=not named,
        detail="" if not named else f"found {named}",
    ))
    return checks


# --------------------------------------------------------------------------
# structural gate over a whole run
# --------------------------------------------------------------------------


def preflight(
    contexts: Sequence[Any],
    *,
    task: Any,
    benchmark_root: Path | None,
    snapshot_root: Path | None,
    expected_mcp_catalog: str | None = None,
    output_dir: Path | None = None,
) -> IsolationReport:
    """Full pre-run gate for one task's set of conditions."""
    from .conditions import assert_condition_isolation, assert_prompt_fairness
    from .snapshot import assert_benchmark_outside

    checks: list[IsolationCheck] = []

    # -- benchmark containment ---------------------------------------------
    if benchmark_root is not None:
        try:
            forbidden = [p for p in (snapshot_root, output_dir) if p is not None]
            assert_benchmark_outside(benchmark_root, *forbidden)
            checks.append(IsolationCheck(
                "benchmark root is outside the participant snapshot", True))
        except IsolationError as exc:
            checks.append(IsolationCheck(
                "benchmark root is outside the participant snapshot", False, str(exc)))

    # -- per-condition structure -------------------------------------------
    for context in contexts:
        try:
            assert_condition_isolation(
                context, expected_mcp_catalog=expected_mcp_catalog,
                snapshot_root=snapshot_root,
            )
            checks.append(IsolationCheck(
                f"{context.condition}: structural isolation", True))
        except IsolationError as exc:
            checks.append(IsolationCheck(
                f"{context.condition}: structural isolation", False, str(exc)))

    # -- prompt fairness ---------------------------------------------------
    try:
        assert_prompt_fairness(contexts)
        checks.append(IsolationCheck("all conditions share the base system prompt", True))
    except IsolationError as exc:
        checks.append(IsolationCheck(
            "all conditions share the base system prompt", False, str(exc)))

    # -- request contamination --------------------------------------------
    for context in contexts:
        checks.extend(scan_request(context, task, benchmark_root=benchmark_root))

    return IsolationReport(checks=tuple(checks))


def assert_engine_import_direction() -> IsolationCheck:
    """The Engine must never import the harness.

    Checked at runtime as well as by the code scan, because an accidental
    import would make evaluation code part of the product runtime.
    """
    import sys

    offenders = [
        name for name, module in list(sys.modules.items())
        if name.startswith("pae_engine")
        and getattr(module, "__dict__", None)
        and any(
            isinstance(value, type(sys))
            and getattr(value, "__name__", "").startswith("pae_eval")
            for value in vars(module).values()
        )
    ]
    return IsolationCheck(
        name="pae_engine does not import pae_eval",
        passed=not offenders,
        detail="" if not offenders else f"offending modules: {offenders[:5]}",
    )


def assert_judge_isolation(payload: str, *, condition_labels: Iterable[str] = (),
                           pae_markers: Iterable[str] = ()) -> IsolationCheck:
    """The judge payload must carry no condition identity and no PAE trace."""
    markers = list(condition_labels) + list(pae_markers)
    hits = [m for m in markers if m and m in payload]
    return IsolationCheck(
        name="judge payload is blind to condition",
        passed=not hits,
        detail="" if not hits else f"found {hits[:3]}",
    )
