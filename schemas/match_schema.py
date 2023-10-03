def match_serializer(match) -> dict:
    return{
        "id" : str(match["_id"]),
        "ma_id" : match["ma_id"],
        "id_like" : match["id_like"],
        "id_matchs": match["id_matchs"]
    }

def matches_serializer(matches) -> list:
    return [match_serializer(match) for match in matches]