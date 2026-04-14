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
- **Database**: PostgreSQL/SQLite
- **Authentication**: JWT (JSON Web Tokens)
- **Task Scheduling**: APScheduler (Advanced Python Scheduler)
- **Validation**: Pydantic (Data validation using Python type annotations)
- **Testing**: Pytest (Testing framework)
- **HTTP Client**: httpx (Async HTTP client library)
- **Security**: argon2, Bcrypt (Password hashing)

### Development & Tools
- **Version Control**: Git & GitHub
- **API Testing**: Postman (REST client for API testing)
- **Code Assistant**: GitHub Copilot (AI-powered code suggestions)
- **AI Assistance**: ChatGPT & Claude Haiku 4.5 (For development support and documentation)
- **Documentation**: Swagger/OpenAPI (Auto-generated API docs)

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
│       └── test_stats.py       # Statistics tests
│
├── .env                        # Environment variables (create this)
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
   Create a `.env` file in the root directory with the following variables:
   ```
   DATABASE_HOSTNAME=localhost
   DATABASE_PORT=5432
   DATABASE_USERNAME=your_db_username
   DATABASE_PASSWORD=your_password
   DATABASE_NAME=api_monitor
   SECRET_KEY=your-secret-key-here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

6. **Run the Application**
   ```bash
   uvicorn app.main:app --reload
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

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and get access token |

### Endpoint Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/endpoints/` | Create a new endpoint to monitor |
| GET | `/endpoints/` | Get all endpoints for the current user |
| GET | `/endpoints/{id}` | Get endpoint details |
| DELETE | `/endpoints/{id}` | Delete an endpoint |
| GET | `/endpoints/protected` | Protected endpoint user |

### Alert Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/alerts/` | Get all alerts for the current user |

### Statistics & Analytics

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/stats/{endpoint_id}` | Get detailed stats for specific endpoint |

### Health Check

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint / Health check |

## Screenshots

### API Documentation Interface
- Access comprehensive API documentation via Swagger UI at `/docs`
- Interactive testing of all endpoints
- Automatic schema validation and response examples

### Sample Request/Response

**Register User**
```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"securepassword"}'
```

**Create Endpoint to Monitor**
```bash
curl -X POST "http://localhost:8000/endpoints/" \
  -H "Authorization: Bearer <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name":"My API",
    "url":"https://api.example.com/health",
    "method":"GET",
    "check_interval":300
  }'
```

**Get Statistics**
```bash
curl -X GET "http://localhost:8000/stats/" \
  -H "Authorization: Bearer <your-token>"
```

## Development

### Project Structure Overview

- **Models**: Define database schemas for Users, Endpoints, Checks, and Alerts
- **Routers**: FastAPI routers handling HTTP requests and responses
- **Services**: Business logic for monitoring and statistics calculation
- **Schemas**: Pydantic models for request/response validation
- **Scheduler**: APScheduler tasks for periodic endpoint health checks
- **Utils**: Helper functions for security, logging, and dependencies
- **Tests**: Comprehensive test suite using Pytest

### Key Features Explained

1. **Authentication**: JWT-based token authentication for secure API access
2. **Health Checks**: Automated scheduler runs periodic HTTP requests to monitored endpoints
3. **Alert System**: Triggers alerts based on endpoint status changes or performance thresholds
4. **Statistics**: Calculates uptime, response times, and success rates for each endpoint

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Support

For issues and questions, please open an issue on the GitHub repository.
