from datetime import datetime
from views.menus import MainMenu, RoundMenu
from views.tournament import TournamentView, TournamentMenu, TournamentDisplay
from views.round import RoundView
from views.match import MatchView
from views.player import PlayerView, PlayerMenu, PlayerDisplay
from views.messages import Error, Information
from views.menus import MainMenu
from controllers.tournament import TournamentController
from controllers.round import RoundController
from controllers.match import MatchController
from controllers.player import PlayerController
from controllers.utils import Utils
from models.tournament import TournamentModel
from models.round import Round
from models.match import MatchModel
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

    def run(self):
        console = Console(width=100)
        console.rule("Gestionnaire de tournoi d'echec | Bienvenue")
        while self.running:
            self.main_menu_controller()
        Information("A bientot !")

    def main_menu_controller(self):
        self.player.load_all_players()
        # self.tournament.load_tournaments()
        match self.mainmenu.get_choice():
            case '9':  # Quitter
                self.running = False
            case '1':  # Créer un nouveau tournoi
                Information("Création d'un nouveau tournoi")
                self.tournament.create_new_tournament(self.tournament_information.creation())
                new_tournament = self.tournament.model.all_tournaments[-1]
                self.tournament_controller(new_tournament)
            case '2':  # Accéder à un tournoi
                if len(self.tournament.model.all_tournaments) > 0:
                    TournamentDisplay().display_tournament_list(self.tournament.model.all_tournaments)
                    selected_tournament = TournamentMenu.select_tournament(self.tournament.model.all_tournaments)
                    self.tournament_controller(selected_tournament)
                else:
                    Error("Aucun tournoi accessible.")
            case '3':  # Ajouter un nouveau joueur
                self.player.create_new_player()
            case '4':  # Modifier un joueur
                self.player.modify_player()
            case '5':  # Rapports
                pass

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
                active_round = self.tournament.create_next_round(tournament)
                if active_round is None:
                    self.tournament_controller(tournament)
                else:
                    self.play_round(tournament,active_round)

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
                    PlayerDisplay.display_players_list(available_players)
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

    def play_round(self, tournament, active_round):
        round_uncompleted = True
        while round_uncompleted:
            RoundView(active_round).display_round_matchs()
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
