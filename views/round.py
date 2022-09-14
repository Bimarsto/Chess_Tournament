"""View for round"""
from rich.console import Console
from rich.table import Table
from views.messages import Error, Information
from views.match import MatchDisplay


class RoundView:

    def __init__(self, active_round):
        self.round = active_round

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


class RoundDisplay:

    def __init__(self):
        self.console = Console(width=200)
        self.match_display = MatchDisplay()

    def display_rounds_list(self, tournament):
        round_table = Table(title=f"Liste des rounds du {tournament.name}", title_style='bold blue')
        round_table.add_column('Nom', justify='center')
        round_table.add_column('Début', justify='center')
        round_table.add_column('Fin', justify='center')
        round_table.add_column('Matchs', justify='center')
        for round in tournament.tournament_rounds:
            matchs = ""
            for match in round.matchs:
                matchs += f"{str(match)}\n"
            round_table.add_row(f"{round.name}",
                                f"{round.start}",
                                f"{round.finish}",
                                f"{matchs}"
                                )
        self.console.print(round_table)
