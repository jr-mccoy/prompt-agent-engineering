---
name: llm-icon-finder
description: Finding and accessing AI/LLM model brand icons from lobe-icons library. Use when users need icon URLs, want to download brand logos for AI models/providers/applications (Claude, GPT, Gemini, etc.), or request icons in SVG/PNG/WEBP formats.
metadata:
  tags:
    - llm-icons
    - brand-assets
    - svg-icons
    - lobe-icons
    - ai-branding
  updated: "2026-04-11"
---

# Finding AI/LLM Brand Icons

Access AI/LLM model brand icons and logos from the [lobe-icons](https://github.com/lobehub/lobe-icons) library. The library contains 100+ icons for models (Claude, GPT, Gemini), providers (OpenAI, Anthropic, Google), and applications (ComfyUI, LobeChat).

## Icon Formats and Variants

**Available formats**: SVG (scalable), PNG (raster), WEBP (compressed)
**Theme variants**: light, dark, and color (some icons)

## CDN URL Patterns

Construct URLs using these patterns:

```
# SVG
https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-svg/{light|dark}/{icon-name}.svg

# PNG
https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-png/{light|dark}/{icon-name}.png

# WEBP
https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-webp/{light|dark}/{icon-name}.webp

# Color variant (append -color to icon-name)
https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-png/dark/{icon-name}-color.png
```

**Icon naming convention**: Lowercase, hyphenated (e.g., `claude`, `chatglm`, `openai`, `huggingface`)

## Workflow

When users request icons:

1. Identify icon name (usually lowercase company/model name, hyphenated if multi-word)
2. Determine format (default: PNG) and theme (default: dark)
3. Construct CDN URL using pattern above
4. Provide URL to user
5. If download requested, use Bash tool with curl
6. Include web viewer link: `https://lobehub.com/icons/{icon-name}`

## Finding Icon Names

**Common icons**: See `references/icons-list.md` for comprehensive list organized by category (Models, Providers, Applications, Chinese AI)

**Uncertain names**:
- Browse https://lobehub.com/icons
- Try variations (e.g., company name vs product name: `alibaba` vs `alibabacloud`)
- Check for `-color` variants if standard URL fails

**Chinese AI models**: Support Chinese queries (e.g., "智谱" → `chatglm`, "月之暗面" → `moonshot`)

## Examples

**Single icon request**:
```
User: "Claude icon"
→ Provide: https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-png/dark/claude.png
→ Also mention color variant and web viewer link
```

**Multiple icons download**:
```bash
curl -o openai.svg "https://raw.githubusercontent.com/lobehub/lobe-icons/.../dark/openai.svg"
curl -o anthropic.svg "https://raw.githubusercontent.com/lobehub/lobe-icons/.../dark/anthropic.svg"
```

**Chinese query**:
```
User: "找一下智谱的图标"
→ Identify: 智谱 = ChatGLM → icon name: chatglm
→ Provide URLs and mention related icons (zhipu, codegeex)
```

## Troubleshooting

If URL returns 404:
1. Try `-color` suffix variant
2. Check alternate naming (e.g., `chatgpt` vs `gpt`, `google` vs `gemini`)
3. Direct user to https://lobehub.com/icons to browse
4. Search repository: https://github.com/lobehub/lobe-icons

## Reference Files

- `references/icons-list.md` - Comprehensive list of 100+ available icons by category
- `references/developer-info.md` - npm installation and React usage examples

---

## Core Concepts

### Icon Library Architecture

The lobe-icons library organizes icons into three tiers:

1. **Models** - Individual AI models (Claude, GPT-4, Gemini, Llama, Mistral, etc.)
2. **Providers** - Companies and platforms (Anthropic, OpenAI, Google, Meta, etc.)
3. **Applications** - Tools and apps built on AI (ComfyUI, LobeChat, Ollama, etc.)

Each icon ships in multiple formats and theme variants, enabling consistent branding across light and dark interfaces.

### Format Selection Guide

| Format | Best For | Pros | Cons |
|--------|----------|------|------|
| **SVG** | Web, documentation, scalable UI | Infinite scaling, small file size, CSS-stylable | Not universally supported in all tools |
| **PNG** | Presentations, markdown, chat | Universal compatibility, predictable rendering | Fixed resolution, larger files at high DPI |
| **WEBP** | Web performance, thumbnails | Smallest file size, good quality | Limited support in older tools |

### Theme Variants

- **Dark** - Light-colored icons designed for dark backgrounds (most common default)
- **Light** - Dark-colored icons designed for light backgrounds
- **Color** - Full-color brand icons (append `-color` to icon name); not available for all icons

---

## Icon Integration Patterns

### React Component Integration

```jsx
// Using the @lobehub/icons npm package
import { Claude, OpenAI, Gemini } from '@lobehub/icons';

function ModelSelector({ models }) {
  const iconMap = {
    claude: <Claude size={24} />,
    openai: <OpenAI size={24} />,
    gemini: <Gemini size={24} />,
  };

  return (
    <div className="model-list">
      {models.map(model => (
        <div key={model.id} className="model-item">
          {iconMap[model.provider]}
          <span>{model.name}</span>
        </div>
      ))}
    </div>
  );
}
```

### Markdown Documentation Embeds

```markdown
## Supported Models

| Model | Provider | Icon |
|-------|----------|------|
| Claude 3.5 Sonnet | Anthropic | ![Claude](https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-png/dark/claude.png) |
| GPT-4o | OpenAI | ![OpenAI](https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-png/dark/openai.png) |
| Gemini Pro | Google | ![Gemini](https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-png/dark/gemini.png) |
```

### HTML with Inline Sizing

```html
<!-- Consistent 32px icons in a toolbar -->
<div class="ai-toolbar">
  <img src="https://...dark/claude.svg" width="32" height="32" alt="Claude" />
  <img src="https://...dark/openai.svg" width="32" height="32" alt="OpenAI" />
  <img src="https://...dark/gemini.svg" width="32" height="32" alt="Gemini" />
</div>
```

---

## Batch Download Workflows

### Download All Icons for a Category

```bash
# Download all major model provider icons
providers=("anthropic" "openai" "google" "meta" "mistral" "cohere" "huggingface")
format="svg"
theme="dark"
base_url="https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-${format}/${theme}"

mkdir -p icons/${theme}
for name in "${providers[@]}"; do
  curl -sL -o "icons/${theme}/${name}.${format}" "${base_url}/${name}.${format}"
  echo "Downloaded: ${name}.${format}"
done
```

### Download Both Theme Variants

```bash
icon_name="claude"
for theme in light dark; do
  for format in svg png; do
    url="https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-${format}/${theme}/${icon_name}.${format}"
    curl -sL -o "${icon_name}-${theme}.${format}" "$url"
  done
done
```

### Download with Verification

```bash
# Download and verify icons exist (non-404)
download_icon() {
  local name=$1 format=${2:-png} theme=${3:-dark}
  local url="https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-${format}/${theme}/${name}.${format}"
  local status=$(curl -sL -o /dev/null -w "%{http_code}" "$url")
  if [ "$status" = "200" ]; then
    curl -sL -o "${name}.${format}" "$url"
    echo "OK: ${name}.${format}"
  else
    echo "MISSING: ${name} (HTTP ${status}) - try -color variant or alternate name"
  fi
}

download_icon "claude"
download_icon "claude-color"
download_icon "openai"
```

---

## Icon Customization

### Sizing Guidelines

| Context | Recommended Size | Notes |
|---------|-----------------|-------|
| Inline text | 16-20px | Align with text baseline |
| Navigation/toolbar | 24-32px | Touch-friendly minimum |
| Card/tile header | 40-48px | Prominent but not dominant |
| Hero/feature section | 64-96px | Large display use |
| Presentation slide | 128-256px | Use SVG to avoid pixelation |

### CSS Color Overlay (SVG only)

```css
/* Tint SVG icons to match your brand */
.icon-brand-tint {
  filter: brightness(0) saturate(100%) invert(33%) sepia(95%)
          saturate(1000%) hue-rotate(200deg) brightness(95%) contrast(95%);
}

/* Grayscale for disabled state */
.icon-disabled {
  filter: grayscale(100%);
  opacity: 0.5;
}

/* Dark mode inversion for light-theme icons */
@media (prefers-color-scheme: dark) {
  .icon-auto-theme {
    filter: invert(1);
  }
}
```

### Background Removal and Padding

When embedding icons on colored backgrounds:

```css
.icon-on-card {
  padding: 8px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(4px);
}

/* Circular icon badge */
.icon-badge {
  width: 48px;
  height: 48px;
  padding: 10px;
  border-radius: 50%;
  background: #1a1a2e;
  display: flex;
  align-items: center;
  justify-content: center;
}
```

---

## Best Practices for Brand Asset Usage

### Licensing and Attribution

- The lobe-icons library is open source under MIT license
- Individual brand logos remain the property of their respective companies
- When using in public-facing materials, follow each company's brand guidelines
- Attribution to lobe-icons is appreciated but not required under MIT

### Usage Guidelines

| Acceptable Use | Avoid |
|---------------|-------|
| Developer documentation showing supported models | Implying endorsement by a model provider |
| Internal dashboards and tools | Modifying brand logos beyond sizing |
| Educational materials about AI models | Using icons in ways that misrepresent capabilities |
| Open-source project documentation | Combining icons to imply partnerships that do not exist |
| Presentation slides comparing models | Using outdated or unofficial icon variants |

### Consistency Rules

1. **Pick one theme** per context -- do not mix light and dark icons on the same page
2. **Use consistent sizing** across all icons in a set
3. **Prefer SVG** for any context where the display size might vary
4. **Cache locally** rather than hotlinking CDN URLs in production apps
5. **Check for updates** periodically -- new models and providers are added regularly

---

## Common Pitfalls

| Pitfall | Symptom | Solution |
|---------|---------|----------|
| Wrong icon name | 404 from CDN URL | Check `references/icons-list.md` or browse lobehub.com/icons |
| Missing `-color` suffix | Get monochrome instead of full-color icon | Append `-color` to icon name for color variant |
| Mixing themes | Icons look inconsistent on page | Use all `dark` or all `light` icons per context |
| Hotlinking in production | Slow loads, potential rate limiting | Download and self-host icons for production use |
| PNG at large sizes | Pixelated icons on high-DPI displays | Use SVG format for any size above 64px |
| Stale icon cache | Outdated icon after library update | Clear cache or add version hash to URL |
| Company vs product name confusion | Wrong icon returned | Try both (e.g., `google` vs `gemini`, `anthropic` vs `claude`) |

---

## Advanced: Creating Icon Sets for Presentations and Dashboards

### Presentation Icon Sheet

Generate a reference sheet with all relevant icons for a presentation:

```bash
#!/bin/bash
# Generate an icon reference sheet as HTML
icons=("claude" "openai" "gemini" "mistral" "llama" "cohere" "huggingface" "perplexity")
theme="dark"

cat > icon-sheet.html << 'HEADER'
<html><head><style>
  body { background: #1a1a2e; color: white; font-family: sans-serif; padding: 2rem; }
  .grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; }
  .icon-card { text-align: center; padding: 1.5rem; border-radius: 12px; background: rgba(255,255,255,0.05); }
  .icon-card img { width: 64px; height: 64px; margin-bottom: 0.5rem; }
  .icon-card p { margin: 0; font-size: 14px; opacity: 0.8; }
</style></head><body><h1>AI Model Icons</h1><div class="grid">
HEADER

for name in "${icons[@]}"; do
  url="https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-png/${theme}/${name}.png"
  echo "<div class='icon-card'><img src='${url}' alt='${name}'><p>${name}</p></div>" >> icon-sheet.html
done

echo "</div></body></html>" >> icon-sheet.html
echo "Generated icon-sheet.html"
```

### Dashboard Integration Pattern

For dashboards comparing multiple AI models:

```javascript
// Model comparison dashboard icon config
const MODEL_ICONS = {
  'claude-3.5-sonnet': { icon: 'claude', color: '#D97706' },
  'gpt-4o':            { icon: 'openai', color: '#10A37F' },
  'gemini-pro':        { icon: 'gemini', color: '#4285F4' },
  'llama-3':           { icon: 'meta',   color: '#0668E1' },
  'mistral-large':     { icon: 'mistral', color: '#FF7000' },
};

function getIconUrl(modelId, format = 'svg', theme = 'dark') {
  const config = MODEL_ICONS[modelId];
  if (!config) return null;
  return `https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-${format}/${theme}/${config.icon}.${format}`;
}
```

### Icon Sprite Sheet for Performance

For pages loading many icons, consider creating a sprite sheet:

```bash
# Combine multiple SVGs into a single sprite sheet
# Requires svgo and svg-sprite packages
npx svg-sprite --symbol --symbol-dest=. --symbol-sprite=ai-icons-sprite.svg icons/*.svg
```

Usage in HTML:
```html
<svg class="icon"><use href="ai-icons-sprite.svg#claude"></use></svg>
<svg class="icon"><use href="ai-icons-sprite.svg#openai"></use></svg>
```
