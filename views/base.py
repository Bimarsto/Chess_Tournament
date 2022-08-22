"""Base view."""


class ConsolView:
    """Consol view."""


    def main_menu(self):
        choise = input("Entrez votre choix : \n"
                       "0 Quitter \n"
                       "1 Ajouter un nouveau joueur \n")
        return choise
