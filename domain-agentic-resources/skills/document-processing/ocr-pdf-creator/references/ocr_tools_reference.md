# OCR Tools Reference

Comprehensive reference for OCR tools, options, and best practices for processing scanned PDFs.

## Tool Comparison

### OCRmyPDF (Recommended)

**What it is:** Command-line tool that adds OCR text layer to existing PDFs while preserving the original visual appearance.

**Why we use it:**
- Preserves original PDF structure and images
- Adds invisible searchable text layer
- Handles multi-page documents efficiently
- Excellent for scanned documents and textbooks

**Installation:**
```bash
# macOS
brew install ocrmypdf tesseract tesseract-lang

# Ubuntu/Debian
sudo apt install ocrmypdf tesseract-ocr

# Python (requires tesseract already installed)
pip install ocrmypdf
```

### Tesseract OCR

**What it is:** The OCR engine that powers OCRmyPDF. Can be used directly for image files.

**Use cases:**
- Direct image-to-text extraction
- Custom OCR pipelines
- Processing individual images

**Direct usage:**
```bash
# Image to text
tesseract image.png output -l eng

# Image to searchable PDF
tesseract image.png output -l eng pdf
```

### Alternative Tools

| Tool | Best For | Limitations |
|------|----------|-------------|
| Adobe Acrobat | Commercial use, GUI | Expensive, closed source |
| ABBYY FineReader | Highest accuracy | Very expensive |
| Google Cloud Vision | Cloud-based, high accuracy | Requires internet, costs per page |
| Amazon Textract | Cloud-based, structured data | Requires AWS account, costs |
| pdfsandwich | Open source alternative | Less maintained |

## OCRmyPDF Detailed Options

### Language Options

**Single language:**
```bash
ocrmypdf -l eng input.pdf output.pdf
```

**Multiple languages (order matters, first is primary):**
```bash
ocrmypdf -l eng+chi_sim input.pdf output.pdf
ocrmypdf -l fra+deu+eng input.pdf output.pdf
```

**Complete language list:**
```bash
tesseract --list-langs
```

### Common Language Codes

| Language | Code | Script | Notes |
|----------|------|--------|-------|
| English | eng | Latin | Default |
| Simplified Chinese | chi_sim | CJK | Mainland China |
| Traditional Chinese | chi_tra | CJK | Taiwan, Hong Kong |
| Japanese | jpn | CJK + Hiragana/Katakana | |
| Korean | kor | Hangul | |
| French | fra | Latin | |
| German | deu | Latin | |
| Spanish | spa | Latin | |
| Russian | rus | Cyrillic | |
| Arabic | ara | Arabic | RTL support |
| Hindi | hin | Devanagari | |

### Image Processing Options

**Deskew (straighten rotated pages):**
```bash
ocrmypdf --deskew input.pdf output.pdf
```
- Automatically detects and corrects page rotation
- Essential for photographed documents
- Adds processing time

**Clean (remove noise):**
```bash
ocrmypdf --clean input.pdf output.pdf
```
- Removes specks and small artifacts
- Improves OCR accuracy on noisy scans
- May affect fine details

**Remove background:**
```bash
ocrmypdf --remove-background input.pdf output.pdf
```
- Whitens page background
- Useful for yellowed or stained documents
- May affect intentional background elements

**Combine cleaning options:**
```bash
ocrmypdf --deskew --clean --remove-background input.pdf output.pdf
```

### Output Options

**Optimization levels:**
```bash
ocrmypdf --optimize 0 input.pdf output.pdf  # No optimization (largest)
ocrmypdf --optimize 1 input.pdf output.pdf  # Light (default)
ocrmypdf --optimize 2 input.pdf output.pdf  # Medium compression
ocrmypdf --optimize 3 input.pdf output.pdf  # Aggressive (smallest)
```

| Level | Size | Quality | Use Case |
|-------|------|---------|----------|
| 0 | Largest | Best | Archival, historical documents |
| 1 | Large | Very good | Default for most uses |
| 2 | Medium | Good | Web distribution |
| 3 | Small | Acceptable | Quick previews, drafts |

**Output type:**
```bash
ocrmypdf --output-type pdf input.pdf output.pdf   # Standard PDF
ocrmypdf --output-type pdfa input.pdf output.pdf  # PDF/A (archival)
```

