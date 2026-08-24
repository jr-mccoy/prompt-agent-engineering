# OpenAPI Spec Generation — Code-First Templates & SDK

## Template 1 — Components Section

The following extends the main YAML spec in SKILL.md with reusable components.

```yaml
components:
  schemas:
    User:
      type: object
      required:
        - id
        - email
        - name
        - status
        - createdAt
      properties:
        id:
          type: string
          format: uuid
          readOnly: true
          description: Unique user identifier
        email:
          type: string
          format: email
        name:
          type: string
          minLength: 1
          maxLength: 100
        status:
          $ref: '#/components/schemas/UserStatus'
        role:
          type: string
          enum: [user, moderator, admin]
          default: user
        avatar:
          type: string
          format: uri
          nullable: true
        metadata:
          type: object
          additionalProperties: true
        createdAt:
          type: string
          format: date-time
          readOnly: true
        updatedAt:
          type: string
          format: date-time
          readOnly: true

    UserStatus:
      type: string
      enum: [active, inactive, suspended, pending]

    CreateUserRequest:
      type: object
      required:
        - email
        - name
      properties:
        email:
          type: string
          format: email
        name:
          type: string
          minLength: 1
          maxLength: 100
        role:
          type: string
          enum: [user, moderator, admin]
          default: user
        metadata:
          type: object
          additionalProperties: true

    UpdateUserRequest:
      type: object
      minProperties: 1
      properties:
        name:
          type: string
          minLength: 1
          maxLength: 100
        status:
          $ref: '#/components/schemas/UserStatus'
        role:
          type: string
          enum: [user, moderator, admin]
        metadata:
          type: object
          additionalProperties: true

    UserListResponse:
      type: object
      required:
        - data
        - pagination
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/User'
        pagination:
          $ref: '#/components/schemas/Pagination'

    Pagination:
      type: object
      required:
        - page
        - limit
        - total
        - totalPages
      properties:
        page:
          type: integer
          minimum: 1
        limit:
          type: integer
          minimum: 1
          maximum: 100
        total:
          type: integer
          minimum: 0
        totalPages:
          type: integer
          minimum: 0
        hasNext:
          type: boolean
        hasPrev:
          type: boolean

    Error:
      type: object
      required:
        - code
        - message
      properties:
        code:
          type: string
        message:
          type: string
        details:
          type: array
          items:
            type: object
            properties:
              field:
                type: string
              message:
                type: string
        requestId:
          type: string

  parameters:
    UserIdParam:
      name: userId
      in: path
      required: true
      schema:
        type: string
        format: uuid

    PageParam:
      name: page
      in: query
      schema:
        type: integer
        minimum: 1
        default: 1

    LimitParam:
      name: limit
      in: query
      schema:
        type: integer
        minimum: 1
        maximum: 100
        default: 20

  responses:
    BadRequest:
      description: Invalid request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'

    Unauthorized:
      description: Authentication required
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'

    NotFound:
      description: Resource not found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'

    RateLimited:
      description: Too many requests
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
      headers:
        Retry-After:
          schema:
            type: integer
        X-RateLimit-Limit:
          schema:
            type: integer
        X-RateLimit-Remaining:
          schema:
            type: integer

  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

    apiKey:
      type: apiKey
      in: header
      name: X-API-Key

security:
  - bearerAuth: []
```

## Template 2: Code-First Generation (Python/FastAPI)

```python
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime
from uuid import UUID
from enum import Enum

app = FastAPI(
    title="User Management API",
    version="2.0.0",
    servers=[
        {"url": "https://api.example.com/v2", "description": "Production"},
        {"url": "http://localhost:8000", "description": "Development"},
    ],
)

class UserStatus(str, Enum):
    active = "active"
    inactive = "inactive"
    suspended = "suspended"
    pending = "pending"

class UserRole(str, Enum):
    user = "user"
    moderator = "moderator"
    admin = "admin"

class UserCreate(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=1, max_length=100)
    role: UserRole = UserRole.user
    metadata: Optional[dict] = None

    model_config = {
        "json_schema_extra": {
            "examples": [{"email": "user@example.com", "name": "John Doe", "role": "user"}]
        }
    }

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    status: Optional[UserStatus] = None
    role: Optional[UserRole] = None
    metadata: Optional[dict] = None

class User(BaseModel):
    id: UUID
    email: EmailStr
    name: str
    status: UserStatus
    role: UserRole
    avatar: Optional[str] = None
    metadata: Optional[dict] = None
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")

    model_config = {"populate_by_name": True}

class Pagination(BaseModel):
    page: int = Field(..., ge=1)
    limit: int = Field(..., ge=1, le=100)
    total: int = Field(..., ge=0)
    total_pages: int = Field(..., ge=0, alias="totalPages")
    has_next: bool = Field(..., alias="hasNext")
    has_prev: bool = Field(..., alias="hasPrev")

class UserListResponse(BaseModel):
    data: List[User]
    pagination: Pagination

class ErrorResponse(BaseModel):
    code: str
    message: str
    details: Optional[List[dict]] = None
    request_id: Optional[str] = Field(None, alias="requestId")

@app.get("/users", response_model=UserListResponse, tags=["Users"])
async def list_users(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    status: Optional[UserStatus] = None,
    search: Optional[str] = Query(None, min_length=2, max_length=100),
):
    pass

@app.post("/users", response_model=User, status_code=201, tags=["Users"])
async def create_user(user: UserCreate):
    pass

@app.get("/users/{user_id}", response_model=User, tags=["Users"])
async def get_user(user_id: UUID = Path(...)):
    pass

@app.patch("/users/{user_id}", response_model=User, tags=["Users"])
async def update_user(user_id: UUID, user: UserUpdate):
    pass

@app.delete("/users/{user_id}", status_code=204, tags=["Users", "Admin"])
async def delete_user(user_id: UUID):
    pass

# Export spec
if __name__ == "__main__":
    import json
    print(json.dumps(app.openapi(), indent=2))
```

