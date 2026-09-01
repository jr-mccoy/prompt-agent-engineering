"""Source-path containment, size ceiling, integrity and encoding.

Every registry path is treated as untrusted input. A consumer may be reading a
registry it did not generate, so "the registry said so" is never sufficient
reason to open a file.
"""

from __future__ import annotations

import os
import unittest

from _support import EngineTestCase, supports_fifo, supports_symlinks
import fixtures as fx

from pae_engine import (
    ChecksumMismatch,
    ContentEncodingError,
    PathSecurityError,
    Repository,
    SourceTooLarge,
    SourceUnavailable,
)
from pae_engine.registry import MAX_CONTENT_BYTES


class _PathCase(EngineTestCase):
    def registry_for(self, stored_path, *, body=b"body\n", sha=None, name="repo",
                     checksum_payload="raw_source_bytes"):
        root = self.tmp_path(name)
        fx.build_repo(
            root,
            [
                fx.record(
                    "pae_0000000000aa",
                    "prompt:fixtures/target",
                    path=stored_path,
                    content_sha256=sha if sha is not None else fx.sha256_of(body),
                    checksum_payload=checksum_payload,
                )
            ],
        )
        return root, Repository.at(root).registry()


class TestPathContainment(_PathCase):
    def test_traversal_is_refused(self) -> None:
        _root, registry = self.registry_for("../outside.md")
        with self.assertRaises(PathSecurityError) as ctx:
            registry.content("prompt:fixtures/target")
        self.assertEqual(ctx.exception.exit_code, 7)

    def test_nested_traversal_is_refused(self) -> None:
        _root, registry = self.registry_for("domain-x/../../outside.md")
        with self.assertRaises(PathSecurityError):
            registry.content("prompt:fixtures/target")

    def test_posix_absolute_path_is_refused(self) -> None:
        _root, registry = self.registry_for("/etc/passwd")
        with self.assertRaises(PathSecurityError) as ctx:
            registry.content("prompt:fixtures/target")
        self.assertIn("absolute", ctx.exception.message)

    def test_windows_drive_path_is_refused(self) -> None:
        _root, registry = self.registry_for("C:\\Windows\\System32\\drivers\\etc\\hosts")
        with self.assertRaises(PathSecurityError):
            registry.content("prompt:fixtures/target")

    def test_unc_path_is_refused(self) -> None:
        for unc in ("\\\\server\\share\\file.md", "//server/share/file.md"):
            with self.subTest(path=unc):
                _root, registry = self.registry_for(unc, name=f"repo{abs(hash(unc))}")
                with self.assertRaises(PathSecurityError):
                    registry.content("prompt:fixtures/target")

    def test_nul_byte_is_refused(self) -> None:
        _root, registry = self.registry_for("fixtures/body\x00.md")
        with self.assertRaises(PathSecurityError):
            registry.content("prompt:fixtures/target")

    def test_empty_path_is_refused(self) -> None:
        root = self.tmp_path()
        fx.build_repo(
            root,
            [fx.record("pae_0000000000aa", "prompt:fixtures/target", path="",
                       content_sha256=fx.sha256_of(b""))],
        )
        registry = Repository.at(root).registry()
        # An empty stored path is not an addressable body at all.
        with self.assertRaises(Exception) as ctx:
            registry.content("prompt:fixtures/target")
        self.assertIn(ctx.exception.exit_code, (6, 7))

    def test_symlink_out_of_the_repository_is_refused(self) -> None:
        """Lexical checks are not enough; the resolved target must be inside too."""
        root = self.tmp_path("repo")
        if not supports_symlinks(root):
            self.skipTest("symlinks unsupported on this platform")
        body = b"CONFIDENTIAL-BODY-CONTENTS\n"
        outside = self.tmp_path("outside") / "elsewhere.md"
        outside.write_bytes(body)
        link = root / "fixtures" / "link.md"
        link.parent.mkdir(parents=True, exist_ok=True)
        link.symlink_to(outside)

        fx.build_repo(
            root,
            [fx.record("pae_0000000000aa", "prompt:fixtures/target",
                       path="fixtures/link.md", content_sha256=fx.sha256_of(body))],
        )
        registry = Repository.at(root).registry()
        with self.assertRaises(PathSecurityError) as ctx:
            registry.content("prompt:fixtures/target")
        self.assertEqual(ctx.exception.exit_code, 7)
        # The resolved path is reported, because a caller needs it to diagnose
        # the escape. The file's contents are not read and cannot leak.
        self.assertNotIn("CONFIDENTIAL-BODY-CONTENTS", str(ctx.exception.to_json_obj()))

    def test_symlink_inside_the_repository_is_allowed(self) -> None:
        root = self.tmp_path("repo")
        if not supports_symlinks(root):
            self.skipTest("symlinks unsupported on this platform")
        real, sha = fx.with_source(root, "fixtures/real.md", b"inside\n")
        link = root / "fixtures" / "alias.md"
        link.symlink_to(root / real)
        fx.build_repo(
            root,
            [fx.record("pae_0000000000aa", "prompt:fixtures/target",
                       path="fixtures/alias.md", content_sha256=sha)],
        )
        registry = Repository.at(root).registry()
        self.assertEqual(registry.content("prompt:fixtures/target").data, b"inside\n")


