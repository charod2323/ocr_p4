from views.MenuViews import MenuView, PlayerView, TournamentView


class MenuController:
    def run(self):
        players = []
        while True:
            menu_view = MenuView()
            started = menu_view.run()

            if started == "1":
                print(" 8 players by default")
                for i in range(8):
                    print()
                    print()
                    print()
                    print("...........................................PLAYER NUMBER ......", i + 1)
                    print()
                    player_view = PlayerView()
                    # Create a new player
                    player = player_view.create_new_player()
                    # Add new player to list containing all players

                    ranking = player_view.verification_rank()
                    player['ranking'] = ranking
                    players.append(player)
                print()
                count = 0
                # afficher le contenu players ligne par ligne
                for i in players:
                    count = count + 1
                    print("player", count, i)

            if started == "4":
                ref_tournament = []
                tournament_view = TournamentView()
                ref = tournament_view.reference_tournament(players)
                ref_tournament.append(ref_tournament)
                players = tournament_view.run(players)
                tournament_view.split_list(players)
                tournament_view.players_face_to_face(players)

            if started == "7":
                return
