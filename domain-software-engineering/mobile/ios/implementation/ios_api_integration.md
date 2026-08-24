---
title: "iOS API Integration"
category: mobile-development
description: "Implement robust URLSession networking with async/await, Codable parsing, auth token interceptors, retry logic, and structured error mapping."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-04
  - ST-03
  - NE-02
difficulty: intermediate
tags:
  - ios
  - swift
  - networking
  - urlsession
  - async-await
  - codable
  - mobile-development
updated: "2026-03-19"
---

# iOS API Integration

**Objective:** Implement a robust, type-safe REST API integration using URLSession with async/await, Codable models, authentication token interceptors, automatic retry logic, and structured error mapping following modern Swift concurrency patterns.

**When to Use:** Use this prompt when integrating with REST APIs in an iOS application. Ideal for new API integrations, refactoring legacy networking code, or adding authentication, caching, or retry logic. Best used after API endpoints and data contracts are defined.

**Prompt Type:** Comprehensive (400-500 lines)

---

## Context Gathering

Before implementing API integration, gather essential context:

1. **API Specification:**
   - "What is the base URL of the API?"
   - "What authentication method is required (API key, OAuth 2.0, JWT)?"
   - "Do you have OpenAPI/Swagger documentation available?"

2. **Existing Setup:**
   - "Is there already a networking layer in the project?"
   - "What serialization approach is preferred (Codable with JSONDecoder)?"
   - "Are there existing API models or response types?"

3. **Requirements:**
   - "Are there specific timeout requirements?"
   - "Should requests be retried on failure (and which status codes)?"
   - "Do you need request/response logging for debugging?"

4. **Error Handling:**
   - "How should network errors be presented to users?"
   - "Are there specific API error formats to parse?"
   - "Should 401 responses trigger token refresh or logout?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before implementing ANY code, you MUST:**

1. **Understand existing patterns** - Check for existing network code, HTTP clients, or API patterns in the codebase.
2. **Verify requirements** - Confirm API specifications, authentication, and error handling expectations before writing code.
3. **Follow project conventions** - Match existing code style, naming conventions, and architectural patterns.
4. **Provide specific, working code** - All code samples MUST include file paths and be copy-paste ready.
5. **Include error handling** - Every network call must handle errors appropriately.

### False-Positive Prevention

- ❌ Do NOT introduce third-party HTTP clients if URLSession suffices
- ❌ Do NOT generate placeholder code with TODOs for critical logic
- ❌ Do NOT assume API structure without verifying specifications
- ❌ Do NOT skip authentication or authorization handling
- ❌ Do NOT block the main thread with synchronous network calls
- ✅ DO use async/await with structured concurrency
- ✅ DO include proper timeout and retry configuration
- ✅ DO provide complete, working code that handles edge cases
- ✅ DO specify exact file paths for all code changes

---

### Phase 1: Core Networking Layer

#### 1.1 API Client

