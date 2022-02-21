from models.players import Player
from views.MenuViews import MenuView


class Controller:
    """
    TODO:
    """

    def run(self):
        v = MenuView()
        choice = v.display_menu()
        if choice == 1:
            self.create_new_player()

    def create_new_player(self):
        v = MenuView()
        infos = v.get_new_player_info()
        new_player = Player(
            lastname=infos['lastname'],
            firstname=infos['firstname'],
            age=infos['age'],
            birth_date=infos['birth_date'],
            birth_month=infos['birth_month'],
            birth_year=infos['birth_year'],
            sex=infos['sex']

        )
        print("Nouveau player cree : ", new_player)
