"""Base view."""
from views.messages import Error, Information


class MainMenu:
    """Menus view."""
    def __init__(self):
        self.choice = ''

    def get_choice(self):
        Information('Menu Principal')
        self.choice = ''
        while self.choice == '':
            self.choice = input('Entrez votre choix : \n'
                                '1 : Creer un nouveau tournoi \n'
                                '2 : Accéder à un tournoi \n'
                                '3 : Ajouter un nouveau joueur \n'
                                '4 : Modifier un joueur \n'
                                '5 : Rapports \n'
                                '9 : Quitter \n')
            if self.choice not in ['9', '1', '2', '3', '4', '5']:
                Error('Veuillez entrer le n° de votre choix dans le menu.')
                self.choice = ''
        return self.choice


class RoundMenu:

    def __init__(self, round):
        self.round = round

    def round_menu(self):
        choice = ""
        count = 0
        while choice == "":
            if count >= 1:
                Error("Veuillez entrer le n° de votre choix dans le menu.")
            Information(f"Menu du {self.round.name}")
            choice = input("Mettre à jour le match n° : \n")
            count += 1
            if int(choice)-1 in range(0, len(self.round.matchs)):
                return int(choice)-1
            choice = ""


class ReportMenu:

    @staticmethod
    def get_report_type():
        choice = ''
        while choice == '':
            choice = input('Entrez votre choix : \n'
                           '1 : Liste de tous les joueurs | par ordre alphabétique \n'
                           '2 : Liste de tous les joueurs | par classement \n'
                           '3 : Liste de tous les tournois \n'
                           '4 : Liste des joueurs pour un tournoi donné | par ordre alphabétique \n'
                           '5 : Liste des joueurs pour un tournoi donné | par classement \n'
                           '6 : Liste des rounds pour un tournoi donné \n'
                           '7 : Liste des matchs pour un tournoi donné \n'
                           '9 : Retour au menu principal \n')
            if choice not in ['9', '1', '2', '3', '4', '5', '6', '7']:
                Error('Veuillez entrer le n° de votre choix dans le menu.')
                choice = ''
        return choice
