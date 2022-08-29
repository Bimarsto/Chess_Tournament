from models.player import Player
from models.round import Round
from models.match import Match

all_tournaments = []

class Tournament:
    """Tournament"""

    def __init__(self, name, location, start_date, end_date, time_control, description,
                 number_of_rounds=4, max_players=8):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.time_control = time_control
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.max_players = max_players

        self.tournament_rounds = []
        self.tournament_players = []

        all_tournaments.append(self)

    def __str__(self):
        return f"Tournoi {self.name} du {self.start_date} au {self.end_date} à {self.location}"

    def add_player(self, player_index):
        if len(self.tournament_players) < self.max_players:
            player = Player.all_players[player_index]
            self.tournament_players.append(player)
        else:
            print('Le nombre de joueurs max pour ce tournoi a été atteint. '
                  'Vous ne pouvez plus ajouter de nouveau joueurs. ')
        return self.tournament_players

    def create_rounds(self):
        self.tournament_rounds.append(Round(f"Round {len(self.tournament_rounds)+1}",
                                            len(self.tournament_rounds)+1,
                                            self.tournament_players
                                            )
                                      )
        return self.tournament_rounds

    def get_tournament_ranking(self, by_score=True):
        return sorted(self.tournament_players, key=lambda x: (x.tournament_score, x.rank), reverse=True)

