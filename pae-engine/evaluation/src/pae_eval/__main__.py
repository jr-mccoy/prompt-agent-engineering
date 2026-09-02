"""``python -m pae_eval`` entry point.

Deliberately not a console script and deliberately not a ``pae`` subcommand:
the end-user CLI is a read-only, no-network runtime, and evaluation must not be
one tab-completion away from it.
"""

from __future__ import annotations

import sys

from .cli import main

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
