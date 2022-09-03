from views.player import PlayerView, PlayerMenu, PlayerDisplay
from models.player import PlayerModel, all_players


class PlayerController:

    @staticmethod
    def create_new_player():
        new_player = PlayerView()
        return PlayerModel(new_player.last_name,
                           new_player.first_name,
                           new_player.birth_date,
                           new_player.sex,
                           new_player.rank)

    @staticmethod
    def modify_player():
        PlayerDisplay().display_players_list(all_players)
        player = PlayerMenu().select_player(all_players)
        field = PlayerMenu().modification_display()
        setattr(player, field[0], field[1])

