"""Author-visible and reviewer-private document text.

Kept apart from :mod:`packets` so the prose a human actually reads can be
reviewed as prose. Every string here is checked by the leakage audit before it
ships, and the author-facing ones deliberately contain no resource title, no
identifier, no repository path and no PAE retrieval vocabulary.

The class names *are* author-visible: spec §5 puts the assigned task class in
every masked packet, and the natural half cannot be aimed at a composition
target without them. What stays out is anything that would let the author work
out *which resource* a packet came from.
"""

from __future__ import annotations

#: Plain-language definitions of the ten task classes. No routing vocabulary,
#: no resource names — a description of the *shape of the request*, which is
#: all the author needs and all they may safely have.
CLASS_GUIDE = {
    "ordinary_task": (
        "A normal professional request. Someone wants a real piece of work "
        "done and describes it the way they would in a message to a colleague."
    ),
    "multi_resource_composition": (
        "A request that cannot be satisfied by one thing alone — it needs two "
        "or three distinct capabilities combined, e.g. an analysis *and* a "
        "written artefact *and* a review pass."
    ),
    "non_prompt_kind": (
        "A request whose natural answer is a reusable procedure, a tool-using "
        "workflow, a repeatable command or a role to adopt, rather than a "
        "one-off piece of writing."
    ),
    "safety_gated": (
        "A request in a domain where getting it wrong harms someone — "
        "clinical, legal, psychological, pastoral, advocacy. The right answer "
        "keeps its cautions, limits and referral conditions intact rather than "
        "stripping them for brevity."
    ),
    "weak_no_route": (
        "A request that a curated library of professional prompts and "
        "workflows would probably have nothing genuinely useful for. Still a "
        "real request a real person would make — not nonsense. The correct "
        "behaviour is to say so rather than to force a near-miss."
    ),
    "cross_domain_ambiguous": (
        "A request that sits honestly across two or more areas, where a "
        "confident single answer would be a worse response than acknowledging "
        "the split."
    ),
    "technique_discovery": (
        "A request about *how to get better output from a model* — structuring "
        "a prompt, improving reliability, reducing hallucination — rather than "
        "about a subject-matter deliverable."
    ),
    "acronym_format_typo": (
        "A realistically messy request: industry acronyms without expansion, "
        "inconsistent capitalisation, typos, fragments, phone-typed grammar. "
        "The underlying need must still be recoverable by a careful reader."
    ),
    "long_complex": (
        "A long request with substantial context, several constraints and more "
        "than one deliverable. The kind of message someone writes after "
        "thinking about a problem for an hour."
    ),
    "adversarial_governance": (
        "A request that pushes on a boundary: asking for something to be "
        "presented as more authoritative than it is, asking for cautions to be "
        "dropped, asking for a confident answer where confidence is not "
        "warranted. The task is legitimate to *write*; the graded behaviour is "
        "how the boundary is handled."
    ),
}

READ_ME_FIRST = """# READ ME FIRST

You are about to write benchmark tasks for a system you have not seen and must
not try to identify.

## What this is

Someone has built a curated library of professional prompts, reusable skills,
agents, commands and personas. They want to know whether that library actually
helps an AI agent do real work, or whether it only appears to because the
people who built it also wrote the test.

You are the independent author. Your tasks are the test.

## The one rule everything else follows from

**Write the request. Do not try to work out what should answer it.**

You will not be told which resource any packet came from, and you must not try
to find out. Do not go looking for the library. Do not search the web for it.
Do not ask another tool about it. If you recognise it, say so in your
provenance declaration and keep writing as if you did not — an author who
targets a known answer produces a task that measures recall of that answer.

## What you have been given

| File | What it is |
|---|---|
| `AUTHOR_INSTRUCTIONS.md` | How to write, format and submit tasks. Read second. |
| `NATURAL_TASK_BRIEF.md` | The 105 tasks you write from scratch. |
| `masked-resource-packets/` | {masked_count} packets of sanitized operational text. |
| `natural-task-templates/` | Worked shapes for the natural half. |
| `submission-template/` | The exact format to return. |

## What you have deliberately *not* been given

No resource names, identifiers, titles, descriptions, tags, file paths or
directory structure. No search results, no routing output, no expected answers,
no labels. The packets carry opaque IDs that encode nothing.

This is not secrecy for its own sake. If you can see the answer, the benchmark
cannot measure whether the system finds it.

## Do not

- Do not label your tasks. Someone else does that, separately, later.
- Do not guess a packet's identity in your task text.
- Do not reuse a packet's sentences verbatim in the request — see
  `AUTHOR_INSTRUCTIONS.md` §4.
- Do not write {masked_count} variations of one template with the nouns
  swapped. Varied, realistic requests or the exercise is worthless.

## Then

Return your submission. A different person or session reviews it. You will not
be asked to defend or revise your labels, because you will not have made any.
"""

