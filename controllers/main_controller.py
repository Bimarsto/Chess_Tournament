from views.menus import MainMenu, TournamentMenu
from views.tournament import TournamentView
from views.player import PlayerView
from views.messages import Error, Information

from models.tournament import Tournament, all_tournaments
from models.round import Round
from models.player import Player

class MainController:


    def run(self):
        running = True
        while running:
            self.main_menu()
            running = False
            Information("A bientot !")

    def main_menu(self):
        menu_selection = MainMenu.main_menu()
        if menu_selection == "1":
            print("\nCreation d'un nouveau tournoi :")
            tournament_information = TournamentView()
            new_tournament = Tournament(tournament_information.name,
                                        tournament_information.location,
                                        tournament_information.start_date,
                                        tournament_information.end_date,
                                        tournament_information.time_control,
                                        tournament_information.description,
                                        tournament_information.number_of_rounds,
                                        tournament_information.max_players
                                        )
            Information("Vous avez créer " + new_tournament.__str__())
            self.tournament(new_tournament)
        elif menu_selection == "0":
            return


    def tournament(self, active_tournament):
        menu_selection = TournamentMenu(active_tournament).tournament_menu()
        if menu_selection == "0":
            self.main_menu()
        elif menu_selection == "1":
            if len(active_tournament.tournament_players) < active_tournament.max_players:
                player_information = PlayerView()
                new_player = Player(player_information.last_name,
                                    player_information.first_name,
                                    player_information.birth_date,
                                    player_information.sex,
                                    player_information.rank
                                    )
                active_tournament.add_player(new_player)
                Information(f"{new_player.first_name} {new_player.last_name} "
                     f"a été ajouter au tournoi {active_tournament.name}")
                self.tournament(active_tournament)
            else:
                Error('Le tournoi est complet, vous ne pouvez pas ajouter de nouveaux joueur.')
                self.tournament(active_tournament)
        elif menu_selection == "2":
            if len(active_tournament.tournament_players) == active_tournament.max_players:
                Information(f"Round n° {len(active_tournament.tournament_rounds) + 1}")
                if len(active_tournament.tournament_rounds) == 0:
                    active_tournament.create_rounds()
                    for match in active_tournament.tournament_rounds:
                        print(match.__dict__)
                elif len(active_tournament.tournament_rounds) < active_tournament.number_of_rounds:
                    pass
                else:
                    Error('Tous les rounds de ce tournoi ont été générés.')
                    self.tournament(active_tournament)
            else:
                Error('Tous les participants ne sont pas inscrits. Vous ne pouvez pas lancer le tournoi')
                self.tournament(active_tournament)
