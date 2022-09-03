from views.tournament import TournamentView, TournamentMenu, TournamentDisplay
from views.messages import Error
from controllers.round import RoundController
from models.tournament import TournamentModel, all_tournaments


class TournamentController:

    @staticmethod
    def create_new_tournament():
        new_tournament = TournamentView()
        TournamentModel(new_tournament.name,
                        new_tournament.location,
                        new_tournament.start_date,
                        new_tournament.end_date,
                        new_tournament.time_control,
                        new_tournament.description,
                        new_tournament.number_of_rounds,
                        new_tournament.number_of_players)

    @staticmethod
    def modify_tournament():
        TournamentDisplay().display_tournament_list(all_tournaments)
        tournament = TournamentMenu().select_tournament(all_tournaments)
        field = TournamentMenu().modification_display()
        setattr(tournament, field[0], field[1])

    @staticmethod
    def add_player(tournament, player):
        TournamentModel.add_player(tournament, player)

    @staticmethod
    def create_next_round(tournament):
        if len(tournament.tournament_players) == tournament.number_of_players:
            if len(tournament.tournament_rounds) == 0:
                for player in tournament.tournament_players:
                    player.tournament_score = 0
            if len(tournament.tournament_rounds) == tournament.number_of_rounds:
                Error('Tous les rounds de ce tournoi ont été lancés.')
                TournamentMenu(tournament).tournament_creation_menu()
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
                return next_round
        else:
            Error('Il manque des participants. Vous ne pouvez pas lancer de rounds.')
            return

