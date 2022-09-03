"""View for round"""
from rich.console import Console
from rich.table import Table
from views.messages import Error, Information


class RoundView:

    def __init__(self, active_round):
        self.round = active_round

    def display_round_matchs(self):
        console = Console()
        match_list = Table(title='Liste des matchs du round', title_style='bold blue')
        match_list.add_column("N°")
        match_list.add_column("Matchs")
        match_list.add_column("Scores")
        for match in self.round.matchs:
            match_list.add_row(f"{self.round.matchs.index(match)+1}",
                               f"{match.player1} contre {match.player2}",
                               f"{match.player1_score} - {match.player2_score}")
        console.print(match_list)

    def round_menu(self):
        match_index = ''
        match_list = []
        while match_index == '':
            match_index = input('Saisir le résultat du match n°: \n'
                                '(entrez le n° du match de la liste ci-dessus) \n')
            for match in self.round.matchs:
                match_list.append(self.round.matchs.index(match))
            if match_index.isdigit():
                if int(match_index)-1 not in match_list:
                    Error('Champs obligatoire! Merci de le renseigner.')
                    match_index = ''
            else:
                match_index = ''
        return match_index


