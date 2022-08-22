


def serialize_player(player):
    serialized_player = {
        "last_name": player.last_name,
        "first_name": player.first_name,
        "birth_date": player.birth_date,
        "gender": player.gender,
        "rank": player.rank
    }
    return serialized_player