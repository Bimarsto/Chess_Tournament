from models.round import RoundModel
from controllers.utils import Utils

from controllers.match import MatchController
from views.round import RoundView
from views.tournament import TournamentDisplay
from views.messages import Information
from views.match import MatchDisplay


class RoundController:

    def __init__(self):
        self.model = RoundModel

    def create_new_round(self, tournament):
        new_round = self.model(f"Round n° {len(tournament.tournament_rounds) + 1}",
                               len(tournament.tournament_rounds) + 1,
                               tournament.tournament_players)
        new_round.start = Utils.parse_date('maintenant')
        new_round.create_players_pairs()
        return new_round

    def play_round(self, tournament, active_round):
        match_display = MatchDisplay()
        tournament_display = TournamentDisplay()
        from controllers.main_controller import MainController
        main_controller = MainController()
        round_uncompleted = True
        while round_uncompleted:
            match_display.display_matchs_list_from_round(active_round, active_round.matchs)
            match_index = RoundView(active_round).round_menu()
            if int(match_index) == 0:
                main_controller.tournament_controller(tournament)
            else:
                MatchController().update_match_score(active_round.matchs[int(match_index) - 1])
                for match in active_round.matchs:
                    if match.player1_score is not None or match.player2_score is not None:
                        round_uncompleted = False
                    else:
                        round_uncompleted = True
                        self.play_round(tournament, active_round)
        active_round.finish = Utils.parse_date('maintenant')
        for match in active_round.matchs:
            match.player1.tournament_score += match.player1_score
            match.player2.tournament_score += match.player2_score
        Information('Round terminé!')
        tournament_display.tournament_classification(tournament)
        main_controller.tournament_controller(tournament)
