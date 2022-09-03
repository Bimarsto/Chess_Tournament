from datetime import datetime
from views.menus import MainMenu, RoundMenu
from views.tournament import TournamentView, TournamentMenu
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
from rich.console import Console

from models.tournament import TournamentModel, all_tournaments
from models.round import Round
from models.match import MatchModel
from models.player import PlayerModel, all_players


class MainController:

    def __init__(self):
        self.running = True

    def run(self):
        console = Console(width=100)
        console.rule("Gestionnaire de tournoi d'echec | Bienvenue")
        while self.running:
            self.mainmenu()
        Information("A bientot !")

    def mainmenu(self):
        match MainMenu().get_choice():
            case '0':  # Quitter
                self.running = False
            case '1':  # Créer un nouveau tournoi
                Information("Création d'un nouveau tournoi")
                TournamentController().create_new_tournament()
                new_tournament = all_tournaments[-1]
                self.new_tournament_controller(new_tournament)
            case '2':  # Accéder à un tournoi
                pass
            case '3':  # Ajouter un nouveau joueur
                pass
            case '4':  # Modifier un joueur
                pass
            case '5':  # Rapports
                pass

    def new_tournament_controller(self, new_tournament):
        match TournamentMenu(new_tournament).tournament_creation_menu():
            case '0':  # Retour au menu principal
                self.mainmenu()
            case '1':  # Ajouter un joueur
                if len(new_tournament.tournament_players) < new_tournament.number_of_players:
                    self.add_tournament_player(new_tournament)
                else:
                    Error('Le nombre de joueurs au tournoi est atteint. Vous ne pouvez plus ajouter de joueurs.')
                    self.new_tournament_controller(new_tournament)
            case '2':  # Démarreer le prochain round
                active_round = TournamentController.create_next_round(new_tournament)
                if active_round is None:
                    self.new_tournament_controller(new_tournament)
                else:
                    self.play_round(new_tournament,active_round)

    def add_tournament_player(self, tournament):
        match TournamentMenu(tournament).add_player():
            case '0':  # Retour au menu du tournoi
                TournamentMenu(tournament).tournament_creation_menu()
            case '1':  # Joueur existant
                available_players = []
                for player in all_players:
                    if player not in tournament.tournament_players:
                        available_players.append(player)
                if len(available_players) > 0:
                    PlayerDisplay.display_players_list(available_players)
                    player = PlayerMenu().select_player(available_players)
                    TournamentController.add_player(tournament, player)
                else:
                    Error("Aucun joueur existant disponnible.")
                    self.add_tournament_player(tournament)
            case '2':  # Nouveau joueur
                player = PlayerController().create_new_player()
                TournamentController.add_player(tournament, player)
                self.new_tournament_controller(tournament)

    def play_round(self, tournament, active_round):
        round_uncompleted = True
        while round_uncompleted:
            RoundView(active_round).display_round_matchs()
            match_index = RoundView(active_round).round_menu()
            if int(match_index) == 0:
                self.new_tournament_controller(tournament)
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
        self.new_tournament_controller(tournament)

    # def main_menu(self):
    #     menu_selection = MainMenu.main_menu()
    #     if menu_selection == "1":
    #         # Créer un nouveau tournoi
    #         print("\nCreation d'un nouveau tournoi :")
    #         tournament_information = TournamentView()
    #         new_tournament = Tournament(tournament_information.name,
    #                                     tournament_information.location,
    #                                     tournament_information.start_date,
    #                                     tournament_information.end_date,
    #                                     tournament_information.time_control,
    #                                     tournament_information.description,
    #                                     tournament_information.number_of_rounds,
    #                                     tournament_information.max_players
    #                                     )
    #         Information("Vous avez créer " + new_tournament.__str__())
    #         self.tournament(new_tournament)
    #     elif menu_selection == "0":
    #         # Quitter
    #         return
    #
    # def tournament(self, active_tournament):
    #     menu_selection = TournamentMenu(active_tournament).tournament_creation_menu()
    #     if menu_selection == "0":
    #         self.main_menu()
    #     elif menu_selection == "1":
    #         # Ajouter un joueur au tournoi
    #         if len(active_tournament.tournament_players) < active_tournament.max_players:
    #             player_information = PlayerView()
    #             new_player = Player(player_information.last_name,
    #                                 player_information.first_name,
    #                                 player_information.birth_date,
    #                                 player_information.sex,
    #                                 player_information.rank
    #                                 )
    #             active_tournament.add_player(new_player)
    #             Information(f"{new_player.first_name} {new_player.last_name} "
    #                         f"a été ajouter au tournoi {active_tournament.name}")
    #             self.tournament(active_tournament)
    #         else:
    #             Error('Le tournoi est complet, vous ne pouvez pas ajouter de nouveaux joueur.')
    #             self.tournament(active_tournament)
    #     elif menu_selection == "2":
    #         # Démarrer le tournoi
    #         if len(active_tournament.tournament_players) == active_tournament.max_players:
    #             Information(f"Round n° {len(active_tournament.tournament_rounds) + 1}")
    #             if len(active_tournament.tournament_rounds) < active_tournament.number_of_rounds:
    #                 active_tournament.create_rounds()
    #                 self.round(active_tournament, active_tournament.tournament_rounds[-1])
    #             else:
    #                 Error('Tous les rounds de ce tournoi ont été générés.')
    #                 self.tournament(active_tournament)
    #         else:
    #             Error('Tous les participants ne sont pas inscrits. Vous ne pouvez pas lancer le tournoi')
    #             self.tournament(active_tournament)
    #
    # def round(self, active_tournament, active_round):
    #     active_round.start = datetime.now()
    #     RoundView(active_round).display_round_matchs()
    #     match_index = RoundMenu(active_round).round_menu()
    #     if match_index == -1:
    #         # Retour au menu du tournoi
    #         self.tournament(active_tournament)
    #     else:
    #         # Saisir le résultat du match séléctionné
    #         active_match = active_round.matchs[match_index]
    #         match_result = MatchView(active_match).get_result()
    #         active_round.matchs[match_index].ranking(match_result)
    #         self.tournament(active_tournament)