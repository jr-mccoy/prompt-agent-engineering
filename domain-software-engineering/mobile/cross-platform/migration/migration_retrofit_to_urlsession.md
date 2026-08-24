---
title: "Retrofit/OkHttp to URLSession Migration"
category: mobile-development
description: "Migrate Retrofit and OkHttp networking to URLSession with async/await covering endpoints, interceptors to URLProtocol, Moshi/Gson to Codable, and error handling"
techniques:
  - ST-01
  - RT-02
  - DS-02
difficulty: intermediate
tags:
  - ios
  - android
  - migration
  - retrofit
  - okhttp
  - urlsession
  - networking
  - codable
updated: "2026-03-19"
---

# Retrofit/OkHttp to URLSession Migration

**Objective:** Translate Android's Retrofit + OkHttp networking stack to iOS's URLSession with async/await, covering API service definitions, interceptors, JSON serialization (Moshi/Gson to Codable), error handling, and multipart uploads.

**When to Use:** When migrating an Android app's networking layer to iOS. This prompt covers the most common Retrofit patterns and their URLSession equivalents, producing a clean, testable networking layer.

**Prompt Type:** Modular (~280 lines)

## Context Gathering

1. How many Retrofit API interfaces does the app define?
2. What OkHttp interceptors are used? (auth, logging, retry, caching)
3. What serialization library is used? (Moshi, Gson, kotlinx.serialization)
4. Are there multipart/form-data uploads?
5. What error handling patterns are used? (sealed Result, custom exceptions)
6. Are there any custom call adapters or converter factories?
7. Is certificate pinning used?

## Instructions

### CRITICAL: Verification Requirements

- Every Retrofit endpoint MUST have a corresponding URLSession method
- Error handling MUST cover the same HTTP status codes and network errors
- Serialization MUST produce identical JSON output for API requests
- Interceptor behavior MUST be replicated in the iOS networking stack

### False-Positive Prevention

- ❌ DO NOT create a Retrofit-like annotation processor on iOS — it adds unnecessary complexity
- ✅ DO use simple protocol-based API service definitions with async methods
- ❌ DO NOT use URLProtocol for interceptors when URLSessionDelegate suffices
- ✅ DO use URLSessionDelegate for auth challenges, URLProtocol for logging/mocking
- ❌ DO NOT assume Codable handles all Moshi/Gson edge cases (custom adapters)
- ✅ DO write custom CodingKeys and init(from:) for non-standard JSON shapes
- ❌ DO NOT ignore URLSession's default caching — it may cause stale data issues
- ✅ DO configure URLCache and cachePolicy explicitly

### Step 1: API Service Definition

**Kotlin (Retrofit interface):**
```kotlin
interface UserApi {
    @GET("users/{id}")
    suspend fun getUser(@Path("id") userId: String): UserResponse

    @GET("users")
    suspend fun searchUsers(
        @Query("q") query: String,
        @Query("page") page: Int = 1,
        @Query("limit") limit: Int = 20
    ): PaginatedResponse<UserResponse>

    @POST("users")
    suspend fun createUser(@Body request: CreateUserRequest): UserResponse

    @PUT("users/{id}")
    suspend fun updateUser(
        @Path("id") userId: String,
        @Body request: UpdateUserRequest
    ): UserResponse

    @DELETE("users/{id}")
    suspend fun deleteUser(@Path("id") userId: String)

    @Multipart
    @POST("users/{id}/avatar")
    suspend fun uploadAvatar(
        @Path("id") userId: String,
        @Part image: MultipartBody.Part
    ): AvatarResponse
}
```

