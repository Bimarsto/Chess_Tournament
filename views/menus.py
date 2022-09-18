"""Base view."""
from views.messages import Error, Information


class MainMenu:

    def __init__(self):
        self.choice = ''

    def get_choice(self):
        Information('Menu Principal')
        self.choice = ''
        while self.choice == '':
            self.choice = input('Entrez votre choix : \n'
                                '1 : Créer un nouveau tournoi \n'
                                '2 : Accéder à un tournoi \n'
                                '3 : Ajouter un nouveau joueur \n'
                                '4 : Modifier un joueur \n'
                                '5 : Rapports \n'
                                '9 : Quitter \n')
            if self.choice not in ['9', '1', '2', '3', '4', '5']:
                Error('Veuillez entrer le n° de votre choix dans le menu.')
                self.choice = ''
        return self.choice


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