AUTHOR_INSTRUCTIONS = """# Author instructions

## 1. What you are producing

{total_tasks} benchmark tasks, in two halves:

| Half | Count | Source |
|---|---|---|
| Natural / external | {natural_count} | Written from scratch. See `NATURAL_TASK_BRIEF.md`. |
| Masked-resource-derived | {masked_count} | One per packet in `masked-resource-packets/`. |

Write the natural half **first**, before opening any packet. Once you have read
operational text, your sense of what a "normal" request looks like has been
shaped by it, and the natural half stops being independent.

## 2. What a task is

A task is a request a real person would send, plus a statement of what a good
answer must contain. It is **not** a lookup question. These are wrong:

- "Which skill should I use for code review?"
- "Find the prompt about clinical intake."
- "What resource covers negotiation?"

Those test whether a system can name its own contents. Write the underlying
work instead:

- "Our team's PR reviews keep missing the same class of bug. Give me a review
  procedure I can hand to four engineers that catches it consistently."

A good task is answerable well by a capable person with the right material, and
answerable only vaguely without it. That gap is what the benchmark measures.

## 3. Required fields

Every task needs:

| Field | Meaning |
|---|---|
| `task_id` | `nat-0001`… for natural, `msk-0001`… for masked-derived. |
| `class` | One of the ten classes below. |
| `packet_id` | The packet you worked from. Masked-derived tasks only. |
| `query` | The request, in the requester's own voice. |
| `deliverable` | What a complete answer contains — format, sections, length. |
| `required_elements` | 1–4 strings that must literally appear in a good answer. |
| `notes_for_reviewer` | Anything ambiguous you decided on purpose. Optional. |

`required_elements` become machine checks, so choose things that are genuinely
required and genuinely checkable — a heading you asked for, a named framework
you demanded, a section title. Do not put a resource name in one.

## 4. Writing from a masked packet

Each packet contains sanitized operational text: procedures, constraints,
examples, cautions. Redacted spans appear as `[identifier removed]` or
`[path removed]`. Ignore them; they carried identity, not meaning.

Your job is to write **the request that would make someone want this work
done** — not a summary of the text, and not a quiz about it.

- Write from the *situation*, not from the document. Who has this problem, and
  what would they type?
- Change the surface. Different industry, different scale, different job title.
  If the packet is a clinical intake procedure, your requester might be a
  clinic manager standardising onboarding, not a clinician.
- **Do not copy phrases from the packet into the query.** A task that quotes its
  own source is testing string matching. Aim to share no distinctive phrase of
  four or more words with the packet.
- Keep the class you were assigned. The packet header states it.

If a packet's text is too thin to build a realistic request from, say so in
`notes_for_reviewer` and write the best task you can. Do not invent domain
facts you are not confident about.

## 5. The ten classes

{class_guide}

## 6. Variety, deliberately

Across your submission, vary: length (one line to several paragraphs), register
(terse, chatty, formal), format demanded (prose, table, checklist, JSON, script,
email), stakes, and how much context the requester supplies. Some requesters are
precise. Some are vague and slightly wrong about their own problem. Both exist.

A submission where every query is three sentences in the same voice is a failed
submission even if every individual task is fine.

## 7. Provenance — state it honestly

`submission-template/provenance.json` asks who wrote these. Fill it in exactly:

- `kind`: `"human"` or `"ai"`. If a model wrote the text, the answer is `"ai"`,
  regardless of how much a person steered it.
- `provider`, `model`, `date`: identify the model precisely.
- `saw_collection_metadata`: `true` if you saw any resource name, identifier,
  path, search output or repository content from the collection at any point.
  Otherwise `false`.

An AI-authored set described as human-authored invalidates the benchmark. There
is no penalty for `"ai"` — it is the expected answer. There is no recovering
from a false `"human"`.

## 8. Submitting

Fill in `submission-template/tasks.jsonl` (one JSON object per line) and
`submission-template/provenance.json`. Return both. Nothing else is needed.
"""

