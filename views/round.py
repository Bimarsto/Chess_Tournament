"""View for round"""
from rich.console import Console
from rich.table import Table
from views.messages import Error, Information

console = Console()


class RoundView:

    def __init__(self, round):
        self.round = round

    def display_round_matchs(self):
        match_list = Table(title='Liste des matchs du round', title_style='bold blue')
        match_list.add_column("Matchs")
        match_list.add_column("Scores")
        for match in self.round.matchs:
            match_list.add_row(f"{match.player1} contre {match.player2}")
            match_list.add_row(f"{match.player1_score} - {match.player2_score}")
        console.print(match_list)

