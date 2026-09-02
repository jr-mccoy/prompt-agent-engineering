"""Condition B's tools, and the containment boundary they enforce.

The path tests are the load-bearing ones. Condition B exists to be a fair
baseline, and it stops being fair the moment it can read the answer key. Every
escape shape is tested textually as well as by resolution, because the
dangerous forms are platform-dependent: ``C:/x`` is absolute on Windows and an
ordinary relative path on POSIX, so a check that only calls
``Path.is_absolute()`` passes on Linux while leaving the hole open.
"""

from __future__ import annotations

import unittest

from _support import TempDirCase, ripgrep_available

from pae_eval.errors import UsageError
from pae_eval.raw_repo import (
    RAW_REPO_LIMITS,
    TOOL_NAMES,
    RawRepoTools,
    _reject_reason,
    find_ripgrep,
    resolve_within,
)


class TestPathRejection(unittest.TestCase):
    """Textual rejection, before the filesystem is touched."""

    def test_absolute_posix(self) -> None:
        self.assertIn("absolute", _reject_reason("/etc/passwd") or "")

    def test_absolute_windows_backslash(self) -> None:
        self.assertIn("absolute", _reject_reason("\\Windows\\system32") or "")

    def test_drive_qualified(self) -> None:
        self.assertIn("drive", _reject_reason("C:/Users/secret.txt") or "")

    def test_drive_qualified_backslash(self) -> None:
        self.assertIn("drive", _reject_reason("C:\\Users\\secret.txt") or "")

    def test_unc(self) -> None:
        self.assertIn("UNC", _reject_reason("//server/share/x") or "")

    def test_unc_backslash(self) -> None:
        self.assertIn("UNC", _reject_reason("\\\\server\\share") or "")

    def test_parent_traversal(self) -> None:
        self.assertIn("traversal", _reject_reason("../../secret") or "")

    def test_traversal_in_the_middle(self) -> None:
        self.assertIn("traversal", _reject_reason("docs/../../secret") or "")

    def test_nul_byte(self) -> None:
        self.assertIn("NUL", _reject_reason("ok\x00.md") or "")

    def test_home_relative(self) -> None:
        self.assertIn("home", _reject_reason("~/secrets") or "")

    def test_empty(self) -> None:
        self.assertIsNotNone(_reject_reason("   "))

    def test_ordinary_relative_path_is_accepted(self) -> None:
        self.assertIsNone(_reject_reason("domain-science/README.md"))

    def test_windows_style_separator_is_accepted(self) -> None:
        self.assertIsNone(_reject_reason("domain-science\\README.md"))


