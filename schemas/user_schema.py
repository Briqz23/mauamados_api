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

def message_serializer(message) -> dict:
    return {
        "id": message.id,
        "sender": message.sender,
        "recipient": message.recipient,
        "content": message.content,
        "timestamp": message.timestamp
    }

def conversation_serializer(conversation) -> dict:
    return {
        "conversationId": conversation.conversationId,
        "participants": conversation.participants,
        "messages": [message_serializer(message) for message in conversation.messages]
    }


def conversations_serializer(conversations) -> list:
    return [conversation_serializer(conversation) for conversation in conversations]
