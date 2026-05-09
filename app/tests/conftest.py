import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine


@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    """Set up test database by dropping and recreating all tables."""
    # Drop all tables first to ensure fresh schema
    Base.metadata.drop_all(bind=engine)
    # Create all tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop tables after tests
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    """Fixture that provides a TestClient for the FastAPI application."""
    return TestClient(app)