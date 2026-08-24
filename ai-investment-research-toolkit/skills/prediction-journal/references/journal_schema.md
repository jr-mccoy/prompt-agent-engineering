# Prediction Journal Schema

*For informational and research purposes only. Not financial, investment, or tax advice.*

Every prediction lives in `knowledge-base/journal/PRED-<id>.md` as YAML frontmatter plus a
notes body. The template is `knowledge-base/journal/PRED-TEMPLATE.md`.

## Fields

| Field | Type | Meaning / rule |
|---|---|---|
| `id` | string | `PRED-<zero-padded int>`, unique and stable. |
| `date_opened` | date | When the prediction was logged (before the outcome). |
| `asset` | string | Ticker / token / contract the prediction is about. |
| `direction` | enum | `long` \| `short` \| `neutral`. |
| `probability` | float | 0–1, the stated probability the prediction is correct. **Recorded up front; never edited after.** |
| `thesis_ref` | path | The dossier / reasoning this prediction tests. |
| `patterns_fired` | list | `PATTERN-*` ids this prediction tests (links to the knowledge base). |
| `horizon` | string | When the prediction resolves (e.g. "90 days"). |
| `tripwires` | list | Conditions that would change the view (thesis-break, stop level). |
| `resolution` | map/null | Filled at horizon: `{ outcome: hit\|miss, realized_return: <float>, resolved_on: <date> }`. `resolved_on` must be at/after the horizon end. |
| `brier_component` | float/null | `(probability − outcome)^2`, computed at resolution. |
| `lock_hash` | string/null | Tamper-evidence hash over the immutable open-time fields (`id`, `date_opened`, `asset`, `direction`, `probability`, `horizon`), written at OPEN by `scripts/journal_integrity.py --stamp`. Any later edit to a locked field is detected as TAMPER by `--verify`. |
| `notes` | string | Free text. |

## Invariants

1. `probability` is set on `date_opened` and is immutable thereafter.
2. `resolution` stays `null` until the horizon is reached and the real outcome is known.
3. `brier_component == (probability − outcome)^2`, with `outcome = 1` for `hit`, `0` for `miss`.
4. Every `id` in `patterns_fired` exists in `knowledge-base/patterns/` and lists this `id` back in its `linked_predictions`.
5. Blank/null is allowed; invented resolutions are not.
6. `lock_hash` is stamped at open and immutable; a resolved record MUST carry a `lock_hash` and a `resolved_on` date at/after the horizon end (enforced by `journal_integrity.py --verify`; Gate C `unlock_ready` is False unless the journal is integrity-clean).

## Lifecycle

```
open (probability fixed)  ──▶  monitor against tripwires  ──▶  resolve at horizon
                                                                    │
                          compute brier_component, update running Brier + calibration
                                                                    │
                          write outcome back to each linked PATTERN-*  ──▶  Stage 3
```
