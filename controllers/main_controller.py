class MainController:

    def __init__(self, view, controllers):
        self.view = view[0]
        self.controller = controllers[0]

    def run(self):
        running = True
        while running:
            choise = self.view.main_menu()
            if choise == "1":
                self.view = view[1]
                print("Vous ajourez un joueur !")
            elif choise == "0":
                print("A bientôt !")
                running = False