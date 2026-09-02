"""Provider adapters.

Adapters are resolved lazily and by name. Importing this package must not
import a vendor SDK, must not read a credential and must never make a request:
`plan`, `validate-benchmark`, the fake-provider run, analysis and reporting all
have to work in an environment with no provider extras installed at all.
"""

from __future__ import annotations

from typing import Any, Callable

from ..errors import ProviderNotAvailable, UsageError
from .base import (
    Message,
    ModelRequest,
    ModelResponse,
    ParticipantAdapter,
    ToolCall,
    ToolResult,
    ToolSpec,
    Usage,
)

#: Provider key -> zero-argument factory. Every factory imports its SDK only
#: when called.
_REGISTRY: dict[str, Callable[..., Any]] = {}


def _anthropic(**kw: Any) -> Any:
    from .anthropic_adapter import AnthropicAdapter

    return AnthropicAdapter(**kw)


def _openai(**kw: Any) -> Any:
    from .openai_adapter import OpenAIAdapter

    return OpenAIAdapter(**kw)


def _fake(**kw: Any) -> Any:
    from .fake import FakeAdapter

    return FakeAdapter(**kw)


_REGISTRY.update({"anthropic": _anthropic, "openai": _openai, "fake": _fake})


def available_providers() -> tuple[str, ...]:
    return tuple(sorted(_REGISTRY))


def get_adapter(provider: str, **kwargs: Any) -> ParticipantAdapter:
    """Build an adapter by provider key.

    Raises ``UsageError`` for an unknown key and ``ProviderNotAvailable`` when
    the key is known but its SDK is missing — two different problems that
    deserve two different messages.
    """
    key = (provider or "").strip().lower()
    if key not in _REGISTRY:
        raise UsageError(
            f"unknown provider {provider!r}; known providers: "
            f"{', '.join(available_providers())}"
        )
    return _REGISTRY[key](**kwargs)


def provider_is_installed(provider: str) -> bool:
    """Whether a provider's SDK can be imported, without constructing a client."""
    key = (provider or "").strip().lower()
    if key == "fake":
        return True
    try:
        __import__(key)
    except ImportError:
        return False
    return True


__all__ = [
    "Message", "ModelRequest", "ModelResponse", "ParticipantAdapter",
    "ToolCall", "ToolResult", "ToolSpec", "Usage",
    "get_adapter", "available_providers", "provider_is_installed",
    "ProviderNotAvailable",
]
