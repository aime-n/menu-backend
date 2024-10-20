# tests/test_users.py

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session
from app.models.user import User
from app.utils.security import get_password_hash
from jose import jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

def test_register_user(client: TestClient):
    """Test registering a new user."""
    response = client.post(
        "/users/register",
        json={
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpassword123",
            "profile_pic": "http://example.com/pic.jpg",
            "bio": "New user bio",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "newuser"
    assert data["email"] == "newuser@example.com"
    assert data["profile_pic"] == "http://example.com/pic.jpg"
    assert data["bio"] == "New user bio"
    assert "user_id" in data
    assert "created_at" in data
    assert "updated_at" in data

# TODO falhando
def test_register_duplicate_username(client: TestClient):
    """Test registering a user with a duplicate username."""
    response = client.post(
        "/users/register",
        json={
            "username": "newuser",  # Duplicate username
            "email": "another@example.com",
            "password": "anotherpassword123",
            "profile_pic": None,
            "bio": "Another bio",
        },
    )
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Username already registered"

def test_register_duplicate_email(client: TestClient):
    """Test registering a user with a duplicate email."""
    response = client.post(
        "/users/register",
        json={
            "username": "anotheruser",
            "email": "newuser@example.com",  # Duplicate email
            "password": "anotherpassword123",
            "profile_pic": None,
            "bio": "Another bio",
        },
    )
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Email already registered"

# TODO falhando
def test_login_user(client: TestClient):  
    """Test logging in with correct credentials."""
    response = client.post(
        "/users/token",
        data={
            "username": "newuser",
            "password": "newpassword123",
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

# TODO falhando
def test_login_wrong_username(client: TestClient):
    """Test logging in with a wrong username."""
    response = client.post(
        "/users/token",
        data={
            "username": "wronguser",
            "password": "testpassword",
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Incorrect username or password"

def test_login_wrong_password(client: TestClient):
    """Test logging in with a wrong password."""
    response = client.post(
        "/users/token",
        data={
            "username": "newuser",
            "password": "wrongpassword",
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Incorrect username or password"

def test_get_current_user(client: TestClient):
    """Test retrieving the current user's profile."""
    # First, log in to get the access token
    login_response = client.post(
        "/users/token",
        data={
            "username": "newuser",
            "password": "newpassword123"
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert login_response.status_code == 200
    access_token = login_response.json()["access_token"]

    # Use the access token to get the current user profile
    response = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "newuser"
    assert data["email"] == "newuser@example.com"
    assert data["bio"] == "New user bio"
    assert "user_id" in data
    assert "created_at" in data
    assert "updated_at" in data

# TODO falhando
def test_get_current_user_unauthorized(client: TestClient):
    """Test retrieving the current user's profile without authentication."""
    response = client.get("/users/me")
    assert response.status_code == 401
    data = response.json()
    assert data["detail"] == "Not authenticated"

# TODO falhando
def test_update_current_user(client: TestClient):
    """Test updating the current user's profile."""
    # Log in to get the access token
    login_response = client.post(
        "/users/token",
        data={
            "username": "newuser",
            "password": "newpassword123"
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert login_response.status_code == 200
    access_token = login_response.json()["access_token"]

    # Update the user's bio and profile picture
    response = client.put(
        "/users/me",
        json={
            "bio": "Updated bio",
            "profile_pic": "http://example.com/newpic.jpg",
        },
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["bio"] == "Updated bio"
    assert data["profile_pic"] == "http://example.com/newpic.jpg"

# TODO falhando
def test_update_current_user_password(client: TestClient):
    """Test updating the current user's password."""
    # Log in to get the access token
    login_response = client.post(
        "/users/token",
        data={
            "username": "newuser",
            "password": "newpassword123"
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert login_response.status_code == 200
    access_token = login_response.json()["access_token"]

    # Update the user's password
    response = client.put(
        "/users/me",
        json={
            "password": "newsecurepassword",
        },
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "password" not in data  # Password should not be returned

    # Attempt to log in with the old password
    old_login_response = client.post(
        "/users/token",
        data={
            "username": "newuser",
            "password": "newpassword123"
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert old_login_response.status_code == 400
    assert old_login_response.json()["detail"] == "Incorrect username or password"

    # Log in with the new password
    new_login_response = client.post(
        "/users/token",
        data={
            "username": "newuser",
            "password": "newsecurepassword"
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert new_login_response.status_code == 200
    assert "access_token" in new_login_response.json()

# TODO falhando
def test_delete_current_user(client: TestClient):
    """Test deleting the current user's profile."""
    # Log in to get the access token
    login_response = client.post(
        "/users/token",
        data={
            "username": "newuser",
            "password": "newsecurepassword"
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert login_response.status_code == 200
    access_token = login_response.json()["access_token"]

    # Delete the user
    response = client.delete(
        "/users/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 204

    # Attempt to retrieve the deleted user's profile
    get_response = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert get_response.status_code == 401  # Token should no longer be valid

    # Attempt to log in again
    login_response = client.post(
        "/users/token",
        data={
            "username": "testuser",
            "password": "testpassword",
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert login_response.status_code == 400
    assert login_response.json()["detail"] == "Incorrect username or password"
