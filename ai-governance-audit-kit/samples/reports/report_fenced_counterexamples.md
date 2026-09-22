# Governance audit — fenced counter-examples

<!-- SYNTHETIC TEST FIXTURE — NOT INDEPENDENT BENCHMARK EVIDENCE -->

SYNTHETIC TEST FIXTURE — NOT INDEPENDENT BENCHMARK EVIDENCE. Negative fixture: the same forbidden sentences, fenced as the counter-examples they are. Documentation about what not to write must stay writable.

## Scope

The corpus `samples/corpus-good` was inventoried and six artifacts were counted.

## What this report will not say

None of the following may appear as prose:

```text
PAE makes AI 20% smarter
PAE has 90% accuracy
proven to improve every model
Consolidation reduces prompt sprawl by 40%.
This bundle is Tier 3.
The engagement pays for itself at an ROI of 3.2x.
```

Each is blocked by Gate B when written outside a fence.

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
