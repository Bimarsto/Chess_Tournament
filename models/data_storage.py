from tinydb import TinyDB
from player import Player

# Players storage


def serialize_player(player):
    serialized_player = {
        'last_name': player.last_name,
        'first_name': player.first_name,
        'birth_date': player.birth_date,
        'gender': player.gender,
        'rank': player.rank
    }
    return serialized_player


def serialize_players(all_players):
    serialized_players = []
    for player in all_players:
        serialized_players.append(serialize_player(player))
    return serialized_players


def save_players(all_players):
    serialized_players = serialize_players(all_players)
    db = TinyDB('db.json')
    players_table = db.table('players')
    players_table.truncate()
    players_table.insert_multiple(serialized_players)


def deserialize_player(serialized_player):
    player = Player(
        last_name=serialized_player['last_name'],
        first_name=serialized_player['first_name'],
        birth_date=serialized_player['birth_date'],
        gender=serialized_player['gender'],
        rank=serialized_player['rank']
    )
    return player


def deserialize_players(serialized_players):
    all_players = []
    for serialized_player in serialized_players:
        all_players.append(deserialize_player(serialized_player))
    return all_players


def load_players():
    db = TinyDB('db.json')
    players_table = db.table('players')
    serialized_players = players_table.all()
    return serialized_players


# ************ code temp de test *****************
