#!/usr/bin/env python3
"""Broker adapters — the stubbable seam between Stage 6 and any execution venue.

For informational and research purposes only. Not financial, investment, or tax advice.
NOTHING here places real-money trades: the only active path is an in-process paper simulator.

Status (Phase 6):
  - IMPLEMENTED (stdlib only) — the PaperBrokerAdapter (builtin_simulator):
      * order-time kill switch check                     (check_halt)
      * order-time Gate B risk-limit check               (check_risk_limits)
      * deterministic paper fill at the order's price    (PaperBrokerAdapter.place_order)
      * position / cash / portfolio tracking + persistence (Portfolio.load/save)
      * loading config/risk_limits.yaml + config/mandate.yaml   (load_config; PyYAML
        if present, else an embedded YAML-subset parser — manual-only stays dependency-free)
  - DISABLED STUB (raises NotImplementedError) — real execution, gated behind Gate C:
      * LiveBrokerAdapter.place_order                     (real orders — kept OFF by design)

The contract these implement is described in ../references/broker_interface.md, the data
shapes in ../references/order_schema.md, and the order-time enforcement in
../references/risk_gate_enforcement.md. Two rules dominate everything else:
  1. Never execute real money. LiveBrokerAdapter ships disabled (Gate C: ≥100 resolved
     predictions AND Brier ≤ 0.18 AND a manual live_enabled flag — see config/mandate.yaml).
  2. Never fabricate a fill. An order that cannot clear the kill switch or Gate B is REJECTED
     (with reasons) or HALTED — it is never silently "filled" to look successful.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

# The two BROKER seams owned by this skill. The five DATA seams (MarketDataAdapter, ...)
# belong to the data-source-adapter skill, not here.
BROKER_SEAMS = ("PaperBrokerAdapter", "LiveBrokerAdapter")

# Asset classes the risk gate understands (must match config/asset_classes.yaml + risk_limits.yaml).
ASSET_CLASSES = ("equity", "crypto", "options")

# Where the running paper ledger persists (Phase-3 addition to the §7 output manifest).
DEFAULT_PORTFOLIO_PATH = "data/output/portfolio.json"

# Mirrors of the TRACKED config defaults, used ONLY so the CLI / a quick simulation runs without
# pyyaml. Real runs MUST pass the parsed config/risk_limits.yaml and config/mandate.yaml instead
# (load_config is the documented stub for that). Keys here are identical to the YAML keys so the
# enforcement logic never hardcodes a threshold — it always reads them from the dict it is given.
DEFAULT_RISK_LIMITS: Dict[str, Any] = {
    "max_position_pct": 0.02,
    "max_asset_class_pct": 0.20,
    "max_deployed_pct": 0.60,
    "per_asset_class": {
        "equity": {"max_position_pct": 0.02},
        "crypto": {"max_position_pct": 0.01},
        "options": {"max_position_pct": 0.005},
    },
    "require_stop_loss": True,
    "reject_if_unsized": True,
    "reject_if_no_premortem": True,
}

DEFAULT_MANDATE: Dict[str, Any] = {
    "halt": False,
    "capital": {"simulated_usd": 50000, "currency": "USD"},
    "live_enabled": False,
    "gate_c": {
        "min_resolved_predictions": 100,
        "max_brier_score": 0.18,
        "require_manual_enable": True,
    },
}


# --------------------------------------------------------------------------------------------
# Normalized data shapes (see ../references/order_schema.md)
# --------------------------------------------------------------------------------------------


@dataclass
class Order:
    """A normalized, venue-agnostic order, drafted by Stage 6 before any gate runs.

    `sizing_ref` / `premortem_ref` are provenance pointers proving the Stage 6 discipline ran;
    Gate B rejects the order if either is missing and the matching reject_if_* limit is set.
    `unavailable` lists any required field that could not be sourced — queued, never guessed.
    """

    order_id: str
    timestamp: str                       # ISO-8601 UTC when the order was drafted
    symbol: str
    asset_class: str                     # equity | crypto | options
    side: str                            # buy | sell
    quantity: float
    price: float                         # reference/limit price the paper fill uses
    order_type: str = "limit"            # limit | market (paper sim fills deterministically)
    stop: Optional[float] = None         # stop / exit trigger (required by Gate B)
    sizing_ref: str = ""                 # pointer to the position-sizing output (Gate B)
    premortem_ref: str = ""              # pointer to the pre-mortem output (Gate B)
    status: str = "DRAFT"                # DRAFT | CHECKED | FILLED | REJECTED | HALTED
    source: str = "stage-6"             # provenance
    notes: str = ""
    unavailable: List[str] = field(default_factory=list)

    @property
    def notional(self) -> float:
        """Cost/exposure of the order at its reference price (quantity x price)."""
        return float(self.quantity) * float(self.price)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Fill:
    """The result of routing an Order through a broker adapter.

    A Fill is emitted for EVERY routed order, including rejections and halts — the status and
    reasons are the audit trail. A REJECTED/HALTED Fill never changes the portfolio.
    """

    order_id: str
    symbol: str
    status: str                          # FILLED | REJECTED | HALTED
    filled_quantity: float = 0.0
    fill_price: Optional[float] = None
    venue: str = "PaperBrokerAdapter"
    timestamp: str = ""
    reasons: List[str] = field(default_factory=list)   # why REJECTED/HALTED (empty if FILLED)
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Position:
    """A held paper position, valued at cost basis (the sim takes no live marks)."""

    symbol: str
    asset_class: str
    quantity: float
    avg_price: float

    @property
    def notional(self) -> float:
        return float(self.quantity) * float(self.avg_price)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Portfolio:
    """The running paper account: a fixed capital base, free cash, and open positions.

    `capital_base` is the denominator for every Gate B percentage cap (it does NOT change as
    positions are opened — deploying cash moves value from `cash` into `positions`).
    """

    capital_base: float                  # = mandate capital.simulated_usd
    cash: float
    currency: str = "USD"
    positions: Dict[str, Position] = field(default_factory=dict)

    # ---- exposure helpers (all denominated against capital_base) ----

    def deployed_notional(self) -> float:
        return sum(p.notional for p in self.positions.values())

    def class_notional(self, asset_class: str) -> float:
        return sum(p.notional for p in self.positions.values() if p.asset_class == asset_class)

    def position_notional(self, symbol: str) -> float:
        return self.positions[symbol].notional if symbol in self.positions else 0.0

    # ---- persistence ----

    def to_dict(self) -> Dict[str, Any]:
        return {
            "capital_base": self.capital_base,
            "cash": self.cash,
            "currency": self.currency,
            "positions": {s: p.to_dict() for s, p in self.positions.items()},
        }

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> "Portfolio":
        positions = {
            s: Position(**p) for s, p in (obj.get("positions") or {}).items()
        }
        return cls(
            capital_base=float(obj["capital_base"]),
            cash=float(obj["cash"]),
            currency=obj.get("currency", "USD"),
            positions=positions,
        )

    @classmethod
    def load(cls, path: str = DEFAULT_PORTFOLIO_PATH, capital_base: Optional[float] = None) -> "Portfolio":
        """Load the paper ledger, or open a fresh one funded to `capital_base` if none exists."""
        if os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                return cls.from_dict(json.load(fh))
        if capital_base is None:
            raise FileNotFoundError(
                f"No portfolio at {path} and no capital_base given to open a fresh paper account."
            )
        return cls(capital_base=float(capital_base), cash=float(capital_base))

    def save(self, path: str = DEFAULT_PORTFOLIO_PATH) -> None:
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(self.to_dict(), fh, indent=2, sort_keys=True)


# --------------------------------------------------------------------------------------------
# Order-time enforcement: kill switch + Gate B (see ../references/risk_gate_enforcement.md)
# --------------------------------------------------------------------------------------------


def check_halt(mandate: Dict[str, Any]) -> bool:
    """Return True if the global kill switch is engaged (mandate.yaml: halt: true)."""
    return bool(mandate.get("halt", False))


def _effective_position_cap(limits: Dict[str, Any], asset_class: str) -> float:
    """Per-position cap for a class: the LOWER of the portfolio cap and any per-class override."""
    portfolio_cap = float(limits["max_position_pct"])
    override = (limits.get("per_asset_class") or {}).get(asset_class, {})
    class_cap = float(override.get("max_position_pct", portfolio_cap))
    return min(portfolio_cap, class_cap)


def check_risk_limits(
    order: Order, portfolio: Portfolio, limits: Dict[str, Any]
) -> Tuple[bool, List[str]]:
    """Gate B: a buy order may proceed only if it clears EVERY check. Returns (passed, reasons).

    Thresholds are read from `limits` (the parsed config/risk_limits.yaml), never hardcoded.
    Sells reduce exposure and skip the caps, but cannot sell more than is held (no naked shorts
    in the paper sim v1). Caps are evaluated on the POST-order state, denominated by capital_base.
    """
    reasons: List[str] = []

    if order.asset_class not in ASSET_CLASSES:
        reasons.append(f"unknown asset_class '{order.asset_class}' (expected one of {ASSET_CLASSES})")
        return False, reasons

    # --- Discipline gates (apply to any order) ---
    if limits.get("require_stop_loss", True) and order.stop is None:
        reasons.append("require_stop_loss: order has no stop / exit trigger")
    if limits.get("reject_if_unsized", True) and not order.sizing_ref:
        reasons.append("reject_if_unsized: no position-sizing output attached (sizing_ref empty)")
    if limits.get("reject_if_no_premortem", True) and not order.premortem_ref:
        reasons.append("reject_if_no_premortem: no pre-mortem attached (premortem_ref empty)")

    side = order.side.lower()
    if side == "sell":
        held = portfolio.positions.get(order.symbol)
        if held is None or order.quantity > held.quantity + 1e-9:
            reasons.append("sell exceeds held quantity (no naked shorts in paper sim v1)")
        return (len(reasons) == 0), reasons

    if side != "buy":
        reasons.append(f"unsupported side '{order.side}' (expected buy | sell)")
        return False, reasons

    base = float(portfolio.capital_base)
    if base <= 0:
        reasons.append("capital_base is zero/negative — cannot evaluate caps")
        return False, reasons

    # --- Cash: a paper buy cannot deploy more than free cash ---
    if order.notional > portfolio.cash + 1e-9:
        reasons.append(
            f"insufficient cash: notional {order.notional:,.2f} > free cash {portfolio.cash:,.2f}"
        )

    # --- Per-position cap (lower of portfolio / per-class), on post-order position notional ---
    pos_cap = _effective_position_cap(limits, order.asset_class)
    post_position = portfolio.position_notional(order.symbol) + order.notional
    if post_position > pos_cap * base + 1e-9:
        reasons.append(
            f"per-position cap: {post_position / base:.4f} of capital > limit {pos_cap:.4f} "
            f"for {order.symbol} ({order.asset_class})"
        )

    # --- Per-asset-class cap, on post-order class notional ---
    class_cap = float(limits["max_asset_class_pct"])
    post_class = portfolio.class_notional(order.asset_class) + order.notional
    if post_class > class_cap * base + 1e-9:
        reasons.append(
            f"per-asset-class cap: {post_class / base:.4f} of capital in '{order.asset_class}' "
            f"> limit {class_cap:.4f}"
        )

    # --- Total deployed cap, on post-order deployed notional ---
    deployed_cap = float(limits["max_deployed_pct"])
    post_deployed = portfolio.deployed_notional() + order.notional
    if post_deployed > deployed_cap * base + 1e-9:
        reasons.append(
            f"deployed cap: {post_deployed / base:.4f} of capital deployed > limit {deployed_cap:.4f}"
        )

    return (len(reasons) == 0), reasons


def exposure_report(portfolio: Portfolio, limits: Dict[str, Any]) -> Dict[str, Any]:
    """Read-only paper-exposure report: deployed / per-class / per-position vs the Gate B caps.

    Computes nothing about orders and never mutates the ledger — it just makes current paper
    exposure auditable (the transparency side of Gate B). Each line carries the fraction of
    capital_base and whether it is within its cap.
    """
    base = float(portfolio.capital_base)
    deployed_cap = float(limits["max_deployed_pct"])
    class_cap = float(limits["max_asset_class_pct"])
    deployed = portfolio.deployed_notional()

    classes = {}
    for cls in sorted({p.asset_class for p in portfolio.positions.values()}):
        cn = portfolio.class_notional(cls)
        classes[cls] = {"notional": cn, "fraction": (cn / base if base else 0.0),
                        "cap": class_cap, "within": cn <= class_cap * base + 1e-9}

    positions = {}
    for sym, pos in sorted(portfolio.positions.items()):
        cap = _effective_position_cap(limits, pos.asset_class)
        pn = pos.notional
        positions[sym] = {"asset_class": pos.asset_class, "notional": pn,
                          "fraction": (pn / base if base else 0.0), "cap": cap,
                          "within": pn <= cap * base + 1e-9}

    return {
        "capital_base": base,
        "cash": portfolio.cash,
        "deployed": {"notional": deployed, "fraction": (deployed / base if base else 0.0),
                     "cap": deployed_cap, "within": deployed <= deployed_cap * base + 1e-9},
        "by_class": classes,
        "by_position": positions,
    }


# --------------------------------------------------------------------------------------------
# Broker adapters
# --------------------------------------------------------------------------------------------


class PaperBrokerAdapter:
    """ACTIVE built-in paper simulator (config/data_sources.yaml: implementation: builtin_simulator).

    Routes an order through the kill switch, then Gate B, then a deterministic fill at the order's
    reference price, updating the portfolio. It never reaches a real venue and never fabricates a
    fill: an order that fails any check returns a REJECTED/HALTED Fill with reasons and leaves the
    portfolio untouched.
    """

    seam = "PaperBrokerAdapter"

    def __init__(self, mandate: Dict[str, Any], limits: Dict[str, Any]):
        self.mandate = mandate
        self.limits = limits

    def place_order(self, order: Order, portfolio: Portfolio) -> Fill:
        now = datetime.now(timezone.utc).isoformat()

        # 1. Kill switch — checked first, before any sizing logic.
        if check_halt(self.mandate):
            order.status = "HALTED"
            return Fill(
                order_id=order.order_id, symbol=order.symbol, status="HALTED",
                venue=self.seam, timestamp=now,
                reasons=["kill switch engaged (mandate.yaml halt: true) — action stages stopped"],
            )

        # 2. Gate B — risk-limit + discipline check.
        passed, reasons = check_risk_limits(order, portfolio, self.limits)
        if not passed:
            order.status = "REJECTED"
            return Fill(
                order_id=order.order_id, symbol=order.symbol, status="REJECTED",
                venue=self.seam, timestamp=now, reasons=reasons,
                notes="Gate B failed — no paper fill.",
            )

        # 3. Deterministic paper fill at the reference price; update the ledger.
        order.status = "CHECKED"
        self._apply_fill(order, portfolio)
        order.status = "FILLED"
        return Fill(
            order_id=order.order_id, symbol=order.symbol, status="FILLED",
            filled_quantity=order.quantity, fill_price=order.price,
            venue=self.seam, timestamp=now,
            notes="Simulated fill at reference price (no slippage model in v1).",
        )

    @staticmethod
    def _apply_fill(order: Order, portfolio: Portfolio) -> None:
        """Mutate the portfolio for a cleared order (buy opens/increases; sell reduces/closes)."""
        side = order.side.lower()
        if side == "buy":
            portfolio.cash -= order.notional
            existing = portfolio.positions.get(order.symbol)
            if existing is None:
                portfolio.positions[order.symbol] = Position(
                    symbol=order.symbol, asset_class=order.asset_class,
                    quantity=order.quantity, avg_price=order.price,
                )
            else:
                total_qty = existing.quantity + order.quantity
                existing.avg_price = (
                    (existing.notional + order.notional) / total_qty if total_qty else order.price
                )
                existing.quantity = total_qty
        elif side == "sell":
            portfolio.cash += order.notional
            existing = portfolio.positions[order.symbol]
            existing.quantity -= order.quantity
            if existing.quantity <= 1e-9:
                del portfolio.positions[order.symbol]


class LiveBrokerAdapter:
    """DISABLED real-execution adapter — present by design, OFF by design (Gate C).

    This is the seam where a real broker API would live. It ships disabled and MUST NOT be
    implemented or enabled until Gate C is met. Even calling place_order is a hard stop.
    """

    seam = "LiveBrokerAdapter"

    def __init__(self, mandate: Dict[str, Any], enabled: bool = False):
        self.mandate = mandate
        # `enabled` mirrors config/data_sources.yaml LiveBrokerAdapter.enabled (false by default).
        self.enabled = enabled

    def gate_c_status(self, resolved_predictions: int, brier: Optional[float]) -> Tuple[bool, List[str]]:
        """Report whether all THREE Gate C conditions are met (does NOT enable anything)."""
        gate_c = self.mandate.get("gate_c", {})
        unmet: List[str] = []
        if resolved_predictions < int(gate_c.get("min_resolved_predictions", 100)):
            unmet.append(
                f"resolved predictions {resolved_predictions} < "
                f"{gate_c.get('min_resolved_predictions', 100)}"
            )
        if brier is None or brier > float(gate_c.get("max_brier_score", 0.18)):
            unmet.append(f"Brier {brier} not at/below {gate_c.get('max_brier_score', 0.18)}")
        if not bool(self.mandate.get("live_enabled", False)):
            unmet.append("live_enabled is false (manual switch not flipped)")
        return (len(unmet) == 0), unmet

    def place_order(self, order: Order, portfolio: Portfolio) -> Fill:
        """Real execution — documented, DISABLED stub. Never wire this on without Gate C + review."""
        raise NotImplementedError(
            "LiveBrokerAdapter is DISABLED (Gate C). Real-money execution is intentionally not "
            "implemented. To ever enable it: (1) accumulate >=100 resolved journaled predictions, "
            "(2) reach a running Brier <= 0.18, (3) set live_enabled: true in config/mandate.yaml by "
            "hand AND enabled: true in config/data_sources.yaml, then implement a real broker API "
            "branch here behind per-trade human approval. Until then, route orders to "
            "PaperBrokerAdapter."
        )


# --------------------------------------------------------------------------------------------
# Minimal YAML-subset loader (stdlib only; PyYAML used if present). Handles exactly what
# config/risk_limits.yaml + config/mandate.yaml need: block maps, block scalars (>, |), flow
# seqs [..], flow maps {..}, and scalars. Keeps manual-only mode dependency-free.
# --------------------------------------------------------------------------------------------


def _load_yaml(text: str):
    try:
        import yaml  # type: ignore
    except ImportError:
        return _mini_yaml_load(text)
    return yaml.safe_load(text)


def _strip_comment(s: str) -> str:
    out, in_s, in_d, i = [], False, False, 0
    while i < len(s):
        c = s[i]
        if c == "'" and not in_d:
            in_s = not in_s
        elif c == '"' and not in_s:
            in_d = not in_d
        elif c == "#" and not in_s and not in_d and (i == 0 or s[i - 1] in " \t"):
            break
        out.append(c)
        i += 1
    return "".join(out).rstrip()


def _split_kv(s: str):
    idx = s.find(":")
    if idx < 0:
        return s.strip(), False, ""
    return s[:idx].strip().strip("\"'"), True, s[idx + 1:]


def _split_flow(inner: str):
    parts, depth, in_s, in_d, cur = [], 0, False, False, ""
    for c in inner:
        if c == '"' and not in_s:
            in_d = not in_d
            cur += c
        elif c == "'" and not in_d:
            in_s = not in_s
            cur += c
        elif not in_s and not in_d:
            if c in "[{":
                depth += 1
                cur += c
            elif c in "]}":
                depth -= 1
                cur += c
            elif c == "," and depth == 0:
                parts.append(cur)
                cur = ""
            else:
                cur += c
        else:
            cur += c
    if cur.strip() != "":
        parts.append(cur)
    return parts


def _parse_scalar(val: str):
    val = val.strip()
    if val == "":
        return None
    if val[0] == "[":
        inner = val[1:-1].strip()
        return [] if inner == "" else [_parse_scalar(p.strip()) for p in _split_flow(inner)]
    if val[0] == "{":
        inner = val[1:-1].strip()
        if inner == "":
            return {}
        out = {}
        for p in _split_flow(inner):
            k, has, v = _split_kv(p.strip())
            if has:
                out[k] = _parse_scalar(v.strip())
        return out
    if (val[0] == '"' and val[-1] == '"') or (val[0] == "'" and val[-1] == "'"):
        return val[1:-1]
    low = val.lower()
    if low in ("null", "~"):
        return None
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    try:
        return int(val)
    except ValueError:
        pass
    try:
        return float(val)
    except ValueError:
        return val


def _mini_yaml_load(text: str):
    lines = text.split("\n")
    index = [0]

    def parse_map(min_indent: int):
        result: Dict[str, Any] = {}
        while index[0] < len(lines):
            raw = lines[index[0]]
            if raw.strip() == "" or raw.lstrip().startswith("#"):
                index[0] += 1
                continue
            indent = len(raw) - len(raw.lstrip(" "))
            if indent < min_indent:
                break
            key, has, val = _split_kv(_strip_comment(raw).strip())
            index[0] += 1
            if not has:
                continue
            val = val.strip()
            if val in (">", "|", ">-", "|-"):
                block = []
                while index[0] < len(lines):
                    bl = lines[index[0]]
                    if bl.strip() == "":
                        block.append("")
                        index[0] += 1
                        continue
                    if (len(bl) - len(bl.lstrip(" "))) <= indent:
                        break
                    block.append(bl.strip())
                    index[0] += 1
                result[key] = " ".join(b for b in block if b != "")
            elif val == "":
                result[key] = parse_map(indent + 1)
            else:
                result[key] = _parse_scalar(val)
        return result

    return parse_map(0)


def load_config(
    risk_limits_path: str = "config/risk_limits.yaml",
    mandate_path: str = "config/mandate.yaml",
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Load (risk_limits, mandate) from YAML.

    Uses PyYAML if installed, else the embedded stdlib YAML-subset parser, so this works in
    manual-only mode with no dependencies. Thresholds are returned unchanged for the order-time
    enforcement to read — never mutated, never defaulted-in silently.
    """
    with open(risk_limits_path, encoding="utf-8") as fh:
        limits = _load_yaml(fh.read())
    with open(mandate_path, encoding="utf-8") as fh:
        mandate = _load_yaml(fh.read())
    if not isinstance(limits, dict) or not isinstance(mandate, dict):
        raise ValueError("config files did not parse to mappings")
    return limits, mandate


