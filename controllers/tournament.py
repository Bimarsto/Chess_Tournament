from views.tournament import TournamentDisplay, TournamentMenu
from views.messages import Error
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
        self.db = TinyDB('db.json')
        self.tournaments_table = self.db.table('tournaments')

    def create_new_tournament(self, tournament_information):
        self.model(tournament_information['name'],
                   tournament_information['location'],
                   tournament_information['start_date'],
                   tournament_information['end_date'],
                   tournament_information['time_control'],
                   tournament_information['description'],
                   tournament_information['number_of_rounds'],
                   tournament_information['number_of_players'])

    def modify_tournament(self, tournament):
        menu = self.menu(tournament)
        self.display().display_tournaments_list(self.model.all_tournaments)
        tournament = menu.select_tournament(self.model.all_tournaments)
        field = menu.modification_display()
        setattr(tournament, field[0], field[1])

    def add_player(self, tournament, player):
        self.model.add_player(tournament, player)

    def create_next_round(self, tournament):
        if len(tournament.tournament_players) == tournament.number_of_players:
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
                next_round = RoundController.create_new_round(tournament)
                tournament.tournament_rounds.append(next_round)
        else:
            Error('Il manque des participants. Vous ne pouvez pas lancer de rounds.')
            return

    def save_all_tournaments(self):
        self.tournaments_table.truncate()
        for tournament in self.model.all_tournaments:
            self.save(tournament)

    def save(self, tournament):
        serialized_tournament = self.model.serialize(tournament)
        self.tournaments_table.insert(serialized_tournament)

    def load_all_tournaments(self):
        serialized_tournaments = self.tournaments_table.all()
        self.model.all_tournaments = []
        for tournament in serialized_tournaments:
            self.model.deserialize(tournament)
