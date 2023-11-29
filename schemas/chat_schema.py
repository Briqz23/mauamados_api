def conversa_serializer(conversa) -> dict:
    return{
        "ma_id_user1" : conversa("ma_id_user1"),
        "ma_id_user2" : conversa("ma_id_user2"),
        "conversa" : conversa("conversa")
    }