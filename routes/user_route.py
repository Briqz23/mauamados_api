from fastapi import HTTPException
from fastapi import APIRouter

from config.database import collection_name
from models.user_model import User

from schemas.user_schema import users_serializer
from bson import ObjectId

from services.services import is_user_over_eighteen


user_api_router = APIRouter()


@user_api_router.get("/user")
async def get_users():
    users = users_serializer(collection_name.find())
    return users

@user_api_router.post("/user")
async def create_user(user: User):
    if not is_user_over_eighteen(user.age):
        raise HTTPException(status_code=400, detail="Only users over 18 can create an account")

    _id = collection_name.insert_one(dict(user))
    return users_serializer(collection_name.find({"_id": _id.inserted_id}))

@user_api_router.put("/user/{id}")
async def update_user(id: str, user: User):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(user)
    })
    return users_serializer(collection_name.find({"_id": ObjectId(id)}))

@user_api_router.delete("/user/{id}")
async def delete_user(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}

