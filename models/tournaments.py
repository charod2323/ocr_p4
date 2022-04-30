from tinydb import TinyDB


class Tournament:
    def __init__(
        self,
        name,
        place,
        dated,
        number_of_turns,
        tour,
        players,
        time_control,
        description,
    ):
        self.name = name
        self.place = place
        self.dated = dated
        self.number_of_turns = number_of_turns
        self.tour = tour
        self.players = players
        self.time_control = time_control
        self.description = description

    def get_serialized_tournament(self):
        """
        Return tinydb serialized tournament.
        :return:
        """
        return {
            "name": self.name,
            "place": self.place,
            "dated": self.dated,
            "number_of_turns": self.number_of_turns,
            "tour": self.tour,
            "players": self.players,
            "time_control": self.time_control,
            "description": self.description,
        }

    def save_to_tiny_db(self):
        """

        :return:
        """
        db = TinyDB("db.json")
        tournamenets_table = db.table("tournaments")
        tournamenets_table.insert(self.get_serialized_tournament())

    @classmethod
    def get_all_tournaments_from_db(cls):
        db = TinyDB("db.json")
        tournaments_table = db.table("tournaments")
        return tournaments_table.all()


