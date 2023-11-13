from fastapi import HTTPException
from fastapi import APIRouter, Response
import json

from config.database import collection_name_user
from models.user_model import User, UpdateUser
from schemas.user_schema import users_serializer
from bson import ObjectId

from services.services import is_user_over_eighteen, validar_login, validate_password



user_api_router = APIRouter()



@user_api_router.get("/user")
async def get_users():
    users = users_serializer(collection_name_user.find())
    return users

@user_api_router.get("/user/{ma_id}")
async def get_user(ma_id: int):
    return users_serializer(collection_name_user.find({"ma_id":ma_id}))

@user_api_router.post("/user")
async def create_user(user: User):

    if not is_user_over_eighteen(user.age):
        raise HTTPException(status_code=400, detail="Apenas usuários maiores de 18 podem criar a conta")

    if not validate_password(user.senha):
        raise HTTPException(status_code=400, detail="Senha deve ter ao menos 8 caracteres")
    if not validar_login(user.login):
        raise HTTPException(status_code=400, detail="login deve ter @maua.br")

    _id = collection_name_user.insert_one(dict(user))
    def send_mail():
        print("Um email de segurança foi enviado para o @maua.br do usuário")
    return users_serializer(collection_name_user.find({"_id": _id.inserted_id}))

@user_api_router.put("/user/{ma_id}")
async def update_user(ma_id: int, user: UpdateUser):
    if user.ma_id is not None:
        return{"POXA DANIEL!!!": "Por favor não altere o ma_id, vai destruir a database"}
    if user.name is not None:
        collection_name_user.find_one_and_update({"ma_id": ma_id}, {"$set": {'name': user.name}})
    if user.profile_picture is not None:
        collection_name_user.find_one_and_update({"ma_id": ma_id}, {"$push": {'profile_picture': user.profile_picture}})
    if user.age is not None:
        collection_name_user.find_one_and_update({"ma_id": ma_id}, {"$set": {'age': user.age}})
    if user.course is not None:
        collection_name_user.find_one_and_update({"ma_id": ma_id}, {"$set": {'course': user.course}})
    if user.bio is not None:
        collection_name_user.find_one_and_update({"ma_id": ma_id}, {"$set": {'bio': user.bio}})
    if user.genero is not None:
        collection_name_user.find_one_and_update({"ma_id": ma_id}, {"$set": {'genero': user.genero}})
    if user.sexual_orientation is not None:
        collection_name_user.find_one_and_update({"ma_id": ma_id}, {"$set": {'sexual_orientation': user.sexual_orientation}})
    if user.tags_preferences is not None:
        collection_name_user.find_one_and_update({"ma_id": ma_id}, {"$push": {'tags_preferences': {"$each": user.tags_preferences}}})
    if user.match is not None:
        collection_name_user.find_one_and_update({"ma_id": ma_id}, {"$push": {'match': {"$each": user.match}}})
    if user.likes is not None:
        collection_name_user.find_one_and_update({"ma_id": ma_id}, {"$push": {'likes': {"$each": user.likes}}})
    if user.login is not None:
        collection_name_user.find_one_and_update({"ma_id": ma_id}, {"$set": {'login': user.login}})
    if user.senha is not None:
        collection_name_user.find_one_and_update({"ma_id": ma_id}, {"$set": {'senha': user.senha}})
    return  users_serializer(collection_name_user.find({"ma_id": ma_id}))

@user_api_router.delete("/user/{ma_id}")
async def delete_user(ma_id:int):
    collection_name_user.find_one_and_delete({"ma_id": ma_id})
    return {"status": "ok"}

@user_api_router.get("/user/matches/{ma_id}")
async def get_matches(ma_id: int):
    query = collection_name_user.find_one({"ma_id": ma_id}, {"match": 1, "_id": 0})
    matches = query.get('match', [])
    return Response(content=json.dumps(matches), media_type="application/json")


@user_api_router.get("/user/likes/{ma_id}")
async def get_likes(ma_id:int):
    query = collection_name_user.find_one({"ma_id": ma_id},{"likes":1,"_id":0})
    likes = query.get('likes',[])
    return Response(content=json.dumps(likes),media_type="application/json")


#var url = Uri.parse('http://127.0.0.1:8000/login/?username=$username&password=$password');
@user_api_router.get("/login/")
async def login(username: str, password: str):
    result = collection_name_user.find_one({"login": username, "senha": password}, {"ma_id": 1})

    if result:
        return {"ID": str(result["ma_id"])}
    else:
        raise HTTPException(status_code=404, detail="Username and/or password not found")

@user_api_router.get("/user/senha/{ma_id}")
async def get_senha(ma_id:int):
    query = collection_name_user.find_one({"ma_id":ma_id},{"senha":1,"_id":0})
    senha = query.get('senha',[])
    return Response(content=json.dumps(senha),media_type="application/json")


@user_api_router.post("/user/post_like/{ma_id}/{like_id}")
async def post_like(ma_id: int, like_id: str):
    # Assuming you have imported and initialized collection_name_user properly
    collection_name_user.update_many(
        {"ma_id": ma_id},
        {"$push": {"likes": {"$each": [like_id]}}}
    )
    return {"Daniel, fique tranquilo": "O Like foi adicionado com sucesso!!!"}

@user_api_router.get("/user/get_matches/{ma_id}")
async def get_info(ma_id: int):
    # Get genero, match list, like list, sexual orientation
    query = collection_name_user.find_one(
        {"ma_id": ma_id},
        {"genero": 1, "match": 1, "likes": 1, "sexual_orientation": 1, "_id": 0},
    )

    if query:
        sexual_orientation = query.get("sexual_orientation")

        # Modify the query based on sexual orientation
        if sexual_orientation == "heterosexual":
            # Filter for different sex
            matches_query = {"genero": "feminino"}

        elif sexual_orientation == "homosexual":
            # Filter for the same sex
            matches_query = {"genero": query.get("genero")}

        elif sexual_orientation == "bisexual":
            # Show potential matches of all genders
            matches_query = {}

        else:
            # Handle other sexual orientations if needed
            matches_query = {}

        # Retrieve detailed information for potential matches of the opposite sex
        potential_matches = list(
            collection_name_user.find(
                {"ma_id": {"$ne": ma_id}, "genero": matches_query["genero"]},
                {"_id": 0, "ma_id": 1, "name": 1, "profile_picture": 1, "age": 1, "course": 1, "bio": 1,
                 "genero": 1, "sexual_orientation": 1, "tags_preferences": 1, "match": 1, "likes": 1,
                 "login": 1, "senha": 1}
            )
        )

        return Response(content=json.dumps(potential_matches), media_type="application/json")

    else:
        return Response(
            content=json.dumps({"error": "User not found"}),
            media_type="application/json",
            status_code=404,
        )

