---
title: "Android Image and Media Churn Review"
category: mobile/android/targeted-reviews
description: "Android Image and Media Churn Review."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - churn
  - image
  - media
  - mobile
  - reviews
updated: "2026-03-19"
related_prompts: []
---

# Android Image and Media Churn Review

---
title: "Android Image and Media Churn Review"
category: mobile/android/performance
description: "Detect image and media loading patterns that slow perceived responsiveness through repeated requests, unnecessary transformations, or visual churn"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - android
  - images
  - coil
  - glide
  - media
  - thumbnails
  - performance
  - perceived-responsiveness
updated: "2026-03-09"
---

**Objective:** Analyze the Android codebase to identify image and media loading patterns that slow perceived UI responsiveness — repeated image requests due to unstable model objects, unnecessary transformations, placeholder/fade effects that make updates look delayed, and excessive decode/resize work that happens too often.

**When to Use:** Use when changing UI state also changes avatars, thumbnails, card images, or preview media, and the UI feels sluggish during these updates. Use when scrolling through image-heavy lists feels heavy, when images flash/reload during state changes, or when placeholder shimmer makes data refreshes look slower than they are. The app isn't frozen, but image work is making UI updates visibly slower.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Confirm the image churn is tied to UI state changes** — Slow initial image load on cold start is a different problem.
2. **Check the image library's cache configuration** — Many issues are already solved by properly configured Coil/Glide/Picasso.
3. **Verify the images are actually reloading** — Use network inspector or cache hit logging to confirm repeated requests.
4. **Provide exact file:line locations.**

**Finding NO issues is an acceptable outcome.**

### False-Positive Prevention

- ❌ Do NOT flag initial image loading on app start or first screen visit
- ❌ Do NOT flag image loading in lists during fast fling — that's expected behavior
- ❌ Do NOT flag placeholder/shimmer on first load — only flag when images that were already loaded show placeholders again
- ❌ Do NOT flag thumbnail quality vs full-resolution trade-offs — those are intentional
- ❌ Do NOT flag crossfade on first image appearance — only flag on subsequent reloads of the same image
- ✅ DO verify cache hit rates for frequently shown images
- ✅ DO check whether the image URL/key changes between state emissions (causing re-fetch)
- ✅ DO confirm transformations are cached by the library (Coil/Glide cache transformed results)
- ✅ DO check memory cache eviction — are images being evicted too aggressively?

---

### 1. Repeated Image Requests Due to Unstable Model Objects

Identify patterns where image URLs are re-requested because the model identity changes:

* **Unstable image URL keys:**
  - Model object `hashCode()` changes between emissions, causing image library to treat it as a new request
  - URL string rebuilt on every emission (e.g., appending timestamp or auth token)
  - `ImageRequest.Builder.data()` receiving a new object each time

* **RecyclerView rebinding causing reloads:**
  - `notifyDataSetChanged()` rebinds all items, triggering image loads for already-visible images
  - ViewHolder recycling combined with no image key stability

* **Compose recomposition causing re-requests:**
  - Image composable (AsyncImage, SubcomposeAsyncImage) recomposing with "new" URL reference
  - Missing `remember` on ImageRequest builder

**Best Practices:**
```kotlin
// ❌ BAD: New URL string on every emission (even if same URL)
fun getAvatarUrl(userId: String): String {
    return "$BASE_URL/avatar/$userId?t=${System.currentTimeMillis()}" // cache-busting!
}

// ✅ GOOD: Stable URL, use cache control headers instead
fun getAvatarUrl(userId: String): String {
    return "$BASE_URL/avatar/$userId" // stable URL, server controls caching via headers
}

// ❌ BAD (Coil/Compose): New ImageRequest on every recomposition
@Composable
fun Avatar(userId: String) {
    AsyncImage(
        model = ImageRequest.Builder(LocalContext.current)
            .data("$BASE_URL/avatar/$userId")
            .crossfade(true)
            .build(), // new ImageRequest object every recomposition!
        contentDescription = "Avatar"
    )
}

// ✅ GOOD: Remember the request
@Composable
fun Avatar(userId: String) {
    val model = remember(userId) {
        ImageRequest.Builder(context)
            .data("$BASE_URL/avatar/$userId")
            .crossfade(true)
            .build()
    }
    AsyncImage(model = model, contentDescription = "Avatar")
}

// ✅ ALSO GOOD: Just pass the URL string — Coil handles equality
@Composable
fun Avatar(userId: String) {
    AsyncImage(
        model = "$BASE_URL/avatar/$userId", // string equality works fine
        contentDescription = "Avatar"
    )
}
```

