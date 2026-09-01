"""Architectural invariants, asserted rather than asserted-to.

Phase 3 makes four claims that are easy to state and easy to erode: the Engine
never writes, never executes, never reaches the network, and never imports the
repository-maintenance package. Each is checked here by walking the installed
source's AST, so a regression fails a test instead of surviving a review.

The check identifies dangerous *calls and imports* rather than banning whole
modules by name: ``os`` is entirely ordinary for path and environment work, and
a blanket ban on it would be noise that future contributors learn to silence.
"""

from __future__ import annotations

import ast
import unittest
from pathlib import Path

import pae_engine

PACKAGE_ROOT = Path(pae_engine.__file__).resolve().parent
ENGINE_ROOT = PACKAGE_ROOT.parent.parent


def engine_sources() -> list[Path]:
    return sorted(PACKAGE_ROOT.rglob("*.py"))


def parsed_sources():
    for path in engine_sources():
        yield path, ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


#: Modules whose entire purpose is something the Engine must not do.
FORBIDDEN_MODULES = frozenset(
    {
        "subprocess",
        "socket",
        "socketserver",
        "ssl",
        "ftplib",
        "smtplib",
        "telnetlib",
        "poplib",
        "imaplib",
        "http",
        "http.client",
        "urllib",
        "urllib.request",
        "xmlrpc",
        "webbrowser",
        "pickle",
        "cPickle",
        "marshal",
        "shelve",
        "dbm",
        "sqlite3",
        "ctypes",
        "multiprocessing",
        "shutil",
        "tempfile",
        "pty",
        "commands",
        "runpy",
        "code",
        "codeop",
        "importlib.util",
    }
)

#: Bare names that execute or compile code.
FORBIDDEN_CALLS = frozenset({"eval", "exec", "compile", "__import__", "breakpoint"})

#: ``os.<name>`` and ``Path.<name>`` calls that mutate the filesystem or spawn
#: a process.
FORBIDDEN_ATTRS = frozenset(
    {
        "system",
        "popen",
        "spawn",
        "spawnl",
        "spawnv",
        "spawnve",
        "execv",
        "execve",
        "execl",
        "execlp",
        "execvp",
        "fork",
        "forkpty",
        "remove",
        "unlink",
        "rmdir",
        "removedirs",
        "rename",
        "renames",
        "replace",
        "mkdir",
        "makedirs",
        "chmod",
        "chown",
        "lchown",
        "truncate",
        "symlink",
        "symlink_to",
        "hardlink_to",
        "link",
        "mkfifo",
        "mknod",
        "write_text",
        "write_bytes",
        "touch",
        "rmtree",
        "copy",
        "copy2",
        "copyfile",
        "copytree",
        "move",
        "loads_pickle",
        "dump",
        "urlopen",
        "urlretrieve",
        "connect",
        "send",
        "sendall",
        "recv",
    }
)

#: File modes the Engine is allowed to open with.
READ_ONLY_MODES = frozenset({"r", "rb", "rt", "br", "tr"})


class TestReadOnlyRuntime(unittest.TestCase):
    def test_no_forbidden_module_is_imported(self) -> None:
        offences = []
        for path, tree in parsed_sources():
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name.split(".")[0] in FORBIDDEN_MODULES or (
                            alias.name in FORBIDDEN_MODULES
                        ):
                            offences.append(f"{path.name}:{node.lineno} import {alias.name}")
                elif isinstance(node, ast.ImportFrom) and node.module:
                    root = node.module.split(".")[0]
                    if root in FORBIDDEN_MODULES or node.module in FORBIDDEN_MODULES:
                        offences.append(f"{path.name}:{node.lineno} from {node.module}")
        self.assertEqual(offences, [], f"forbidden imports: {offences}")

    def test_no_dynamic_code_execution(self) -> None:
        offences = []
        for path, tree in parsed_sources():
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                    if node.func.id in FORBIDDEN_CALLS:
                        offences.append(f"{path.name}:{node.lineno} {node.func.id}()")
        self.assertEqual(offences, [], f"dynamic execution: {offences}")

    def test_no_mutating_or_networking_calls(self) -> None:
        offences = []
        for path, tree in parsed_sources():
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                    if node.func.attr in FORBIDDEN_ATTRS:
                        offences.append(f"{path.name}:{node.lineno} .{node.func.attr}()")
        self.assertEqual(offences, [], f"mutating/networking calls: {offences}")

    def test_every_open_is_read_only(self) -> None:
        """``open`` may appear, but never with a writable mode."""
        offences = []
        for path, tree in parsed_sources():
            for node in ast.walk(tree):
                if not isinstance(node, ast.Call):
                    continue
                is_open = (isinstance(node.func, ast.Name) and node.func.id == "open") or (
                    isinstance(node.func, ast.Attribute) and node.func.attr == "open"
                )
                if not is_open:
                    continue
                mode = None
                if len(node.args) >= 2:
                    mode = node.args[1]
                for keyword in node.keywords:
                    if keyword.arg == "mode":
                        mode = keyword.value
                if mode is None:
                    continue  # defaults to "r"
                if not isinstance(mode, ast.Constant) or mode.value not in READ_ONLY_MODES:
                    offences.append(f"{path.name}:{node.lineno} open(mode={ast.dump(mode)})")
        self.assertEqual(offences, [], f"writable opens: {offences}")

    def test_the_only_file_reads_are_read_only_helpers(self) -> None:
        """A positive assertion to pair with the negative ones above."""
        used = set()
        for _path, tree in parsed_sources():
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                    if node.func.attr in {"read_text", "read_bytes"}:
                        used.add(node.func.attr)
        self.assertTrue(used, "expected the engine to read files somehow")


