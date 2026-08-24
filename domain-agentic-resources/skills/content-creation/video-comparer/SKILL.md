---
name: video-comparer
description: This skill should be used when comparing two videos to analyze compression results or quality differences. Generates interactive HTML reports with quality metrics (PSNR, SSIM) and frame-by-frame visual comparisons. Triggers when users mention "compare videos", "video quality", "compression analysis", "before/after compression", or request quality assessment of compressed videos.
metadata:
  tags:
    - video-comparison
    - compression-analysis
    - psnr
    - ssim
    - ffmpeg
    - quality-metrics
  updated: "2026-04-11"
---
# Video Comparer

## Overview

Compare two videos and generate an interactive HTML report analyzing compression results. The script extracts video metadata, calculates quality metrics (PSNR, SSIM), and creates frame-by-frame visual comparisons with three viewing modes: slider, side-by-side, and grid.

## When to Use This Skill

Use this skill when:
- Comparing original and compressed videos
- Analyzing video compression quality and efficiency
- Evaluating codec performance or bitrate reduction impact
- Users mention "compare videos", "video quality", "compression analysis", or "before/after compression"

## Core Usage

### Basic Command

```bash
python3 scripts/compare.py original.mp4 compressed.mp4
```

Generates `comparison.html` with:
- Video parameters (codec, resolution, bitrate, duration, file size)
- Quality metrics (PSNR, SSIM, size/bitrate reduction percentages)
- Frame-by-frame comparison (default: frames at 5s intervals)

### Command Options

```bash
# Custom output file
python3 scripts/compare.py original.mp4 compressed.mp4 -o report.html

# Custom frame interval (larger = fewer frames, faster processing)
python3 scripts/compare.py original.mp4 compressed.mp4 --interval 10

# Batch comparison
for original in originals/*.mp4; do
    compressed="compressed/$(basename "$original")"
    output="reports/$(basename "$original" .mp4).html"
    python3 scripts/compare.py "$original" "$compressed" -o "$output"
done
```

## Requirements

### System Dependencies

