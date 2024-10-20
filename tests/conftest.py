import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel
from app.main import app
from app.database import get_session, engine
from alembic import command
from alembic.config import Config
import os

# Path to your Alembic configuration file
ALEMBIC_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "alembic.ini")

# Override the get_session dependency to use the test database
def get_test_session():
    with Session(engine) as session:
        yield session

# Apply the override in the FastAPI app
app.dependency_overrides[get_session] = get_test_session

# Setup the database using Alembic migrations
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Load the Alembic configuration
    alembic_config = Config(ALEMBIC_CONFIG_PATH)
    
    # Run Alembic migrations to set up the database
    command.upgrade(alembic_config, "head")  # Apply all migrations
    
    yield  # Tests run here

    # Tear down the database after tests (if necessary)
    # command.downgrade(alembic_config, "base")  # Optionally drop tables or reset the database

# Initialize TestClient for FastAPI
@pytest.fixture(scope="module")
def client():
    return TestClient(app)
