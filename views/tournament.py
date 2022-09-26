"""View for tournament"""
from rich.console import Console
from rich.table import Table, box
from views.messages import Error, Information
from controllers.utils import Utils


class TournamentView:
    """Tournament view"""

    def creation(self):
        return {'name': self.get_information('Quel est le nom du tournoi?',
                                             'Champs obligatoire! Merci de le renseigner.').lower(),
                'location': self.get_information('Indiquez le lieu ou se déroule le tournoi?',
                                                 'Champs obligatoire! Merci de le renseigner.').capitalize(),
                'start_date': self.get_tournament_date('Quel est la date de début du tournoi?',
                                                       'Champs obligatoire! Merci de le renseigner.'),
                'end_date': self.get_tournament_date('Quel est la date de fin du tournoi?',
                                                     'Champs obligatoire! Merci de le renseigner.'),
                'time_control': self.get_tournament_time_control(),
                'description': self.get_information('Ajoutez une description du tournoi',
                                                    'Champs obligatoire! Merci de le renseigner.').lower(),
                'number_of_rounds': self.get_value("Quel est le nombre de rounds pour ce tournoi? (4 par défaut)",
                                                   1, 4),
                'number_of_players': self.get_value("Quel est le nombre de joueurs pour ce tournoi? (8 par défaut)",
                                                    2, 8)
                }

    def get_tournament_date(self, message, error_message):
        date = self.get_information(message, error_message)
        parsed_date = Utils.parse_date(date)
        if parsed_date is None:
            self.get_tournament_date(message, error_message)
        else:
            return parsed_date

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
    def get_tournament_time_control():
        tournament_time_control = ''
        while tournament_time_control == '':
            tournament_time_control = input('Sélectionnez le contrôle de temps du tournoi: \n'
                                            '1 : Bullet \n'
                                            '2 : Blitz \n'
                                            '3 : Coup rapide \n')
            match tournament_time_control:
                case '1':
                    tournament_time_control = 'Bullet'
                case '2':
                    tournament_time_control = 'Blitz'
                case '3':
                    tournament_time_control = 'Coup rapide'
                case _:
                    Error('Champs obligatoire! Merci de le renseigner.')
                    tournament_time_control = ''
        return tournament_time_control

    @staticmethod
    def get_value(message, min_value, default_value=0):
        value = ''
        valid_value = False
        while not valid_value:
            value = input(message + '\n')
            if value == '':
                value = default_value
            if not str(value).isdigit():
                Error("La valeur saisie doit être un nombre entier positif.")
            elif int(value) < min_value:
                Error(f"La valeur saisie doit être supérieure ou égale à {min_value}.")
            else:
                valid_value = True
        return int(value)


