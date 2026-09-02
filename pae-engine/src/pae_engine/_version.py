"""Single source of truth for the Engine version.

Literal only. Nothing is computed here so that packaging tools, the CLI and
tests all read the same value without importing the rest of the package.
"""

__version__ = "0.5.0.dev0"
