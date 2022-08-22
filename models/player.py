class Player:
    """Player."""

    def __init__(self, last_name, first_name, birth_date, gender, rank):
        """Has a last name, a first name, a date of birth, a gender and a ranking place."""
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank

    def __str__(self):
        return f"{self.first_name} {self.last_name} né(e) le {self.birth_date} est classé(e) {self.rank}"
