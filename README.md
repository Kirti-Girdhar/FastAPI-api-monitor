# FastAPI API Monitor

## Project Description

FastAPI API Monitor is a comprehensive monitoring and alerting system built with FastAPI. It enables users to monitor the health and performance of API endpoints, receive alerts when endpoints go down or experience issues, and access detailed statistics and analytics about monitored endpoints.

## Features

- **Endpoint Monitoring**: Add, manage, and monitor multiple API endpoints
- **Real-time Health Checks**: Automated periodic checks with configurable intervals
- **Alert Management**: Create and manage alerts based on endpoint status changes
- **Statistics & Analytics**: Track response times, success rates, and uptime metrics
- **User Authentication**: Secure user registration and JWT-based authentication
- **Scheduled Monitoring**: Background scheduler for continuous endpoint monitoring
- **RESTful API**: Complete REST API for all monitoring operations
- **Comprehensive Logging**: Built-in logging system for debugging and monitoring

## Tech Stack

### Backend Technologies
- **Language**: Python 3.8+
- **Framework**: FastAPI (Modern, fast web framework)
- **Database ORM**: SQLAlchemy (SQL toolkit and ORM)
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens with OAuth2)
- **Task Scheduling**: APScheduler (Advanced Python Scheduler for background jobs)
- **Rate Limiting**: SlowAPI (Distributed rate limiting for FastAPI)
- **Validation**: Pydantic (Data validation using Python type annotations)
- **Testing**: Pytest (Testing framework)
- **HTTP Client**: httpx (Async HTTP client library)
- **Security**: argon2-cffi, Bcrypt (Password hashing)
- **Database Migrations**: Alembic (SQLAlchemy database migration tool)

### Development & Tools
- **Version Control**: Git & GitHub
- **API Testing**: Postman (REST client for API testing)
- **Code Assistant**: GitHub Copilot (AI-powered code suggestions)
- **AI Assistance**: ChatGPT & Claude Haiku 4.5 (For development support and documentation)
- **API Documentation**: Swagger UI & ReDoc (Auto-generated interactive API docs)
- **Containerization**: Docker ready (for deployment)

## Folder Structure

```
FastAPI-api-monitor/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Application entry point
│   ├── config.py               # Configuration settings
│   ├── database.py             # Database setup & connection
│   │
│   ├── models/                 # SQLAlchemy ORM models
│   │   ├── __init__.py
│   │   ├── users.py            # User model
│   │   ├── endpoint.py         # Endpoint model
│   │   ├── check.py            # Health check model
│   │   └── alert.py            # Alert model
│   │
│   ├── routers/                # API route handlers
│   │   ├── __init__.py
│   │   ├── auth.py             # Authentication endpoints
│   │   ├── endpoints.py        # Endpoint management endpoints
│   │   ├── alerts.py           # Alert management endpoints
│   │   └── stats.py            # Statistics endpoints
│   │
│   ├── schemas/                # Pydantic validation schemas
│   │   ├── __init__.py
│   │   ├── user.py             # User schemas
│   │   ├── endpoint.py         # Endpoint schemas
│   │   ├── alert_schema.py     # Alert schemas
│   │   └── stats_schema.py     # Statistics schemas
│   │
│   ├── services/               # Business logic & services
│   │   ├── __init__.py
│   │   ├── monitoring_service.py    # Endpoint monitoring logic
│   │   └── stats_service.py         # Statistics calculation
│   │
│   ├── scheduler/              # Background task scheduling
│   │   ├── __init__.py
│   │   └── monitor_scheduler.py     # Scheduled monitoring tasks
│   │core/                  # Core application modules
│   │   ├── __init__.py
│   │   ├── cache.py            # Caching functionality
│   │   └── limiter.py          # Rate limiting configuration
│   │
│   ├── utils/                  # Utility functions
│   │   ├── __init__.py
│   │   ├── dependencies.py     # Dependency injection
│   │   ├── logger.py           # Logging configuration
│   │   └── security.py         # Password & token utilities
│   │
│   └── tests/                  # Unit & integration tests
│       ├── conftest.py         # Pytest configuration
│       ├── test_auth.py        # Auth endpoint tests
│       ├── test_endpoint.py    # Endpoint management tests
│       ├── test_alerts.py      # Alert management tests
│       ├── test_monitoring.py  # Monitoring service tests
│       ├── test_check.py       # Health check tests
│       ├── test_stats.py       # Statistics tests
│       └── test_retry.py       # Retry logic tests
│
├── alembic/                    # Database migrations
│   ├── versions/               # Migration scripts
│   ├── env.py                  # Alembic configuration
│   └── script.py.mako          # Migration template
│
├── .env                        # Environment variables (create this)
├── .gitignor12+ (required for production)
- pip (Python package manager)
- Virtual environment support  # Alembic configuration                  # Environment variables (create this)
├── .gitignore
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## How to Run

### Prerequisites

- Python 3.8 or higher
- PostgreSQL (or SQLite for development)
- pip (Python package manager)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd FastAPI-api-monitor
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate Virtual Environment**
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure Environment Variables**
   Creenv
   # Database Configuration
   DATABASE_HOSTNAME=localhost
   DATABASE_PORT=5432
   DATABASE_USERNAME=your_db_username
   DATABASE_PASSWORD=your_secure_password
   DATABASE_NAME=api_monitor
   
   # Authentication & Security
   SECRET_KEY=your-super-secret-key-change-this-in-production
   ALGORITHM=HS256
7. **Run the Application**
   ```bash
   # Development with auto-reload
   uvicorn app.main:app --reload
   
   # Production
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

   The API will be available at `http://localhost:8000`

