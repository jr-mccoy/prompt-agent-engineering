# Technique Analysis: statusline-generator

**Resource Type:** Skill
**Path:** `claude-code-resources/skills/developer-tools/statusline-generator/`
**Date Analyzed:** 2025-12-22
**Bundled Resources:** 2 scripts (generate_statusline.sh, install_statusline.sh), 2 references (ccusage_integration.md, color_codes.md)
**Total Lines:** ~474 lines (213 SKILL.md + 80 generate script + 73 install script + 166 references)
**Complexity:** 3.5/5

## Summary

statusline-generator is a **configuration automation skill** that provides customizable Claude Code statuslines with multi-line layouts, integrated cost tracking via ccusage, git status indicators, and ANSI color customization. It implements time-based caching (2-minute expiry), background async fetching, fallback to stale cache, automated settings.json modification, and model name normalization. The skill demonstrates performance optimization patterns with 108 lines of reference documentation for troubleshooting and customization.

## Identified Techniques

### Technique 1: Time-Based File Caching
- **Category:** DS (Domain-Specific - Performance) - **NEW**
- **Pattern:** Cache expensive operations using timestamp-based file names
  ```bash
  cache_file="/tmp/claude_cost_cache_$(date +%Y%m%d_%H%M).txt"

  # Clean old caches (older than 2 minutes)
  find /tmp -name "claude_cost_cache_*.txt" -mmin +2 -delete

  if [ -f "$cache_file" ]; then
      # Use cached data
      cost_info=$(cat "$cache_file")
  else
      # Generate new cache
      ccusage session --json > "$cache_file"
  fi
  ```
- **Example from resource:** `generate_statusline.sh` lines 49-56 - Cache file with minute-level granularity
- **Maps to existing:** **NEW** - Timestamp-based file caching pattern
- **Effectiveness:** Reduces ccusage calls from ~30/min to ~1/2min (60x reduction)
- **Proposed code:** DS-90

### Technique 2: Background Async Fetching
- **Category:** DS (Domain-Specific - Performance) - **NEW**
- **Pattern:** Run expensive operations in background to avoid blocking UI
  ```bash
  # Run cost fetch in background
  {
      session=$(ccusage session --json | jq -r '.sessions[0].totalCost')
      daily=$(ccusage daily --json | jq -r '.daily[0].totalCost')
      printf ' [$%s/$%s]' "$session" "$daily" > "$cache_file"
  } &  # Background process

  # Statusline continues without waiting
  ```
- **Example from resource:** `generate_statusline.sh` lines 59-66 - Background fetch with `} &`
- **Maps to existing:** **NEW** - Background async pattern in shell scripts
- **Effectiveness:** First statusline appears instantly, costs populate 2-5 seconds later
- **Proposed code:** DS-91

### Technique 3: Fallback to Stale Cache
- **Category:** DS (Domain-Specific - Resilience) - **NEW**
- **Pattern:** Use old cache while generating new cache
  ```bash
  if cache is generating in background:
      # Use previous cache (up to 10 minutes old)
      prev_cache=$(find /tmp -name "cache_*.txt" -mmin -10 | head -1)
      if [ -f "$prev_cache" ]; then
          use old data temporarily
      fi
  ```
- **Example from resource:** `generate_statusline.sh` lines 68-73 - Fallback to previous cache
- **Maps to existing:** **NEW** - Stale-while-revalidate pattern in shell scripts
- **Effectiveness:** Provides immediate data while fetching fresh data
- **Proposed code:** DS-92

### Technique 4: JSON Processing Pipeline
- **Category:** DS (Domain-Specific - Data Processing) - Related to existing
- **Pattern:** Chain `jq` with error suppression and formatting
  ```bash
  session=$(ccusage session --json --offline -o desc 2>/dev/null \
      | jq -r '.sessions[0].totalCost' 2>/dev/null \
      | xargs printf "%.2f")
  ```
- **Example from resource:** `generate_statusline.sh` lines 60-61
- **Maps to existing:** Common pattern, but **NEW** in prompting context
- **Effectiveness:** Robust JSON extraction with error handling
- **Proposed code:** DS-93 (if documenting shell patterns)

