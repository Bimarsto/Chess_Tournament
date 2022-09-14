from views.tournament import TournamentView, TournamentMenu, TournamentDisplay
from views.round import RoundView, RoundDisplay
from views.match import MatchDisplay
from views.player import PlayerMenu, PlayerDisplay
from views.messages import Error, Information
from views.menus import MainMenu, ReportMenu
from controllers.tournament import TournamentController
from controllers.match import MatchController
from controllers.player import PlayerController
from controllers.utils import Utils
from models.player import PlayerModel
from rich.console import Console


class MainController:

    def __init__(self):
        self.running = True
        self.mainmenu = MainMenu()
        self.tournament_information = TournamentView()
        self.tournament = TournamentController()
        self.player = PlayerController()
        self.player_model = PlayerModel
        self.report = ReportMenu()
        self.player_display = PlayerDisplay()
        self.tournament_display = TournamentDisplay()
        self.match_display = MatchDisplay()
        self.round_display = RoundDisplay()

    def run(self):
        console = Console(width=200)
        console.rule("Gestionnaire de tournoi d'echec | Bienvenue")
        self.player.load_all_players()
        self.tournament.load_all_tournaments()
        while self.running:
            self.main_menu_controller()

    def main_menu_controller(self):
        # self.tournament.load_tournaments()
        match self.mainmenu.get_choice():
            case '9':  # Quitter
                self.player.save_all_players()
                self.tournament.save_all_tournaments()
                self.running = False
                Information("A bientot !")
                exit()
            case '1':  # Créer un nouveau tournoi
                Information("Création d'un nouveau tournoi")
                self.tournament.create_new_tournament(self.tournament_information.creation())
                new_tournament = self.tournament.model.all_tournaments[-1]
                self.tournament_controller(new_tournament)
            case '2':  # Accéder à un tournoi
                if len(self.tournament.model.all_tournaments) > 0:
                    TournamentDisplay().display_tournaments_list(self.tournament.model.all_tournaments)
                    selected_tournament = TournamentMenu.select_tournament(self.tournament.model.all_tournaments)
                    self.tournament_controller(selected_tournament)
                else:
                    Error("Aucun tournoi accessible.")
            case '3':  # Ajouter un nouveau joueur
                self.player.create_new_player()
            case '4':  # Modifier un joueur
                if len(self.player.model.all_players) > 0:
                    self.player.modify_player()
                else:
                    Error("Aucun joueur accessible.")
            case '5':  # Rapports
                self.reports_controller(self.report.get_report_type())

    def tournament_controller(self, tournament):
        match TournamentMenu(tournament).tournament_creation_menu():
            case '9':  # Retour au menu principal
                self.main_menu_controller()
            case '1':  # Ajouter un joueur
                if len(tournament.tournament_players) < tournament.number_of_players:
                    self.add_tournament_player(tournament)
                else:
                    Error('Le nombre de joueurs au tournoi est atteint. Vous ne pouvez plus ajouter de joueurs.')
                    self.tournament_controller(tournament)
            case '2':  # Démarreer le prochain round
                self.tournament.create_next_round(tournament)
                active_round = tournament.tournament_rounds[-1]
                if active_round is None:
                    self.tournament_controller(tournament)
                else:
                    self.play_round(tournament, active_round)

    def add_tournament_player(self, tournament):
        match TournamentMenu(tournament).add_player():
            case '9':  # Retour au menu du tournoi
                TournamentMenu(tournament).tournament_creation_menu()
            case '1':  # Joueur existant
                available_players = []
                for player in self.player_model.all_players:
                    if player not in tournament.tournament_players:
                        available_players.append(player)
                if len(available_players) > 0:
                    self.player_display.display_players_list(available_players)
                    player = PlayerMenu().select_player(available_players)
                    self.tournament.add_player(tournament, player)
                    self.tournament_controller(tournament)
                else:
                    Error("Aucun joueur existant disponnible.")
                    self.add_tournament_player(tournament)
            case '2':  # Nouveau joueur
                player = self.player.create_new_player()
                self.tournament.add_player(tournament, player)
                self.tournament_controller(tournament)

    def reports_controller(self, report):
        match report:
            case '9':
                self.main_menu_controller()
            case '1':
                if len(self.player_model.all_players) > 0:
                    self.player_display.report(self.player_model.all_players, 'ordre alphabétique')
                    input('Appuyer sur "Entrée" pour revenir au menu')
                    self.reports_controller(self.report.get_report_type())
                else:
                    Error("Aucun joueur accessible.")
            case '2':
                if len(self.player_model.all_players) > 0:
                    self.player_display.report(self.player_model.all_players, 'classement')
                    input('Appuyer sur "Entrée" pour revenir au menu')
                    self.reports_controller(self.report.get_report_type())
                else:
                    Error("Aucun joueur accessible.")
            case '3':
                if len(self.tournament.model.all_tournaments) > 0:
                    self.tournament_display.display_tournaments_list(self.tournament.model.all_tournaments)
                    input('Appuyer sur "Entrée" pour revenir au menu')
                    self.reports_controller(self.report.get_report_type())
                else:
                    Error("Aucun tournoi accessible.")
            case '4':
                if len(self.tournament.model.all_tournaments) > 0:
                    self.tournament_display.display_tournaments_list(self.tournament.model.all_tournaments)
                    tournament = self.tournament.menu.select_tournament(self.tournament.model.all_tournaments)
                    if len(tournament.tournament_players) > 0:
                        self.player_display.report(tournament.tournament_players, 'ordre alphabétique')
                        input('Appuyer sur "Entrée" pour revenir au menu')
                    else:
                        Error("Aucun joueur inscrit pour ce tournoi.")
                    self.reports_controller(self.report.get_report_type())
                else:
                    Error("Aucun tournoi accessible.")
            case '5':
                if len(self.tournament.model.all_tournaments) > 0:
                    self.tournament_display.display_tournaments_list(self.tournament.model.all_tournaments)
                    tournament = self.tournament.menu.select_tournament(self.tournament.model.all_tournaments)
                    if len(tournament.tournament_players) > 0:
                        self.player_display.report(tournament.tournament_players, 'classement')
                        input('Appuyer sur "Entrée" pour revenir au menu')
                    else:
                        Error("Aucun joueur inscrit pour ce tournoi.")
                    self.reports_controller(self.report.get_report_type())
                else:
                    Error("Aucun tournoi accessible.")
            case '6':
                if len(self.tournament.model.all_tournaments) > 0:
                    self.tournament_display.display_tournaments_list(self.tournament.model.all_tournaments)
                    tournament = self.tournament.menu.select_tournament(self.tournament.model.all_tournaments)
                    if len(tournament.tournament_rounds) > 0:
                        self.round_display.display_rounds_list(tournament)
                        input('Appuyer sur "Entrée" pour revenir au menu')
                    else:
                        Error("Aucun round n'est créé pour ce tournoi.")
                    self.reports_controller(self.report.get_report_type())
                else:
                    Error("Aucun tournoi accessible.")
            case '7':
                if len(self.tournament.model.all_tournaments) > 0:
                    self.tournament_display.display_tournaments_list(self.tournament.model.all_tournaments)
                    tournament = self.tournament.menu.select_tournament(self.tournament.model.all_tournaments)
                    if len(tournament.tournament_rounds) > 0:
                        self.match_display.display_matchs_list_from_tournament(tournament)
                        input('Appuyer sur "Entrée" pour revenir au menu')
                    else:
                        Error("Aucun round n'est créé pour ce tournoi.")
                    self.reports_controller(self.report.get_report_type())
                else:
                    Error("Aucun tournoi accessible.")

    def play_round(self, tournament, active_round):
        round_uncompleted = True
        while round_uncompleted:
            self.match_display.display_matchs_list_from_round(active_round, active_round.matchs)
            # RoundView(active_round).display_round_matchs()
            match_index = RoundView(active_round).round_menu()
            if int(match_index) == 0:
                self.tournament_controller(tournament)
            else:
                MatchController.update_match_score(active_round.matchs[int(match_index)-1])
                for match in active_round.matchs:
                    if match.player1_score is not None or match.player2_score is not None:
                        round_uncompleted = False
                    else:
                        round_uncompleted = True
                        self.play_round(tournament, active_round)
        active_round.finish = Utils.parse_date('maintenant')
        for match in active_round.matchs:
            match.player1.tournament_score += match.player1_score
            match.player2.tournament_score += match.player2_score
        Information('Round terminé!')
        self.tournament_controller(tournament)
