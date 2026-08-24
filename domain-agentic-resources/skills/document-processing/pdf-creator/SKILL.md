---
name: pdf-creator
description: Create PDF documents from markdown with proper Chinese font support using weasyprint. This skill should be used when converting markdown to PDF, generating formal documents (legal, trademark filings, reports), or when Chinese typography is required. Triggers include "convert to PDF", "generate PDF", "markdown to PDF", or any request for creating printable documents.
metadata:
  tags:
    - pdf-generation
    - document-processing
    - weasyprint
    - markdown-conversion
    - chinese-fonts
  updated: "2026-04-11"
---

# PDF Creator

Create professional PDF documents from markdown with proper Chinese font support.

## Quick Start

Convert a single markdown file:

```bash
uv run --with weasyprint --with markdown scripts/md_to_pdf.py input.md output.pdf
```

Batch convert multiple files:

```bash
uv run --with weasyprint --with markdown scripts/batch_convert.py *.md --output-dir ./pdfs
```

## macOS Environment Setup

If encountering library errors, set these environment variables first:

```bash
export DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH"
export PKG_CONFIG_PATH="/opt/homebrew/lib/pkgconfig:$PKG_CONFIG_PATH"
```

## Font Configuration

The scripts use these Chinese fonts (with fallbacks):

| Font Type | Primary | Fallbacks |
|-----------|---------|-----------|
| Body text | Songti SC | SimSun, STSong, Noto Serif CJK SC |
| Headings | Heiti SC | SimHei, STHeiti, Noto Sans CJK SC |

## Output Specifications

- **Page size**: A4
- **Margins**: 2.5cm top/bottom, 2cm left/right
- **Body font**: 12pt, 1.8 line height
- **Max file size**: Designed to stay under 2MB for form submissions

## Common Use Cases

1. **Legal documents**: Trademark filings, contracts, evidence lists
2. **Reports**: Business reports, technical documentation
3. **Formal letters**: Official correspondence requiring print format

## Troubleshooting

**Problem**: Chinese characters display as boxes
**Solution**: Ensure Songti SC or other Chinese fonts are installed on the system

**Problem**: `weasyprint` import error
**Solution**: Run with `uv run --with weasyprint --with markdown` to ensure dependencies

---

## Core Concepts

### WeasyPrint Rendering Pipeline

WeasyPrint converts HTML/CSS to PDF using a pipeline: Markdown is first converted to HTML via the `markdown` library, then CSS stylesheets are applied, and finally WeasyPrint renders the result into a paginated PDF. Understanding this pipeline is key to controlling output quality.

### CSS Paged Media

PDF generation relies on the CSS Paged Media specification (`@page` rules). This is fundamentally different from screen CSS -- you control paper size, margins, headers, footers, and page breaks explicitly. WeasyPrint supports most of the CSS Paged Media Level 3 spec.

### Font Embedding

WeasyPrint embeds fonts directly into the PDF. For CJK (Chinese, Japanese, Korean) text, this means the PDF is self-contained and renders correctly on any system, even without the fonts installed locally. Font embedding increases file size -- a typical CJK font adds 5-15MB.

---

## Advanced CSS Styling Patterns

### Headers and Footers

```css
@page {
  size: A4;
  margin: 2.5cm 2cm;

  @top-center {
    content: "Company Name - Confidential";
    font-size: 9pt;
    color: #666;
  }

  @bottom-right {
    content: "Page " counter(page) " of " counter(pages);
    font-size: 9pt;
    color: #666;
  }

  @bottom-left {
    content: "Generated: 2026-04-11";
    font-size: 9pt;
    color: #999;
  }
}
```

### Page Numbers with Named Pages

```css
/* Cover page without page numbers */
@page cover {
  margin: 0;
  @bottom-right { content: none; }
  @top-center { content: none; }
}

/* Regular content pages with numbers */
@page content {
  @bottom-center {
    content: counter(page);
    font-size: 10pt;
  }
}

.cover-page { page: cover; }
.content { page: content; }
```