## Template 3: Code-First (TypeScript/tsoa)

```typescript
import {
  Controller, Get, Post, Patch, Delete,
  Route, Path, Query, Body, Response, SuccessResponse,
  Tags, Security,
} from "tsoa";

interface User {
  id: string;
  email: string;
  name: string;
  status: UserStatus;
  role: UserRole;
  avatar?: string;
  metadata?: Record<string, unknown>;
  createdAt: Date;
  updatedAt?: Date;
}

enum UserStatus { Active = "active", Inactive = "inactive", Suspended = "suspended", Pending = "pending" }
enum UserRole { User = "user", Moderator = "moderator", Admin = "admin" }

interface CreateUserRequest { email: string; name: string; role?: UserRole; metadata?: Record<string, unknown>; }
interface UpdateUserRequest { name?: string; status?: UserStatus; role?: UserRole; metadata?: Record<string, unknown>; }
interface ErrorResponse { code: string; message: string; details?: { field: string; message: string }[]; requestId?: string; }

@Route("users")
@Tags("Users")
export class UsersController extends Controller {
  @Get()
  @Security("bearerAuth")
  @Response<ErrorResponse>(400, "Invalid request")
  @Response<ErrorResponse>(401, "Unauthorized")
  public async listUsers(
    @Query() page: number = 1,
    @Query() limit: number = 20,
    @Query() status?: UserStatus,
    @Query() search?: string
  ): Promise<{ data: User[]; pagination: object }> {
    throw new Error("Not implemented");
  }

  @Post()
  @Security("bearerAuth")
  @SuccessResponse(201, "Created")
  @Response<ErrorResponse>(400, "Invalid request")
  @Response<ErrorResponse>(409, "Email exists")
  public async createUser(@Body() body: CreateUserRequest): Promise<User> {
    this.setStatus(201);
    throw new Error("Not implemented");
  }

  @Get("{userId}")
  @Security("bearerAuth")
  @Response<ErrorResponse>(404, "Not found")
  public async getUser(@Path() userId: string): Promise<User> {
    throw new Error("Not implemented");
  }

  @Patch("{userId}")
  @Security("bearerAuth")
  @Response<ErrorResponse>(404, "Not found")
  public async updateUser(@Path() userId: string, @Body() body: UpdateUserRequest): Promise<User> {
    throw new Error("Not implemented");
  }

  @Delete("{userId}")
  @Tags("Users", "Admin")
  @Security("bearerAuth")
  @SuccessResponse(204, "Deleted")
  @Response<ErrorResponse>(404, "Not found")
  public async deleteUser(@Path() userId: string): Promise<void> {
    this.setStatus(204);
  }
}
```

## Template 4: Validation & Linting

```bash
# Install tools
npm install -g @stoplight/spectral-cli @redocly/cli

# .spectral.yaml
cat > .spectral.yaml << 'EOF'
extends: ["spectral:oas"]
rules:
  operation-operationId: error
  operation-description: warn
  info-description: error
  operation-security-defined: error
  operation-success-response: error

  path-params-snake-case:
    description: Path parameters should be snake_case
    severity: warn
    given: "$.paths[*].parameters[?(@.in == 'path')].name"
    then:
      function: pattern
      functionOptions:
        match: "^[a-z][a-z0-9_]*$"

  schema-properties-camelCase:
    description: Schema properties should be camelCase
    severity: warn
    given: "$.components.schemas[*].properties[*]~"
    then:
      function: casing
      functionOptions:
        type: camel
EOF

spectral lint openapi.yaml

# redocly.yaml
cat > redocly.yaml << 'EOF'
extends:
  - recommended
rules:
  no-invalid-media-type-examples: error
  no-invalid-schema-examples: error
  operation-4xx-response: warn
  request-mime-type:
    severity: error
    allowedValues: [application/json]
  response-mime-type:
    severity: error
    allowedValues: [application/json, application/problem+json]
EOF

redocly lint openapi.yaml
redocly bundle openapi.yaml -o bundled.yaml
redocly preview-docs openapi.yaml
```

## SDK Generation

```bash
npm install -g @openapitools/openapi-generator-cli

# TypeScript client
openapi-generator-cli generate \
  -i openapi.yaml \
  -g typescript-fetch \
  -o ./generated/typescript-client \
  --additional-properties=supportsES6=true,npmName=@myorg/api-client

# Python client
openapi-generator-cli generate \
  -i openapi.yaml \
  -g python \
  -o ./generated/python-client \
  --additional-properties=packageName=api_client

# Go client
openapi-generator-cli generate \
  -i openapi.yaml \
  -g go \
  -o ./generated/go-client
```
