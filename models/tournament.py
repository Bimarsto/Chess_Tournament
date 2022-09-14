from models.round import RoundModel
from models.player import PlayerModel


class TournamentModel:
    """Tournament"""
    all_tournaments = []

    def __init__(self, name, location, start_date, end_date, time_control, description,
                 number_of_rounds=4, number_of_players=8):

        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.time_control = time_control
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.number_of_players = number_of_players
        self.tournament_rounds = []
        self.tournament_players = []

        self.all_tournaments.append(self)

    def __str__(self):
        return f"tournoi {self.name} (du {self.start_date} au {self.end_date} à {self.location}) \n" \
               f"{self.tournament_players}"

    def __repr__(self):
        return f"'name': {self.name}, " \
               f"'location': {self.location}, " \
               f"'start_date': {self.start_date}, " \
               f"'end_date': {self.end_date}, " \
               f"'time_control': {self.time_control}, " \
               f"'description': {self.description}, " \
               f"'number_of_rounds': {self.number_of_rounds}, " \
               f"'number_of_players': {self.number_of_players}, " \
               f"'tournament_rounds': {self.tournament_rounds}, " \
               f"'tournament_players': {self.tournament_players}"

    def add_player(self, player):
        self.tournament_players.append(player)

    def create_rounds(self):
        self.tournament_rounds.append(RoundModel(f"Round {len(self.tournament_rounds)+1}",
                                                 len(self.tournament_rounds)+1,
                                                 self.tournament_players
                                                 )
                                      )

    def get_tournament_ranking(self, by_score=True):
        return sorted(self.tournament_players, key=lambda x: (x.tournament_score, x.rank), reverse=True)

    def serialize(self):
        players = []
        rounds = []
        for player in self.tournament_players:
            players.append(player.id)
        for active_round in self.tournament_rounds:
            rounds.append(RoundModel.serialize(active_round))
        return {'name': self.name,
                'location': self.location,
                'start_date': self.start_date,
                'end_date': self.end_date,
                'time_control': self.time_control,
                'description': self.description,
                'number_of_rounds': self.number_of_rounds,
                'number_of_players': self.number_of_players,
                'tournament_rounds': rounds,
                'tournament_players': players}

    @staticmethod
    def deserialize(serialized_tournament):
        deserialized_tournament = TournamentModel(serialized_tournament['name'],
                                                  serialized_tournament['location'],
                                                  serialized_tournament['start_date'],
                                                  serialized_tournament['end_date'],
                                                  serialized_tournament['time_control'],
                                                  serialized_tournament['description'],
                                                  serialized_tournament['number_of_rounds'],
                                                  serialized_tournament['number_of_players']
                                                  )
        for player_id in serialized_tournament['tournament_players']:
            for player in PlayerModel.all_players:
                if player.id == player_id:
                    deserialized_tournament.tournament_players.append(player)
                    break
        for round in serialized_tournament['tournament_rounds']:
            deserialized_tournament.tournament_rounds.append(RoundModel.deserialize(round))
        return deserialized_tournament