**FFmpeg and FFprobe** (required for video analysis and frame extraction):

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
# Or use: winget install ffmpeg
```

**Python 3.8+** (uses type hints, f-strings, pathlib)

### Video Specifications

- **Supported formats:** `.mp4` (recommended), `.mov`, `.avi`, `.mkv`, `.webm`
- **File size limit:** 500MB per video (configurable)
- **Processing time:** ~1-2 minutes for typical videos; varies by duration and frame interval

## Script Behavior

### Automatic Validation

The script automatically validates:
- FFmpeg/FFprobe installation and availability
- File existence, extensions, and size limits
- Path security (prevents directory traversal)

Clear error messages with resolution guidance appear when validation fails.

### Quality Metrics

The script calculates two standard quality metrics:

**PSNR (Peak Signal-to-Noise Ratio):** Pixel-level similarity measurement (20-50 dB scale, higher is better)

**SSIM (Structural Similarity Index):** Perceptual similarity measurement (0.0-1.0 scale, higher is better)

For detailed interpretation scales and quality thresholds, consult `references/video_metrics.md`.

### Frame Extraction

The script extracts frames at specified intervals (default: 5 seconds), scales them to consistent height (800px) for comparison, and embeds them as base64 data URLs in self-contained HTML. Temporary files are automatically cleaned after processing.

### Output Report

The generated HTML report includes:
- **Slider Mode**: Drag to reveal original vs compressed (default)
- **Side-by-Side Mode**: Simultaneous display for direct comparison
- **Grid Mode**: Compact 2-column layout
- **Zoom Controls**: 50%-200% magnification
- Self-contained format (no server required, works offline)

## Important Implementation Details

### Security

The script implements:
- Path validation (absolute paths, prevents directory traversal)
- Command injection prevention (no `shell=True`, validated arguments)
- Resource limits (file size, timeouts)
- Custom exceptions: `ValidationError`, `FFmpegError`, `VideoComparisonError`

### Common Error Scenarios

**"FFmpeg not found"**: Install FFmpeg via platform package manager (see Requirements section)

**"File too large"**: Compress videos before comparison, or adjust `MAX_FILE_SIZE_MB` in `scripts/compare.py`

**"Operation timed out"**: Increase `FFMPEG_TIMEOUT` constant or use larger `--interval` value (processes fewer frames)

**"Frame count mismatch"**: Videos have different durations/frame rates; script auto-truncates to minimum frame count and shows warning

## Configuration

The script includes adjustable constants for file size limits, timeouts, frame dimensions, and extraction intervals. To customize behavior, edit the constants at the top of `scripts/compare.py`. For detailed configuration options and their impacts, consult `references/configuration.md`.

## Reference Materials

Consult these files for detailed information:
- **`references/video_metrics.md`**: Quality metrics interpretation (PSNR/SSIM scales, compression targets, bitrate guidelines)
- **`references/ffmpeg_commands.md`**: FFmpeg command reference (metadata extraction, frame extraction, troubleshooting)
- **`references/configuration.md`**: Script configuration options and adjustable constants
- **`assets/template.html`**: HTML report template for customizing viewing modes and styling

---

## Core Concepts

### Perceptual Quality vs Mathematical Metrics

Video quality assessment involves two fundamentally different approaches:

- **Objective metrics** (PSNR, SSIM) measure mathematical differences between pixel values. They are fast, reproducible, and automatable -- but they do not always correlate with what humans perceive as "good quality."
- **Perceptual quality** is what a human viewer actually experiences. A video can have low PSNR but look fine to most viewers (e.g., slight noise reduction), or high PSNR but visible artifacts in perceptually important areas (e.g., faces, text).

**Rule of thumb:** Use objective metrics for automated pipelines and regression testing. Use visual frame comparison (slider mode in the HTML report) for final quality sign-off.

### Rate-Distortion Theory

Rate-distortion theory describes the fundamental trade-off in video compression:

```
Higher Bitrate  ->  Higher Quality  ->  Larger File Size
Lower Bitrate   ->  Lower Quality   ->  Smaller File Size
```

The goal of compression analysis is to find the "knee" of the rate-distortion curve -- the point where further bitrate reduction causes disproportionate quality loss. This skill helps identify that point by quantifying quality at each compression level.

**Key terms:**
- **Bitrate** - Data rate of the video stream (measured in kbps or Mbps)
- **CRF (Constant Rate Factor)** - Quality-based encoding parameter (lower = better quality, larger file)
- **QP (Quantization Parameter)** - How aggressively the codec discards information
- **Rate-distortion optimization** - The encoder's internal process of balancing quality vs size

### Quality Metric Interpretation

| Metric | Excellent | Good | Acceptable | Poor |
|--------|-----------|------|------------|------|
| **PSNR** | > 40 dB | 35-40 dB | 30-35 dB | < 30 dB |
| **SSIM** | > 0.97 | 0.93-0.97 | 0.85-0.93 | < 0.85 |
| **File size reduction** | < 30% | 30-60% | 60-80% | > 80% |

Note: These thresholds are content-dependent. Animation tolerates lower PSNR better than live action. Fast motion tolerates more compression than static scenes with fine detail.

---

## Advanced Comparison Workflows

### Multi-Codec Benchmarking

Compare the same source encoded with multiple codecs to find the best option:

```bash
#!/bin/bash
source="original.mp4"
mkdir -p reports

# Encode with different codecs at similar visual quality
ffmpeg -i "$source" -c:v libx264 -crf 23 -preset medium h264_crf23.mp4
ffmpeg -i "$source" -c:v libx265 -crf 28 -preset medium h265_crf28.mp4
ffmpeg -i "$source" -c:v libsvtav1 -crf 35 -preset 6 av1_crf35.mp4
ffmpeg -i "$source" -c:v libvpx-vp9 -crf 32 -b:v 0 vp9_crf32.mp4

# Generate comparison reports for each
for encoded in h264_crf23.mp4 h265_crf28.mp4 av1_crf35.mp4 vp9_crf32.mp4; do
  name=$(basename "$encoded" .mp4)
  python3 scripts/compare.py "$source" "$encoded" -o "reports/${name}.html"
done
```

### ABR (Adaptive Bitrate) Ladder Analysis

Evaluate quality across an entire ABR ladder for streaming:

```bash
#!/bin/bash
source="original.mp4"
mkdir -p ladder reports

