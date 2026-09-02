"""Secret redaction.

Credentials come from the environment and must never reach a log, a trial
record, a manifest or an exception message. Redaction is applied at the last
possible moment — on the way out to disk — because that is the only place that
sees everything: a provider exception carrying an ``Authorization`` header, a
raw response fixture, a stack trace with a key in a repr.

The design is deliberately paranoid in two directions at once. Known secret
*values* from the environment are matched exactly, and secret-*shaped* strings
are matched by pattern, so a key that arrives from somewhere we did not think
of is still caught.
"""

from __future__ import annotations

import os
import re
from typing import Any, Iterable, Mapping

PLACEHOLDER = "[REDACTED]"

#: Environment variables whose values must never appear in output.
SECRET_ENV_NAMES = (
    "ANTHROPIC_API_KEY",
    "ANTHROPIC_AUTH_TOKEN",
    "OPENAI_API_KEY",
    "OPENAI_ADMIN_KEY",
    "AWS_SECRET_ACCESS_KEY",
    "AWS_SESSION_TOKEN",
    "GITHUB_TOKEN",
    "GH_TOKEN",
    "PAE_EVAL_TOKEN",
)

#: Keys whose value is dropped wherever they appear in a mapping.
SECRET_KEY_PATTERN = re.compile(
    r"(api[_-]?key|auth[_-]?token|authorization|secret|password|passwd|"
    r"credential|cookie|set-cookie|bearer|session[_-]?token|access[_-]?token|"
    r"refresh[_-]?token|private[_-]?key)",
    re.IGNORECASE,
)

#: Secret-shaped literals. Ordered longest-first at use time so a broader
#: pattern cannot leave a fragment of a narrower one behind.
SECRET_VALUE_PATTERNS = (
    re.compile(r"sk-ant-[A-Za-z0-9_\-]{8,}"),
    re.compile(r"sk-proj-[A-Za-z0-9_\-]{8,}"),
    re.compile(r"sk-[A-Za-z0-9_\-]{20,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{16,}"),
    re.compile(r"whsec_[A-Za-z0-9_\-]{8,}"),
    re.compile(r"AKIA[0-9A-Z]{12,}"),
    re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._\-]{12,}"),
)

#: Minimum length for an env value to be treated as a secret literal. Short
#: values ("1", "true") would otherwise censor unrelated text.
MIN_SECRET_LENGTH = 8


def known_secrets(env: Mapping[str, str] | None = None) -> tuple[str, ...]:
    source = os.environ if env is None else env
    found = {
        value
        for name in SECRET_ENV_NAMES
        if (value := source.get(name)) and len(value) >= MIN_SECRET_LENGTH
    }
    # Longest first: redacting a prefix before its longer superstring would
    # leave the tail of the longer secret in the output.
    return tuple(sorted(found, key=len, reverse=True))


def redact_text(text: str, secrets: Iterable[str] | None = None,
                env: Mapping[str, str] | None = None) -> str:
    if not isinstance(text, str) or not text:
        return text
    for secret in (secrets if secrets is not None else known_secrets(env)):
        if secret:
            text = text.replace(secret, PLACEHOLDER)
    for pattern in SECRET_VALUE_PATTERNS:
        text = pattern.sub(PLACEHOLDER, text)
    return text


def redact(obj: Any, secrets: Iterable[str] | None = None,
           env: Mapping[str, str] | None = None, _depth: int = 0) -> Any:
    """Recursively redact a JSON-shaped structure.

    Both the key name and the value are considered: ``{"api_key": "abc"}`` is
    redacted by key even though ``"abc"`` matches no pattern, and a bearer
    token buried in free text is redacted by pattern even under an innocuous
    key.
    """
    if _depth > 50:  # pragma: no cover - runaway structure guard
        return PLACEHOLDER
    resolved = tuple(secrets) if secrets is not None else known_secrets(env)

    if isinstance(obj, str):
        return redact_text(obj, resolved)
    if isinstance(obj, Mapping):
        out: dict[Any, Any] = {}
        for key, value in obj.items():
            if isinstance(key, str) and SECRET_KEY_PATTERN.search(key):
                out[key] = PLACEHOLDER
            else:
                out[key] = redact(value, resolved, env, _depth + 1)
        return out
    if isinstance(obj, (list, tuple)):
        return [redact(item, resolved, env, _depth + 1) for item in obj]
    return obj


def assert_clean(obj: Any, env: Mapping[str, str] | None = None) -> None:
    """Raise if any known secret survives in ``obj``. Used in tests and CI."""
    from .canonical import canonical_json
    from .errors import IsolationError

    blob = canonical_json(redact(obj, env=env)) if not isinstance(obj, str) else obj
    for secret in known_secrets(env):
        if secret and secret in blob:
            raise IsolationError("a credential survived redaction")
    for pattern in SECRET_VALUE_PATTERNS:
        if pattern.search(blob):
            raise IsolationError(
                f"secret-shaped value survived redaction: {pattern.pattern}"
            )


def safe_environment_names(env: Mapping[str, str] | None = None) -> list[str]:
    """Which credential variables are *set* — names only, never values."""
    source = os.environ if env is None else env
    return sorted(name for name in SECRET_ENV_NAMES if source.get(name))
