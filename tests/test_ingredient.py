# import pytest
# from fastapi.testclient import TestClient
# from sqlmodel import Session, create_engine, SQLModel
# from app.main import app
# from app.database import get_session, engine
# import os
# from datetime import datetime
# from loguru import logger

# # Override the get_session dependency to use the test database
# def get_test_session():
#     with Session(engine) as session:
#         yield session

# # Apply the override in the FastAPI app
# app.dependency_overrides[get_session] = get_test_session

# # Create the database and tables
# @pytest.fixture(scope="module", autouse=True)
# def setup_database():
#     SQLModel.metadata.create_all(engine)
#     yield
#     SQLModel.metadata.drop_all(engine)

# # Initialize TestClient for FastAPI
# client = TestClient(app)

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
