from datetime import datetime
from fastapi.testclient import TestClient

# Assuming user_id 7 as testuser exists

# Helper function to login and obtain an access token
def get_access_token(client: TestClient) -> str:
    """Helper function to get a JWT token by logging in."""
    # Log in to get the token
    response = client.post(
        "/users/token",
        data={
            "username": "testuser",
            "password": "testpassword123"
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == 200
    token_data = response.json()
    return token_data["access_token"]

# Test creating a new recipe
def test_create_recipe(client: TestClient):
    access_token = get_access_token(client)
    response = client.post(
        "/recipes/",
        json={
            "user_id": 7, 
            "title": "Chocolate Cake",
            "description": "A delicious and rich chocolate cake recipe",
            "instructions": "Mix all ingredients and bake at 350 degrees for 45 minutes.",
            "prep_time": 15,
            "cook_time": 45,
            "servings": 8,
            "image_url": "http://example.com/chocolate_cake.jpg",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        },
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Chocolate Cake"
    assert data["description"] == "A delicious and rich chocolate cake recipe"
    assert "recipe_id" in data

# Test getting a recipe by ID
def test_get_recipe(client: TestClient):
    access_token = get_access_token(client)
    
    # First, create a recipe to test retrieval
    create_response = client.post(
        "/recipes/",
        json={
            "user_id": 7, 
            "title": "Vanilla Cake",
            "description": "A light and fluffy vanilla cake",
            "instructions": "Mix ingredients and bake for 30 minutes at 350 degrees.",
            "prep_time": 10,
            "cook_time": 30,
            "servings": 6,
            "image_url": "http://example.com/vanilla_cake.jpg",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        },
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert create_response.status_code == 201
    created_recipe_id = create_response.json()['recipe_id']

    # Now retrieve the recipe by its ID
    response = client.get(
        f"/recipes/{created_recipe_id}",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Vanilla Cake"

# Test retrieving a list of recipes
def test_get_recipes(client: TestClient):
    access_token = get_access_token(client)
    
    response = client.get(
        "/recipes/",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list) 
    assert len(data) > 0 

# Test updating a recipe
def test_update_recipe(client: TestClient):
    access_token = get_access_token(client)
    
    # First, create a recipe to update
    create_response = client.post(
        "/recipes/",
        json={
            "user_id": 7,  
            "title": "Cheese Cake",
            "description": "A delicious cheesecake",
            "instructions": "Mix and bake for 45 minutes.",
            "prep_time": 20,
            "cook_time": 45,
            "servings": 8,
            "image_url": "http://example.com/cheesecake.jpg",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        },
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert create_response.status_code == 201
    created_recipe_id = create_response.json()['recipe_id']

    # Update the recipe's title and description
    update_response = client.put(
        f"/recipes/{created_recipe_id}",
        json={
            "user_id": 7,
            "title": "Updated Cheese Cake",
            "description": "A rich and updated cheesecake recipe",
            "instructions": "Mix, bake for 45 minutes, and let it cool.",
            "prep_time": 15,
            "cook_time": 45,
            "servings": 10,
            "image_url": "http://example.com/updated_cheesecake.jpg",
            "updated_at": datetime.now().isoformat()
        },
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert update_response.status_code == 200
    updated_data = update_response.json()
    assert updated_data["title"] == "Updated Cheese Cake"
    assert updated_data["description"] == "A rich and updated cheesecake recipe"

# Test deleting a recipe
def test_delete_recipe(client: TestClient):
    access_token = get_access_token(client)
    
    # First, create a recipe to delete
    create_response = client.post(
        "/recipes/",
        json={
            "user_id": 7,  
            "title": "Banana Bread",
            "description": "A moist and tasty banana bread",
            "instructions": "Mix ingredients and bake for 60 minutes at 350 degrees.",
            "prep_time": 15,
            "cook_time": 60,
            "servings": 8,
            "image_url": "http://example.com/banana_bread.jpg",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        },
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert create_response.status_code == 201
    created_recipe_id = create_response.json()['recipe_id']

    # Delete the recipe
    delete_response = client.delete(
        f"/recipes/{created_recipe_id}",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert delete_response.status_code == 204

    # Verify the recipe no longer exists
    get_response = client.get(
        f"/recipes/{created_recipe_id}",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert get_response.status_code == 404
