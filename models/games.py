from random import *


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score = None
        self.list_players_games = None

    def pairs_generated(self):
        print("the players and their opponents are")
        print("")
        print("games1 => " + games1.player1 + " VS " + games1.player2)
        print("games2 => " + games2.player1 + " VS " + games2.player2)
        print("games3 => " + games3.player1 + " VS " + games3.player2)
        print("games4 => " + games4.player1 + " VS " + games4.player2)

    def start_of_the_match(self):
        for i in range(1):
            i = i + 1
            self.list_players_games1 = [games1.player1, games1.player2]
            print(f"the winner of the match {i} is :")
            print(sample(self.list_players_games1, 1))
            print("")
            i = i + 1
            self.list_players_games2 = [games2.player1, games2.player2]
            print(f"the winner of the match {i} is :")
            print(sample(self.list_players_games2, 1))
            print("")
            i = i + 1
            self.list_players_games3 = [games3.player1, games3.player2]
            print(f"the winner of the match {i} is :")
            print(sample(self.list_players_games3, 1))
            print("")
            i = i + 1
            self.list_players_games4 = [games4.player1, games4.player2]
            print(f"the winner of the match {i} is :")
            print(sample(self.list_players_games4, 1))


rank = [["Carlsen", 2882],
        ["Kasparov", 2851],
        ["Caruana", 2844],
        ["Aronian", 2830],
        ["So", 2822],
        ["Mamedyarov", 2820],
        ["Vachier-Lagrave", 2819],
        ["Anand", 2817]]

games1 = Game(rank[0][0], rank[4][0])
games2 = Game(rank[1][0], rank[5][0])
games3 = Game(rank[3][0], rank[6][0])
games4 = Game(rank[5][0], rank[7][0])

games1.pairs_generated()
print("")
response = input("do you want to start the tournament: ")
print("")

if response == "yes":
    games1.start_of_the_match()
else:
    print("")
    print("the tournament does not start")
