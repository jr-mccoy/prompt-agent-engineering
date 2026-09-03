# ADR-0042 — Prompt caching on the paid path, and the token accounting it requires

## Status

Accepted. Implemented pre-freeze, before any independent author received a
packet and before any paid provider call. No sealed run has happened.

## Context

The sealed evaluation is 150 tasks × 2 model families × 6 trials (A×1, B×2,
C×1, D×2) = **1,800 participant trials**, and two of the four conditions are
agentic tool loops with a 40-turn budget. A tool loop resends its transcript
every turn, so input cost grows with the square of the turn count: at *n* turns
a per-turn delta of *E* tokens is billed *E·n(n+1)/2* times over.

Priced with no caching, that put the run at roughly **$1,088** if the loops
average 10 turns and **$11,239** at the configured 40-turn ceiling. Against a
$2,500 budget only 17 turns fit. That framed the decision as a choice between
two bad options:

1. **Cut `max_tool_turns`** so the run fits. This is the option that damages
   the result. Condition B is the raw-repository baseline — ripgrep, list, read
   — and it needs more turns than Condition D precisely *because* it has no
   compiled bundle to work from. Capping turns to fit a budget handicaps the
   baseline that PAE is being compared against, and a favourable D-vs-B result
   obtained that way measures the cap, not the product.
2. **Ask for more money**, without having first done the obvious thing.

The obvious thing had not been done. The Anthropic adapter never sent
`cache_control`, so every resend was billed at the full input rate even though
the resent prefix — system prompt, tool catalog, prior turns — is exactly what
prompt caching exists for.

Investigating that surfaced a second, quieter problem. `cost_usd` computed
`uncached = input_tokens - cache_read_tokens`, which assumed the provider's
`input_tokens` *includes* the cached part. Anthropic's does not: it reports a
partition, where `input_tokens + cache_read_input_tokens +
cache_creation_input_tokens` is the total. OpenAI's does. So the same line was
wrong for one provider in one direction and right for the other by accident,
and neither error was visible while caching was off and both counters were
always zero.

And the OpenAI counters were always zero for a third reason: the adapter read
`cached_input_tokens` off `usage`, but the Responses API nests them under
`usage.input_tokens_details` as `cached_tokens` and `cache_write_tokens`.
Reading a field that does not exist returns `None` silently — no error, no
cache ever recorded, every cached token billed at the full rate.

## Decision

**Enable prompt caching by default, and fix the accounting it depends on.**

*Caching.* The Anthropic adapter uses the documented combination of both
mechanisms, occupying three of the four available breakpoint slots: explicit
`cache_control` on the last tool definition (one breakpoint caches the whole
catalog, since a cached prefix ends at the block the marker sits on), explicit
`cache_control` on the system prompt, and the **top-level** `cache_control`
field for the rolling conversation breakpoint. The top-level form is automatic
caching: the API places the remaining breakpoint on the last cacheable block
and walks it forward as the conversation grows. Letting the API track that is
both the recommended approach and one fewer thing for the adapter to get wrong;
an earlier draft hand-rolled it and would have competed for the same slot.

The 5-minute TTL is used. Writes cost 1.25× base input rather than the 2× the
1-hour window charges, and a run working through trials back to back does not
need the longer window.

OpenAI needs no opt-in — caching is that API's default, and
`prompt_cache_options.mode` is left unset so the run gets the default rather
than a mode the harness chose.

*Accounting.* `Usage` now specifies that its three input buckets are
**disjoint**: `input_tokens` counts only tokens billed at the full rate. Each
adapter normalizes to that convention — Anthropic passes through, OpenAI reads
the nested details and subtracts them out — and `cost_usd` simply adds the
buckets at their own rates. `ModelPrice` gains `cache_write_per_million`,
because a cache write costs *more* than plain input, not less, and billing it
at 1.0× understated an Anthropic run by the 25% premium.

*Estimation.* `estimate_trial_cost` gains `cache_reads`, defaulting to
**False**. The split it applies is derived rather than guessed: over *n* turns
the loop writes *E·n* and reads *E·n(n-1)/2*, the same total volume at two
rates. `--dry-run` reports both figures.

## Why caching is a default and not an experimental decision

Every other knob on the paid path is a recorded decision because it could move
the result. This one cannot. `cache_control` is request metadata: the prompt is
byte-identical with and without it, so the token sequence the model sees and
the distribution it samples from are unchanged.

That claim is asserted rather than assumed. `test_pricing_and_caching.py` sends
the same request with caching on and off and diffs the payloads, requiring the
messages, model, output cap, system text and tool list to be identical and only
the metadata to differ. It is recorded in the plan hash
(`limits.prompt_caching`) and in the run manifest (`describe()`) regardless, so
a reader can always tell whether the cache counters in the trial records were
even requested.

