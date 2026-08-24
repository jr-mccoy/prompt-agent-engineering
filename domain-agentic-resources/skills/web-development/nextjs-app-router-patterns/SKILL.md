---
name: nextjs-app-router-patterns
description: Master Next.js 14+ App Router with Server Components, streaming, parallel routes, and advanced data fetching. Use when building Next.js applications, implementing SSR/SSG, or optimizing React Server Components.
metadata:
  tags:
    - app
    - next.js
    - nextjs
    - react
    - router
    - ssr
    - web-development
  updated: "2026-04-11"
---
# Next.js App Router Patterns

Comprehensive patterns for Next.js 14+ App Router architecture, Server Components, and modern full-stack React development.

## When to Use This Skill

- Building new Next.js applications with App Router
- Migrating from Pages Router to App Router
- Implementing Server Components and streaming
- Setting up parallel and intercepting routes
- Optimizing data fetching and caching
- Building full-stack features with Server Actions

## Core Concepts

### 1. Rendering Modes

| Mode | Where | When to Use |
|------|-------|-------------|
| **Server Components** | Server only | Data fetching, heavy computation, secrets |
| **Client Components** | Browser | Interactivity, hooks, browser APIs |
| **Static** | Build time | Content that rarely changes |
| **Dynamic** | Request time | Personalized or real-time data |
| **Streaming** | Progressive | Large pages, slow data sources |

### 2. File Conventions

```
app/
├── layout.tsx       # Shared UI wrapper
├── page.tsx         # Route UI
├── loading.tsx      # Loading UI (Suspense)
├── error.tsx        # Error boundary
├── not-found.tsx    # 404 UI
├── route.ts         # API endpoint
├── template.tsx     # Re-mounted layout
├── default.tsx      # Parallel route fallback
└── opengraph-image.tsx  # OG image generation
```

## Quick Start

```typescript
// app/layout.tsx
import { Inter } from 'next/font/google'
import { Providers } from './providers'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: { default: 'My App', template: '%s | My App' },
  description: 'Built with Next.js App Router',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={inter.className}>
        <Providers>{children}</Providers>
      </body>
    </html>
  )
}

// app/page.tsx - Server Component by default
async function getProducts() {
  const res = await fetch('https://api.example.com/products', {
    next: { revalidate: 3600 }, // ISR: revalidate every hour
  })
  return res.json()
}

export default async function HomePage() {
  const products = await getProducts()

  return (
    <main>
      <h1>Products</h1>
      <ProductGrid products={products} />
    </main>
  )
}
```

## Patterns

### Pattern 1: Server Components with Data Fetching

```typescript
// app/products/page.tsx
import { Suspense } from 'react'
import { ProductList, ProductListSkeleton } from '@/components/products'
import { FilterSidebar } from '@/components/filters'

interface SearchParams {
  category?: string
  sort?: 'price' | 'name' | 'date'
  page?: string
}

export default async function ProductsPage({
  searchParams,
}: {
  searchParams: Promise<SearchParams>
}) {
  const params = await searchParams

  return (
    <div className="flex gap-8">
      <FilterSidebar />
      <Suspense
        key={JSON.stringify(params)}
        fallback={<ProductListSkeleton />}
      >
        <ProductList
          category={params.category}
          sort={params.sort}
          page={Number(params.page) || 1}
        />
      </Suspense>
    </div>
  )
}

// components/products/ProductList.tsx - Server Component
async function getProducts(filters: ProductFilters) {
  const res = await fetch(
    `${process.env.API_URL}/products?${new URLSearchParams(filters)}`,
    { next: { tags: ['products'] } }
  )
  if (!res.ok) throw new Error('Failed to fetch products')
  return res.json()
}

export async function ProductList({ category, sort, page }: ProductFilters) {
  const { products, totalPages } = await getProducts({ category, sort, page })

  return (
    <div>
      <div className="grid grid-cols-3 gap-4">
        {products.map((product) => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
      <Pagination currentPage={page} totalPages={totalPages} />
    </div>
  )
}
```

### Pattern 2: Client Components with 'use client'

```typescript
// components/products/AddToCartButton.tsx
'use client'

import { useState, useTransition } from 'react'
import { addToCart } from '@/app/actions/cart'

export function AddToCartButton({ productId }: { productId: string }) {
  const [isPending, startTransition] = useTransition()
  const [error, setError] = useState<string | null>(null)

  const handleClick = () => {
    setError(null)
    startTransition(async () => {
      const result = await addToCart(productId)
      if (result.error) {
        setError(result.error)
      }
    })
  }

  return (
    <div>
      <button
        onClick={handleClick}
        disabled={isPending}
        className="btn-primary"
      >
        {isPending ? 'Adding...' : 'Add to Cart'}
      </button>
      {error && <p className="text-red-500 text-sm">{error}</p>}
    </div>
  )
}
```

### Pattern 3: Server Actions

