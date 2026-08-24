---
name: memory-safety-patterns
description: Implement memory-safe programming with RAII, ownership, smart pointers, and resource management across Rust, C++, and C. Use when writing safe systems code, managing resources, or preventing memory bugs.
metadata:
  tags:
    - memory
    - rust
    - safety
  updated: "2026-04-11"
---
# Memory Safety Patterns

Cross-language patterns for memory-safe programming including RAII, ownership, smart pointers, and resource management.

## When to Use This Skill

- Writing memory-safe systems code
- Managing resources (files, sockets, memory)
- Preventing use-after-free and leaks
- Implementing RAII patterns
- Choosing between languages for safety
- Debugging memory issues

## Core Concepts

### 1. Memory Bug Categories

| Bug Type | Description | Prevention |
|----------|-------------|------------|
| **Use-after-free** | Access freed memory | Ownership, RAII |
| **Double-free** | Free same memory twice | Smart pointers |
| **Memory leak** | Never free memory | RAII, GC |
| **Buffer overflow** | Write past buffer end | Bounds checking |
| **Dangling pointer** | Pointer to freed memory | Lifetime tracking |
| **Data race** | Concurrent unsynchronized access | Ownership, Sync |

### 2. Safety Spectrum

```
Manual (C) → Smart Pointers (C++) → Ownership (Rust) → GC (Go, Java)
Less safe                                              More safe
More control                                           Less control
```

## Patterns by Language

### Pattern 1: RAII in C++

```cpp
// RAII: Resource Acquisition Is Initialization
// Resource lifetime tied to object lifetime

#include <memory>
#include <fstream>
#include <mutex>

// File handle with RAII
class FileHandle {
public:
    explicit FileHandle(const std::string& path)
        : file_(path) {
        if (!file_.is_open()) {
            throw std::runtime_error("Failed to open file");
        }
    }

    // Destructor automatically closes file
    ~FileHandle() = default; // fstream closes in its destructor

    // Delete copy (prevent double-close)
    FileHandle(const FileHandle&) = delete;
    FileHandle& operator=(const FileHandle&) = delete;

    // Allow move
    FileHandle(FileHandle&&) = default;
    FileHandle& operator=(FileHandle&&) = default;

    void write(const std::string& data) {
        file_ << data;
    }

private:
    std::fstream file_;
};

// Lock guard (RAII for mutexes)
class Database {
public:
    void update(const std::string& key, const std::string& value) {
        std::lock_guard<std::mutex> lock(mutex_); // Released on scope exit
        data_[key] = value;
    }

    std::string get(const std::string& key) {
        std::shared_lock<std::shared_mutex> lock(shared_mutex_);
        return data_[key];
    }

private:
    std::mutex mutex_;
    std::shared_mutex shared_mutex_;
    std::map<std::string, std::string> data_;
};

// Transaction with rollback (RAII)
template<typename T>
class Transaction {
public:
    explicit Transaction(T& target)
        : target_(target), backup_(target), committed_(false) {}

    ~Transaction() {
        if (!committed_) {
            target_ = backup_; // Rollback
        }
    }

    void commit() { committed_ = true; }

    T& get() { return target_; }

private:
    T& target_;
    T backup_;
    bool committed_;
};
```

### Pattern 2: Smart Pointers in C++

```cpp
#include <memory>

// unique_ptr: Single ownership
class Engine {
public:
    void start() { /* ... */ }
};

class Car {
public:
    Car() : engine_(std::make_unique<Engine>()) {}

    void start() {
        engine_->start();
    }

    // Transfer ownership
    std::unique_ptr<Engine> extractEngine() {
        return std::move(engine_);
    }

private:
    std::unique_ptr<Engine> engine_;
};

// shared_ptr: Shared ownership
class Node {
public:
    std::string data;
    std::shared_ptr<Node> next;

    // Use weak_ptr to break cycles
    std::weak_ptr<Node> parent;
};

void sharedPtrExample() {
    auto node1 = std::make_shared<Node>();
    auto node2 = std::make_shared<Node>();

    node1->next = node2;
    node2->parent = node1; // Weak reference prevents cycle

    // Access weak_ptr
    if (auto parent = node2->parent.lock()) {
        // parent is valid shared_ptr
    }
}

// Custom deleter for resources
class Socket {
public:
    static void close(int* fd) {
        if (fd && *fd >= 0) {
            ::close(*fd);
            delete fd;
        }
    }
};

auto createSocket() {
    int fd = socket(AF_INET, SOCK_STREAM, 0);
    return std::unique_ptr<int, decltype(&Socket::close)>(
        new int(fd),
        &Socket::close
    );
}

// make_unique/make_shared best practices
void bestPractices() {
    // Good: Exception safe, single allocation
    auto ptr = std::make_shared<Widget>();

    // Bad: Two allocations, not exception safe
    std::shared_ptr<Widget> ptr2(new Widget());

    // For arrays
    auto arr = std::make_unique<int[]>(10);
}
```