# --------------------------------------------------------------------------------------------
# CLI — simulate placing one order against a (loaded or fresh) paper portfolio.
# --------------------------------------------------------------------------------------------


def _self_check() -> int:
    """Prove the order-time gates in code, on an in-memory portfolio (no files written)."""
    failures: List[str] = []
    mandate = dict(DEFAULT_MANDATE)
    limits = DEFAULT_RISK_LIMITS
    capital_base = float(mandate["capital"]["simulated_usd"])  # 50,000

    def fresh():
        return Portfolio(capital_base=capital_base, cash=capital_base)

    def order(**kw):
        base = dict(
            order_id="ORD-TEST", timestamp="2026-06-18T00:00:00+00:00",
            symbol="EXMP", asset_class="equity", side="buy", quantity=100, price=5.0,
            stop=4.25, sizing_ref="orders.md#sizing", premortem_ref="orders.md#premortem",
        )
        base.update(kw)
        return Order(**base)

    broker = PaperBrokerAdapter(mandate=mandate, limits=limits)

    # 1. Compliant equity buy ($500 = 1% of $50k) -> FILLED, ledger updated.
    pf = fresh()
    f = broker.place_order(order(), pf)
    if f.status != "FILLED" or "EXMP" not in pf.positions or abs(pf.cash - 49500) > 1e-6:
        failures.append(f"compliant order should FILL and deploy $500, got {f.to_dict()}")

    # 2. Unsized order (no sizing_ref) -> REJECTED (Gate B discipline).
    f = broker.place_order(order(sizing_ref=""), fresh())
    if f.status != "REJECTED" or not any("unsized" in r for r in f.reasons):
        failures.append(f"unsized order should be REJECTED, got {f.to_dict()}")

    # 3. No stop -> REJECTED (Gate B discipline).
    f = broker.place_order(order(stop=None), fresh())
    if f.status != "REJECTED" or not any("stop" in r for r in f.reasons):
        failures.append(f"no-stop order should be REJECTED, got {f.to_dict()}")

    # 4. Over per-position cap (500 x $5 = $2,500 = 5% > 2%) -> REJECTED.
    f = broker.place_order(order(quantity=500), fresh())
    if f.status != "REJECTED" or not any("per-position cap" in r for r in f.reasons):
        failures.append(f"over-cap order should be REJECTED, got {f.to_dict()}")

    # 5. Kill switch engaged -> HALTED, no fill.
    halted_broker = PaperBrokerAdapter(mandate={**mandate, "halt": True}, limits=limits)
    pf = fresh()
    f = halted_broker.place_order(order(), pf)
    if f.status != "HALTED" or pf.positions:
        failures.append(f"halt:true should HALT with no fill, got {f.to_dict()}")

    # 6a. Exposure report on the filled ledger: $500 of $50k deployed = 1% (within all caps).
    pf = fresh()
    broker.place_order(order(), pf)
    rep = exposure_report(pf, limits)
    if abs(rep["deployed"]["fraction"] - 0.01) > 1e-9 or not rep["deployed"]["within"]:
        failures.append(f"exposure report should show 1% deployed within cap, got {rep['deployed']}")
    if not rep["by_position"]["EXMP"]["within"]:
        failures.append(f"EXMP position should be within its per-class cap, got {rep['by_position']}")

    # 6. Gate C: LiveBrokerAdapter is unreachable (place_order raises).
    live = LiveBrokerAdapter(mandate=mandate)
    try:
        live.place_order(order(), fresh())
        failures.append("LiveBrokerAdapter.place_order must raise (Gate C) — it did not")
    except NotImplementedError:
        pass
    ready, unmet = live.gate_c_status(resolved_predictions=3, brier=0.29)
    if ready or not unmet:
        failures.append(f"Gate C must report not-ready for a thin record, got {(ready, unmet)}")

    if failures:
        print("SELF-CHECK FAILED:", file=sys.stderr)
        for x in failures:
            print(f"  - {x}", file=sys.stderr)
        return 1
    print("SELF-CHECK PASSED (FILLED / 3x REJECTED / HALTED / Live disabled)")
    return 0


