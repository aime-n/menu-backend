from loguru import logger

def test_create_category(client):
    # Test creating a category
    response = client.post(
        "/categories/",
        json={
            "name": "Test Category",
            "parent_id": None,
            }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Category"
    assert data["parent_id"] is None
    assert "category_id" in data

def test_get_all_categories(client):
    # Test retrieving all categories
    response = client.get("/categories/")
    assert response.status_code == 200
    data = response.json()
    logger.info('All categories:')
    assert isinstance(data, list)
    assert len(data) > 0
    # assert data[-1]["name"] == "Test Category"

def test_get_category(client):
    # Test retrieving a single category by ID
    response = client.post(
        "/categories/",
        json={
            "name": "Another Category",
            "parent_id": None,
            }
    )
    assert response.status_code == 200
    category_id = response.json()["category_id"]
    response = client.get(f"/categories/{category_id}")
    assert response.status_code == 200
    data = response.json()
    logger.info('Data Get Category', data)
    assert data["name"] == "Another Category"
    assert data["category_id"] == category_id

def test_update_category(client):
    # Test updating a category
    response = client.post(
        "/categories/",
        json={
            "name": "Category to Update",
            "parent_id": None,
            }
    )

    assert response.status_code == 200
    category_id = response.json()["category_id"]

    # Update the category
    response = client.patch(
        f"/categories/{category_id}",
        json={"name": "Updated Category", 
              "parent_id": 1}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Category"
    assert data["parent_id"] == 1
    assert data["category_id"] == category_id
