from tinydb import Query, TinyDB


class PlayerModel:
    """Player."""
    all_players = []

    def __init__(self, last_name, first_name, birth_date, sex, rank=0, tournament_score=0, played_against=None):
        """Has a last name, a first name, a date of birth,
        a gender and a ranking place."""
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sex = sex
        self.rank = rank
        self.tournament_score = tournament_score
        self.id = len(self.all_players)+1

        if played_against is None:
            self.played_against = []
        else:
            self.played_against = played_against

        self.all_players.append(self)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"'last_name': {self.last_name}, " \
               f"'first_name': {self.first_name}, " \
               f"'birth_date': {self.birth_date}, " \
               f"'sex': {self.sex}, " \
               f"'rank': {self.rank}, " \
               f"'tournament_score': {self.tournament_score}, " \
               f"'played_against': {self.played_against}"

    def serialize(self):
        return vars(self)

    @staticmethod
    def deserialize(serialized_player):
        PlayerModel(**serialized_player)