**Swift (URLSession-based API service):**
```swift
protocol UserAPIService: Sendable {
    func getUser(id: String) async throws -> UserResponse
    func searchUsers(query: String, page: Int, limit: Int) async throws -> PaginatedResponse<UserResponse>
    func createUser(_ request: CreateUserRequest) async throws -> UserResponse
    func updateUser(id: String, _ request: UpdateUserRequest) async throws -> UserResponse
    func deleteUser(id: String) async throws
    func uploadAvatar(userId: String, imageData: Data, filename: String) async throws -> AvatarResponse
}

final class URLSessionUserAPIService: UserAPIService {
    private let session: URLSession
    private let baseURL: URL
    private let encoder = JSONEncoder()
    private let decoder: JSONDecoder = {
        let d = JSONDecoder()
        d.keyDecodingStrategy = .convertFromSnakeCase
        return d
    }()

    init(session: URLSession = .shared, baseURL: URL) {
        self.session = session
        self.baseURL = baseURL
    }

    func getUser(id: String) async throws -> UserResponse {
        let url = baseURL.appendingPathComponent("users/\(id)")
        let (data, response) = try await session.data(from: url)
        try validateResponse(response)
        return try decoder.decode(UserResponse.self, from: data)
    }

    func searchUsers(
        query: String, page: Int = 1, limit: Int = 20
    ) async throws -> PaginatedResponse<UserResponse> {
        var components = URLComponents(
            url: baseURL.appendingPathComponent("users"),
            resolvingAgainstBaseURL: false
        )!
        components.queryItems = [
            URLQueryItem(name: "q", value: query),
            URLQueryItem(name: "page", value: "\(page)"),
            URLQueryItem(name: "limit", value: "\(limit)")
        ]
        let (data, response) = try await session.data(from: components.url!)
        try validateResponse(response)
        return try decoder.decode(PaginatedResponse<UserResponse>.self, from: data)
    }

    func createUser(_ request: CreateUserRequest) async throws -> UserResponse {
        var urlRequest = URLRequest(url: baseURL.appendingPathComponent("users"))
        urlRequest.httpMethod = "POST"
        urlRequest.setValue("application/json", forHTTPHeaderField: "Content-Type")
        urlRequest.httpBody = try encoder.encode(request)
        let (data, response) = try await session.data(for: urlRequest)
        try validateResponse(response)
        return try decoder.decode(UserResponse.self, from: data)
    }

    func deleteUser(id: String) async throws {
        var urlRequest = URLRequest(
            url: baseURL.appendingPathComponent("users/\(id)")
        )
        urlRequest.httpMethod = "DELETE"
        let (_, response) = try await session.data(for: urlRequest)
        try validateResponse(response)
    }

    // Multipart upload
    func uploadAvatar(
        userId: String, imageData: Data, filename: String
    ) async throws -> AvatarResponse {
        let boundary = UUID().uuidString
        var urlRequest = URLRequest(
            url: baseURL.appendingPathComponent("users/\(userId)/avatar")
        )
        urlRequest.httpMethod = "POST"
        urlRequest.setValue(
            "multipart/form-data; boundary=\(boundary)",
            forHTTPHeaderField: "Content-Type"
        )

        var body = Data()
        body.append("--\(boundary)\r\n".data(using: .utf8)!)
        body.append("Content-Disposition: form-data; name=\"image\"; filename=\"\(filename)\"\r\n".data(using: .utf8)!)
        body.append("Content-Type: image/jpeg\r\n\r\n".data(using: .utf8)!)
        body.append(imageData)
        body.append("\r\n--\(boundary)--\r\n".data(using: .utf8)!)
        urlRequest.httpBody = body

        let (data, response) = try await session.data(for: urlRequest)
        try validateResponse(response)
        return try decoder.decode(AvatarResponse.self, from: data)
    }

    private func validateResponse(_ response: URLResponse) throws {
        guard let http = response as? HTTPURLResponse else {
            throw APIError.invalidResponse
        }
        switch http.statusCode {
        case 200...299: return
        case 401: throw APIError.unauthorized
        case 404: throw APIError.notFound
        case 429: throw APIError.rateLimited
        case 500...599: throw APIError.serverError(http.statusCode)
        default: throw APIError.httpError(http.statusCode)
        }
    }
}
```

### Step 2: Interceptor to URLSession Adaptation

| OkHttp Interceptor | iOS Equivalent | Pattern |
|-------------------|----------------|---------|
| Auth interceptor (add token header) | `URLSessionDelegate` or request modifier | Inject auth header before each request |
| Logging interceptor | `URLProtocol` subclass | Intercept and log requests/responses |
| Retry interceptor | Custom retry logic in async function | Wrap with retry loop |
| Cache interceptor | `URLCache` configuration | Built into URLSession |

**Kotlin (OkHttp auth interceptor):**
```kotlin
class AuthInterceptor @Inject constructor(
    private val tokenProvider: TokenProvider
) : Interceptor {
    override fun intercept(chain: Interceptor.Chain): Response {
        val token = tokenProvider.getAccessToken()
        val request = chain.request().newBuilder()
            .header("Authorization", "Bearer $token")
            .build()
        val response = chain.proceed(request)
        if (response.code == 401) {
            val newToken = tokenProvider.refreshToken()
            val retryRequest = chain.request().newBuilder()
                .header("Authorization", "Bearer $newToken")
                .build()
            return chain.proceed(retryRequest)
        }
        return response
    }
}
```

