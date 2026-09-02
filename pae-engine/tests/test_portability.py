"""Developer tooling must import and run where POSIX-only modules are absent.

``resource`` is POSIX-only. Two diagnostic runners used to import it at module
scope, and ``test_search_regression`` imports one of them at module scope in
turn — so on Windows the whole search/routing regression suite failed at import
while Linux CI stayed green and reported nothing.

These tests simulate the missing module rather than trusting the host platform,
so they fail on Linux too if the guard regresses. Asserting "it works on
Windows" only where Windows happens to run is exactly the blind spot that let
the original defect through.
"""

from __future__ import annotations

import importlib
import sys
import unittest

#: Modules that must survive a platform without ``resource``.
GUARDED_MODULES = (
    "_support",
    "run_search_routing_diagnostics",
    "run_context_compiler_diagnostics",
    "test_search_regression",
)


class _BlockingFinder:
    """A meta-path finder that refuses one module name."""

    def __init__(self, name: str) -> None:
        self.name = name

    def find_module(self, fullname, path=None):  # pragma: no cover - legacy API
        return None

    def find_spec(self, fullname, path=None, target=None):
        if fullname == self.name:
            raise ImportError(f"No module named {self.name!r}")
        return None


class _BlockResource:
    """Context manager making ``resource`` unimportable, as on Windows.

    Implemented as a ``sys.meta_path`` finder rather than a patched
    ``builtins.__import__``. Both intercept an ``import resource`` statement,
    but ``importlib.import_module`` goes straight to the import machinery and
    never touches ``builtins.__import__`` — so the patched version silently
    stopped blocking anything the moment a test used ``import_module``, which
    is exactly how this test passed on Windows (where ``resource`` genuinely
    does not exist) while proving nothing on Linux.
    """

    def __init__(self, name: str = "resource") -> None:
        self.name = name

    def __enter__(self) -> "_BlockResource":
        self._saved_module = sys.modules.pop(self.name, None)
        self._saved_targets = {
            name: sys.modules.pop(name) for name in GUARDED_MODULES if name in sys.modules
        }
        self._finder = _BlockingFinder(self.name)
        sys.meta_path.insert(0, self._finder)
        return self

    def __exit__(self, *exc) -> None:
        try:
            sys.meta_path.remove(self._finder)
        except ValueError:  # pragma: no cover - already removed
            pass
        for name in GUARDED_MODULES:
            sys.modules.pop(name, None)
        if self._saved_module is not None:
            sys.modules[self.name] = self._saved_module
        sys.modules.update(self._saved_targets)


class TestImportsWithoutResource(unittest.TestCase):
    def test_the_block_actually_blocks(self) -> None:
        """Guard the guard: a test that cannot fail proves nothing."""
        with _BlockResource():
            with self.assertRaises(ImportError):
                importlib.import_module("resource")

    def test_the_block_also_defeats_a_plain_import_statement(self) -> None:
        """Both import paths must be blocked, not just the one we happened
        to use first."""
        with _BlockResource():
            with self.assertRaises(ImportError):
                import resource  # noqa: F401, PLC0415

    def test_guarded_modules_import(self) -> None:
        with _BlockResource():
            for name in GUARDED_MODULES:
                with self.subTest(module=name):
                    sys.modules.pop(name, None)
                    importlib.import_module(name)

    def test_peak_rss_is_reported_as_unavailable_not_raised(self) -> None:
        with _BlockResource():
            sys.modules.pop("_support", None)
            support = importlib.import_module("_support")
            value = support.peak_rss_mib()
        # Windows still answers through psapi; elsewhere the honest answer is
        # None. Either is fine — raising is not.
        self.assertTrue(
            value is None or (isinstance(value, float) and value > 0),
            msg=f"expected a positive float or None, got {value!r}",
        )

    def test_peak_rss_works_on_the_host_platform(self) -> None:
        from _support import peak_rss_mib

        value = peak_rss_mib()
        self.assertTrue(value is None or value > 0)


class TestDiagnosticsTolerateMissingRss(unittest.TestCase):
    """The reporting paths must not assume a number is available."""

    def test_search_diagnostics_renders_without_rss(self) -> None:
        import run_search_routing_diagnostics as diagnostics

        # The human-readable branch is a conditional expression on None; the
        # JSON branch nulls the field. Both are asserted by construction here
        # rather than by running a full 120-case sweep.
        source = diagnostics.__file__
        with open(source, encoding="utf-8") as handle:
            text = handle.read()
        self.assertIn("peak_mb = peak_rss_mib()", text)
        self.assertIn("None if peak_mb is None else round(peak_mb, 1)", text)
        self.assertIn("unavailable on this platform", text)

    def test_context_diagnostics_rounds_optional_rss(self) -> None:
        import run_context_compiler_diagnostics as diagnostics

        self.assertIsNone(diagnostics._rounded(None))
        self.assertEqual(diagnostics._rounded(12.345), 12.3)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
