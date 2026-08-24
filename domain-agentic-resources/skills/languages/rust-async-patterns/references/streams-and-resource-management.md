# Rust Async Patterns: Streams and Resource Management

Async streams with `async-stream` and `futures::StreamExt`, connection pool implementation with `Semaphore`, and `RwLock`-based shared cache.

## Pattern 6: Streams and Async Iteration

```rust
use futures::stream::{self, Stream, StreamExt};
use async_stream::stream;

// Create stream from async iterator
fn numbers_stream() -> impl Stream<Item = i32> {
    stream! {
        for i in 0..10 {
            tokio::time::sleep(Duration::from_millis(100)).await;
            yield i;
        }
    }
}

// Process stream
async fn process_stream() {
    let stream = numbers_stream();

    // Map and filter
    let processed: Vec<_> = stream
        .filter(|n| futures::future::ready(*n % 2 == 0))
        .map(|n| n * 2)
        .collect()
        .await;

    println!("{:?}", processed);
}

// Chunked processing
async fn process_in_chunks() {
    let stream = numbers_stream();

    let mut chunks = stream.chunks(3);

    while let Some(chunk) = chunks.next().await {
        println!("Processing chunk: {:?}", chunk);
    }
}

// Merge multiple streams
async fn merge_streams() {
    let stream1 = numbers_stream();
    let stream2 = numbers_stream();

    let merged = stream::select(stream1, stream2);

    merged
        .for_each(|n| async move {
            println!("Got: {}", n);
        })
        .await;
}
```

## Pattern 7: Resource Management

```rust
use std::sync::Arc;
use tokio::sync::{Mutex, RwLock, Semaphore};

// Shared state with RwLock (prefer for read-heavy)
struct Cache {
    data: RwLock<HashMap<String, String>>,
}

impl Cache {
    async fn get(&self, key: &str) -> Option<String> {
        self.data.read().await.get(key).cloned()
    }

    async fn set(&self, key: String, value: String) {
        self.data.write().await.insert(key, value);
    }
}

// Connection pool with semaphore
struct Pool {
    semaphore: Semaphore,
    connections: Mutex<Vec<Connection>>,
}

impl Pool {
    fn new(size: usize) -> Self {
        Self {
            semaphore: Semaphore::new(size),
            connections: Mutex::new((0..size).map(|_| Connection::new()).collect()),
        }
    }

    async fn acquire(&self) -> PooledConnection<'_> {
        let permit = self.semaphore.acquire().await.unwrap();
        let conn = self.connections.lock().await.pop().unwrap();
        PooledConnection { pool: self, conn: Some(conn), _permit: permit }
    }
}

struct PooledConnection<'a> {
    pool: &'a Pool,
    conn: Option<Connection>,
    _permit: tokio::sync::SemaphorePermit<'a>,
}

impl Drop for PooledConnection<'_> {
    fn drop(&mut self) {
        if let Some(conn) = self.conn.take() {
            let pool = self.pool;
            tokio::spawn(async move {
                pool.connections.lock().await.push(conn);
            });
        }
    }
}
```
