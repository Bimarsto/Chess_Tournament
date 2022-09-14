from models.player import PlayerModel


class MatchModel:
    """Match"""

    def __init__(self, player1, player2, player1_score=None, player2_score=None):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = player1_score
        self.player2_score = player2_score
        self.match = ([self.player1, self.player1_score], [self.player2, self.player2_score])

        # self.player1.played_against.append(self.player2.id)
        # self.player2.played_against.append(self.player1.id)

    def __str__(self):
        return f'{self.player1.first_name} {self.player1.last_name} - ' \
               f'{self.player2.first_name} {self.player2.last_name}'

    def serialize(self):
        match = ([self.player1.id, self.player1_score], [self.player2.id,self.player2_score])
        return {'player1': self.player1.id,
                'player2': self.player2.id,
                'player1_score': self.player1_score,
                'player2_score': self.player2_score,
                'match': match}

    @staticmethod
    def deserialize(serialized_match):
        player1 = serialized_match['player1']
        player2 = serialized_match['player2']
        for player in PlayerModel.all_players:
            if player.id == player1:
                player1 = player
            elif player.id == player2:
                player2 = player
        deserialized_match = MatchModel(player1,
                                        player2,
                                        serialized_match['player1_score'],
                                        serialized_match['player2_score'])
        return deserialized_match

    def results(self, match_result):
        self.player1_score = 0
        self.player2_score = 0
        if match_result == '1':
            self.player1_score += 1
        elif match_result == '2':
            self.player1_score += 0.5
            self.player2_score += 0.5
        elif match_result == '3':
            self.player2_score += 1