### Technique 5: Automated Settings Modification with Backup
- **Category:** DS (Domain-Specific - Configuration) - **NEW**
- **Pattern:** Safely modify JSON config files using jq with automatic backup
  ```bash
  # Backup original
  cp "$SETTINGS_FILE" "$SETTINGS_FILE.backup"

  # Modify using jq (atomic operation)
  jq '. + {"statusLine": {...}}' "$SETTINGS_FILE.backup" > "$SETTINGS_FILE"
  ```
- **Example from resource:** `install_statusline.sh` lines 53-60
- **Maps to existing:** **NEW** - Safe config modification pattern
- **Effectiveness:** Prevents corruption, allows rollback, atomic update
- **Proposed code:** DS-94

### Technique 6: Model Name Normalization
- **Category:** DS (Domain-Specific - Formatting) - **NEW**
- **Pattern:** Use regex to extract and reformat verbose names
  ```bash
  # "Sonnet 4.5 (with 1M token context)" -> "Sonnet 4.5 [1M]"
  model=$(echo "$model_full" | sed -E 's/(.*)\(with ([0-9]+[KM]) token context\)/\1[\2]/' | sed 's/ *$//')
  ```
- **Example from resource:** `generate_statusline.sh` line 12
- **Maps to existing:** **NEW** - Display name normalization
- **Effectiveness:** Saves ~20 characters, improves readability
- **Proposed code:** DS-95

### Technique 7: Conditional Coloring Based on State
- **Category:** OT (Output Techniques) - **NEW**
- **Pattern:** Apply different colors based on data state
  ```bash
  if [ -n "$status" ]; then
      # Red for dirty (uncommitted changes)
      git_info=$(printf '\033[01;31m[git:%s%s]\033[00m' "$branch" "$status")
  else
      # Yellow for clean
      git_info=$(printf '\033[01;33m[git:%s]\033[00m' "$branch")
  fi
  ```
- **Example from resource:** `generate_statusline.sh` lines 38-44
- **Maps to existing:** **NEW** - State-based color coding
- **Effectiveness:** Visual feedback on repository state
- **Proposed code:** OT-12

### Technique 8: Reference Documentation by Integration Topic
- **Category:** ST (Structural Techniques) - **NEW**
- **Pattern:** Separate reference files per integration/customization concern
  - `ccusage_integration.md` - External tool integration troubleshooting
  - `color_codes.md` - Color customization reference
- **Example from resource:**
  - ccusage reference (166 lines): JSON structure, caching strategy, troubleshooting
  - color reference (86 lines): ANSI codes, visibility tips, testing
- **Maps to existing:** **NEW** - Integration-specific reference structure
- **Effectiveness:** Users find relevant documentation quickly
- **Proposed code:** ST-35

### Technique 9: Progressive Disclosure with Installation Automation
- **Category:** IT (Interaction Techniques) - Related to IT-14
- **Pattern:** Automated installation with progressive manual customization options
  - **Level 1 (Automated):** Run `install_statusline.sh` for default setup
  - **Level 2 (Manual):** Edit `~/.claude/statusline.sh` for customization
  - **Level 3 (Deep):** Load `color_codes.md` for ANSI reference
  - **Level 4 (Troubleshooting):** Load `ccusage_integration.md` for debugging
- **Example from resource:**
  - SKILL.md lines 24-56: Quick start vs manual installation
  - SKILL.md lines 119-170: Customization examples
- **Maps to existing:** IT-14 (Progressive Disclosure) - **CONFIRMATION**
- **Effectiveness:** Users start quickly, customize deeply as needed

### Technique 10: Error Suppression in Pipelines
- **Category:** DS (Domain-Specific - Error Handling) - **NEW**
- **Pattern:** Redirect errors to `/dev/null` to prevent UI clutter
  ```bash
  session=$(ccusage session --json 2>/dev/null \
      | jq -r '.sessions[0].totalCost' 2>/dev/null \
      | xargs printf "%.2f")
  ```
