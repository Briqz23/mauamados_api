from enum import Enum
from typing import Optional
from pydantic import BaseModel

class SexualOrientation(str, Enum):
    heterosexual = "heterosexual"
    homosexual = "homosexual"
    bisexual = "bisexual"

class User(BaseModel):
    name: str
    profile_picture: Optional[str] = None  
    age: int
    bio: Optional[str] = None  
    sexual_orientation: SexualOrientation