### Pattern 3: Ownership in Rust

```rust
// Move semantics (default)
fn move_example() {
    let s1 = String::from("hello");
    let s2 = s1; // s1 is MOVED, no longer valid

    // println!("{}", s1); // Compile error!
    println!("{}", s2);
}

// Borrowing (references)
fn borrow_example() {
    let s = String::from("hello");

    // Immutable borrow (multiple allowed)
    let len = calculate_length(&s);
    println!("{} has length {}", s, len);

    // Mutable borrow (only one allowed)
    let mut s = String::from("hello");
    change(&mut s);
}

fn calculate_length(s: &String) -> usize {
    s.len()
} // s goes out of scope, but doesn't drop since borrowed

fn change(s: &mut String) {
    s.push_str(", world");
}

// Lifetimes: Compiler tracks reference validity
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}

// Struct with references needs lifetime annotation
struct ImportantExcerpt<'a> {
    part: &'a str,
}

impl<'a> ImportantExcerpt<'a> {
    fn level(&self) -> i32 {
        3
    }

    // Lifetime elision: compiler infers 'a for &self
    fn announce_and_return_part(&self, announcement: &str) -> &str {
        println!("Attention: {}", announcement);
        self.part
    }
}

// Interior mutability
use std::cell::{Cell, RefCell};
use std::rc::Rc;

struct Stats {
    count: Cell<i32>,           // Copy types
    data: RefCell<Vec<String>>, // Non-Copy types
}

impl Stats {
    fn increment(&self) {
        self.count.set(self.count.get() + 1);
    }

    fn add_data(&self, item: String) {
        self.data.borrow_mut().push(item);
    }
}

// Rc for shared ownership (single-threaded)
fn rc_example() {
    let data = Rc::new(vec![1, 2, 3]);
    let data2 = Rc::clone(&data); // Increment reference count

    println!("Count: {}", Rc::strong_count(&data)); // 2
}

// Arc for shared ownership (thread-safe)
use std::sync::Arc;
use std::thread;

fn arc_example() {
    let data = Arc::new(vec![1, 2, 3]);

    let handles: Vec<_> = (0..3)
        .map(|_| {
            let data = Arc::clone(&data);
            thread::spawn(move || {
                println!("{:?}", data);
            })
        })
        .collect();

    for handle in handles {
        handle.join().unwrap();
    }
}
```

## Additional Patterns

Safe C resource management (goto cleanup, opaque pointers, cleanup attributes), bounds checking in C++ and Rust, and data race prevention with atomics and locks.

See [references/c-bounds-and-data-race-patterns.md](references/c-bounds-and-data-race-patterns.md)

## Best Practices

### Do's
- **Prefer RAII** - Tie resource lifetime to scope
- **Use smart pointers** - Avoid raw pointers in C++
- **Understand ownership** - Know who owns what
- **Check bounds** - Use safe access methods
- **Use tools** - AddressSanitizer, Valgrind, Miri

### Don'ts
- **Don't use raw pointers** - Unless interfacing with C
- **Don't return local references** - Dangling pointer
- **Don't ignore compiler warnings** - They catch bugs
- **Don't use `unsafe` carelessly** - In Rust, minimize it
- **Don't assume thread safety** - Be explicit

## Debugging Tools

```bash
# AddressSanitizer (Clang/GCC)
clang++ -fsanitize=address -g source.cpp

# Valgrind
valgrind --leak-check=full ./program

# Rust Miri (undefined behavior detector)
cargo +nightly miri run

# ThreadSanitizer
clang++ -fsanitize=thread -g source.cpp
```

## Resources

- [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/)
- [Rust Ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html)
- [AddressSanitizer](https://clang.llvm.org/docs/AddressSanitizer.html)
