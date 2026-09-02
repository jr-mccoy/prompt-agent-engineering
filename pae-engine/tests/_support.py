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


def peak_rss_mib() -> float | None:
    """Peak resident set size in MiB, or ``None`` where it cannot be read.

    ``resource`` is POSIX-only. Importing it at module scope makes the whole
    module unimportable on Windows, which is how the search/routing regression
    suite came to fail at import there while Linux CI stayed green. A memory
    reading is a diagnostic nicety; never let it decide whether the diagnostics
    can run at all.
    """
    try:  # Unix
        import resource
    except ImportError:  # Windows
        return _windows_peak_rss_mib()

    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # Linux reports kilobytes; macOS reports bytes.
    return value / 1024 if sys.platform != "darwin" else value / (1024 * 1024)


def _windows_peak_rss_mib() -> float | None:
    try:
        import ctypes
        from ctypes import wintypes

        class _Counters(ctypes.Structure):
            _fields_ = [
                ("cb", wintypes.DWORD),
                ("PageFaultCount", wintypes.DWORD),
                ("PeakWorkingSetSize", ctypes.c_size_t),
                ("WorkingSetSize", ctypes.c_size_t),
                ("QuotaPeakPagedPoolUsage", ctypes.c_size_t),
                ("QuotaPagedPoolUsage", ctypes.c_size_t),
                ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
                ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
                ("PagefileUsage", ctypes.c_size_t),
                ("PeakPagefileUsage", ctypes.c_size_t),
            ]

        # argtypes/restype are mandatory: a process HANDLE is pointer-sized, and
        # without them ctypes passes it as a 32-bit int on 64-bit Windows.
        kernel32 = ctypes.windll.kernel32
        psapi = ctypes.windll.psapi
        kernel32.GetCurrentProcess.restype = wintypes.HANDLE
        psapi.GetProcessMemoryInfo.argtypes = [
            wintypes.HANDLE,
            ctypes.POINTER(_Counters),
            wintypes.DWORD,
        ]
        psapi.GetProcessMemoryInfo.restype = wintypes.BOOL

        counters = _Counters()
        counters.cb = ctypes.sizeof(counters)
        if not psapi.GetProcessMemoryInfo(
            kernel32.GetCurrentProcess(), ctypes.byref(counters), counters.cb
        ):
            return None
        return counters.PeakWorkingSetSize / (1024 * 1024)
    except Exception:  # pragma: no cover - non-Windows, or psapi unavailable
        return None


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
