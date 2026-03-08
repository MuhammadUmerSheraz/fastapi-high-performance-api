# fastapi-high-performance-api

Production-ready FastAPI High-Performance API built with Clean Architecture and SOLID principles.

## Architecture

- **Clean Architecture** - Separation of concerns across domain, data, and presentation layers
- **Modular Structure** - Independently deployable and testable modules
- **SOLID Principles** - Maintainable, extensible codebase

## Tech Stack

FastAPI, Python 3.12, SQLAlchemy, Pydantic, Redis

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload
```

## Testing

```bash
pytest
```

## Docker

```bash
docker-compose up -d
```

## Documentation

- [Architecture](docs/architecture.md)
- [System Design](docs/system-design.md)
- [Deployment](docs/deployment.md)
