from fastapi import HTTPException
from fastapi import APIRouter

from config.database import collection_name_match,collection_name_user
from models.match_model import MatchLikes, UpdateMatchLikes
from models.user_model import User, UpdateUser

from schemas.match_schema import match_serializer,matches_serializer
from schemas.user_schema import user_serializer
from bson import ObjectId

match_api_router = APIRouter()

@match_api_router.get("/match")
async def get_match():
    matches = matches_serializer(collection_name_match.find())
    return matches

