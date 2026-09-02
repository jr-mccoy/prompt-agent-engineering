"""The long-lived objects one MCP server process owns.

A stdio MCP server is the Engine's first genuinely *persistent* consumer. Every
earlier surface — the CLI — was one process per operation, so laziness was free:
nothing was ever built that the single operation did not need. A server inverts
that. The lexical index costs roughly a second to build and is then reused for
the life of the process, which is the whole reason a server is worth running.

Two properties follow, and both are load-bearing:

* **One process is one snapshot.** There is no watcher, no reload, no cache file
  and no repository-switching tool. A server answers from the checkout it was
  started against, and the way to observe a changed checkout is to restart it.
  Anything else would let an agent receive answers from a repository state it
  never asked for and cannot name.
* **The index is built exactly once.** The SDK dispatches synchronous tool
  handlers onto a thread pool, so several first-calls can land concurrently on
  an unbuilt index. Phase 6A measured that: eight concurrent cold searches
  built the index eight times and took ~11.7 s instead of ~1.2 s. The guard
  below is the fix, and it is deliberately adapter-local — the core stays
  single-threaded by construction, which is what Phases 2-5 designed for.
"""

from __future__ import annotations

import threading
from typing import Any, Optional

from ..context import ContextCompiler
from ..registry import Registry
from ..repository import Repository
from ..routing import Router
from ..search import SearchEngine

__all__ = ["PaeRuntime"]


class PaeRuntime:
    """Repository, Registry, Search, Router and Compiler, bound once.

    Construction reads nothing. That is inherited from the core: ``Registry``
    opens no file until asked, and ``SearchEngine`` builds no index until a
    lexical query needs one. The server can therefore answer ``tools/list``
    immediately while the index is still building in the background.
    """

    def __init__(self, repository: Repository) -> None:
        self.repository = repository
        self.registry: Registry = repository.registry()
        self.search = SearchEngine(self.registry)
        self.router = Router(self.search)
        self.compiler = ContextCompiler(self.registry)

        # Guards the *first* build only, and is never held during a query.
        self._warm_lock = threading.Lock()
        self._warm_thread: Optional[threading.Thread] = None
        self._warm_error: Optional[BaseException] = None

    # -- introspection -----------------------------------------------------

    @property
    def index_built(self) -> bool:
        return bool(self.search.index_info.get("built"))

    def index_info(self) -> dict[str, Any]:
        return dict(self.search.index_info)

    # -- warmup ------------------------------------------------------------

    def ensure_search_warm(self) -> None:
        """Build the lexical index if it is not built. Idempotent and safe to race.

        Double-checked: the fast path is a plain attribute read with no lock, so
        a warm server pays nothing. Only a genuinely cold caller takes the lock,
        and only the first one through it does the work — the others find the
        index built and return.

        ``search.scopes`` is used as the trigger rather than a throwaway query
        because it builds the index without going through query normalization,
        so a warmup can never fail on the shape of a synthetic query string.
        """
        if self.index_built:
            return
        with self._warm_lock:
            if self.index_built:
                return
            # Touching .scopes forces _ensure_index() and returns the scope set.
            _ = self.search.scopes

    def start_background_warmup(self) -> None:
        """Begin exactly one warmup thread, so the first real call is usually warm.

        Deliberately started *after* the server is listening: a blocking warmup
        would delay ``tools/list`` by the full build time for no benefit, since
        listing tools does not need an index. A call that arrives mid-warmup
        simply waits on the same lock, so this never causes a second build.

        A failure here is recorded rather than raised. The thread is an
        optimisation; if it dies, the next real call rebuilds through
        ``ensure_search_warm`` and reports the failure to that caller, where it
        can actually be acted on.
        """
        if self._warm_thread is not None or self.index_built:
            return

        def _warm() -> None:
            try:
                self.ensure_search_warm()
            except BaseException as exc:  # noqa: BLE001 - recorded, see docstring
                self._warm_error = exc

        thread = threading.Thread(
            target=_warm, name="pae-mcp-search-warmup", daemon=True
        )
        self._warm_thread = thread
        thread.start()

    def join_warmup(self, timeout: Optional[float] = None) -> None:
        """Wait for the background warmup. Tests use this; the server does not."""
        if self._warm_thread is not None:
            self._warm_thread.join(timeout)

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        state = "warm" if self.index_built else "cold"
        return f"PaeRuntime(root={self.repository.root!s}, index={state})"
