# Governance audit — corpus-good (sample)

<!-- SYNTHETIC TEST FIXTURE — NOT INDEPENDENT BENCHMARK EVIDENCE -->

SYNTHETIC TEST FIXTURE — NOT INDEPENDENT BENCHMARK EVIDENCE. Every figure below
comes from `samples/corpus-good`, a fixture built for this kit's own tests. It
is not a measurement of anything outside that fixture.

## Scope

The corpus was inventoried under the roots declared in `config/audit.json`.
Six artifacts were counted: four prompts and two skills. Five markdown files
under those roots were excluded, each with a recorded reason.

## Duplication

One exact cluster was found, evidenced by content hash: two byte-identical
files under `prompts/`. Two candidate near-neighbour clusters were found by
BM25F query-by-document, the strongest at similarity 0.67.

No cluster names a canonical. Which member of a byte-identical pair came first
is not something an audit can determine, and lexical similarity is not
provenance. These are findings for the corpus owner to adjudicate.

## Structural findings

Of the 100-point authoring rubric, 54 points are mechanically observable. The
two skill bundles were scored against that observable subset only, with the
subset's maximum stated beside every figure.

| Bundle | Observed | Observable max | Verdict |
|---|---|---|---|
| `skills/deploy-helper` | 54 | 54 | clean |
| `skills/release-notes` | 26 | 54 | blocked |

`skills/release-notes` carries three blocking security findings: a
credential-shaped assignment, an absolute user path, and a contact address. Each
is reported with its file and line.

No tier is asserted for either bundle. The observable subset cannot support one.

## Limitations

- Every figure is specific to this fixture corpus, this config and this commit.
  Nothing here generalises to another corpus.
- Only 54 of the rubric's 100 points are mechanically observable. A high
  observable score says the structure is present, not that the content is good.
- Candidate clusters are lexical. A pair that shares vocabulary without sharing
  purpose will appear here, and a genuine duplicate written in different words
  will not.
- Scores are observed by regex from the artifacts. Where an author supplied
  their own rubric block, it is reported separately and never merged in.
- The author of an artifact is not its reviewer. Adjudication of these findings
  belongs to someone other than whoever wrote the corpus.
