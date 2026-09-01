"""Inspect a module's executable code without its prose.

Docstrings and comments in this package deliberately describe what the Engine
must *not* do. A plain text search over the source would flag those very
sentences as violations, so invariant tests strip them first and assert against
what actually runs.
"""

from __future__ import annotations

import io
import tokenize
from pathlib import Path
from types import ModuleType


def code_only(module: ModuleType | str | Path) -> str:
    """The module's source with comments and string literals removed."""
    if isinstance(module, ModuleType):
        path = Path(module.__file__)  # type: ignore[arg-type]
    else:
        path = Path(module)
    source = path.read_text(encoding="utf-8")
    kept: list[str] = []
    readline = io.StringIO(source).readline
    for token in tokenize.generate_tokens(readline):
        if token.type in (tokenize.COMMENT, tokenize.STRING):
            continue
        kept.append(token.string)
    return " ".join(kept)


def _docstring_nodes(tree: "object") -> set[int]:
    import ast

    marked: set[int] = set()
    for node in ast.walk(tree):  # type: ignore[arg-type]
        if not isinstance(
            node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)
        ):
            continue
        body = getattr(node, "body", None)
        if not body:
            continue
        first = body[0]
        if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant):
            if isinstance(first.value.value, str):
                marked.add(id(first.value))
    return marked


def string_constants(path: "Path | str") -> list[str]:
    """Every string literal in a module except its docstrings.

    Docstrings describe intent, including intent to avoid something. Only the
    literals the code actually uses — paths, filenames, URLs — are returned.
    """
    import ast

    source = Path(path).read_text(encoding="utf-8")
    tree = ast.parse(source)
    skip = _docstring_nodes(tree)
    values: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if id(node) not in skip:
                values.append(node.value)
    return values
