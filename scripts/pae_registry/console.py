"""Console output that survives a legacy code page.

The validators print Unicode status marks (``✓``, ``✗``, ``…``). On a Windows
console still running cp1252 those characters cannot be encoded, so printing a
validation failure raised ``UnicodeEncodeError`` and the *reporting* became the
crash — the real failure never reached the developer.

The fix is deliberately narrow:

* internal strings stay Unicode; nothing is downgraded to ASCII;
* only the process's own stdout/stderr are reconfigured, and only when the
  stream actually supports it;
* the error policy is ``backslashreplace``, so a character that still cannot be
  encoded degrades to a visible escape instead of destroying the message;
* generated artifacts are untouched — every writer passes ``encoding="utf-8"``
  explicitly, so file bytes do not depend on console configuration.
"""

from __future__ import annotations

import io
from typing import Any

#: Encoding error policy. ``backslashreplace`` keeps the message readable and,
#: unlike ``ignore``, never silently deletes content from a diagnostic.
ERRORS = "backslashreplace"


def configure_stream(stream: Any) -> bool:
    """Make ``stream`` tolerant of un-encodable characters.

    Returns ``True`` when the stream was reconfigured. A stream without
    ``reconfigure`` (a ``StringIO`` under test, a pipe wrapper, a closed
    handle) is left exactly as it is: this is a best-effort convenience, never
    a precondition.
    """
    reconfigure = getattr(stream, "reconfigure", None)
    if reconfigure is None:
        return False
    try:
        reconfigure(encoding="utf-8", errors=ERRORS)
        return True
    except (ValueError, OSError, io.UnsupportedOperation):
        # Detached, already-closed, or a stream that refuses re-encoding.
        return False


def configure(*streams: Any) -> None:
    """Best-effort configuration of every given stream."""
    for stream in streams:
        configure_stream(stream)


def safe_text(text: str, stream: Any) -> str:
    """``text`` rendered so that writing it to ``stream`` cannot raise.

    For streams that could not be reconfigured — the constrained console this
    module exists for — round-tripping through the stream's own encoding with
    ``backslashreplace`` guarantees the write succeeds while preserving as much
    of the message as the terminal can actually show.
    """
    encoding = getattr(stream, "encoding", None)
    if not encoding:
        return text
    try:
        return text.encode(encoding, ERRORS).decode(encoding, "replace")
    except (LookupError, UnicodeError):
        return text
