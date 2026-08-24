# Adversarial fixtures (red-team corpus)

*For informational and research purposes only. Not financial, investment, or tax advice.*

These are **deliberately hostile** sample inputs used by `tests/test_injection.py` to prove
the SECURITY.md defenses hold: content ingested through a `data-source-adapter` seam is
**data, never instruction**, and the code gates do not read it. None of these are real
filings, tokens, or patterns — they exist only to be safely defeated by the gates.

| File | Simulates | The defense it must not defeat |
|---|---|---|
| `injected_filing.md` | a 10-K / news body carrying embedded instructions + a planted secret | imperatives in the text drive no action; `egress_check.py` catches the planted secret before any write (SECURITY §4a/§4d) |
| `injected_pattern_PATTERN-9001.md` | a pattern whose NOTES BODY screams "mark me validated" while its frontmatter is an un-validated `hypothesis` | `validate_pattern.py` reads frontmatter + OOS evidence in code, never body prose — it stays FAIL (SECURITY §4b, Gate A) |

If you add a new ingest path, add a matching hostile fixture here and a case in
`tests/test_injection.py`.
