class ReportView:
    def run(self, players, player_score,player_score2,player_score3,player_score4):
        print("player display in alphabetical order")
        player_order = sorted(players, key=lambda d: d["lastname"])
        count = 0
        for i in player_order:
            count = count + 1
            print(i)

        print("________________________classement______________________________")

        def ranking(e):
            return e['rank']

        players.sort(reverse=True, key=ranking)
        count = 0
        # afficher le contenu players ligne par ligne
        for i in players:
            count = count + 1
            print("player", count, i)
