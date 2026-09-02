"""Typed failures.

Two rules shape this hierarchy.

First, the harness must distinguish *infrastructure* failures (retryable; the
request never produced a model outcome) from *model behaviour* (not retryable;
the behaviour is the measurement). Retrying a refusal until the model complies
would silently select for agreeable samples and bias the arm, so the type
system carries that distinction rather than leaving it to a string check.

Second, anything that could let a condition see what it must not — the
benchmark, another condition's output, a gold label — raises
``IsolationError``. Isolation failures are never warnings and never recoverable;
they fail closed before any paid request.
"""

from __future__ import annotations


class PaeEvalError(Exception):
    """Base for every harness error."""


class UsageError(PaeEvalError):
    """The operator asked for something incoherent. Exit code 2."""


class ValidationError(PaeEvalError):
    """A benchmark, plan or record failed schema or semantic validation."""

    def __init__(self, message: str, problems: list[str] | None = None) -> None:
        super().__init__(message)
        self.problems = problems or []

    def __str__(self) -> str:
        base = super().__str__()
        if not self.problems:
            return base
        shown = "\n".join(f"  - {p}" for p in self.problems[:25])
        more = (
            f"\n  ... and {len(self.problems) - 25} more"
            if len(self.problems) > 25
            else ""
        )
        return f"{base}\n{shown}{more}"


class IsolationError(PaeEvalError):
    """A condition could observe something it must not.

    Always fatal. There is no mode in which the right response to "the raw-repo
    agent can reach the gold labels" is to continue and note it.
    """


class FrozenPlanError(PaeEvalError):
    """The world no longer matches the frozen plan."""


class CostCeilingError(PaeEvalError):
    """The next request could cross the configured ceiling.

    Raised *before* the request is sent. Discovering an overage from a bill is
    not a cost guard.
    """


class ProviderNotAvailable(PaeEvalError):
    """A provider adapter was requested but its SDK is not installed."""


# --------------------------------------------------------------------------
# trial-level outcomes
# --------------------------------------------------------------------------


class TrialFailure(PaeEvalError):
    """Base for a failure attributable to one trial attempt."""

    #: Recorded verbatim in the trial record's ``error_class``.
    error_class = "unknown"
    #: Whether a bounded retry is legitimate.
    retryable = False


class InfrastructureFailure(TrialFailure):
    """The request never reached a model outcome. Bounded retries apply."""

    retryable = True

    def __init__(self, message: str, error_class: str = "provider_transport_error",
                 retry_after_s: float | None = None) -> None:
        super().__init__(message)
        self.error_class = error_class
        self.retry_after_s = retry_after_s


class ModelBehaviourFailure(TrialFailure):
    """The model produced an outcome, and the outcome is the datum.

    Never retried. A refusal, a tool loop and a behavioural timeout are results,
    not accidents.
    """

    retryable = False

    def __init__(self, message: str, error_class: str = "empty_answer") -> None:
        super().__init__(message)
        self.error_class = error_class
