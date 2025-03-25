# tests/test_users.py
import pytest
from src.json_api import JSONAPI

client = JSONAPI()

@pytest.mark.smoke
def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.regression
def test_create_user():
    payload = {
        "name": "Vinod Vukkalam",
        "email": "Vinod.Vukkalam@example.com",
        "username": "vinodvr"
    }
    response = client.post("/users", data=payload)
    assert response.status_code == 201
    assert response.json().get("name") == "Vinod Vukkalam"

@pytest.mark.regression
def test_update_user():
    payload = {"name": "Vinod Rangaswamy Vukkalam"}
    response = client.put("/users/1", data=payload)
    assert response.status_code == 200
    assert response.json().get("name") == "Vinod Rangaswamy Vukkalam"

@pytest.mark.regression
def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
