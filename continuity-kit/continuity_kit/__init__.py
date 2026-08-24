"""continuity-kit — Project Continuity Memory.

A portable, repo-local, human-readable ledger of durable project state for
human–agent software work. The CLI lives in :mod:`continuity_kit.cli` and is
exposed as the ``continuity`` console script (see pyproject.toml).

``__version__`` is the in-tree fallback used for source-checkout runs; the
installed distribution's authoritative version comes from package metadata
(``continuity_kit.cli.get_version``).
"""

# Plain literal first so setuptools can read it statically and so importing the
# package never requires importing the (heavier) CLI module.
__version__ = "0.1.0"

from continuity_kit.cli import SCHEMA_VERSION, get_version, main

__all__ = ["main", "get_version", "SCHEMA_VERSION", "__version__"]
