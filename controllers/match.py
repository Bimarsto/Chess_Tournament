from views.match import MatchView
from models.match import MatchModel


class MatchController:

    def __init__(self):
        self.view = MatchView
        self.model = MatchModel

    def update_match_score(self, match):
        match_results = self.view(match).get_results()
        self.model.results(match, match_results)
