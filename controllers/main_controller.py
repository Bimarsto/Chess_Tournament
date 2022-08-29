from views.menus import MainMenu
from views.tournament import TournamentView

from models.tournament import Tournament

class MainController:


    def run(self):
        running = True
        while running:
            choise = MainMenu.main_menu()
            if choise == "1":
                print("Creation d'un nouveau tournoi : \n")
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
                print(new_tournament.__str__())
            elif choise == "0":
                print("A bientot !")
                running = False