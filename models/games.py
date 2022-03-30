from tinydb import TinyDB, Query

class Game:
    def __init__(self, player1, player2,score, number_games):
        self.number_games = number_games
        self.player1 = player1
        self.player2 = player2
        self.score = score


    def get_serialized_player(self):
        """
        Return tinydb serialized player.
        :return:
        """
        return {
            "number_games": self.number_games,
            "player1": self.player1,
            "player2": self.player2,
            "score": self.score
             }

    def save_to_tiny_db(self):
        """

        :return:
        """
        db = TinyDB("db.json")
        games_table = db.table("games")
        games_table.insert(self.get_serialized_player())

    @classmethod
    def get_all_players_from_db(cls):
        db = TinyDB("db.json")
        games_table = db.table("games")
        return games_table.all()

    @classmethod
    def get_games_by_number_games(cls, number_games):
        """

        :param number_games:
        :return:
        """
        q = Query()
        db = TinyDB("db.json")
        print(db)
        print("number_games:", number_games)
        return db.search(q.games.number_games == number_games)

    @classmethod
    def save_players(cls, serialized_games):
        """

        :param serialized_games:
        :return:
        """
        db = TinyDB("db.json")
        games_table = db.table("games")
        games_table.insert_multiple(serialized_games)