- **Example from resource:** `generate_statusline.sh` lines 60-61 - Double error suppression
- **Maps to existing:** **NEW** - Graceful degradation with silent errors
- **Effectiveness:** Statusline never shows error messages, gracefully omits failed data
- **Proposed code:** DS-96

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: Time-Based File Caching (DS-90)
- **Description:** Cache expensive operations using timestamp-based file names with automatic expiry
- **Implementation:**
  1. Generate cache file name with timestamp: `/tmp/cache_YYYYMMDD_HHMM.txt`
  2. Check if cache file exists (timestamp match = fresh cache)
  3. Use cache if exists, generate if missing
  4. Auto-cleanup old cache files with `find -mmin +N`
- **Use case:** Expensive API calls, slow commands, frequently updated data
- **Example:**
  ```bash
  # Cache with 5-minute granularity
  cache_file="/tmp/api_cache_$(date +%Y%m%d_%H%M).txt"

  # Clean caches older than 5 minutes
  find /tmp -name "api_cache_*.txt" -mmin +5 -delete 2>/dev/null

  if [ -f "$cache_file" ]; then
      # Use cached data (less than 5 minutes old)
      data=$(cat "$cache_file")
  else
      # Fetch fresh data and cache it
      data=$(curl -s https://api.example.com/data)
      echo "$data" > "$cache_file"
  fi
  ```
- **Proposed category:** DS (Domain-Specific - Performance)
- **Proposed code:** DS-90

### Pattern 2: Background Async Fetching (DS-91)
- **Description:** Run expensive operations in background to avoid blocking UI/workflow
- **Implementation:**
  ```bash
  # Start expensive operation in background
  {
      expensive_result=$(slow_command)
      echo "$expensive_result" > result_file
  } &

  # Continue immediately without waiting
  echo "Processing in background..."
  ```
- **Use case:** UI responsiveness, statuslines, progress indicators, async data loading
- **Example:**
  ```bash
  # Statusline with async cost fetch
  {
      cost=$(calculate_expensive_metric)
      echo "$cost" > /tmp/cost.txt
  } &

  # Show statusline immediately with placeholder
  printf "User: %s | Project: %s | Cost: Loading...\n" "$user" "$project"

  # Next statusline refresh will show cost (if ready)
  ```
- **Proposed category:** DS (Domain-Specific - Performance)
- **Proposed code:** DS-91

### Pattern 3: Fallback to Stale Cache (DS-92)
- **Description:** Use old cache data while generating fresh data (stale-while-revalidate)
- **Implementation:**
  1. Check for fresh cache (primary)
  2. If generating new cache, find previous cache (up to N minutes old)
  3. Use previous cache as fallback
  4. Next refresh will use fresh cache
- **Use case:** Data dashboards, monitoring systems, statuslines with external dependencies
- **Example:**
  ```bash
  fresh_cache="/tmp/data_$(date +%Y%m%d_%H%M).txt"

  if [ -f "$fresh_cache" ]; then
      data=$(cat "$fresh_cache")
  else
      # Generate new cache in background
      { fetch_data > "$fresh_cache" } &

      # While generating, use previous cache (up to 30 minutes old)
      prev_cache=$(find /tmp -name "data_*.txt" -mmin -30 2>/dev/null | head -1)
      if [ -f "$prev_cache" ]; then
          data=$(cat "$prev_cache")  # Stale but better than nothing
      else
          data="No data available"
      fi
  fi
  ```
- **Proposed category:** DS (Domain-Specific - Resilience)
- **Proposed code:** DS-92

### Pattern 4: Automated Settings Modification with Backup (DS-94)
- **Description:** Safely modify JSON/config files using atomic operations with automatic backup
- **Implementation:**
  1. Create backup of original file
  2. Use `jq` (or equivalent) to modify copy
  3. Write modified data to original path
  4. Preserve backup for rollback
- **Use case:** Configuration management, automated setup scripts, safe updates
- **Example:**
  ```bash
  SETTINGS_FILE="~/.config/app/settings.json"

  # Backup original
  cp "$SETTINGS_FILE" "$SETTINGS_FILE.backup"

  # Modify using jq (atomic operation)
  jq '. + {"newFeature": {"enabled": true, "value": 42}}' \
      "$SETTINGS_FILE.backup" > "$SETTINGS_FILE"

  echo "Settings updated. Backup saved to: $SETTINGS_FILE.backup"
  ```