8. **Access API Documentation**
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

### Running Tests

```bash
# Run all tests with verbose output
pytest app/tests/ -v

# Run tests with coverage report
pytest app/tests/ --cov=app

# Run specific test file
pytest app/tests/test_auth.py -v
```

### API Health Checks

The application provides health check endpoints for container orchestration and monitoring:

- `GET /health` - Basic health check
- `GET /ready` - Readiness check (verifies database connectivity)uvicorn app.main:app --reload
   ```

   The API will be available at `http://localhost:8000`

7. **Access API Documentation**
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

### Running Tests

```bash
pytest app/tests/
```

## API Endpoints

All endpoints (except registration and login) require JWT authentication via `Authorization: Bearer <token>` header.

### Authentication Endpoints

| Method | Endpoint | Description | Rate Limit |
|--------|----------|-------------|-----------|
| POST | `/api/v1/auth/register` | Register a new user | 3 per minute |
| POST | `/api/v1/auth/login` | Login and get access token | 5 per minute |

### Endpoint Management

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---|
| POST | `/api/v1/endpoints/` | Create a new endpoint to monitor | ✓ |
| GET | `/api/v1/endpoints/` | Get all endpoints for current user (paginated) | ✓ |
| DELETE | `/api/v1/endpoints/{id}` | Delete an endpoint | ✓ |
| GET | `/api/v1/endpoints/protected` | Protected test endpoint | ✓ |

### Alert Management

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---|
| GET | `/api/v1/alerts/` | Get all alerts for current user | ✓ |

### Statistics & Analytics

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---|
| GET | `/api/v1/stats/{endpoint_id}` | Get detailed statistics for specific endpoint | ✓ |

### System Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---|
| GET | `/` | Root endpoint / Basic health check | ✗ |
| GET | `/health` | Health check for container orchestration | ✗ |
| GET | `/ready` | Readiness check (database connectivity) | ✗ |

## Key Features

### 1. **Rate Limiting**
The application implements distributed rate limiting using SlowAPI:
- **Register endpoint**: 3 requests per minute
- **Login endpoint**: 5 requests per minute
- Helps prevent abuse and ensures fair API usage

### 2. **JWT Authentication**
- Secure token-based authentication using JWT
- OAuth2 password flow for login
- Automatic token validation on protected routes

### 3. **CORS Support**
- Configurable CORS origins via environment variables
- Allows cross-origin requests from specified domains
- Support for credentials and multiple HTTP methods

