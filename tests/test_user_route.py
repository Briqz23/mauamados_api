from fastapi.testclient import TestClient
from main import app  # replace with the actual name of your FastAPI app
import pytest

client = TestClient(app)

def test_update_user():
    # Define a sample user to update
    user = {
        "name": "New Name",
        "profile_picture": ["new_photo.jpg"],
        "age": 25,
        "course": "New Course",
        "bio": "New Bio",
        "genero": "New Gender",
        "sexual_orientation": "New Orientation",
        "tags_preferences": ["new_tag"],
        "match": ["new_match"],
        "likes": ["new_like"],
        "login": "new_login@maua.br",
        "senha": "new_password"
    }

    # Replace 1 with the actual ma_id of the user you want to update
    response = client.put("/user/1", json=user)

    assert response.status_code == 200
    assert response.json()["name"] == "New Name"
    assert "new_photo.jpg" in response.json()["profile_picture"]
    # Add more assertions for the other fields