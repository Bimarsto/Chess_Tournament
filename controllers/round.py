from models.round import RoundModel
from views.round import RoundView
from views.messages import Information
from controllers.match import MatchController
from controllers.utils import Utils


class RoundController:

    @staticmethod
    def create_new_round(tournament):
        new_round = Round(f"Round n° {len(tournament.tournament_rounds) + 1}",
                          len(tournament.tournament_rounds) + 1,
                          tournament.tournament_players)
        new_round.start = Utils.parse_date('maintenant')
        return new_round

