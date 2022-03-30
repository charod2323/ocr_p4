from controllers.menu import MenuController
from models.players import Player


if __name__ == "__main__":
    # menu_controller = MenuController()
    # menu_controller.run()
    p = Player.get_player_by_lastname("l1")
    print(p)
