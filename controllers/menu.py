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
                # Create a new player
                player = player_view.create_new_player()
                # Add new player to list containing all players
                players.append(player)
                ranking = player_view.verification_rank()
                player_view.display_listing(players)


"""
            if players and started == "4":
                tournament_view = TournamentView()
                tournament_view.run(players)
            if started == "7":
                return
"""