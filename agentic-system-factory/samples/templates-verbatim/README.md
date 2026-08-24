# templates-verbatim — anti-gaming negative fixture

Verbatim, **unfilled** copies of the factory templates, renamed to the bundle
file names. This fixture pins the anti-gaming rule in the gate scripts:

- The templates quote the *passing* marker values only inside fenced code
  blocks, and the scripts **ignore markers inside code fences / inline code**.
- Therefore a lazy "copy the templates, change nothing" bundle must **FAIL**
  Gates 0, A, B, C and rubric scoring. `--self-check` in `check_gate.py` and
  `score_rubric.py` asserts exactly that (and `validate_bundle.py` expects the
  structural FAIL, since this is deliberately not a full bundle).

If a template edit or a script change ever makes this fixture pass a gate,
the gates have been re-armed for gaming — the self-checks will catch it.

Do not fill these files in. Regenerate them by re-copying `templates/*` if the
templates change:

```
cp templates/ARCHITECTURE_TEMPLATE.md        samples/templates-verbatim/ARCHITECTURE.md
cp templates/GATE_DESIGN_TEMPLATE.md         samples/templates-verbatim/GATE_DESIGN.md
cp templates/EVAL_HARNESS_TEMPLATE.md        samples/templates-verbatim/EVAL_HARNESS.md
cp templates/DISCLOSURE_MANIFEST_TEMPLATE.md samples/templates-verbatim/DISCLOSURE_MANIFEST.md
cp templates/BUNDLE_MANIFEST_TEMPLATE.md     samples/templates-verbatim/RUBRIC_SCORE.md
```
