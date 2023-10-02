from enum import Enum
from typing import Optional
from pydantic import BaseModel

class SexualOrientation(str, Enum):
    heterosexual = "heterosexual"
    homosexual = "homosexual"
    bisexual = "bisexual"

class Genero(str,Enum):
    male = "masculino"
    famale = "feminio"
    no_binary = "não-binário"

class User(BaseModel):
    name: str
    profile_picture: Optional[list] =  None  
    age: int
    course : str
    bio: Optional[str] = None 
    genero: Genero 
    sexual_orientation: SexualOrientation
    tags_preferences: list

class UpdateUser(BaseModel):
    name: Optional[str] = None
    profile_picture: Optional[list] = None
    age: Optional[int] = None
    course : Optional[str] = None
    bio: Optional[str] = None
    genero: Optional[Genero] = None
    sexual_orientation: Optional[SexualOrientation] = None
    tags_preferences: Optional[list] = None

