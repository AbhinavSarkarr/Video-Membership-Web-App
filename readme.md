# Video Membership Web Application

A modern web application built with FastAPI and Apache Cassandra (AstraDB) for managing video membership subscriptions. Features user authentication, session management, and a scalable NoSQL database backend.

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![Cassandra](https://img.shields.io/badge/Cassandra-AstraDB-blue.svg)](https://www.datastax.com/products/datastax-astra)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Author](#author)
- [License](#license)

## Overview

This project demonstrates building a production-ready membership application using modern Python web development practices. It leverages FastAPI for high-performance API endpoints and Apache Cassandra (via AstraDB) for scalable, distributed data storage.

### Key Objectives

- Build a scalable video membership platform
- Implement secure user authentication with password hashing
- Use NoSQL database for horizontal scalability
- Create RESTful API endpoints with automatic documentation
- Follow clean architecture patterns

## Features

- **User Management**: Registration, authentication, and profile management
- **Secure Authentication**: Argon2 password hashing for security
- **NoSQL Database**: Cassandra/AstraDB for distributed storage
- **Async API**: FastAPI with async/await for high performance
- **Template Rendering**: Jinja2 templates for server-side rendering
- **Auto Documentation**: Swagger UI and ReDoc API docs
- **Testing**: Pytest integration for test coverage

## Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    VIDEO MEMBERSHIP APPLICATION                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐         │
│   │   Client     │    │   FastAPI    │    │   AstraDB    │         │
│   │   Browser    │◄──►│   Backend    │◄──►│   Cassandra  │         │
│   └──────────────┘    └──────┬───────┘    └──────────────┘         │
│                              │                                       │
│                              ▼                                       │
│                    ┌─────────────────────┐                          │
│                    │   Jinja2 Templates  │                          │
│                    │   HTML Rendering    │                          │
│                    └─────────────────────┘                          │
│                                                                      │
│   ┌──────────────────────────────────────────────────────────────┐  │
│   │                      User Service                              │  │
│   │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐         │  │
│   │  │ Register│  │  Login  │  │ Profile │  │ Session │         │  │
│   │  └─────────┘  └─────────┘  └─────────┘  └─────────┘         │  │
│   └──────────────────────────────────────────────────────────────┘  │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

## Installation

### Prerequisites

- Python 3.10 or higher
- AstraDB account (free tier available at datastax.com)

### Setup

```bash
# Clone the repository
git clone https://github.com/AbhinavSarkarr/Video-Membership-Web-App.git
cd Video-Membership-Web-App

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Dependencies

```
fastapi
uvicorn
cassandra-driver
python-dotenv
pydantic-settings
email-validator
argon2-cffi
pytest
jinja2
```

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# AstraDB Configuration
ASTRA_DB_CLIENT_ID=your_client_id
ASTRA_DB_CLIENT_SECRET=your_client_secret
ASTRA_DB_KEYSPACE=your_keyspace

# Application Settings
SECRET_KEY=your_secret_key
DEBUG=true
```

### AstraDB Setup

1. Create an account at [DataStax Astra](https://www.datastax.com/products/datastax-astra)
2. Create a new database
3. Download the secure connect bundle
4. Get your client ID and secret from the database settings
5. Update the `.env` file with your credentials

## Usage

### Running the Application

```bash
# Development mode with auto-reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Access the application at `http://localhost:8000`

### API Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Running Tests

```bash
pytest app/tests/
```

## API Endpoints

### User Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Home page |
| `GET` | `/users` | List all users (limit 10) |
| `POST` | `/users/register` | Register new user |
| `POST` | `/users/login` | User login |
| `GET` | `/users/{user_id}` | Get user profile |
| `PUT` | `/users/{user_id}` | Update user profile |

### Example Request

```python
import requests

# Register a new user
response = requests.post(
    "http://localhost:8000/users/register",
    json={
        "email": "user@example.com",
        "password": "securepassword123",
        "username": "newuser"
    }
)
print(response.json())
```

## Technologies

| Technology | Purpose |
|------------|---------|
| **FastAPI** | High-performance web framework |
| **Cassandra/AstraDB** | Distributed NoSQL database |
| **Pydantic** | Data validation and settings |
| **Argon2** | Secure password hashing |
| **Jinja2** | Template rendering |
| **Uvicorn** | ASGI server |
| **pytest** | Testing framework |

## Project Structure

```
Video-Membership-Web-App/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry
│   ├── config.py            # Configuration settings
│   ├── db.py                # Database connection
│   ├── users/
│   │   ├── __init__.py
│   │   ├── models.py        # Cassandra models
│   │   ├── routes.py        # User endpoints
│   │   └── schemas.py       # Pydantic schemas
│   ├── templates/
│   │   └── *.html           # Jinja2 templates
│   └── tests/
│       └── test_*.py        # Test files
├── nbs/
│   └── *.ipynb              # Development notebooks
├── requirements.txt          # Dependencies
├── requirements.dev.txt      # Dev dependencies
├── pytest.ini               # Pytest configuration
├── .env                     # Environment variables
├── .gitignore
└── readme.md                # This file
```

## Database Schema

### User Model

```python
class User:
    user_id: UUID          # Primary key
    email: str             # Unique email address
    username: str          # Display name
    password_hash: str     # Argon2 hashed password
    created_at: datetime   # Registration timestamp
    is_active: bool        # Account status
```

## Security Features

- **Password Hashing**: Argon2id for secure password storage
- **Environment Variables**: Sensitive data stored in `.env`
- **Input Validation**: Pydantic models for request validation
- **Email Validation**: Built-in email format validation

## Future Enhancements

- [ ] Add video content management
- [ ] Implement subscription tiers
- [ ] Add payment integration (Stripe)
- [ ] Build frontend with React/Vue
- [ ] Add OAuth2 social login
- [ ] Implement rate limiting

## Author

**Abhinav Sarkar**
- GitHub: [@AbhinavSarkarr](https://github.com/AbhinavSarkarr)
- LinkedIn: [abhinavsarkarrr](https://www.linkedin.com/in/abhinavsarkarrr)
- Portfolio: [abhinav-ai-portfolio.lovable.app](https://abhinav-ai-portfolio.lovable.app/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- FastAPI documentation and community
- DataStax for AstraDB free tier
- The Python async community

---

<p align="center">
  <strong>Modern membership management with FastAPI and Cassandra</strong>
</p>
