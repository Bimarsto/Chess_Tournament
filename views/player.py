"""Base view for player."""


class PlayerView:
    """Player view."""

    def get_player_last_name(self, player_information):
        last_name = input("Saisissez le nom de famille du joueur :")
        if not last_name:
            return None
        player_information.append(last_name)