```swift
// File: Networking/APIClient.swift

import Foundation

actor APIClient {
    private let session: URLSession
    private let baseURL: URL
    private let decoder: JSONDecoder
    private let encoder: JSONEncoder
    private let authProvider: AuthTokenProvider?
    private let maxRetries: Int

    init(
        baseURL: URL,
        authProvider: AuthTokenProvider? = nil,
        maxRetries: Int = 3,
        configuration: URLSessionConfiguration = .default
    ) {
        configuration.timeoutIntervalForRequest = 30
        configuration.timeoutIntervalForResource = 60
        configuration.waitsForConnectivity = true

        self.baseURL = baseURL
        self.session = URLSession(configuration: configuration)
        self.authProvider = authProvider
        self.maxRetries = maxRetries

        self.decoder = JSONDecoder()
        decoder.dateDecodingStrategy = .iso8601
        decoder.keyDecodingStrategy = .convertFromSnakeCase

        self.encoder = JSONEncoder()
        encoder.dateEncodingStrategy = .iso8601
        encoder.keyEncodingStrategy = .convertToSnakeCase
    }

    // MARK: - Public Interface

    func request<T: Decodable>(
        _ endpoint: Endpoint,
        responseType: T.Type
    ) async throws -> T {
        let request = try await buildRequest(for: endpoint)
        return try await executeWithRetry(request, responseType: T.self)
    }

    func request(_ endpoint: Endpoint) async throws {
        let request = try await buildRequest(for: endpoint)
        let _: EmptyResponse = try await executeWithRetry(request, responseType: EmptyResponse.self)
    }

    // MARK: - Request Building

    private func buildRequest(for endpoint: Endpoint) async throws -> URLRequest {
        var components = URLComponents(
            url: baseURL.appendingPathComponent(endpoint.path),
            resolvingAgainstBaseURL: true
        )
        components?.queryItems = endpoint.queryItems

        guard let url = components?.url else {
            throw APIError.invalidURL(endpoint.path)
        }

        var request = URLRequest(url: url)
        request.httpMethod = endpoint.method.rawValue
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.setValue("application/json", forHTTPHeaderField: "Accept")

        // Add auth token
        if let authProvider, endpoint.requiresAuth {
            let token = try await authProvider.currentToken()
            request.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        }

        // Add custom headers
        for (key, value) in endpoint.headers {
            request.setValue(value, forHTTPHeaderField: key)
        }

        // Encode body
        if let body = endpoint.body {
            request.httpBody = try encoder.encode(body)
        }

        return request
    }

    // MARK: - Execution with Retry

    private func executeWithRetry<T: Decodable>(
        _ request: URLRequest,
        responseType: T.Type,
        attempt: Int = 0
    ) async throws -> T {
        do {
            return try await execute(request, responseType: T.self)
        } catch let error as APIError {
            // Retry on server errors and rate limiting
            if error.isRetryable && attempt < maxRetries {
                let delay = retryDelay(for: attempt)
                try await Task.sleep(for: .seconds(delay))
                return try await executeWithRetry(
                    request, responseType: T.self, attempt: attempt + 1
                )
            }

            // Attempt token refresh on 401
            if case .unauthorized = error, let authProvider {
                try await authProvider.refreshToken()
                var refreshedRequest = request
                let newToken = try await authProvider.currentToken()
                refreshedRequest.setValue(
                    "Bearer \(newToken)",
                    forHTTPHeaderField: "Authorization"
                )
                return try await execute(refreshedRequest, responseType: T.self)
            }

            throw error
        }
    }

    private func execute<T: Decodable>(
        _ request: URLRequest,
        responseType: T.Type
    ) async throws -> T {
        let (data, response) = try await session.data(for: request)

        guard let httpResponse = response as? HTTPURLResponse else {
            throw APIError.invalidResponse
        }

        #if DEBUG
        logRequest(request, response: httpResponse, data: data)
        #endif

        switch httpResponse.statusCode {
        case 200...299:
            return try decoder.decode(T.self, from: data)
        case 401:
            throw APIError.unauthorized
        case 403:
            throw APIError.forbidden
        case 404:
            throw APIError.notFound
        case 422:
            let validationError = try? decoder.decode(ValidationError.self, from: data)
            throw APIError.validationFailed(validationError?.errors ?? [:])
        case 429:
            throw APIError.rateLimited
        case 500...599:
            throw APIError.serverError(httpResponse.statusCode)
        default:
            throw APIError.unexpectedStatus(httpResponse.statusCode)
        }
    }

    private func retryDelay(for attempt: Int) -> Double {
        // Exponential backoff: 1s, 2s, 4s
        pow(2.0, Double(attempt))
    }

    #if DEBUG
    private nonisolated func logRequest(
        _ request: URLRequest,
        response: HTTPURLResponse,
        data: Data
    ) {
        print("[\(request.httpMethod ?? "?")] \(request.url?.absoluteString ?? "")")
        print("  Status: \(response.statusCode)")
        if let body = String(data: data, encoding: .utf8)?.prefix(500) {
            print("  Body: \(body)")
        }
    }
    #endif
}

private struct EmptyResponse: Decodable {}
```

#### 1.2 Endpoint Definition

