"""A standard-library validator for the JSON Schema subset this registry uses.

ADR-0003 keeps the core to the standard library plus PyYAML, so ``jsonschema``
is not available. The schemas in ``meta/registry/schemas/`` are still real JSON
Schema documents — they are the published contract — and this module implements
exactly the keywords they use. An unsupported keyword is a hard error rather
than a silent pass, so the validator can never drift behind the schema.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

SUPPORTED = frozenset(
    {
        "$schema",
        "$id",
        "$ref",
        "$defs",
        "title",
        "description",
        "type",
        "enum",
        "const",
        "pattern",
        "format",
        "properties",
        "required",
        "additionalProperties",
        "items",
        "minItems",
        "uniqueItems",
        "minLength",
        "anyOf",
        "examples",
    }
)

TYPES = {
    "object": dict,
    "array": list,
    "string": str,
    "integer": int,
    "number": (int, float),
    "boolean": bool,
    "null": type(None),
}


class SchemaError(RuntimeError):
    """The schema itself uses something this validator does not implement."""


def load(path: Path) -> dict:
    schema = json.loads(path.read_text(encoding="utf-8"))
    _assert_supported(schema, path.name)
    return schema


def _assert_supported(node: Any, where: str) -> None:
    if isinstance(node, dict):
        unknown = set(node) - SUPPORTED
        if unknown and "properties" not in where:
            # Property *names* are arbitrary; only schema nodes are checked.
            pass
        for key, value in node.items():
            if key == "properties" and isinstance(value, dict):
                for prop, sub in value.items():
                    _assert_supported(sub, f"{where}.properties.{prop}")
            elif key == "$defs" and isinstance(value, dict):
                for name, sub in value.items():
                    _assert_supported(sub, f"{where}.$defs.{name}")
            elif key in {"items", "additionalProperties"} and isinstance(value, dict):
                _assert_supported(value, f"{where}.{key}")
            elif key == "anyOf" and isinstance(value, list):
                for i, sub in enumerate(value):
                    _assert_supported(sub, f"{where}.anyOf[{i}]")
            elif key not in SUPPORTED:
                raise SchemaError(f"{where}: unsupported schema keyword {key!r}")


def _resolve(schema: dict, root: dict) -> dict:
    ref = schema.get("$ref")
    if not ref:
        return schema
    if not ref.startswith("#/$defs/"):
        raise SchemaError(f"unsupported $ref {ref!r}")
    name = ref[len("#/$defs/"):]
    target = root.get("$defs", {}).get(name)
    if target is None:
        raise SchemaError(f"unresolved $ref {ref!r}")
    return target


def validate(instance: Any, schema: dict, root: dict | None = None, path: str = "$") -> list[str]:
    """Return a list of human-readable errors; empty means valid."""
    root = root if root is not None else schema
    schema = _resolve(schema, root)
    errors: list[str] = []

    if "anyOf" in schema:
        branches = [validate(instance, sub, root, path) for sub in schema["anyOf"]]
        if all(branch for branch in branches):
            errors.append(f"{path}: does not match any allowed variant")
        return errors

    expected = schema.get("type")
    if expected is not None:
        types = expected if isinstance(expected, list) else [expected]
        # bool is a subclass of int in Python; JSON Schema treats them apart.
        ok = any(
            isinstance(instance, TYPES[t]) and not (t in {"integer", "number"} and isinstance(instance, bool))
            for t in types
        )
        if not ok:
            return [f"{path}: expected type {expected}, got {type(instance).__name__}"]

    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected const {schema['const']!r}, got {instance!r}")
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: {instance!r} is not one of {schema['enum']}")
    if isinstance(instance, str):
        if "pattern" in schema and not re.search(schema["pattern"], instance):
            errors.append(f"{path}: {instance!r} does not match {schema['pattern']}")
        if "minLength" in schema and len(instance) < schema["minLength"]:
            errors.append(f"{path}: shorter than minLength {schema['minLength']}")

    if isinstance(instance, dict):
        for key in schema.get("required", []):
            if key not in instance:
                errors.append(f"{path}: missing required property {key!r}")
        properties = schema.get("properties", {})
        for key, value in instance.items():
            if key in properties:
                errors.extend(validate(value, properties[key], root, f"{path}.{key}"))
            else:
                extra = schema.get("additionalProperties", True)
                if extra is False:
                    errors.append(f"{path}: unexpected property {key!r}")
                elif isinstance(extra, dict):
                    errors.extend(validate(value, extra, root, f"{path}.{key}"))

    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            errors.append(f"{path}: fewer than minItems {schema['minItems']}")
        if schema.get("uniqueItems") and len(instance) != len({json.dumps(i, sort_keys=True) for i in instance}):
            errors.append(f"{path}: items are not unique")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for i, item in enumerate(instance):
                errors.extend(validate(item, item_schema, root, f"{path}[{i}]"))

    return errors