def _main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Paper-broker simulator (Phase 6). Routes ONE order through the kill switch and Gate B, "
            "then a deterministic paper fill. Real execution is disabled (Gate C). Uses the tracked "
            "config defaults unless --config points at the YAML files."
        ),
    )
    parser.add_argument("--self-check", action="store_true",
                        help="Run the embedded gate fixtures and exit (no files written).")
    parser.add_argument("--report", action="store_true",
                        help="Read-only: print current paper exposure (deployed/class/position vs caps) and exit.")
    parser.add_argument("--symbol", help="Ticker / token / underlying.")
    parser.add_argument("--asset-class", dest="asset_class",
                        choices=list(ASSET_CLASSES), help="equity | crypto | options.")
    parser.add_argument("--side", default="buy", choices=["buy", "sell"], help="buy | sell.")
    parser.add_argument("--quantity", type=float, help="Units to trade.")
    parser.add_argument("--price", type=float, help="Reference/limit price.")
    parser.add_argument("--stop", type=float, default=None, help="Stop / exit trigger (Gate B).")
    parser.add_argument("--sizing-ref", dest="sizing_ref", default="",
                        help="Pointer to the position-sizing output (Gate B).")
    parser.add_argument("--premortem-ref", dest="premortem_ref", default="",
                        help="Pointer to the pre-mortem output (Gate B).")
    parser.add_argument("--portfolio", default=DEFAULT_PORTFOLIO_PATH,
                        help=f"Paper ledger path (default {DEFAULT_PORTFOLIO_PATH}).")
    parser.add_argument("--config", metavar="CONFIG_DIR", default=None,
                        help="Directory holding risk_limits.yaml + mandate.yaml (else tracked defaults).")
    parser.add_argument("--halt", action="store_true",
                        help="Engage the kill switch for this run (overrides config mandate).")
    parser.add_argument("--no-save", action="store_true",
                        help="Do not persist the resulting portfolio (dry run).")
    args = parser.parse_args(argv)

    if args.self_check:
        return _self_check()

    if args.report:
        if args.config:
            limits, mandate = load_config(
                os.path.join(args.config, "risk_limits.yaml"),
                os.path.join(args.config, "mandate.yaml"),
            )
        else:
            mandate, limits = dict(DEFAULT_MANDATE), DEFAULT_RISK_LIMITS
        capital_base = float(mandate["capital"]["simulated_usd"])
        portfolio = Portfolio.load(args.portfolio, capital_base=capital_base)
        print(json.dumps(exposure_report(portfolio, limits), indent=2, sort_keys=True))
        return 0

    for req in ("symbol", "asset_class", "quantity", "price"):
        if getattr(args, req) in (None,):
            parser.error(f"--{req.replace('_', '-')} is required (or use --self-check)")

    if args.config:
        limits, mandate = load_config(
            os.path.join(args.config, "risk_limits.yaml"),
            os.path.join(args.config, "mandate.yaml"),
        )
    else:
        mandate = dict(DEFAULT_MANDATE)
        limits = DEFAULT_RISK_LIMITS
    if args.halt:
        mandate = {**mandate, "halt": True}
    capital_base = float(mandate["capital"]["simulated_usd"])

    portfolio = Portfolio.load(args.portfolio, capital_base=capital_base)

    order = Order(
        order_id=f"ORD-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}",
        timestamp=datetime.now(timezone.utc).isoformat(),
        symbol=args.symbol, asset_class=args.asset_class, side=args.side,
        quantity=args.quantity, price=args.price, stop=args.stop,
        sizing_ref=args.sizing_ref, premortem_ref=args.premortem_ref,
    )

    broker = PaperBrokerAdapter(mandate=mandate, limits=limits)
    fill = broker.place_order(order, portfolio)

    if fill.status == "FILLED" and not args.no_save:
        portfolio.save(args.portfolio)

    print(json.dumps(
        {"order": order.to_dict(), "fill": fill.to_dict(), "portfolio": portfolio.to_dict()},
        indent=2, sort_keys=True,
    ))
    return 0 if fill.status == "FILLED" else 1


if __name__ == "__main__":
    raise SystemExit(_main())