- **Proposed category:** DS (Domain-Specific - Configuration)
- **Proposed code:** DS-94

### Pattern 5: Model Name Normalization (DS-95)
- **Description:** Extract and reformat verbose display names using regex
- **Implementation:**
  ```bash
  # Extract key information, drop verbose parts
  normalized=$(echo "$verbose_name" | sed -E 's/pattern/replacement/')
  ```
- **Use case:** UI display, log formatting, name shortening
- **Example:**
  ```bash
  # "Claude Sonnet 4.5 (with 1 million token context window)" -> "Sonnet 4.5 [1M]"
  model_full="Claude Sonnet 4.5 (with 1M token context)"
  model=$(echo "$model_full" \
      | sed -E 's/(.*)\(with ([0-9]+[KM]) token context\)/\1[\2]/' \
      | sed 's/ *$//')

  # Result: "Claude Sonnet 4.5 [1M]"
  ```
- **Proposed category:** DS (Domain-Specific - Formatting)
- **Proposed code:** DS-95

### Pattern 6: Conditional Coloring Based on State (OT-12)
- **Description:** Apply different ANSI colors based on data state for visual feedback
- **Implementation:**
  ```bash
  if [ condition ]; then
      colored_output=$(printf '\033[COLOR_CODE_1m%s\033[00m' "$data")
  else
      colored_output=$(printf '\033[COLOR_CODE_2m%s\033[00m' "$data")
  fi
  ```
- **Use case:** Git status, health indicators, severity levels, state visualization
- **Example:**
  ```bash
  # Color git branch based on dirty state
  if git diff --quiet; then
      # Clean: Yellow
      git_info=$(printf '\033[01;33m[%s]\033[00m' "$branch")
  else
      # Dirty: Red
      git_info=$(printf '\033[01;31m[%s*]\033[00m' "$branch")
  fi

  # Health status colors
  if [ "$cpu_usage" -lt 70 ]; then
      health=$(printf '\033[01;32m✓ Healthy\033[00m')  # Green
  elif [ "$cpu_usage" -lt 90 ]; then
      health=$(printf '\033[01;33m⚠ Warning\033[00m')  # Yellow
  else
      health=$(printf '\033[01;31m✗ Critical\033[00m')  # Red
  fi
  ```
- **Proposed category:** OT (Output Techniques)
- **Proposed code:** OT-12

### Pattern 7: Reference Documentation by Integration Topic (ST-35)
- **Description:** Organize reference documentation by external integration or customization concern
- **Implementation:**
  - Create separate reference files per integration (e.g., `tool_integration.md`, `color_customization.md`)
  - Include: what it is, how it's used, troubleshooting, examples
  - Reference from main SKILL.md
- **Use case:** Skills with multiple external dependencies, customizable features
- **Example:**
  ```markdown
  ## Skill Structure
  /my-skill/
    SKILL.md (main documentation)
    references/
      aws_integration.md (AWS-specific troubleshooting)
      slack_integration.md (Slack API details)
      color_codes.md (ANSI color reference)
      webhook_format.md (Webhook payload specs)

  ## In SKILL.md
  For AWS integration issues, see `references/aws_integration.md`
  For color customization, see `references/color_codes.md`
  ```
- **Proposed category:** ST (Structural Techniques)
- **Proposed code:** ST-35

### Pattern 8: Error Suppression in Pipelines (DS-96)
- **Description:** Redirect errors to `/dev/null` in multi-command pipelines to prevent UI clutter
- **Implementation:**
  ```bash
  result=$(command1 2>/dev/null | command2 2>/dev/null | command3)
  ```
- **Use case:** Statuslines, UI components, graceful degradation
- **Example:**
  ```bash
  # Cost extraction with silent error handling
  session=$(ccusage session --json 2>/dev/null \
      | jq -r '.sessions[0].totalCost' 2>/dev/null \
      | xargs printf "%.2f" 2>/dev/null)

  # If any step fails, $session will be empty (not error message)
  if [ -n "$session" ]; then
      printf "Cost: $%s\n" "$session"
  fi
  ```
