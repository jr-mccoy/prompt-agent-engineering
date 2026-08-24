"""Enable ``python -m continuity_kit`` as an alias for the ``continuity`` CLI."""

from continuity_kit.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
