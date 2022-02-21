class MenuView:


    def display_menu(self):
        choice = input('hello, taper 1 pour creer un nouveau player')
        return choice


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