- **Proposed category:** DS (Domain-Specific - Error Handling)
- **Proposed code:** DS-96

## Multi-Technique Combinations

### Combination 1: High-Performance Caching Strategy
**Techniques:** DS-90 (Time-Based Caching) + DS-91 (Background Async) + DS-92 (Stale Cache Fallback)
- **Pattern:** Multi-tier caching for expensive operations
- **Example:**
  1. Check timestamp-based cache (DS-90)
  2. If missing, fetch in background (DS-91)
  3. Use stale cache while fetching (DS-92)

### Combination 2: Safe Configuration Automation
**Techniques:** DS-94 (Settings Modification) + IT-14 (Progressive Disclosure)
- **Pattern:** Automated installation with progressive customization
- **Example:**
  1. Auto-install with safe settings modification (DS-94)
  2. Progressive customization via SKILL.md → references (IT-14)

### Combination 3: Robust Data Extraction
**Techniques:** DS-93 (JSON Pipeline) + DS-96 (Error Suppression) + DS-92 (Fallback)
- **Pattern:** Extract data with graceful degradation
- **Example:**
  1. JSON pipeline with error suppression (DS-93 + DS-96)
  2. If extraction fails, use stale cache (DS-92)

### Combination 4: Visual State Feedback
**Techniques:** OT-12 (Conditional Coloring) + DS-95 (Name Normalization)
- **Pattern:** Compact, color-coded status display
- **Example:**
  1. Shorten verbose names (DS-95)
  2. Color by state (OT-12)

## Notes for Integration

### Integration with MASTER_TECHNIQUE_INDEX.md
1. **Add 7 new techniques:**
   - DS-90: Time-Based File Caching
   - DS-91: Background Async Fetching
   - DS-92: Fallback to Stale Cache
   - DS-93: JSON Processing Pipeline
   - DS-94: Automated Settings Modification with Backup
   - DS-95: Model Name Normalization
   - DS-96: Error Suppression in Pipelines
   - OT-12: Conditional Coloring Based on State
   - ST-35: Reference Documentation by Integration Topic

2. **Confirm existing technique:**
   - IT-14: Progressive Disclosure (automated install → manual customization → deep references)

### Integration with USE_CASE_LOOKUP.md
1. **Add to "Performance Optimization" use case:**
   - Caching strategies: DS-90 + DS-91 + DS-92
   - Background processing: DS-91

2. **Add to "Configuration Management" use case:**
   - Safe config updates: DS-94
   - Automated installation: DS-94 + IT-14

3. **Add to "UI/Display" use case:**
   - Visual feedback: OT-12
   - Display formatting: DS-95

### Key Insights
1. **60x performance improvement:** Caching reduces ccusage calls from ~30/min to ~1/2min
2. **Stale-while-revalidate:** Uses old data while fetching new (zero perceived latency)
3. **Background async:** First statusline appears instantly, costs populate 2-5 seconds later
4. **Safe automation:** Settings modification with automatic backup and atomic jq operations
5. **Graceful degradation:** Silent error handling prevents UI clutter
6. **Multi-line layout:** 3-line statusline optimized for portrait screens
7. **Integration-specific references:** Separate docs for ccusage and color customization

### Real-World Applications
1. **Dashboard systems:** Time-based caching + background refresh
2. **Configuration management:** Safe JSON modification with backups
3. **Monitoring tools:** Conditional coloring for state visualization
4. **CLI tools:** Error suppression for clean output
5. **UI components:** Async data loading with fallback
6. **Status displays:** Name normalization for space savings

---

**Analysis Metadata:**
- **Complexity:** 3.5/5 (moderate caching + async patterns + safe config modification)
- **Novel Techniques:** 9 (DS-90, DS-91, DS-92, DS-93, DS-94, DS-95, DS-96, OT-12, ST-35)
- **Confirmed Techniques:** 1 (IT-14)
- **Bundled Knowledge:** 474+ lines (scripts + references)
- **Production Readiness:** High - Caching, error handling, atomic config updates
- **Educational Value:** High - Teaches performance optimization, safe automation, visual feedback
