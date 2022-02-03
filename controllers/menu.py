from views.menu import MenuView, PlayerView, TournamentView, ReportView


class MenuController:
    def run(self):
        players = []
        player_score = []
        player_score2 = []
        player_score3 = []
        player_score4 = []
        while True:
            menu_view = MenuView()
            started = menu_view.run()
            print(f"{started=}")
            if started == "1":
                player_view = PlayerView()
                players = player_view.run()
            if players and started == "4":
                tournament_view = TournamentView()
                tournament_view.run(players)
            if started == "3":
                report_view = ReportView()
                report_view.run(players,player_score,player_score2,player_score3,player_score4)
            if started == "7":
                return