class TestResolveWithin(TempDirCase):
    def setUp(self) -> None:
        super().setUp()
        self.root = self.tmp_path("root")
        self.root.mkdir(parents=True, exist_ok=True)
        (self.root / "inside.md").write_text("inside", encoding="utf-8")
        self.outside = self.tmp_path("outside")
        self.outside.mkdir(parents=True, exist_ok=True)
        (self.outside / "gold.json").write_text("SECRET", encoding="utf-8")

    def test_resolves_inside(self) -> None:
        resolved = resolve_within(self.root, "inside.md")
        self.assertTrue(resolved.is_file())

    def test_refuses_escape(self) -> None:
        with self.assertRaises(UsageError):
            resolve_within(self.root, "../outside/gold.json")

    def test_refuses_symlink_that_escapes(self) -> None:
        link = self.root / "escape"
        try:
            link.symlink_to(self.outside, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unavailable on this platform/account")
        with self.assertRaises(UsageError):
            resolve_within(self.root, "escape/gold.json")


class TestToolSurface(TempDirCase):
    """The three tools, and nothing else."""

    def setUp(self) -> None:
        super().setUp()
        self.root = self.tmp_path("snap")
        (self.root / "docs").mkdir(parents=True, exist_ok=True)
        (self.root / "docs" / "readme.md").write_text(
            "# Title\nreadiness and rollback\n", encoding="utf-8")
        (self.root / "other.md").write_text("unrelated\n", encoding="utf-8")

    def tools(self, **kw):
        return RawRepoTools(self.root, require_ripgrep=False,
                            files=("docs/readme.md", "other.md"), **kw)

    def test_exactly_three_tools(self) -> None:
        self.assertEqual(sorted(TOOL_NAMES),
                         ["repo_list", "repo_read", "repo_search"])

    def test_no_shell_or_pae_tool_exists(self) -> None:
        forbidden = {"bash", "shell", "python", "pae", "pae_search_resources",
                     "pae_route_task", "pae_compose_bundle", "pae_get_resource"}
        self.assertFalse(forbidden & set(TOOL_NAMES))

    def test_unknown_tool_is_an_error_not_a_crash(self) -> None:
        outcome = self.tools().call("bash", {"command": "ls"})
        self.assertTrue(outcome.is_error)
        self.assertIn("unknown tool", outcome.content)

    def test_read_returns_content(self) -> None:
        outcome = self.tools().call("repo_read", {"path": "docs/readme.md"})
        self.assertFalse(outcome.is_error)
        self.assertIn("rollback", outcome.content)

    def test_read_refuses_escape(self) -> None:
        outcome = self.tools().call("repo_read", {"path": "../../../etc/passwd"})
        self.assertTrue(outcome.is_error)

    def test_read_refuses_a_directory(self) -> None:
        outcome = self.tools().call("repo_read", {"path": "docs"})
        self.assertTrue(outcome.is_error)
        self.assertIn("not a regular file", outcome.content)

    def test_list_matches_glob(self) -> None:
        outcome = self.tools().call("repo_list", {"glob": "docs/*.md"})
        self.assertIn("docs/readme.md", outcome.content)
        self.assertNotIn("other.md", outcome.content.replace("docs/readme.md", ""))

    def test_list_never_leaves_the_root(self) -> None:
        outcome = self.tools().call("repo_list", {"glob": "**/*"})
        for line in outcome.content.splitlines():
            self.assertFalse(line.startswith(("/", "\\", "..")))

    def test_bad_arguments_do_not_crash_the_loop(self) -> None:
        outcome = self.tools().call("repo_read", {"nonsense": 1})
        self.assertTrue(outcome.is_error)

    def test_observability_is_recorded(self) -> None:
        tools = self.tools()
        tools.call("repo_read", {"path": "docs/readme.md"})
        tools.call("repo_list", {"glob": "*.md"})
        summary = tools.log.summary()
        self.assertEqual(summary["read_calls"], 1)
        self.assertEqual(summary["list_calls"], 1)
        self.assertGreater(summary["total_tool_bytes"], 0)

    def test_read_result_is_byte_capped(self) -> None:
        big = "x" * (RAW_REPO_LIMITS["read_max_result_bytes"] * 2)
        (self.root / "big.md").write_text(big, encoding="utf-8")
        tools = RawRepoTools(self.root, require_ripgrep=False,
                             files=("big.md",))
        outcome = tools.call("repo_read", {"path": "big.md"})
        self.assertLessEqual(
            len(outcome.content.encode("utf-8")),
            RAW_REPO_LIMITS["read_max_result_bytes"] + 200,
        )


class TestRipgrepPolicy(TempDirCase):
    """Without ripgrep the baseline must refuse, not quietly become something else."""

    def test_missing_ripgrep_refuses_rather_than_substituting(self) -> None:
        import pae_eval.raw_repo as raw_repo

        root = self.tmp_path("snap")
        root.mkdir(parents=True, exist_ok=True)

        original = raw_repo.find_ripgrep
        raw_repo.find_ripgrep = lambda: None  # simulate a host without rg
        self.addCleanup(setattr, raw_repo, "find_ripgrep", original)

        with self.assertRaises(UsageError) as caught:
            raw_repo.RawRepoTools(root, require_ripgrep=True, files=())
        message = str(caught.exception)
        self.assertIn("ripgrep", message)
        self.assertIn("would change what the baseline is", message)

    def test_it_can_be_constructed_without_rg_for_non_search_use(self) -> None:
        import pae_eval.raw_repo as raw_repo

        root = self.tmp_path("snap2")
        root.mkdir(parents=True, exist_ok=True)
        original = raw_repo.find_ripgrep
        raw_repo.find_ripgrep = lambda: None
        self.addCleanup(setattr, raw_repo, "find_ripgrep", original)
        # require_ripgrep=False is for dry-run and unit tests only; a sealed
        # run always requires it.
        tools = raw_repo.RawRepoTools(root, require_ripgrep=False, files=())
        self.assertIsNone(tools.ripgrep_version)


@unittest.skipUnless(ripgrep_available(), "ripgrep is not installed")
class TestRipgrepIntegration(TempDirCase):
    """At least one test must drive the real binary (spec §102)."""

    def setUp(self) -> None:
        super().setUp()
        self.root = self.tmp_path("snap")
        (self.root / "a").mkdir(parents=True, exist_ok=True)
        (self.root / "a" / "one.md").write_text(
            "alpha readiness\nbeta\n", encoding="utf-8")
        (self.root / "two.md").write_text("gamma readiness\n", encoding="utf-8")
        self.tools = RawRepoTools(self.root, require_ripgrep=True,
                                  files=("a/one.md", "two.md"))

    def test_version_is_reported(self) -> None:
        self.assertIn("ripgrep", (self.tools.ripgrep_version or "").lower())

    def test_search_finds_matches_in_both_files(self) -> None:
        outcome = self.tools.call("repo_search", {"pattern": "readiness"})
        self.assertFalse(outcome.is_error)
        self.assertIn("one.md", outcome.content)
        self.assertIn("two.md", outcome.content)
        self.assertEqual(outcome.matches, 2)

    def test_no_matches_is_a_result_not_an_error(self) -> None:
        outcome = self.tools.call("repo_search", {"pattern": "zzzqqqnothing"})
        self.assertFalse(outcome.is_error)
        self.assertIn("no matches", outcome.content)

    def test_glob_restricts_the_search(self) -> None:
        outcome = self.tools.call(
            "repo_search", {"pattern": "readiness", "glob": "two.md"})
        self.assertIn("two.md", outcome.content)
        self.assertNotIn("one.md", outcome.content)

    def test_search_cannot_escape_the_root(self) -> None:
        (self.tmp_path() / "outside-secret.md").write_text(
            "readiness SECRET", encoding="utf-8")
        outcome = self.tools.call("repo_search", {"pattern": "SECRET"})
        self.assertNotIn("SECRET", outcome.content)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
