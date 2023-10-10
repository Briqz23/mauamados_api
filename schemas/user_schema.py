def user_serializer(user) -> dict:
    return {
        "id": str(user["_id"]),
        "ma_id": user["ma_id"],
        "name": user["name"],
        "profile_picture": user["profile_picture"],
        "age": user["age"],
        "course" : user["course"],
        "bio": user["bio"],
        "genero" : user["genero"],
        "sexual_orientation": user["sexual_orientation"],
        "tags_preferences": user["tags_preferences"],
        "match" : user["match"],
        "likes" : user["likes"],
        "login" : user["login"],
        "senha" : user["senha"]
    }

def users_serializer(users) -> list:
    return [user_serializer(user) for user in users]