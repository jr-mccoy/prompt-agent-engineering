// src/content/config.ts
// Example content collection schemas for common use cases

import { defineCollection, z, reference } from 'astro:content';

// ===================
// BLOG COLLECTION
// ===================

const blog = defineCollection({
  type: 'content', // Markdown/MDX files
  schema: ({ image }) => z.object({
    // Required fields
    title: z.string().max(100),
    description: z.string().max(200),
    pubDate: z.coerce.date(),

    // Optional fields
    updatedDate: z.coerce.date().optional(),
    draft: z.boolean().default(false),

    // Image with validation (requires @astrojs/image)
    heroImage: image().optional(),
    // Or simple string path
    // heroImage: z.string().optional(),

    // Author reference to another collection
    author: reference('authors').optional(),

    // Tags with validation
    tags: z.array(z.string()).default([]),

    // Category with enum
    category: z.enum(['tutorial', 'news', 'opinion', 'review']).default('news'),

    // SEO fields
    canonicalUrl: z.string().url().optional(),
    noIndex: z.boolean().default(false),

    // Reading time (can be computed)
    readingTime: z.number().optional(),
  }),
});

// ===================
// AUTHORS COLLECTION
// ===================

const authors = defineCollection({
  type: 'data', // JSON/YAML files
  schema: ({ image }) => z.object({
    name: z.string(),
    email: z.string().email(),
    avatar: image().optional(),
    bio: z.string().max(500).optional(),
    social: z.object({
      twitter: z.string().optional(),
      github: z.string().optional(),
      linkedin: z.string().optional(),
    }).optional(),
    role: z.enum(['author', 'editor', 'admin']).default('author'),
  }),
});

// ===================
// DOCS COLLECTION
// ===================

const docs = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),

    // Sidebar configuration
    sidebar: z.object({
      label: z.string().optional(),
      order: z.number().default(999),
      hidden: z.boolean().default(false),
      badge: z.object({
        text: z.string(),
        variant: z.enum(['note', 'tip', 'caution', 'danger']).default('note'),
      }).optional(),
    }).default({}),

    // Table of contents
    tableOfContents: z.union([
      z.boolean(),
      z.object({
        minHeadingLevel: z.number().min(1).max(6).default(2),
        maxHeadingLevel: z.number().min(1).max(6).default(3),
      }),
    ]).default(true),

    // Page metadata
    editUrl: z.boolean().default(true),
    head: z.array(z.object({
      tag: z.string(),
      attrs: z.record(z.string()).optional(),
      content: z.string().optional(),
    })).default([]),

    // Related content
    next: z.union([
      z.boolean(),
      z.string(),
      z.object({
        link: z.string(),
        label: z.string(),
      }),
    ]).optional(),
    prev: z.union([
      z.boolean(),
      z.string(),
      z.object({
        link: z.string(),
        label: z.string(),
      }),
    ]).optional(),
  }),
});

// ===================
// PROJECTS COLLECTION
// ===================

const projects = defineCollection({
  type: 'content',
  schema: ({ image }) => z.object({
    title: z.string(),
    description: z.string(),
    thumbnail: image(),

    // Project metadata
    status: z.enum(['planning', 'in-progress', 'completed', 'archived']),
    startDate: z.coerce.date(),
    endDate: z.coerce.date().optional(),

    // Links
    liveUrl: z.string().url().optional(),
    repoUrl: z.string().url().optional(),

    // Tech stack
    technologies: z.array(z.string()),

    // Featured flag
    featured: z.boolean().default(false),
    order: z.number().default(999),
  }),
});

// ===================
// PRODUCTS COLLECTION (E-commerce)
// ===================

const products = defineCollection({
  type: 'data',
  schema: ({ image }) => z.object({
    name: z.string(),
    slug: z.string(),
    description: z.string(),

    // Pricing
    price: z.number().positive(),
    salePrice: z.number().positive().optional(),
    currency: z.enum(['USD', 'EUR', 'GBP']).default('USD'),

    // Inventory
    sku: z.string(),
    inStock: z.boolean().default(true),
    quantity: z.number().int().nonnegative().default(0),

    // Images
    images: z.array(image()),

    // Categorization
    category: z.string(),
    tags: z.array(z.string()).default([]),

    // Variants
    variants: z.array(z.object({
      name: z.string(),
      options: z.array(z.string()),
    })).default([]),

    // SEO
    metaTitle: z.string().optional(),
    metaDescription: z.string().optional(),
  }),
});

// ===================
// TESTIMONIALS COLLECTION
// ===================

const testimonials = defineCollection({
  type: 'data',
  schema: ({ image }) => z.object({
    name: z.string(),
    role: z.string().optional(),
    company: z.string().optional(),
    avatar: image().optional(),
    quote: z.string(),
    rating: z.number().min(1).max(5).optional(),
    featured: z.boolean().default(false),
  }),
});

// ===================
// CHANGELOG COLLECTION
// ===================

const changelog = defineCollection({
  type: 'content',
  schema: z.object({
    version: z.string(),
    date: z.coerce.date(),
    title: z.string().optional(),
    description: z.string().optional(),

    // Change categories
    added: z.array(z.string()).default([]),
    changed: z.array(z.string()).default([]),
    deprecated: z.array(z.string()).default([]),
    removed: z.array(z.string()).default([]),
    fixed: z.array(z.string()).default([]),
    security: z.array(z.string()).default([]),
  }),
});

// ===================
// EXPORT ALL COLLECTIONS
// ===================

export const collections = {
  blog,
  authors,
  docs,
  projects,
  products,
  testimonials,
  changelog,
};

// ===================
// USAGE EXAMPLES
// ===================

/*
Query examples in .astro files:

// Get all blog posts (excluding drafts)
const posts = await getCollection('blog', ({ data }) => {
  return import.meta.env.PROD ? data.draft !== true : true;
});

// Get single entry
const post = await getEntry('blog', 'my-post-slug');

// Get entry by reference
const author = await getEntry(post.data.author);

// Render content
const { Content, headings, remarkPluginFrontmatter } = await post.render();

// In Astro component
---
import { getCollection, getEntry } from 'astro:content';

const posts = await getCollection('blog');
const sortedPosts = posts.sort(
  (a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf()
);
---

{sortedPosts.map((post) => (
  <article>
    <a href={`/blog/${post.slug}`}>{post.data.title}</a>
    <time datetime={post.data.pubDate.toISOString()}>
      {post.data.pubDate.toLocaleDateString()}
    </time>
  </article>
))}
*/