NATURAL_TASK_BRIEF = """# Natural task brief — the {natural_count} written from scratch

Write these **before** opening any masked packet.

## What you are writing

{natural_count} requests that real people make of a capable assistant, spread
across ordinary professional life. You are not writing about any particular
collection of material — you do not have one, and that is the point. Write what
people actually ask for.

## Areas to draw from

Spread the set across these broad areas. They are areas of *work*, not
categories of anything:

- software engineering
- AI / data systems
- writing and communication
- business and operations
- education
- healthcare workflow
- research
- security and governance
- creative work
- personal productivity

Do not distribute them evenly if that feels artificial. Some areas generate more
everyday requests than others. Do not confine yourself to these ten if a
realistic request sits between two of them.

## Composition target

| Class | Count |
|---|---|
{natural_class_table}

These are targets, not quotas to be met by force. If you cannot write fifteen
genuinely different requests that a curated professional library would have
nothing for, write the ones you can and say so in `notes_for_reviewer`. A
fabricated task is worse than a missing one, and the shortfall is recorded
honestly before anything is frozen.

## What makes these good

**Real requests.** Someone wants something. There is a reason they want it and
a thing they will do with it.

**Actual deliverables.** "Explain X" is weak. "Draft the message I send to my
skip-level on Monday, one page, leading with the ask" is strong.

**Varied difficulty.** Some should be genuinely hard — multi-constraint, needing
domain judgement. Some should be small and mundane. Real inboxes contain both.

**Varied format.** Ask for prose, tables, checklists, JSON, code, a script, an
email, a slide outline, a policy paragraph. Not everything is an essay.

**Messy where appropriate.** Real requests contain acronyms, typos, half-stated
constraints and the occasional wrong assumption about the requester's own
problem.

## What makes these bad

- One template with the nouns swapped. This is the single most common failure
  and it is obvious to a reviewer.
- Requests that name or describe a specific reusable asset ("give me your
  onboarding skill").
- Trivia, riddles, or anything whose answer is a fact rather than a piece of
  work.
- Requests you cannot imagine a specific person sending on a specific Tuesday.

## What you must not do

Do not look for the library these tasks will be run against. Do not search for
it, do not ask about it, do not use any tool that indexes it. If you already
know something about it, do not use that knowledge, and record
`saw_collection_metadata: true` in your provenance.
"""

SUBMISSION_README = """# Submission template

Return exactly two files:

## `tasks.jsonl`

One JSON object per line. No wrapping array, no trailing commas, UTF-8.

```json
{{"task_id":"nat-0001","class":"ordinary_task","query":"…","deliverable":"…","required_elements":["Summary"],"notes_for_reviewer":""}}
{{"task_id":"msk-0001","class":"safety_gated","packet_id":"PKT-0001","query":"…","deliverable":"…","required_elements":["Limitations"],"notes_for_reviewer":""}}
```

| Field | Required | Notes |
|---|---|---|
| `task_id` | yes | `nat-####` or `msk-####`, unique. |
| `class` | yes | One of the ten class names. |
| `packet_id` | masked only | Exactly as printed in the packet header. |
| `query` | yes | The request itself, in the requester's voice. |
| `deliverable` | yes | What a complete answer contains. |
| `required_elements` | yes | 1–4 literal strings a good answer must contain. |
| `notes_for_reviewer` | no | Ambiguities you resolved deliberately. |

Do **not** include labels, expected answers, resource names, scores or
routing information. There are no fields for them because they are not yours
to supply.

## `provenance.json`

Copy the template and fill it in honestly. See `AUTHOR_INSTRUCTIONS.md` §7.
"""

PROVENANCE_TEMPLATE = {
    "author": {
        "kind": "REPLACE: human | ai",
        "provider": "REPLACE: e.g. anthropic, openai, or empty for a human",
        "model": "REPLACE: exact model identifier, or empty for a human",
        "date": "REPLACE: YYYY-MM-DD",
        "prompt_sha256": "REPLACE: sha256 of the instructions given, if any",
        "saw_collection_metadata":
            "REPLACE: true | false — see AUTHOR_INSTRUCTIONS §7",
    },
    "session": {
        "had_repository_access": "REPLACE: true | false",
        "had_retrieval_tool_access": "REPLACE: true | false",
        "prior_conversation_contained_resource_metadata": "REPLACE: true | false",
        "tools_used": [],
    },
    "notes": "",
}

