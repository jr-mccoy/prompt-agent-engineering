"""LLM judging — absolute rubric scoring and blinded pairwise comparison.

The judge sees the task, the deliverable spec, the rubric, and answers under
opaque IDs. It does not see the condition, the participant model, tool traces,
PAE identifiers, bundle hashes, or the repository. Those omissions are enforced
when the payload is built, not asked for in the prompt, because a prompt is a
request and a construction is a guarantee (spec §60).

Pairwise comparison is used only on the primary D-vs-B contrast, where its extra
sensitivity is worth the extra call. Answer order comes from the frozen
randomization schedule, and the mapping from side to condition is applied only
*after* the verdict is stored — so nothing in the judging path can condition on
which arm produced which answer.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence

from .. import canonical
from ..errors import IsolationError, UsageError
from ..providers.base import Message, ModelRequest, ParticipantAdapter

ABSOLUTE_JUDGE_PROMPT = """\
You are grading one answer against a fixed rubric.

You will be given a task, the deliverable the answer was supposed to produce,
and a list of rubric criteria. Score each criterion independently on its own
terms. Do not reward length, confidence, or formatting that the criterion does
not ask for.

For each criterion return:
  - score: a number from 0.0 to 1.0
  - passed: true or false
  - evidence: one or two sentences quoting or citing the part of the answer
    that decided it

Also return fabrication_flagged: true if the answer states facts, citations,
identifiers or authorities that it invents or cannot support. An answer that
says it is uncertain is not fabricating.

Respond with a single JSON object and nothing else:

{"criteria": {"<criterion_id>": {"score": 0.0, "passed": false,
 "evidence": "..."}}, "fabrication_flagged": false}
"""

PAIRWISE_JUDGE_PROMPT = """\
You are comparing two answers to the same task against a fixed rubric.

The answers are labelled LEFT and RIGHT. Their order is randomized and carries
no meaning. Judge only how well each satisfies the rubric.

Respond with a single JSON object and nothing else:

{"winner": "left" | "right" | "tie" | "unjudgeable", "reason": "..."}

Use "tie" when the answers are genuinely equivalent against the rubric, and
"unjudgeable" only when the rubric cannot be applied to what you were given.
"""

#: Substrings that must never reach a judge payload. A condition label or a PAE
#: identifier would let the judge infer the arm and grade the arm.
FORBIDDEN_IN_PAYLOAD = (
    "condition A", "condition B", "condition C", "condition D",
    "pae_search_resources", "pae_route_task", "pae_compose_bundle",
    "pae_get_resource", "bundle_sha256", "acceptable_resource_uids",
    "label_rationale", "scored_dimensions", "participant_model",
)


@dataclass(frozen=True)
class OpaqueAnswer:
    """An answer stripped of everything that identifies its condition."""

    answer_id: str
    text: str

    @classmethod
    def create(cls, trial_id: str, text: str, salt: str = "") -> "OpaqueAnswer":
        digest = canonical.sha256_obj({"trial": trial_id, "salt": salt})
        return cls(answer_id=f"ans_{canonical.short(digest, 10)}", text=text)


@dataclass
class JudgeVerdict:
    payload: Mapping[str, Any]
    raw_text: str
    judge_provider: str
    judge_model: str
    ok: bool = True
    error: str | None = None

    def to_json_obj(self) -> dict[str, Any]:
        return {
            "payload": dict(self.payload),
            "raw_text": self.raw_text,
            "judge_provider": self.judge_provider,
            "judge_model": self.judge_model,
            "ok": self.ok,
            "error": self.error,
        }


def _assert_payload_blind(text: str) -> None:
    hits = [marker for marker in FORBIDDEN_IN_PAYLOAD if marker in text]
    if hits:
        raise IsolationError(
            f"judge payload leaks condition or evaluation metadata: {hits[:3]}"
        )


def render_rubric(task: Any) -> str:
    lines = []
    for criterion in task.criteria:
        if criterion.type != "judge":
            continue
        lines.append(
            f"- {criterion.criterion_id}: {criterion.description}\n"
            f"  Instruction: {criterion.judge_instruction}"
        )
    return "\n".join(lines) if lines else "(no judge-scored criteria)"


def build_absolute_payload(task: Any, answer: OpaqueAnswer) -> str:
    payload = (
        f"TASK\n{task.query.strip()}\n\n"
        f"DELIVERABLE\n{task.deliverable.strip()}\n\n"
        f"RUBRIC\n{render_rubric(task)}\n\n"
        f"ANSWER {answer.answer_id}\n{answer.text.strip()}\n"
    )
    _assert_payload_blind(payload)
    return payload


def build_pairwise_payload(task: Any, left: OpaqueAnswer, right: OpaqueAnswer) -> str:
    payload = (
        f"TASK\n{task.query.strip()}\n\n"
        f"DELIVERABLE\n{task.deliverable.strip()}\n\n"
        f"RUBRIC\n{render_rubric(task)}\n\n"
        f"LEFT ({left.answer_id})\n{left.text.strip()}\n\n"
        f"RIGHT ({right.answer_id})\n{right.text.strip()}\n"
    )
    _assert_payload_blind(payload)
    return payload


def parse_json_object(text: str) -> Mapping[str, Any] | None:
    """Extract the judge's JSON object, tolerating a fenced block."""
    candidate = text.strip()
    fence = re.search(r"```(?:json)?\s*\n(.*?)```", candidate, re.DOTALL)
    if fence:
        candidate = fence.group(1).strip()
    if not candidate.startswith("{"):
        start = candidate.find("{")
        end = candidate.rfind("}")
        if start < 0 or end <= start:
            return None
        candidate = candidate[start:end + 1]
    try:
        parsed = json.loads(candidate)
    except json.JSONDecodeError:
        return None
    return parsed if isinstance(parsed, Mapping) else None


