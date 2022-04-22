from tinydb import TinyDB, Query


class Player:
    def __init__(
        self, lastname, firstname, age, birth_date, birth_month, birth_year, sex, identifier
    ):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age
        self.birth_date = birth_date
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.sex = sex
        self.identifier = identifier

    def get_serialized_player(self):
        """
        Return tinydb serialized player.
        :return:
        """
        return {
            "lastname": self.lastname,
            "firstname": self.firstname,
            "age": self.age,
            "birth_date": self.birth_date,
            "birth_month": self.birth_month,
            "birth_year": self.birth_year,
            "sex": self.sex,
            "identifier":self.identifier,
        }

    def save_to_tiny_db(self):
        """

        :return:
        """
        db = TinyDB("db.json")
        players_table = db.table("players")
        players_table.insert(self.get_serialized_player())

    @classmethod
    def get_all_players_from_db(cls):
        db = TinyDB("db.json")
        players_table = db.table("players")
        return players_table.all()

    @classmethod
    def get_player_by_lastname(cls, lastname):
        """

        :param lastname:
        :return:
        """
        q = Query()
        db = TinyDB("db.json")
        print(db)
        print("lastname:", lastname)
        return db.search(q.players.lastname==lastname)

    @classmethod
    def save_players(cls, serialized_players):
        """

        :param serialized_players:
        :return:
        """
        db = TinyDB("db.json")
        players_table = db.table("players")
        players_table.insert_multiple(serialized_players)



if __name__ == "__main__":
    p1 = Player(
    lastname = input("lastname?"),
    firstname = "john",
    age = "35",
    birth_date ="29",
    birth_month = "12",
    birth_year = "80",
    sex = "m",
    identifier = "23"
    )
    p1.save_to_tiny_db()
    print("Voici tous les joueurs enregistrés dans la db : ")
    players = Player.get_all_players_from_db()
    for t in players:
        print("===================")
        print(t)