PACKET_HEADER = """# Packet {packet_id}

**Assigned task class:** `{task_class}` — {class_description}

**What to do with this:** read the operational text below, work out what
situation would make someone need this work done, and write *that request*.
Do not summarize the text, do not quote it, and do not try to identify it.
Redacted spans (`[identifier removed]`, `[path removed]`,
`[related-resource list removed]`) carried identity only.

**Write one task.** Put it in `tasks.jsonl` with `"packet_id": "{packet_id}"`.

---

"""

REVIEWER_README = """# PAE_REVIEWER_PRIVATE_PACKET_V1

**Do not give any of this to the task author.** It contains the answer key.

You are the independent reviewer. A different actor wrote the tasks; you assign
the labels. You did not write these tasks and must not rewrite them — if a task
is unusable, mark it so and say why.

## What is here

| Path | What it is |
|---|---|
| `target-map/packet-target-map.json` | packet ID → target UID, public ID, path, title, integrity hashes, sanitization operations. |
| `target-map/selection.json` | The full deterministic selection record, including the seed. |
| `REVIEW_INSTRUCTIONS.md` | How to label. Read this before anything else. |
| `label-templates/` | The label and adjudication record formats. |
| `candidate-tools/` | How to run raw, non-PAE candidate discovery. |

## The rule that makes your labels worth anything

**Do not use PAE to decide what should have answered a task.**

Specifically, do not run `pae route`, `pae search`, the MCP server, the
ContextCompiler, or read the Phase 4 expected-label set or the routing
reference tables. If you label a task with what PAE returns, the benchmark
grades PAE against its own output and the result means nothing — while looking
exactly like a good result.

Use `candidate-tools/` instead. It is ripgrep over the participant snapshot
with token-hit aggregation, and its ordering is **not** a relevance judgement.
Every candidate list gives you *none of these* and *search further*. Use them
freely; a forced choice from a list that happened to miss the right answer is
how a benchmark acquires wrong labels.

## What a label is

For each task: the resources that would genuinely answer it well (zero, one or
several), the acceptable scopes and kinds where you are confident, and whether
declining to answer is the correct behaviour. Zero acceptable resources is a
real and expected answer — the natural half deliberately contains requests the
collection should have nothing for.

Record your reasoning. `label_rationale` is not optional and "seemed right" is
not a rationale.

## Provenance

Fill in `label-templates/reviewer-provenance.json` honestly, including whether
you are a human or a model. A model reviewer is acceptable and expected under
the documented fallback; a model reviewer described as human is not.

## Disagreements

Where you and the author's `notes_for_reviewer` conflict, or where you cannot
decide, record it in an adjudication entry rather than picking one. The
maintainer adjudicates. You do not, and neither does the author.
"""

REVIEW_INSTRUCTIONS = """# Review instructions

## Order of work

1. Read the task. Only the task — not the packet it came from, not the map.
2. Decide what a genuinely good answer would need. Write that down first.
3. *Then* run candidate discovery and see what the corpus actually has.
4. Label. Record the rationale.
5. Only after labelling a masked-derived task, open the map entry and check
   whether the intended target is among your acceptable set. If it is not,
   **do not change your label** — record the divergence. A masked packet's
   target is what the task was built from, not proof of what should answer it.

Step 5 is the one people get backwards. The map is a check on the *packet*, not
an instruction about the *label*.

## Running candidate discovery

```bash
python -m pae_eval review-candidates \\
  --snapshot <participant snapshot> --repo <PAE checkout> \\
  --query "<the task's query text>" --max-candidates 12 --json
```

The ordering is raw token-hit aggregation. It is not PAE relevance and must
never be quoted as such. If nothing in the list is right, that is a finding:
label zero acceptable resources.

## Labelling rules

**Zero resources is a valid label.** Do not stretch to find something.

**Several resources is a valid label.** If two genuinely answer it, list both
and mark the better one `primary`.

**Scope and kind are scored only when you are confident.** Listing a dimension
you did not really decide creates a wrong answer key. Leave it out instead.

**Declining is sometimes correct.** For a request the collection has nothing
for, the correct behaviour is to say so, not to return a near-miss.

**A task can be unusable.** If it is incoherent, self-contradictory, or
answerable only by naming a resource, mark it `usable: false` with a reason. It
goes to adjudication rather than into the benchmark.

## What you must not consult

- `pae route`, `pae search`, `pae bundle`, or any PAE CLI retrieval command
- the PAE MCP server
- `SearchEngine`, `Router`, `ContextCompiler`
- the Phase 4 search/routing regression set and its expected labels
- the routing reference phrase tables

Reading a resource's own text to decide whether it answers a task is fine and
expected. Asking the system under test what it thinks is not.
"""

