"""Base view."""
from rich.console import Console

from views.messages import Error, Information

console = Console(width=75)

class MainMenu:
    """Menus view."""

    @staticmethod
    def main_menu():
        choice = ""
        count = 0
        while choice == "":
            console.rule("Gestionnaire de tournoi d'echec | Bienvenue")
            if count >=1:
                Error("Veuillez entrer le n° de votre choix dans le menu.")
            Information("Menu Principal")
            choice = input("Entrez votre choix : \n"
                           "0 Quitter \n"
                           "1 Creer un nouveau tournoi \n")
            count +=1
            if choice not in ["0", "1"]:
                choice = ""
        return choice


class TournamentMenu:
    def __init__(self, tournament):
        self.tournament = tournament


    def tournament_menu(self):
        choice = ""
        count = 0
        while choice == "":
            if count >= 1:
                Error("Veuillez entrer le n° de votre choix dans le menu.")
            Information(f"Menu du tournoi {self.tournament.name} - {len(self.tournament.tournament_players)}/"
                        f"{self.tournament.max_players} joueur(s) inscrit(s)")
            choice = input("Entrez votre choix : \n"
                           "0 Retour au menu principal \n"
                           "1 Ajouter un joueur \n"
                           "2 Démarrer le tournoi \n")
            count += 1
            if choice not in ["0", "1", "2"]:
                choice = ""
        return choice
