"""The real `pae mcp` process, over a real pipe.

The in-memory client tests prove the tool contract. They cannot prove the thing
that actually breaks stdio servers: something writing to stdout.

The checker below reads **raw bytes** rather than asking the client whether it
was happy, because Phase 6A established that the official client skips
unparseable stdout lines and completes the session anyway. A test that trusted a
successful session would pass against a server printing a banner and an absolute
repository path on every start.

So the same checker is run against two servers: the real one, which must be
clean, and a fixture that is contaminated on purpose, which must be caught. The
second assertion is what makes the first one mean anything.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

import fixtures
from _support import EngineTestCase

from pae_engine.mcp import sdk_available

if not sdk_available():  # pragma: no cover - exercised by the base CI job
    raise unittest.SkipTest("the MCP extra is not installed")

from mcp_types import (  # noqa: E402
    CLIENT_CAPABILITIES_META_KEY,
    CLIENT_INFO_META_KEY,
    LATEST_PROTOCOL_VERSION,
    PROTOCOL_VERSION_META_KEY,
)

ENGINE_ROOT = Path(__file__).resolve().parent.parent
SRC = ENGINE_ROOT / "src"
TESTS = ENGINE_ROOT / "tests"
DIRTY_FIXTURE = TESTS / "mcp_dirty_fixture.py"

TIMEOUT = 180

#: The 2026-07-28 core is stateless: there is no `initialize` handshake, and
#: capability negotiation happens per request instead. Every request therefore
#: carries the same `_meta` envelope, which the SDK's own client fills in
#: automatically and a hand-rolled probe like this one must supply itself.
_ENVELOPE = {
    "_meta": {
        PROTOCOL_VERSION_META_KEY: LATEST_PROTOCOL_VERSION,
        CLIENT_CAPABILITIES_META_KEY: {},
        CLIENT_INFO_META_KEY: {"name": "pae-stdio-purity-probe", "version": "1"},
    }
}

REQUESTS = (
    {"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": dict(_ENVELOPE)},
    {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {
            **_ENVELOPE,
            "name": "pae_search_resources",
            "arguments": {"query": "fixture", "limit": 3},
        },
    },
)


class StdoutReport:
    """What a raw stdout stream contained, split into protocol and not."""

    def __init__(self, stdout: bytes, stderr: bytes) -> None:
        self.stderr = stderr
        self.protocol: list[dict] = []
        self.foreign: list[str] = []
        for line in stdout.decode("utf-8", errors="replace").splitlines():
            if not line.strip():
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                self.foreign.append(line)
                continue
            if isinstance(obj, dict) and obj.get("jsonrpc") == "2.0":
                self.protocol.append(obj)
            else:
                self.foreign.append(line)

    @property
    def pure(self) -> bool:
        return not self.foreign


def _probe(argv: list[str], repo: Path) -> StdoutReport:
    env = dict(os.environ)
    env["PYTHONPATH"] = os.pathsep.join([str(SRC), str(TESTS)])
    env["PAE_REPO"] = str(repo)
    payload = "".join(json.dumps(request) + "\n" for request in REQUESTS)
    completed = subprocess.run(
        argv,
        input=payload.encode("utf-8"),
        capture_output=True,
        env=env,
        cwd=str(Path(sys.executable).parent),  # deliberately NOT the checkout
        timeout=TIMEOUT,
    )
    return StdoutReport(completed.stdout, completed.stderr)


class TestStdioPurity(EngineTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.repo = fixtures.standard_repo(self.tmp_path())

    def test_real_server_emits_protocol_only(self) -> None:
        report = _probe(
            [sys.executable, "-m", "pae_engine", "mcp", "--repo", str(self.repo)],
            self.repo,
        )
        self.assertTrue(
            report.pure,
            f"non-protocol bytes on stdout: {report.foreign[:5]}",
        )
        self.assertTrue(report.protocol, "the server produced no protocol output at all")

    def test_real_server_never_prints_the_checkout_path(self) -> None:
        report = _probe(
            [sys.executable, "-m", "pae_engine", "mcp", "--repo", str(self.repo)],
            self.repo,
        )
        raw = json.dumps(report.protocol) + "".join(report.foreign)
        self.assertNotIn(str(self.repo), raw)
        self.assertNotIn(str(Path.home()), raw)

    def test_the_purity_checker_catches_a_contaminated_server(self) -> None:
        # The negative control. If this passes as "pure", the assertions above
        # prove nothing.
        report = _probe([sys.executable, str(DIRTY_FIXTURE)], self.repo)
        self.assertFalse(report.pure, "the purity checker failed to detect contamination")
        joined = "\n".join(report.foreign)
        self.assertIn("PAE Engine (dirty fixture)", joined)
        self.assertIn(str(self.repo), joined)

    def test_tools_list_over_a_real_pipe_matches_the_catalog(self) -> None:
        report = _probe(
            [sys.executable, "-m", "pae_engine", "mcp", "--repo", str(self.repo)],
            self.repo,
        )
        listings = [
            message
            for message in report.protocol
            if message.get("id") == 1 and "result" in message
        ]
        self.assertTrue(listings, f"no tools/list response; stderr={report.stderr[:400]!r}")
        names = [tool["name"] for tool in listings[0]["result"]["tools"]]
        self.assertEqual(
            names,
            [
                "pae_search_resources",
                "pae_route_task",
                "pae_get_resource",
                "pae_compose_bundle",
            ],
        )


class TestStartupFailures(EngineTestCase):
    """A startup failure is an exit code and stderr, never stdout noise."""

    def test_missing_repository_fails_before_serving(self) -> None:
        empty = self.tmp_path("not-a-checkout")
        env = dict(os.environ)
        env["PYTHONPATH"] = os.pathsep.join([str(SRC), str(TESTS)])
        env.pop("PAE_REPO", None)
        completed = subprocess.run(
            [sys.executable, "-m", "pae_engine", "mcp", "--repo", str(empty)],
            input=b"",
            capture_output=True,
            env=env,
            timeout=TIMEOUT,
        )
        self.assertEqual(completed.returncode, 3)
        self.assertEqual(completed.stdout, b"", "startup failure must not touch stdout")
        self.assertIn(b"repository_not_found", completed.stderr)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
