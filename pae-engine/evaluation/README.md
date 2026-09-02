# pae-eval — the PAE independent evaluation harness

Developer tooling. Not part of the installed Engine, not reachable from `pae`,
and not shipped in any Engine artifact.

**No independent benchmark exists yet, and no result in this repository says
anything about whether PAE improves task quality.** This directory is the
machinery that could eventually answer that question. It has never been run
against a sealed benchmark.

---

## Why the existing numbers are not evaluation

The repository already contains material that looks like evaluation and is not:

| Artifact | What it actually is |
|---|---|
| `pae-engine/tests/data/search_routing_regression.v1.json` (120 cases) | A Phase 4 **tuning** set. The router's coverage and margin thresholds were fitted on it. |
| `FLOORS` in `test_search_regression.py` | Conservative regression guards set *below* the measured values, so an ordinary corpus edit does not fail the build. Not measurements. |
| `meta/ROUTING_REFERENCE.md` phrase mappings | Documentation labels. Many share vocabulary with their target's title, which flatters any lexical ranker. |
| Phase 5 packing diagnostics | Design-time instrumentation. |
| Phase 6 MCP tests | Correctness tests for an adapter. |
| `tests/prompting-technique-comparison/` | Single-run, unblinded, self-scored prompt experiments. |

They may be used to test *this harness*. None of them may support a public
quality claim. A benchmark that grades a system on the data used to design it
measures memory, not capability.

## The three layers

**Layer A — retrieval and routing.** Machine-scorable against acceptable
resource UIDs, scopes, kinds and route statuses. No model calls, so it costs
nothing and can be re-run on every Engine change forever.

**Layer B — context-packing ablations.** Development-set only. Its question is
mostly answered by Condition C below, which shares the same infrastructure.

**Layer C — end-to-end agent tasks.** The evidence that matters for "does this
help an agent do the work?"

## The four conditions

| | Context | Tools | PAE used |
|---|---|---|---|
| **A** | none | none | no |
| **B** | none | `repo_search`, `repo_list`, `repo_read` (ripgrep-backed) | no |
| **C** | canonical `ContextBundle` Markdown, injected | none | route + compile, outside the model |
| **D** | none | the four Phase 6 MCP tools | the whole product |

**D vs B is the primary comparison.** A vs D is close to a tautology on a
corpus-specific benchmark and must never be the headline: it mostly establishes
that the tasks are about this corpus.

Condition C is the *second cheapest* arm — one call, no tool loop — so it is
kept rather than cut. It is the only thing that separates "the bundle is good"
from "the agent drove the tools well".

## Fairness, and why the baseline is not a strawman

Condition B gets ripgrep, because that is what a real coding agent has. It is
explicitly **not** given a hidden semantic index or a generic BM25 ranker: the
moment we build retrieval for the baseline, the comparison stops being "PAE vs
generic access" and becomes "PAE vs our BM25".

Every condition shares one base system prompt, one turn budget, one output
limit and one timeout. Conditions with tools get one extra generic paragraph
about tool use, rendered identically for B and D. `assert_prompt_fairness`
enforces this, because a baseline quietly given a worse deal produces a win
that means nothing.

## Benchmark isolation

The sealed benchmark lives **outside** the participant checkout, in a separate
repository (`pae-benchmark`, not created by this phase). At run time it is
cloned to a path the participant cannot address.

Containment is by construction, not by denylist. The raw-repo tools are rooted
at the participant snapshot and resolve every path against that root; a
denylist is a list of the attacks someone thought of, and the gold labels are
exactly what an unlucky glob would reach.

### The participant snapshot

Once `pae-engine/evaluation/` is committed, pointing Condition B at the
developer checkout would let it read the condition definitions, the participant
prompt and the judge logic. So a run never binds to the working tree. It binds
to a snapshot extracted from **Git objects** at an explicit commit, with the
evaluation tree excluded:

```bash
python -m pae_eval snapshot --repo . --dest /tmp/snap --require-clean
```

Reading from Git objects means an uncommitted file cannot leak in, the bytes
are exactly what the commit says, and the result is reproducible from
`(commit, exclusions)` alone. B, C and D all bind to the same snapshot — if
they did not, the comparison would be measuring different corpora.

## Commands

```bash
python -m pae_eval validate-benchmark --benchmark-root <root> --repo <repo>
python -m pae_eval plan --benchmark-root <root> --repo <repo> --out plan.json
python -m pae_eval plan --check --plan plan.json
python -m pae_eval run  --benchmark-root <root> --repo <repo> --output-dir <out>
python -m pae_eval run  --execute ... --max-cost-usd 25 --max-trials 800
python -m pae_eval judge   --output-dir <out> --benchmark-root <root>
python -m pae_eval layer-a --benchmark-root <root> --snapshot <snap>
python -m pae_eval analyze --output-dir <out>
python -m pae_eval report  --output-dir <out> --benchmark-root <root>

python -m pae_eval prepare-authoring --repo <repo> --out-dir <private> --commit <sha>
python -m pae_eval audit-author-packet --author-root <dir> --map <map.json>
python -m pae_eval review-candidates --snapshot <snap> --repo <repo> --query "..."
python -m pae_eval check-composition --benchmark-root <root> --repo <repo>
```