### Cover Page Styling

```css
.cover-page {
  page: cover;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  text-align: center;
  page-break-after: always;
}

.cover-page h1 {
  font-size: 36pt;
  font-weight: bold;
  margin-bottom: 1cm;
}

.cover-page .subtitle {
  font-size: 18pt;
  color: #555;
  margin-bottom: 2cm;
}

.cover-page .author {
  font-size: 14pt;
  color: #777;
}
```

### Page Break Control

```css
/* Force page break before every h1 */
h1 { page-break-before: always; }

/* Prevent orphaned headings at page bottom */
h2, h3 { page-break-after: avoid; }

/* Keep tables together */
table { page-break-inside: avoid; }

/* Keep figure with its caption */
figure { page-break-inside: avoid; }
```

---

## Multi-Document Workflows

### Table of Contents Generation

Generate a table of contents by extracting headings from markdown before conversion:

```python
import re

def generate_toc(markdown_content):
    """Extract headings and build a TOC with page anchors."""
    toc_lines = ["# Table of Contents\n"]
    for match in re.finditer(r'^(#{1,3})\s+(.+)$', markdown_content, re.MULTILINE):
        level = len(match.group(1))
        title = match.group(2)
        anchor = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
        indent = "  " * (level - 1)
        toc_lines.append(f"{indent}- [{title}](#{anchor})")
    return "\n".join(toc_lines)
```

### Document Merging

Combine multiple markdown files into a single PDF with page breaks:

```bash
# Merge multiple markdown files with separator
for file in 01-intro.md 02-body.md 03-appendix.md; do
  cat "$file"
  echo -e "\n\n---PAGE-BREAK---\n\n"
done | uv run --with weasyprint --with markdown scripts/md_to_pdf.py - merged.pdf
```

### Batch Conversion with Consistent Styling

```bash
# Apply a shared stylesheet across all documents
for file in docs/*.md; do
  output="pdfs/$(basename "${file%.md}.pdf")"
  uv run --with weasyprint --with markdown \
    scripts/md_to_pdf.py "$file" "$output" --css shared-styles.css
done
```

---

## Best Practices for Print-Ready Output

### Bleed and Trim Marks

For professional printing, add bleed (extra area beyond trim) and trim marks:

```css
@page {
  size: 216mm 303mm; /* A4 + 3mm bleed on each side */
  margin: 2.5cm;
  marks: crop cross;
  bleed: 3mm;
}
```

### Color Profiles

- **Screen PDFs**: sRGB is the default and works well for on-screen viewing
- **Print PDFs**: Use CMYK-safe colors; avoid pure RGB values that do not convert cleanly
- **Tip**: Stick to web-safe colors or define colors in HSL to maintain consistency across output modes

### Typography for Print

```css
body {
  font-size: 12pt;        /* Standard for body text */
  line-height: 1.8;       /* Generous leading for CJK text */
  orphans: 3;             /* Minimum lines at bottom of page */
  widows: 3;              /* Minimum lines at top of page */
  hyphens: auto;          /* Enable hyphenation for English */
  text-align: justify;    /* Justified text for formal documents */
}
```

### File Size Optimization

| Strategy | Impact | Trade-off |
|----------|--------|-----------|
| Subset CJK fonts | -60-80% file size | Build complexity |
| Compress images before embedding | -30-50% | Image quality |
| Use SVG for diagrams | Smaller than PNG | Rendering complexity |
| Limit embedded font weights | -20-40% | Design flexibility |
| Avoid base64 inline images | -10-20% | Requires file references |

---

## Common Pitfalls

