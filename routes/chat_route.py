import asyncio
import collections
from fastapi import HTTPException
from fastapi import APIRouter, Response
import json
from config.database import collection_name_conversas
from models.chat_model import Conversation, Message
from schemas.user_schema import conversation_serializer



chat_api_router = APIRouter()


@chat_api_router.post("/conversations")
def create_conversation(conversation: Conversation):
    conversation_dict = conversation.dict()
    collection_name_conversas.insert_one(conversation_dict)
    return {"messages": "Conversation created successfully"}

# não funcionam ainda
@chat_api_router.get("/conversations/{conversation_id}")
async def get_conversation(conversation_id: str):
    
    conversation = await collection_name_conversas.find_one({"conversationId": conversation_id})
    if conversation:
        return conversation
    return {"messages": "Conversation not found"}

@chat_api_router.put("/conversations/{conversation_id}/messages/")
async def add_message(conversation_id: str, message: Message):
    message_dict = message.model_dump()
    await collection_name_conversas.update_one(
        {"conversationId": conversation_id},
        {"$push": {"messages": message_dict}}
    )
    return {"message": "Message added successfully"}