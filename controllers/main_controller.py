from views.tournament import TournamentView, TournamentMenu, TournamentDisplay
from views.round import RoundDisplay
from views.match import MatchDisplay
from views.player import PlayerDisplay
from views.messages import Information
from views.menus import MainMenu, ReportMenu
from controllers.tournament import TournamentController
from controllers.player import PlayerController
from controllers.report import ReportController
from models.player import PlayerModel
from rich.console import Console


class MainController:

    def __init__(self):
        self.running = True
        self.tournament_information = TournamentView()
        self.tournament = TournamentController
        self.player = PlayerController
        self.player_model = PlayerModel
        self.report = ReportMenu()
        self.report_controller = ReportController
        self.player_display = PlayerDisplay()
        self.tournament_display = TournamentDisplay()
        self.match_display = MatchDisplay()
        self.round_display = RoundDisplay()
        self.console = Console(width=200)

    def run(self):
        self.console.rule("Gestionnaire de tournoi d'échec | Bienvenue")
        self.player().load_all_players()
        self.tournament().load_all_tournaments()
        self.main_menu_controller()

    def main_menu_controller(self):
        # self.tournament.load_tournaments()
        match MainMenu().get_choice():
            case '9':  # Quitter
                self.save_data()
                Information("A bientôt !")
                exit()
            case '1':  # Créer un nouveau tournoi
                self.tournament().create_new_tournament(self.tournament_information.creation())
                self.main_menu_controller()
            case '2':  # Accéder à un tournoi
                self.tournament_controller(self.tournament().access_tournament())
                self.main_menu_controller()
            case '3':  # Ajouter un nouveau joueur
                self.player().create_new_player()
                self.main_menu_controller()
            case '4':  # Modifier un joueur
                self.player().modify_player()
                self.main_menu_controller()
            case '5':  # Rapports
                self.reports_controller(self.report.get_report_type())
                self.main_menu_controller()

    def tournament_controller(self, tournament):
        match TournamentMenu(tournament).tournament_creation_menu():
            case '9':  # Retour au menu principal
                self.main_menu_controller()
            case '1':  # Modifier le tournoi
                self.tournament().modify_tournament(tournament)
                self.tournament_controller(tournament)
            case '2':  # Ajouter un joueur
                self.add_tournament_player(tournament)
                self.tournament_controller(tournament)
            case '3':  # Démarrer le prochain round
                self.tournament().start_round(tournament)
                self.tournament_controller(tournament)
            case '4':  # Afficher le classement
                self.tournament_display.tournament_classification(tournament)
                input('Appuyer sur "Entrée" pour revenir au menu')
                self.tournament_controller(tournament)

    def add_tournament_player(self, tournament):
        if self.tournament().is_full(tournament):
            self.tournament_controller(tournament)
        else:
            match TournamentMenu(tournament).add_player():
                case '9':  # Retour au menu du tournoi
                    self.tournament_controller(tournament)
                case '1':  # Joueur existant
                    self.player().select_player_to_add(tournament)
                    self.tournament_controller(tournament)
                case '2':  # Nouveau joueur
                    self.tournament().add_player(tournament, self.player().create_new_player())
                    self.tournament_controller(tournament)

    def reports_controller(self, report):
        match report:
            case '9':  # Retour au menu principal
                self.main_menu_controller()
            case '1':  # Liste de tous les joueurs | par ordre alphabétique
                self.report_controller().all_players_by_alphabetical_order()
            case '2':  # Liste de tous les joueurs | par classement
                self.report_controller().all_players_by_rank_order()
            case '3':  # Liste de tous les tournois
                self.report_controller().all_tournaments()
            case '4':  # Liste des joueurs pour un tournoi donné | par ordre alphabétique
                self.report_controller().players_by_alphabetical_order_for_a_tournament()
            case '5':  # Liste des joueurs pour un tournoi donné | par classement
                self.report_controller().players_by_rank_order_for_a_tournament()
            case '6':  # Liste des rounds pour un tournoi donné
                self.report_controller().rounds_for_a_tournament()
            case '7':  # Liste des matchs pour un tournoi donné
                self.report_controller().matchs_for_a_tournament()

    def save_data(self):
        self.player().save_all_players()
        self.tournament().save_all_tournaments()
