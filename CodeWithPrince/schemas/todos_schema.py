def todo_serializer(todo) -> dict:
    return {
        "id" : str(todo["_id"]),
        "name" : todo(["name"]),
        "description" : todo["description"],
        "completed" : todo["completed"]
    }

def todos_serializer(todos) -> list:
    return[todo_serializer(todo) for todo in todos]