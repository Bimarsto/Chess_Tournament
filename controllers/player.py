from views.player import PlayerView, PlayerMenu, PlayerDisplay
from models.player import PlayerModel
from controllers.tournament import TournamentController

from tinydb import TinyDB
from views.messages import Error, Information


class PlayerController:

    def __init__(self):
        self.model = PlayerModel
        self.display = PlayerDisplay
        self.tournament = TournamentController()
        self.menu = PlayerMenu
        self.serialized_players = []

    def create_new_player(self):
        new_player_information = PlayerView()
        new_player = self.model(new_player_information.last_name,
                                new_player_information.first_name,
                                new_player_information.birth_date,
                                new_player_information.sex,
                                new_player_information.rank)
        if new_player.sex == 'Homme':
            Information(f"Joueur {str(new_player)} créé.")
        else:
            Information(f"Joueuse {str(new_player)} créée.")
        return new_player

    def modify_player(self):
        if len(self.model.all_players) > 0:
            self.display().display_players_list(self.model.all_players)
            player = self.menu.select_player(self.model.all_players)
            field = self.menu.modification_display()
            setattr(player, field[0], field[1])
        else:
            Error("Aucun joueur accessible.")

    def save_all_players(self):
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.truncate()
        for player in self.model.all_players:
            self.save(player)

    def save(self, player):
        db = TinyDB('db.json')
        players_table = db.table('players')
        serialized_player = self.model.serialize(player)
        players_table.insert(serialized_player)

    def load_all_players(self):
        db = TinyDB('db.json')
        players_table = db.table('players')
        serialized_players = players_table.all()
        self.model.all_players = []
        for player in serialized_players:
            self.model.deserialize(player)

    def list_available_players(self, tournament):
        available_players = []
        for player in self.model.all_players:
            if player not in tournament.tournament_players:
                available_players.append(player)
        return available_players

    def select_player_to_add(self, tournament):
        from controllers.main_controller import MainController
        main = MainController()
        available_players = self.list_available_players(tournament)
        if len(available_players) > 0:
            self.display().display_players_list(available_players)
            player = PlayerMenu().select_player(available_players)
            self.tournament.add_player(tournament, player)
            main.tournament_controller(tournament)
        else:
            Error("Aucun joueur existant disponible.")
            main.add_tournament_player(tournament)
