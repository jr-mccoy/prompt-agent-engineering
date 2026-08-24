#!/usr/bin/env python3
"""
OCR PDF Converter - Add searchable text layer to scanned PDFs.

Converts image-based PDFs (scanned documents, textbook pages, frozen ink)
into searchable PDFs using Tesseract OCR via ocrmypdf.

Usage:
    python ocr_pdf.py <input.pdf> <output.pdf> [options]
    python ocr_pdf.py scan.pdf output.pdf --language chi_sim
    python ocr_pdf.py document.pdf searchable.pdf --deskew --clean

Options:
    --language LANG    OCR language(s), e.g., eng, chi_sim, eng+fra (default: eng)
    --deskew           Straighten rotated pages
    --clean            Remove specks and noise from scans
    --remove-background Remove background for cleaner output
    --force            Force OCR even if text layer exists
    --fast             Use fast mode (lower quality, faster processing)
    --optimize LEVEL   Optimization level 0-3 (default: 1)
    --output-type TYPE Output type: pdf or pdfa (default: pdf)
    --verbose          Show detailed progress

Requirements:
    pip install ocrmypdf

    System requirements:
    - Tesseract OCR: brew install tesseract (macOS) or apt install tesseract-ocr (Linux)
    - Language packs: brew install tesseract-lang or apt install tesseract-ocr-<lang>

Examples:
    # Basic OCR (English)
    python ocr_pdf.py scanned_book.pdf searchable_book.pdf

    # Chinese textbook
    python ocr_pdf.py textbook.pdf textbook_ocr.pdf --language chi_sim

    # Mixed languages with image cleanup
    python ocr_pdf.py scan.pdf output.pdf --language eng+chi_sim --deskew --clean

    # High quality archival
    python ocr_pdf.py historical.pdf archive.pdf --optimize 0 --output-type pdfa
"""

import argparse
import subprocess
import sys
from pathlib import Path


def check_dependencies() -> tuple[bool, str]:
    """
    Check if required dependencies are installed.

    Returns:
        Tuple of (success, message)
    """
    # Check ocrmypdf
    try:
        result = subprocess.run(
            ["ocrmypdf", "--version"],
            capture_output=True,
            text=True,
            check=True
        )
    except FileNotFoundError:
        return False, "ocrmypdf not found. Install with: pip install ocrmypdf"
    except subprocess.CalledProcessError as e:
        return False, f"ocrmypdf error: {e.stderr}"

    # Check tesseract
    try:
        result = subprocess.run(
            ["tesseract", "--version"],
            capture_output=True,
            text=True,
            check=True
        )
    except FileNotFoundError:
        return False, "Tesseract not found. Install with: brew install tesseract (macOS) or apt install tesseract-ocr (Linux)"
    except subprocess.CalledProcessError as e:
        return False, f"Tesseract error: {e.stderr}"

    return True, "All dependencies found"


def get_available_languages() -> list[str]:
    """
    Get list of available Tesseract languages.

    Returns:
        List of language codes
    """
    try:
        result = subprocess.run(
            ["tesseract", "--list-langs"],
            capture_output=True,
            text=True,
            check=True
        )
        lines = result.stdout.strip().split("\n")
        # Skip the first line (header)
        return [lang.strip() for lang in lines[1:] if lang.strip()]
    except (FileNotFoundError, subprocess.CalledProcessError):
        return []


def validate_language(language: str, available: list[str]) -> tuple[bool, str]:
    """
    Validate that specified language(s) are available.

    Args:
        language: Language code(s), potentially combined with +
        available: List of available language codes

    Returns:
        Tuple of (valid, message)
    """
    if not available:
        return True, "Could not verify languages, proceeding anyway"

    langs = language.split("+")
    missing = [lang for lang in langs if lang not in available]

    if missing:
        return False, f"Language(s) not available: {', '.join(missing)}. Install with: apt install tesseract-ocr-<lang>"

    return True, "Languages available"


