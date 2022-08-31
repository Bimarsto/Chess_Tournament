from models.player import Player
# from models.tournament import Tournament

class Match:
    """Match"""

    def __init__(self, player1, player2, player1_score=None, player2_score=None):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = player1_score
        self.player2_score = player2_score
        self.match = ([self.player1,self.player1_score],[self.player2,self.player2_score])

    def __str__(self):
        return f"Match entre {self.player1.first_name} {self.player1.last_name} et {self.player2.first_name} {self.player2.last_name}"

    def ranking(self, player1_score, player2_score):
        if player1_score and player2_score:
            if player1_score > player2_score:
                player1_score += 1
            elif player1_score < player2_score:
                player2_score += 1
            else:
                player1_score += 0.5
                player2_score += 0.5

