from models.player import PlayerModel
from models.tournament import TournamentModel
from views.menus import ReportMenu
from views.player import PlayerDisplay
from views.tournament import TournamentDisplay
from views.round import RoundDisplay
from views.match import MatchDisplay
from views.messages import Error
from controllers.tournament import TournamentController


class ReportController:

    def __init__(self):
        from controllers.main_controller import MainController
        self.player_model = PlayerModel
        self.tournament_model = TournamentModel
        self.player_display = PlayerDisplay()
        self.tournament_display = TournamentDisplay()
        self.round_display = RoundDisplay()
        self.match_display = MatchDisplay()
        self.main = MainController()
        self.tournament = TournamentController()
        self.report = ReportMenu()

    def all_players_by_alphabetical_order(self):
        if len(self.player_model.all_players) > 0:
            self.player_display.report(self.player_model.all_players, 'ordre alphabétique')
            input('Appuyer sur "Entrée" pour revenir au menu')
            self.main.reports_controller(self.report.get_report_type())
        else:
            Error("Aucun joueur accessible.")

    def all_players_by_rank_order(self):
        if len(self.player_model.all_players) > 0:
            self.player_display.report(self.player_model.all_players, 'classement')
            input('Appuyer sur "Entrée" pour revenir au menu')
            self.main.reports_controller(self.report.get_report_type())
        else:
            Error("Aucun joueur accessible.")

    def all_tournaments(self):
        if len(self.tournament_model.all_tournaments) > 0:
            self.tournament_display.display_tournaments_list(self.tournament_model.all_tournaments)
            input('Appuyer sur "Entrée" pour revenir au menu')
            self.main.reports_controller(self.report.get_report_type())
        else:
            Error("Aucun tournoi accessible.")

    def players_by_alphabetical_order_for_a_tournament(self):
        if len(self.tournament_model.all_tournaments) > 0:
            self.tournament_display.display_tournaments_list(self.tournament_model.all_tournaments)
            tournament = self.tournament.menu.select_tournament(self.tournament_model.all_tournaments)
            if len(tournament.tournament_players) > 0:
                self.player_display.report(tournament.tournament_players, 'ordre alphabétique')
                input('Appuyer sur "Entrée" pour revenir au menu')
            else:
                Error("Aucun joueur inscrit pour ce tournoi.")
            self.main.reports_controller(self.report.get_report_type())
        else:
            Error("Aucun tournoi accessible.")

    def players_by_rank_order_for_a_tournament(self):
        if len(self.tournament.model.all_tournaments) > 0:
            self.tournament_display.display_tournaments_list(self.tournament.model.all_tournaments)
            tournament = self.tournament.menu.select_tournament(self.tournament.model.all_tournaments)
            if len(tournament.tournament_players) > 0:
                self.player_display.report(tournament.tournament_players, 'classement')
                input('Appuyer sur "Entrée" pour revenir au menu')
            else:
                Error("Aucun joueur inscrit pour ce tournoi.")
            self.main.reports_controller(self.report.get_report_type())
        else:
            Error("Aucun tournoi accessible.")

    def rounds_for_a_tournament(self):
        if len(self.tournament.model.all_tournaments) > 0:
            self.tournament_display.display_tournaments_list(self.tournament.model.all_tournaments)
            tournament = self.tournament.menu.select_tournament(self.tournament.model.all_tournaments)
            if len(tournament.tournament_rounds) > 0:
                self.round_display.display_rounds_list(tournament)
                input('Appuyer sur "Entrée" pour revenir au menu')
            else:
                Error("Aucun round n'est créé pour ce tournoi.")
            self.main.reports_controller(self.report.get_report_type())
        else:
            Error("Aucun tournoi accessible.")

    def matchs_for_a_tournament(self):
        if len(self.tournament.model.all_tournaments) > 0:
            self.tournament_display.display_tournaments_list(self.tournament.model.all_tournaments)
            tournament = self.tournament.menu.select_tournament(self.tournament.model.all_tournaments)
            if len(tournament.tournament_rounds) > 0:
                self.match_display.display_matchs_list_from_tournament(tournament)
                input('Appuyer sur "Entrée" pour revenir au menu')
            else:
                Error("Aucun round n'est créé pour ce tournoi.")
            self.main.reports_controller(self.report.get_report_type())
        else:
            Error("Aucun tournoi accessible.")