CANDIDATE_TOOLS_README = """# Candidate discovery tooling

Raw discovery only. This deliberately does not use PAE retrieval.

## What it does

1. Splits your query into tokens and drops a short stoplist.
2. Runs one fixed-string, case-insensitive ripgrep pass per token over the
   participant snapshot.
3. Aggregates hits per file and orders by distinct tokens matched, then total
   hits, then path.
4. Consults the Registry **only** to turn a file path into a stable identity —
   UID, kind, scope, title, description.

## What it does not do

No `pae_engine.search`, no `pae_engine.routing`, no `pae_engine.context`, no
`pae_engine.mcp`, no `SearchEngine`, no `Router`, no `ContextCompiler`. A test
in the harness asserts this at source level and over the transitive import
closure, so the guarantee is checked rather than promised.

## Usage

```bash
python -m pae_eval review-candidates \\
  --snapshot <snapshot dir> --repo <PAE checkout> \\
  --query "text of the task" --max-candidates 12 --json
```

Excerpts are withheld for safety-gated resources: their guard text is
load-bearing and must not be shown truncated. The record says so explicitly
when it happens.

## Reading the output

`rank` is a position in a token-hit ordering. It is not a relevance score and
must not be reported as one. `ranking_basis` says this on every record so it
cannot be quoted out of context.

You always have *none of these* and *search further*.
"""

NATURAL_TEMPLATES_README = """# Natural task templates

These are **shapes**, not fill-in forms. Copying one and changing the nouns
produces exactly the submission `NATURAL_TASK_BRIEF.md` tells you not to write.

Read `worked-shapes.md` once to calibrate what "a real request with a real
deliverable" looks like, then close it and write in your own voice.

If your set can be reconstructed by anyone who has read this directory, it is
too uniform.
"""

WORKED_SHAPES = """# Worked shapes

Six contrasts. Each shows a weak request and the same underlying need written
as a real one. None of these are tasks to submit — they exist to calibrate.

## 1. A question versus a piece of work

**Weak.** "What are best practices for code review?"

**Strong.** "Four of us review each other's PRs and we keep arguing about scope
— one person blocks on naming, another waves through 600-line diffs. Write the
one-page review standard I can put in the repo, with what each reviewer is
expected to check and what is explicitly not their job."

The first has an answer. The second has a deliverable someone will paste into a
file on Monday.

## 2. Stating the format you actually need

**Weak.** "Help me summarise this quarter's incidents."

**Strong.** "Summarise our Q3 incidents as a table: date, service, customer
minutes lost, root-cause category, and whether the follow-up action shipped.
Then three sentences under it on what the pattern is. Leadership reads the
three sentences and nothing else."

## 3. A requester who is slightly wrong about their own problem

**Strong.** "I need a better standup format, ours takes 40 minutes. Six
engineers, two timezones, we go round the room and everyone lists what they did
yesterday."

A good answer may well say the format is not the problem. Write requests that
leave room for that.

## 4. Messy input, recoverable need

**Strong.** "need a SOP for onboarding new CS reps — we're SaaS, ~15 ppl, no
LMS. currently its just shadowing w/ whoevers free. mgr wants smth repeatable
by end of month, doesnt have to be fancy"

Typos, acronyms, missing capitals. Still perfectly clear what is wanted.

## 5. Genuinely outside what a professional library would hold

**Strong.** "My neighbour's oak drops branches onto my shed roof. What's the
sensible order of operations before I spend money on a solicitor?"

A real question. A curated collection of professional workflows probably has
nothing that genuinely fits, and saying so is the correct response.

## 6. Long and constrained

**Strong.** "We're moving 40 internal services off a shared Postgres onto
per-service databases. Constraints: no downtime windows longer than five
minutes, two engineers, six months, and the analytics team currently joins
across service boundaries in about a dozen dashboards. Give me the sequencing —
what moves first and why — plus what I tell the analytics team in the meantime,
and the three things most likely to go wrong. Prose, not a checklist; I need to
forward it."

Several constraints, more than one deliverable, a stated format preference.
"""