### OCR Behavior

**Skip pages with existing text (default):**
```bash
ocrmypdf --skip-text input.pdf output.pdf
```

**Force re-OCR all pages:**
```bash
ocrmypdf --force-ocr input.pdf output.pdf
```

**Redo OCR (remove old, add new):**
```bash
ocrmypdf --redo-ocr input.pdf output.pdf
```

### Performance Options

**Fast mode:**
```bash
ocrmypdf --fast-web-view 0 input.pdf output.pdf
```

**Timeout per page (seconds):**
```bash
ocrmypdf --tesseract-timeout 300 input.pdf output.pdf
```

**Parallel processing (for multi-page documents):**
```bash
ocrmypdf --jobs 4 input.pdf output.pdf
```

## Quality Considerations

### Input Quality Requirements

**Minimum resolution:**
- 300 DPI: Recommended minimum for text OCR
- 400 DPI: Better for small text or poor quality scans
- 600 DPI: Optimal for archival and complex documents

**Image issues that reduce OCR accuracy:**
- Low resolution (< 200 DPI)
- Heavy compression artifacts (low-quality JPEG)
- Skewed or rotated pages
- Background patterns or watermarks
- Handwritten text (limited support)
- Complex layouts with multiple columns

### Improving OCR Accuracy

1. **Use appropriate language packs**
   - Always specify correct primary language
   - For mixed-language documents, list primary first

2. **Apply image preprocessing**
   ```bash
   ocrmypdf --deskew --clean input.pdf output.pdf
   ```

3. **Check source quality**
   - Re-scan at higher resolution if possible
   - Use flat, well-lit scanning conditions

4. **Try different optimization levels**
   - Higher optimization may affect OCR quality
   - Use level 0 for maximum accuracy

### Post-Processing Verification

**Check text extraction:**
```bash
# Extract text to verify OCR quality
pdftotext output.pdf -
```

**Verify searchability:**
```bash
# Search for known text
pdfgrep "known phrase" output.pdf
```

## Error Reference

### Common Errors and Solutions

**"Tesseract not found"**
```
Error: tesseract is not installed or not in PATH
```
Solution: Install Tesseract
```bash
brew install tesseract  # macOS
sudo apt install tesseract-ocr  # Linux
```

**"Language not available"**
```
Error: Failed loading language 'chi_sim'
```
Solution: Install language pack
```bash
brew install tesseract-lang  # macOS (all languages)
sudo apt install tesseract-ocr-chi-sim  # Linux (specific)
```

**"Already has text"**
```
Error: PDF already has text that is selectable
```
Solution: Use --force-ocr or --redo-ocr
```bash
ocrmypdf --force-ocr input.pdf output.pdf
```

**"Out of memory"**
```
Error: OCR failed with code -11
```
Solution: Process with lower jobs count
```bash
ocrmypdf --jobs 1 input.pdf output.pdf
```

**"Corrupt or invalid PDF"**
```
Error: Failed to read PDF
```
Solution: Try repairing with ghostscript first
```bash
gs -o repaired.pdf -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress input.pdf
ocrmypdf repaired.pdf output.pdf
```

## Performance Benchmarks

Approximate processing times on modern hardware (4-core CPU):

| Pages | Basic OCR | With Cleaning | With Deskew |
|-------|-----------|---------------|-------------|
| 10 | ~30 sec | ~45 sec | ~1 min |
| 50 | ~2 min | ~3 min | ~4 min |
| 100 | ~4 min | ~6 min | ~8 min |
| 500 | ~20 min | ~30 min | ~40 min |

Factors affecting speed:
- Page complexity (more text = slower)
- Image resolution (higher = slower)
- Language (CJK languages are slower)
- Cleaning/deskewing options (add overhead)
- Optimization level (higher = faster output but slower processing)

## Best Practices Summary

1. **Always verify OCR results** - Spot-check a few pages
2. **Keep original scans** - Never delete originals
3. **Use appropriate language** - Specify correct language for best results
4. **Consider optimization level** - Match to your use case
5. **Batch similar documents** - Use same settings for consistency
6. **Monitor file sizes** - High optimization may affect quality
7. **Document your settings** - For reproducibility