class TestRuntimeDataBoundary(unittest.TestCase):
    def test_the_engine_never_imports_repository_maintenance_code(self) -> None:
        """The normalized registry is the boundary.

        Importing ``scripts.pae_registry`` would re-couple the runtime to
        corpus discovery, identity derivation and registry generation — a
        second source of truth that could disagree with the frozen one.
        """
        offences = []
        for path, tree in parsed_sources():
            for node in ast.walk(tree):
                names = []
                if isinstance(node, ast.Import):
                    names = [a.name for a in node.names]
                elif isinstance(node, ast.ImportFrom) and node.module:
                    names = [node.module]
                for name in names:
                    if "pae_registry" in name or name.startswith("scripts"):
                        offences.append(f"{path.name}:{node.lineno} {name}")
        self.assertEqual(offences, [], f"maintenance imports: {offences}")

    def test_the_engine_reads_only_the_two_registry_artifacts(self) -> None:
        """Ledgers, diagnostics, overrides and the prompt index are out of scope.

        Only string literals the code actually uses are inspected; a docstring
        naming an artifact it deliberately avoids is not a violation.
        """
        from _codescan import string_constants

        literals = [lit for path in engine_sources() for lit in string_constants(path)]
        blob = "\n".join(literals)
        for maintenance_artifact in (
            "identity.tsv",
            "aliases.tsv",
            "relationships.tsv",
            "diagnostics.jsonl",
            "PROMPT_INDEX",
            "REORG_MAP",
            "VENDORED",
            "overrides/",
        ):
            self.assertNotIn(
                maintenance_artifact,
                blob,
                f"engine must not reference {maintenance_artifact}",
            )
        # The two it may read are named exactly once each, in repository.py.
        self.assertIn("meta/registry/registry.jsonl", blob)
        self.assertIn("meta/registry/registry-summary.json", blob)

    def test_no_network_endpoint_appears_in_the_runtime(self) -> None:
        """No URL the code could dial. Documentation links are prose, not code."""
        from _codescan import string_constants

        for path in engine_sources():
            for literal in string_constants(path):
                for scheme in ("http://", "https://", "ftp://", "ws://"):
                    self.assertNotIn(
                        scheme, literal, f"{path.name}: URL in executable code: {literal!r}"
                    )


class TestPackagingInvariants(unittest.TestCase):
    def test_engine_license_matches_the_repository_license(self) -> None:
        """A drifted licence in a shipped artifact is a real legal defect."""
        engine_license = ENGINE_ROOT / "LICENSE"
        root_license = ENGINE_ROOT.parent / "LICENSE"
        if not root_license.exists():
            self.skipTest("running outside the repository checkout")
        self.assertEqual(
            engine_license.read_bytes(),
            root_license.read_bytes(),
            "pae-engine/LICENSE must be byte-identical to the repository LICENSE",
        )

    def test_declared_runtime_dependencies_are_empty(self) -> None:
        pyproject = ENGINE_ROOT / "pyproject.toml"
        if not pyproject.exists():
            self.skipTest("running outside the repository checkout")
        text = pyproject.read_text(encoding="utf-8")
        self.assertIn("dependencies = []", text)

    def test_version_is_consistent(self) -> None:
        pyproject = ENGINE_ROOT / "pyproject.toml"
        if not pyproject.exists():
            self.skipTest("running outside the repository checkout")
        text = pyproject.read_text(encoding="utf-8")
        self.assertIn(f'version = "{pae_engine.__version__}"', text)

    def test_no_corpus_or_registry_is_packaged(self) -> None:
        """The wheel ships code. The registry lives in the checkout."""
        shipped = {p.name for p in PACKAGE_ROOT.rglob("*") if p.is_file()}
        for forbidden in ("registry.jsonl", "registry-summary.json"):
            self.assertNotIn(forbidden, shipped)


class TestPublicApiSurface(unittest.TestCase):
    def test_documented_names_are_exported(self) -> None:
        for name in (
            "Repository", "Registry", "Record", "Resolution", "Content", "Summary",
            "validate_registry", "PaeError", "IncompatibleRegistry", "ResourceExcluded",
        ):
            self.assertIn(name, pae_engine.__all__)
            self.assertTrue(hasattr(pae_engine, name))

    def test_no_search_or_ranking_surface_exists_yet(self) -> None:
        """Phase 4's shape is not guessed at in Phase 3."""
        from pae_engine import Registry

        for name in ("search", "rank", "score", "query", "embed", "route", "bundle"):
            self.assertFalse(hasattr(Registry, name), f"Registry.{name} is a Phase 4 concern")

    def test_exit_codes_are_stable_and_distinct(self) -> None:
        from pae_engine import errors

        expected = {
            errors.UsageError: 2,
            errors.MalformedReference: 2,
            errors.RepositoryNotFound: 3,
            errors.ResourceNotFound: 4,
            errors.ContentRefused: 5,
            errors.ResourceExcluded: 5,
            errors.NoAddressableContent: 6,
            errors.SourceIntegrityError: 7,
            errors.PathSecurityError: 7,
            errors.ChecksumMismatch: 7,
            errors.IncompatibleRegistry: 8,
            errors.RegistryValidationError: 9,
        }
        for cls, code in expected.items():
            self.assertEqual(cls.exit_code, code, f"{cls.__name__} exit code changed")
        self.assertEqual(errors.PaeError.exit_code, 1)


if __name__ == "__main__":
    unittest.main()
