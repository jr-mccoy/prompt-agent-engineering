# Scientific & Technical Illustration Prompts

Production-ready prompts for **scientific and technical figures** — labeled scientific illustrations, exploded/assembly diagrams, and chart/graph images. These are the **highest-accuracy-risk** image tasks in this repository: image models render plausible-looking but frequently **wrong** structures, fits, and data, and they **hallucinate label text and numbers**. Every prompt in this directory carries a mandatory accuracy/anti-fabrication protocol and an expert-verification gate.

**Parent guide:** [IMAGE_MODEL_SELECTION_GUIDE.md](../IMAGE_MODEL_SELECTION_GUIDE.md) · related: [nano-banana/nanobana_search_grounded_infographic.md](../nano-banana/nanobana_search_grounded_infographic.md)

---

## ⚠️ Read Before Using Any Prompt Here

1. **Image models are not reliable for precise scientific/technical content.** They invent structures, fits, organelle counts, bond geometry, fastener counts, and data values; they misrender labels and numbers.
2. **Supply the ground truth.** Enumerate the exact structures/parts/values in the prompt — never let the model decide what is "correct."
3. **Add labels/keys in post.** Model-rendered text is unreliable; prefer numbered callout placeholders and place verified text in a vector editor.
4. **Expert / spec / real-tool verification is mandatory** before any publication, teaching, clinical, manual, or decision use.
5. **For correct charts, use a real charting library** (matplotlib, D3, spreadsheet) — image models draw chart-like pictures, they do not plot data.

---

## Prompts

| Prompt | Produces | Accuracy Gate | Recommended Model |
|--------|----------|---------------|-------------------|
| [Scientific Illustration](scientific_illustration.md) | Clean labeled journal-style figure (cell, anatomy, process, apparatus) | Expert verifies every structure/relationship/label; labels in post | gpt-image-2 (clean figures) · Nano Banana Pro (text + search grounding) |
| [Exploded / Assembly Diagram](technical_exploded_diagram.md) | Exploded-view of a product/mechanism with numbered callouts | Engineer/spec verifies parts, counts, orientation, fit | gpt-image-2 (line-art) · Nano Banana 2 (reference real parts) |
| [Data Visualization Chart Image](data_visualization_chart_image.md) | Chart/graph rendered as a styled image | Value-by-value proportion check; prefer a real charting tool for data-bearing charts | Nano Banana Pro (text + grounding) · gpt-image-2 (styled layout) |

---

## Model ID Quick Reference

| Name | Model ID | Why for sci/tech |
|------|----------|------------------|
| gpt-image-2 | `gpt-image-2` | Clean labeled-figure / line-art layouts; ~95% text (still verify) |
| Nano Banana | `gemini-2.5-flash-image` | Budget drafts |
| Nano Banana Pro | `gemini-3-pro-image` | Near-perfect text + Google Search grounding — best when figures must reflect verifiable data (grounding reduces, never eliminates, error) |
| Nano Banana 2 | `gemini-3.1-flash-image` | Object slots to reference real parts (reduces invented geometry) |

---

## Why Search Grounding Helps (and Its Limit)

Nano Banana Pro's Google Search grounding can fetch and confirm current/established facts and values, which lowers fabrication risk for data and standard depictions. It **does not** guarantee correct *plotting* (chart proportions) or correct *structural geometry*. Grounding is a risk reducer, not a substitute for expert / real-tool verification.
