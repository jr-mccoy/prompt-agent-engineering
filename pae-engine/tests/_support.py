"""Shared test scaffolding."""

from __future__ import annotations

import io
import os
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from typing import Sequence


class _CapturedStdout(io.StringIO):
    """A text stream that also exposes a byte buffer, like real stdout.

    ``pae get --content`` writes bytes; capturing only text would let a
    regression in byte-exactness slip through.
    """

    def __init__(self) -> None:
        super().__init__()
        self.buffer = io.BytesIO()


class CliResult:
    def __init__(self, code: int, out: _CapturedStdout, err: io.StringIO) -> None:
        self.code = code
        self.stdout = out.getvalue()
        self.stdout_bytes = out.buffer.getvalue()
        self.stderr = err.getvalue()

    @property
    def stdout_empty(self) -> bool:
        return self.stdout == "" and self.stdout_bytes == b""


class EngineTestCase(unittest.TestCase):
    """Builds throwaway checkouts and runs the CLI in-process."""

    def setUp(self) -> None:
        self._tmp = tempfile.mkdtemp(prefix="pae-engine-test-")
        self.addCleanup(shutil.rmtree, self._tmp, ignore_errors=True)

    def tmp_path(self, name: str = "repo") -> Path:
        path = Path(self._tmp) / name
        path.mkdir(parents=True, exist_ok=True)
        return path

    def run_cli(self, argv: Sequence[str], *, env: dict[str, str] | None = None) -> CliResult:
        from pae_engine.cli import main

        out = _CapturedStdout()
        err = io.StringIO()
        saved_env = dict(os.environ)
        if env is not None:
            os.environ.clear()
            os.environ.update(env)
        try:
            with redirect_stdout(out), redirect_stderr(err):
                try:
                    code = main(list(argv))
                except SystemExit as exc:  # argparse usage failures
                    code = int(exc.code or 0)
        finally:
            os.environ.clear()
            os.environ.update(saved_env)
        return CliResult(code, out, err)

    def assertFails(self, result: CliResult, code: int) -> None:
        self.assertEqual(result.code, code, msg=f"stderr was: {result.stderr!r}")
        self.assertTrue(
            result.stdout_empty,
            msg=f"stdout must be empty on a nonzero exit; got {result.stdout!r}",
        )


def supports_symlinks(root: Path) -> bool:
    probe = root / "_symlink_probe"
    try:
        probe.symlink_to(root)
    except (OSError, NotImplementedError):
        return False
    probe.unlink()
    return True


def supports_fifo() -> bool:
    return hasattr(os, "mkfifo") and sys.platform != "win32"
