from views.MenuViews import MenuView, PlayerView


class MenuController:
    def run(self):
        players = []
        while True:
            menu_view = MenuView()
            started = menu_view.run()
            print(f"{started=}")
            if started == "1":
                player_view = PlayerView()
                listings = player_view.create_new_player()
                print(listings)
                ranking = player_view.verification_rank()
                player_view.display_listing()


"""
            if players and started == "4":
                tournament_view = TournamentView()
                tournament_view.run(players)
            if started == "7":
                return
"""