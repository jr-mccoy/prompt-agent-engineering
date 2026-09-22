# Governance audit — forbidden sentence

<!-- SYNTHETIC TEST FIXTURE — NOT INDEPENDENT BENCHMARK EVIDENCE -->

SYNTHETIC TEST FIXTURE — NOT INDEPENDENT BENCHMARK EVIDENCE. Negative fixture: a claim ADR-0040 forbids by name.

## Scope

The corpus `samples/corpus-good` was inventoried and six artifacts were counted.

## Findings

PAE has 90% accuracy on this corpus and the remediation follows from that.

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
