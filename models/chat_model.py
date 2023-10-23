from typing import List
from pydantic import BaseModel
from typing import List

class Message(BaseModel):
    id: str
    sender: str
    recipient: str
    content: str
    timestamp: str

class Conversation(BaseModel):
    conversationId: str
    participants: List[str]
    messages: List[Message]
