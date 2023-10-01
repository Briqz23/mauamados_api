def user_serializer(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "profile_picture": user["profile_picture"],
        "age": user["age"],
        "bio": user["bio"],
        "sexual_orientation": user["sexual_orientation"],
    }

def users_serializer(users) -> list:
    return [user_serializer(user) for user in users]