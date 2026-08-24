---
name: schema-org-markup
description: Generate and validate Schema.org structured data (JSON-LD) for the most rank-impactful types — Article, Product, FAQPage, HowTo, Recipe, LocalBusiness, BreadcrumbList, Organization. Use when implementing structured data for the first time, when rich results disappear after a redesign, or when validating against Google's evolving requirements.
metadata:
  tags:
    - seo
    - structured-data
    - schema-org
    - json-ld
    - rich-results
  updated: "2026-05-05"
---

# Schema.org Markup

Structured data doesn't make pages rank — but rich results raise CTR significantly when they appear, and Google increasingly uses Schema as ground truth for entity understanding. This skill generates the markup, validates it, and tracks Google's rules (which change without notice).

## When to Use This Skill

- Implementing structured data for the first time on a site
- Rich results disappeared after a redesign or CMS migration
- A specific page type needs to support Google rich result eligibility
- Auditing existing markup for validity and completeness
- Adding structured data to a JS-rendered SPA (special considerations)

## Format Choice: JSON-LD

Always JSON-LD. Microdata and RDFa work, but Google recommends JSON-LD, it's separate from HTML rendering, and it's easier to manage at scale. Place it in `<head>` or just before `</body>` — Google reads either.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "...",
  ...
}
</script>
```

## High-Value Types and Templates

### Article (and BlogPosting, NewsArticle)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{title, ≤110 chars for safety}",
  "description": "{meta description}",
  "image": [
    "https://example.com/photos/1x1.jpg",
    "https://example.com/photos/4x3.jpg",
    "https://example.com/photos/16x9.jpg"
  ],
  "datePublished": "2026-05-05T08:00:00+00:00",
  "dateModified": "2026-05-05T14:22:00+00:00",
  "author": [{
    "@type": "Person",
    "name": "Jane Author",
    "url": "https://example.com/authors/jane-author/"
  }],
  "publisher": {
    "@type": "Organization",
    "name": "Example Publisher",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://example.com/article-slug/"
  }
}
```

**Required by Google for rich results:** headline, image, datePublished, author. The rest improves entity understanding.

### Product (with Offers and AggregateRating)

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Acme Widget Pro",
  "description": "...",
  "image": ["https://example.com/widget-1x1.jpg"],
  "brand": {"@type": "Brand", "name": "Acme"},
  "sku": "WIDGET-PRO-2026",
  "gtin13": "0123456789012",
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/products/widget-pro",
    "priceCurrency": "USD",
    "price": "49.99",
    "priceValidUntil": "2026-12-31",
    "availability": "https://schema.org/InStock",
    "shippingDetails": {
      "@type": "OfferShippingDetails",
      "shippingRate": {"@type": "MonetaryAmount", "value": "5.00", "currency": "USD"},
      "shippingDestination": {"@type": "DefinedRegion", "addressCountry": "US"},
      "deliveryTime": {
        "@type": "ShippingDeliveryTime",
        "handlingTime": {"@type": "QuantitativeValue", "minValue": 0, "maxValue": 1, "unitCode": "DAY"},
        "transitTime": {"@type": "QuantitativeValue", "minValue": 2, "maxValue": 5, "unitCode": "DAY"}
      }
    },
    "hasMerchantReturnPolicy": {
      "@type": "MerchantReturnPolicy",
      "applicableCountry": "US",
      "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
      "merchantReturnDays": 30,
      "returnMethod": "https://schema.org/ReturnByMail",
      "returnFees": "https://schema.org/FreeReturn"
    }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.6",
    "reviewCount": "247"
  }
}
```

**Note (2026):** Google's free product listings require `shippingDetails` and `hasMerchantReturnPolicy` for eligibility. Markup without them is valid Schema but doesn't enable the rich result.

### FAQPage

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is X?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "X is..."
      }
    },
    {
      "@type": "Question",
      "name": "How does X work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "X works by..."
      }
    }
  ]
}
```

**Eligibility note:** Google narrowed FAQ rich results in 2023 to mostly authoritative government and health sites. Markup is still valuable for entity understanding even when the rich result doesn't show.