```swift
// File: Networking/Endpoint.swift

import Foundation

struct Endpoint {
    let path: String
    let method: HTTPMethod
    let queryItems: [URLQueryItem]?
    let headers: [String: String]
    let body: (any Encodable)?
    let requiresAuth: Bool

    init(
        path: String,
        method: HTTPMethod = .get,
        queryItems: [URLQueryItem]? = nil,
        headers: [String: String] = [:],
        body: (any Encodable)? = nil,
        requiresAuth: Bool = true
    ) {
        self.path = path
        self.method = method
        self.queryItems = queryItems
        self.headers = headers
        self.body = body
        self.requiresAuth = requiresAuth
    }
}

enum HTTPMethod: String {
    case get = "GET"
    case post = "POST"
    case put = "PUT"
    case patch = "PATCH"
    case delete = "DELETE"
}
```

#### 1.3 Error Types

```swift
// File: Networking/APIError.swift

import Foundation

enum APIError: LocalizedError {
    case invalidURL(String)
    case invalidResponse
    case unauthorized
    case forbidden
    case notFound
    case validationFailed([String: [String]])
    case rateLimited
    case serverError(Int)
    case unexpectedStatus(Int)
    case decodingFailed(Error)

    var errorDescription: String? {
        switch self {
        case .invalidURL(let path): return "Invalid URL: \(path)"
        case .invalidResponse: return "Invalid server response"
        case .unauthorized: return "Authentication required"
        case .forbidden: return "Access denied"
        case .notFound: return "Resource not found"
        case .validationFailed(let errors):
            let messages = errors.flatMap { $0.value }.joined(separator: ", ")
            return "Validation failed: \(messages)"
        case .rateLimited: return "Too many requests. Please try again later."
        case .serverError(let code): return "Server error (\(code))"
        case .unexpectedStatus(let code): return "Unexpected response (\(code))"
        case .decodingFailed(let error): return "Data parsing failed: \(error.localizedDescription)"
        }
    }

    var isRetryable: Bool {
        switch self {
        case .rateLimited, .serverError: return true
        default: return false
        }
    }
}

struct ValidationError: Decodable {
    let errors: [String: [String]]
}
```

---

### Phase 2: Auth Token Management

**CHECKPOINT 1:** Confirm core networking before implementing auth.

#### 2.1 Token Provider

```swift
// File: Networking/Auth/AuthTokenProvider.swift

import Foundation

protocol AuthTokenProvider: Sendable {
    func currentToken() async throws -> String
    func refreshToken() async throws
}

actor KeychainAuthProvider: AuthTokenProvider {
    private var accessToken: String?
    private var refreshTokenValue: String?
    private var isRefreshing = false
    private var refreshContinuations: [CheckedContinuation<Void, Error>] = []
    private let keychainService: KeychainService
    private let session: URLSession
    private let tokenURL: URL

    init(keychainService: KeychainService, tokenURL: URL) {
        self.keychainService = keychainService
        self.tokenURL = tokenURL
        self.session = URLSession(configuration: .default)
        self.accessToken = keychainService.read(key: "access_token")
        self.refreshTokenValue = keychainService.read(key: "refresh_token")
    }

    func currentToken() async throws -> String {
        guard let token = accessToken else {
            throw APIError.unauthorized
        }
        return token
    }

    func refreshToken() async throws {
        // Coalesce concurrent refresh requests
        if isRefreshing {
            try await withCheckedThrowingContinuation { continuation in
                refreshContinuations.append(continuation)
            }
            return
        }

        isRefreshing = true
        defer {
            isRefreshing = false
            refreshContinuations.forEach { $0.resume() }
            refreshContinuations.removeAll()
        }

        guard let refresh = refreshTokenValue else {
            throw APIError.unauthorized
        }

        var request = URLRequest(url: tokenURL)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")

        let body = ["refresh_token": refresh]
        request.httpBody = try JSONEncoder().encode(body)

        let (data, response) = try await session.data(for: request)

        guard let httpResponse = response as? HTTPURLResponse,
              httpResponse.statusCode == 200 else {
            // Refresh failed - clear tokens and require re-login
            clearTokens()
            throw APIError.unauthorized
        }

        let tokenResponse = try JSONDecoder().decode(TokenResponse.self, from: data)
        accessToken = tokenResponse.accessToken
        refreshTokenValue = tokenResponse.refreshToken

        keychainService.save(key: "access_token", value: tokenResponse.accessToken)
        keychainService.save(key: "refresh_token", value: tokenResponse.refreshToken)
    }

    func clearTokens() {
        accessToken = nil
        refreshTokenValue = nil
        keychainService.delete(key: "access_token")
        keychainService.delete(key: "refresh_token")
    }
}

struct TokenResponse: Decodable {
    let accessToken: String
    let refreshToken: String
    let expiresIn: Int
}
```

