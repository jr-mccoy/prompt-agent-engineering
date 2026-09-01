"""Governance, provenance, licensing, quality assertions and serving policy.

Every value here is either read from repository evidence or is an explicit
``unknown``. Nothing is inferred from similarity, and nothing is scored.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

MATURITY = ("experimental", "candidate", "stable", "deprecated")
REVIEW_STATUS = ("unknown", "unreviewed", "reviewed", "needs_review")
EVAL_STATUS = ("unknown", "untested", "passing", "failing", "partial")
PROVENANCE_ORIGIN = ("project_native", "vendored", "adapted", "unknown")
LICENSE_STATUS = ("resolved", "inherited", "unresolved")
SERVING_POLICY = ("standard", "safety_gated", "metadata_only", "excluded")

#: Most restrictive wins. ``excluded`` is never assigned automatically.
POLICY_RANK = {"standard": 0, "safety_gated": 1, "metadata_only": 2, "excluded": 3}

#: Fail-closed default. The field is always populated by generation, so this
#: only applies if a record somehow reaches a consumer without one.
DEFAULT_SERVING_POLICY = "metadata_only"

#: Domains whose ordinary content carries load-bearing safety framing.
SAFETY_SENSITIVE_ROOTS = frozenset(
    {
        "domain-discipleship",
        "domain-healthcare-clinical",
        "domain-legal",
        "domain-medical-education",
        "domain-parenting",
        "domain-psy-ops",
        "domain-psychology",
        "domain-written-advocacy",
    }
)

#: Authorized-offensive content: the authorization and scope gate is the point.
AUTHORIZED_OFFENSIVE_PREFIXES = ("domain-software-engineering/bug-bounty/",)

STRONG_GUARD_MARKER = "STRONG-GUARD"
SAFETY_BLOCK_RE = re.compile(r"^#+\s.*safety block", re.IGNORECASE | re.MULTILINE)

#: Third-party components with machine-readable per-file evidence.
VENDORED_UPSTREAM_KEYS = ("upstream", "upstream-commit", "upstream-path")

#: Corpus-level attribution where the notices explicitly say no per-file map is
#: maintained. Recorded as a reference, never expanded into invented mappings.
ADAPTED_CORPUS_PREFIXES = {
    "domain-agentic-resources/agents/": "THIRD_PARTY_NOTICES.md#3-wshobsonagents",
    "domain-agentic-resources/commands/": "THIRD_PARTY_NOTICES.md#3-wshobsonagents",
    "domain-agentic-resources/skills/": "THIRD_PARTY_NOTICES.md#3-wshobsonagents",
}

GOOGLE_SKILLS_PREFIX = "domain-agentic-resources/skills/mobile-development/android-"
GOOGLE_NOTICE_REF = "THIRD_PARTY_NOTICES.md#1-google--androidskills"
GOOGLE_LICENSE_BASIS = (
    "THIRD_PARTY_NOTICES.md §1 + "
    "domain-agentic-resources/skills/mobile-development/ANDROID_SKILLS_LICENSE.txt"
)


def default_governance() -> dict[str, Any]:
    """Migration defaults. Absence of a record is not evidence of absence."""
    return {
        "maturity": "experimental",
        "review_status": "unknown",
        "eval_status": "unknown",
        "eval_artifacts": [],
    }


def quality_assertions(frontmatter: dict, body: str) -> list[dict[str, str]]:
    """Typed, evidence-backed assertions — never an ordered scale.

    ``Tier 1``, ``Gold Standard``, ``STRONG-GUARD`` and ``model-testing`` are
    four unrelated concepts and nothing in the repository defines an ordering
    among them, so they live in separate ``scheme`` namespaces.

    No quality *tier* is ever asserted: ``PROMPT_QUALITY_STANDARDS.md`` defines
    the scheme but no resource records a value for it, and inferring one from
    document structure would be fabricating a rubric score.
    """
    out: list[dict[str, str]] = []
    intended_use = frontmatter.get("intended_use")
    if isinstance(intended_use, str) and intended_use.strip():
        out.append(
            {
                "scheme": "intended-use",
                "value": " ".join(intended_use.split()),
                "evidence": "frontmatter:intended_use",
            }
        )
    if STRONG_GUARD_MARKER in body:
        out.append(
            {
                "scheme": "guard-level",
                "value": "strong-guard",
                "evidence": f"body-marker:{STRONG_GUARD_MARKER}",
            }
        )
    return out


def provenance_and_license(path: str, frontmatter: dict) -> tuple[dict, dict]:
    """Resolve provenance and licensing from repository evidence only."""
    metadata = frontmatter.get("metadata") if isinstance(frontmatter.get("metadata"), dict) else {}
    declared_license = frontmatter.get("license")

    if any(metadata.get(key) for key in VENDORED_UPSTREAM_KEYS):
        upstream = {
            "repository": metadata.get("upstream"),
            "path": metadata.get("upstream-path"),
            "revision": metadata.get("upstream-commit"),
            "synced": str(metadata.get("upstream-synced")) if metadata.get("upstream-synced") else None,
            "author": metadata.get("author"),
        }
        upstream = {k: v for k, v in upstream.items() if v}
        provenance = {
            "origin": "vendored",
            "upstream": upstream,
            "notes_ref": GOOGLE_NOTICE_REF if path.startswith(GOOGLE_SKILLS_PREFIX) else None,
        }
        license_block = {
            "spdx": "Apache-2.0" if path.startswith(GOOGLE_SKILLS_PREFIX) else None,
            "status": "resolved" if path.startswith(GOOGLE_SKILLS_PREFIX) else "unresolved",
            "basis": GOOGLE_LICENSE_BASIS
            if path.startswith(GOOGLE_SKILLS_PREFIX)
            else "frontmatter metadata declares an upstream but no license",
            "attribution": metadata.get("author"),
            "redistribution_note": (
                "Body is byte-identical to upstream; must not be rewritten in place."
                if path.startswith(GOOGLE_SKILLS_PREFIX)
                else None
            ),
        }
        return _prune(provenance), _prune(license_block)

    if path.startswith(GOOGLE_SKILLS_PREFIX):
        return (
            _prune({"origin": "vendored", "notes_ref": GOOGLE_NOTICE_REF}),
            _prune(
                {
                    "spdx": "Apache-2.0",
                    "status": "inherited",
                    "basis": GOOGLE_LICENSE_BASIS,
                    "attribution": "Copyright Google LLC",
                }
            ),
        )

    notes_ref = next(
        (ref for prefix, ref in sorted(ADAPTED_CORPUS_PREFIXES.items()) if path.startswith(prefix)),
        None,
    )
    if notes_ref:
        # The notices state plainly that no per-file attribution map is
        # maintained for these upstreams. Record the reference; invent nothing.
        license_block = {
            "spdx": "MIT",
            "status": "inherited",
            "basis": "THIRD_PARTY_NOTICES.md §3/§4 (MIT upstreams; no per-file map maintained)",
        }
        if isinstance(declared_license, str) and declared_license.strip():
            license_block["basis"] += f"; source declares license: {declared_license.strip()}"
        return {"origin": "adapted", "notes_ref": notes_ref}, license_block

    if isinstance(declared_license, str) and declared_license.strip():
        value = declared_license.strip()
        spdx = value if re.match(r"^[A-Za-z0-9.\-+]+$", value) else None
        return (
            {"origin": "project_native"},
            _prune(
                {
                    "spdx": spdx,
                    "status": "resolved" if spdx else "unresolved",
                    "basis": f"frontmatter:license ({value})",
                }
            ),
        )

    return (
        {"origin": "project_native"},
        {"spdx": "MIT", "status": "resolved", "basis": "repository LICENSE"},
    )


def _prune(mapping: dict) -> dict:
    return {k: v for k, v in mapping.items() if v is not None}


def serving_policy(
    *,
    path: Optional[str],
    frontmatter: dict,
    body: str,
    metadata_completeness: str,
    maturity: str,
    license_status: str,
    provenance_origin: str,
) -> dict[str, Any]:
    """Most restrictive applicable policy, with every trigger recorded."""
    triggers: list[tuple[str, str]] = []

    intended_use = frontmatter.get("intended_use")
    if isinstance(intended_use, str) and intended_use.strip() == "model-testing":
        triggers.append(("safety_gated", "frontmatter:intended_use=model-testing"))
    if STRONG_GUARD_MARKER in body:
        triggers.append(("safety_gated", f"body-marker:{STRONG_GUARD_MARKER}"))
    if SAFETY_BLOCK_RE.search(body):
        triggers.append(("safety_gated", "body-marker:safety-block"))
    if path:
        root = path.split("/", 1)[0]
        if root in SAFETY_SENSITIVE_ROOTS:
            triggers.append(("safety_gated", f"domain:{root}"))
        if path.startswith(AUTHORIZED_OFFENSIVE_PREFIXES):
            triggers.append(("safety_gated", "domain:bug-bounty-authorized-offensive"))
    if metadata_completeness == "degraded":
        triggers.append(("metadata_only", "metadata_completeness:degraded"))
    if maturity == "deprecated":
        triggers.append(("metadata_only", "maturity:deprecated"))
    if license_status == "unresolved" and provenance_origin != "project_native":
        triggers.append(("metadata_only", "license:unresolved"))

    if not triggers:
        return {"value": "standard", "basis": ["default"]}

    value = max((t[0] for t in triggers), key=lambda v: POLICY_RANK[v])
    policy: dict[str, Any] = {"value": value, "basis": sorted({t[1] for t in triggers})}
    if value == "safety_gated":
        # Enough for a future context compiler to know what it may not drop.
        # No serving or truncation behaviour is implemented in this phase.
        policy["guard_preservation"] = {
            "must_not_truncate": True,
            "note": (
                "Guard, disclaimer, authorization and safety sections are "
                "load-bearing content. Serve the resource whole or not at all."
            ),
        }
    return policy