# Common ABR ladder rungs
declare -A ladder_rungs=(
  ["1080p_5000k"]="1920:1080:5000k"
  ["720p_3000k"]="1280:720:3000k"
  ["480p_1500k"]="854:480:1500k"
  ["360p_800k"]="640:360:800k"
  ["240p_400k"]="426:240:400k"
)

for rung in "${!ladder_rungs[@]}"; do
  IFS=: read -r w h br <<< "${ladder_rungs[$rung]}"
  ffmpeg -i "$source" -vf "scale=${w}:${h}" -c:v libx264 -b:v "$br" \
    -preset medium "ladder/${rung}.mp4"
  # Compare each rung against a scaled-down version of the original
  ffmpeg -i "$source" -vf "scale=${w}:${h}" -c:v libx264 -crf 0 "ladder/${rung}_ref.mp4"
  python3 scripts/compare.py "ladder/${rung}_ref.mp4" "ladder/${rung}.mp4" \
    -o "reports/${rung}.html"
done
```

### Scene-Based Quality Analysis

Different scenes in a video may compress very differently. Extract quality metrics per scene:

```bash
# Detect scene changes
ffmpeg -i original.mp4 -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2>&1 \
  | grep showinfo | awk -F'pts_time:' '{print $2}' | awk '{print $1}' > scenes.txt

# Compare frames at each scene boundary (high-information moments)
while IFS= read -r timestamp; do
  python3 scripts/compare.py original.mp4 compressed.mp4 \
    --timestamp "$timestamp" -o "reports/scene_${timestamp}.html"
done < scenes.txt
```

---

## Codec-Specific Guidance

### H.264 (AVC)

- **Best for:** Maximum compatibility, real-time encoding, legacy device support
- **CRF range:** 18 (visually lossless) to 28 (noticeable compression)
- **Recommended CRF:** 23 for general use, 18-20 for archival
- **Presets:** `ultrafast` to `veryslow` -- use `medium` for balanced speed/quality
- **Key flags:** `-c:v libx264 -crf 23 -preset medium -profile:v high -level 4.1`

### H.265 (HEVC)

- **Best for:** 30-50% bitrate savings over H.264 at equivalent quality
- **CRF range:** 22 (visually lossless) to 32 (noticeable compression)
- **Recommended CRF:** 28 for general use (roughly equivalent to H.264 CRF 23)
- **Trade-off:** 2-5x slower encoding than H.264
- **Key flags:** `-c:v libx265 -crf 28 -preset medium`
- **Gotcha:** Patent licensing costs may apply for commercial distribution

### AV1

- **Best for:** Maximum compression efficiency, royalty-free distribution
- **CRF range:** 25 (visually lossless) to 45 (noticeable compression)
- **Recommended CRF:** 35 for general use (roughly equivalent to H.264 CRF 23)
- **Trade-off:** 5-20x slower encoding than H.264; decoding requires modern hardware
- **Key flags (SVT-AV1):** `-c:v libsvtav1 -crf 35 -preset 6`
- **Key flags (libaom):** `-c:v libaom-av1 -crf 35 -cpu-used 4 -row-mt 1`

### VP9

- **Best for:** Web delivery (YouTube, WebRTC), royalty-free alternative to H.265
- **CRF range:** 25 (high quality) to 40 (noticeable compression)
- **Recommended CRF:** 32 for general use
- **Trade-off:** Slower encoding than H.264; better than AV1 encoding speed
- **Key flags:** `-c:v libvpx-vp9 -crf 32 -b:v 0 -row-mt 1`

### Codec Comparison Summary

| Codec | Efficiency | Encode Speed | Decode Compat | Royalty |
|-------|-----------|-------------|---------------|---------|
| H.264 | Baseline | Fast | Universal | Licensed |
| H.265 | +30-50% | Slow | Good | Licensed |
| AV1 | +40-60% | Very slow | Growing | Free |
| VP9 | +30-40% | Moderate | Good (web) | Free |

---

## Best Practices for Compression Quality Evaluation

### Systematic Evaluation Process

1. **Establish baseline** - Always compare against the original uncompressed source
2. **Control variables** - Change one parameter at a time (codec, CRF, preset, resolution)
3. **Test representative content** - Include both easy (static) and hard (motion, detail) scenes
4. **Use both metrics and visual inspection** - Numbers catch regressions; eyes catch perceptual issues
5. **Document your findings** - Save comparison reports for future reference

### What to Look For in Visual Comparison

| Artifact Type | Where to Look | Cause |
|--------------|---------------|-------|
| **Blocking** | Flat areas, gradients, sky | QP too high, bitrate too low |
| **Banding** | Gradients, shadows | Color depth reduction, low bitrate |
| **Ringing** | Sharp edges, text overlays | Quantization of high-frequency detail |
| **Mosquito noise** | Around text, high-contrast edges | Temporal prediction errors |
| **Blur/softness** | Fine detail, hair, foliage | Aggressive quantization or denoising |
| **Color shift** | Skin tones, brand colors | Chroma subsampling artifacts |

### When to Accept vs Reject Compression

```
Accept when:
  SSIM > 0.95 AND no visible artifacts in slider mode
  File size reduction meets target (e.g., 50%+)
  No artifacts on text, faces, or brand elements

