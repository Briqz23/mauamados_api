from fastapi import HTTPException
from fastapi import APIRouter, Response
import json

from config.database import collection_name_user
from models.user_model import User, UpdateUser
from schemas.user_schema import users_serializer
from bson import ObjectId

from services.services import is_user_over_eighteen


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
        raise HTTPException(status_code=400, detail="Only users over 18 can create an account")

    _id = collection_name_user.insert_one(dict(user))
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

@user_api_router.get("/user/login/{ma_id}")
async def get_login(ma_id:int):
    query = collection_name_user.find_one({"ma_id":ma_id},{"login":1,"_id":0})
    login = query.get('login',[])
    return Response(content=json.dumps(login),media_type="application/json")

@user_api_router.get("/user/senha/{ma_id}")
async def get_senha(ma_id:int):
    query = collection_name_user.find_one({"ma_id":ma_id},{"senha":1,"_id":0})
    senha = query.get('senha',[])
    return Response(content=json.dumps(senha),media_type="application/json")

@user_api_router.put("/user/put_like/{ma_id}/{like_id}")
async def put_like(ma_id:int, like_id:str):
    collection_name_user.update_one(
        {"ma_id" : ma_id},
        {"$push" :{"likes" : {"$each" : [like_id]}} }
    )
    return {"Daniel, fique tranquilo" : "O Like foi adicionado com sucesso!!!"}

@user_api_router.put("/user/put_match/{ma_id}/{match_id}")
async def put_match(ma_id:int, match_id:str):
    collection_name_user.update_one(
        {"ma_id":ma_id},
        {"$push" :{"match" : {"$each" : [match_id]}} }
    )
    return{"Daniel, fique tranquilo" : "O match foi adicionado com sucesso!!!"
           " Já pode conservar com a gatinha, Marca um date" " Chama ela pra fazer Calestenia"}

