from tinydb import TinyDB, Query


class Player:
    def __init__(
        self, lastname, firstname, age, birth_date, birth_month, birth_year, sex
    ):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age
        self.birth_date = birth_date
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.sex = sex

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
