from views.menu import MenuView, PlayerView


class MenuController:
    def run(self):
        menu_view = MenuView()
        choice = menu_view.run()
        print(f"{choice=}")
        if choice =="1":
            player_view = PlayerView()
            player_view.run()


if __name__ == "__main__":
    menu_controller = MenuController()
    menu_controller.run()
