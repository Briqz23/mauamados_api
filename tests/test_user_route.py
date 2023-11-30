import pytest
from fastapi import HTTPException
from routes.user_route import create_user, create_users

class TestCreateUsers:
    
    def test_create_users_valid_data(self):
        valid_user_data = [
            {
                "ma_id": 1,
                "name": "John Doe",
                "age": 20,
                "course": "Computer Science",
                "genero": "Masculino",
                "sexual_orientation": "Heterossexual",
                "tags_preferences": ["tag1", "tag2"],
                "login": "john.doe@maua.br",
                "senha": "securepassword",
            }
        ]

        result = create_users(valid_user_data)
        assert result


    def test_create_underage_user():
        underage_user = {
            "ma_id": 2,
            "name": "Jane Doe",
            "age": 16,
            "course": "Engineering",
            "genero": "Feminino",
            "sexual_orientation": "Heterossexual",
            "tags_preferences": ["tag1", "tag2"],
            "login": "jane.doe@maua.br",
            "senha": "securepassword",
        }

        with pytest.raises(HTTPException) as exc_info:
            create_user(underage_user) 
        assert exc_info.value.status_code == 400
            
        