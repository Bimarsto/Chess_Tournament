from views.tournament import TournamentDisplay, TournamentMenu
from views.messages import Error, Information
from controllers.round import RoundController

from models.tournament import TournamentModel
from models.player import PlayerModel
from tinydb import TinyDB


class TournamentController:

    def __init__(self):
        self.model = TournamentModel
        self.menu = TournamentMenu
        self.display = TournamentDisplay
        self.serialized_tournaments = []
        self.player = PlayerModel

    def create_new_tournament(self, tournament_information):
        from controllers.main_controller import MainController
        main = MainController()
        Information("Création d'un nouveau tournoi")
        self.model(tournament_information['name'],
                   tournament_information['location'],
                   tournament_information['start_date'],
                   tournament_information['end_date'],
                   tournament_information['time_control'],
                   tournament_information['description'],
                   tournament_information['number_of_rounds'],
                   tournament_information['number_of_players'])
        main.tournament_controller(self.model.all_tournaments[-1])

    def access_tournament(self):
        from controllers.main_controller import MainController
        main = MainController()
        if len(self.model.all_tournaments) > 0:
            TournamentDisplay().display_tournaments_list(self.model.all_tournaments)
            selected_tournament = TournamentMenu.select_tournament(self.model.all_tournaments)
            main.tournament_controller(selected_tournament)
        else:
            Error("Aucun tournoi accessible.")

    def modify_tournament(self, tournament):
        if len(self.model.all_tournaments) > 0:
            field = self.menu.modification_display()
            setattr(tournament, field[0], field[1])
        else:
            Error("Aucun tournoi accessible")

    def add_player(self, tournament, player):
        self.model.add_player(tournament, player)

    @staticmethod
    def is_full(tournament):
        if len(tournament.tournament_players) < tournament.number_of_players:
            is_full = False
        else:
            is_full = True
            Error('Le nombre de joueurs au tournoi est atteint. Vous ne pouvez plus ajouter de joueurs.')
        return is_full

    def start_round(self, tournament):
        if not self.is_full(tournament):
            Error('Il manque des participants. Vous ne pouvez pas lancer de rounds.')
        else:
            self.create_next_round(tournament)
            RoundController().play_round(tournament, tournament.tournament_rounds[-1])

    def create_next_round(self, tournament):
        if len(tournament.tournament_rounds) == 0:
            for player in tournament.tournament_players:
                player.tournament_score = 0
        if len(tournament.tournament_rounds) == tournament.number_of_rounds:
            Error('Tous les rounds de ce tournoi ont été lancés.')
            self.menu(tournament).tournament_creation_menu()
        else:
            if len(tournament.tournament_rounds) > 0:
                previous_round = tournament.tournament_rounds[-1]
                for match in previous_round.matchs:
                    if match.player1_score is None or match.player1_score is None:
                        Error('Tous les matchs du round précédent ne sont pas joués.'
                              ' Impossible de créer le prochain round.')
                        return
            next_round = RoundController().create_new_round(tournament)
            tournament.tournament_rounds.append(next_round)

    def save_all_tournaments(self):
        db = TinyDB('db.json')
        tournaments_table = db.table('tournaments')
        tournaments_table.truncate()
        for tournament in self.model.all_tournaments:
            self.save(tournament)

    def save(self, tournament):
        db = TinyDB('db.json')
        tournaments_table = db.table('tournaments')
        serialized_tournament = self.model.serialize(tournament)
        tournaments_table.insert(serialized_tournament)

    def load_all_tournaments(self):
        db = TinyDB('db.json')
        tournaments_table = db.table('tournaments')
        serialized_tournaments = tournaments_table.all()
        self.model.all_tournaments = []
        for tournament in serialized_tournaments:
            self.model.deserialize(tournament)