**Suggested Fixes:**
- Use stable, deterministic URLs without cache-busting parameters
- In Compose, use `remember(key)` for `ImageRequest` builders, or pass plain URL strings
- In RecyclerView, ensure `DiffUtil.areContentsTheSame` doesn't cause image rebinding when only non-image fields change
- Use image library's memory key / cache key mechanisms (Glide's `signature`, Coil's `memoryCacheKey`)
- For avatar/profile images that change rarely, use ETag-based cache validation

---

### 2. Unnecessary Image Transformations

Identify transformations that re-run without need:

* **Transformation on every bind/recompose:**
  - Circular crop, rounded corners, blur applied on every image load
  - Library should cache transformed results, but check if cache key includes transform

* **Runtime transformations that could be server-side:**
  - Client-side resize when the server could serve appropriate sizes
  - Client-side format conversion (WebP, AVIF) when CDN supports it

* **Redundant transformations:**
  - Applying `CircleCropTransformation` on an already-circular source image
  - Resizing an image that's already the target size

**Best Practices:**
```kotlin
// ❌ BAD: Transform AND custom size on every load
Glide.with(context)
    .load(url)
    .transform(CircleCrop(), RoundedCorners(16)) // runs every time if cache miss
    .override(200, 200) // client-side resize
    .into(imageView)

// ✅ GOOD: Request correct size from server, let library cache transforms
Glide.with(context)
    .load("$url?w=200&h=200&fit=crop") // server-side resize if CDN supports it
    .transform(CircleCrop())
    .diskCacheStrategy(DiskCacheStrategy.ALL) // cache both original and transformed
    .into(imageView)

// ✅ GOOD (Coil/Compose): Size determined by composable
AsyncImage(
    model = url,
    contentDescription = "Thumbnail",
    contentScale = ContentScale.Crop,
    modifier = Modifier
        .size(48.dp)
        .clip(CircleShape) // Compose handles clipping, no image transform needed
)
```

**Suggested Fixes:**
- Use Compose `Modifier.clip()` for shapes instead of image library transformations when possible
- Request appropriately sized images from the server/CDN
- Ensure `DiskCacheStrategy.ALL` caches both original and transformed images
- Avoid redundant transformations — check if the source already matches the target format/size

---

### 3. Placeholder and Fade Effects Making Updates Look Slow

Identify visual patterns that make content updates feel delayed:

* **Crossfade on every reload:**
  - Image crossfade animation plays even when transitioning between cached images
  - Placeholder shimmer appears briefly even on cache hits, creating a "flash"

* **Placeholder shown for cached content:**
  - Loading placeholder visible for 100-200ms on images that are in memory cache
  - Creates a perception of "loading" when no loading is actually happening

* **Shimmer/skeleton on data refresh:**
  - Full shimmer/skeleton UI shown during data refresh even when previous data is still valid
  - Could show stale data → update, instead of shimmer → fresh data

**Best Practices:**
```kotlin
// ❌ BAD: Crossfade on every image, including cache hits
AsyncImage(
    model = ImageRequest.Builder(LocalContext.current)
        .data(url)
        .crossfade(true) // fades even on cache hit!
        .build(),
    contentDescription = "Image"
)

// ✅ GOOD: Only crossfade on first load
AsyncImage(
    model = ImageRequest.Builder(LocalContext.current)
        .data(url)
        .crossfade(true)
        .placeholderMemoryCacheKey(url) // use cached version as placeholder
        .build(),
    contentDescription = "Image"
)

// ❌ BAD: Glide always shows placeholder, even on cache hit
Glide.with(context)
    .load(url)
    .placeholder(R.drawable.placeholder) // visible on every bind, even cached
    .transition(DrawableTransitionOptions.withCrossFade())
    .into(imageView)

// ✅ GOOD: Only show placeholder when actually loading
Glide.with(context)
    .load(url)
    .placeholder(R.drawable.placeholder)
    .transition(DrawableTransitionOptions.withCrossFade())
    .onlyRetrieveFromCache(false) // or use a listener to detect cache hits
    .into(imageView)

// Even better: Use a RequestListener to skip transition on cache hits
```

**Suggested Fixes:**
- Use `placeholderMemoryCacheKey` (Coil) or `thumbnail()` (Glide) to show cached versions instantly
- Disable crossfade for images that are already in memory cache
- For data refreshes, show existing content with a subtle refresh indicator, not full skeleton screens
- Consider `SubcomposeAsyncImage` (Coil) to customize loading vs. success states

