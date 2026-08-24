# Technique Analysis: youtube-downloader

**Resource Type:** Skill
**Category:** Content Creation
**Path:** `skills/content-creation/youtube-downloader/`
**Date Analyzed:** 2025-12-22
**Bundled Resources:** 1 script (download_video.py - 149 lines), 1 reference (po-token-setup.md - 168 lines), 1 other (.security-scan-passed)
**Total Lines:** ~680 lines (362 SKILL.md + 318 bundled)

## Overview

This skill enables reliable video and audio downloads from YouTube and HLS streaming platforms using yt-dlp and ffmpeg. It provides comprehensive workflows for handling protected content, quality selection, and troubleshooting common download failures.

**Core Purpose:** Transform complex, frequently-changing video download workflows into reliable, reproducible procedures with fallback strategies for when primary methods fail.

**Complexity Score:** 4.5/5 (Very high complexity due to multi-path fallback strategies, environment-specific guidance, and external tool dependency management)

---

## Identified Techniques

### Technique 1: Quality Expectation Matrix
- **Category:** OT (Output Techniques)
- **Maps to existing:** NEW - **OT-09: Capability Transparency Matrix**
- **Pattern:** Upfront matrix showing exactly what each method/setup achieves, preventing false expectations
- **Example from resource:**
```markdown
| Setup | 360p | 720p | 1080p | 1440p | 4K |
|-------|------|------|-------|-------|-----|
| No setup (default) | ✗ | ✗ | ✗ | ✗ | ✗ |
| Android client only | ✓ | ✗ | ✗ | ✗ | ✗ |
| **PO token provider** | ✓ | ✓ | ✓ | ✓ | ✓ |
| Browser cookies | ✓ | ✓ | ✓ | ✓ | ✓ |
```
- **Effectiveness:** Users immediately understand tradeoffs before investing time in setup. Prevents frustration from discovering limitations after configuration.
- **Novel aspect:** Matrix shows negative capabilities (what doesn't work) as prominently as positive ones. Most docs only show success cases.

### Technique 2: Fallback Strategy Chain
- **Category:** DS (Domain-Specific - Tool Integration)
- **Maps to existing:** DS-51 (Fallback Strategy) - confirmed and extended
- **Pattern:** Ordered sequence of methods from ideal to acceptable, with clear transition criteria
- **Example from resource:**
```markdown
### Step 1: Install PO Token Provider (One-time Setup)
[Ideal method - full quality access]

## Alternative: Browser Cookies Method
[Fallback if PO token setup is problematic]

### nsig Extraction Failed
**Solution**:
1. Update yt-dlp to latest version
2. Install PO token provider
3. If still failing, use Android client: [fallback command]
```
- **Effectiveness:** Users never get stuck. Each failure point has next-best alternative. Clear "when to use which" guidance.

### Technique 3: Verification-Driven Workflow
- **Category:** QA (Quality Assurance)
- **Maps to existing:** QA-01 (Self-Verification) - extended with domain-specific checks
- **Pattern:** Check → Execute → Verify cycle at each stage
- **Example from resource:**
```markdown
### 1. Verify yt-dlp Installation
```bash
which yt-dlp
yt-dlp --version
```

### 2. Check Current Quality Access
```bash
yt-dlp -F "https://youtu.be/VIDEO_ID"
```
**If only format 18 (360p) appears**: PO token provider setup needed

### Step 3: Verify Download Quality
```bash
ffprobe -v error -select_streams v:0 -show_entries stream=width,height
```
Expected output for 1080p:
```
width=1920
height=1080
```
```
- **Effectiveness:** Catches problems at earliest possible point. Users confirm prerequisites before attempting complex operations. Verification commands prove success objectively.

### Technique 4: Warning Message Interpretation Guide
- **Category:** DS (Domain-Specific - Troubleshooting)
- **Maps to existing:** NEW - **DS-77: Warning Triage Classification**
- **Pattern:** Classify warnings as actionable vs harmless with explicit guidance
- **Example from resource:**
```markdown
### PO Token Warning (Harmless)

```
WARNING: android client https formats require a GVS PO Token
```

**Action**: Ignore if download succeeds. This indicates Android client
has limited format access without PO tokens.

---

### nsig Extraction Failed

**Symptoms**:
```
WARNING: [youtube] nsig extraction failed: Some formats may be missing
```

**Solution**:
1. Update yt-dlp to latest version
2. Install PO token provider
3. If still failing, use Android client: [command]
```
- **Effectiveness:** Prevents panic over harmless warnings. Users know which warnings require action vs which can be ignored. Saves support time.
- **Novel aspect:** Explicitly labels warnings as "Harmless" vs "Action Required" rather than leaving interpretation to user.

### Technique 5: Environment-Specific Guidance
- **Category:** DS (Domain-Specific - Context-Aware Instructions)
- **Maps to existing:** DS-60 (Environment-Specific Guidance) - confirmed from previous analysis
- **Pattern:** Identify geographic/network contexts requiring special handling
- **Example from resource:**
```markdown
### Slow Downloads or Network Errors

For users in China or behind restrictive proxies:
- Downloads may be slow due to network conditions
- Allow sufficient time for completion
- yt-dlp automatically retries on transient failures
```
- **Effectiveness:** Prevents false bug reports. Users in restricted regions understand slowness is expected, not a tool failure.

### Technique 6: Tool Dependency Resolution Workflow
- **Category:** DS (Domain-Specific - Dependency Management)
- **Maps to existing:** NEW - **DS-78: Isolated Environment Dependency Installation**
- **Pattern:** Identify tool's isolated environment, then install dependencies into that environment
- **Example from resource:**
```markdown
**Step 1: Locate yt-dlp's Python**
```bash
head -1 $(which yt-dlp)
# Output example: #!/opt/homebrew/Cellar/yt-dlp/2025.10.22/libexec/bin/python
```

**Step 2: Install Plugin**
```bash
# For Homebrew-installed yt-dlp (macOS)
/opt/homebrew/Cellar/yt-dlp/$(yt-dlp --version)/libexec/bin/python -m pip install bgutil-ytdlp-pot-provider
```
```
- **Effectiveness:** Solves common plugin installation failures where users install to wrong Python environment. Shows how to inspect shebang to find correct Python.
- **Novel aspect:** Teaches debugging technique (check shebang) rather than just providing command. Users can apply to other tools.

### Technique 7: Command Pattern Library with Inline Documentation
- **Category:** OT (Output Techniques)
- **Maps to existing:** OT-01 (Format Specification) + DS-02 (Metric Specification)
- **Pattern:** Collection of ready-to-use commands with parameter explanations inline
- **Example from resource:**
```markdown
### Convert WebM to MP4

```bash
ffmpeg -i "video.webm" -c:v libx264 -preset medium -crf 23 -c:a aac -b:a 128k "video.mp4"
```

**Parameters explained:**
- `-c:v libx264`: Use H.264 video codec (widely compatible)
- `-preset medium`: Balance between encoding speed and file size
- `-crf 23`: Constant Rate Factor for quality (18-28 range, lower = better quality)
- `-c:a aac`: Use AAC audio codec
- `-b:a 128k`: Audio bitrate 128 kbps

**Tip**: Conversion maintains 1080p resolution and provides ~6x encoding speed on modern hardware.
```
- **Effectiveness:** Users understand what each flag does, enabling customization. Performance expectations (6x encoding speed) prevent premature termination.

### Technique 8: Problem-Symptom-Solution Mapping
- **Category:** DS (Domain-Specific - Troubleshooting)
- **Maps to existing:** DS-03 (Error Pattern Recognition) - extended with symptom matching
- **Pattern:** Structured troubleshooting entries with symptoms, cause, and ordered solutions
- **Example from resource:**
```markdown
### nsig Extraction Failed

**Symptoms**:
```
WARNING: [youtube] nsig extraction failed: Some formats may be missing
```

**Solution**:
1. Update yt-dlp to latest version
2. Install PO token provider
3. If still failing, use Android client: `yt-dlp --extractor-args "youtube:player_client=android" "VIDEO_URL"`
```
- **Effectiveness:** Users match their error message to symptom, immediately get relevant solutions. Ordered solutions (1,2,3) provide escalation path.

### Technique 9: Bundled Wrapper Script with Automatic Workarounds
- **Category:** DS (Domain-Specific - Tool Integration)
- **Maps to existing:** IT-14 (Resource Bundling) + AG-19 (Production App as Skill)
- **Pattern:** Python wrapper that applies common workarounds by default
- **Example from resource:**
```python
def download_video(..., use_android_client: bool = True, ...):
    # Build yt-dlp command
    cmd = ["yt-dlp"]

    # Use Android client by default to avoid nsig extraction issues
    if use_android_client:
        cmd.extend(["--extractor-args", "youtube:player_client=android"])
```
- **Effectiveness:** Common workarounds applied automatically. Users don't need to remember complex flags. Script encodes institutional knowledge.

### Technique 10: Progressive Complexity Disclosure
- **Category:** IT (Interaction Techniques)
- **Maps to existing:** IT-01 (Progressive Disclosure) - domain-specific application
- **Pattern:** Start with basic YouTube downloads, then add HLS streams, then protected content
- **Example from resource:**
```markdown
## High-Quality Download Workflow
[Basic YouTube downloads]

## Common Tasks
[Audio extraction, subtitles, playlists]

## HLS Stream Downloads (m3u8)
[Advanced: streaming platforms with authentication]

### Handling Separate Audio/Video Streams
[Most advanced: manual stream merging]
```
- **Effectiveness:** Users don't get overwhelmed by HLS complexity when they just need basic YouTube downloads. Advanced users can find deep content.

### Technique 11: Critical Information Highlighting
- **Category:** ST (Structural Techniques)
- **Maps to existing:** NEW - **ST-32: Criticality Labeling**
- **Pattern:** Mark critical information with **Bold** prefix indicators
- **Example from resource:**
```markdown
**Critical**: Outdated yt-dlp versions cause nsig extraction failures and missing formats.

**Verification**: Run `yt-dlp -F "VIDEO_URL"` again. Look for formats 137 (1080p), 271 (1440p), or 313 (4K).

**Cause**: Missing or incorrect authentication headers.

**Benefits**: Access to age-restricted and members-only content.
**Requirement**: Must be logged into YouTube in the specified browser.
```
- **Effectiveness:** Users scan for bold keywords (Critical, Verification, Cause, Benefits, Requirement) to quickly identify information type.
- **Novel aspect:** Semantic prefixes rather than generic bold. "Critical" means "will fail if ignored," "Verification" means "how to confirm success."

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: Capability Transparency Matrix (OT-09)
- **Description:** Matrix showing exactly what each configuration achieves and doesn't achieve, displayed upfront
- **Implementation:**
  - Create table with configurations as rows, capabilities as columns
  - Use ✓ for supported, ✗ for unsupported
  - Highlight recommended approach with **bold**
  - Place matrix before detailed setup instructions
- **Use case:** Tool configuration, API tier comparison, feature availability by plan, browser compatibility
- **Example:**
```markdown
## Browser Compatibility Matrix

| Feature | Chrome | Firefox | Safari | Edge |
|---------|--------|---------|--------|------|
| File upload | ✓ | ✓ | ✓ | ✓ |
| Drag & drop | ✓ | ✓ | ✗ | ✓ |
| WebRTC | ✓ | ✓ | ⚠️ Limited | ✓ |
| **Recommended** | ✓ | ✓ | | ✓ |

**Legend:**
- ✓ Full support
- ⚠️ Partial support (see notes)
- ✗ Not supported
```
- **Proposed category:** OT (Output Techniques)
- **Proposed code:** OT-09

**Why this is novel:** Existing techniques show success paths but rarely document limitations upfront. This matrix prevents disappointment by setting accurate expectations before users invest time.

### Pattern 2: Warning Triage Classification (DS-77)
- **Description:** Classify warning messages as "Harmless" vs "Action Required" with explicit ignore/act guidance
- **Implementation:**
  - Create "Troubleshooting" section with subsections per warning
  - Label each warning as "Harmless" or priority level
  - For harmless warnings: "**Action**: Ignore if [success condition]"
  - For actionable warnings: "**Solution**: [ordered steps]"
  - Show exact warning text so users can pattern-match
- **Use case:** CLI tool documentation, API error handling guides, build system troubleshooting, deployment runbooks
- **Example:**
```markdown
## Warning Messages

### "deprecation warning: oldMethod() will be removed" (Harmless)

**Example:**
```
DeprecationWarning: oldMethod() is deprecated, use newMethod() instead
```

**Action**: Ignore for now. Your code will continue working until version 3.0.
Schedule migration before upgrading to 3.0.

---

### "connection refused on port 8080" (Action Required)

**Example:**
```
Error: Connection refused on localhost:8080
```

**Solution**:
1. Check if service is running: `systemctl status myservice`
2. Verify port not in use: `lsof -i :8080`
3. Check firewall rules: `sudo iptables -L`
```
- **Proposed category:** DS (Domain-Specific - Troubleshooting)
- **Proposed code:** DS-77

**Why this is novel:** Documentation rarely explicitly labels warnings as safe to ignore. Users assume all warnings require action, creating unnecessary support load. This pattern provides triage framework.

### Pattern 3: Isolated Environment Dependency Installation (DS-78)
- **Description:** Workflow to identify tool's isolated environment (venv, Homebrew Cellar, etc.) and install dependencies into that environment
- **Implementation:**
  - Step 1: Show how to inspect tool to find its Python/environment (check shebang, check PATH)
  - Step 2: Use that environment's package manager to install dependency
  - Include path inspection commands that work across different installation methods
  - Show both Homebrew and pip installation patterns
- **Use case:** Plugin installation for CLI tools, system tool extension, debugging "module not found" errors
- **Example:**
```markdown
## Installing Plugins

Many tools use isolated Python environments. Install plugins into the tool's environment, not your global Python.

### Step 1: Find the tool's Python

```bash
# Check the shebang line
head -1 $(which tool-name)
# Example output: #!/opt/homebrew/Cellar/tool-name/1.2.3/libexec/bin/python
```

### Step 2: Install to that Python

```bash
# Use the tool's Python directly
/opt/homebrew/Cellar/tool-name/$(tool-name --version)/libexec/bin/python -m pip install plugin-name

# Or for pip-installed tools
python3 -m pip install plugin-name --user
```

### Verification

```bash
tool-name --list-plugins
# Should show newly installed plugin
```
```
- **Proposed category:** DS (Domain-Specific - Dependency Management)
- **Proposed code:** DS-78

**Why this is novel:** Most docs say "install the plugin" without addressing environment isolation. This teaches debugging technique (inspect shebang) that users can apply to any tool.

### Pattern 4: Criticality Labeling (ST-32)
- **Description:** Use semantic bold prefixes to label information type: **Critical**, **Verification**, **Cause**, **Benefits**, **Requirement**
- **Implementation:**
  - **Critical**: Information that causes failure if ignored
  - **Verification**: Commands/checks to confirm success
  - **Cause**: Root cause explanation for errors
  - **Benefits**: Advantages of choosing this approach
  - **Requirement**: Prerequisites that must be met
  - **Tip**: Optional optimization or convenience
- **Use case:** Technical documentation, troubleshooting guides, installation instructions, API references
- **Example:**
```markdown
## Setup

**Critical**: Update to version 2.0+ before proceeding. Version 1.x has security vulnerability CVE-2024-1234.

**Requirement**: Python 3.8 or higher. Check with `python3 --version`

**Verification**: Run `tool --check-config` to confirm setup is correct.

**Tip**: Add `alias t='tool'` to your shell config for convenience.
```
- **Proposed category:** ST (Structural Techniques)
- **Proposed code:** ST-32

**Why this is novel:** Generic bold text doesn't convey semantic meaning. These prefixes create scannable structure where users quickly identify critical info vs nice-to-have.

---

## Multi-Technique Combinations

### Complete Download Workflow
This skill combines techniques into a fail-safe download process:

1. **Environment Check Phase:**
   - QA-01 (Verification): Check yt-dlp installation and version
   - DS-78 (Dependency Resolution): Install PO token provider to correct environment
   - OT-09 (Capability Matrix): Show what each setup achieves

2. **Pre-Download Phase:**
   - QA-01 (Verification): Check available formats with `-F` flag
   - DS-77 (Warning Triage): Interpret format list warnings
   - ST-32 (Criticality Labeling): Highlight critical quality limitations

3. **Download Phase:**
   - DS-51 (Fallback Strategy): PO token → Browser cookies → Android client
   - OT-01 (Command Library): Provide ready-to-use commands
   - IT-14 (Bundled Script): Automatic workaround application

4. **Post-Download Phase:**
   - QA-01 (Verification): Verify quality with ffprobe
   - OT-01 (Command Library): Provide conversion commands if needed
   - DS-60 (Environment-Specific): Set expectations for slow networks

5. **Troubleshooting Phase:**
   - DS-03 (Problem-Symptom-Solution): Match error to solution
   - DS-77 (Warning Triage): Classify warnings as harmless or actionable
   - DS-51 (Fallback Strategy): Try next-best method

**Effectiveness:** No single point of failure. Each failed step has verification command and fallback path. Users never get stuck without next action.

---

## Integration Notes

### For MASTER_TECHNIQUE_INDEX.md
Recommend adding 4 new techniques:
1. **OT-09: Capability Transparency Matrix** - High priority for any comparison documentation
2. **DS-77: Warning Triage Classification** - High priority for troubleshooting guides
3. **DS-78: Isolated Environment Dependency Installation** - Medium priority for plugin/extension docs
4. **ST-32: Criticality Labeling** - Medium priority for technical documentation

### For USE_CASE_LOOKUP.md
Add to "Tool Integration & Troubleshooting" use case:
- OT-09: When documenting configuration options or API tiers
- DS-77: When creating troubleshooting guides for tools with verbose output
- DS-78: When documenting plugin installation for CLI tools
- ST-32: When writing installation or setup documentation

### For AI_AGENT_QUICK_START.md
Reference this skill as example of:
- Failsafe workflow design (multiple fallback paths)
- Capability transparency (showing what doesn't work)
- Warning message interpretation for tools with noisy output

### Cross-References
- **Similar to:** cloudflare-troubleshooting (problem-symptom-solution mapping), statusline-generator (environment detection)
- **Complements:** transcript-fixer (production app with bundled scripts), video-comparer (ffmpeg usage patterns)
- **Extends:** Standard CLI documentation with fallback strategies and warning triage

---

## Statistical Summary

- **Novel Techniques Identified:** 4
- **Existing Techniques Referenced:** 7
- **Fallback Methods:** 3 (PO token → Browser cookies → Android client)
- **Quality Levels Supported:** 5 (360p, 720p, 1080p, 1440p, 4K)
- **Bundled Knowledge:** 680 lines (362 SKILL.md + 149 script + 168 reference + 1 security marker)
- **Troubleshooting Scenarios:** 9 distinct problems with solutions
- **Command Patterns:** 20+ ready-to-use commands

---

## Key Insights

1. **Capability Transparency Builds Trust:** Showing limitations upfront (what doesn't work) prevents frustration and builds realistic expectations. Users appreciate honesty about tool constraints.

2. **Fallback Strategies Prevent Abandonment:** Multiple paths to success (PO token → cookies → Android client) mean users never hit dead ends. Each failure has documented next step.

3. **Warning Triage Reduces Support Load:** Explicitly labeling warnings as "Harmless" vs "Action Required" prevents unnecessary panic and support tickets. Users learn to distinguish noise from signal.

4. **Environment Isolation Teaching:** Rather than just providing commands, teaching how to inspect tool environments (check shebang) gives users debugging skills applicable to any tool.

5. **Verification Commands Prove Success:** Objective verification (check formats, check resolution) removes ambiguity. Users know definitively whether setup succeeded.

6. **Command Libraries with Inline Docs:** Providing ready-to-use commands with parameter explanations enables both copy-paste usage and customization. Users learn by example.

7. **Semantic Bold Prefixes Create Scannability:** Labels like **Critical**, **Verification**, **Tip** let users quickly scan for information type, improving documentation usability.
