from rich.console import Console
from rich.table import Table
from views.messages import Error, Information


class MatchView:

    def __init__(self, active_match):
        self.match = active_match

    def get_results(self):
        match_result = ''
        Information(f'Résultats du match entre {self.match.player1.first_name} {self.match.player1.last_name} et'
                    f'{self.match.player2.first_name} {self.match.player2.last_name}.')
        while match_result == '':
            match_result = input(f'Quel est le résultat du match? \n'
                                 f'1 : Victoire de {self.match.player1.first_name} {self.match.player1.last_name} \n'
                                 f'2 : Match nul \n'
                                 f'3 : Victoire de {self.match.player2.first_name} {self.match.player2.last_name} \n')
            if match_result not in ['1', '2', '3']:
                Error('Champs obligatoire! Merci de le renseigner.')
                match_result = ''
        return match_result


class MatchDisplay:

    def __init__(self):
        self.console = Console(width=200)

    def display_matchs_list(self, list_origin, matchs_list):
        if len(list_origin) >= 6 and list_origin.name[:6] == 'Round ':
            match_table = Table(title='', title_style='bold blue')
        else:
            match_table = Table(title=f"Liste des matchs du {str(list_origin)}", title_style='bold blue')
        match_table.add_column('N°', justify='center')
        match_table.add_column('Matchs', justify='center')
        match_table.add_column('Scores', justify='center')
        for match in matchs_list:
            match_table.add_row(f"{matchs_list.index(match)+1}",
                                f"{match.player1} contre {match.player2}",
                                f"{match.player1_score} - {match.player2_score}")
        self.console.print(match_table)
