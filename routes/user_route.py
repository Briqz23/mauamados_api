from fastapi import HTTPException
from fastapi import APIRouter

from config.database import collection_name_user,collection_name_match
from models.user_model import User, UpdateUser
from models.match_model import MatchLikes

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
    ma_id = user.ma_id
    document = collection_name_user.find({"ma_id":ma_id})

    if document:
        return{"POXA DANIEL!!!": "Já existe um usuário com esse ID"}
    
    if not is_user_over_eighteen(user.age):
        raise HTTPException(status_code=400, detail="Only users over 18 can create an account")

    _id = collection_name_user.insert_one(dict(user))
    match = MatchLikes(ma_id=user.ma_id)
    collection_name_match.insert_one({"ma_id": dict(match)})
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
    return  users_serializer(collection_name_user.find({"ma_id": ma_id}))

@user_api_router.delete("/user/{ma_id}")
async def delete_user(ma_id:int):
    collection_name_user.find_one_and_delete({"ma_id": ma_id})
    return {"status": "ok"}