| Pitfall | Symptom | Solution |
|---------|---------|----------|
| Missing CJK fonts | Characters render as boxes or tofu | Install Songti SC / Noto Serif CJK SC on the system |
| Forgetting `@page` rules | Default browser-like margins, no headers/footers | Always define `@page` with explicit size and margins |
| Images exceeding page width | Content overflows or is clipped | Set `img { max-width: 100%; height: auto; }` |
| No page break control | Tables split across pages awkwardly | Use `page-break-inside: avoid` on tables and figures |
| Enormous file size | PDF exceeds upload limits (e.g., 2MB forms) | Subset fonts, compress images, remove unused font weights |
| Relative image paths broken | Images missing in output | Use absolute paths or embed images as base64 |
| CSS `flexbox`/`grid` limitations | Layout does not render as expected | WeasyPrint has partial flexbox support; prefer block/table layout for complex structures |
| Incorrect `DYLD_LIBRARY_PATH` on macOS | Library load errors on Apple Silicon | Export paths before running (see macOS Environment Setup) |

---

## Template Examples

### Report Template

```markdown
<div class="cover-page">
  <h1>Quarterly Report</h1>
  <p class="subtitle">Q1 2026 Performance Summary</p>
  <p class="author">Prepared by: Finance Team</p>
  <p class="date">April 2026</p>
</div>

## Executive Summary
[Brief overview of key findings...]

## Financial Highlights
| Metric | Q1 2026 | Q4 2025 | Change |
|--------|---------|---------|--------|
| Revenue | $X.XM | $X.XM | +X% |

## Detailed Analysis
[Section content...]

## Appendix
[Supporting data...]
```

### Formal Letter Template

```markdown
<div class="letter-header">
  <p class="sender">Company Name<br>123 Business Ave<br>City, State ZIP</p>
  <p class="date">April 11, 2026</p>
  <p class="recipient">Recipient Name<br>Organization<br>Address</p>
</div>

Dear [Recipient],

[Body of the letter...]

Sincerely,

[Signature Block]
```

### Contract Template

```markdown
<div class="cover-page">
  <h1>Service Agreement</h1>
  <p class="subtitle">Between Party A and Party B</p>
  <p class="date">Effective Date: April 11, 2026</p>
</div>

## 1. Definitions
In this Agreement, the following terms shall have the meanings set out below:
- **"Services"** means...
- **"Term"** means...

## 2. Scope of Services
[Description of services...]

## 3. Payment Terms
| Milestone | Amount | Due Date |
|-----------|--------|----------|
| Signing | $X,XXX | Upon execution |
| Delivery | $X,XXX | 30 days after delivery |

## 4. Confidentiality
[Confidentiality clause...]

## Signatures
_________________________    _________________________
Party A                      Party B
Date: _______________        Date: _______________
```

---

## Advanced Usage

### Custom Stylesheets per Document Type

Maintain a library of CSS files for different document types:

```
styles/
  report.css       # Cover pages, headers, TOC styling
  letter.css       # Letterhead, signature blocks
  contract.css     # Numbered clauses, signature lines
  invoice.css      # Tables, totals, payment terms
  technical.css    # Code blocks, diagrams, callouts
```

Pass the appropriate stylesheet at conversion time:

```bash
uv run --with weasyprint --with markdown \
  scripts/md_to_pdf.py contract.md contract.pdf --css styles/contract.css
```

### Watermarks

```css
@page {
  background-image: url('watermark.png');
  background-repeat: no-repeat;
  background-position: center center;
  background-size: 50%;
}

/* Text-based watermark alternative */
@page {
  @top-center {
    content: "DRAFT";
    font-size: 72pt;
    color: rgba(200, 200, 200, 0.3);
    transform: rotate(-45deg);
  }
}
```

### Conditional Content for Print vs Screen

```css
@media print {
  .screen-only { display: none; }
  a[href]::after { content: " (" attr(href) ")"; font-size: 9pt; color: #666; }
}

@media screen {
  .print-only { display: none; }
}
```

### Embedding Metadata

WeasyPrint supports PDF metadata through the HTML `<meta>` tags:

```html
<meta name="author" content="Document Author">
<meta name="description" content="Document description for PDF metadata">
<meta name="keywords" content="pdf, report, quarterly">
<title>Document Title Shown in PDF Viewer</title>
```