---

### 4. Excessive Decode and Resize Work

Identify decode/resize work that happens too often:

* **Loading full-resolution images for thumbnails:**
  - Decoding 4000×3000px images for 48dp avatar circles
  - Memory pressure causing cache evictions, causing more re-decodes

* **No size hints:**
  - Missing `override()` (Glide) or `size()` (Coil) causing full-size decode
  - Compose `AsyncImage` without explicit size constraints

* **Decode on main thread:**
  - Custom image loading without background threading
  - `BitmapFactory.decodeStream` on main thread

**Best Practices:**
```kotlin
// ❌ BAD: No size hint — decodes full resolution
Glide.with(context)
    .load(highResUrl)
    .into(smallThumbnailView) // decodes full res, then scales down

// ✅ GOOD: Specify target size
Glide.with(context)
    .load(highResUrl)
    .override(100, 100) // decode at target size
    .downsample(DownsampleStrategy.CENTER_INSIDE)
    .into(smallThumbnailView)

// ✅ GOOD (Coil): Size determined by Compose layout
AsyncImage(
    model = highResUrl,
    contentDescription = "Thumbnail",
    modifier = Modifier.size(48.dp) // Coil reads this to determine decode size
)
```

**Suggested Fixes:**
- Always provide size hints to image loading libraries
- Use thumbnail URLs from the server when available (don't decode 4K images for list items)
- Ensure memory cache is sized appropriately (`MemoryCache.Builder.maxSizePercent()`)
- Use `downsampling` strategies to reduce decode cost
- For large images, use subsampling libraries (e.g., `SubsamplingScaleImageView`)

---

### 5. Image Churn During State Changes

Identify state changes that cause unnecessary image reloading:

* **List updates causing image flash:**
  - RecyclerView `notifyDataSetChanged()` → all images reload → flash
  - Compose `LazyColumn` without stable keys → items reshuffled → images re-requested

* **State emission with new list instances:**
  - ViewModel emits new `List<Item>` where `Item` has a new reference but same image URL
  - Image library sees new `ImageRequest` → cancels old → starts new → flashes

**Suggested Fixes:**
- Use `DiffUtil` with payload-based partial binding — don't rebind images for non-image field changes
- Ensure stable keys in `LazyColumn` so items aren't reshuffled
- Use URL-string-based image loading (not model-object-based) for stable cache keys
- Cancel image loading only when the ViewHolder is recycled, not on every rebind

---

## Expected Output

Provide an image/media churn analysis report including:

### 1. Executive Summary
- Image loading efficiency rating
- Cache hit rate assessment
- Number of unnecessary reload patterns found

### 2. Image Loading Audit

| Screen | Image Count | Cache Hit Rate | Churn Trigger | Perceived Delay | Priority |
|--------|-------------|----------------|---------------|-----------------|----------|
| [Screen] | [N visible] | [est. %] | [rebind/recompose/URL change] | [flash/fade/reload] | [Level] |

### 3. Detailed Findings

For each issue:
- **Location:** file:line
- **Category:** Unstable Keys / Unnecessary Transforms / Placeholder Delay / Decode Cost / State Churn
- **Image context:** What images, how many, how often
- **Impact:** Visual churn, perceived delay, memory pressure
- **Confidence:** High / Medium / Low
- **Current Code:** Loading pattern
- **Recommended Fix:** Optimized pattern
- **Verification:** Cache hit logging, visual inspection

### 4. Prioritized Remediation Plan

Ordered by perceived responsiveness improvement.

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on image/media perceived responsiveness
- **ST-02** (Structured Sequential Instructions) — Systematic category analysis
- **RT-02** (Multi-Dimensional Analysis) — Keys, transforms, placeholders, decode, churn
- **RT-05** (Evidence-Based Reasoning) — Cache hit rates and reload frequency
- **DS-06** (Prioritization Guidance) — Ranked by visual impact
- **QA-01** (Chain-of-Verification) — Verify actual reloading before flagging

---

## Related Prompts

- `android_list_rendering_inefficiency_review.md` — For list-level rendering issues
- `android_overbroad_ui_updates_review.md` — For broad update patterns causing image churn
- `android_per_update_expensive_work_review.md` — For transformation cost issues
- `performance_resource_usage_profiling.md` — For memory pressure analysis
