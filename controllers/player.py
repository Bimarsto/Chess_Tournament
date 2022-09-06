from views.player import PlayerView, PlayerMenu, PlayerDisplay
from models.player import PlayerModel
from tinydb import TinyDB


class PlayerController:

    def __init__(self):
        self.model = PlayerModel
        self.display = PlayerDisplay
        self.menu = PlayerMenu
        self.serialized_players = []
        self.db = TinyDB('db.json')
        self.players_table = self.db.table('players')

    def create_new_player(self):
        new_player_information = PlayerView()
        new_player = self.model(new_player_information.last_name,
                                new_player_information.first_name,
                                new_player_information.birth_date,
                                new_player_information.sex,
                                new_player_information.rank)
        self.save(new_player)
        return new_player

    def modify_player(self):
        self.display().display_players_list(self.model.all_players)
        player = self.menu.select_player(self.model.all_players)
        field = self.menu.modification_display()
        setattr(player, field[0], field[1])
        self.save_all_players()

    def save_all_players(self):
        self.players_table.truncate()
        for player in self.model.all_players:
            self.save(player)

    def save(self, player):
        serialized_player = self.model.serialize(player)
        self.players_table.insert(serialized_player)

    def load_all_players(self):
        serialized_players = self.players_table.all()
        self.model.all_players = []
        for player in serialized_players:
            self.model.deserialize(player)
