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

    @staticmethod
    def display_matchs_list_from_round(list_origin, matchs_list):
        console = Console(width=200)
        matchs_table = Table(title='', title_style='bold blue')
        matchs_table.add_column('N°', justify='center')
        matchs_table.add_column('Matchs', justify='center')
        matchs_table.add_column('Scores', justify='center')
        for match in matchs_list:
            if match.player1_score is not None or match.player2_score is not None:
                matchs_table.add_row(f"{matchs_list.index(match)+1}",
                                     f"{match.player1} contre {match.player2}",
                                     f"{match.player1_score} - {match.player2_score}")
            else:
                matchs_table.add_row(f"{matchs_list.index(match) + 1}",
                                     f"{match.player1} contre {match.player2}",
                                     "Score à venir")
        console.print(matchs_table)

    @staticmethod
    def display_matchs_list_from_tournament(tournament):
        console = Console(width=200)
        Information(f"Liste des match du tournoi {str(tournament)}")
        if len(tournament.tournament_rounds) > 0:
            match_number = 1
            matchs_table = Table()
            matchs_table.add_column('N°', justify='center')
            matchs_table.add_column('Rounds', justify='center')
            matchs_table.add_column('Matchs', justify='center')
            matchs_table.add_column('Scores', justify='center')
            for round in tournament.tournament_rounds:
                for match in round.matchs:
                    if match.player1_score is not None or match.player2_score is not None:
                        matchs_table.add_row(f"{match_number}",
                                             f"{round.name}",
                                             f"{str(match)}",
                                             f"{match.player1_score} - {match.player2_score}")
                    else:
                        matchs_table.add_row(f"{match_number}",
                                             f"{round.name}",
                                             f"{str(match)}",
                                             "Score à venir")
                    match_number += 1
            console.print(matchs_table)
        else:
            Error("Aucun match n'a été trouver pour ce tournoi")
