"""Base view for player."""
from rich.console import Console
from rich.table import Table
from views.messages import Error
from controllers.utils import Utils


class PlayerView:
    """Player view."""

    def __init__(self):
        self.last_name = self.get_information('Quel est le nom de famille du joueur?',
                                              'Champs obligatoire! Merci de le renseigner.')
        self.first_name = self.get_information('Quel est le prénom du joueur?',
                                               'Champs obligatoire! Merci de le renseigner.')
        self.birth_date = self.get_player_birth_date()
        self.sex = self.get_player_sex()
        self.rank = self.get_rank('Quel est le classement du joueur? (0 par défaut)')

    def get_player_birth_date(self):
        birth_date = self.get_information("Quel est la date d'anniversaire du joueur?",
                                          "Champs obligatoire! Merci de le renseigner.")
        parsed_birth_date = Utils.parse_date(birth_date)
        if parsed_birth_date is None:
            self.get_player_birth_date()
        else:
            return parsed_birth_date

    @staticmethod
    def get_information(message, error_message):
        answer = ''
        valid_answer = False
        while answer == '' and not valid_answer:
            answer = input(message + '\n')
            if answer == '':
                valid_answer = False
                Error(error_message)
            else:
                valid_answer = True
        return answer

    @staticmethod
    def get_player_sex():
        sex = ''
        while sex == '':
            sex = input('Sélectionnez le sexe du joueur: \n'
                        '1 : Homme \n'
                        '2 : Femme \n')
            match sex:
                case '1':
                    sex = 'Homme'
                case '2':
                    sex = 'Femme'
                case _:
                    Error('Champs obligatoire! Merci de le renseigner.')
                    sex = ''
        return sex

    @staticmethod
    def get_rank(message, default_value=0):
        rank = ''
        valid_value = False
        while not valid_value:
            rank = input(message + '\n')
            if rank == '':
                rank = default_value
            if not str(rank).isdigit():
                Error("La valeur saisie doit être un nombre entier positif.")
            else:
                valid_value = True
        return int(rank)


class PlayerMenu:

    @staticmethod
    def modification_display():
        field = ['', '']
        while field[0] == '':
            field[0] = input('Quel information souhaitez-vous modifier? \n'
                             '1 : Nom de famille \n'
                             '2 : Prénom \n'
                             '3 : Date de naissance \n'
                             '4 : Sexe \n'
                             '5 : Classement \n')
            match field[0]:
                case '1':
                    field[0] = 'last_name'
                    field[1] = PlayerView().get_information('Quel est le nom de famille du joueur?',
                                                            'Champs obligatoire! Merci de le renseigner.')
                case '2':
                    field[0] = 'first_name'
                    field[1] = PlayerView().get_information('Quel est le prénom du joueur?',
                                                            'Champs obligatoire! Merci de le renseigner.')
                case '3':
                    field[0] = 'birth_date'
                    field[1] = PlayerView().get_player_birth_date()
                case '4':
                    field[0] = 'sex'
                    field[1] = PlayerView().get_player_sex()
                case '5':
                    field[0] = 'rank'
                    field[1] = PlayerView().get_rank('Quel est le classement du joueur? (0 par défaut)')
                case _:
                    Error('Merci de sélectioner une information à modifier dans la liste.')
            return field

    @staticmethod
    def select_player(all_players):
        selection = ''
        valid_value = False
        while not valid_value:
            selection = input("Entrez l'id du joueur désiré: (liste des joueurs ci-dessus)")
            if selection == '':
                Error('Champs obligatoire! Merci de le renseigner.')
            if not str(selection).isdigit():
                Error("L'id du joueur doit être un entier positif.")
            elif int(selection) > len(all_players) - 1:
                Error("La valeur saisie n'est pas dans la liste de joueurs.")
            else:
                valid_value = True
        return all_players[int(selection)]


class PlayerDisplay:

    @staticmethod
    def display_players_list(player_list):
        console = Console()
        player_table = Table(title="Liste de l'ensemble des joueurs", title_style='bold blue')
        player_table.add_column('ID')
        player_table.add_column('Nom')
        player_table.add_column('Prénom')
        player_table.add_column('Date de naissance')
        player_table.add_column('Sexe')
        player_table.add_column('Classement')
        for player in player_list:
            player_table.add_row(f"{player_list.index(player)}",
                                 f"{player.last_name}",
                                 f"{player.first_name}",
                                 f"{player.birth_date}",
                                 f"{player.sex}",
                                 f"{player.rank}"
                                 )
        console.print(player_table)
