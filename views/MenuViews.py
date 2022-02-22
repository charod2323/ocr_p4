from enum import IntEnum

class MenuView(IntEnum):
    CreationPlayer = 1
    CreationRound = 2
    CreationTournament = 3
    AccessReports = 4

    def display_menu(self):
        choice = input(int('what is your choice(Player[1], Round[2], Tournament[3], AcessReport[4]'))
        your_request = MenuView(choice)
        return your_request

    def get_new_player_info(self):
        infos = {}
        infos['firstname'] = input("enter the firstname")
        infos['lastname'] = input("enter the lastname")
        infos['age'] = input("enter the age")
        infos['birth_date'] = input("enter the birth_date")
        infos['birth_date'] = input("enter the birth_month")
        infos['birth_year'] = input("enter the birth_year")
        infos['sex'] = input("sex")
        return infos
