---
name: ocr-pdf-creator
description: Converts scanned or image-based PDF documents into searchable PDFs using OCR (Optical Character Recognition). This skill should be used when processing scanned textbook pages, frozen ink documents, photographed documents, or any PDF containing images of text rather than actual text. Triggers include "make PDF searchable", "OCR this PDF", "extract text from scanned PDF", "recognize text in PDF", "convert image PDF to text", "frozen ink", or "textbook page scan".
metadata:
  tags:
    - creator
    - document-processing
    - ocr
    - pdf
  updated: "2026-04-11"
---
# OCR PDF Creator

Convert scanned documents and image-based PDFs into fully searchable PDF documents with recognized text layers.

## Purpose

This skill transforms PDFs that contain images of text (scanned textbooks, photographed documents, "frozen ink" PDFs) into searchable PDFs where text can be selected, copied, and indexed. The original visual appearance is preserved while an invisible text layer is added beneath the images.

## When to Use This Skill

Use this skill when you need to:
- Make scanned textbook pages searchable
- Extract text from photographed or scanned documents
- Convert "frozen ink" PDFs (image-only PDFs) to searchable format
- Enable copy/paste from image-based PDFs
- Prepare scanned documents for indexing or archival
- Process historical documents or digitized books

## When NOT to Use This Skill

Do NOT use this skill when:
- The PDF already contains selectable text (use text extraction tools instead)
- You want to create a PDF from markdown (use `pdf-creator` skill)
- You need to edit the PDF content (use PDF editing tools)
- The source is not a PDF (convert to PDF first, then OCR)

## Prerequisites

Install `ocrmypdf` and Tesseract OCR:

**macOS:**
```bash
brew install ocrmypdf tesseract tesseract-lang
```

**Ubuntu/Debian:**
```bash
sudo apt install ocrmypdf tesseract-ocr tesseract-ocr-eng
# For additional languages:
sudo apt install tesseract-ocr-chi-sim tesseract-ocr-fra tesseract-ocr-deu
```

**Verify installation:**
```bash
ocrmypdf --version
tesseract --list-langs
```

## Quick Start

### Step 1: Basic OCR Conversion

**Purpose:** Add searchable text layer to a scanned PDF.

```bash
python scripts/ocr_pdf.py input_scan.pdf output_searchable.pdf
```

**Expected output:**
```
Processing: input_scan.pdf
Pages: 15
Language: eng
OCR complete: output_searchable.pdf
File size: 2.4 MB (original: 2.1 MB)
```

**Validation:**
- [ ] Open output PDF and verify text is selectable
- [ ] Use Ctrl+F to search for known text in the document

### Step 2: Multi-Language Documents

**Purpose:** Process documents with multiple languages or non-English text.

```bash
# Chinese textbook
python scripts/ocr_pdf.py textbook.pdf textbook_ocr.pdf --language chi_sim

# Mixed English and Chinese
python scripts/ocr_pdf.py document.pdf output.pdf --language eng+chi_sim

# French document
python scripts/ocr_pdf.py french_doc.pdf output.pdf --language fra
```

**Common language codes:**
| Language | Code |
|----------|------|
| English | eng |
| Simplified Chinese | chi_sim |
| Traditional Chinese | chi_tra |
| French | fra |
| German | deu |
| Spanish | spa |
| Japanese | jpn |
| Korean | kor |

### Step 3: Optimize for Quality vs Speed

**Purpose:** Balance OCR accuracy with processing time.

**High quality (slower, best for important documents):**
```bash
python scripts/ocr_pdf.py scan.pdf output.pdf --optimize 0 --deskew --clean
```

**Balanced (default):**
```bash
python scripts/ocr_pdf.py scan.pdf output.pdf
```

**Fast mode (lower quality, good for drafts):**
```bash
python scripts/ocr_pdf.py scan.pdf output.pdf --fast
```

### Step 4: Batch Processing

**Purpose:** Process multiple scanned PDFs at once.

