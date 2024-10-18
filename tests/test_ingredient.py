# # tests/test_ingredient.py

# import pytest
# from httpx import AsyncClient
# from sqlmodel import Session
# from loguru import logger  # Import loguru for logging
# from app.main import app
# from app.database import get_session, init_db, engine
# # from app.models.ingredient import Ingredient
# # from app.schemas.ingredient import IngredientCreate

# # Use a test database (e.g., SQLite in-memory)
# DATABASE_URL = "sqlite:///./test.db"

# logger.add("test_log.log", rotation="500 MB")  # Log to a file with rotation

# logger.info("Initializing test...")

# @pytest.fixture(scope="module")
# def test_db():
#     logger.info("Setting up the test database.")
#     init_db()
#     with Session(engine) as session:
#         yield session
#     logger.info("Tearing down the test database.")

# @pytest.fixture(scope="module")
# def client():
#     logger.info("Setting up the test client.")
#     app.dependency_overrides[get_session] = lambda: test_db()
    
#     with AsyncClient(app=app, base_url="http://test") as ac:
#         yield ac
    
#     logger.info("Tearing down the test client.")
#     app.dependency_overrides.clear()

# # @pytest.mark.asyncio
# # async def test_create_ingredient(client: AsyncClient):
# #     logger.info("Starting test: test_create_ingredient")
# #     ingredient_data = {
# #         "openfoodfacts_id": "12345",
# #         "name": "Test Ingredient",
# #         "standard_name": "Test Standard Name",
# #         "category_id": None,
# #         "synonyms": ["test_synonym"]
# #     }
    
# #     response = await client.post("/ingredients/", json=ingredient_data)
# #     logger.debug(f"Response status code: {response.status_code}, Response data: {response.json()}")
    
# #     assert response.status_code == 201
# #     data = response.json()
# #     assert data["name"] == "Test Ingredient"
# #     assert data["standard_name"] == "Test Standard Name"
# #     logger.info("Test test_create_ingredient passed successfully.")

# # @pytest.mark.asyncio
# # async def test_read_ingredient(client: AsyncClient):
# #     logger.info("Starting test: test_read_ingredient")
# #     response = await client.get("/ingredients/1")
# #     logger.debug(f"Response status code: {response.status_code}, Response data: {response.json()}")
    
# #     assert response.status_code == 200
# #     data = response.json()
# #     assert data["name"] == "Test Ingredient"
# #     logger.info("Test test_read_ingredient passed successfully.")

# # @pytest.mark.asyncio
# # async def test_update_ingredient(client: AsyncClient):
# #     logger.info("Starting test: test_update_ingredient")
# #     update_data = {"name": "Updated Ingredient Name"}
# #     response = await client.put("/ingredients/1", json=update_data)
# #     logger.debug(f"Response status code: {response.status_code}, Response data: {response.json()}")
    
# #     assert response.status_code == 200
# #     data = response.json()
# #     assert data["name"] == "Updated Ingredient Name"
# #     logger.info("Test test_update_ingredient passed successfully.")

# # @pytest.mark.asyncio
# # async def test_delete_ingredient(client: AsyncClient):
# #     logger.info("Starting test: test_delete_ingredient")
# #     response = await client.delete("/ingredients/1")
# #     logger.debug(f"Response status code: {response.status_code}")
    
# #     assert response.status_code == 204
# #     logger.info("Test test_delete_ingredient passed successfully.")