**Swift (iOS auth via URLSessionDelegate):**
```swift
final class AuthenticatedAPIClient: NSObject, URLSessionTaskDelegate {
    private let tokenProvider: TokenProvider
    private lazy var session: URLSession = {
        URLSession(configuration: .default, delegate: self, delegateQueue: nil)
    }()

    init(tokenProvider: TokenProvider) {
        self.tokenProvider = tokenProvider
    }

    func authorizedRequest(for url: URL) async throws -> (Data, URLResponse) {
        var request = URLRequest(url: url)
        let token = await tokenProvider.getAccessToken()
        request.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")

        let (data, response) = try await session.data(for: request)

        if let http = response as? HTTPURLResponse, http.statusCode == 401 {
            let newToken = try await tokenProvider.refreshToken()
            request.setValue("Bearer \(newToken)", forHTTPHeaderField: "Authorization")
            return try await session.data(for: request)
        }

        return (data, response)
    }
}
```

### Step 3: Serialization Mapping

| Moshi/Gson | Codable | Notes |
|-----------|---------|-------|
| `@Json(name = "user_name")` | `CodingKeys` enum | Key mapping |
| `@JsonAdapter` | Custom `init(from: Decoder)` | Custom parsing |
| `MoshiConverterFactory` | `JSONDecoder` on URLSession response | Automatic |
| Null safety via `@JsonClass` | Optional properties | Swift optionals |
| Date adapters | `dateDecodingStrategy` | Built-in decoder config |

**Kotlin (Moshi data class):**
```kotlin
@JsonClass(generateAdapter = true)
data class UserResponse(
    @Json(name = "user_id") val userId: String,
    @Json(name = "display_name") val displayName: String,
    @Json(name = "created_at") val createdAt: Instant,
    val email: String,
    val avatar: String?
)
```

**Swift (Codable struct):**
```swift
struct UserResponse: Codable, Sendable {
    let userId: String
    let displayName: String
    let createdAt: Date
    let email: String
    let avatar: String?

    // snake_case handled by decoder.keyDecodingStrategy = .convertFromSnakeCase
    // OR explicit CodingKeys:
    // enum CodingKeys: String, CodingKey {
    //     case userId = "user_id"
    //     case displayName = "display_name"
    //     case createdAt = "created_at"
    //     case email, avatar
    // }
}
```

## Expected Output

1. **API service protocol and implementation** with all endpoints
2. **Authentication handling** matching OkHttp interceptor behavior
3. **Codable model definitions** for all API response types
4. **Error handling enum** covering all HTTP and network error cases
5. **Unit tests** with URLProtocol-based mocking

## Example Interaction

**User:** Our Android app has 4 Retrofit interfaces (User, Product, Order, Auth) with an auth interceptor and logging interceptor. We use Moshi with snake_case JSON.

**Assistant:**

```
Retrofit Interface        →  Swift Protocol + URLSession Implementation
─────────────────             ────────────────────────────────────────
UserApi (8 endpoints)    →  UserAPIService protocol + URLSessionUserAPIService
ProductApi (6 endpoints) →  ProductAPIService protocol + URLSessionProductAPIService
OrderApi (5 endpoints)   →  OrderAPIService protocol + URLSessionOrderAPIService
AuthApi (3 endpoints)    →  AuthAPIService protocol + URLSessionAuthAPIService

Auth Interceptor         →  AuthenticatedAPIClient (shared base)
Logging Interceptor      →  LoggingURLProtocol (debug builds only)
Moshi snake_case         →  JSONDecoder with .convertFromSnakeCase
```

## Techniques Used

| Technique | Application |
|-----------|-------------|
| **ST-01: Structured Task Decomposition** | API, interceptors, serialization, error handling steps |
| **RT-02: Contextual Reference Integration** | Retrofit, OkHttp, URLSession documentation |
| **DS-02: Output Specification Framework** | Protocol definitions, implementation code, test patterns |

## Related Prompts

- `migration_architecture_adaptation.md` — Repository layer consuming the API service
- `migration_coroutines_to_swift_concurrency.md` — Async patterns for network calls
- `migration_hilt_to_swift_di.md` — Injecting API services

## Customization Guide

- **Alamofire:** If preferring a third-party library, Alamofire provides Retrofit-like request building on iOS.
- **Ktor (KMP):** If using KMP, share the networking layer with Ktor client for both platforms.
- **GraphQL:** If the app uses Apollo Android, migrate to Apollo iOS which has a similar API.
- **Certificate Pinning:** Use `URLSessionDelegate`'s `urlSession(_:didReceive:completionHandler:)` for pinning on iOS.