```bash
# Process all PDFs in a directory
python scripts/batch_ocr.py ./scanned_books/ --output-dir ./searchable_books/

# With language specification
python scripts/batch_ocr.py ./chinese_docs/ --output-dir ./ocr_output/ --language chi_sim
```

**Validation:**
- [ ] Verify all files processed without errors
- [ ] Spot-check 2-3 output files for text selectability

## Advanced Options

### Deskewing and Cleaning

For crooked scans or noisy images:

```bash
python scripts/ocr_pdf.py scan.pdf output.pdf --deskew --clean --remove-background
```

| Option | Description |
|--------|-------------|
| `--deskew` | Straighten rotated pages |
| `--clean` | Remove specks and noise |
| `--remove-background` | Whiten background for cleaner output |

### Force Re-OCR

If a PDF already has (incorrect) OCR:

```bash
python scripts/ocr_pdf.py bad_ocr.pdf fixed.pdf --force
```

### Preserve Original Resolution

For archival quality:

```bash
python scripts/ocr_pdf.py scan.pdf archive.pdf --output-type pdf --optimize 0
```

## Common Issues

### Issue: "Unable to find Tesseract"

**Quick Diagnosis:**
```bash
which tesseract
tesseract --version
```

**Resolution:**
1. Install Tesseract: `brew install tesseract` (macOS) or `apt install tesseract-ocr` (Linux)
2. Ensure it's in PATH
3. Restart terminal

### Issue: Poor OCR Accuracy

**Quick Diagnosis:**
- Check if scan is high quality (300 DPI minimum recommended)
- Verify correct language is specified

**Root Causes:**
1. Low resolution scan
2. Wrong language specified
3. Heavily skewed or rotated pages
4. Background noise or artifacts

**Resolution:**
```bash
# Try with cleaning and deskewing
python scripts/ocr_pdf.py scan.pdf output.pdf --deskew --clean --optimize 0
```

### Issue: "Language not available"

**Quick Diagnosis:**
```bash
tesseract --list-langs
```

**Resolution:**
Install the required language pack:
```bash
# macOS
brew install tesseract-lang

# Linux
sudo apt install tesseract-ocr-<lang-code>
```

### Issue: Output File Much Larger

**Cause:** OCR adds text layer, and default settings may not optimize images.

**Resolution:**
```bash
# Use optimization
python scripts/ocr_pdf.py scan.pdf output.pdf --optimize 2
```

| Optimize Level | Description |
|----------------|-------------|
| 0 | No optimization (largest, highest quality) |
| 1 | Light compression (good balance) |
| 2 | Medium compression (smaller files) |
| 3 | Aggressive compression (smallest, some quality loss) |

## Processing Tips

### For Textbook Pages

- Use `--deskew` for photographed pages
- Specify appropriate language
- Consider `--clean` if pages have margin notes or artifacts

### For Historical Documents

- Use `--optimize 0` to preserve quality
- May need to experiment with `--clean` settings
- Consider batch processing with consistent settings

### For Mixed Content (Text + Diagrams)

- OCR focuses on text; diagrams remain as images
- Text in diagrams may not be recognized accurately
- Use higher quality settings for important documents

## Safety & Constraints

**NEVER:**
- Delete original scanned PDFs before verifying OCR output
- Use aggressive optimization on archival documents
- Assume OCR is 100% accurate (always spot-check critical documents)

**ALWAYS:**
- Keep original scans as backup
- Verify text selectability in output
- Check a few random pages for OCR accuracy
- Use appropriate language settings for non-English documents

## Reference Files

| Resource | Purpose |
|----------|---------|
| `scripts/ocr_pdf.py` | Main OCR conversion script |
| `scripts/batch_ocr.py` | Batch processing for multiple files |
| `references/ocr_tools_reference.md` | Comparison of OCR tools and detailed options |

## Related Skills

- `pdf-creator` - Create PDFs from markdown (opposite direction)
- `pdf-extractor` - Extract content from PDFs
- `image-processing` - Pre-process images before OCR
