class Player:
    def __init__(self, lastname, firstname, age, birth_date, sex):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age
        self.birth_date = birth_date
        self.sex = sex
        self.rank = None


    def print_players(self):
        print(f"all players: {a_player} ")


if __name__ == "__main__":
    # création de quelques joueurs
    p1 = Player("jean", "Dupont", 35, "1986-01-01", "M")
    p2 = Player("pierre", "Hubert", 38, "1983-25-01", "M")
    p3 = Player("rené", "Vasseur", 35, "1986-02-05", "M")
    p4 = Player("daniel", "Lambert", 29, "1992-04-01", "M")
    p5 = Player("richard", "Morel", 29, "1992-04-01", "M")
    p6 = Player("alfred", "Garcia", 35, "1986-01-01", "M")
    p7 = Player("kevin", "Jones", 38, "1983-25-01", "M")


    all_player = [p1, p2, p3, p4, p5, p6, p7]
    for a_player in all_player:
        a_player.print_players()

    # ajout d'un joueur
    p8 = Player("anthony", "Roche", 29, "1992-07-01", "M")
    all_player.append(p8)
