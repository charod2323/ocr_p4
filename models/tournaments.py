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
