import pytest
from datetime import datetime
from fastapi.testclient import TestClient

# Test creating a new ingredient
def test_create_ingredient(client: TestClient):
    response = client.post(
        "/ingredients/",
        json={
            "openfoodfacts_id": "1234",
            "name": "Tomato",
            "category_id": None,
            "created_at": datetime.now().isoformat(),
            "openfoodfacts_content": {},
            "updated_at": datetime.now().isoformat()
            }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Tomato"
    assert data["openfoodfacts_id"] == "1234"
    assert "ingredient_id" in data

# Test getting an ingredient by ID
def test_get_ingredient(client: TestClient):
    # First, create an ingredient to test retrieval
    create_response = client.post(
        "/ingredients/",
        json={
            "openfoodfacts_id": "1234",
            "name": "Cucumber",
            "category_id": None,
            "created_at": datetime.now().isoformat(),
            "openfoodfacts_content": {},
            "updated_at": datetime.now().isoformat()
            }
    )
    assert create_response.status_code == 201
    created_ingredient = create_response.json()

    # Now retrieve the ingredient by its ID
    response = client.get(f"/ingredients/{created_ingredient['ingredient_id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Cucumber"

# Test retrieving a list of ingredients
def test_get_ingredients(client: TestClient):
    response = client.get("/ingredients/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)  # Should return a list
    assert len(data) > 0  # Ensure there is at least one item

# Test updating an ingredient
def test_update_ingredient(client: TestClient):
    # First, create an ingredient to update
    create_response = client.post(
        "/ingredients/",
        json={
            "openfoodfacts_id": "1234",
            "name": "Spicy",
            "category_id": None,
            "created_at": datetime.now().isoformat(),
            "openfoodfacts_content": {},
            "updated_at": datetime.now().isoformat()
            }
    )
    assert create_response.status_code == 201
    created_ingredient = create_response.json()

    # Update the ingredient's name
    update_response = client.put(
        f"/ingredients/{created_ingredient['ingredient_id']}",
        json={
            "openfoodfacts_id": "321",
            "name": "Spicy Pepper",
            "openfoodfacts_content": {},
            "updated_at": "2024-10-18T15:50:13.114Z",
            "category_id": None
            }
    )
    assert update_response.status_code == 200
    updated_data = update_response.json()
    assert updated_data["name"] == "Spicy Pepper"

# Test deleting an ingredient
def test_delete_ingredient(client: TestClient):
    # First, create an ingredient to delete
    create_response = client.post(
        "/ingredients/",
        json={
            "openfoodfacts_id": "1234",
            "name": "Spicy",
            "category_id": None,
            "created_at": datetime.now().isoformat(),
            "openfoodfacts_content": {},
            "updated_at": datetime.now().isoformat()
            }
    )
    assert create_response.status_code == 201
    created_ingredient = create_response.json()

    # Delete the ingredient
    delete_response = client.delete(f"/ingredients/{created_ingredient['ingredient_id']}")
    assert delete_response.status_code == 204

    # Verify the ingredient no longer exists
    get_response = client.get(f"/ingredients/{created_ingredient['ingredient_id']}")
    assert get_response.status_code == 404