def ocr_pdf(
    input_file: Path,
    output_file: Path,
    language: str = "eng",
    deskew: bool = False,
    clean: bool = False,
    remove_background: bool = False,
    force: bool = False,
    fast: bool = False,
    optimize: int = 1,
    output_type: str = "pdf",
    verbose: bool = False
) -> tuple[bool, str]:
    """
    Perform OCR on a PDF file.

    Args:
        input_file: Path to input PDF
        output_file: Path to output PDF
        language: Tesseract language code(s)
        deskew: Straighten rotated pages
        clean: Remove specks and noise
        remove_background: Remove background
        force: Force OCR even if text exists
        fast: Use fast mode
        optimize: Optimization level (0-3)
        output_type: Output type (pdf or pdfa)
        verbose: Show detailed progress

    Returns:
        Tuple of (success, message)
    """
    cmd = ["ocrmypdf"]

    # Language
    cmd.extend(["--language", language])

    # Image processing options
    if deskew:
        cmd.append("--deskew")
    if clean:
        cmd.append("--clean")
    if remove_background:
        cmd.append("--remove-background")

    # OCR behavior
    if force:
        cmd.append("--force-ocr")
    else:
        cmd.append("--skip-text")  # Skip pages that already have text

    if fast:
        cmd.append("--fast-web-view")
        cmd.extend(["--tesseract-timeout", "60"])

    # Output options
    cmd.extend(["--optimize", str(optimize)])
    cmd.extend(["--output-type", output_type])

    # Progress
    if verbose:
        cmd.append("--verbose")
    else:
        cmd.append("--quiet")

    # Input and output files
    cmd.append(str(input_file))
    cmd.append(str(output_file))

    if verbose:
        print(f"Running: {' '.join(cmd)}")

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        return True, f"OCR complete: {output_file}"
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.strip() if e.stderr else str(e)

        # Parse common errors
        if "already has text" in error_msg.lower():
            return False, "PDF already contains text. Use --force to re-OCR."
        elif "language" in error_msg.lower():
            return False, f"Language error: {error_msg}. Check available languages with: tesseract --list-langs"
        else:
            return False, f"OCR failed: {error_msg}"


def get_pdf_info(pdf_path: Path) -> dict:
    """
    Get basic information about a PDF file.

    Args:
        pdf_path: Path to PDF file

    Returns:
        Dictionary with PDF information
    """
    info = {
        "file": str(pdf_path),
        "size_mb": round(pdf_path.stat().st_size / (1024 * 1024), 2)
    }

    # Try to get page count using pdfinfo if available
    try:
        result = subprocess.run(
            ["pdfinfo", str(pdf_path)],
            capture_output=True,
            text=True,
            check=True
        )
        for line in result.stdout.split("\n"):
            if line.startswith("Pages:"):
                info["pages"] = int(line.split(":")[1].strip())
                break
    except (FileNotFoundError, subprocess.CalledProcessError, ValueError):
        pass

    return info


def main():
    parser = argparse.ArgumentParser(
        description="Add searchable text layer to scanned PDFs using OCR",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s scan.pdf output.pdf
  %(prog)s textbook.pdf output.pdf --language chi_sim
  %(prog)s document.pdf output.pdf --deskew --clean
  %(prog)s scan.pdf output.pdf --language eng+fra --optimize 0
        """
    )

    parser.add_argument("input_pdf", help="Path to input PDF file")
    parser.add_argument("output_pdf", help="Path to output PDF file")

    parser.add_argument(
        "--language", "-l",
        default="eng",
        help="OCR language(s), e.g., eng, chi_sim, eng+fra (default: eng)"
    )

    parser.add_argument(
        "--deskew",
        action="store_true",
        help="Straighten rotated pages"
    )

    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove specks and noise from scans"
    )

    parser.add_argument(
        "--remove-background",
        action="store_true",
        help="Remove background for cleaner output"
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Force OCR even if text layer already exists"
    )

    parser.add_argument(
        "--fast",
        action="store_true",
        help="Use fast mode (lower quality, faster processing)"
    )

    parser.add_argument(
        "--optimize",
        type=int,
        choices=[0, 1, 2, 3],
        default=1,
        help="Optimization level 0-3 (default: 1)"
    )

    parser.add_argument(
        "--output-type",
        choices=["pdf", "pdfa"],
        default="pdf",
        help="Output type: pdf or pdfa (default: pdf)"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed progress"
    )

    args = parser.parse_args()

    # Validate input file
    input_path = Path(args.input_pdf)
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)

    if not input_path.suffix.lower() == ".pdf":
        print(f"Error: Input file must be a PDF: {input_path}")
        sys.exit(1)

    output_path = Path(args.output_pdf)

    # Check dependencies
    deps_ok, deps_msg = check_dependencies()
    if not deps_ok:
        print(f"Error: {deps_msg}")
        sys.exit(1)

    # Validate language
    available_langs = get_available_languages()
    lang_ok, lang_msg = validate_language(args.language, available_langs)
    if not lang_ok:
        print(f"Error: {lang_msg}")
        sys.exit(1)

    # Get input file info
    if args.verbose:
        info = get_pdf_info(input_path)
        print(f"Processing: {info['file']}")
        if "pages" in info:
            print(f"Pages: {info['pages']}")
        print(f"Size: {info['size_mb']} MB")
        print(f"Language: {args.language}")
    else:
        print(f"Processing: {input_path.name}")

    # Perform OCR
    success, message = ocr_pdf(
        input_file=input_path,
        output_file=output_path,
        language=args.language,
        deskew=args.deskew,
        clean=args.clean,
        remove_background=args.remove_background,
        force=args.force,
        fast=args.fast,
        optimize=args.optimize,
        output_type=args.output_type,
        verbose=args.verbose
    )

    if success:
        output_info = get_pdf_info(output_path)
        print(message)
        print(f"Output size: {output_info['size_mb']} MB")
    else:
        print(f"Error: {message}")
        sys.exit(1)


if __name__ == "__main__":
    main()
