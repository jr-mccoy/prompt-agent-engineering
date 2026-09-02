"""Deterministic serialization and hashing.

Every hash the evidence chain depends on — plan, benchmark, schedule, snapshot,
prompts, tool catalog — is computed here, so there is exactly one definition of
"the canonical bytes of this object". Two runs that disagree about whitespace
must not disagree about identity.

The settings are fixed and not configurable:

``sort_keys=True``
    Dict iteration order is an implementation detail; hashing it would make the
    same content hash differently between runs.
``separators=(",", ":")``
    No incidental whitespace.
``ensure_ascii=False`` + UTF-8
    A resource title with an em dash hashes as the character it is, not as an
    escape sequence.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any

#: Prefix on every digest we emit, so a bare hex string is never mistaken for
#: one of ours and the algorithm travels with the value.
DIGEST_PREFIX = "sha256:"


def canonical_json(obj: Any) -> str:
    """The one canonical text form of ``obj``."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def canonical_bytes(obj: Any) -> bytes:
    return canonical_json(obj).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return DIGEST_PREFIX + hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def sha256_obj(obj: Any) -> str:
    """Digest of the canonical form of ``obj``."""
    return sha256_bytes(canonical_bytes(obj))


def sha256_file(path, chunk: int = 1 << 20) -> str:
    """Digest of a file's bytes, read incrementally.

    Used on corpus files that can reach several megabytes; never load the whole
    repository into memory to hash it.
    """
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            block = handle.read(chunk)
            if not block:
                break
            digest.update(block)
    return DIGEST_PREFIX + digest.hexdigest()


def short(digest: str, length: int = 12) -> str:
    """A digest abbreviated for display only. Never for comparison."""
    return digest[len(DIGEST_PREFIX):][:length] if digest.startswith(DIGEST_PREFIX) else digest[:length]


def write_canonical(path, obj: Any) -> str:
    """Write ``obj`` canonically and return its digest.

    The digest is of exactly the bytes written, so a reader that hashes the
    file gets the same answer we recorded.
    """
    data = canonical_bytes(obj)
    with open(path, "wb") as handle:
        handle.write(data)
    return sha256_bytes(data)
