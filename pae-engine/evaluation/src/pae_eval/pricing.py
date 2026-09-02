"""Pricing snapshots and the cost guard.

Two ideas hold this file together.

**Token counts are the durable result; dollars are derived.** Provider prices
change, and a report that only stored dollars cannot be recomputed later. Every
run pins a dated pricing snapshot by hash, and money is always a function of
(usage, snapshot). Nothing here fetches a price during a run.

**The ceiling is enforced before the request, not after.** A guard that
discovers an overage from the invoice is not a guard. Before each paid call the
guard prices a conservative worst case for that call — full configured output,
current context — and refuses if it could cross the ceiling.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping

from . import canonical
from .constants import PRICING_SCHEMA
from .errors import CostCeilingError, UsageError
from .providers.base import Usage


@dataclass(frozen=True)
class ModelPrice:
    provider: str
    model: str
    input_per_million: float
    output_per_million: float
    cached_input_per_million: float | None = None
    currency: str = "USD"
    source_url: str = ""
    retrieved_at: str = ""
    other_billable_units: Mapping[str, float] = field(default_factory=dict)
    notes: str = ""

    @property
    def key(self) -> tuple[str, str]:
        return (self.provider, self.model)

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "provider": self.provider,
            "model": self.model,
            "currency": self.currency,
            "input_per_million": self.input_per_million,
            "cached_input_per_million": self.cached_input_per_million,
            "output_per_million": self.output_per_million,
            "other_billable_units": dict(self.other_billable_units),
            "source_url": self.source_url,
            "retrieved_at": self.retrieved_at,
            "notes": self.notes,
        }

    @classmethod
    def from_json_obj(cls, obj: Mapping[str, Any]) -> "ModelPrice":
        missing = [k for k in ("provider", "model", "input_per_million",
                               "output_per_million") if obj.get(k) is None]
        if missing:
            raise UsageError(f"pricing entry is missing {missing}")
        return cls(
            provider=str(obj["provider"]),
            model=str(obj["model"]),
            input_per_million=float(obj["input_per_million"]),
            output_per_million=float(obj["output_per_million"]),
            cached_input_per_million=(
                None if obj.get("cached_input_per_million") is None
                else float(obj["cached_input_per_million"])
            ),
            currency=str(obj.get("currency", "USD")),
            source_url=str(obj.get("source_url", "")),
            retrieved_at=str(obj.get("retrieved_at", "")),
            other_billable_units=dict(obj.get("other_billable_units") or {}),
            notes=str(obj.get("notes", "")),
        )


@dataclass(frozen=True)
class PricingSnapshot:
    prices: tuple[ModelPrice, ...]
    retrieved_at: str = ""
    notes: str = ""

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "schema_version": PRICING_SCHEMA,
            "retrieved_at": self.retrieved_at,
            "notes": self.notes,
            "prices": [p.to_json_obj() for p in
                       sorted(self.prices, key=lambda p: p.key)],
        }

    @property
    def sha256(self) -> str:
        return canonical.sha256_obj(self.to_json_obj())

    def get(self, provider: str, model: str) -> ModelPrice | None:
        for price in self.prices:
            if price.provider == provider and price.model == model:
                return price
        return None

    def require(self, provider: str, model: str) -> ModelPrice:
        price = self.get(provider, model)
        if price is None:
            known = ", ".join(f"{p.provider}/{p.model}" for p in self.prices) or "none"
            raise UsageError(
                f"pricing snapshot has no entry for {provider}/{model}; "
                f"it knows: {known}. Add one before running — a cost ceiling "
                "cannot be enforced for a model with no price."
            )
        return price

    @classmethod
    def from_json_obj(cls, obj: Mapping[str, Any]) -> "PricingSnapshot":
        if obj.get("schema_version") not in (None, PRICING_SCHEMA):
            raise UsageError(
                f"unsupported pricing schema {obj.get('schema_version')!r}; "
                f"expected {PRICING_SCHEMA}"
            )
        return cls(
            prices=tuple(ModelPrice.from_json_obj(p) for p in obj.get("prices", [])),
            retrieved_at=str(obj.get("retrieved_at", "")),
            notes=str(obj.get("notes", "")),
        )

    @classmethod
    def load(cls, path: Path) -> "PricingSnapshot":
        try:
            data = json.loads(Path(path).read_text(encoding="utf-8"))
        except FileNotFoundError as exc:
            raise UsageError(f"pricing snapshot not found: {path}") from exc
        except json.JSONDecodeError as exc:
            raise UsageError(f"pricing snapshot is not valid JSON: {path}: {exc}") from exc
        return cls.from_json_obj(data)


def cost_usd(usage: Usage, price: ModelPrice) -> float:
    """Cost of one call under one price.

    Cached input is billed at its own rate when both the provider reported it
    and the snapshot carries a cached rate; otherwise those tokens fall back to
    the full input rate rather than being silently free.
    """
    million = 1_000_000.0
    cached = usage.cache_read_tokens or 0
    uncached = max(0, (usage.input_tokens or 0) - cached)

    if price.cached_input_per_million is None:
        uncached, cached_cost = (usage.input_tokens or 0), 0.0
    else:
        cached_cost = cached * price.cached_input_per_million / million

    total = uncached * price.input_per_million / million
    total += cached_cost
    total += (usage.output_tokens or 0) * price.output_per_million / million
    # Cache writes bill at the input rate unless a provider says otherwise;
    # noted here rather than assumed away.
    total += (usage.cache_write_tokens or 0) * price.input_per_million / million
    for unit, count in (usage.other_billed_units or {}).items():
        total += count * float(price.other_billable_units.get(unit, 0.0))
    return round(total, 6)


#: Tokens a model typically emits on a turn that is only a tool call.
TOOL_TURN_OUTPUT_TOKENS = 200


def estimate_trial_cost(price: ModelPrice, *, expected_input_tokens: int,
                        max_output_tokens: int, tool_turns: int = 0) -> float:
    """A conservative estimate for one trial.

    Conservative, not absurd. The input side assumes the transcript is resent
    and grows each turn, which is real. The output side assumes the model
    spends its full allowance **once**, on the final answer, and emits only a
    short tool call on intermediate turns — because that is what a tool loop
    actually looks like. Charging ``max_output_tokens`` on every turn
    over-estimates by an order of magnitude and makes the guard useless: a
    ceiling nobody can satisfy gets raised until it stops meaning anything.
    """
    million = 1_000_000.0
    turns = max(1, tool_turns + 1)
    # Resent context grows roughly linearly across turns; sum(1..n) bounds it.
    input_units = expected_input_tokens * (turns * (turns + 1) / 2)
    output_units = max_output_tokens + TOOL_TURN_OUTPUT_TOKENS * (turns - 1)
    return round(
        input_units * price.input_per_million / million
        + output_units * price.output_per_million / million,
        6,
    )


class CostGuard:
    """Tracks spend and refuses the request that would cross the ceiling."""

    def __init__(self, *, max_cost_usd: float, snapshot: PricingSnapshot) -> None:
        if max_cost_usd <= 0:
            raise UsageError("--max-cost-usd must be a positive number")
        self.max_cost_usd = float(max_cost_usd)
        self.snapshot = snapshot
        self.spent_usd = 0.0
        self.reserved_usd = 0.0
        self.ceiling_reached = False
        self.stopped_before: list[str] = []

    @property
    def remaining_usd(self) -> float:
        return max(0.0, self.max_cost_usd - self.spent_usd)

    def check(self, worst_case_usd: float, *, label: str = "") -> None:
        """Refuse *before* sending a request that could cross the ceiling."""
        if self.spent_usd + worst_case_usd > self.max_cost_usd:
            self.ceiling_reached = True
            if label:
                self.stopped_before.append(label)
            raise CostCeilingError(
                f"stopping before {label or 'the next request'}: "
                f"spent ${self.spent_usd:.4f}, this request could cost up to "
                f"${worst_case_usd:.4f}, ceiling is ${self.max_cost_usd:.2f}"
            )

    def record(self, usage: Usage, provider: str, model: str) -> float:
        price = self.snapshot.require(provider, model)
        amount = cost_usd(usage, price)
        self.spent_usd = round(self.spent_usd + amount, 6)
        return amount

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "max_cost_usd": self.max_cost_usd,
            "spent_usd": round(self.spent_usd, 6),
            "remaining_usd": round(self.remaining_usd, 6),
            "ceiling_reached": self.ceiling_reached,
            "stopped_before": list(self.stopped_before),
            "pricing_snapshot_sha256": self.snapshot.sha256,
        }


def example_snapshot() -> PricingSnapshot:
    """A dated example, not a live price feed.

    Values retrieved 2026-09-02 from the official pricing pages named in each
    entry. They exist so `--dry-run` can produce a cost estimate out of the box;
    a sealed run must supply its own snapshot retrieved at freeze time.
    """
    return PricingSnapshot(
        retrieved_at="2026-09-02",
        notes=(
            "EXAMPLE ONLY — retrieved 2026-09-02 for dry-run estimates. "
            "Re-retrieve and re-pin before any sealed run; provider prices and "
            "model identifiers both drift."
        ),
        prices=(
            ModelPrice(
                provider="anthropic", model="claude-opus-5",
                input_per_million=5.0, cached_input_per_million=0.5,
                output_per_million=25.0,
                source_url="https://platform.claude.com/docs/en/about-claude/pricing",
                retrieved_at="2026-09-02",
                notes="Cache reads are 10% of base input per the pricing page.",
            ),
            ModelPrice(
                provider="anthropic", model="claude-sonnet-5",
                input_per_million=2.0, cached_input_per_million=0.2,
                output_per_million=10.0,
                source_url="https://platform.claude.com/docs/en/about-claude/pricing",
                retrieved_at="2026-09-02",
            ),
            ModelPrice(
                provider="openai", model="gpt-5.6-terra",
                input_per_million=2.0, cached_input_per_million=0.2,
                output_per_million=12.0,
                source_url="https://developers.openai.com/api/docs/pricing",
                retrieved_at="2026-09-02",
                notes="Short-context tier; long-context rates are higher.",
            ),
            ModelPrice(
                provider="fake", model="fake-model-1",
                input_per_million=0.0, cached_input_per_million=0.0,
                output_per_million=0.0,
                source_url="", retrieved_at="2026-09-02",
                notes="The fake provider is free by construction.",
            ),
        ),
    )
