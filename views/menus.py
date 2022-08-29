"""Base view."""
from rich.console import Console

console = Console(width=75)

class MainMenu:
    """Menus view."""

    def main_menu():
        console.rule("Gestionnaire de tournoi d'echec | Bienvenue")
        console.print("Menu Principal", style="bold blue")
        choise = input("Entrez votre choix : \n"
                       "0 Quitter \n"
                       "1 Creer un nouveau tournoi \n")
        if choise in ["0", "1"]:
            return choise
        else:
            MainMenu.main_menu()
