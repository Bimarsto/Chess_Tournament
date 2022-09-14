from models.match import MatchModel
from models.player import PlayerModel
from views.messages import Error


class RoundModel:
    """Round."""

    def __init__(self, name, round_number, players):
        self.name = name
        self.start = None
        self.finish = None
        self.round_number = round_number
        self.players = players

        self.matchs = []

    def __str__(self):
        return f"{self.name}"

    def serialize(self):
        players = []
        matchs = []
        for player in self.players:
            players.append(player.id)
        for match in self.matchs:
            matchs.append(MatchModel.serialize(match))
        return {'name': self.name,
                'start': self.start,
                'finish': self.finish,
                'round_number': self.round_number,
                'players': players,
                'matchs': matchs}

    @staticmethod
    def deserialize(serialized_round):
        players_id = serialized_round['players']
        for player_id in players_id:
            for player in PlayerModel.all_players:
                if player.id == player_id:
                    players_id[player_id-1] = player
                    break
        deserialized_round = RoundModel(serialized_round['name'],
                                        serialized_round['round_number'],
                                        players_id
                                        )
        deserialized_round.start = serialized_round['start']
        deserialized_round.finish = serialized_round['finish']
        for match in serialized_round['matchs']:
            deserialized_round.matchs.append(MatchModel.deserialize(match))
        return deserialized_round

    def create_players_pairs(self, tournament):
        if self.round_number == 1:
            self.create_first_player_pairs()
        elif self.round_number > 1:
            self.create_player_pairs(tournament)

    def create_first_player_pairs(self):
        sorted_players = sorted(self.players, key=lambda players: players.rank, reverse=True)
        upper_half_group = sorted_players[:int(len(self.players) / 2)]
        lower_half_group = sorted_players[int(len(self.players) / 2):]
        for i in range(0, len(upper_half_group)):
            self.matchs.append(MatchModel(upper_half_group[i], lower_half_group[i]))

    def create_player_pairs(self, tournament):
        sorted_players = sorted(self.players,
                                key=lambda players: (players.tournament_score, players.rank),
                                reverse=True
                                )
        i = 0
        j = 1
        while len(sorted_players) > 0:
            if i < len(sorted_players)-1:
                if j < len(sorted_players):
                    played_against = []
                    if sorted_players[i+j] not in played_against:
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