```typescript
// app/actions/cart.ts
'use server'

import { revalidateTag } from 'next/cache'
import { cookies } from 'next/headers'
import { redirect } from 'next/navigation'

export async function addToCart(productId: string) {
  const cookieStore = await cookies()
  const sessionId = cookieStore.get('session')?.value

  if (!sessionId) {
    redirect('/login')
  }

  try {
    await db.cart.upsert({
      where: { sessionId_productId: { sessionId, productId } },
      update: { quantity: { increment: 1 } },
      create: { sessionId, productId, quantity: 1 },
    })

    revalidateTag('cart')
    return { success: true }
  } catch (error) {
    return { error: 'Failed to add item to cart' }
  }
}

export async function checkout(formData: FormData) {
  const address = formData.get('address') as string
  const payment = formData.get('payment') as string

  // Validate
  if (!address || !payment) {
    return { error: 'Missing required fields' }
  }

  // Process order
  const order = await processOrder({ address, payment })

  // Redirect to confirmation
  redirect(`/orders/${order.id}/confirmation`)
}
```

### Pattern 4: Parallel Routes

```typescript
// app/dashboard/layout.tsx
export default function DashboardLayout({
  children,
  analytics,
  team,
}: {
  children: React.ReactNode
  analytics: React.ReactNode
  team: React.ReactNode
}) {
  return (
    <div className="dashboard-grid">
      <main>{children}</main>
      <aside className="analytics-panel">{analytics}</aside>
      <aside className="team-panel">{team}</aside>
    </div>
  )
}

// app/dashboard/@analytics/page.tsx
export default async function AnalyticsSlot() {
  const stats = await getAnalytics()
  return <AnalyticsChart data={stats} />
}

// app/dashboard/@analytics/loading.tsx
export default function AnalyticsLoading() {
  return <ChartSkeleton />
}

// app/dashboard/@team/page.tsx
export default async function TeamSlot() {
  const members = await getTeamMembers()
  return <TeamList members={members} />
}
```

### Pattern 5: Intercepting Routes (Modal Pattern)

```typescript
// File structure for photo modal
// app/
// ├── @modal/
// │   ├── (.)photos/[id]/page.tsx  # Intercept
// │   └── default.tsx
// ├── photos/
// │   └── [id]/page.tsx            # Full page
// └── layout.tsx

// app/@modal/(.)photos/[id]/page.tsx
import { Modal } from '@/components/Modal'
import { PhotoDetail } from '@/components/PhotoDetail'

export default async function PhotoModal({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const photo = await getPhoto(id)

  return (
    <Modal>
      <PhotoDetail photo={photo} />
    </Modal>
  )
}

// app/photos/[id]/page.tsx - Full page version
export default async function PhotoPage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const photo = await getPhoto(id)

  return (
    <div className="photo-page">
      <PhotoDetail photo={photo} />
      <RelatedPhotos photoId={id} />
    </div>
  )
}

// app/layout.tsx
export default function RootLayout({
  children,
  modal,
}: {
  children: React.ReactNode
  modal: React.ReactNode
}) {
  return (
    <html>
      <body>
        {children}
        {modal}
      </body>
    </html>
  )
}
```

### Pattern 6: Streaming with Suspense

```typescript
// app/product/[id]/page.tsx
import { Suspense } from 'react'

export default async function ProductPage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params

  // This data loads first (blocking)
  const product = await getProduct(id)

  return (
    <div>
      {/* Immediate render */}
      <ProductHeader product={product} />

      {/* Stream in reviews */}
      <Suspense fallback={<ReviewsSkeleton />}>
        <Reviews productId={id} />
      </Suspense>

      {/* Stream in recommendations */}
      <Suspense fallback={<RecommendationsSkeleton />}>
        <Recommendations productId={id} />
      </Suspense>
    </div>
  )
}

// These components fetch their own data
async function Reviews({ productId }: { productId: string }) {
  const reviews = await getReviews(productId) // Slow API
  return <ReviewList reviews={reviews} />
}

async function Recommendations({ productId }: { productId: string }) {
  const products = await getRecommendations(productId) // ML-based, slow
  return <ProductCarousel products={products} />
}
```

## Route Handlers, Caching Strategies, SEO & Best Practices

Route Handler API routes (GET/POST with NextRequest/NextResponse), `generateMetadata` + `generateStaticParams` for dynamic SEO, fetch cache options (`no-store`/`force-cache`/`revalidate`/tag-based), `revalidateTag`/`revalidatePath` in Server Actions, and Do/Don't best practices.

See [references/route-handlers-caching-and-seo.md](references/route-handlers-caching-and-seo.md)

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/route-handlers-caching-and-seo.md` | Route handlers, metadata/SEO, caching strategies, best practices |

## Related Skills

- `react-development` - When building React without Next.js
- `tailwind-design-system` - When styling Next.js components with Tailwind
- `astro-development` - When content-focused sites suit better than Next.js
