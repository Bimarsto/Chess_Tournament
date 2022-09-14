

class PlayerModel:
    """Player."""
    all_players = []

    def __init__(self, last_name, first_name, birth_date, sex, rank=0):
        """Has a last name, a first name, a date of birth,
        a gender and a ranking place."""
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sex = sex
        self.rank = rank
        self.tournament_score = 0
        self.id = len(self.all_players) + 1

        self.all_players.append(self)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"'last_name': {self.last_name}, " \
               f"'first_name': {self.first_name}, " \
               f"'birth_date': {self.birth_date}, " \
               f"'sex': {self.sex}, " \
               f"'rank': {self.rank}, " \
               f"'tournament_score': {self.tournament_score}"

    def serialize(self):
        return {'last_name': self.last_name,
                'first_name': self.first_name,
                'birth_date': self.birth_date,
                'sex': self.sex,
                'rank': self.rank,
                'tournament_score': self.tournament_score,
                'id': self.id}

    @staticmethod
    def deserialize(serialized_player):
        last_name = serialized_player['last_name']
        first_name = serialized_player['first_name']
        birth_date = serialized_player['birth_date']
        sex = serialized_player['sex']
        rank = serialized_player['rank']
        tournament_score = serialized_player['tournament_score']
        id = serialized_player['id']
        deserialized_player = PlayerModel(last_name, first_name, birth_date, sex, rank)
        deserialized_player.tournament_score = tournament_score
        deserialized_player.id = id
        return deserialized_player