### 4. **Background Scheduling**
- Automated periodic health checks using APScheduler
- Runs scheduled monitoring tasks in the background
- Configurable check intervals per endpoint

### 5. **Database Migrations**
- Alembic for database schema management
- Version-controlled migrations
- Easy rollback and upgrade capabilities

## Example API Usage

### 1. Register a New User
```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepassword123"
  }'
```

### 2. Login and Get Access Token
```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=securepassword123"
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### 3. Create Endpoint to Monitor
```bash
curl -X POST "http://localhost:8000/api/v1/endpoints/" \
  -H "Authorization: Bearer {access_token}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My API Health",
    "url": "https://api.example.com/health",
    "method": "GET",
    "check_interval": 300
  }'
```

### 4. Get User Endpoints
```bash
curl -X GET "http://localhost:8000/api/v1/endpoints/?skip=0&limit=10" \
  -H "Authorization: Bearer {access_token}"
```

### 5. Get Endpoint Statistics
```bash
curl -X GET "http://localhost:8000/api/v1/stats/1" \
  -H "Authorization: Bearer {access_token}"
```

## Architecture & Core Modules

### App Structure

#### **Models** (`app/models/`)
- `users.py`: User account model with JWT authentication support
- `endpoint.py`: API endpoint to monitor with configuration
- `check.py`: Individual health check results and history
- `alert.py`: Alert definitions and notifications

#### **Schemas** (`app/schemas/`)
- `user.py`: User registration and token schemas
- `endpoint.py`: Endpoint creation and response schemas
- `alert_schema.py`: Alert creation and management schemas
- `stats_schema.py`: Statistics and analytics response schemas

#### **Services** (`app/services/`)
- `monitoring_service.py`: Core monitoring logic for endpoint health checks
- `stats_service.py`: Statistics calculation and aggregation

#### **Routers** (`app/routers/`)
- `auth.py`: User registration and login with rate limiting
- `endpoints.py`: CRUD operations for monitoring endpoints
- `alerts.py`: Alert management and retrieval
- `stats.py`: Statistics and analytics endpoints

#### **Core Modules** (`app/core/`)
- `limiter.py`: Rate limiting configuration and setup
- `cache.py`: Caching layer for improved performance

#### **Utils** (`app/utils/`)
- `security.py`: Password hashing (Argon2) and JWT token creation/validation
- `logger.py`: Structured logging setup and configuration
- `dependencies.py`: Dependency injection helpers (e.g., `get_current_user`)

#### **Scheduler** (`app/scheduler/`)
- `monitor_scheduler.py`: Background task scheduling using APScheduler for periodic health checks

### Database

The application uses **PostgreSQL** with SQLAlchemy ORM. Database schema is managed through **Alembic** migrations located in the `alembic/versions/` directory.

## Deployment

### Docker Deployment (Recommended)

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Run with:
```bash
docker build -t api-monitor .
docker run -p 8000:8000 --env-file .env api-monitor
```

### Environment Variables for Deployment

Ensure these variables are set in production:
- `DATABASE_HOSTNAME`: PostgreSQL server hostname
- `DATABASE_PORT`: PostgreSQL port (default: 5432)
- `DATABASE_USERNAME`: Database user
- `DATABASE_PASSWORD`: Database password (use strong password)
- `DATABASE_NAME`: Database name
- `SECRET_KEY`: Strong random string (use `openssl rand -hex 32`)
- `ALGORITHM`: JWT algorithm (HS256 recommended)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time
- `ALLOWED_ORIGINS`: Comma-separated list of allowed CORS origins

### Production Checklist

- [ ] Set `SECRET_KEY` to a strong random value
- [ ] Use PostgreSQL (not SQLite)
- [ ] Enable HTTPS/SSL
- [ ] Configure proper CORS origins
- [ ] Set up database backups
- [ ] Use environment variables for sensitive data
- [ ] Configure logging and monitoring
- [ ] Run database migrations before deployment
- [ ] Test health check endpoints (`/health`, `/ready`)
