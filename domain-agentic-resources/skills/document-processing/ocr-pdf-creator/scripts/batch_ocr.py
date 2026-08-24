#!/usr/bin/env python3
"""
Batch OCR Processor - Process multiple PDFs with OCR.

Converts multiple image-based PDFs to searchable PDFs using Tesseract OCR.
Useful for processing entire directories of scanned documents or textbooks.

Usage:
    python batch_ocr.py <input_dir> --output-dir <output_dir> [options]
    python batch_ocr.py ./scans/ --output-dir ./searchable/
    python batch_ocr.py ./chinese_books/ --output-dir ./ocr/ --language chi_sim

Options:
    --output-dir DIR   Output directory for processed PDFs (required)
    --language LANG    OCR language(s), e.g., eng, chi_sim (default: eng)
    --deskew           Straighten rotated pages
    --clean            Remove specks and noise
    --force            Force OCR even if text layer exists
    --optimize LEVEL   Optimization level 0-3 (default: 1)
    --recursive        Process subdirectories recursively
    --parallel N       Number of parallel processes (default: 1)
    --dry-run          Show what would be processed without doing it

Requirements:
    pip install ocrmypdf

Examples:
    # Process all PDFs in a directory
    python batch_ocr.py ./scanned_docs/ --output-dir ./searchable_docs/

    # Chinese documents with cleaning
    python batch_ocr.py ./chinese/ --output-dir ./ocr/ --language chi_sim --clean

    # Recursive processing with parallelization
    python batch_ocr.py ./library/ --output-dir ./processed/ --recursive --parallel 4

    # Preview what would be processed
    python batch_ocr.py ./scans/ --output-dir ./output/ --dry-run
"""

import argparse
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path


def ocr_single_file(
    input_file: Path,
    output_file: Path,
    language: str,
    deskew: bool,
    clean: bool,
    force: bool,
    optimize: int
) -> tuple[Path, bool, str]:
    """
    Process a single PDF file with OCR.

    Args:
        input_file: Path to input PDF
        output_file: Path to output PDF
        language: Tesseract language code(s)
        deskew: Straighten rotated pages
        clean: Remove specks and noise
        force: Force OCR even if text exists
        optimize: Optimization level

    Returns:
        Tuple of (input_file, success, message)
    """
    cmd = ["ocrmypdf", "--language", language, "--optimize", str(optimize), "--quiet"]

    if deskew:
        cmd.append("--deskew")
    if clean:
        cmd.append("--clean")
    if force:
        cmd.append("--force-ocr")
    else:
        cmd.append("--skip-text")

    cmd.extend([str(input_file), str(output_file)])

    try:
        # Ensure output directory exists
        output_file.parent.mkdir(parents=True, exist_ok=True)

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        return (input_file, True, "OK")
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.strip() if e.stderr else str(e)
        return (input_file, False, error_msg[:100])  # Truncate long errors


def find_pdf_files(input_dir: Path, recursive: bool = False) -> list[Path]:
    """
    Find all PDF files in a directory.

    Args:
        input_dir: Directory to search
        recursive: Search subdirectories

    Returns:
        List of PDF file paths
    """
    if recursive:
        return sorted(input_dir.rglob("*.pdf"))
    else:
        return sorted(input_dir.glob("*.pdf"))


def generate_output_path(
    input_file: Path,
    input_dir: Path,
    output_dir: Path,
    suffix: str = "_ocr"
) -> Path:
    """
    Generate output file path, preserving directory structure.

    Args:
        input_file: Input PDF path
        input_dir: Base input directory
        output_dir: Base output directory
        suffix: Suffix to add to filename (before extension)

    Returns:
        Output file path
    """
    try:
        relative_path = input_file.relative_to(input_dir)
    except ValueError:
        relative_path = Path(input_file.name)

    # Add suffix to filename
    output_name = f"{relative_path.stem}{suffix}{relative_path.suffix}"

    if relative_path.parent != Path("."):
        return output_dir / relative_path.parent / output_name
    else:
        return output_dir / output_name