---

### Phase 3: Endpoint Definitions

#### 3.1 Domain-Specific Endpoints

```swift
// File: Networking/Endpoints/ItemEndpoints.swift

import Foundation

enum ItemEndpoints {
    static func list(page: Int = 1, perPage: Int = 20) -> Endpoint {
        Endpoint(
            path: "/api/v1/items",
            queryItems: [
                URLQueryItem(name: "page", value: "\(page)"),
                URLQueryItem(name: "per_page", value: "\(perPage)")
            ]
        )
    }

    static func detail(id: String) -> Endpoint {
        Endpoint(path: "/api/v1/items/\(id)")
    }

    static func create(request: CreateItemRequest) -> Endpoint {
        Endpoint(
            path: "/api/v1/items",
            method: .post,
            body: request
        )
    }

    static func update(id: String, request: UpdateItemRequest) -> Endpoint {
        Endpoint(
            path: "/api/v1/items/\(id)",
            method: .put,
            body: request
        )
    }

    static func delete(id: String) -> Endpoint {
        Endpoint(
            path: "/api/v1/items/\(id)",
            method: .delete
        )
    }

    static func search(query: String) -> Endpoint {
        Endpoint(
            path: "/api/v1/items/search",
            queryItems: [URLQueryItem(name: "q", value: query)]
        )
    }
}

// Request/Response Models
struct CreateItemRequest: Encodable {
    let title: String
    let description: String
    let categoryId: String
}

struct UpdateItemRequest: Encodable {
    let title: String?
    let description: String?
}

struct ItemResponse: Decodable {
    let id: String
    let title: String
    let description: String
    let createdAt: Date
    let updatedAt: Date
}

struct PaginatedResponse<T: Decodable>: Decodable {
    let data: [T]
    let meta: PaginationMeta
}

struct PaginationMeta: Decodable {
    let currentPage: Int
    let totalPages: Int
    let totalCount: Int
}
```

#### 3.2 Service Layer

```swift
// File: Networking/Services/ItemService.swift

import Foundation

protocol ItemServiceProtocol: Sendable {
    func fetchItems(page: Int) async throws -> PaginatedResponse<ItemResponse>
    func fetchItem(id: String) async throws -> ItemResponse
    func createItem(_ request: CreateItemRequest) async throws -> ItemResponse
    func updateItem(id: String, _ request: UpdateItemRequest) async throws -> ItemResponse
    func deleteItem(id: String) async throws
}

final class ItemService: ItemServiceProtocol {
    private let client: APIClient

    init(client: APIClient) {
        self.client = client
    }

    func fetchItems(page: Int = 1) async throws -> PaginatedResponse<ItemResponse> {
        try await client.request(
            ItemEndpoints.list(page: page),
            responseType: PaginatedResponse<ItemResponse>.self
        )
    }

    func fetchItem(id: String) async throws -> ItemResponse {
        try await client.request(
            ItemEndpoints.detail(id: id),
            responseType: ItemResponse.self
        )
    }

    func createItem(_ request: CreateItemRequest) async throws -> ItemResponse {
        try await client.request(
            ItemEndpoints.create(request: request),
            responseType: ItemResponse.self
        )
    }

    func updateItem(id: String, _ request: UpdateItemRequest) async throws -> ItemResponse {
        try await client.request(
            ItemEndpoints.update(id: id, request: request),
            responseType: ItemResponse.self
        )
    }

    func deleteItem(id: String) async throws {
        try await client.request(ItemEndpoints.delete(id: id))
    }
}
```

---

## Expected Output

### File Structure

```
Networking/
├── APIClient.swift               # Core HTTP client
├── APIError.swift                # Error types
├── Endpoint.swift                # Request definition
├── Auth/
│   └── AuthTokenProvider.swift   # Token management
├── Endpoints/
│   └── ItemEndpoints.swift       # Domain endpoints
└── Services/
    └── ItemService.swift         # Business-level API
```

### Implementation Checklist

