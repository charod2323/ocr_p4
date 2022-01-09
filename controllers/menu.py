from views.menu import MenuView, PlayerView, TournamentView


class MenuController:
    def run(self):
        players = []
        while True:
            menu_view = MenuView()
            started = menu_view.run()
            print(f"{started=}")
            if started == "1":
                player_view = PlayerView()
                players = player_view.run()
            if started == "4":
                tournament_view = TournamentView()
                tournament_view.run(players)
            if started == "q":
                return
