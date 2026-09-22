# Governance audit — unstamped fixture figures

Negative fixture: figures drawn from `samples/corpus-good` with no synthetic stamp, so sample output could be read as a result.

## Findings

Of the 100-point rubric, 54 points are observable; the two bundles scored 54 and 26.

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