class Judge:
    """Runs one judge model over stored answers, in its own process/session.

    Never shares a session with a participant: the judge must not be able to
    condition on having produced the answer it is grading.
    """

    def __init__(self, adapter: ParticipantAdapter, model: str, *,
                 max_output_tokens: int = 2000, effort: str | None = None) -> None:
        self.adapter = adapter
        self.model = model
        self.max_output_tokens = max_output_tokens
        self.effort = effort

    @property
    def provider(self) -> str:
        return getattr(self.adapter, "provider", "unknown")

    def _ask(self, system: str, payload: str) -> tuple[str, Mapping[str, Any] | None]:
        request = ModelRequest(
            model=self.model, system=system,
            messages=(Message(role="user", content=payload),),
            tools=(),  # a judge never gets tools
            max_output_tokens=self.max_output_tokens, effort=self.effort,
        )
        response = self.adapter.complete(request)
        return response.text, parse_json_object(response.text)

    def score_absolute(self, task: Any, answer: OpaqueAnswer) -> JudgeVerdict:
        payload = build_absolute_payload(task, answer)
        raw, parsed = self._ask(ABSOLUTE_JUDGE_PROMPT, payload)
        if parsed is None:
            return JudgeVerdict(
                payload={}, raw_text=raw, judge_provider=self.provider,
                judge_model=self.model, ok=False,
                error="judge did not return a parseable JSON object",
            )
        return JudgeVerdict(
            payload={
                "criteria": parsed.get("criteria") or {},
                "fabrication_flagged": bool(parsed.get("fabrication_flagged", False)),
                "judge_provider": self.provider,
                "judge_model": self.model,
            },
            raw_text=raw, judge_provider=self.provider, judge_model=self.model,
        )

    def compare_pairwise(self, task: Any, left: OpaqueAnswer,
                         right: OpaqueAnswer) -> JudgeVerdict:
        payload = build_pairwise_payload(task, left, right)
        raw, parsed = self._ask(PAIRWISE_JUDGE_PROMPT, payload)
        if parsed is None or parsed.get("winner") not in (
            "left", "right", "tie", "unjudgeable"
        ):
            return JudgeVerdict(
                payload={"winner": "unjudgeable"}, raw_text=raw,
                judge_provider=self.provider, judge_model=self.model, ok=False,
                error="judge did not return a valid winner",
            )
        return JudgeVerdict(
            payload={
                "winner": parsed["winner"],
                "reason": str(parsed.get("reason", ""))[:800],
                "left_answer_id": left.answer_id,
                "right_answer_id": right.answer_id,
                "judge_provider": self.provider,
                "judge_model": self.model,
            },
            raw_text=raw, judge_provider=self.provider, judge_model=self.model,
        )


def resolve_pairwise_winner(verdict: JudgeVerdict, *, left_condition: str,
                            right_condition: str) -> str | None:
    """Map a blinded verdict back to conditions — only after it is stored."""
    winner = (verdict.payload or {}).get("winner")
    if winner == "left":
        return left_condition
    if winner == "right":
        return right_condition
    if winner == "tie":
        return "tie"
    return None


def assert_judge_family_separation(participant_provider: str, judge_provider: str,
                                   *, allow_same: bool = False) -> None:
    """Refuse a plan that grades a model with its own family, unless overridden."""
    if participant_provider == judge_provider and not allow_same:
        raise UsageError(
            f"judge provider {judge_provider!r} is the same family as the "
            f"participant. Cross-family judging is the default because a model "
            "family scoring its own output is a known bias. Set "
            "judge.allow_same_family=true in the plan to override, and expect "
            "to justify it in the report."
        )
