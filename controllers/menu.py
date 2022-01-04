from views.menu import MenuView, PlayerView, TournamentView


class MenuController:
    def run(self):
        menu_view = MenuView()
        started = menu_view.run()
        print(f"{started=}")
        if started == "1":
            player_view = PlayerView()
            player_view.run()

        if started == "9":
            tournament_view = TournamentView()
            tournament_view.run()


if __name__ == "__main__":
    menu_controller = MenuController()
    menu_controller.run()
