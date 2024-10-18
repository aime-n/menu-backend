import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel
from app.main import app
from app.database import get_session, engine

# Override the get_session dependency to use the test database
def get_test_session():
    with Session(engine) as session:
        yield session

# Apply the override in the FastAPI app
app.dependency_overrides[get_session] = get_test_session

# Setup the database once per test session
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    SQLModel.metadata.create_all(engine)  # Create the database and tables
    yield
    SQLModel.metadata.drop_all(engine)  # Drop the tables after tests

# Initialize TestClient for FastAPI
@pytest.fixture(scope="module")
def client():
    return TestClient(app)
