import json
from fastapi import FastAPI
from fastapi.testclient import TestClient
from config.database import collection_name_user
from models.user_model import User
from schemas.user_schema import users_serializer
from routes.user_route import user_api_router

app = FastAPI()

app.include_router(user_api_router)
client = TestClient(app)
"""
def test_create_users():
    # Assuming 'users_serializer' just returns the user data without modification
    # This is a basic test, and you may need to adjust it based on your actual implementation

    # Create a list of User objects for testing
    test_users = [
        User(name="Test User 1", age=25, login="test1@maua.br", senha="password1"),
        User(name="Test User 2", age=30, login="test2@maua.br", senha="password2"),
    ]

    response = client.post("/users", json=test_users)

    # Check if the response status code is 200 OK
    assert response.status_code == 200

    # Parse the response JSON
    created_users = response.json()

    # Check if the created users match the expected users
    assert len(created_users) == len(test_users)

    # Check if the created users exist in the database
    for created_user in created_users:
        assert collection_name_user.find_one({"_id": created_user["_id"]})
"""