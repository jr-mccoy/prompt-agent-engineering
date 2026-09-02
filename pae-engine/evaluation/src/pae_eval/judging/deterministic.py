"""Deterministic graders.

Every criterion answered here is free, stable, and immune to judge drift, so
push as much rubric weight into this file as a rubric honestly can. Phase 7A
estimated ~55–60% of weight is mechanically checkable: required strings, JSON
validity, section presence, forbidden leakage, format gates, tool-use
constraints.

Rules are data, not code. The harness supplies *rule kinds*; a benchmark's
rubric supplies the arguments. Task-specific business correctness deliberately
does not live here (spec §59) — the moment the harness knows what a good DCF
model looks like, the harness is part of the benchmark.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any, Callable, Mapping, Sequence

from ..errors import ValidationError


@dataclass(frozen=True)
class CheckResult:
    passed: bool
    detail: str
    rule: str

    def to_json_obj(self) -> dict[str, Any]:
        return {"passed": self.passed, "detail": self.detail, "rule": self.rule}


Rule = Callable[[str, Mapping[str, Any], Mapping[str, Any]], CheckResult]


def _ok(rule: str, detail: str = "") -> CheckResult:
    return CheckResult(True, detail, rule)


def _no(rule: str, detail: str) -> CheckResult:
    return CheckResult(False, detail, rule)


# --------------------------------------------------------------------------
# rule implementations
# --------------------------------------------------------------------------


def contains_all(answer: str, args: Mapping[str, Any], _ctx: Mapping[str, Any]
                 ) -> CheckResult:
    needles = list(args.get("strings") or [])
    ci = bool(args.get("case_insensitive", True))
    hay = answer.casefold() if ci else answer
    missing = [n for n in needles if (n.casefold() if ci else n) not in hay]
    if missing:
        return _no("contains_all", f"missing required text: {missing[:5]}")
    return _ok("contains_all", f"all {len(needles)} required strings present")


def contains_none(answer: str, args: Mapping[str, Any], _ctx: Mapping[str, Any]
                  ) -> CheckResult:
    needles = list(args.get("strings") or [])
    ci = bool(args.get("case_insensitive", True))
    hay = answer.casefold() if ci else answer
    present = [n for n in needles if (n.casefold() if ci else n) in hay]
    if present:
        return _no("contains_none", f"forbidden text present: {present[:5]}")
    return _ok("contains_none", "no forbidden text present")


def matches_regex(answer: str, args: Mapping[str, Any], _ctx: Mapping[str, Any]
                  ) -> CheckResult:
    pattern = str(args.get("pattern", ""))
    flags = re.IGNORECASE if args.get("case_insensitive", True) else 0
    if not pattern:
        raise ValidationError("matches_regex needs a 'pattern'")
    expect = bool(args.get("expect", True))
    found = re.search(pattern, answer, flags) is not None
    if found == expect:
        return _ok("matches_regex", f"pattern {'found' if found else 'absent'} as required")
    return _no("matches_regex",
               f"pattern {pattern!r} was {'found' if found else 'not found'}")


def valid_json(answer: str, args: Mapping[str, Any], _ctx: Mapping[str, Any]
               ) -> CheckResult:
    text = _extract_code_block(answer) if args.get("in_code_block", True) else answer
    try:
        parsed = json.loads(text)
    except (json.JSONDecodeError, TypeError) as exc:
        return _no("valid_json", f"answer does not contain valid JSON: {exc}")
    required = list(args.get("required_fields") or [])
    if required:
        if not isinstance(parsed, Mapping):
            return _no("valid_json", "JSON is not an object, so fields cannot be checked")
        missing = [f for f in required if f not in parsed]
        if missing:
            return _no("valid_json", f"JSON missing fields: {missing}")
    return _ok("valid_json", "valid JSON with all required fields")


def has_sections(answer: str, args: Mapping[str, Any], _ctx: Mapping[str, Any]
                 ) -> CheckResult:
    headings = {
        line.lstrip("#").strip().casefold()
        for line in answer.splitlines() if line.lstrip().startswith("#")
    }
    required = [str(s) for s in (args.get("sections") or [])]
    missing = [s for s in required if s.casefold() not in headings]
    if missing:
        return _no("has_sections", f"missing sections: {missing}")
    return _ok("has_sections", f"all {len(required)} sections present")


def min_length(answer: str, args: Mapping[str, Any], _ctx: Mapping[str, Any]
               ) -> CheckResult:
    words = len(answer.split())
    floor = int(args.get("words", 1))
    if words < floor:
        return _no("min_length", f"{words} words, needs at least {floor}")
    return _ok("min_length", f"{words} words")


def no_absolute_paths(answer: str, _args: Mapping[str, Any],
                      _ctx: Mapping[str, Any]) -> CheckResult:
    """Absolute filesystem paths in an answer are a leak, not a deliverable."""
    patterns = (
        r"(?<![\w.])/(?:home|Users|root|var|tmp|etc|mnt)/[\w./-]+",
        r"[A-Za-z]:[\\/](?:Users|Windows|Program Files)[\\/][\w\\/. -]+",
        r"\\\\[\w.-]+\\[\w$.-]+",
    )
    for pattern in patterns:
        found = re.search(pattern, answer)
        if found:
            return _no("no_absolute_paths",
                       f"answer discloses an absolute path: {found.group(0)[:60]!r}")
    return _ok("no_absolute_paths", "no absolute paths disclosed")


def no_gold_leakage(answer: str, args: Mapping[str, Any],
                    ctx: Mapping[str, Any]) -> CheckResult:
    """The answer must not quote evaluation metadata it could only have leaked."""
    markers = list(args.get("markers") or [])
    markers += [str(u) for u in (ctx.get("acceptable_resource_uids") or [])]
    markers += ["label_rationale", "acceptable_resource_uids", "scored_dimensions"]
    hits = [m for m in markers if m and m in answer]
    if hits:
        return _no("no_gold_leakage", f"answer contains evaluation metadata: {hits[:3]}")
    return _ok("no_gold_leakage", "no evaluation metadata in the answer")


def tool_use_within(answer: str, args: Mapping[str, Any],
                    ctx: Mapping[str, Any]) -> CheckResult:
    """Constrain observable tool behaviour, e.g. a maximum call count."""
    calls = list(ctx.get("observable_tool_calls") or [])
    max_calls = args.get("max_calls")
    if max_calls is not None and len(calls) > int(max_calls):
        return _no("tool_use_within",
                   f"{len(calls)} tool calls exceeds the limit of {max_calls}")
    forbidden = set(args.get("forbidden_tools") or [])
    used = {c.get("tool") for c in calls}
    overlap = sorted(forbidden & used)
    if overlap:
        return _no("tool_use_within", f"used forbidden tools: {overlap}")
    required = set(args.get("required_tools") or [])
    if required and not required <= used:
        return _no("tool_use_within",
                   f"did not use required tools: {sorted(required - used)}")
    return _ok("tool_use_within", f"{len(calls)} tool calls within constraints")


def bundle_bodies_whole(_answer: str, _args: Mapping[str, Any],
                        ctx: Mapping[str, Any]) -> CheckResult:
    """A compiled bundle must never contain a shortened guarded body.

    An Engine invariant surfaced as a rubric criterion, so a safety-gated task
    can assert it per trial rather than only in the Engine's own suite.
    """
    bundle = ctx.get("route_bundle") or {}
    if not bundle:
        return _ok("bundle_bodies_whole", "no bundle in this condition")
    truncated = [
        item.get("uid") for item in (bundle.get("omitted") or [])
        if item.get("reason") not in (None, "", "budget", "oversized", "excluded",
                                      "filtered")
    ]
    if truncated:
        return _no("bundle_bodies_whole",
                   f"unexpected omission reasons: {truncated[:5]}")
    return _ok("bundle_bodies_whole", "all omissions carry known reason codes")


RULES: Mapping[str, Rule] = {
    "contains_all": contains_all,
    "contains_none": contains_none,
    "matches_regex": matches_regex,
    "valid_json": valid_json,
    "has_sections": has_sections,
    "min_length": min_length,
    "no_absolute_paths": no_absolute_paths,
    "no_gold_leakage": no_gold_leakage,
    "tool_use_within": tool_use_within,
    "bundle_bodies_whole": bundle_bodies_whole,
}


def _extract_code_block(text: str) -> str:
    """The first fenced block, or the whole text when there is no fence."""
    match = re.search(r"```(?:json)?\s*\n(.*?)```", text, re.DOTALL)
    return match.group(1) if match else text


def run_rule(rule: Mapping[str, Any], answer: str,
             context: Mapping[str, Any]) -> CheckResult:
    kind = str(rule.get("kind", ""))
    handler = RULES.get(kind)
    if handler is None:
        raise ValidationError(
            f"unknown deterministic rule kind {kind!r}; "
            f"known kinds: {', '.join(sorted(RULES))}"
        )
    return handler(answer, rule.get("args") or {}, context)


def available_rules() -> tuple[str, ...]:
    return tuple(sorted(RULES))