Reject when:
  Visible blocking or banding in any frame
  Text becomes unreadable at target resolution
  SSIM < 0.90 (almost always perceptible)
  Color shift on skin tones or brand colors
```

---

## Common Pitfalls

| Pitfall | Symptom | Solution |
|---------|---------|----------|
| Comparing different resolutions | Misleadingly low PSNR/SSIM | Scale both videos to the same resolution before comparison |
| Ignoring temporal artifacts | Metrics look fine but video stutters | Watch the video, not just static frames; check for frame drops |
| Trusting PSNR alone | High PSNR but visible artifacts | Always pair PSNR with SSIM and visual inspection |
| Comparing re-encoded to re-encoded | Generation loss masks true quality | Always compare against the original source, not an intermediate |
| Wrong frame alignment | Frames are offset, metrics are meaningless | Verify both videos start at the same point; check for A/V sync |
| Testing only easy scenes | Good metrics but artifacts in complex scenes | Include high-motion, low-light, and detail-heavy test segments |
| Ignoring color space differences | Subtle color shifts between original and compressed | Ensure both videos use the same color space (bt709, bt601, etc.) |
| File size as sole quality metric | Small file but unwatchable | Size reduction without quality assessment is meaningless |

---

## Template: Standard Comparison Report Format

Use this template when documenting compression analysis results:

```markdown
# Video Compression Analysis Report

**Date:** [YYYY-MM-DD]
**Analyst:** [Name]
**Source file:** [filename, resolution, duration, codec, bitrate, file size]

## Test Matrix

| Variant | Codec | CRF/Bitrate | Preset | Resolution | File Size | Reduction |
|---------|-------|-------------|--------|------------|-----------|-----------|
| Original | [codec] | N/A | N/A | [res] | [size] | - |
| Variant A | H.264 | CRF 23 | medium | [res] | [size] | [%] |
| Variant B | H.265 | CRF 28 | medium | [res] | [size] | [%] |
| Variant C | AV1 | CRF 35 | preset 6 | [res] | [size] | [%] |

## Quality Metrics

| Variant | PSNR (dB) | SSIM | Visual Assessment |
|---------|-----------|------|-------------------|
| Variant A | [value] | [value] | [pass/fail + notes] |
| Variant B | [value] | [value] | [pass/fail + notes] |
| Variant C | [value] | [value] | [pass/fail + notes] |

## Visual Inspection Notes

### Easy scenes (static, well-lit)
- [Notes on quality for each variant]

### Hard scenes (motion, low-light, fine detail)
- [Notes on quality for each variant]

### Critical content (text overlays, faces, brand elements)
- [Notes on quality for each variant]

## Recommendation

**Selected variant:** [Variant X]
**Rationale:** [Why this codec/settings combination was chosen]
**Trade-offs accepted:** [What compromises were made]

## Comparison Reports

- [Link to Variant A HTML report]
- [Link to Variant B HTML report]
- [Link to Variant C HTML report]
```