class TournamentMenu:

    def __init__(self, tournament):
        self.tournament = tournament

    def tournament_creation_menu(self):
        choice = ''
        Information(f"Menu du tournoi {self.tournament.name} | {len(self.tournament.tournament_players)}/"
                    f"{self.tournament.number_of_players} joueur(s) inscrit(s) | "
                    f"{len(self.tournament.tournament_rounds)}/{self.tournament.number_of_rounds} rounds joués")
        while choice == '':
            choice = input('Entrez votre choix : \n'
                           '1 : Modifier le tournoi \n'
                           '2 : Ajouter un joueur \n'
                           '3 : Démarrer le prochain round \n'
                           '4 : Afficher le classement \n'
                           '9 : Retour au menu principal \n')
            if choice not in ['9', '1', '2', '3', '4']:
                Error('Veuillez entrer le n° de votre choix dans le menu.')
                choice = ''
        return choice

    @staticmethod
    def add_player():
        choice = ''
        while choice == '':
            choice = input('Entrez votre choix : \n'
                           '1 : Joueur existant \n'
                           '2 : Nouveau joueur \n'
                           '9 : Retour au menu du tournoi \n')
            if choice not in ['9', '1', '2']:
                Error('Veuillez entrer le n° de votre choix dans le menu.')
                choice = ''
        return choice

    @staticmethod
    def modification_display():
        field = ['', '']
        while field[0] == '':
            field[0] = input('Quel information souhaitez-vous modifier? \n'
                             '1 : Nom du tournoi \n'
                             '2 : Lieu \n'
                             '3 : Date de début \n'
                             '4 : Date de fin \n'
                             '5 : Contrôle de temps \n'
                             '6 : Nombre de rounds \n'
                             '7 : Nombre de joueurs \n'
                             '8 : Description\n')
            match field[0]:
                case '1':
                    field[0] = 'name'
                    field[1] = TournamentView().get_information('Quel est le nom du tournoi?',
                                                                'Champs obligatoire! Merci de le renseigner.')
                case '2':
                    field[0] = 'location'
                    field[1] = TournamentView().get_information('Indiquez le lieu ou se déroule le tournoi?',
                                                                'Champs obligatoire! Merci de le renseigner.')
                case '3':
                    field[0] = 'start_date'
                    field[1] = TournamentView().get_tournament_date('Quel est la date de début du tournoi?',
                                                                    'Champs obligatoire! Merci de le renseigner.')
                case '4':
                    field[0] = 'end_date'
                    field[1] = TournamentView().get_tournament_date('Quel est la date de fin du tournoi?',
                                                                    'Champs obligatoire! Merci de le renseigner.')
                case '5':
                    field[0] = 'time_control'
                    field[1] = TournamentView().get_tournament_time_control()
                case '6':
                    field[0] = 'number_of_rounds'
                    field[1] = TournamentView().get_value("Quel est le nombre de rounds pour ce tournoi? "
                                                          "(4 par défaut)", 1, 4)
                case '7':
                    field[0] = 'number_of_players'
                    field[1] = TournamentView().get_value("Quel est le nombre de joueurs pour ce tournoi? "
                                                          "(8 par défaut)", 2, 8)
                case '8':
                    field[0] = 'description'
                    field[1] = TournamentView().get_information('Ajoutez une description du tournoi',
                                                                'Champs obligatoire! Merci de le renseigner.')
                case _:
                    Error('Merci de sélectionner une information à modifier dans la liste.')
            return field

    @staticmethod
    def select_tournament(all_tournaments):
        selection = ''
        valid_value = False
        while not valid_value:
            selection = input("Entrez l'id du tournoi désiré: (liste des tournois ci-dessus)\n")
            if selection == '':
                Error('Champs obligatoire! Merci de le renseigner.')
            if not str(selection).isdigit():
                Error("L'id du tournoi doit être un entier positif.")
            elif int(selection) > len(all_tournaments) - 1:
                Error("La valeur saisie n'est pas dans la liste de tournois.")
            else:
                valid_value = True
        return all_tournaments[int(selection)]


class TournamentDisplay:

    @staticmethod
    def display_tournaments_list(tournaments_list):
        console = Console(width=200)
        tournament_table = Table(title="Liste des tournois", title_style='bold blue')
        tournament_table.add_column('ID', justify='center')
        tournament_table.add_column('Nom', justify='center')
        tournament_table.add_column('Lieu', justify='center')
        tournament_table.add_column('Date de début', justify='center')
        tournament_table.add_column('Date de fin', justify='center')
        tournament_table.add_column('Contrôle de temps', justify='center')
        tournament_table.add_column('Nombre de rounds', justify='center')
        tournament_table.add_column('Nombre de joueurs', justify='center')
        tournament_table.add_column('Description', justify='center')
        for tournament in tournaments_list:
            tournament_table.add_row(f"{tournaments_list.index(tournament)}",
                                     f"{tournament.name}",
                                     f"{tournament.location}",
                                     f"{tournament.start_date}",
                                     f"{tournament.end_date}",
                                     f"{tournament.time_control}",
                                     f"{tournament.number_of_rounds}",
                                     f"{tournament.number_of_players}",
                                     f"{tournament.description}"
                                     )
        console.print(tournament_table)

    def tournament_classification(self, tournament):
        sorted_players = self.generate_classification(tournament)
        console = Console(width=200)
        classification = Table(title='Classement du tournoi',
                               title_style='bold yellow',
                               box=box.DOUBLE_EDGE,
                               border_style="blue"
                               )
        classification.add_column('Class.', justify='center')
        classification.add_column('Nom', justify='center', min_width=50)
        classification.add_column('Points', justify='center')
        classification.add_column('Ranking', justify='center')
        for player in sorted_players:
            if isinstance(player[1], float) and player[1].is_integer():
                score = int(player[1])
            else:
                score = player[1]
            classification.add_row(f"{sorted_players.index(player)+1}",
                                   f"{player[0].first_name} {player[0].last_name}",
                                   f"{score}",
                                   f"{player[0].rank}"
                                   )
        console.print(classification)

    @staticmethod
    def generate_classification(tournament):
        players_list = []
        for player in tournament.tournament_players:
            players_list.append([player, 0])
        for round in tournament.tournament_rounds:
            for match in round.matchs:
                for player in players_list:
                    if match.player1 == player[0]:
                        player[1] += match.player1_score
                    if match.player2 == player[0]:
                        player[1] += match.player2_score
        sorted_players = sorted(players_list,
                                key=lambda players: (players[1], players[0].rank),
                                reverse=True
                                )
        return sorted_players
