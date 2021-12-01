class NumberPracticingOfTournament:


    def __init__(self, numbers_participating):
        self.numbers_participating = numbers_participating


class NumberOrganizer:


    def organizer(self,numbers_organizer):
        self.numbers_organizer = numbers_organizer


class PlaceOfTournament:


    def place_of_tournament(self,numbers_participating):
        self.numbers_participating = numbers_participating


class Materials:


    def materials(self,numbers_of_tables,numbers_of_chairs,numbers_of_chessboards):
        self.numbers_of_tables = numbers_of_tables
        self.numbers_of_chairs = numbers_of_chairs
        self.numbers_of_chessboards =numbers_of_chessboards
        for numbers in range(numbers_of_tables):
            numbers_of_chairs(numbers_of_tables*2)
            numbers_of_chessboards(numbers_of_tables)


class EnergyConsumption:


    def energy_consumption(self,electricity_kilowatt_kW):
        self.electricity_kilowatt_kw = electricity_kilowatt_kW


class LastTournament:


    def how_many_times(self,hours):
        self.hours = hours


class  NumberedChair:


    def Number(self,numbers):
        self.numbers = numbers