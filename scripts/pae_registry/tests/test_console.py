"""Reporting a validation failure must not become the failure.

``generate_registry.py`` prints Unicode status marks. On a console still using a
legacy code page, ``print("  ✗ ...")`` raised ``UnicodeEncodeError`` — so the
check failed, and then the *report* of the failure crashed on top of it, hiding
the real message behind a traceback.

These tests drive a stream that genuinely cannot encode the status marks, so
they fail wherever they run rather than only on a cp1252 console.
"""

from __future__ import annotations

import io
import sys
import unittest
from pathlib import Path

from pae_registry import console

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import generate_registry  # noqa: E402


class ConstrainedStream(io.TextIOBase):
    """A text stream limited to a legacy code page, like a Windows console.

    Deliberately offers no ``reconfigure``: this is the stream shape the repair
    must survive without cooperation from the runtime.
    """

    def __init__(self, encoding: str = "cp1252") -> None:
        super().__init__()
        self._encoding = encoding
        self.written: list[str] = []

    @property
    def encoding(self) -> str:  # type: ignore[override]
        return self._encoding

    def write(self, text: str) -> int:
        # Raises exactly where a real constrained console would.
        text.encode(self._encoding)
        self.written.append(text)
        return len(text)

    def getvalue(self) -> str:
        return "".join(self.written)


class TestConstrainedStreamIsRealistic(unittest.TestCase):
    """Guard the guard: if the fake stream accepts ✗, it proves nothing."""

    def test_stream_rejects_the_status_mark(self) -> None:
        stream = ConstrainedStream()
        with self.assertRaises(UnicodeEncodeError):
            stream.write("✗")

    def test_stream_accepts_plain_ascii(self) -> None:
        stream = ConstrainedStream()
        stream.write("registry artifacts are not current:")
        self.assertIn("not current", stream.getvalue())


class TestFailureOutputSurvives(unittest.TestCase):
    def test_printing_a_failure_does_not_raise(self) -> None:
        stream = ConstrainedStream()
        # Would raise UnicodeEncodeError before the repair.
        generate_registry._say("  ✗ registry.jsonl: stale", stream)
        self.assertTrue(stream.getvalue())

    def test_the_underlying_failure_stays_visible(self) -> None:
        stream = ConstrainedStream()
        generate_registry._say("  ✗ registry.jsonl: stale — regenerate", stream)
        written = stream.getvalue()
        # The diagnostic content survives; only the unencodable glyphs degrade.
        self.assertIn("registry.jsonl", written)
        self.assertIn("stale", written)
        self.assertIn("regenerate", written)

    def test_ellipsis_overflow_line_survives(self) -> None:
        stream = ConstrainedStream()
        generate_registry._say("  … and 7 more", stream)
        self.assertIn("and 7 more", stream.getvalue())

    def test_full_fail_path_reports_every_error_and_returns_one(self) -> None:
        stream = ConstrainedStream()
        errors = [f"artifact-{n}.jsonl: stale" for n in range(30)]
        saved = sys.stdout
        sys.stdout = stream  # _fail writes to the configured default stream
        try:
            code = generate_registry._fail(errors)
        finally:
            sys.stdout = saved

        self.assertEqual(code, 1)
        written = stream.getvalue()
        # 25 shown, then the truncation notice — nothing silently swallowed.
        self.assertIn("artifact-0.jsonl", written)
        self.assertIn("artifact-24.jsonl", written)
        self.assertIn("and 5 more", written)


class TestConfigureIsBestEffort(unittest.TestCase):
    def test_streams_without_reconfigure_are_left_alone(self) -> None:
        stream = ConstrainedStream()
        self.assertFalse(console.configure_stream(stream))
        # Still usable afterwards; configure must never damage a stream.
        stream.write("ok")
        self.assertEqual(stream.getvalue(), "ok")

    def test_configure_tolerates_anything(self) -> None:
        console.configure(ConstrainedStream(), io.StringIO(), None, object())

    def test_reconfigurable_stream_is_switched_to_utf8(self) -> None:
        raw = io.BytesIO()
        stream = io.TextIOWrapper(raw, encoding="cp1252")
        self.assertTrue(console.configure_stream(stream))
        self.assertEqual(stream.encoding.lower().replace("-", ""), "utf8")
        stream.write("✗ ok")
        stream.flush()
        self.assertIn("✗", raw.getvalue().decode("utf-8"))

    def test_safe_text_degrades_without_losing_content(self) -> None:
        stream = ConstrainedStream()
        rendered = console.safe_text("✗ stale — regenerate", stream)
        rendered.encode("cp1252")  # must not raise
        self.assertIn("stale", rendered)
        self.assertIn("regenerate", rendered)

    def test_safe_text_passes_through_when_encoding_is_capable(self) -> None:
        stream = ConstrainedStream(encoding="utf-8")
        self.assertEqual(console.safe_text("✗ fine", stream), "✗ fine")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
