# ADR-0041 — Author/reviewer separation, and the masked authoring firewall

## Status

Accepted. Implemented in Phase 8A. The sealed benchmark it prepares for has not
been authored, labelled or frozen.

## Context

ADR-0034 established that the independent benchmark must be separate from the
Phase 4 tuning data. That removes one contamination route and leaves a larger
one open: **who writes the tasks, and what did they know when they wrote them?**

Three failures are available, and each produces numbers that look entirely
normal:

**The system writes its own exam.** If Claude Code authors the sealed tasks
with the repository open, it writes requests it already knows the corpus
answers well. The benchmark then measures how faithfully PAE remembers its own
design.

**The labeller asks the system under test.** If the reviewer decides what
*should* have answered a task by running `pae route`, the gold label *is* PAE's
output. Accuracy against it approaches 100% by construction, the result is
unfalsifiable, and it is indistinguishable from a genuinely good result.

**One actor does both.** A session that wrote a task already knows its intended
answer. Its label records that intent, not an independent judgement — and this
holds even when the "two roles" are two turns of the same conversation.

A fourth problem is subtler. Tasks must be *about* the corpus's subject matter
or they measure nothing, but an author who can see resource titles, IDs and
paths writes tasks whose vocabulary matches those titles, flattering any
lexical ranker. The author needs the *work* without the *identity*.

## Decision

**Three roles, three actors, no overlap.**

| Role | Sees | Produces |
|---|---|---|
| Author | sanitized operational text under opaque packet IDs | task text |
| Reviewer | tasks, packet→target map, raw non-PAE discovery | labels |
| Maintainer | everything | adjudications, freeze |

Author and reviewer are different sessions. AI actors are acceptable — no
second human is assumed — under the documented fallback *independent AI author
→ independent AI reviewer → maintainer adjudication*, with provenance recorded
honestly on every task. An AI-authored set described as human-authored
invalidates every number computed from it.

**Masked targets are drawn deterministically.** Order is
`SHA256(seed ‖ uid)` ascending, seed is `SHA256("pae-independent-benchmark-
masked-targets-v1\n" + commit)`. There is no random number generator anywhere
in the path, so the selection is a pure function of the commit and "we
resampled until the mix looked right" is not a statement anyone can make about
it. A target is skipped only for mechanical ineligibility — dead body, wrong
serving policy, reserved by the development set — the replacement is the next
candidate in the same order, and every skip is recorded with its reason.

**Sanitization removes identity and preserves operation.** Frontmatter, the
title heading, UIDs, public IDs, repository paths and related-resource lists
go. Objectives, procedures, examples, constraints and every safety guard stay,
byte for byte. Nothing is summarized: a paraphrase would put the masking tool's
words in front of the author instead of the corpus's, and the tasks would then
be about the paraphrase.

**The export is gated by an audit that fails closed.** UID, public ID, source
path, ordered title sequence, reviewer mapping, gold labels and PAE retrieval
output must each be exactly zero. Scattered title-token overlap is *measured
and reported, not gated* — a body about medication review contains the words
"medication" and "review", and a zero-overlap gate would be satisfiable only by
destroying the content the author is supposed to write about.

**Reviewer discovery is ripgrep and nothing else.** Token-hit aggregation over
the participant snapshot, with the Registry consulted only to turn a discovered
path into a stable identity. `pae_engine.search`, `.routing`, `.context` and
`.mcp` are not imported and `SearchEngine`, `Router` and `ContextCompiler` are
not referenced; a test proves this over the parsed AST and again over the
transitive import closure. Candidate order is labelled as raw hit aggregation
on every record, and the reviewer always has *none of these* and *search
further* — a forced choice from a list that happened to miss the right answer
is how a benchmark acquires wrong labels.

## Consequences

**The author manifest carries a seed commitment, not the seed.** Spec §12 lists
the selection seed among the author manifest's fields. Seed + repository +
published algorithm reproduces the whole mapping, so writing it there would
hand the author the answer key one command away. The author manifest records
`SHA256(seed)`; the reviewer manifest records the seed. Anyone holding both can
verify the match, so provenance is intact and only invertibility is removed.
This is a deliberate, documented deviation and the only one.

**The recommended kind allocation was unreachable and was adjusted.** Phase 8A
recommends `skill 12 / agent 8 / command 8 / persona 5 / prompt 12` alongside a
hard requirement of exactly 18 safety-gated packets. In this corpus
`serving_policy == "safety_gated"` occurs on prompts and nothing else — 1319
prompts, zero skills, agents, commands or personas — so 18 safety-gated packets
force at least 18 prompts. The class counts are requirements and the allocation
is a recommendation, so prompts are held at the forced minimum of 18 and the
remaining 27 slots keep the recommendation's 12:8:8:5 ratio (10:7:6:4). The
selector refuses a configuration where the prompt quota and the safety-gated
class quota disagree, rather than silently producing a set that satisfies
neither.

**Method is public, key is private.** The selection, masking, audit and
discovery code lives in this repository with its tests; the 45 UIDs, the
packets and the mapping live only in the private benchmark repository. The
procedure should be auditable by anyone. The answer key should not be guessable
by the author.

**Development and sealed sets cannot overlap.** Every resource the development
benchmark uses is recorded by canonical cluster as well as UID, and the sealed
draw excludes those clusters — so a *copy* of a development target cannot be
drawn either. Generic rubric structure may be shared; a rubric is a grading
form, not content.

**Nothing here has measured anything.** This ADR describes machinery for
producing a trustworthy benchmark. No sealed task has been authored, no label
assigned, no paid provider call made.

## Related

- [ADR-0033](0033-evaluation-runtime-separate-from-engine.md) — evaluation runtime separate from the Engine
- [ADR-0034](0034-independent-benchmark-separate-from-tuning-data.md) — benchmark separate from tuning data
- [ADR-0037](0037-benchmark-leakage-isolation.md) — external benchmark and participant snapshot
- [ADR-0040](0040-public-performance-claim-governance.md) — public claim governance
