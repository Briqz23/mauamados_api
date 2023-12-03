from fastapi import APIRouter, HTTPException
from models.chat_model import Mensagem, Conversa
from schemas.chat_schema import conversa_serializer
from config.database import collection_name_conversas
from fastapi.encoders import jsonable_encoder

chat_api_router = APIRouter()

# @app.post('/enviar_mensagem/{remetente}/{receptor}')
# async def enviar_mensagem(mensagem: Mensagem):


@chat_api_router.post("/create_chat/")
async def criar_conversa(ma_id_1: int, ma_id_2: int, conversa: Conversa):
    conversa_dict = conversa.dict()
    result = collection_name_conversas.insert_one(conversa_dict)
    if result.inserted_id:
        return {"status": "Conversa criada com sucesso", "conversa_id": str(result.inserted_id)}
    else:
        raise HTTPException(status_code=500, detail="Erro ao criar a conversa no banco de dados")

@chat_api_router.get("/get_chat/{ma_id_1}/{ma_id_2}")
async def get_conversa(ma_id_1: int, ma_id_2: int):
    conversa_1_para_2 = collection_name_conversas.find_one(
        {"ma_id_user1": ma_id_1, "ma_id_user2": ma_id_2}
    )
    conversa_2_para_1 = collection_name_conversas.find_one(
        {"ma_id_user1": ma_id_2, "ma_id_user2": ma_id_1}
    )
    conversa = conversa_1_para_2 or conversa_2_para_1

    if conversa:
        conversa["_id"] = str(conversa["_id"])
        conversa = jsonable_encoder(conversa, by_alias=True)
        return {"conversa": conversa}
    else:
        raise HTTPException(status_code=404, detail="Poxa Daniel, não tem conversa ainda, vai lá bater um papo com a gatinha")
    
@chat_api_router.get("/get_todas_conversas/{maua_id}")
async def get_all_chats(maua_id: int):
   
    conversas_1 = collection_name_conversas.find({"ma_id_user1": maua_id})
    conversas_2 = collection_name_conversas.find({"ma_id_user2": maua_id})
    
    todas_as_conversas = list(conversas_1) + list(conversas_2)
    for conversa in todas_as_conversas:
        conversa["_id"] = str(conversa["_id"])
    todas_as_conversas_json = jsonable_encoder(todas_as_conversas, by_alias=True)
    return {"todas_as_conversas": todas_as_conversas_json}


@chat_api_router.post("/enviar_mensagem/")
async def add_message(mensagem: Mensagem):
    conversa = collection_name_conversas.find_one({
        "$or": [
            {"ma_id_user1": mensagem.remetente, "ma_id_user2": mensagem.receptor},
            {"ma_id_user1": mensagem.receptor, "ma_id_user2": mensagem.remetente}
        ]
    })

    if not conversa:
        raise HTTPException(status_code=404, detail="Conversa não encontrada")

    collection_name_conversas.update_one(
        {"_id": conversa["_id"]},
        {"$push": {"conversa": mensagem.dict()}}
    )

    return {"mensagem_adicionada": mensagem.dict()}

@chat_api_router.delete("/delete_chat/{ma_id_1}/{ma_id_2}")
async def delete_chat(ma_id_1:int, ma_id_2: int):
    resultado_1 = collection_name_conversas.delete_one(
        {"ma_id_user1": ma_id_1, "ma_id_user2": ma_id_2}
    )

    resultado_2 = collection_name_conversas.delete_one(
        {"ma_id_user1": ma_id_2, "ma_id_user2": ma_id_1}
    )

    if resultado_1.deleted_count or resultado_2.deleted_count:
        return {"POXA DANIEL!!!": "Queimando arquivos, o Oliver vai vim te pegar"}
    else:
        raise HTTPException(status_code=404, detail="Daniel, a conversa não foi delete, o Oliver ainda vai te pegar")
