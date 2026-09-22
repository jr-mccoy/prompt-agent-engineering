---
name: Release_Notes
description: Writes release notes.
---

<!-- SYNTHETIC TEST FIXTURE — NOT INDEPENDENT BENCHMARK EVIDENCE -->

This fixture is deliberately defective. It is the negative case for the
observed-score detectors: the frontmatter name is uppercase, carries an
underscore and does not match the bundle directory `release-notes`; the
description is far under the length band and states no trigger; there is no
"When to Use" or "When NOT to Use" section, no related-skills section, no
verification, and no safety or failure-handling section. It also plants the
three blocking security findings.

# Release Notes

Paste the changelog and I will tidy it up.

Configuration, as the original author left it:

    token = "xoxb-EXAMPLE-NOT-A-REAL-SECRET-fixture-only"
    template_path = "/Users/jdoe/work/release/template.md"
    notify = "jane.doe@example-corp.test"

Run it and send the output.
