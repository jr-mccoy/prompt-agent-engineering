"""pae-eval — the PAE independent evaluation harness.

Separate from the Engine by design: this package calls provider APIs, spends
money and writes files, none of which the Engine runtime is permitted to do.
The dependency direction is one-way — ``pae_eval`` may import ``pae_engine``
and never the reverse.

Nothing here is imported by the ``pae`` CLI or by ``pae mcp``.
"""

from .constants import CONDITIONS, HARNESS_VERSION

__version__ = HARNESS_VERSION

__all__ = ["__version__", "CONDITIONS", "HARNESS_VERSION"]
