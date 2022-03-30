from tinydb import TinyDB, Query



class Round:

    def __init__(self, round_number, games, date, heure_debut, heure_fin):

        self.round_number = round_number
        self.date = date
        self.heure_debut = heure_debut
        self.heure_fin = heure_fin
        self.games = games

    def get_serialized_player(self):
        """
        Return tinydb serialized player.
        :return:
        """
        return {
            "round_number": self.round_number,
            "date": self.date,
            "heure_debut": self.heure_debut,
            "heure_fin": self.heure_fin,
            "games": self.games
             }

    def save_to_tiny_db(self):
        """

        :return:
        """
        db = TinyDB("db.json")
        rounds_table = db.table("rounds")
        rounds_table.insert(self.get_serialized_player())

    @classmethod
    def get_all_rounds_from_db(cls):
        db = TinyDB("db.json")
        rounds_table = db.table("rounds")
        return rounds_table.all()

    @classmethod
    def get_player_by_round_number(cls, round_number):
        """

        :param round_number:
        :return:
        """
        q = Query()
        db = TinyDB("db.json")
        print(db)
        print("round_number:", round_number)
        return db.search(q.rounds.round_number == round_number)

    @classmethod
    def save_players(cls, serialized_rounds):
        """

        :param serialized_rounds:
        :return:
        """
        db = TinyDB("db.json")
        rounds_table = db.table("rounds")
        rounds_table.insert_multiple(serialized_rounds)
