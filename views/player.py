"""Base view for player."""
import dateparser
from datetime import time
from views.messages import Error


class PlayerView:
    """Player view."""

    def __init__(self):
        self.last_name = self._get_information('Quel est le nom de famille du joueur?',
                                               'Champs obligatoire! Merci de le renseigner.')
        self.first_name = self._get_information('Quel est le prénom du joueur?',
                                                'Champs obligatoire! Merci de le renseigner.')
        self.birth_date = self._get_player_birth_date()
        self.sex = self._get_player_sex()
        self.rank = self._get_rank()

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

    def _get_player_birth_date(self):
        birth_date = self._get_information("Quel est la date d'anniversaire du joueur?",
                                           "Champs obligatoire! Merci de le renseigner.")
        parsed_birth_date = dateparser.parse(birth_date).strftime("%d/%m/%Y")
        print(parsed_birth_date)
        return parsed_birth_date

    @staticmethod
    def _get_player_sex():
        sex = ""
        count = 0
        while sex == "":
            if count >= 1:
                Error("Champs obligatoire! Merci de le renseigner.")
            sex = input("Sélectionnez le sexe du joueur: \n"
                        "1 : Homme \n"
                        "2 : Femme \n")
            count += 1
            if sex not in ["1", "2"]:
                sex = ""
            return sex

    @staticmethod
    def _get_rank():
        rank = input("Quel est le classement du joueur? (0 par défaut) \n")
        if not rank:
            return 0
        return rank