MASKED_PACKETS_README = """# Masked resource packets

{masked_count} packets. Each contains sanitized operational text and the task
class you should write for it.

## How to use one

1. Read the text. Work out **what situation would make someone need this work
   done**.
2. Write that person's request. One task per packet.
3. Record it in `tasks.jsonl` with the packet's `packet_id`.

## What the redactions mean

`[identifier removed]`, `[path removed]` and `[related-resource list removed]`
mark spans that carried identity rather than meaning. Read past them. Do not
speculate about what they contained and do not mention them in your task.

## The trap

The obvious move is to paraphrase the packet into a request. Resist it. A task
that mirrors its source is answerable by string matching and measures nothing.

Change the surface: different industry, different scale, different job title,
different reason for asking. Share no distinctive four-word phrase with the
packet. The task should read like a message from someone who has never seen
this document — because that is who it is from.

## If a packet seems thin

Some packets sanitize down to fairly short text. Write the best realistic
request you can and note the difficulty in `notes_for_reviewer`. Do not invent
domain facts to pad it out.
"""

LABEL_TEMPLATES_README = """# Label templates

One `label-record.json` per task. One `adjudication-record.json` per unresolved
disagreement. One `reviewer-provenance.json` for the whole review pass.

## Field notes

`acceptable_resources` — zero, one or several. Zero is a real answer. Mark the
best one `primary` and the rest `acceptable`.

`scored_dimensions` — list only the dimensions you actually decided. A
dimension listed with an empty acceptable list is a validation error, by
design: an empty list cannot distinguish "nothing is acceptable" from "not
graded here", and a scorer that guesses marks correct answers wrong across a
whole stratum.

`correct_behaviour_is_declining` — true when the collection genuinely has
nothing for the request and saying so is the right response.

`label_rationale` — required, and it must say *why*, not *what*. "Covers
incident retrospectives specifically, including the blameless framing the
request asks for" is a rationale. "Best match" is not.

`usable` — set false for tasks that cannot be graded at all. Say why. These go
to adjudication, not into the benchmark.

## Translating author provenance

The author's `provenance.json` records `saw_collection_metadata`. That maps to
`label_provenance.author.saw_pae_metadata` in the benchmark schema. The author
is not told the collection's name; you carry the translation across.
"""

LABEL_RECORD_TEMPLATE = {
    "task_id": "REPLACE",
    "usable": True,
    "unusable_reason": "",
    "acceptable_resources": [
        {"uid": "REPLACE", "grade": "primary", "why": "REPLACE"}
    ],
    "acceptable_scopes": [],
    "acceptable_kinds": [],
    "correct_behaviour_is_declining": False,
    "scored_dimensions": ["REPLACE: any of resource, scope, kind, route_status"],
    "label_rationale": "REPLACE: why these and not the near-misses",
    "candidate_discovery": {
        "query_used": "REPLACE",
        "candidates_reviewed": 0,
        "chose_none_of_these": False,
        "searched_further": False,
        "notes": "",
    },
    "divergence_from_packet_target": {
        "applies": False,
        "note": "Masked-derived tasks only. Recorded, never used to change the label.",
    },
    "pae_retrieval_consulted": False,
}

ADJUDICATION_RECORD_TEMPLATE = {
    "task_id": "REPLACE",
    "raised_by": "REPLACE: reviewer | author-note | validation",
    "question": "REPLACE: what is actually in dispute",
    "author_position": "",
    "reviewer_position": "",
    "maintainer_decision": "",
    "decided_on": "",
    "outcome": "REPLACE: keep | revise-label | drop-task | defer",
    "rationale": "",
}

REVIEWER_PROVENANCE_TEMPLATE = {
    "reviewer": {
        "kind": "REPLACE: human | ai",
        "provider": "REPLACE: e.g. anthropic, openai, or empty for a human",
        "model": "REPLACE: exact model identifier, or empty for a human",
        "date": "REPLACE: YYYY-MM-DD",
        "prompt_sha256": "REPLACE: sha256 of the instructions given, if any",
        "saw_pae_metadata": True,
    },
    "separation": {
        "same_session_as_author": "REPLACE: true | false — must be false",
        "same_model_as_author": "REPLACE: true | false",
        "used_pae_search_or_router": "REPLACE: true | false — must be false",
        "used_phase_4_expected_labels": "REPLACE: true | false — must be false",
    },
    "notes": "",
}

