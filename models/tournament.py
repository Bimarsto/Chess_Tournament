TIME_CONTROL=("bullet", "blitz", "coup rapide")


class Tournament:
    """Tournament"""

    def __init__(self, name, location, date, duration, number_of_rounds, rounds, players, time_control, description):
        self.name = name
        self.location = location
        self.date = date
        self.duration = duration
        self.number_of_rounds = number_of_rounds
        self.rounds = rounds
        self.players = players
        self.time_control = time_control
        self.description = description