### One place where it *would* have moved a reported number

The claim above is about the prompt. It was not automatically true of the
*analysis*, and checking it found a defect.

`total_tokens` is a reported secondary endpoint, and the efficiency claim is a
function of it for the two conditions in the primary comparison. Both
`Usage.total_tokens` and `efficiency_by_condition` computed it as
`input_tokens + output_tokens`. Once the buckets are disjoint, that omits every
cached token — so identical work would report fewer tokens the moment caching
was switched on.

Worse, it would omit a *different* share per condition. Condition B's long
agentic loops cache their transcript heavily; Condition D's shorter ones cache
less. So the distortion is not even a constant factor cancelling out of a
ratio: it is enough to move, and conceivably to reverse the sign of, the
efficiency claim — from a change that is supposed to be billing-only.

Both now sum all four buckets. The endpoint measures work; `cost_usd` is the
only place the discount appears. `efficiency_by_condition` additionally reports
`cached_input_tokens` and `cache_write_tokens` separately, so a reader can see
how much was cached instead of inferring it. Caching-invariance is asserted
directly: the same 101,000 tokens of work, reported once as uncached and once
as mostly cache reads, must produce the same total and a lower cost.

This is the argument for enabling caching *before* freezing rather than after.
The defect was in analysis code that had been correct for as long as the cache
counters were always zero.

## Why the cost guard still assumes no cache hits

`estimate_trial_cost` defaults to the uncached figure, and the ceiling is
checked against that. A cache entry can expire between turns — the TTL is five
minutes and nothing guarantees a loop stays inside it — so an estimate that
assumes hits would let a run walk past the limit it was given. The cached
figure is for *sizing* a budget; the uncached figure is for *enforcing* one.
`--dry-run` prints both and labels which is which.

## Consequences

Measured on the 30-task development schedule, the estimate falls from
**$217.68 to $100.50** — 54%, on identical token volume. Scaled to the 1,800
sealed trials:

| Avg. B/D tool turns | Uncached | Cached | Saving |
|---|---|---|---|
| 10 | $1,088 | $502 | 54% |
| 15 | $1,993 | $685 | 66% |
| 20 | $3,212 | $900 | 72% |
| 30 | $6,595 | $1,423 | 78% |
| 40 (the configured ceiling) | $11,239 | $2,072 | 82% |

The saving grows with turn count, because the resent prefix is what caching
addresses and the prefix is what grows.

**`max_tool_turns` therefore stays at 40.** That is the consequence that
matters. Caching buys the entire configured turn budget for about $2,072, so
the run no longer has to choose between fitting a budget and letting the
raw-repository baseline work as hard as it needs to. Under the old accounting
only 17 turns fit inside $2,500 and Condition B would have been truncated to
afford Condition D. The number was not changed from taste in either direction:
it stays where it was because the measurement stopped arguing for moving it.

Two costs are accepted. Single-call conditions pay one cache write at 1.25× on
the first trial and read the system prompt back at 0.1× on every trial after
it, which is why the top-level breakpoint is applied only once a conversation
exists. And a prefix below the model's minimum cacheable length — 512 tokens on
Claude Opus 5 — is silently not cached; that is a no-op, not an error, and no
write is billed for it.

Prices are pinned in a dated snapshot, not fetched at run time, and the shipped
example is still labelled `EXAMPLE ONLY`. A sealed run must re-retrieve and
re-pin, because cache rates drift with base rates.

## Alternatives rejected

**Lower `max_tool_turns` instead.** Rejected above: it handicaps the baseline
and makes the primary comparison measure the cap.

**Use the 1-hour TTL.** Doubles the write rate to buy a window a back-to-back
run does not need. Available to a plan that wants it.

**Batch API (50% off both directions).** Rejected: the conditions are
interactive tool loops, and the harness has no batch path.

**Model caching in the cost guard.** Rejected: see above. A ceiling that
assumes cache hits is not a ceiling.

**Leave the accounting alone and just enable caching.** This was the tempting
one, and it is the worst option. With the buckets mis-specified, enabling
caching would have made the run *look* cheaper than it was — every cached token
double-counted or dropped depending on the provider — and the error would have
appeared only as a discrepancy against the invoice, after the money was spent.

## Related

- [ADR-0035](0035-four-condition-comparison.md) — the four conditions, and why D vs B is primary
- [ADR-0036](0036-raw-repository-baseline.md) — why Condition B needs its turns
- [ADR-0038](0038-frozen-plan-and-append-only-evidence.md) — the plan hash that records this
- `pae-engine/evaluation/README.md` → "Provider SDK verification" → "Prompt caching"
