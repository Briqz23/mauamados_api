from typing import Optional
from pydantic import BaseModel

class MatchLikes(BaseModel):
    ma_id: int
    id_likes: list = None
    id_matchs: list = None

class UpdateMatchLikes(BaseModel):
    ma_id: int = None
    id_likes: Optional[list]
    id_matchs: Optional[list]