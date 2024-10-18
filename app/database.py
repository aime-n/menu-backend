# Manages database connection and session.

from sqlmodel import create_engine, SQLModel, Session, select
from contextlib import contextmanager
import os
from dotenv import load_dotenv
from loguru import logger
from sqlalchemy.orm import declarative_base
from app.models import Category, Ingredient

load_dotenv()  # Load environment variables from .env file

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    # echo=True,
    isolation_level="READ COMMITTED"  # Set the appropriate isolation level
)


Base = declarative_base()

def init_db():
    logger.info(f"Initializing DB with engine: {engine}")
    SQLModel.metadata.create_all(engine)
    logger.info("DB initialized successfully")

def get_session():
    with Session(engine) as session:
        yield session

