class MenuView:
    def run(self):
        print("Welcome, 1 for create a player with his opponent, 2 for create a tournament.")
        choice = input("Enter your choice: ")
        return choice


class PlayerView:
    def run(self):
        for c in range(2):
            print("identification player number: ")
            lastname = input("enter lastname: ")
            print(lastname)


class TournamentView:
    pass
