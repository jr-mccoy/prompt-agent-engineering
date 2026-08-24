---
title: "Android API Integration"
category: mobile-development
description: ""
tags:
  - android
  - mobile-development
updated: "2026-03-19"
---

# Android API Integration

**Objective:** Implement a robust, type-safe REST API integration using Retrofit with proper error handling, authentication, and network resilience following Android best practices.

**When to Use:** Use this prompt when integrating with REST APIs in an Android application. Ideal for new API integrations, refactoring existing network code, or adding advanced features like authentication, caching, or retry logic. Best used after API endpoints and data contracts are defined.

**Prompt Type:** Comprehensive (350-450 lines)

---

## Context Gathering

Before implementing API integration, gather essential context:

1. **API Specification:**
   - "What is the base URL of the API?"
   - "What authentication method is required (API key, OAuth, JWT)?"
   - "Do you have OpenAPI/Swagger documentation available?"

2. **Existing Setup:**
   - "Is Retrofit already configured in the project?"
   - "What serialization library is preferred (Kotlinx Serialization, Moshi, Gson)?"
   - "Is there an existing network module or pattern to follow?"

3. **Requirements:**
   - "Are there specific timeout requirements?"
   - "Should requests be retried on failure?"
   - "Do you need request/response logging for debugging?"

4. **Error Handling:**
   - "How should network errors be presented to users?"
   - "Are there specific API error formats to parse?"
   - "Should certain errors trigger specific actions (e.g., 401 → logout)?"

---

## Instructions

### CRITICAL: Implementation Requirements

**Before implementing ANY code, you MUST:**

1. **Understand existing patterns** - Check for existing network code, HTTP clients, or API patterns already in the codebase. Don't introduce conflicting approaches.
2. **Verify requirements** - Confirm API specifications, authentication requirements, and error handling expectations before writing code.
3. **Follow project conventions** - Match existing code style, naming conventions, and architectural patterns.
4. **Provide specific, working code** - All code samples MUST include file paths (e.g., `data/api/UserApi.kt`) and be copy-paste ready.
5. **Include error handling** - Every network call must handle errors appropriately for the app's UX patterns.

**Adapting to existing code is preferred over introducing new patterns.** If the project already has a network layer, extend it rather than replacing it.

### Quality Requirements

