from models.players import Player
from views.MenuViews import MenuView, PlayerView
#from tinydb import TinyDB, Query

# from pprint import pprint

class MenuController:
    def run(self):
        players = []
        started1 = ""
        while True:
            menu_view = MenuView()
            started = menu_view.run()

            if started == "1":
                menu_view = MenuView()
                started1 = menu_view.submenu_players()

            if started1 == "1.0":
                player_view = PlayerView()
                player_infos = player_view.create_new_player()


                print()
                print("player_infos:", player_infos)
                new_player = Player(
                    lastname=player_infos["lastname"],
                    firstname=player_infos["firstname"],
                    age=player_infos["age"],
                    birth_date=player_infos["birth_date"],
                    birth_month=player_infos["birth_month"],
                    birth_year=player_infos["birth_year"],
                    sex=player_infos["sex"],
                    identifier=player_infos["identifier"],
                )
                print()
                print()
                print("new_player:", new_player)
                # Save the new player into the database
                new_player.save_to_tiny_db()
                print("Voici tous les joueurs enregistrés dans la db : ")


"""
            if started == "3":
                ref_tournament = []
                infos_winners = []
                tournament_view = TournamentView()
                ref = tournament_view.reference_report(players)
                ref_tournament.append(ref_tournament)
                players = tournament_view.run(players)
                tournament_view.split_list(players)
                infos_winners = tournament_view.players_face_to_face(players)

            if started == "4":
                return
"""
