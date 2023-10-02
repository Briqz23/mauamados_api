from fastapi import HTTPException
from fastapi import APIRouter

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

@user_api_router.post("/user")
async def create_user(user: User):
    if not is_user_over_eighteen(user.age):
        raise HTTPException(status_code=400, detail="Only users over 18 can create an account")

    _id = collection_name_user.insert_one(dict(user))
    return users_serializer(collection_name_user.find({"_id": _id.inserted_id}))

@user_api_router.put("/user/{id}")
async def update_user(id: str, user: UpdateUser):
    if user.name is not None:
        collection_name_user.find_one_and_update({"_id": ObjectId(id)}, {"$set": {'name': user.name}})
    if user.profile_picture is not None:
        collection_name_user.find_one_and_update({"_id": ObjectId(id)}, {"$push": {'profile_picture': user.profile_picture}})
    if user.age is not None:
        collection_name_user.find_one_and_update({"_id": ObjectId(id)}, {"$set": {'age': user.age}})
    if user.course is not None:
        collection_name_user.find_one_and_update({"_id": ObjectId(id)}, {"$set": {'course': user.course}})
    if user.bio is not None:
        collection_name_user.find_one_and_update({"_id": ObjectId(id)}, {"$set": {'bio': user.bio}})
    if user.genero is not None:
        collection_name_user.find_one_and_update({"_id": ObjectId(id)}, {"$set": {'genero': user.genero}})
    if user.sexual_orientation is not None:
        collection_name_user.find_one_and_update({"_id": ObjectId(id)}, {"$set": {'sexual_orientation': user.sexual_orientation}})
    if user.tags_preferences is not None:
        collection_name_user.find_one_and_update({"_id": ObjectId(id)}, {"$push": {'tags_preferences': {"$each": user.tags_preferences}}})
    return  users_serializer(collection_name_user.find({"_id": ObjectId(id)}))

@user_api_router.delete("/user/{id}")
async def delete_user(id: str):
    collection_name_user.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}