def format_size(size_bytes: int) -> str:
    """Format file size in human-readable format."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"


def main():
    parser = argparse.ArgumentParser(
        description="Batch process PDFs with OCR",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s ./scans/ --output-dir ./searchable/
  %(prog)s ./docs/ --output-dir ./ocr/ --language chi_sim --clean
  %(prog)s ./library/ --output-dir ./processed/ --recursive --parallel 4
        """
    )

    parser.add_argument(
        "input_dir",
        help="Directory containing PDF files to process"
    )

    parser.add_argument(
        "--output-dir", "-o",
        required=True,
        help="Output directory for processed PDFs"
    )

    parser.add_argument(
        "--language", "-l",
        default="eng",
        help="OCR language(s), e.g., eng, chi_sim (default: eng)"
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
        "--force",
        action="store_true",
        help="Force OCR even if text layer exists"
    )

    parser.add_argument(
        "--optimize",
        type=int,
        choices=[0, 1, 2, 3],
        default=1,
        help="Optimization level 0-3 (default: 1)"
    )

    parser.add_argument(
        "--recursive", "-r",
        action="store_true",
        help="Process subdirectories recursively"
    )

    parser.add_argument(
        "--parallel", "-j",
        type=int,
        default=1,
        help="Number of parallel processes (default: 1)"
    )

    parser.add_argument(
        "--suffix",
        default="_ocr",
        help="Suffix for output filenames (default: _ocr)"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be processed without doing it"
    )

    args = parser.parse_args()

    # Validate input directory
    input_dir = Path(args.input_dir)
    if not input_dir.exists():
        print(f"Error: Input directory not found: {input_dir}")
        sys.exit(1)

    if not input_dir.is_dir():
        print(f"Error: Not a directory: {input_dir}")
        sys.exit(1)

    output_dir = Path(args.output_dir)

    # Find PDF files
    pdf_files = find_pdf_files(input_dir, recursive=args.recursive)

    if not pdf_files:
        print(f"No PDF files found in: {input_dir}")
        sys.exit(0)

    print(f"Found {len(pdf_files)} PDF files")
    print(f"Language: {args.language}")
    print(f"Output directory: {output_dir}")
    print()

    # Generate output paths
    tasks = []
    total_size = 0
    for pdf_file in pdf_files:
        output_file = generate_output_path(pdf_file, input_dir, output_dir, args.suffix)
        tasks.append((pdf_file, output_file))
        total_size += pdf_file.stat().st_size

    print(f"Total input size: {format_size(total_size)}")
    print()

    if args.dry_run:
        print("DRY RUN - Would process:")
        for input_file, output_file in tasks:
            print(f"  {input_file.name} -> {output_file}")
        sys.exit(0)

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Process files
    success_count = 0
    fail_count = 0
    results = []

    if args.parallel > 1:
        # Parallel processing
        with ProcessPoolExecutor(max_workers=args.parallel) as executor:
            futures = {
                executor.submit(
                    ocr_single_file,
                    input_file,
                    output_file,
                    args.language,
                    args.deskew,
                    args.clean,
                    args.force,
                    args.optimize
                ): (input_file, output_file)
                for input_file, output_file in tasks
            }

            for i, future in enumerate(as_completed(futures), 1):
                input_file, success, message = future.result()
                if success:
                    success_count += 1
                    print(f"[{i}/{len(tasks)}] OK: {input_file.name}")
                else:
                    fail_count += 1
                    print(f"[{i}/{len(tasks)}] FAIL: {input_file.name} - {message}")
                results.append((input_file, success, message))
    else:
        # Sequential processing
        for i, (input_file, output_file) in enumerate(tasks, 1):
            print(f"[{i}/{len(tasks)}] Processing: {input_file.name}...", end=" ", flush=True)

            input_file, success, message = ocr_single_file(
                input_file,
                output_file,
                args.language,
                args.deskew,
                args.clean,
                args.force,
                args.optimize
            )

            if success:
                success_count += 1
                print("OK")
            else:
                fail_count += 1
                print(f"FAIL - {message}")
            results.append((input_file, success, message))

    # Summary
    print()
    print("=" * 50)
    print(f"Processed: {len(tasks)} files")
    print(f"Success: {success_count}")
    print(f"Failed: {fail_count}")

    if fail_count > 0:
        print()
        print("Failed files:")
        for input_file, success, message in results:
            if not success:
                print(f"  - {input_file.name}: {message}")
        sys.exit(1)


if __name__ == "__main__":
    main()
