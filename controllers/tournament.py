from views.tournament import TournamentDisplay, TournamentMenu
from views.messages import Error
from controllers.round import RoundController
from controllers.player import PlayerController
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
        self.model(tournament_information['name'],
                   tournament_information['location'],
                   tournament_information['start_date'],
                   tournament_information['end_date'],
                   tournament_information['time_control'],
                   tournament_information['description'],
                   tournament_information['number_of_rounds'],
                   tournament_information['number_of_players'])
        self.save_tournaments()

    def modify_tournament(self, tournament):
        menu = self.menu(tournament)
        self.display().display_tournament_list(self.model.all_tournaments)
        tournament = menu.select_tournament(self.model.all_tournaments)
        field = menu.modification_display()
        setattr(tournament, field[0], field[1])
        self.save_tournaments()

    def add_player(self, tournament, player):
        self.model.add_player(tournament, player)
        self.save_tournaments()
        # self.load_tournaments()

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
            self.save_tournaments()
        else:
            Error('Il manque des participants. Vous ne pouvez pas lancer de rounds.')
            return

    def save_tournaments(self):
        serialized_tournaments = []
        db = TinyDB('db.json')
        tournaments_table = db.table('tournaments')
        tournaments_table.truncate()
        for tournament in self.model.all_tournaments:
            serialized_players = [self.player.serialize(player)
                                  for player in tournament.tournament_players]
            tournament_information = vars(tournament)
            print(tournament_information)
            tournament_information['tournament_players'] = serialized_players
            print(tournament_information)
            tournaments_table.insert(tournament_information)

    # def load_tournaments(self):
    #     db = TinyDB('db.json')
    #     tournaments_table = db.table('players')
    #     self.serialized_tournaments = tournaments_table.all()
    #     self.deserialize_tournaments()
    #
    # def deserialize_tournaments(self):
    #     self.model.all_tournaments = []
    #     for serialized_tournament in self.serialized_tournaments:
    #         self.deserialize_tournament(serialized_tournament)
    #     return self.model.all_tournaments

    # def deserialize_tournament(self, serialized_tournament):
    #     self.model(**serialized_tournament)
