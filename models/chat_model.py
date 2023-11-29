from typing import List
from pydantic import BaseModel
from typing import List

class Mensagem(BaseModel):
    remetente: int
    receptor: int
    corpo: str

class Conversa(BaseModel):
    ma_id_user1 : int
    ma_id_user2: int
    conversa: list[Mensagem]