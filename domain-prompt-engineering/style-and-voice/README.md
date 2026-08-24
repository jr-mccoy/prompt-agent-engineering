# Style and Voice

**Purpose:** Prompts for extracting, encoding, applying, and auditing writing style and voice. Use these when the *how something is written* matters as much as *what is written*.

---

## When to Use This Subdirectory

- You need to codify a writer's or brand's voice into rules a model can follow.
- You want to enforce a specific formality register or ban specific tics.
- You need to adapt the same content for different audiences.
- You want to audit whether multiple outputs from the same prompt are stylistically consistent.

---

## Prompts

| File | One-line description |
|------|---------------------|
| `style_voice_extraction_from_corpus.md` | Codify a voice from 5+ text samples into a ranked operational rule set with evidence citations and a self-test. |
| `style_voice_transfer_prompt.md` | Apply a target voice rule set to a source text without altering any factual claim; produces a change ledger. |
| `style_register_control.md` | Rewrite text at a specified formality level (Formal / Neutral / Casual) using a banned/required forms table. |
| `style_brand_guideline_to_prompt.md` | Convert a brand book or style guide into an enforceable ≤20-rule prompt block, classifying each guideline by enforceability tier. |
| `style_persona_designer_for_writing.md` | Design a bounded writing persona (sentence length, vocabulary tier, hedging level) for use in prompts — not an agent persona. |
| `style_anti_voice_designer.md` | Build a banlist of specific voice tics (em-dashes, hedges, "Sure,", emoji) with detection patterns and one-line repair rules. |
| `style_audience_adaptation_prompt.md` | Produce N audience-specific variants of the same content with per-variant delta annotations classifying every change. |
| `style_length_and_density_control.md` | Enforce words-per-claim, sentences-per-paragraph, and total word count caps with a before/after compliance table. |
| `style_consistency_audit_across_outputs.md` | Measure style drift across N outputs from the same prompt across 8 signals; produces a ranked drift report with repair recommendations. |
| `style_signature_phrase_kill_list.md` | Detect AI-signature phrases in a corpus, frequency-rank them, and produce a banlist with per-phrase repair rules. |

---

## Typical Workflow

```
Corpus available?
│
├─→ YES: voice_extraction → voice_transfer (to apply)
│                        → consistency_audit (to verify)
│
└─→ NO brand guidelines available?
    │
    ├─→ YES: brand_guideline_to_prompt
    │
    └─→ NO: persona_designer_for_writing → register_control
                                         → anti_voice_designer (to suppress unwanted tics)
                                         → audience_adaptation (to serve multiple readers)
```

---

## Related Subdirectories

- `output-formatting/` — for structural and length formatting (headings, lists, word caps)
- `domain-prompt-engineering/escape-median/` — for moving outputs off the model's default style
- `domain-prompt-engineering/instruction-design/` — for encoding style rules into a rule hierarchy
