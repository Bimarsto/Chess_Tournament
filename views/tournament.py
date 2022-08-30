"""View for tournament"""
from views.messages import Error


class TournamentView:
    """Tournament view"""

    def __init__(self):
        self.name = self._get_information('Quel est le nom du tournoi?',
                                          'Champs obligatoire! Merci de le renseigner.')
        self.location = self._get_information('Indiquez le lieu ou se déroule le tournoi?',
                                              'Champs obligatoire! Merci de le renseigner.')
        self.start_date = self._get_information('Quel est la date de début du tournoi?',
                                                'Champs obligatoire! Merci de le renseigner.')
        self.end_date = self._get_information('Quel est la date de fin du tournoi?',
                                              'Champs obligatoire! Merci de le renseigner.')
        self.time_control = self._get_tournament_time_control()
        self.description = self._get_information('Ajoutez une decsription du tournoi',
                                                 'Champs obligatoire! Merci de le renseigner.')
        self.number_of_rounds = self._get_tournament_number_of_rounds()
        self.max_players = self._get_tournament_max_players()

    @staticmethod
    def _get_information(message, error_message):
        answer = ''
        count = 0
        while answer == '':
            if count >= 1:
                Error(error_message)
            answer = input(message + '\n')
            count += 1
        return answer

    @staticmethod
    def _get_tournament_time_control():
        tournament_time_control = ""
        count = 0
        while tournament_time_control == "":
            if count >= 1:
                Error("Champs obligatoire! Merci de le renseigner.").__call__()
            tournament_time_control = input("Sélectionnez le contrôle de temps du tournoi: \n"
                                        "1 : Bullet \n"
                                        "2 : Blitz \n"
                                        "3 : Coup rapide \n")
            count += 1
            if tournament_time_control not in ["1", "2", "3"]:
                tournament_time_control = ""
        return tournament_time_control

    @staticmethod
    def _get_tournament_number_of_rounds():
        tournament_number_of_rounds = input("Quel est le nombre de rounds pour ce tournoi? (4 par défaut) \n")
        if not tournament_number_of_rounds:
            return 4
        return tournament_number_of_rounds

    @staticmethod
    def _get_tournament_max_players():
        tournament_max_players = input("Quel est le nombre de joueurs pour ce tournoi? (8 par défaut) \n")
        if not tournament_max_players:
            return 8
        return tournament_max_players