class TestSourceAvailability(_PathCase):
    def test_missing_source_file(self) -> None:
        _root, registry = self.registry_for("fixtures/never-written.md")
        with self.assertRaises(SourceUnavailable) as ctx:
            registry.content("prompt:fixtures/target")
        self.assertEqual(ctx.exception.exit_code, 7)

    def test_directory_is_not_a_regular_file(self) -> None:
        root = self.tmp_path()
        (root / "fixtures" / "adirectory.md").mkdir(parents=True)
        fx.build_repo(
            root,
            [fx.record("pae_0000000000aa", "prompt:fixtures/target",
                       path="fixtures/adirectory.md", content_sha256=fx.sha256_of(b""))],
        )
        registry = Repository.at(root).registry()
        with self.assertRaises(SourceUnavailable) as ctx:
            registry.content("prompt:fixtures/target")
        self.assertIn("not a regular file", ctx.exception.message)

    @unittest.skipUnless(supports_fifo(), "FIFOs unsupported here")
    def test_fifo_is_not_a_regular_file(self) -> None:
        """A FIFO would block forever on read; refuse before opening it."""
        root = self.tmp_path()
        (root / "fixtures").mkdir(parents=True, exist_ok=True)
        os.mkfifo(root / "fixtures" / "pipe.md")
        fx.build_repo(
            root,
            [fx.record("pae_0000000000aa", "prompt:fixtures/target",
                       path="fixtures/pipe.md", content_sha256=fx.sha256_of(b""))],
        )
        registry = Repository.at(root).registry()
        with self.assertRaises(SourceUnavailable):
            registry.content("prompt:fixtures/target")


class TestIntegrity(_PathCase):
    def test_checksum_mismatch_returns_no_bytes(self) -> None:
        """A local edit must fail loudly, and the body must not leak."""
        root = self.tmp_path()
        path, _sha = fx.with_source(root, "fixtures/body.md", b"edited locally\n")
        fx.build_repo(
            root,
            [fx.record("pae_0000000000aa", "prompt:fixtures/target", path=path,
                       content_sha256=fx.sha256_of(b"as generated\n"))],
        )
        registry = Repository.at(root).registry()
        with self.assertRaises(ChecksumMismatch) as ctx:
            registry.content("prompt:fixtures/target")
        exc = ctx.exception
        self.assertEqual(exc.exit_code, 7)
        self.assertEqual(exc.details["expected"], fx.sha256_of(b"as generated\n"))
        self.assertEqual(exc.details["actual"], fx.sha256_of(b"edited locally\n"))
        self.assertEqual(exc.details["path"], "fixtures/body.md")
        self.assertEqual(exc.details["id"], "prompt:fixtures/target")
        self.assertIn("differs from the one the generated registry describes", exc.message)
        self.assertNotIn("edited locally", exc.message)

    def test_missing_checksum_is_refused_rather_than_served_unverified(self) -> None:
        root = self.tmp_path()
        path, _sha = fx.with_source(root, "fixtures/body.md", b"body\n")
        fx.build_repo(
            root,
            [fx.record("pae_0000000000aa", "prompt:fixtures/target", path=path,
                       content_sha256=None)],
        )
        registry = Repository.at(root).registry()
        with self.assertRaises(ChecksumMismatch):
            registry.content("prompt:fixtures/target")

    def test_unknown_checksum_payload_is_refused(self) -> None:
        root, registry = self.registry_for(
            "fixtures/body.md", checksum_payload="normalized_text"
        )
        (root / "fixtures").mkdir(parents=True, exist_ok=True)
        (root / "fixtures" / "body.md").write_bytes(b"body\n")
        with self.assertRaises(ChecksumMismatch) as ctx:
            registry.content("prompt:fixtures/target")
        self.assertEqual(ctx.exception.details["checksum_payload"], "normalized_text")

    def test_there_is_no_verification_bypass(self) -> None:
        """No CLI flag may serve unverified bytes."""
        from pae_engine import cli

        parser = cli._build_parser()
        help_text = parser.format_help()
        for banned in ("--no-verify", "--skip-verify", "--unsafe", "--force"):
            self.assertNotIn(banned, help_text)


