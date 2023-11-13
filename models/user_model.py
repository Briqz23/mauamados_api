from enum import Enum
from typing import Optional
from pydantic import BaseModel

class SexualOrientation(str, Enum):
    heterosexual = "Heterossexual"
    homosexual = "Homossexual"
    bisexual = "Bissexual"

class Genero(str,Enum):
    male = "Masculino"
    famale = "Feminino"
    no_binary = "Não-binário"

class User(BaseModel):
    ma_id: int
    name: str
    profile_picture: Optional[list] =  None  
    age: int
    course : str
    bio: Optional[str] = None 
    genero: Genero 
    sexual_orientation: SexualOrientation
    tags_preferences: list
    match : list
    likes : list
    login : str
    senha : str

class UpdateUser(BaseModel):
    ma_id: int = None
    name: Optional[str] = None
    profile_picture: Optional[list] = None
    age: Optional[int] = None
    course : Optional[str] = None
    bio: Optional[str] = None
    genero: Optional[Genero] = None
    sexual_orientation: Optional[SexualOrientation] = None
    tags_preferences: Optional[list] = None
    match : Optional[list] = None
    likes : Optional[list] = None
    login : Optional[str] = None
    senha : Optional[str] = None