### Cost guard

`run` **dry-runs by default** and makes zero provider calls; it needs no API
key. `--execute` requires both `--max-cost-usd` and `--max-trials` with
explicit positive values. There is no default ceiling, because a default
ceiling is a number nobody chose.

The guard prices a conservative worst case *before* each request and stops
rather than crossing the ceiling. Discovering an overage from the invoice is
not a cost guard.

### Secrets

Environment variables only. Never a CLI argument, a config file, a plan or a
trial record. Everything written to disk passes through `redaction.py`, and the
redaction tests plant recognizable fake secrets in the environment, in provider
exceptions, in raw response fixtures and in HTTP-style headers, then prove none
survives.

## The authoring firewall

`src/pae_eval/authoring/` prepares the conditions under which someone *else*
can write the sealed benchmark. It authors nothing.

The problem it solves is that a benchmark written by the system under test
measures the system's memory of itself, and a label assigned by asking `pae
route` grades PAE against its own output — a result that is unfalsifiable and
looks exactly like a good one.

So three roles, three actors:

| | Sees | Produces |
|---|---|---|
| **Author** | sanitized operational text under opaque packet IDs | task text |
| **Reviewer** | tasks, the packet→target map, raw non-PAE discovery | labels |
| **Maintainer** | everything | adjudications, freeze |

`prepare-authoring` draws 45 masked targets deterministically —
`SHA256(seed ‖ uid)` ordering, seed from the PAE commit, no RNG anywhere — then
strips identity from their bodies while preserving every operational
instruction and every safety guard verbatim, writes an author export and a
reviewer-private export that share no path and no bytes, and refuses to ship if
the audit finds a single UID, public ID, source path, ordered title, mapping
file, gold label or PAE retrieval output in the author tree.

Scattered title-token overlap is measured and reported rather than gated: a
packet about medication review contains the words "medication" and "review",
and a disjointness gate there would be satisfiable only by destroying the
content the author has to write about.

`review-candidates` is the reviewer's discovery tool: ripgrep, token-hit
aggregation, and the Registry used only to map a path to an identity. It
imports no PAE retrieval module, and `test_authoring_candidates` proves that
over the parsed AST and again over the transitive import closure rather than
asserting it in a comment. Its ordering is labelled as raw hit aggregation on
every record, and the reviewer always has *none of these* and *search further*.

**The method is public; the answer key is not.** The code and its tests live
here. The 45 UIDs, the packets and the mapping live only in the private
benchmark repository.

See [ADR-0041](../../meta/adr/0041-author-reviewer-separation.md), including
why the author manifest carries a commitment to the selection seed instead of
the seed itself.

## Statistics

- **Unit of analysis is the task.** Repeats aggregate to one value per
  task-condition before anything statistical happens. Treating repeats as
  independent observations multiplies *n* by the repeat count and shrinks every
  interval — the easiest way to manufacture significance.
- **Primary:** task pass rate, D vs B, paired. Exact McNemar plus a paired
  percentile bootstrap CI. The interval is the headline; the p-value is
  secondary.
- **Repeat handling:** with two repeats a majority vote can tie, and inventing
  a tie rule after seeing data is exactly the freedom pre-registration removes.
  The example plan uses `first_repeat_confirmatory` — repeat 0 is the
  confirmatory endpoint, repeat 1 is pre-planned variance/sensitivity. Both are
  run and reported.
- **Secondary:** continuous rubric score (bootstrap + Wilcoxon), Layer A
  metrics, safety, efficiency. Holm–Bonferroni across the secondary family; the
  single pre-declared primary is **not** corrected.
- **Wilcoxon comes from SciPy** under the `analysis` extra or not at all. A
  hand-rolled version that mishandles ties and zeros produces a plausible wrong
  number, which is worse than an honest "not available".
- **Efficiency is gated.** A token-reduction claim is reported only when the
  quality non-inferiority gate passes first. Cheaper-but-worse is not an
  efficiency result.

## Judging

Deterministic rules first — required strings, JSON validity, section presence,
format gates, absolute-path leakage, tool-use constraints. Those carry the
majority of rubric weight, cost nothing and cannot drift.

An LLM judge scores only the genuinely qualitative residue. It sees the task,
the deliverable spec, the rubric, and answers under opaque IDs. It does **not**
see the condition, the participant model, tool traces, PAE identifiers, bundle
hashes or the repository — enforced when the payload is built, not requested in
the prompt.

**A judge can never rescue a deterministic required failure.** If the required
elements are absent, the task failed, however impressed the judge was.

Cross-family judging is the default and a same-family plan fails validation
unless `judge.allow_same_family` is set explicitly.

No chain-of-thought is requested, and no field exists to store one.

## Reporting

The report generator reads the analysis object and nothing else. It contains no
canned sentence asserting that PAE improved, won or saved money — every
comparative word comes from `_direction()`, which reads the confidence
interval. If the interval straddles zero, the only sentence available says so.

Null and negative results get the same template, section order and prominence
as a positive one, and there are tests that render all three and assert the
wording follows the numbers.

A claim-ready sentence is emitted **only** for a sealed run whose interval
excludes zero, and it always names benchmark, task count, commit, model,
conditions, effect, CI and repeat design. There is no generic
"PAE accuracy = X" output.

## Reproducibility

Every run emits `run-manifest.json`, `trial-schedule.json` and
`participant-snapshot.json`, each with a sidecar digest. The schedule is
materialized and hashed **before the first paid request**, and conditions are
interleaved rather than blocked so provider drift cannot line up with the
primary contrast.

Trials are append-only, one line per attempt. Resume skips only exact completed
trial IDs, and only when the plan, benchmark and snapshot hashes still match —
a different configuration is a different experiment.

**Reproducibility here means the inputs and procedure are frozen, not that
outputs repeat.** The current frontier models accept neither a seed nor a
temperature, so run-to-run variation cannot be eliminated, only measured. Any
report that implies otherwise is wrong.

## Installation

```bash
pip install -e path/to/repo/pae-engine
pip install -e "path/to/repo/pae-engine/evaluation[mcp,anthropic,openai,analysis]"
```

The Engine is installed from the local checkout — the distribution is not
published, so the harness deliberately does **not** declare a PyPI dependency
on it. The harness records the imported Engine version at run time.

The base install has no dependencies at all: `plan`, `validate-benchmark`,
fake-provider runs, statistics and reporting all work with nothing installed.

## Provider SDK verification

Adapters were written against these sources on **2026-09-02**. Re-verify before
a sealed run; provider APIs, model identifiers and prices all drift, and the
model IDs in the example plan are placeholders rather than choices.

| What | Source | Verified |
|---|---|---|
| Anthropic models, context, pricing | `platform.claude.com/docs/en/about-claude/models/overview` | 2026-09-02 |
| Anthropic Messages API, tool use, usage fields | Anthropic API reference / SDK | 2026-09-02 |
| OpenAI Responses API request/response shape | `developers.openai.com/api/docs/api-reference/responses/create` | 2026-09-02 |
| OpenAI pricing | `developers.openai.com/api/docs/pricing` | 2026-09-02 |
| SDK version floors (`anthropic` 1.3, `openai` 3.7, `mcp` 2.1.1, `scipy` 1.18) | PyPI | 2026-09-02 |

Two current-API facts shape the adapters:

- `temperature`, `top_p` and `top_k` are **removed** on current frontier models
  and return 400. Adapters forward only what the plan set explicitly and never
  supply a sampling default of their own.
- There is no seed parameter. Determinism is unavailable, which is why repeats
  exist and why the limitations section says so in every report.

## CI

The `Evaluation` workflow runs on every PR with **no provider credentials and
no paid requests**: unit tests, fake-provider end-to-end runs (known-positive
and known-negative), fixture benchmark validation, condition-isolation tests,
snapshot tests, raw-repo path security, real-ripgrep integration, statistics
against known answers, report fixtures, redaction, Engine package-contamination
and the architecture import-direction check.

A focused Windows lane covers the developer diagnostics and the constrained-
encoding failure path, because Phase 7A found defects that a Linux-only CI
could not see.

The sealed benchmark never runs on a pull request.

## Publication rules

A public claim must name the benchmark and version, the task count, the PAE
commit, the model, the conditions, the effect and its uncertainty. Forbidden:
"PAE makes AI 20% smarter", "PAE has 90% accuracy", "proven to improve every
model", and any number quoted from the Phase 4/5 internal sets.

Nothing in this directory has produced a publishable number.

## Fixtures

`tests/fixtures/mini-benchmark/` holds six synthetic tasks that exist only to
exercise the harness in CI. Every fixture artifact carries:

```
SYNTHETIC TEST FIXTURE — NOT INDEPENDENT BENCHMARK EVIDENCE
```

They were not independently authored, were not independently reviewed, and must
never appear in a report headline.

## Related decisions

- [ADR-0033](../../meta/adr/0033-evaluation-runtime-separate-from-engine.md) — evaluation runtime is separate from the Engine runtime
- [ADR-0034](../../meta/adr/0034-independent-benchmark-separate-from-tuning-data.md) — the independent benchmark is separate from tuning data
- [ADR-0035](../../meta/adr/0035-four-condition-comparison.md) — four conditions, D vs B primary
- [ADR-0036](../../meta/adr/0036-raw-repository-baseline.md) — ripgrep + list + read, no shell, no BM25
- [ADR-0037](../../meta/adr/0037-benchmark-leakage-isolation.md) — external benchmark and participant snapshot
- [ADR-0038](../../meta/adr/0038-frozen-plan-and-append-only-evidence.md) — frozen plan, append-only evidence
- [ADR-0039](../../meta/adr/0039-statistical-primary-endpoint.md) — paired pass rate, McNemar, confirmatory repeat
- [ADR-0040](../../meta/adr/0040-public-performance-claim-governance.md) — public claim governance
- [ADR-0041](../../meta/adr/0041-author-reviewer-separation.md) — author/reviewer separation and the masked authoring firewall
