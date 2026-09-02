"""Measure the MCP adapter against a real checkout.

A local command, not a CI step — the same call the context-compiler diagnostics
make. It needs the ``mcp`` extra, it reads bodies, and its numbers are
observations rather than thresholds: there are no wall-clock correctness gates
here, because a shared runner's timings would fail for reasons that have nothing
to do with the adapter.

What it *does* assert is the one invariant that is not a matter of timing:
**no body crosses the wire twice**.

    PYTHONPATH=src:tests python3 tests/run_mcp_diagnostics.py --repo /path/to/checkout
"""

from __future__ import annotations

import argparse
import asyncio
import gc
import json
import sys
import time
from pathlib import Path

from mcp import Client

from pae_engine import Repository
from pae_engine.mcp.runtime import PaeRuntime
from pae_engine.mcp.server import build_server


def peak_rss_mb() -> float:
    """Best-effort peak RSS, portable across the platforms the Engine supports."""
    try:  # Unix
        import resource

        value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # Linux reports kilobytes; macOS reports bytes.
        return value / 1024 if sys.platform != "darwin" else value / (1024 * 1024)
    except ImportError:  # Windows
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

            # argtypes/restype are mandatory here: a process HANDLE is
            # pointer-sized, and without them ctypes passes it as a 32-bit int
            # on 64-bit Windows, so the call fails and reports zero.
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
                return float("nan")
            return counters.PeakWorkingSetSize / (1024 * 1024)
        except Exception:  # pragma: no cover - diagnostics only
            return float("nan")


def channel_sizes(result) -> tuple[str, int, int]:
    text = "".join(getattr(block, "text", "") or "" for block in result.content)
    blob = (
        json.dumps(result.structured_content, ensure_ascii=False)
        if result.structured_content
        else ""
    )
    return text, len(text.encode("utf-8")), len(blob.encode("utf-8"))


def largest_servable(registry) -> str | None:
    best_id, best_size = None, -1
    for record in registry.records():
        if record.serving_policy in ("standard", "safety_gated") and record.source_path:
            # byte_length is not on the record, so use the checksum'd source size
            # only when the file is actually present.
            try:
                size = (registry.repository.root / record.source_path).stat().st_size
            except OSError:
                continue
            if size > best_size:
                best_id, best_size = record.id, size
    return best_id


async def run(repo: Path) -> int:
    print(f"repository: {repo}")
    print()

    t0 = time.perf_counter()
    runtime = PaeRuntime(Repository.at(repo))
    construct_ms = (time.perf_counter() - t0) * 1000
    server = build_server(runtime)
    print(f"runtime construction (lazy)      {construct_ms:8.2f} ms")

    big = largest_servable(runtime.registry)

    rows: list[tuple[str, float, int, int]] = []
    duplication_failures: list[str] = []

    async with Client(server) as client:
        t0 = time.perf_counter()
        tools = await client.list_tools()
        print(f"tools/list                       {(time.perf_counter()-t0)*1000:8.2f} ms"
              f"  ({len(tools.tools)} tools)")
        print()

        async def measure(label, name, args, *, body_probe: str | None = None):
            t = time.perf_counter()
            result = await client.call_tool(name, args)
            elapsed = (time.perf_counter() - t) * 1000
            text, text_bytes, struct_bytes = channel_sizes(result)
            rows.append((label, elapsed, text_bytes, struct_bytes))
            if body_probe:
                blob = json.dumps(result.structured_content, ensure_ascii=False)
                if body_probe in blob:
                    duplication_failures.append(label)
            return result, text

        # First call pays for the index; everything after is warm.
        await measure("search limit=10 (cold, builds index)",
                      "pae_search_resources", {"query": "android security audit", "limit": 10})
        await measure("search limit=10 (warm)",
                      "pae_search_resources", {"query": "kubernetes helm chart", "limit": 10})
        await measure("search limit=100 (warm)",
                      "pae_search_resources", {"query": "security audit review", "limit": 100})
        await measure("route limit=5", "pae_route_task",
                      {"task": "review my terraform setup", "limit": 5})
        await measure("route limit=25", "pae_route_task",
                      {"task": "review my terraform setup", "limit": 25})
        await measure("get metadata", "pae_get_resource", {"ref": "technique:ST-01"})

        if big:
            result, text = await measure(
                f"get largest body ({big[:40]}…)",
                "pae_get_resource", {"ref": big, "include_content": True},
            )
            # Probe with a distinctive slice of the returned body.
            marker = text[len(text) // 2: len(text) // 2 + 120]
            blob = json.dumps(result.structured_content, ensure_ascii=False)
            if marker and marker in blob:
                duplication_failures.append("get largest body")

        for budget in (8000, 16000, 32000):
            result, text = await measure(
                f"bundle {budget // 1000}k", "pae_compose_bundle",
                {"task": "android security audit", "budget_estimated_tokens": budget},
            )
            included = (result.structured_content or {}).get("included", [])
            if any("content" in item for item in included):
                duplication_failures.append(f"bundle {budget}")

        # Concurrency burst, after warm.
        t = time.perf_counter()
        await asyncio.gather(*[
            client.call_tool("pae_search_resources", {"query": f"audit {i}", "limit": 5})
            for i in range(8)
        ])
        burst_ms = (time.perf_counter() - t) * 1000

    print(f"{'operation':40} {'ms':>9} {'text B':>10} {'struct B':>10} {'total B':>10}")
    print("-" * 84)
    for label, elapsed, text_bytes, struct_bytes in rows:
        print(f"{label:40} {elapsed:9.2f} {text_bytes:10} {struct_bytes:10} "
              f"{text_bytes + struct_bytes:10}")
    print()
    print(f"8-call warm burst                {burst_ms:8.2f} ms")
    print(f"index builds                     {1 if runtime.index_built else 0:8}")
    gc.collect()
    print(f"peak RSS                         {peak_rss_mb():8.1f} MB")
    print()

    if duplication_failures:
        print(f"BODY DUPLICATION DETECTED in: {duplication_failures}")
        return 1
    print("body duplication: none (0 bodies appear in structured output)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="path to a PAE checkout")
    args = parser.parse_args()
    return asyncio.run(run(Path(args.repo).resolve()))


if __name__ == "__main__":
    raise SystemExit(main())