- [ ] APIClient with async/await
- [ ] Codable request/response models
- [ ] Auth token interceptor with refresh
- [ ] Exponential backoff retry logic
- [ ] Structured error mapping from HTTP status codes
- [ ] Debug logging (DEBUG builds only)
- [ ] Endpoint definitions per domain
- [ ] Service layer with protocol
- [ ] Pagination support

---

## Example Interaction

**User:** "I need to integrate with a REST API that uses JWT auth and returns paginated results."

**Assistant:**
```swift
// Usage in a ViewModel
@Observable
final class ItemListViewModel {
    private(set) var items: [ItemResponse] = []
    private(set) var isLoading = false
    private(set) var error: String?
    private var currentPage = 1
    private var hasMorePages = true

    private let service: ItemServiceProtocol

    init(service: ItemServiceProtocol) {
        self.service = service
    }

    func loadItems() async {
        isLoading = true
        error = nil
        do {
            let response = try await service.fetchItems(page: 1)
            items = response.data
            currentPage = 1
            hasMorePages = response.meta.currentPage < response.meta.totalPages
        } catch {
            self.error = error.localizedDescription
        }
        isLoading = false
    }

    func loadNextPage() async {
        guard hasMorePages, !isLoading else { return }
        currentPage += 1
        do {
            let response = try await service.fetchItems(page: currentPage)
            items.append(contentsOf: response.data)
            hasMorePages = response.meta.currentPage < response.meta.totalPages
        } catch {
            currentPage -= 1
        }
    }
}
```

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective for API integration
- **ST-02** (Sequential Instructions): Phased approach from client to service layer
- **RT-02** (Multi-Dimensional Analysis): Covers networking, auth, errors, pagination
- **RT-04** (Best Practice Review): URLSession async/await and Swift concurrency best practices
- **ST-03** (Output Format Templates): Code templates for endpoints and services
- **NE-02** (Phased Workflow): Clear phases with checkpoints

---

## Related Prompts

- [ios_data_layer_implementation.md](ios_data_layer_implementation.md) - Persist API responses locally
- [ios_state_management.md](ios_state_management.md) - Connect API data to UI state
- [ios_offline_first_sync.md](ios_offline_first_sync.md) - Offline-first with API sync
- [ios_background_tasks.md](ios_background_tasks.md) - Background API sync

---

## Customization Guide

### For Multipart Upload

Add file upload support:
```swift
extension APIClient {
    func upload(
        _ endpoint: Endpoint,
        fileData: Data,
        fileName: String,
        mimeType: String
    ) async throws -> UploadResponse {
        var request = try await buildRequest(for: endpoint)
        let boundary = UUID().uuidString
        request.setValue(
            "multipart/form-data; boundary=\(boundary)",
            forHTTPHeaderField: "Content-Type"
        )

        var body = Data()
        body.append("--\(boundary)\r\n".data(using: .utf8)!)
        body.append("Content-Disposition: form-data; name=\"file\"; filename=\"\(fileName)\"\r\n".data(using: .utf8)!)
        body.append("Content-Type: \(mimeType)\r\n\r\n".data(using: .utf8)!)
        body.append(fileData)
        body.append("\r\n--\(boundary)--\r\n".data(using: .utf8)!)
        request.httpBody = body

        return try await execute(request, responseType: UploadResponse.self)
    }
}
```

### For WebSocket Connections

Add real-time support:
```swift
func connectWebSocket(url: URL) -> AsyncStream<WebSocketMessage> {
    AsyncStream { continuation in
        let task = session.webSocketTask(with: url)
        Task {
            while task.state == .running {
                let message = try await task.receive()
                // Process message...
            }
        }
        task.resume()
    }
}
```

### For Certificate Pinning

Add SSL pinning:
```swift
class PinningDelegate: NSObject, URLSessionDelegate {
    func urlSession(
        _ session: URLSession,
        didReceive challenge: URLAuthenticationChallenge
    ) async -> (URLSession.AuthChallengeDisposition, URLCredential?) {
        guard let trust = challenge.protectionSpace.serverTrust else {
            return (.cancelAuthenticationChallenge, nil)
        }
        // Validate against pinned certificate
        return (.useCredential, URLCredential(trust: trust))
    }
}
```