### HowTo

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Tie a Bowline Knot",
  "description": "...",
  "totalTime": "PT3M",
  "supply": [{"@type": "HowToSupply", "name": "Rope"}],
  "tool": [{"@type": "HowToTool", "name": "Hands"}],
  "step": [
    {
      "@type": "HowToStep",
      "name": "Form a loop",
      "text": "Make a small loop in the rope...",
      "image": "https://example.com/step1.jpg",
      "url": "https://example.com/article#step1"
    }
  ]
}
```

### LocalBusiness

```json
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "name": "Acme Diner",
  "image": "https://example.com/photo.jpg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St",
    "addressLocality": "Springfield",
    "addressRegion": "IL",
    "postalCode": "62701",
    "addressCountry": "US"
  },
  "geo": {"@type": "GeoCoordinates", "latitude": 39.78, "longitude": -89.65},
  "telephone": "+1-555-555-1234",
  "url": "https://example.com",
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "opens": "07:00",
    "closes": "21:00"
  }],
  "priceRange": "$$",
  "servesCuisine": "American"
}
```

### BreadcrumbList

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://example.com/"},
    {"@type": "ListItem", "position": 2, "name": "Guides", "item": "https://example.com/guides/"},
    {"@type": "ListItem", "position": 3, "name": "This Article"}
  ]
}
```

### Organization (sitewide, in homepage and root layout)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Acme",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "sameAs": [
    "https://twitter.com/acme",
    "https://www.linkedin.com/company/acme",
    "https://en.wikipedia.org/wiki/Acme"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-555-555-0100",
    "contactType": "customer service",
    "areaServed": "US",
    "availableLanguage": ["English", "Spanish"]
  }
}
```

`sameAs` to authoritative profiles (Wikipedia, Crunchbase, official social) is a strong entity signal.

## Combining Multiple Types on One Page

Use an array, not nested:

```json
[
  {"@context": "https://schema.org", "@type": "Article", ...},
  {"@context": "https://schema.org", "@type": "BreadcrumbList", ...}
]
```

Or a single graph with `@id` references:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {"@type": "Article", "@id": "#article", ...},
    {"@type": "Person", "@id": "#author", ...}
  ]
}
```

## SPA Considerations

JavaScript-rendered SPAs (React, Vue, Angular) must inject JSON-LD that's present at server render or via SSR. Google does render JS, but rendering is delayed and structured data injected client-side after `DOMContentLoaded` may be missed or seen late.

- **Next.js/Nuxt SSR:** inject into `<head>` server-side
- **Pure SPA:** prerender, server-render, or accept the risk
- **Verify with URL Inspection** in Google Search Console after deploy

## Validation

Run every page through:

1. **Schema.org Validator** (validator.schema.org) — basic syntax and type validity
2. **Google Rich Results Test** (search.google.com/test/rich-results) — Google-specific eligibility
3. **Search Console → Enhancements** — production drift, errors, warnings

Programmatic validation in CI:

```python
import requests

def validate_schema(html: str) -> ValidationResult:
    r = requests.post(
        "https://validator.schema.org/validate",
        data={"html": html},
    )
    return parse_validator_response(r.json())
```

## Implementation Checklist

- [ ] JSON-LD format (not microdata or RDFa)
- [ ] Uses `https://schema.org` context (not http)
- [ ] Each page has the appropriate primary type
- [ ] Sitewide Organization markup on homepage
- [ ] BreadcrumbList on every non-home page
- [ ] All required Google fields populated for the type
- [ ] Image URLs are absolute, not relative
- [ ] Dates in ISO 8601 with timezone
- [ ] Validation against Schema.org Validator passes
- [ ] Validation against Google Rich Results Test passes
- [ ] Search Console monitored weekly for errors

## Anti-Patterns to Avoid

- **Marking up content not visible to users** — Google penalizes mismatch between visible and structured content
- **Fake reviews or aggregate ratings** — actively penalized
- **Stale `priceValidUntil` dates** — Google may suppress the rich result
- **JSON-LD injected only client-side in a pure SPA** — high risk of being missed
- **Marking up the same entity twice with different IDs** — entity confusion
- **HowTo on transactional/product pages** — Google deprecated this combination
- **Schema mismatched with page content** (e.g., FAQPage with no visible FAQs)

## Companion Skills

- `content-brief-scaffolding` — specifies which schema types are required per page
- `core-web-vitals-audit` — performance affects whether rich results actually display

## Related Resources

- Schema.org documentation: https://schema.org/docs/full.html
- Google's structured data guidelines: https://developers.google.com/search/docs/appearance/structured-data
