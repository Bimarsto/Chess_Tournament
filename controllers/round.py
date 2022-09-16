from models.round import RoundModel
from controllers.utils import Utils


class RoundController:

    @staticmethod
    def create_new_round(tournament):
        new_round = RoundModel(f"Round n° {len(tournament.tournament_rounds) + 1}",
                               len(tournament.tournament_rounds) + 1,
                               tournament.tournament_players)
        new_round.start = Utils.parse_date('maintenant')
        new_round.create_players_pairs()
        return new_round
