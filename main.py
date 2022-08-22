"""Entry point."""

from models.player import Player


from controllers.main_controller import MainController


from views.base import ConsolView
from views.player import PlayerView

def main():

    views = [ConsolView(), PlayerView()]

    controllers = [MainController]

    application = MainController(views, controllers)
    application.run()

if __name__ == "__main__":
    main()