- ❌ Do NOT introduce new HTTP clients if one already exists (e.g., don't add OkHttp if Ktor is used)
- ❌ Do NOT generate placeholder code with TODOs for critical logic
- ❌ Do NOT assume API structure without verifying specifications
- ❌ Do NOT skip authentication or authorization handling
- ✅ DO follow existing error handling patterns in the project
- ✅ DO include proper timeout and retry configuration
- ✅ DO provide complete, tested code that handles edge cases
- ✅ DO specify exact file paths for all code changes

---

### Phase 1: Core Network Setup

#### 1.1 Dependencies Configuration

Add required dependencies to your build configuration:

```kotlin
// build.gradle.kts (Module)
dependencies {
    // Retrofit core
    implementation("com.squareup.retrofit2:retrofit:2.9.0")

    // Kotlinx Serialization (recommended)
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.6.0")
    implementation("com.jakewharton.retrofit:retrofit2-kotlinx-serialization-converter:1.0.0")

    // OR Moshi
    // implementation("com.squareup.moshi:moshi-kotlin:1.15.0")
    // implementation("com.squareup.retrofit2:converter-moshi:2.9.0")

    // OkHttp
    implementation("com.squareup.okhttp3:okhttp:4.12.0")
    implementation("com.squareup.okhttp3:logging-interceptor:4.12.0")
}
```

#### 1.2 OkHttpClient Configuration

Create a properly configured OkHttpClient:

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {

    @Provides
    @Singleton
    fun provideOkHttpClient(
        authInterceptor: AuthInterceptor,
        loggingInterceptor: HttpLoggingInterceptor
    ): OkHttpClient = OkHttpClient.Builder()
        .connectTimeout(30, TimeUnit.SECONDS)
        .readTimeout(30, TimeUnit.SECONDS)
        .writeTimeout(30, TimeUnit.SECONDS)
        .addInterceptor(authInterceptor)
        .addInterceptor(loggingInterceptor)
        .retryOnConnectionFailure(true)
        .build()

    @Provides
    @Singleton
    fun provideLoggingInterceptor(): HttpLoggingInterceptor =
        HttpLoggingInterceptor().apply {
            level = if (BuildConfig.DEBUG) {
                HttpLoggingInterceptor.Level.BODY
            } else {
                HttpLoggingInterceptor.Level.NONE
            }
        }
}
```

#### 1.3 Retrofit Configuration

Configure Retrofit with appropriate converters:

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object ApiModule {

    private const val BASE_URL = "https://api.example.com/v1/"

    @Provides
    @Singleton
    fun provideJson(): Json = Json {
        ignoreUnknownKeys = true
        coerceInputValues = true
        explicitNulls = false
        isLenient = true
    }

    @Provides
    @Singleton
    fun provideRetrofit(
        okHttpClient: OkHttpClient,
        json: Json
    ): Retrofit = Retrofit.Builder()
        .baseUrl(BASE_URL)
        .client(okHttpClient)
        .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
        .build()

    @Provides
    @Singleton
    fun provideApiService(retrofit: Retrofit): ApiService =
        retrofit.create(ApiService::class.java)
}
```

---

### Phase 2: API Service Definition

**CHECKPOINT 1:** Review network configuration before defining endpoints.

```markdown
## Network Configuration Summary

### Base Setup
- Base URL: [URL]
- Timeout: [X] seconds
- Serialization: [Kotlinx/Moshi/Gson]

### Interceptors Configured
| Interceptor | Purpose |
|-------------|---------|
| AuthInterceptor | Add authentication headers |
| LoggingInterceptor | Debug logging (debug builds only) |

### Security Considerations
- [ ] HTTPS enforced
- [ ] Certificate pinning (if required)
- [ ] Sensitive data not logged

**Does this configuration meet your requirements?**
```

#### 2.1 API Service Interface

Define clean, typed API endpoints:

```kotlin
interface ApiService {

    // GET requests
    @GET("users/{id}")
    suspend fun getUser(@Path("id") userId: String): UserDto

    @GET("users")
    suspend fun getUsers(
        @Query("page") page: Int = 1,
        @Query("limit") limit: Int = 20,
        @Query("sort") sort: String? = null
    ): PaginatedResponse<UserDto>

    @GET("users/search")
    suspend fun searchUsers(@Query("q") query: String): List<UserDto>

    // POST requests
    @POST("users")
    suspend fun createUser(@Body request: CreateUserRequest): UserDto

    @POST("auth/login")
    suspend fun login(@Body request: LoginRequest): AuthResponse

    // PUT/PATCH requests
    @PUT("users/{id}")
    suspend fun updateUser(
        @Path("id") userId: String,
        @Body request: UpdateUserRequest
    ): UserDto

    @PATCH("users/{id}")
    suspend fun patchUser(
        @Path("id") userId: String,
        @Body updates: Map<String, @JvmSuppressWildcards Any>
    ): UserDto

    // DELETE requests
    @DELETE("users/{id}")
    suspend fun deleteUser(@Path("id") userId: String): Response<Unit>

    // File uploads
    @Multipart
    @POST("users/{id}/avatar")
    suspend fun uploadAvatar(
        @Path("id") userId: String,
        @Part image: MultipartBody.Part
    ): UserDto

    // Headers
    @Headers("Cache-Control: max-age=300")
    @GET("config")
    suspend fun getConfig(): ConfigDto

    @GET("protected/resource")
    suspend fun getProtectedResource(
        @Header("X-Custom-Header") customValue: String
    ): ResourceDto
}
```

#### 2.2 DTO Definitions

Create Data Transfer Objects matching API contracts:

```kotlin
@Serializable
data class UserDto(
    val id: String,
    val email: String,
    val name: String,
    @SerialName("created_at") val createdAt: String,
    @SerialName("updated_at") val updatedAt: String,
    @SerialName("profile_image_url") val profileImageUrl: String? = null
)

@Serializable
data class CreateUserRequest(
    val email: String,
    val name: String,
    val password: String
)

@Serializable
data class UpdateUserRequest(
    val name: String? = null,
    val email: String? = null
)

@Serializable
data class PaginatedResponse<T>(
    val data: List<T>,
    val page: Int,
    @SerialName("total_pages") val totalPages: Int,
    @SerialName("total_items") val totalItems: Int
)

@Serializable
data class ApiError(
    val code: String,
    val message: String,
    val details: Map<String, String>? = null
)
```

---

### Phase 3: Authentication Implementation

#### 3.1 Auth Interceptor

Implement authentication header injection:

```kotlin
class AuthInterceptor @Inject constructor(
    private val tokenProvider: TokenProvider
) : Interceptor {

    override fun intercept(chain: Interceptor.Chain): Response {
        val originalRequest = chain.request()

        // Skip auth for public endpoints
        if (originalRequest.url.encodedPath.contains("/auth/")) {
            return chain.proceed(originalRequest)
        }

        val token = tokenProvider.getAccessToken()
            ?: return chain.proceed(originalRequest)

        val authenticatedRequest = originalRequest.newBuilder()
            .header("Authorization", "Bearer $token")
            .build()

        return chain.proceed(authenticatedRequest)
    }
}
```

#### 3.2 Token Management

Implement secure token storage and refresh:

```kotlin
interface TokenProvider {
    fun getAccessToken(): String?
    fun getRefreshToken(): String?
    suspend fun refreshTokens(): Boolean
    fun clearTokens()
}

class TokenProviderImpl @Inject constructor(
    private val secureStorage: SecureStorage
) : TokenProvider {

    private var cachedAccessToken: String? = null

    override fun getAccessToken(): String? {
        return cachedAccessToken ?: secureStorage.getString(KEY_ACCESS_TOKEN)
            .also { cachedAccessToken = it }
    }

    override fun getRefreshToken(): String? =
        secureStorage.getString(KEY_REFRESH_TOKEN)

    override suspend fun refreshTokens(): Boolean {
        // Implement token refresh logic
        return false
    }

    override fun clearTokens() {
        cachedAccessToken = null
        secureStorage.remove(KEY_ACCESS_TOKEN)
        secureStorage.remove(KEY_REFRESH_TOKEN)
    }

    companion object {
        private const val KEY_ACCESS_TOKEN = "access_token"
        private const val KEY_REFRESH_TOKEN = "refresh_token"
    }
}
```

#### 3.3 Token Refresh Authenticator

Handle automatic token refresh on 401 responses:

```kotlin
class TokenAuthenticator @Inject constructor(
    private val tokenProvider: TokenProvider,
    private val authApi: Lazy<AuthApi>
) : Authenticator {

    private val refreshLock = Mutex()

    override fun authenticate(route: Route?, response: Response): Request? {
        // Don't retry if we've already tried
        if (response.request.header("X-Retry-Auth") != null) {
            return null
        }

        return runBlocking {
            refreshLock.withLock {
                // Check if token was already refreshed by another request
                val currentToken = tokenProvider.getAccessToken()
                val requestToken = response.request.header("Authorization")
                    ?.removePrefix("Bearer ")

                if (currentToken != null && currentToken != requestToken) {
                    // Token was refreshed, retry with new token
                    return@runBlocking response.request.newBuilder()
                        .header("Authorization", "Bearer $currentToken")
                        .header("X-Retry-Auth", "true")
                        .build()
                }

                // Try to refresh
                val refreshed = tokenProvider.refreshTokens()
                if (refreshed) {
                    val newToken = tokenProvider.getAccessToken()
                    response.request.newBuilder()
                        .header("Authorization", "Bearer $newToken")
                        .header("X-Retry-Auth", "true")
                        .build()
                } else {
                    // Refresh failed, clear tokens and return null
                    tokenProvider.clearTokens()
                    null
                }
            }
        }
    }
}
```

---

### Phase 4: Error Handling

**CHECKPOINT 2:** Review authentication setup before implementing error handling.

```markdown
## Authentication Summary

### Auth Method
- Type: [API Key / OAuth / JWT Bearer]
- Header: [Authorization: Bearer / X-API-Key]

### Token Management
- Storage: [Encrypted SharedPreferences / DataStore]
- Refresh: [Automatic / Manual]

### Protected Endpoints
| Endpoint Pattern | Auth Required |
|-----------------|---------------|
| /auth/* | No |
| /public/* | No |
| /* | Yes |

**Ready to implement error handling?**
```

#### 4.1 Network Result Wrapper

Create a sealed class for network results:

```kotlin
sealed class NetworkResult<out T> {
    data class Success<T>(val data: T) : NetworkResult<T>()
    data class Error(val exception: NetworkException) : NetworkResult<Nothing>()

    val isSuccess: Boolean get() = this is Success
    val isError: Boolean get() = this is Error

    fun getOrNull(): T? = (this as? Success)?.data

    fun getOrThrow(): T = when (this) {
        is Success -> data
        is Error -> throw exception
    }

    inline fun <R> map(transform: (T) -> R): NetworkResult<R> = when (this) {
        is Success -> Success(transform(data))
        is Error -> this
    }

    inline fun onSuccess(action: (T) -> Unit): NetworkResult<T> {
        if (this is Success) action(data)
        return this
    }

    inline fun onError(action: (NetworkException) -> Unit): NetworkResult<T> {
        if (this is Error) action(exception)
        return this
    }
}
```

#### 4.2 Exception Hierarchy

Define typed exceptions for different error scenarios:

```kotlin
sealed class NetworkException(
    message: String,
    cause: Throwable? = null
) : Exception(message, cause) {

    // Connection issues
    data object NoInternetConnection : NetworkException("No internet connection")
    data object Timeout : NetworkException("Request timed out")
    data class ConnectionFailed(override val cause: Throwable) :
        NetworkException("Connection failed", cause)

    // HTTP errors
    data class HttpError(
        val code: Int,
        val errorBody: ApiError?
    ) : NetworkException("HTTP $code: ${errorBody?.message ?: "Unknown error"}")

    data object Unauthorized : NetworkException("Unauthorized - please log in again")
    data object Forbidden : NetworkException("Access forbidden")
    data object NotFound : NetworkException("Resource not found")
    data class ServerError(val code: Int) : NetworkException("Server error ($code)")

    // Parsing errors
    data class ParseError(override val cause: Throwable) :
        NetworkException("Failed to parse response", cause)

    // Unknown
    data class Unknown(override val cause: Throwable) :
        NetworkException("Unknown error occurred", cause)
}
```

#### 4.3 Safe API Call Wrapper

Create a wrapper function for safe API calls:

```kotlin
suspend fun <T> safeApiCall(
    errorParser: ErrorParser,
    apiCall: suspend () -> T
): NetworkResult<T> = try {
    NetworkResult.Success(apiCall())
} catch (e: Exception) {
    NetworkResult.Error(e.toNetworkException(errorParser))
}

private fun Exception.toNetworkException(errorParser: ErrorParser): NetworkException =
    when (this) {
        is UnknownHostException,
        is ConnectException -> NetworkException.NoInternetConnection

        is SocketTimeoutException -> NetworkException.Timeout

        is IOException -> NetworkException.ConnectionFailed(this)

        is HttpException -> {
            val code = code()
            val errorBody = errorParser.parse(response()?.errorBody()?.string())
            when (code) {
                401 -> NetworkException.Unauthorized
                403 -> NetworkException.Forbidden
                404 -> NetworkException.NotFound
                in 500..599 -> NetworkException.ServerError(code)
                else -> NetworkException.HttpError(code, errorBody)
            }
        }

        is SerializationException,
        is JsonException -> NetworkException.ParseError(this)

        else -> NetworkException.Unknown(this)
    }

class ErrorParser @Inject constructor(private val json: Json) {
    fun parse(errorJson: String?): ApiError? = try {
        errorJson?.let { json.decodeFromString<ApiError>(it) }
    } catch (e: Exception) {
        null
    }
}
```

---

### Phase 5: Remote Data Source

#### 5.1 Clean Data Source Implementation

```kotlin
class UserRemoteDataSource @Inject constructor(
    private val api: ApiService,
    private val errorParser: ErrorParser
) {
    suspend fun getUser(id: String): NetworkResult<UserDto> =
        safeApiCall(errorParser) { api.getUser(id) }

    suspend fun getUsers(page: Int, limit: Int): NetworkResult<PaginatedResponse<UserDto>> =
        safeApiCall(errorParser) { api.getUsers(page, limit) }

    suspend fun createUser(request: CreateUserRequest): NetworkResult<UserDto> =
        safeApiCall(errorParser) { api.createUser(request) }

    suspend fun updateUser(id: String, request: UpdateUserRequest): NetworkResult<UserDto> =
        safeApiCall(errorParser) { api.updateUser(id, request) }

    suspend fun deleteUser(id: String): NetworkResult<Unit> =
        safeApiCall(errorParser) {
            val response = api.deleteUser(id)
            if (!response.isSuccessful) {
                throw HttpException(response)
            }
        }

    suspend fun uploadAvatar(userId: String, imageFile: File): NetworkResult<UserDto> =
        safeApiCall(errorParser) {
            val requestFile = imageFile.asRequestBody("image/*".toMediaType())
            val body = MultipartBody.Part.createFormData("avatar", imageFile.name, requestFile)
            api.uploadAvatar(userId, body)
        }
}
```

#### 5.2 Repository Integration

Integrate with repository layer:

```kotlin
class UserRepositoryImpl @Inject constructor(
    private val remoteDataSource: UserRemoteDataSource,
    private val localDataSource: UserLocalDataSource,
    private val mapper: UserMapper,
    private val dispatchers: DispatcherProvider
) : UserRepository {

    override suspend fun getUser(id: String): Result<User> =
        withContext(dispatchers.io) {
            remoteDataSource.getUser(id)
                .map(mapper::toDomain)
                .toResult()
        }

    override suspend fun refreshUsers(): Result<List<User>> =
        withContext(dispatchers.io) {
            remoteDataSource.getUsers(page = 1, limit = 100)
                .map { response ->
                    val users = response.data.map(mapper::toDomain)
                    localDataSource.replaceAll(users.map(mapper::toDb))
                    users
                }
                .toResult()
        }
}

// Extension to convert NetworkResult to kotlin.Result
fun <T> NetworkResult<T>.toResult(): Result<T> = when (this) {
    is NetworkResult.Success -> Result.success(data)
    is NetworkResult.Error -> Result.failure(exception)
}
```

---

## Expected Output

### File Structure Created

```
network/
├── di/
│   ├── NetworkModule.kt
│   └── ApiModule.kt
├── interceptor/
│   ├── AuthInterceptor.kt
│   └── TokenAuthenticator.kt
├── api/
│   └── ApiService.kt
├── dto/
│   ├── UserDto.kt
│   ├── CreateUserRequest.kt
│   └── PaginatedResponse.kt
├── result/
│   ├── NetworkResult.kt
│   └── NetworkException.kt
├── util/
│   ├── SafeApiCall.kt
│   └── ErrorParser.kt
└── datasource/
    └── UserRemoteDataSource.kt
```

### Implementation Checklist

- [ ] OkHttpClient configured with timeouts and interceptors
- [ ] Retrofit configured with JSON converter
- [ ] API service interface with typed endpoints
- [ ] DTOs matching API contracts
- [ ] Auth interceptor for token injection
- [ ] Token authenticator for refresh handling
- [ ] NetworkResult sealed class for results
- [ ] NetworkException hierarchy for errors
- [ ] Safe API call wrapper function
- [ ] Remote data source with error handling

---

## Example Interaction

**User:** I need to integrate with a REST API for a social media app. The API uses JWT authentication and returns errors in a specific JSON format.

**Agent:** I'll help you set up a robust API integration. Let me gather some details:

1. What's the base URL of the API?
2. Can you share an example of the error response format?
3. Do you need token refresh functionality?

**User:** Base URL is `https://api.socialapp.com/v2/`. Errors look like: `{"error": {"code": "USER_NOT_FOUND", "message": "User does not exist"}}`. Yes, we need token refresh.

**Agent:** Based on your requirements, here's the error DTO:

```kotlin
@Serializable
data class ApiErrorResponse(
    val error: ApiError
)

@Serializable
data class ApiError(
    val code: String,
    val message: String
)
```

And the error parser:

```kotlin
class ErrorParser @Inject constructor(private val json: Json) {
    fun parse(errorJson: String?): ApiError? = try {
        errorJson?.let { json.decodeFromString<ApiErrorResponse>(it).error }
    } catch (e: Exception) {
        null
    }
}
```

**Shall I continue with the full network setup including token refresh?**

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective for API integration
- **ST-02** (Sequential Instructions): Phased approach from setup to error handling
- **RT-02** (Multi-Dimensional Analysis): Covers setup, auth, errors, data sources
- **RT-04** (Best Practice Review): Retrofit and OkHttp best practices
- **ST-03** (Output Format Templates): Code templates for each component
- **OC-05** (Severity Classification): Error categorization
- **NE-02** (Phased Workflow): Clear phases with checkpoints
- **NE-07** (Discussion Before Action): Review points before implementation

---

## Related Prompts

- [android_data_layer_implementation.md](android_data_layer_implementation.md) - Integrate API with data layer
- [android_dependency_injection.md](android_dependency_injection.md) - Configure network DI modules
- [android_error_handling_improvement.md](../improvement/android_error_handling_improvement.md) - Improve error handling patterns
- [android_offline_first_sync.md](android_offline_first_sync.md) - Add offline support
- [android_unit_test_generation.md](../testing/android_unit_test_generation.md) - Test API integration

---

## Customization Guide

### For GraphQL APIs

Replace Retrofit with Apollo Kotlin:
- Use Apollo Gradle plugin for code generation
- Replace API service with generated Query/Mutation classes
- Adapt error handling for GraphQL errors

### For WebSocket Connections

Add OkHttp WebSocket support:
- Implement `WebSocketListener` for real-time updates
- Add reconnection logic with exponential backoff
- Consider Scarlet library for reactive WebSockets

### For Certificate Pinning

Add SSL pinning for security:
```kotlin
val certificatePinner = CertificatePinner.Builder()
    .add("api.example.com", "sha256/AAAA...")
    .build()

OkHttpClient.Builder()
    .certificatePinner(certificatePinner)
    .build()
```

### For Caching

Add HTTP caching:
```kotlin
val cache = Cache(cacheDir, 10 * 1024 * 1024) // 10 MB

OkHttpClient.Builder()
    .cache(cache)
    .addNetworkInterceptor(CacheInterceptor())
    .build()
```

### For Request Throttling

Add rate limiting:
```kotlin
class ThrottlingInterceptor(
    private val maxRequestsPerSecond: Int
) : Interceptor {
    private val rateLimiter = RateLimiter.create(maxRequestsPerSecond.toDouble())

    override fun intercept(chain: Interceptor.Chain): Response {
        rateLimiter.acquire()
        return chain.proceed(chain.request())
    }
}
```
