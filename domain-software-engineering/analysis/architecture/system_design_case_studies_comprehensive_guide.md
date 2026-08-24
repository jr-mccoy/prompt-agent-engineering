---
title: "System Design Case Studies: Comprehensive Guide"
category: analysis/architecture
description: "Reference compilation of 19 system design case studies (Stock Exchange, Uber Payments, YouTube, Google Docs, Kafka, URL Shortener, etc.) sourced from System Design One newsletter."
techniques:
  - ST-03
  - RT-02
  - DS-01
difficulty: intermediate
tags:
  - architecture
  - system-design
  - case-studies
  - reference
updated: "2026-04-17"
related_prompts: []
artifact_type: "reference"
---

# System Design Case Studies: Comprehensive Guide

> **Source:** [System Design One Newsletter](https://newsletter.systemdesign.one/) by Neo Kim
> **Compiled:** 2026-02-22 | **Case Studies:** 19

---

## Table of Contents

1. [Stock Exchange](#1-stock-exchange)
2. [Payment System (Uber)](#2-payment-system-uber)
3. [YouTube](#3-youtube)
4. [Google Docs](#4-google-docs)
5. [Apache Kafka](#5-apache-kafka)
6. [URL Shortener](#6-url-shortener)
7. [WhatsApp](#7-whatsapp)
8. [Airbnb](#8-airbnb)
9. [Spotify](#9-spotify)
10. [Slack](#10-slack)
11. [Reddit](#11-reddit)
12. [Bluesky](#12-bluesky)
13. [Tinder](#13-tinder)
14. [Twitter/X Timeline](#14-twitterx-timeline)
15. [Uber Nearby Drivers](#15-uber-nearby-drivers)
16. [AWS Lambda](#16-aws-lambda)
17. [Amazon S3](#17-amazon-s3)
18. [Apple AirTags](#18-apple-airtags)
19. [Large Language Models (LLMs)](#19-large-language-models-llms)
20. [Cross-Cutting Patterns & Lessons](#20-cross-cutting-patterns--lessons)

---

## 1. Stock Exchange

### Architecture Overview
An **asynchronous, event-sourced architecture** with three layers: Broker (user-facing REST/WebSocket), Gateway (validation/routing), and Matching Engine (core trading logic).

### Key Components

**Broker Layer**
- REST APIs and WebSockets for real-time market data
- Uses the **FIX protocol** (Financial Information Exchange) for secure bidirectional communication with the gateway
- FIX assigns unique sequence numbers and uses checksums for data integrity

**Gateway Layer** (three parts)
- **Risk Manager:** Validates funds, blocks unusual activity, determines fees
- **Wallet Service:** Stores user funds and trading assets
- **Order Manager:** Assigns globally increasing sequence numbers, maintains order states

**Matching Engine**
- **Order Book:** Separate in-memory BUY/SELL lists per stock symbol
- Each price level maintains a **doubly-linked list** (FIFO ordering)
- New orders added at tail — O(1); filled/canceled orders removed via pointer — O(1)
- Hash index maps order IDs to pointers for O(1) cancellation lookups

### Critical Design Decisions
- **Sequence numbers** guarantee ordering for fairness, enable deterministic replay, and provide exactly-once delivery
- **Separate topic queues** per message type (new order, cancel, trade) with independent sequence numbers reduce contention and enable parallel processing
- **In-memory order book** for microsecond latency; recovery via event replay

### Message Distribution
- New orders: ~50% of messages
- Cancels: ~40% of messages
- Executions: ~2% of messages

### Key Trade-offs
| Decision | Trade-off |
|----------|-----------|
| In-memory order book | Speed vs. durability (mitigated by event replay) |
| Separate message queues | Multiple sequence streams vs. reduced contention |
| Event sourcing | Storage overhead vs. perfect replay/audit capability |

---

## 2. Payment System (Uber)

### Scale
- **30 million transactions per day**

### Core Challenges
1. **Security:** Storing sensitive payment data on mobile/servers creates vulnerability
2. **Disbursement:** Single payments must split across driver, platform, taxes/fees
3. **Reliability:** External dependencies (banks, card networks) introduce failure points

### Architecture: Tokenization
- Mobile app uses payment provider SDK to collect card details
- SDK transmits data **directly to payment provider** (never touches Uber servers)
- Provider returns a **scoped token** representing the card
- Token is tied to Uber's account, app, and specific use cases
- "A stolen token is useless" — eliminates sensitive data storage entirely

### Key Insight
Tokenization shifts PCI compliance burden to payment providers while maintaining transactional capability.

---

## 3. YouTube

### Architecture Overview
Application servers handle lightweight metadata while heavy video data is offloaded directly to cloud storage and CDNs.

### Key Design Decisions

**Upload Strategy**
- **Pre-signed URLs** bypass app servers — direct client uploads to blob storage
- Multipart upload support for files up to 256 GB with resume capability
- Asynchronous processing (10-30 minute acceptable latency)
- Eventual consistency acceptable for new uploads

**Streaming Approach**
- **Adaptive bitrate streaming (ABR)** from CDN
- Target: first frame under 500ms
- Support for 240p to 4K (MP4, AVI, MOV)
- Automatic quality adjustment for varying network speeds

**Write Optimization**
- Progress tracking uses fire-and-forget pattern
- DynamoDB handles millions of writes/second
- Speed prioritized over immediate consistency

### Data Flow
1. Client requests pre-signed S3 URL
2. Direct upload to blob storage (bypasses app servers)
3. Transcoding pipeline → multiple renditions
4. Manifest file distributed via CDN
5. Client streams segments adaptively
6. Progress updates flow asynchronously

### Scale Metrics
| Metric | Value |
|--------|-------|
| Upload volume | 1M uploads/day |
| DAU | 100M |
| Read:write ratio | ~100:1 |
| Real YouTube uploads | 500+ hours/minute |
| Uptime target | 99.9% |

---

## 4. Google Docs

### Core Problem
Real-time collaborative editing requires convergence, conflict resolution, real-time visibility, and offline support.

### Approaches Evaluated

| Approach | Verdict | Why |
|----------|---------|-----|
| Pessimistic Locking | Rejected | Only one user edits at a time; no offline |
| Last-Write-Wins | Rejected | Risk of data loss in high-latency networks |
| Differential Sync | Evaluated | Performance cost from computing diffs; manual conflict handling |
| **Operational Transformation** | **Selected** | Optimistic concurrency; automatic conflict resolution |

### Operational Transformation (OT)
- Allows simultaneous writes across multiple document copies
- Automatic conflict resolution without locks or user intervention
- Documents represented as **revision logs**; replay from start for display
- Tolerates temporary divergence; guarantees eventual convergence

### Latency Hiding
To address 200ms round-trip times, the system maintains local document copies and executes operations immediately, creating responsiveness illusion while propagating changes asynchronously.

### Key Trade-offs
- **Consistency vs. Responsiveness:** Local-first execution sacrifices immediate global consistency
- **Simplicity vs. Conflict Resolution:** OT adds complexity but enables automatic conflict handling
- **Storage vs. Computation:** Revision logs enable replay-based convergence at storage cost

---

## 5. Apache Kafka

### Core Architecture
A **log data structure** — append-only, distributed storage indexed by monotonically increasing offsets.

### Key Components

**Brokers & Clusters**
- Minimum 3 broker nodes; configurable replication factor (default: 3)
- Only the leader accepts writes — single source of truth
- Followers replicate data and serve reads

**Topics & Partitions**
- Topics sharded into partitions for horizontal scalability
- Each partition is an independent log instance

**Controllers (KRaft)**
- Dedicated control-plane brokers via KRaft consensus (replacing ZooKeeper)
- `__cluster_metadata` topic stores all cluster state changes as ordered events
- Broker fencing after 6 consecutive seconds without heartbeat

### Exactly-Once Processing
- Two-phase commit for atomic multi-partition writes
- Producer deduplication via monotonic IDs and epoch tracking
- Achievable when all reads/writes remain within Kafka

### Tiered Storage
- Hot tier: broker disks (recent data)
- Cold tier: S3/object storage (historical data)
- **10x cheaper** than disk-only retention
- Maintains O(1) performance across tiers

### Ecosystem
- **Kafka Streams:** Client-side stream processing (windowing, joins, aggregations)
- **Kafka Connect:** Source/sink connectors for external system integration
- **Schema Registry:** External HTTP service for schema management

### Scale Metrics
| Metric | Value |
|--------|-------|
| Adoption | 70% of Fortune 500, 150K+ organizations |
| Throughput | Linearly scalable (50 GiB/s → 100 GiB/s by doubling cluster) |
| Replication | Default 3x across separate AZs |
| Default retention | 7 days |

---

## 6. URL Shortener

### Architecture Overview
Four core operations: generate unique short URLs, encode for readability, persist mappings, redirect clients.

### Three Shortening Approaches

| Approach | Pros | Cons |
|----------|------|------|
| Random UUID | Simple | Collision risk; requires DB verification |
| Hashing (MD5/SHA256) | Deterministic | Predictable; truncation causes collisions |
| **Token Range** (recommended) | Collision-free; scalable | Requires coordination service |

### Token Range Service
- Monotonically increasing counter distributed across instances
- Non-overlapping ranges per instance; exhausted ranges trigger fresh requests
- Coordination via Apache ZooKeeper or DynamoDB

### Encoding: Base62
- 7-character length → 62^7 = **3.5 trillion combinations**
- All alphanumeric; O(1) time complexity

### Dual Database Strategy
- **NoSQL (DynamoDB/MongoDB):** URL table — flexible schema, high throughput
- **SQL (PostgreSQL/MySQL):** Users table — ACID compliance, complex joins
- **Inverted index:** Separate key-value store mapping long_url → short_url

### Collision Prevention
1. **Bloom filter** checks long URL existence (O(1))
2. **Distributed lock** (Redis/Chubby) acquired on long URL
3. False positives trigger database lookups

### Caching Strategy
- Cache-aside with LRU eviction
- Bloom filter prevents cache thrashing (only cache after 2+ accesses)
- Request collapse forwards duplicate concurrent requests as single query
- Layers: client-side → CDN → reverse proxy → dedicated cache servers

### Analytics Pipeline
```
Redirect Request → Extract Headers → Kafka → Archive Service → HDFS/Data Warehouse → MapReduce
```

### Scale Metrics
| Metric | Value |
|--------|-------|
| DAU | 100M |
| Read:write ratio | 100:1 |
| QPS (reads) | ~100,000 |
| Short URL length | 7 characters |
| Record size | ~2.5 KB |
| 5-year storage | ~1.875 PB (3x replicated) |
| Cache memory (20% hot) | ~5 TB |

---

## 7. WhatsApp

### Architecture Overview
Distributed, layered architecture for **1 billion registered users**, **500 million DAU**, and **50 million concurrent peak connections**.

### Protocol: WebSockets
| Alternative | Why Rejected |
|------------|-------------|
| Polling | Wastes bandwidth with empty responses |
| Long polling | Full HTTP handshake per message |
| **WebSockets** | Persistent bidirectional; minimal per-message overhead |

Heartbeat pings every 30 seconds; server closes after 60 seconds without response.

### Data Models
| Store | Technology | Purpose |
|-------|-----------|---------|
| Users | PostgreSQL | Identity, auth, profiles |
| Messages | Cassandra | Partition by conversation; clustering by timestamp |
| Connections | Redis | user_id → chat_server_address; O(1) routing |
| Offline inbox | Redis | 30-day retention for undelivered messages |

### Message Flow
1. Client → Chat server (WebSocket)
2. Server acknowledges immediately
3. Message pushed to queue (Kafka/RabbitMQ)
4. Storage service persists to Cassandra
5. Online recipient: delivered through WebSocket
6. Offline recipient: stored in inbox → push notification (APNs/FCM)

### Delivery Status Tracking
- **Sent:** Accepted by server
- **Delivered:** Received by recipient device
- **Read:** User opened chat

### Scale Metrics
| Metric | Value |
|--------|-------|
| Daily messages | 10 billion |
| Average throughput | 115,000 msg/sec |
| Peak throughput | 350,000-500,000 msg/sec |
| Daily storage | ~10 TB |
| Active storage | 400-500 TB (30-day retention) |
| Group limit | 100 participants |

---

## 8. Airbnb

### Architecture Overview
**Service-oriented architecture** with shared transactional data for tightly coupled domains. Key insight: reservation and inventory data live in the same database for local ACID transactions.

### Core Services
- **Hotel Service:** Static info (heavily cacheable)
- **Rate Service:** Dynamic pricing by date/demand
- **Reservation Service:** Booking logic, concurrency handling
- **Payment Service:** Gateway integration
- **Search Service:** Elasticsearch for discovery

### Critical Design: Strong Consistency
Rather than saga patterns or two-phase commit, the architecture keeps reservation + inventory in **one PostgreSQL database** for local ACID guarantees. This prevents double bookings.

### Idempotency Keys
Frontend-generated idempotency keys prevent duplicate bookings from double-clicks — critical for payment operations.

### Scale Metrics
| Metric | Value |
|--------|-------|
| Bookings/day | ~1.5M |
| Write TPS | ~17 |
| Read RPS | ~1,000 |
| Read:write ratio | ~60:1 |
| Inventory rows | 620M |
| Search latency target | <500ms |
| Booking confirmation | 2-3 seconds |
| Uptime | 99.9%+ |

### Key Trade-off
Shared database sacrifices microservices purity for **correctness** at moderate write volumes (17 TPS). Distributed transactions would introduce more risk than benefit.

---

## 9. Spotify

### Architecture Overview
Distributed, **stateless microservices** optimized for audio streaming at scale.

### Audio Streaming
- **Adaptive bitrate** via HLS/DASH
- Three quality tiers: 64kbps (mobile), 128kbps (standard), 320kbps (premium)
- Hierarchical blob storage: `/artist/album/song.ogg`
- **Signed URLs** with expiration (hours) for access control
- Range requests for chunk-based delivery

### Data Flow: Song Playback
1. User initiates playback → `GET /songs/{id}`
2. JWT validation at API server
3. Metadata lookup in SQL database
4. Signed URL generation for blob storage
5. Client fetches audio chunks via HTTP streaming
6. Analytics tracking via `POST /songs/{id}/play`

### Reliability Patterns
- Circuit breakers prevent cascading failures
- Connection pooling optimizes DB resources
- Fallback mechanisms for non-critical services
- Load balancer health checks every 30 seconds

### Storage
| Type | Size |
|------|------|
| Audio (30M songs) | 90 TB base (2-3x with replication) |
| Song metadata | ~3 GB |
| User metadata | ~0.5 GB |

---

## 10. Slack

### Architecture Overview
Hybrid email/IRC with client-server architecture supporting real-time messaging via WebSockets.

### Key Components

**Data Layer**
- MySQL (source of truth) sharded by channel_id
- **Vitess** for transparent horizontal scaling and automatic re-sharding
- Redis cache for materialized SQL views
- Apache Solr for search (partitioned by channel_id)

**Real-time Platform**
- **Gateway servers:** Stateful in-memory services with channel-to-client connection maps
- **Envoy edge proxies:** SSL termination, WebSocket proxying, consistent hashing
- **Snapshot service:** Application-level edge query engine with lazy loading

**Message Distribution**
- Pub-sub pattern **without message brokers** (reduces operational complexity)
- Dispatcher service queries endpoint store for subscriber discovery
- Cross-data center subscription model

### Message Ordering
**Logical clocks** (Lamport/Vector) instead of timestamps — preserves message causality in distributed contexts and avoids clock skew.

### Pagination
**Cursor-based** with Base64-encoded offsets — scalable through database index leverage; prevents duplicates during high-frequency writes.

### Replication
Active-active topology with **single leader and orchestrator** (replacing leader-leader) for automated failover and reduced complexity.

### Scale Metrics
| Metric | Value |
|--------|-------|
| DAU writes | 1 billion messages |
| Write QPS | 12,000 msg/sec |
| Read:write ratio | 10:1 |
| Daily storage | ~100 GB |
| 5-year storage | ~150 TB (3x replication) |
| Organizations | 500,000+ |

### Performance Optimizations
- Lazy loading of workspace snapshots
- Incremental updates via cached timestamps
- Just-in-time annotation (proactive data push)
- Thrift over JSON for event format
- Adaptive replacement cache (ARC) eviction
- Viewport-aware presence subscriptions
- Jitter on client reconnection (prevents thundering herd)

---

## 11. Reddit

### Architecture Evolution
From single-machine PostgreSQL to distributed system serving **100 million daily users**.

### Database Scaling Journey
1. **Monolithic PostgreSQL** → hit vertical limits
2. **Partitioned database** → scaled writes
3. **Read replicas** → distributed read traffic
4. **Denormalized cache** → pre-computed rankings

### Voting System: Queue Partitioning
**Problem:** Lock contention skyrocketed during peak traffic when processors competed for locks on popular posts.

**Solution:**
- Votes routed to queues based on `subreddit_id % N`
- Multiple processors handle separate queues independently
- **ZooKeeper** manages distributed locks for atomic read-mutate-write operations
- Result: fewer processors contend for the same lock

### Pre-computed Lists
Rankings computed asynchronously via job queues and stored on cache servers. Votes invalidate cache entries, triggering recalculation.

### Technologies
| Component | Technology |
|-----------|-----------|
| Primary DB | PostgreSQL |
| Durability | Cassandra |
| Distributed locking | ZooKeeper |
| Cache | Custom (likely Memcached/Redis) |

### Key Trade-offs
| Decision | Benefit | Cost |
|----------|---------|------|
| Pre-computed lists | Low-latency reads | Stale data, cache invalidation complexity |
| Async job processing | User responsiveness | Eventual consistency |
| Queue partitioning | Reduced contention | Consistent hashing complexity |

---

## 12. Bluesky

### Architecture Overview
**Federated decentralized** architecture on the Authenticated Transfer Protocol (ATProto). Servers distribute messages to each other; users' data is portable across apps.

### Key Components

**User Repositories**
- Individual **SQLite databases** per user
- Data encoded in **CBOR** (compact binary format)
- Stores primary data (posts); not follower actions

**Personal Data Servers (PDS)**
- Host multiple user repositories
- "6 million user repositories on a single server at **$150/month**"
- Enable repository portability between servers

**Crawler (Relay)**
- WebSocket subscriptions for real-time updates
- Combines each user's actions into a single TCP connection
- Generates unified stream without indexing

**Index Server (App View)**
- Built in **Go** for concurrency
- **ScyllaDB** (NoSQL) for horizontal scalability
- **Redis** cache for popular results
- Most read-heavy service

### Social Proof: Roaring Bitmaps
Optimized set intersection for "mutual followers" using compressed bitmap structures that adapt storage by data sparsity:
- Dense data → fixed-size bit arrays
- Contiguous integers → run-length encoding
- Sparse data → sorted integer arrays

### Decentralized Identity (DID)
- Posts stored using immutable DIDs
- Handles are mutable and reassignable
- DNS TXT records verify custom domain handles

### Video Streaming
HLS with adaptive bitrate: 480p, 720p, 1080p in 5-second chunks. View tracking via last fetched segment.

---

## 13. Tinder

### Architecture Overview
~**500 microservices** handling **1.6 billion daily swipes** and **26 million daily matches**.

### Geospatial Indexing: Google S2
- Square-shaped hierarchical system using **Hilbert curve** (preserves spatial locality)
- 64-bit cell identifiers at variable resolutions
- Average **3 database shards** queried to find users within 160 km

### Matching Pipeline
1. Swipes ingested via **Amazon Kinesis**
2. Match workers check Likes cache
3. **WebSockets** deliver real-time match notifications
4. Disliked profiles stored in **S3** for analytics

### Hot Shard Problem
Geographic sharding creates traffic imbalances due to time zones. Solution: randomly assign multiple shards to single physical servers, distributing peak loads.

### Data Consistency
Initially faced ordering issues with rapid location changes. Solution: **Apache Kafka** with FIFO ordering guarantees. Consumers acquire partition locks ensuring sequential processing per user.

### Technologies
| Component | Technology |
|-----------|-----------|
| Geospatial | Google S2 Library |
| Stream processing | Amazon Kinesis |
| Ordering | Apache Kafka |
| Cache | Redis (cache-aside pattern) |
| Real-time | WebSockets |
| Analytics storage | Amazon S3 |

---

## 14. Twitter/X Timeline

### Architecture Overview (Frontend Focus)
**Layered SPA** with four tiers: View (React), Store (Redux/Zustand), Data Access (RTK Query/Relay), Server.

### Key Decisions

**Client-Side Rendering (CSR)**
Chosen over SSR because timelines are heavily personalized — "SSR benefits don't outweigh the complexity."

**Data Normalization**
Entities (tweets, users, timelines) stored separately with ID-based references. Profile changes update once, reflected everywhere automatically.

**Cursor-Based Pagination**
Doesn't depend on dataset size; handles real-time updates where new tweets appear constantly.

### Performance Optimizations
| Technique | How It Works |
|-----------|-------------|
| Code splitting | Lazy-load route-specific JavaScript |
| List virtualization | Render only visible items; invisible placeholders maintain scroll |
| Optimistic updates | Immediate local reflection before server confirmation; auto-rollback on failure |
| LQIP | Low Quality Image Placeholders with progressive decoding |
| Skeleton screens | Loading states instead of spinners |

### Key Insight
The frontend is "a distributed system in its own right" — managing state, orchestrating fetching, caching, handling concurrency, and maintaining real-time sync.

---

## 15. Uber Nearby Drivers

### Scale
**1 million requests per second** for finding nearby drivers.

### Geospatial Indexing: Uber H3
- **Hexagonal** grid (vs. S2's squares) — "each neighboring cell is the same distance from center"
- 16 resolution levels (1 sq meter to continental)
- 122 base cells globally (12 pentagons due to sphere geometry)
- 64-bit integer identifiers; resolution switching via bitwise truncation

### Location Storage
- **Apache Cassandra:** Durable storage optimized for write-heavy operations
- **Redis:** Buffers recent driver locations for read performance
- **Map matching:** Transforms noisy GPS signals into accurate road segments
- Flow: Raw GPS → Redis buffer → map-matched → Cassandra

### Query Processing
1. Identify H3 cells covering rider's location
2. List drivers in relevant cells (using H3 cell ID as shard key)
3. Sort candidates by estimated time of arrival (ETA)

### H3 vs. S2 Comparison
| Feature | H3 (Uber) | S2 (Tinder) |
|---------|-----------|-------------|
| Grid shape | Hexagons | Squares |
| Neighbor distance | Uniform | Variable |
| Developer | Uber | Google |
| Sphere tiling | Imperfect (12 pentagons) | Complete |

---

## 16. AWS Lambda

### Architecture Overview
Four core components handling **10 trillion requests per month**.

### Components
| Component | Role |
|-----------|------|
| **Invoke Service** | Routes requests to workers; returns results |
| **Assignment Service** | Tracks worker-function mapping; leader-follower pattern |
| **Worker** | EC2 instances running multiple isolated microVMs |
| **Journal Log** | External durable storage for fault-tolerant metadata |

### Firecracker MicroVMs
Lightweight VMs isolating customer workloads while maximizing resource utilization on single workers.

### Cold Start Optimization
| Technique | Impact |
|-----------|--------|
| Warm starts | 99% of requests reuse existing microVMs |
| Snapshot restoration | 90% cold start latency reduction |
| Lazy loading | Only download needed container image chunks |

### Key Design Decisions
- Microservices for independent scaling
- Tenant isolation via microVMs (not separate workers) for cost efficiency
- Journal log persistence for resilience
- Snapshot-based cold starts over traditional provisioning

---

## 17. Amazon S3

### Architecture Overview
Distributed, microservices-based design with **separated metadata and file content** for independent scaling.

### Key Innovation: ShardStore
A variant of **log-structured merge (LSM) tree** optimized for mechanical hard disks, addressing inherent seek/rotation time limitations.

### Performance: Parallel Disk Reads
- Data replicated across multiple disks
- Parallel reads increase aggregate throughput
- Prevents hot spots; maintains availability despite disk failures

### Erasure Coding
Instead of full 3-way replication, S3 uses **erasure coding** — providing durability with smaller storage overhead. Trades computational complexity for storage efficiency.

### Key Trade-offs
| Decision | Benefit |
|----------|---------|
| Mechanical HDDs | Cost efficiency at massive scale |
| Erasure coding | Reduced storage overhead vs. full replication |
| Separated metadata/content | Independent scaling |
| Parallel reads | Throughput optimization |

---

## 18. Apple AirTags

### Architecture Overview
Uses **Bluetooth Low Energy (BLE)** instead of GPS/WiFi/cellular — minimizing power consumption and cost.

### Crowdsourced Tracking Model
AirTag doesn't send location data. It broadcasts only its **public key**. Nearby iPhones encrypt their own location with the received key and upload to Apple servers. Only the owner's private key can decrypt.

### Data Flow
1. **Setup:** Elliptic curve cryptography generates key pairs; shared with user account
2. **Broadcasting:** AirTag broadcasts public key every 2 seconds via BLE
3. **Relay:** Nearby iPhones receive broadcast, encrypt own location + timestamp with public key, upload to Apple servers
4. **Recovery:** Owner decrypts location data using private key

### Security Model
- Public key = broadcast identifier (like email address)
- Private key = only owner can decrypt (like inbox password)
- Digital signatures verify authenticity
- End-to-end encryption; Apple cannot see location data

### Key Insight
Inverts traditional tracking — the tag broadcasts identity, not position. Leverages the massive iPhone install base as a passive relay network.

---

## 19. Large Language Models (LLMs)

### Architecture Overview
LLMs function as "a powerful autocomplete system" predicting tokens sequentially.

### Processing Pipeline
1. **Tokenization:** Text → numerical tokens
2. **Embeddings:** Tokens → vector representations encoding semantic meaning
3. **Latent Space:** Mathematical space where embeddings organize by relationships
4. **Parameters:** Billions of internal variables encoding learned patterns

### Training Stages
1. Pre-training on massive internet datasets
2. Fine-tuning on task-specific data
3. Alignment via RLHF (Reinforcement Learning from Human Feedback)

### Key Concepts
| Concept | Description |
|---------|-------------|
| RAG | Retrieve → Augment → Generate; grounds outputs in external sources |
| Chain-of-Thought | Prompting for complex step-by-step reasoning |
| Few-shot learning | Examples guide model behavior |
| Temperature | Controls output randomness (deterministic vs. stochastic) |
| Context window | Token limit for visible history |
| Agents | Adaptive multi-step autonomous task planning |

### Model Variants
- Base vs. Instruct (conversation-optimized)
- Proprietary vs. open-weight vs. open-source
- Small Language Models (SLMs): <15B parameters for efficiency

### Failure Modes & Mitigations
| Failure | Mitigation |
|---------|-----------|
| Hallucination | RAG and grounding |
| Poor reasoning | External tools (calculators, interpreters) |
| Bias | RLHF and safety guardrails |
| Knowledge cutoff | Retrieval, fine-tuning, web integration |

---

## 20. Cross-Cutting Patterns & Lessons

### Universal Architecture Patterns

#### 1. Pagination: Cursor-Based Wins
Every case study that discusses pagination chooses **cursor-based over offset-based**:
- **Slack:** Base64-encoded offsets leveraging database indexes
- **Bluesky:** Sequential unique columns preventing full table scans
- **Twitter:** Handles real-time updates where new items appear constantly
- **URL Shortener:** Prevents duplicates during high-frequency writes

#### 2. Real-Time Communication: WebSockets Dominate
- **WhatsApp:** Persistent bidirectional channels; heartbeat every 30s
- **Slack:** Gateway servers with channel-to-client connection maps
- **Tinder:** Real-time match notifications
- **Stock Exchange:** Market data streaming

#### 3. Geospatial Indexing: Hierarchical Grids
| System | Library | Grid Shape | Use Case |
|--------|---------|-----------|----------|
| Tinder | Google S2 | Squares | User matching within 160km |
| Uber | H3 | Hexagons | Driver discovery at 1M req/sec |
| AirTags | BLE proximity | N/A | Crowdsourced relay network |

#### 4. Event Streaming: Kafka Everywhere
Used across: Stock Exchange, Tinder, WhatsApp, URL Shortener, Slack. Common purposes:
- Ordering guarantees (Stock Exchange, Tinder)
- Decoupling components (URL Shortener analytics)
- Async processing (WhatsApp message persistence)

#### 5. Caching Strategy: Cache-Aside Pattern
Dominant pattern across systems:
- **Tinder:** Redis for read-heavy workloads
- **URL Shortener:** Multi-layer (client → CDN → reverse proxy → dedicated cache)
- **Slack:** Redis for materialized SQL views with ARC eviction
- **Bluesky:** Redis for popular index server results
- **Reddit:** Denormalized pre-computed rankings

### Database Selection Patterns

| Workload | Choice | Examples |
|----------|--------|----------|
| Write-heavy, high throughput | Cassandra/DynamoDB | WhatsApp messages, Uber locations, YouTube progress |
| Transactional integrity | PostgreSQL/MySQL | Airbnb reservations, WhatsApp users, Reddit accounts |
| Search/discovery | Elasticsearch/Solr | Airbnb search, Slack message search |
| Real-time state | Redis | WhatsApp connections, Tinder likes cache, Uber GPS buffer |
| User data (decentralized) | SQLite | Bluesky user repositories |
| Cluster metadata | ScyllaDB | Bluesky index server |

### Scalability Strategies Ranked by Frequency

1. **Horizontal sharding** — Slack (channel_id), URL Shortener (short_url), Uber (H3 cell ID), Tinder (S2 cell ID)
2. **Read replicas** — Reddit, Slack (CQRS), Airbnb
3. **CDN offloading** — YouTube, Spotify, WhatsApp media, Bluesky video
4. **Async job queues** — Reddit (voting), URL Shortener (analytics), WhatsApp (persistence)
5. **Pre-computation** — Reddit (rankings), Slack (snapshots), URL Shortener (Bloom filters)

### Consistency vs. Availability Trade-offs

| System | Choice | Rationale |
|--------|--------|-----------|
| Airbnb | **Strong consistency** | Double-booking is unacceptable |
| YouTube | **Eventual consistency** | New uploads can be delayed |
| WhatsApp | **Eventual with ordering** | Messages must arrive in order |
| Stock Exchange | **Deterministic ordering** | Financial fairness requirements |
| Reddit | **Eventual** | Stale rankings acceptable briefly |
| Slack | **Logical clocks** | Causality preservation over wall-clock time |

### Security Patterns

| Pattern | Used By |
|---------|---------|
| Tokenization (PCI) | Uber Payments |
| Signed/Pre-signed URLs | YouTube, Spotify, WhatsApp media |
| End-to-end encryption | AirTags (public/private key pairs) |
| JWT authentication | Spotify, Bluesky |
| Rate limiting | URL Shortener, Tinder, Slack |

### Cost Optimization Techniques

| Technique | System | Savings |
|-----------|--------|---------|
| Tiered storage | Kafka | 10x cheaper than all-disk |
| Erasure coding | S3 | Less overhead than 3x replication |
| CBOR encoding | Bluesky | Compact binary vs. JSON |
| Pre-signed URL bypass | YouTube | Eliminates app server bandwidth |
| Snapshot restoration | AWS Lambda | 90% cold start reduction |
| SQLite per-user | Bluesky | 6M repos at $150/month |
| MicroVMs | AWS Lambda | Multi-tenant on single EC2 |

### Message Ordering Solutions

| System | Approach |
|--------|----------|
| Slack | Lamport/Vector logical clocks |
| Stock Exchange | Global increasing sequence numbers |
| Tinder | Kafka partition locks |
| WhatsApp | Cassandra clustering by timestamp |
| Kafka | Monotonically increasing offsets per partition |

---

## Quick Reference: Technologies by Category

### Databases
| Technology | Type | Used By |
|-----------|------|---------|
| PostgreSQL | Relational | Airbnb, WhatsApp, Reddit |
| MySQL | Relational | Slack |
| Cassandra | Wide-column | WhatsApp, Uber, Reddit |
| DynamoDB | Key-value | YouTube, Tinder, URL Shortener |
| ScyllaDB | Wide-column | Bluesky |
| SQLite | Embedded | Bluesky |
| Elasticsearch | Search | Airbnb |
| Apache Solr | Search | Slack |

### Caching
| Technology | Used By |
|-----------|---------|
| Redis | Slack, Tinder, Uber, Bluesky, WhatsApp, URL Shortener |
| Memcached | URL Shortener (alternative) |

### Streaming & Messaging
| Technology | Used By |
|-----------|---------|
| Apache Kafka | Stock Exchange, Tinder, WhatsApp, URL Shortener, Slack, Kafka (itself) |
| Amazon Kinesis | Tinder |
| RabbitMQ | WhatsApp (alternative) |

### Infrastructure
| Technology | Used By |
|-----------|---------|
| Vitess | Slack (MySQL scaling) |
| Envoy | Slack (edge proxy) |
| Consul | Slack, WhatsApp (service discovery) |
| ZooKeeper | URL Shortener, Reddit (coordination/locking) |
| Firecracker | AWS Lambda (microVMs) |

### Protocols
| Protocol | Used By |
|---------|---------|
| WebSocket | WhatsApp, Slack, Tinder, Stock Exchange, Bluesky |
| FIX | Stock Exchange |
| HLS | Spotify, Bluesky (video) |
| BLE | AirTags |
| ATProto | Bluesky |
