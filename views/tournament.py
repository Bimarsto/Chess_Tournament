"""View for tounament"""
from views.error import Error

class TournamentView:
    """Tournament view"""

    def __init__(self):
        self.name = self._get_tournament_name(),
        self.location = self._get_tournament_location(),
        self.start_date = self._get_tournament_start_date(),
        self.end_date = self._get_tournament_end_date(),
        self.time_control = self._get_tournament_time_control(),
        self.description = self._get_tournament_description(),
        self.number_of_rounds = self._get_tournament_number_of_rounds(),
        self.max_players = self._get_tournament_max_players()


# ---------------------- A Factoriser -----------------
    @staticmethod
    def _get_tournament_name():
        tournament_name = ""
        count = 0
        while tournament_name == "":
            if count >= 1:
                Error("Champs obligatoire! Merci de le renseigner.").__call__()
            tournament_name = input("Quel est le nom du tournoi? \n")
            count += 1
        return tournament_name

    @staticmethod
    def _get_tournament_location():
        tournament_location = ""
        count = 0
        tournament_location = input("Indiquez le lieu ou se déroule le tournoi? \n")
        if not tournament_location:
            return None
        return tournament_location

    @staticmethod
    def _get_tournament_start_date():
        tournament_start_date = input("Quel est la date de début du tournoi? \n")
        if not tournament_start_date:
            return None
        return tournament_start_date

    @staticmethod
    def _get_tournament_end_date():
        tournament_end_date = input("Quel est la date de fin du tournoi? \n")
        if not tournament_end_date:
            return None
        return tournament_end_date

    @staticmethod
    def _get_tournament_time_control():
        tournament_time_control = input("Sélectionnez le contrôle de temps du tournoi: \n"
                                        "1 : Bullet \n"
                                        "2 : Blitz \n"
                                        "3 : Coup rapide \n")
        if not tournament_time_control:
            return None
        return tournament_time_control

    @staticmethod
    def _get_tournament_description():
        tournament_description = input("Ajoutez une decsription du tournoi? \n")
        if not tournament_description:
            return None
        return tournament_description

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

# --------------------------------------------------------------
