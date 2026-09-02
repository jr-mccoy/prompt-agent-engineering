"""Shared scaffolding for the evaluation tests."""

from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

EVAL_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = EVAL_ROOT.parent.parent
FIXTURES = EVAL_ROOT / "tests" / "fixtures"
MINI_BENCHMARK = FIXTURES / "mini-benchmark"

# The harness is on sys.path for the whole suite; the Engine may or may not be
# installed, and tests that need it skip rather than fail.
for candidate in (EVAL_ROOT / "src", REPO_ROOT / "pae-engine" / "src"):
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))


def engine_available() -> bool:
    try:
        import pae_engine  # noqa: F401
    except ImportError:
        return False
    return True


def mcp_sdk_available() -> bool:
    try:
        from mcp.server import MCPServer  # noqa: F401
    except Exception:
        return False
    return True


def ripgrep_available() -> bool:
    return shutil.which("rg") is not None


def git_repo_available() -> bool:
    return (REPO_ROOT / ".git").exists()


class TempDirCase(unittest.TestCase):
    """A test case with a throwaway directory."""

    def setUp(self) -> None:
        self._tmp = tempfile.mkdtemp(prefix="pae-eval-test-")
        self.addCleanup(shutil.rmtree, self._tmp, ignore_errors=True)

    def tmp_path(self, name: str = "") -> Path:
        path = Path(self._tmp) / name if name else Path(self._tmp)
        if name:
            path.parent.mkdir(parents=True, exist_ok=True)
        return path

    def write(self, relative: str, content: str) -> Path:
        path = Path(self._tmp) / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        return path


def load_mini_benchmark():
    from pae_eval.benchmark import load_benchmark

    return load_benchmark(MINI_BENCHMARK)
