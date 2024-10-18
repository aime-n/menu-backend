import pytest
from datetime import datetime
from fastapi.testclient import TestClient

# Test creating a new ingredient
def test_create_ingredient(client: TestClient):
    response = client.post(
        "/ingredients/",
        json={
            "openfood_facts_id": "12345",
            "openfoodfacts_content": null,
            "name": "Tomato",
            "category_id": None,
            "created_at": datetime.now()}

    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Tomato"
    assert data["standard_name"] == "Solanum lycopersicum"
    assert data["synonyms"] == ["Red Fruit", "Tomato Plant"]
    assert "ingredient_id" in data

# Test getting an ingredient by ID
def test_get_ingredient(client: TestClient):
    # First, create an ingredient to test retrieval
    create_response = client.post(
        "/ingredients/",
        json={
            "openfood_facts_id": "54321",
            "name": "Cucumber",
            "standard_name": "Cucumis sativus",
            "category_id": None,
            "synonyms": ["Green Cucumber", "Salad Cucumber"]
        }
    )
    assert create_response.status_code == 201
    created_ingredient = create_response.json()

    # Now retrieve the ingredient by its ID
    response = client.get(f"/ingredients/{created_ingredient['ingredient_id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Cucumber"
    assert data["standard_name"] == "Cucumis sativus"

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
            "openfood_facts_id": "67890",
            "name": "Pepper",
            "standard_name": "Capsicum annuum",
            "category_id": None,
            "synonyms": ["Bell Pepper", "Capsicum"]
        }
    )
    assert create_response.status_code == 201
    created_ingredient = create_response.json()

    # Update the ingredient's name
    update_response = client.put(
        f"/ingredients/{created_ingredient['ingredient_id']}",
        json={
            "name": "Spicy Pepper",
            "openfood_facts_id": "67890",
            "standard_name": "Capsicum annuum",
            "category_id": None,
            "synonyms": ["Hot Pepper", "Spicy Capsicum"]
        }
    )
    assert update_response.status_code == 200
    updated_data = update_response.json()
    assert updated_data["name"] == "Spicy Pepper"
    assert updated_data["synonyms"] == ["Hot Pepper", "Spicy Capsicum"]

# Test deleting an ingredient
def test_delete_ingredient(client: TestClient):
    # First, create an ingredient to delete
    create_response = client.post(
        "/ingredients/",
        json={
            "openfood_facts_id": "98765",
            "name": "Carrot",
            "standard_name": "Daucus carota",
            "category_id": None,
            "synonyms": ["Orange Root", "Carrot Root"]
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
