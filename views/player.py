"""Base view for player."""


class PlayerView:
    """Player view."""

    def get_player_last_name(self):
        last_name = input("Quel est le nom de famille du joueur ? \n")
        if not last_name:
            return None
        return last_name

    def get_player_first_name(self):
        first_name = input("Quel est le prénom du joueur ? \n")
        if not first_name:
            return None
        return first_name

    def get_player_birth_date(self):
        birth_date = input("Quel est la date de naissance du joueur ? \n")
        if not birth_date:
            return None
        return birth_date

    def get_player_sex(self):
        sex = input("Sélectionnez le sexe du joueur: \n"
                    "1 : Homme \n"
                    "2 : Femme \n")
        if not sex:
            return None
        return sex

    def get_player_rank(self):
        is_ranked = input("Le joueur est-il classé ? (Y/N) \n")
        if is_ranked in ["Y", "y"]:
            rank = input("Quel est le classement du joueur ? \n")
        else:
            return None

        if not rank:
            return None
        return rank
