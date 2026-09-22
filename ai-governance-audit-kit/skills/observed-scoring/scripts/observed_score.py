#!/usr/bin/env python3
"""observed_score.py — score an artifact from what is *in* it, not from what it claims.

Part of ai-governance-audit-kit. Stdlib-only; no network, no LLM.

**The difference from the factory's scorer.**
``agentic-system-factory/scripts/score_rubric.py`` scores a ``<!-- RUBRIC -->``
block the author wrote about their own bundle. Its honesty caveat says so
outright: the per-category numbers are self-reported, and the script enforces
the caps and the load-bearing minimums rather than the truth of the numbers.
That is the right design for a curator scoring their own work. An audit cannot
use it, because the thing under audit is the author's own account.

So the caps, the load-bearing minimum, the tier-capping behaviour, the CLI and
the exit-code contract are kept; ``parse_rubric`` is replaced by **detectors
that read the artifact**. Every detector is pure regex or a filesystem fact.
Nothing here needs a model, and nothing here reads the author's score.

**What this deliberately cannot do.** Most of the 100-point rubric is not
mechanically observable. "Describes WHAT the skill does", "logical section
ordering", "content is accurate" are judgements. Scoring them with a regex and
reporting 100 as the denominator would be the exact fabrication
``pae_registry/governance.py`` refuses when it declines to infer a quality tier
from document structure: *"inferring one from document structure would be
fabricating a rubric score."*

This script therefore reports an **observable subset** with the subset's own
maximum stated beside it (54 of the rubric's 100 points), and it emits
``tier: null``. It never says "this artifact is Tier 3". A structural finding
with a path and a quoted line is a fact; a tier is not.

Gate A — SCOREABLE. A score without a named rubric version and a stated
observed-versus-self-reported provenance is not a finding, and this script
refuses to emit one.

Usage:
  python3 observed_score.py <bundle_or_file> [--config PATH] [--json]
  python3 observed_score.py --gate-a <score.json>
  python3 observed_score.py --self-check

Exit code: 0 = PASS (no blocking security finding, Gate A satisfied),
1 = FAIL, 2 = usage error.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
KIT_ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
DEFAULT_CONFIG = os.path.join(KIT_ROOT, "config", "audit.json")

#: Rubric category → (points the full rubric allots, points observable here).
#: The second number is the honest denominator. Reporting the first would claim
#: coverage of judgements no regex can make.
CATS = {
    "cat1_metadata": (20, 11),
    "cat2_structure": (20, 14),
    "cat3_content": (25, 7),
    "cat4_resources": (15, 9),
    "cat5_safety": (20, 13),
}
RUBRIC_MAX = sum(full for full, _ in CATS.values())          # 100
OBSERVABLE_MAX = sum(observable for _, observable in CATS.values())  # 54

#: The rubric's own "Must Pass (Blocking)" security checks. A failure here caps
#: the verdict regardless of the total, the same way ``score_rubric.py``'s
#: ``SECURITY_MIN`` caps the tier regardless of the total.
BLOCKING_CHECKS = ("no_hardcoded_secret", "no_absolute_user_path", "no_personal_contact")

RECOGNIZED_PROVENANCE = ("observed", "self_reported")

_FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)
_NAME_OK = re.compile(r"\A[a-z0-9]+(?:-[a-z0-9]+)*\Z")
_FIRST_SECOND_PERSON = re.compile(r"\b(?:I|we|our|you|your|my|me|us)\b", re.I)
_TRIGGER = re.compile(
    r"use (?:this|the) skill when|use when|use this when|activates? when|"
    r"when the user|trigger(?:s|ed)? (?:when|by)",
    re.I,
)
_SECRET = re.compile(
    r"(?:api[_-]?key|secret|passwd|password|token|bearer|private[_-]?key)"
    r"\s*[:=]\s*[\"']?[A-Za-z0-9_\-./+]{12,}"
    r"|AKIA[0-9A-Z]{16}"
    r"|-----BEGIN [A-Z ]*PRIVATE KEY-----",
    re.I,
)
_ABSOLUTE_USER_PATH = re.compile(r"(?:/Users/|/home/|[A-Za-z]:\\Users\\)[A-Za-z0-9._-]+/")
#: An email, or a phone number in a shape a human would dial. The phone half is
#: deliberately narrow: an earlier draft matched ``2026-06-18`` — an ISO date is
#: ten characters of digits and hyphens, and a detector that reports every
#: ``updated:`` line as leaked contact detail would train its reader to ignore
#: it, which is worse than not running.
_CONTACT = re.compile(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    r"|(?<!\d)(?:\+\d{1,3}[ .-]?)?\(?\d{3}\)?[ .-]\d{3}[ .-]\d{4}(?!\d)"
)
_ISO_DATE = re.compile(r"\A\d{4}-\d{2}-\d{2}\Z")
_ENV_USE = re.compile(
    r"\b(?:os\.environ|getenv|environ\[|\$\{?[A-Z][A-Z0-9_]{2,}\}?"
    r"|environment variable|from the environment)"
)
_SENSITIVE_NAME = re.compile(r"\b[A-Z][A-Z0-9_]*(?:TOKEN|KEY|SECRET|PASSWORD|CREDENTIAL)S?\b")
_BACKTICK_PATH = re.compile(r"`([A-Za-z0-9_][A-Za-z0-9_./-]*/[A-Za-z0-9_.-]+)`")
_NUMBERED_STEP = re.compile(r"^\s{0,3}\d+\.\s+\S", re.M)
_FENCE = re.compile(r"(```|~~~)")
_DOCSTRING = re.compile(r'\A(?:#![^\n]*\n)?(?:\s*(?:#[^\n]*\n)|\s*\n)*\s*(?:"""|\'\'\')')
_RUBRIC_BLOCK = re.compile(r"<!--\s*RUBRIC\b(.*?)-->", re.S)


