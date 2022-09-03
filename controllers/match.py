from views.match import MatchView
from models.match import MatchModel


class MatchController:

    @staticmethod
    def update_match_score(match):
        match_results = MatchView(match).get_results()
        MatchModel.results(match, match_results)
