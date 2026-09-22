#!/usr/bin/env python3
"""inventory.py — discover the auditable resources in a corpus, from config.

Part of ai-governance-audit-kit. Stdlib-only; no network, no LLM.

This is the config-driven counterpart to this repository's own
``scripts/pae_registry/membership.py``. That module hard-codes the roots it
walks and parses ``DOMAIN_DIRS`` out of the *text* of
``scripts/generate_prompt_index.py`` — a coupling a client tree cannot inherit.
Here the roots, component directories, meta-document filenames, anchored
non-resource prefixes and kind detectors all come from ``config/audit.json``.

**The load-bearing invariant is carried over verbatim, and enforced:**
exclusions are anchored path *prefixes*, never bare directory names. A
bare-segment blocklist is provably wrong. In the parent repository,
``domain-agentic-resources/agents/documentation/`` is a category of
documentation-*writing* agents, while ``domain-agentic-resources/documentation/``
is documentation *about* resources; a segment rule on ``documentation`` deletes
six genuine resources while intending to exclude the other tree. Prefixes can
tell those apart and segment names cannot, so ``validate_config`` **rejects** a
``non_resource_prefixes`` entry that contains no ``/``.

Gate 0 — INVENTORIABLE. A corpus with no discoverable artifacts, or a config
that matches nothing, cannot be audited. The gate fails closed rather than
reporting an empty clean bill of health, which is the one outcome an audit must
never produce by accident.

Usage:
  python3 inventory.py <corpus_dir> [--config PATH] [--json] [--out PATH]
  python3 inventory.py --self-check

Exit code: 0 = Gate 0 PASS, 1 = Gate 0 BLOCKED, 2 = usage error.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
KIT_ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PAE_ROOT = os.path.dirname(KIT_ROOT)
DEFAULT_CONFIG = os.path.join(KIT_ROOT, "config", "audit.json")

# Identity is reused, never reimplemented. ``uid_for(kind, birth_path)`` is
# sha256(kind + "\0" + birth_path) folded to 60 bits of Crockford base32; it
# takes two strings and knows nothing about this repository, which is exactly
# what makes it correct for a foreign tree. Reimplementing it here would mean a
# handback whose UIDs disagree with the Engine that has to open it.
sys.path.insert(0, os.path.join(PAE_ROOT, "scripts"))
try:
    from pae_registry.identity import (  # noqa: E402  (intentional: after path shim)
        PUBLIC_ID_RE,
        normalize_component,
        uid_for,
    )
except ImportError as exc:  # pragma: no cover - environment defect, not input
    raise SystemExit(
        "ai-governance-audit-kit needs the PAE checkout it ships inside: expected "
        f"{os.path.join(PAE_ROOT, 'scripts', 'pae_registry', 'identity.py')}. "
        f"Identity is reused rather than reimplemented ({exc})."
    ) from exc

#: Reasons a markdown file was seen and not counted. Recorded rather than
#: dropped, so the exclusion set is auditable as a partition of the corpus.
EXCLUSION_REASONS = (
    "outside_root",
    "non_resource_prefix",
    "meta_document",
    "bundled_component",
    "not_markdown",
)


class ConfigError(ValueError):
    """The audit config cannot be used. Never softened into a warning."""


# ---------------------------------------------------------------- config


def load_config(path=None):
    path = path or DEFAULT_CONFIG
    try:
        with open(path, encoding="utf-8") as fh:
            cfg = json.load(fh)
    except OSError as exc:
        raise ConfigError(f"config unreadable: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ConfigError(f"config is not valid JSON: {exc}") from exc
    errors = validate_config(cfg)
    if errors:
        raise ConfigError("; ".join(errors))
    return cfg


def validate_config(cfg):
    """Return a list of reasons this config must not be used (empty = usable)."""
    errors = []
    if not isinstance(cfg, dict):
        return ["config is not a JSON object"]

    membership = cfg.get("membership")
    if not isinstance(membership, dict):
        return ["config.membership missing or not an object"]

    roots = membership.get("roots")
    if not isinstance(roots, list) or not roots:
        errors.append("membership.roots must be a non-empty list")
    else:
        for root in roots:
            if not isinstance(root, str) or not root:
                errors.append(f"membership.roots entry is not a name: {root!r}")
            elif root.startswith("/") or ".." in root.split("/"):
                errors.append(f"membership.roots entry escapes the corpus: {root!r}")

    prefixes = membership.get("non_resource_prefixes", [])
    if not isinstance(prefixes, list):
        errors.append("membership.non_resource_prefixes must be a list")
    else:
        for prefix in prefixes:
            if not isinstance(prefix, str) or not prefix:
                errors.append(f"non_resource_prefixes entry is not a path: {prefix!r}")
                continue
            if "/" not in prefix.rstrip("/"):
                # The invariant, enforced rather than commented.
                errors.append(
                    f"non_resource_prefixes entry {prefix!r} is a bare directory name; "
                    "exclusions must be anchored path prefixes (see "
                    "references/membership.md)"
                )
            elif not prefix.endswith("/"):
                errors.append(
                    f"non_resource_prefixes entry {prefix!r} must end with '/' so it "
                    "cannot match a sibling whose name merely starts the same way"
                )

    for key in ("component_dirs", "meta_doc_filenames"):
        value = membership.get(key, [])
        if not isinstance(value, list):
            errors.append(f"membership.{key} must be a list")
            continue
        for entry in value:
            if not isinstance(entry, str) or "/" in entry:
                errors.append(f"membership.{key} entry must be a bare name: {entry!r}")

    detectors = cfg.get("kind_detectors")
    if not isinstance(detectors, list) or not detectors:
        errors.append("kind_detectors must be a non-empty list")
    else:
        fallbacks = [i for i, d in enumerate(detectors)
                     if isinstance(d, dict) and d.get("fallback")]
        if len(fallbacks) != 1:
            errors.append(
                f"kind_detectors must declare exactly one fallback; found {len(fallbacks)}"
            )
        elif fallbacks[0] != len(detectors) - 1:
            errors.append(
                "the fallback kind detector must be last, or it shadows every "
                "detector after it"
            )
        for detector in detectors:
            if not isinstance(detector, dict) or not detector.get("kind"):
                errors.append(f"kind_detectors entry has no kind: {detector!r}")
    return errors


# ---------------------------------------------------------------- classify


def _under_root(rel, roots):
    for root in roots:
        root = root.rstrip("/")
        if rel == root or rel.startswith(root + "/"):
            return root
    return None


def classify(rel, cfg):
    """Return ``(kind, reason)``. Exactly one of the two is ever non-None.

    Precedence is fixed and ordered most-specific first, mirroring the parent
    repository's ``membership.classify``: root membership, then anchored
    non-resource prefixes, then meta documents, then bundled components, then
    file type, then the kind detectors.
    """
    membership = cfg["membership"]
    rel = rel.replace(os.sep, "/").lstrip("./")

    if _under_root(rel, membership["roots"]) is None:
        return None, "outside_root"

    for prefix in membership.get("non_resource_prefixes", []):
        if rel.startswith(prefix):
            return None, "non_resource_prefix"

    basename = rel.rsplit("/", 1)[-1]
    if basename in set(membership.get("meta_doc_filenames", [])):
        return None, "meta_document"

    component_dirs = set(membership.get("component_dirs", []))
    segments = rel.split("/")[:-1]
    if any(segment in component_dirs for segment in segments):
        return None, "bundled_component"

    if not basename.endswith(".md"):
        return None, "not_markdown"

    for detector in cfg["kind_detectors"]:
        if detector.get("fallback"):
            return detector["kind"], None
        if "basename" in detector and basename == detector["basename"]:
            return detector["kind"], None
        prefix = detector.get("path_prefix")
        if prefix and rel.startswith(prefix):
            return detector["kind"], None
    # validate_config guarantees a trailing fallback, so this is unreachable.
    return None, "no_detector_matched"


# ---------------------------------------------------------------- discover


_FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)
_HEADING = re.compile(r"^#\s+(.+?)\s*$", re.M)


def _scalar(block, key):
    """Read one top-level scalar from a frontmatter block.

    Deliberately not a YAML parser: the audit must read a client's files
    without assuming they are well-formed YAML, and a parse failure is a
    finding rather than a crash.
    """
    match = re.search(rf"^{re.escape(key)}\s*:\s*(.+?)\s*$", block, re.M)
    if not match:
        return None
    value = match.group(1).strip()
    if value.startswith(("'", '"')) and value.endswith(("'", '"')) and len(value) > 1:
        value = value[1:-1]
    return value or None


def _list_field(block, key):
    match = re.search(rf"^{re.escape(key)}\s*:\s*(.*)$", block, re.M)
    if not match:
        return []
    inline = match.group(1).strip()
    if inline.startswith("["):
        return [t.strip().strip("'\"") for t in inline[1:-1].split(",") if t.strip()]
    items = []
    tail = block[match.end():]
    for line in tail.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            items.append(stripped[2:].strip().strip("'\""))
        elif stripped and not line.startswith((" ", "\t")):
            break
    return items


class IdentityError(ValueError):
    """A path from which no valid public ID can be derived."""


def public_id_for(kind, rel, scope_prefix):
    """``<kind>:<scope_prefix>/<path components>/<slug>`` for a foreign tree.

    The *shape* is the parent repository's (``<kind>:<scope>/<slug>``) and the
    component normalization is literally its ``normalize_component``, but the
    scope comes from config rather than from PAE's ``domain-*`` convention —
    a client tree has no ``domain-`` prefixes to strip. A skill is named by its
    bundle directory, every other kind by its filename stem, which is the same
    rule ``public_id_for`` applies.
    """
    parts = [p for p in rel.split("/") if p]
    if kind == "skill" and len(parts) >= 2:
        parts = parts[:-1]
    else:
        parts = parts[:-1] + [parts[-1].rsplit(".", 1)[0]]
    components = [normalize_component(scope_prefix)] + [
        normalize_component(p) for p in parts
    ]
    components = [c for c in components if c]
    if not components:
        raise IdentityError(f"no public-ID components derived from {rel!r}")
    public_id = f"{kind}:" + "/".join(components)
    if "//" in public_id or not PUBLIC_ID_RE.match(public_id):
        raise IdentityError(f"malformed public ID {public_id!r} derived from {rel}")
    return public_id


def describe(corpus, rel, kind, scope_depth=1, scope_prefix="client"):
    """Read the facts every later stage needs, and nothing more."""
    path = os.path.join(corpus, rel)
    with open(path, "rb") as fh:
        data = fh.read()
    text = data.decode("utf-8", errors="replace")
    fm = _FRONTMATTER.search(text)
    block = fm.group(1) if fm else ""
    title = _scalar(block, "title") or _scalar(block, "name")
    if not title:
        heading = _HEADING.search(text[fm.end():] if fm else text)
        title = heading.group(1).strip() if heading else rel.rsplit("/", 1)[-1]
    segments = rel.split("/")
    scope = "/".join(segments[:max(1, scope_depth)])
    return {
        "uid": uid_for(kind, rel),
        "id": public_id_for(kind, rel, scope_prefix),
        "path": rel,
        "kind": kind,
        "scope": scope,
        "title": title,
        "description": _scalar(block, "description"),
        "tags": _list_field(block, "tags"),
        "techniques": _list_field(block, "techniques"),
        "has_frontmatter": bool(fm),
        "bytes": len(data),
        "lines": text.count("\n") + (0 if text.endswith("\n") or not text else 1),
        "content_sha256": "sha256:" + hashlib.sha256(data).hexdigest(),
    }


def discover(corpus, cfg):
    """Walk the corpus once and partition every file into counted or excluded."""
    membership = cfg["membership"]
    scope_depth = int(membership.get("scope_depth", 1))
    scope_prefix = (cfg.get("handback") or {}).get("scope_prefix") or "client"
    resources = []
    reasons = Counter()
    identity_errors = []
    missing_roots = [
        root for root in membership["roots"]
        if not os.path.isdir(os.path.join(corpus, root))
    ]
    markdown_seen = 0

    for dirpath, dirnames, filenames in os.walk(corpus):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith("."))
        for name in sorted(filenames):
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, corpus).replace(os.sep, "/")
            kind, reason = classify(rel, cfg)
            if name.endswith(".md") and reason != "outside_root":
                markdown_seen += 1
            if kind is None:
                reasons[reason] += 1
                continue
            try:
                resources.append(
                    describe(corpus, rel, kind, scope_depth, scope_prefix)
                )
            except IdentityError as exc:
                # A path that cannot carry an identity cannot be handed back,
                # so it is recorded as a finding rather than silently dropped.
                identity_errors.append(str(exc))

    resources.sort(key=lambda r: r["path"])
    duplicate_ids = sorted(
        pid for pid, count in Counter(r["id"] for r in resources).items() if count > 1
    )
    return {
        "corpus": os.path.abspath(corpus),
        # The label names the corpus actually walked. The config's
        # ``corpus_label`` is the *declared* engagement label and is reported
        # beside it rather than instead of it: a report that labels the corpus
        # from config alone can name a corpus it never read.
        "corpus_label": os.path.basename(os.path.abspath(corpus).rstrip(os.sep)),
        "declared_label": cfg.get("corpus_label"),
        "resources": resources,
        "by_kind": dict(Counter(r["kind"] for r in resources)),
        "excluded": dict(reasons),
        "markdown_under_roots": markdown_seen,
        "missing_roots": missing_roots,
        "identity_errors": identity_errors,
        "duplicate_public_ids": duplicate_ids,
    }


# ---------------------------------------------------------------- gate 0


def gate_0(inventory):
    """Return ``(passed, unmet)``. Fails closed on an empty or unmatched corpus."""
    unmet = []
    if inventory["missing_roots"]:
        unmet.append(
            "configured root(s) do not exist in the corpus: "
            + ", ".join(sorted(inventory["missing_roots"]))
        )
    for problem in inventory.get("identity_errors", []):
        unmet.append(f"identity cannot be derived: {problem}")
    for pid in inventory.get("duplicate_public_ids", []):
        unmet.append(
            f"public ID {pid} is claimed by more than one artifact; a handback "
            "carrying it would fail `pae validate-registry` on duplicate_public_id"
        )
    if not inventory["resources"]:
        if inventory["markdown_under_roots"]:
            unmet.append(
                f"{inventory['markdown_under_roots']} markdown file(s) sit under the "
                "configured roots and every one was excluded — the config matches "
                "nothing, which is not the same as a clean corpus"
            )
        else:
            unmet.append(
                "no discoverable artifacts under the configured roots; an audit of "
                "an empty corpus would report a clean bill of health it cannot support"
            )
    return (not unmet), unmet


# ---------------------------------------------------------------- cli


def run_one(corpus, cfg, as_json=False, out=None):
    inventory = discover(corpus, cfg)
    passed, unmet = gate_0(inventory)
    inventory["gate_0"] = {"passed": passed, "unmet": unmet}
    if out:
        with open(out, "w", encoding="utf-8") as fh:
            json.dump(inventory, fh, indent=2, sort_keys=True)
            fh.write("\n")
    if as_json:
        print(json.dumps(inventory, indent=2, sort_keys=True))
    else:
        label = inventory["corpus_label"]
        print(f"{'PASS' if passed else 'BLOCK'}  Gate 0 (inventoriable) — {label}")
        print(f"        resources: {len(inventory['resources'])} "
              f"{inventory['by_kind'] or '{}'}")
        print(f"        excluded:  {inventory['excluded'] or '{}'}")
        for reason in unmet:
            print(f"        - {reason}")
    return passed


def self_check():
    samples = os.path.join(KIT_ROOT, "samples")
    print("inventory --self-check:")
    ok = True

    cfg = load_config()
    for name, expect in (("corpus-good", True), ("corpus-empty", False)):
        result = run_one(os.path.join(samples, name), cfg)
        if result != expect:
            ok = False
        print(f"   -> {name}: expected {'PASS' if expect else 'BLOCK'}, "
              f"got {'PASS' if result else 'BLOCK'} "
              f"[{'ok' if result == expect else 'UNEXPECTED'}]")

    # The prefixes-not-segments invariant is a config error, not a warning.
    bare = json.loads(json.dumps(cfg))
    bare["membership"]["non_resource_prefixes"] = ["documentation"]
    errors = validate_config(bare)
    bare_rejected = any("bare directory name" in e for e in errors)
    ok = ok and bare_rejected
    print(f"   -> bare-segment exclusion rejected: "
          f"{'ok' if bare_rejected else 'UNEXPECTED'}")

    # A fallback detector that is not last would shadow its successors.
    misordered = json.loads(json.dumps(cfg))
    misordered["kind_detectors"] = [
        {"kind": "prompt", "fallback": True},
        {"kind": "skill", "basename": "SKILL.md"},
    ]
    errors = validate_config(misordered)
    order_rejected = any("must be last" in e for e in errors)
    ok = ok and order_rejected
    print(f"   -> misordered fallback rejected: "
          f"{'ok' if order_rejected else 'UNEXPECTED'}")

    print("SELF-CHECK", "PASS" if ok else "FAIL")
    return ok


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="inventory.py",
        description="Discover the auditable resources in a corpus, from config.",
        epilog="Exit codes: 0 = Gate 0 PASS, 1 = Gate 0 BLOCKED, 2 = usage error.")
    parser.add_argument("corpus", nargs="?", help="path to the corpus root to inventory")
    parser.add_argument("--config", help=f"audit config (default: {DEFAULT_CONFIG})")
    parser.add_argument("--json", action="store_true", help="emit the full inventory as JSON")
    parser.add_argument("--out", help="also write the inventory JSON to this path")
    parser.add_argument("--self-check", action="store_true",
                        help="run the regression suite against the tracked samples/ fixtures")
    args = parser.parse_args(argv)

    if args.self_check:
        return 0 if self_check() else 1
    if not args.corpus:
        parser.error("a corpus directory is required (or use --self-check)")
    if not os.path.isdir(args.corpus):
        parser.error(f"{args.corpus} is not a directory")
    try:
        cfg = load_config(args.config)
    except ConfigError as exc:
        print(f"BLOCK  Gate 0 (inventoriable) — config rejected\n        - {exc}")
        return 1
    return 0 if run_one(args.corpus, cfg, as_json=args.json, out=args.out) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
