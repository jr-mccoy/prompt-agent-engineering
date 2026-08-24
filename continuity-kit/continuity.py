#!/usr/bin/env python3
"""Source-checkout compatibility shim for the continuity CLI.

Phase 7 moved the implementation into the installable ``continuity_kit``
package (``continuity_kit/cli.py``). This thin shim keeps two source-tree
workflows working with zero changes:

  * ``python continuity.py <command>``  — the form CI and the docs use; and
  * ``import continuity``               — the form the test suite uses
                                          (``continuity.main``, ``continuity.Record``,
                                          ``continuity._VERDICTS``, …).

It re-exports every public *and* private module-level name from
``continuity_kit.cli`` so existing tests that reach into internals keep passing.
Installed users get the ``continuity`` console script instead and never touch
this file.
"""

import continuity_kit.cli as _cli

# Re-export everything except dunders, so this module's own __name__/__file__
# stay intact (the __main__ guard below depends on __name__ == "__main__").
globals().update({k: v for k, v in vars(_cli).items() if not k.startswith("__")})

main = _cli.main

if __name__ == "__main__":
    raise SystemExit(main())
