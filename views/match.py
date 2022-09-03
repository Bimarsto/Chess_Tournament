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
