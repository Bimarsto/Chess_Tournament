from models.match import MatchModel
from views.messages import Error


class Round:
    """Round."""

    def __init__(self, name, round_number, players):
        self.name = name
        self.start = None
        self.finish = None
        self.round_number = round_number
        self.players = players

        self.matchs = []

        if self.round_number == 1:
            self.create_first_player_pairs()
        elif self.round_number > 1:
            self.create_player_pairs()

    def create_first_player_pairs(self):
        sorted_players = sorted(self.players, key=lambda players: players.rank, reverse=True)
        upper_half_group = sorted_players[:int(len(self.players) / 2)]
        lower_half_group = sorted_players[int(len(self.players) / 2):]
        for i in range(0, len(upper_half_group)):
            self.matchs.append(MatchModel(upper_half_group[i], lower_half_group[i]))

    def create_player_pairs(self):
        sorted_players = sorted(self.players,
                                key=lambda players: (players.tournament_score, players.rank),
                                reverse=True
                                )
        i = 0
        j = 1
        while len(sorted_players) > 0:
            if i < len(sorted_players)-1:
                if j < len(sorted_players):
                    if sorted_players[i+j] not in sorted_players[i].played_against:
                        self.matchs.append(MatchModel(sorted_players[i], sorted_players[i+j]))
                        sorted_players.remove(sorted_players[i+j])
                        sorted_players.remove(sorted_players[i])
                        i = 0
                        j = 1
                    else:
                        j += 1
                else:
                    i += 1
                    j = 0
            else:
                Error('Génération des matchs impossible')

