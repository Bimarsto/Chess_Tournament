from models.match import Match


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
            self.matchs.append(Match(upper_half_group[i], lower_half_group[i]))
            print(Match(upper_half_group[i], lower_half_group[i]))

    def create_player_pairs(self):
        pass
