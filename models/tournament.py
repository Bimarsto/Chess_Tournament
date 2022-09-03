from models.round import Round

all_tournaments = []


class TournamentModel:
    """Tournament"""

    def __init__(self, name, location, start_date, end_date, time_control, description,
                 number_of_rounds=4, number_of_players=8):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.time_control = time_control
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.number_of_players = number_of_players

        self.tournament_rounds = []
        self.tournament_players = []

        all_tournaments.append(self)

    def __str__(self):
        return f"le tournoi {self.name} (du {self.start_date} au {self.end_date} à {self.location}) \n"

    def add_player(self, player):
        self.tournament_players.append(player)

    def create_rounds(self):
        self.tournament_rounds.append(Round(f"Round {len(self.tournament_rounds)+1}",
                                            len(self.tournament_rounds)+1,
                                            self.tournament_players
                                            )
                                      )

    def get_tournament_ranking(self, by_score=True):
        return sorted(self.tournament_players, key=lambda x: (x.tournament_score, x.rank), reverse=True)

