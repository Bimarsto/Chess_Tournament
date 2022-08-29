# from data_storage import save_players

class Player:
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

        self.all_players.append(self)

    def __str__(self):
        return f"{self.first_name} {self.last_name} " \
               f"né(e) le {self.birth_date} est classé(e) {self.rank}"