def _read(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return None


def _strip_code(text):
    """Drop fenced blocks and inline code spans before a *prose* detector runs.

    Same rule as ``check_gate.py``: a documented example must never satisfy or
    trip a check. Security detectors deliberately run on the **unstripped**
    text, because a secret inside a fence is still a secret in the file.
    """
    text = re.sub(r"(```|~~~).*?\1", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def _heading(text, *patterns):
    for pattern in patterns:
        if re.search(rf"^#{{1,6}}\s*{pattern}", text, re.M | re.I):
            return True
    return False


# ---------------------------------------------------------------- target


def resolve_target(path):
    """Return ``(skill_md_path, bundle_dir or None)``.

    A directory is read as a skill bundle; a file is read alone, and the
    bundle-shaped detectors then score 0 with the reason recorded rather than
    being silently skipped.
    """
    if os.path.isdir(path):
        return os.path.join(path, "SKILL.md"), path
    return path, None


def _bundle_files(bundle):
    if not bundle:
        return []
    found = []
    for dirpath, dirnames, filenames in os.walk(bundle):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith((".", "__")))
        for name in sorted(filenames):
            full = os.path.join(dirpath, name)
            found.append((os.path.relpath(full, bundle).replace(os.sep, "/"), full))
    return found


# ---------------------------------------------------------------- detectors


def detect(path, cfg):
    """Run every observable detector. Returns ``(checks, findings)``.

    ``checks`` maps ``category -> {check_name: points_awarded}``; ``findings``
    is the evidence list, each entry naming the check, the path and what was
    seen. A finding is a fact with a location; that is the whole contract.
    """
    skill_md, bundle = resolve_target(path)
    raw = _read(skill_md)
    findings = []
    checks = {cat: {} for cat in CATS}

    if raw is None:
        findings.append({
            "check": "artifact_readable",
            "path": os.path.relpath(skill_md, KIT_ROOT) if skill_md else str(path),
            "detail": "file could not be read",
            "severity": "blocking",
        })
        return checks, findings

    prose = _strip_code(raw)
    fm = _FRONTMATTER.search(raw)
    block = fm.group(1) if fm else ""
    name_match = re.search(r"^name\s*:\s*(.+?)\s*$", block, re.M)
    name = (name_match.group(1).strip().strip("'\"") if name_match else "")
    desc_match = re.search(r"^description\s*:\s*(.+?)\s*$", block, re.M)
    description = (desc_match.group(1).strip().strip("'\"") if desc_match else "")
    lines = raw.count("\n") + 1
    rel = os.path.relpath(skill_md, os.path.dirname(bundle) if bundle else ".")

    def award(cat, check, points, passed, detail=None, severity="finding"):
        checks[cat][check] = points if passed else 0
        if not passed:
            findings.append({
                "check": check,
                "category": cat,
                "path": rel,
                "points_lost": points,
                "detail": detail or f"{check} not satisfied",
                "severity": severity,
            })

    # ---- cat1 metadata (11 observable of 20)
    award("cat1_metadata", "name_length", 1, 1 <= len(name) <= 64,
          f"name is {len(name)} characters")
    award("cat1_metadata", "name_lowercase", 1, bool(name) and name == name.lower(),
          f"name {name!r} is not lowercase")
    award("cat1_metadata", "name_charset", 1, bool(_NAME_OK.match(name)),
          f"name {name!r} is not alphanumeric-and-single-hyphens")
    award("cat1_metadata", "name_no_edge_hyphens", 1,
          bool(name) and not name.startswith("-") and not name.endswith("-")
          and "--" not in name,
          f"name {name!r} has a leading, trailing or doubled hyphen")
    expected = os.path.basename(bundle.rstrip("/")) if bundle else None
    award("cat1_metadata", "name_matches_directory", 1,
          bool(expected) and name == expected,
          f"name {name!r} does not match bundle directory {expected!r}"
          if expected else "not a bundle, so there is no directory to match")
    award("cat1_metadata", "description_length_band", 2,
          50 <= len(description) <= 500,
          f"description is {len(description)} characters, outside the 50-500 band")
    award("cat1_metadata", "description_third_person", 2,
          bool(description) and not _FIRST_SECOND_PERSON.search(description),
          "description uses first- or second-person voice")
    award("cat1_metadata", "description_states_trigger", 2,
          bool(_TRIGGER.search(description)),
          "description names no trigger condition (no \"use when\" / "
          "\"activates when\" / \"when the user\")")

    # ---- cat2 structure (14 observable of 20)
    award("cat2_structure", "under_500_lines", 2, lines < 500,
          f"{lines} lines, over the 500-line progressive-disclosure ceiling")
    references = [r for r, _ in _bundle_files(bundle) if r.startswith("references/")]
    award("cat2_structure", "long_content_pushed_to_references", 2,
          lines < 300 or bool(references),
          f"{lines} lines with no references/ directory to disclose into")
    backticked = sorted(set(_BACKTICK_PATH.findall(raw)))
    award("cat2_structure", "explicit_bundled_references", 2, bool(backticked),
          "no bundled resource is referenced explicitly from the body")
    award("cat2_structure", "when_to_use_section", 1,
          _heading(prose, r"When to Use"), "no \"When to Use\" section")
    award("cat2_structure", "when_not_to_use_section", 1,
          _heading(prose, r"When NOT to Use", r"When Not to Use"),
          "no \"When NOT to Use\" section")
    award("cat2_structure", "related_section", 2,
          _heading(prose, r"Related"), "no Related section")
    award("cat2_structure", "skill_md_at_root", 2, os.path.isfile(skill_md),
          "SKILL.md is not present at the bundle root")
    nested = [r for r, _ in _bundle_files(bundle)
              if r.endswith("SKILL.md") and r != "SKILL.md"]
    award("cat2_structure", "no_nested_skill", 1, not nested,
          f"nested skill bundle(s): {', '.join(nested)}")
    component_dirs = set((cfg.get("membership") or {}).get("component_dirs") or [])
    stray_dirs = sorted({
        r.split("/", 1)[0] for r, _ in _bundle_files(bundle) if "/" in r
    } - component_dirs)
    award("cat2_structure", "resource_dirs_named_conventionally", 1, not stray_dirs,
          f"unrecognized resource directory: {', '.join(stray_dirs)}")

    # ---- cat3 content (7 observable of 25)
    award("cat3_content", "numbered_instruction_steps", 3,
          len(_NUMBERED_STEP.findall(raw)) >= 3,
          "fewer than three numbered instruction steps")
    award("cat3_content", "verification_section", 2,
          _heading(prose, r"Verification", r"Validation"),
          "no Verification or Validation section")
    award("cat3_content", "worked_example_present", 2,
          bool(_FENCE.search(raw)) or bool(re.search(r"^\s{4,}\S", raw, re.M)),
          "no fenced or indented example anywhere in the body")

    # ---- cat4 resources (9 observable of 15)
    present = {r for r, _ in _bundle_files(bundle)}
    unresolved = sorted(
        ref for ref in backticked
        if ref.split("/", 1)[0] in component_dirs and ref not in present
    )
    award("cat4_resources", "referenced_files_resolve", 3, not unresolved,
          f"referenced bundled file(s) missing: {', '.join(unresolved)}")
    scripts = [(r, full) for r, full in _bundle_files(bundle) if r.endswith(".py")]
    undocumented = [r for r, full in scripts if not _DOCSTRING.match(_read(full) or "")]
    award("cat4_resources", "scripts_have_docstrings", 2, not undocumented,
          f"script(s) with no module docstring: {', '.join(undocumented)}")
    unvalidated = [
        r for r, full in scripts
        if "argparse" not in (_read(full) or "") and "sys.argv" not in (_read(full) or "")
    ]
    award("cat4_resources", "scripts_validate_input", 1, not unvalidated,
          f"script(s) with no argument parsing: {', '.join(unvalidated)}")
    non_markdown_refs = [r for r in references if not r.endswith(".md")]
    award("cat4_resources", "references_are_markdown", 1, not non_markdown_refs,
          f"non-markdown file(s) under references/: {', '.join(non_markdown_refs)}")
    oversized = [r for r, full in _bundle_files(bundle)
                 if os.path.getsize(full) > 1024 * 1024]
    award("cat4_resources", "no_oversized_bundled_file", 2, not oversized,
          f"bundled file(s) over 1 MiB: {', '.join(oversized)}")

    # ---- cat5 safety (13 observable of 20).
    #
    # These read the **whole bundle**, not just SKILL.md, and on the unstripped
    # text: a credential inside a code fence is still a credential in the file,
    # and a credential in a bundled script is the more likely place to find one.
    # Each finding names the file and line it was seen at, because a security
    # finding without a location is not actionable.
    texts = [(rel, raw)] + [
        (r, _read(full) or "")
        for r, full in _bundle_files(bundle)
        if r != "SKILL.md" and os.path.splitext(r)[1] in
        (".py", ".md", ".sh", ".txt", ".json", ".yaml", ".yml", ".toml", ".cfg", ".ini")
    ]

    def first_hit(pattern, *, reject=None):
        for where, text in texts:
            for match in pattern.finditer(text):
                token = match.group(0)
                if reject is not None and reject.match(token):
                    continue
                line = text[:match.start()].count("\n") + 1
                return where, line, token
        return None

    secret = first_hit(_SECRET)
    award("cat5_safety", "no_hardcoded_secret", 3, not secret,
          f"credential-shaped assignment at {secret[0]}:{secret[1]}" if secret else "",
          severity="blocking")
    abs_path = first_hit(_ABSOLUTE_USER_PATH)
    award("cat5_safety", "no_absolute_user_path", 2, not abs_path,
          f"absolute user path {abs_path[2]!r} at {abs_path[0]}:{abs_path[1]}"
          if abs_path else "", severity="blocking")
    contact = first_hit(_CONTACT, reject=_ISO_DATE)
    award("cat5_safety", "no_personal_contact", 2, not contact,
          f"contact detail {contact[2]!r} at {contact[0]}:{contact[1]}"
          if contact else "", severity="blocking")
    bundle_text = "\n".join(text for _, text in texts)
    needs_env = bool(_SENSITIVE_NAME.search(bundle_text))
    award("cat5_safety", "env_vars_for_sensitive_values", 3,
          (not needs_env) or bool(_ENV_USE.search(bundle_text)),
          "names a credential-shaped variable without reading it from the environment")
    award("cat5_safety", "safety_section", 2,
          _heading(prose, r"Safety", r"Warnings?", r"Cautions?"),
          "no Safety or Warnings section")
    award("cat5_safety", "failure_handling_section", 1,
          _heading(prose, r"Troubleshooting", r"Failure", r"Recovery", r"Errors?"),
          "no Troubleshooting or failure-handling section")

    return checks, findings


# ---------------------------------------------------------------- scoring


def self_reported_block(path):
    """Read the author's own ``<!-- RUBRIC -->`` block, if there is one.

    Reported **beside** the observed numbers and never merged into them. The
    gap between the two is itself one of the audit's more useful findings, and
    merging them would destroy it.
    """
    skill_md, _ = resolve_target(path)
    text = _read(skill_md)
    if text is None:
        return None
    for match in _RUBRIC_BLOCK.finditer(_strip_code(text)):
        if re.search(r"cat\d+_\w+\s*:", match.group(1)):
            declared = {
                key: int(value) for key, value in
                re.findall(r"(cat\d+_\w+)\s*:\s*(\d+)", match.group(1))
            }
            return {"provenance": "self_reported", "scores": declared,
                    "total": sum(declared.values())}
    return None


def score(path, cfg):
    """Build the score record. Provenance and rubric version are mandatory."""
    rubric = cfg.get("rubric") or {}
    checks, findings = detect(path, cfg)
    observed = {cat: sum(values.values()) for cat, values in checks.items()}
    blocking = [f for f in findings if f.get("severity") == "blocking"]
    skill_md, bundle = resolve_target(path)

    verdict = "clean"
    if blocking:
        verdict = "blocked"
    elif findings:
        verdict = "findings"

    return {
        "artifact": os.path.relpath(bundle or skill_md, KIT_ROOT),
        "rubric": {
            "name": rubric.get("name"),
            "version": rubric.get("version"),
        },
        "provenance": "observed",
        "scores": observed,
        "observable_max_by_category": {
            cat: observable for cat, (_, observable) in CATS.items()
        },
        "rubric_max_by_category": {cat: full for cat, (full, _) in CATS.items()},
        "structural_coverage": {
            "observed": sum(observed.values()),
            "observable_max": OBSERVABLE_MAX,
            "rubric_max": RUBRIC_MAX,
        },
        "tier": None,
        "tier_basis": (
            "not asserted. Only 54 of the rubric's 100 points are mechanically "
            "observable; the remainder are judgements. Reporting a tier from the "
            "observable subset would fabricate a rubric score, which "
            "pae_registry/governance.py refuses for the same reason."
        ),
        "blocking_findings": blocking,
        "findings": findings,
        "self_reported": self_reported_block(path),
        "verdict": verdict,
        "checks": checks,
    }


# ---------------------------------------------------------------- gate A


def gate_a(record):
    """Return ``(passed, unmet)``. A score with no provenance is not a finding."""
    unmet = []
    if not isinstance(record, dict):
        return False, ["score record is not an object"]
    rubric = record.get("rubric") or {}
    if not rubric.get("name"):
        unmet.append("rubric.name is missing; a score with no named rubric is unreadable")
    if not rubric.get("version"):
        unmet.append(
            "rubric.version is missing; a score that cannot be tied to a rubric "
            "version cannot be re-run or disputed"
        )
    provenance = record.get("provenance")
    if provenance not in RECOGNIZED_PROVENANCE:
        unmet.append(
            f"provenance {provenance!r} is not one of {RECOGNIZED_PROVENANCE}; an "
            "undisclosed score cannot be told apart from the author's own"
        )
    if record.get("tier") is not None:
        unmet.append(
            f"tier {record['tier']!r} is asserted; this kit may report structural "
            "findings and disclosed scores, never a quality tier as a fact"
        )
    scores = record.get("scores")
    if not isinstance(scores, dict) or not scores:
        unmet.append("scores block is missing or empty")
    else:
        caps = record.get("observable_max_by_category") or {}
        for cat, value in scores.items():
            cap = caps.get(cat)
            if cap is not None and value > cap:
                unmet.append(f"{cat}={value} exceeds its observable maximum {cap}")
    return (not unmet), unmet


# ---------------------------------------------------------------- cli


def run_one(path, cfg, as_json=False):
    record = score(path, cfg)
    passed_gate, unmet = gate_a(record)
    record["gate_a"] = {"passed": passed_gate, "unmet": unmet}
    if as_json:
        print(json.dumps(record, indent=2, sort_keys=True))
        return passed_gate and record["verdict"] != "blocked"

    coverage = record["structural_coverage"]
    ok = passed_gate and record["verdict"] != "blocked"
    print(f"{'PASS' if ok else 'FAIL'}  {record['artifact']}: "
          f"{coverage['observed']}/{coverage['observable_max']} observable "
          f"(of {coverage['rubric_max']} rubric points; tier not asserted) — "
          f"{record['verdict']}")
    if not passed_gate:
        for reason in unmet:
            print(f"        ! Gate A: {reason}")
    for finding in record["findings"]:
        mark = "!!" if finding.get("severity") == "blocking" else " -"
        print(f"      {mark} {finding['check']}: {finding['detail']}")
    return ok


def self_check():
    print("observed_score --self-check:")
    with open(DEFAULT_CONFIG, encoding="utf-8") as fh:
        cfg = json.load(fh)
    corpus = os.path.join(KIT_ROOT, "samples", "corpus-good", "skills")
    ok = True

    for name, expect in (("deploy-helper", True), ("release-notes", False)):
        result = run_one(os.path.join(corpus, name), cfg)
        if result != expect:
            ok = False
        print(f"   -> {name}: expected {'PASS' if expect else 'FAIL'}, "
              f"got {'PASS' if result else 'FAIL'} "
              f"[{'ok' if result == expect else 'UNEXPECTED'}]")

    # The load-bearing cap: a blocking security finding must sink the verdict
    # even when the rest of the artifact scores well.
    leaky = score(os.path.join(corpus, "release-notes"), cfg)
    capped = leaky["verdict"] == "blocked" and bool(leaky["blocking_findings"])
    ok = ok and capped
    print(f"   -> blocking security finding caps the verdict: "
          f"{'ok' if capped else 'UNEXPECTED'}")

    no_tier = leaky["tier"] is None and score(
        os.path.join(corpus, "deploy-helper"), cfg)["tier"] is None
    ok = ok and no_tier
    print(f"   -> no tier is asserted for either fixture: "
          f"{'ok' if no_tier else 'UNEXPECTED'}")

    # Gate A negatives, from tracked fixtures rather than inline dicts.
    scores_dir = os.path.join(KIT_ROOT, "samples", "scores")
    for name, expect in (("score_observed_valid.json", True),
                         ("score_no_rubric_version.json", False),
                         ("score_no_provenance.json", False),
                         ("score_tier_asserted.json", False),
                         ("score_over_cap.json", False)):
        with open(os.path.join(scores_dir, name), encoding="utf-8") as fh:
            candidate = json.load(fh)
        passed, unmet = gate_a(candidate)
        if passed != expect:
            ok = False
        detail = "" if passed else f" ({unmet[0]})"
        print(f"   -> Gate A {name}: expected "
              f"{'PASS' if expect else 'BLOCK'}, got "
              f"{'PASS' if passed else 'BLOCK'}"
              f"{detail} [{'ok' if passed == expect else 'UNEXPECTED'}]")

    print("SELF-CHECK", "PASS" if ok else "FAIL")
    return ok


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="observed_score.py",
        description="Score an artifact from detectors, disclosing observed provenance.",
        epilog="Exit codes: 0 = PASS, 1 = FAIL, 2 = usage error.")
    parser.add_argument("target", nargs="?", help="a skill bundle directory or a single file")
    parser.add_argument("--config", help=f"audit config (default: {DEFAULT_CONFIG})")
    parser.add_argument("--gate-a", metavar="SCORE_JSON",
                        help="check an existing score record against Gate A and exit")
    parser.add_argument("--json", action="store_true", help="emit the score record as JSON")
    parser.add_argument("--self-check", action="store_true",
                        help="run the regression suite against the tracked samples/ fixtures")
    args = parser.parse_args(argv)

    if args.self_check:
        return 0 if self_check() else 1
    if args.gate_a:
        with open(args.gate_a, encoding="utf-8") as fh:
            record = json.load(fh)
        passed, unmet = gate_a(record)
        print(f"{'PASS' if passed else 'BLOCK'}  Gate A (scoreable) — {args.gate_a}")
        for reason in unmet:
            print(f"        - {reason}")
        return 0 if passed else 1
    if not args.target:
        parser.error("a target is required (or use --gate-a / --self-check)")
    with open(args.config or DEFAULT_CONFIG, encoding="utf-8") as fh:
        cfg = json.load(fh)
    return 0 if run_one(args.target, cfg, as_json=args.json) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
