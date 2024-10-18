from sqlmodel import create_engine, SQLModel, Session
from contextlib import contextmanager
import os
from dotenv import load_dotenv
from loguru import logger
from app.models import Category, Ingredient  # Import your SQLModel models

# Load environment variables from .env file
load_dotenv()

# Fetch database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the engine using the provided database URL
engine = create_engine(
    DATABASE_URL,
    isolation_level="READ COMMITTED"  # Set the appropriate isolation level
)

def init_db():
    """Initialize the database by creating tables."""
    logger.info(f"Initializing DB with engine: {engine}")
    SQLModel.metadata.create_all(engine)  # This creates tables for all SQLModel models
    logger.info("DB initialized successfully")

# Dependency for FastAPI to get a database session
def get_session():
    """Provide a transactional scope around a series of operations."""
    with Session(engine) as session:
        yield session