class TestSizeCeiling(_PathCase):
    def test_oversized_source_fails_rather_than_truncating(self) -> None:
        root = self.tmp_path()
        big = b"x" * (MAX_CONTENT_BYTES + 1)
        path, sha = fx.with_source(root, "fixtures/big.md", big)
        fx.build_repo(
            root,
            [fx.record("pae_0000000000aa", "prompt:fixtures/target", path=path,
                       content_sha256=sha)],
        )
        registry = Repository.at(root).registry()
        with self.assertRaises(SourceTooLarge) as ctx:
            registry.content("prompt:fixtures/target")
        self.assertEqual(ctx.exception.exit_code, 7)
        self.assertEqual(ctx.exception.details["ceiling"], MAX_CONTENT_BYTES)

    def test_the_ceiling_is_four_mebibytes(self) -> None:
        self.assertEqual(MAX_CONTENT_BYTES, 4 * 1024 * 1024)


class TestEncoding(EngineTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.root = self.tmp_path()
        self.body = b"# heading\n\xff\xfe not utf-8\n"
        path, sha = fx.with_source(self.root, "fixtures/binary.md", self.body)
        fx.build_repo(
            self.root,
            [fx.record("pae_0000000000aa", "prompt:fixtures/target", path=path,
                       content_sha256=sha)],
        )
        self.registry = Repository.at(self.root).registry()

    def test_raw_bytes_are_still_returned_exactly(self) -> None:
        self.assertEqual(self.registry.content("prompt:fixtures/target").data, self.body)

    def test_text_decoding_is_strict(self) -> None:
        """Invalid bytes are an integrity failure, not a silent substitution."""
        content = self.registry.content("prompt:fixtures/target")
        with self.assertRaises(ContentEncodingError) as ctx:
            content.text()
        self.assertEqual(ctx.exception.exit_code, 7)
        with self.assertRaises(ContentEncodingError):
            content.to_json_obj()

    def test_cli_raw_mode_succeeds_and_json_mode_fails(self) -> None:
        raw = self.run_cli(
            ["get", "prompt:fixtures/target", "--repo", str(self.root), "--content"]
        )
        self.assertEqual(raw.code, 0)
        self.assertEqual(raw.stdout_bytes, self.body)

        as_json = self.run_cli(
            ["get", "prompt:fixtures/target", "--repo", str(self.root), "--content", "--json"]
        )
        self.assertFails(as_json, 7)


class TestWholeBodyInvariant(EngineTestCase):
    def test_no_partial_body_flags_exist(self) -> None:
        """Truncation is structurally unavailable, not merely discouraged."""
        from pae_engine import cli

        help_text = cli._build_parser().format_help()
        for banned in ("--head", "--tail", "--lines", "--max-bytes", "--excerpt",
                       "--summarize", "--truncate"):
            self.assertNotIn(banned, help_text)

    def test_content_exposes_no_partial_accessor(self) -> None:
        from pae_engine import Content

        for banned in ("head", "tail", "excerpt", "truncate", "preview"):
            self.assertFalse(hasattr(Content, banned), f"Content.{banned} must not exist")


if __name__ == "__main__":
    unittest.main()
