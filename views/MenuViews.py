# import sys
import time


class MenuView:
    def run(self):
        """Creation menu"""
        print()
        print()
        print("CHESS TOURNAMENT                    ")
        print()
        message = "                                  \n " \
                  "1   ENTER THE PLAYERS SUBMENU     \n " \
                  "2   ENTER THE TOURNAMENTS SUBMENU \n " \
                  "3   ENTER THE RAPPORTS SUBMENU    \n " \
                  "4          EXIT                   \n " \
                  "                                  \n " \

        print(message)
        print()
        print()
        print()
        started = input("ENTER A NUMBER TO START      =>: ")
        return started

    def submenu_players(self):
        """Creation submenu_players"""
        message1 = "                                  \n " \
                   "1.0   create a player               \n " \
                   "1.1   update a player from his id   \n " \
                   "1.2   display a player from his id  \n " \
                   "1.3   delete a player from his id   \n " \

        print(message1)
        print()
        print()
        print()
        started1 = input("ENTER A CODE NUMBER       =>: ")
        return started1

    def submenu_tournaments(self):
        """Creation submenu_tournament"""
        message2 = "                                      \n " \
                   "1   create a tournament               \n " \
                   "2   update a tournament from his id   \n " \
                   "3   display a tournament from his id  \n " \
                   "4   delete a tournament from his id   \n " \

        print(message2)
        print()
        print()
        print()
        started2 = input("ENTER A NUMBER TO START      =>: ")
        return started2

    def submenu_rapports(self):
        """Creation submenu_rapport"""
        message3 = "                                      \n " \
                   "1   create a rapport                  \n " \
                   "2   update a rapport from his id      \n " \
                   "3   display a rapport from his id     \n " \
                   "4   delete a rapport from his id      \n " \

        print(message3)
        print()
        print()
        print()
        started3 = input("ENTER A NUMBER TO START      =>: ")
        return started3


class PlayerView:
    def create_new_player(self):
        """creation new player"""
        player = {}
        print()
        print()
        player = {
            "lastname": input("lastname?:  "),
            "firstname": input("firstname?:  "),
            "age": input("age?:  "),
            "birth_date": input("birthdate?:  "),
            "birth_month": input("birth_month?:  "),
            "birth_year": input("birth_year?:  "),
            "sex": input("sex?:  "),
            "identifier": input("identifier?:  "),
        }
        return player

    def verification_rank(self, player):
        """force the user to enter a number less than 100"""
        while True:
            try:
                rank = int(input("rank/100 ?:  "))
                break
            except ValueError:
                print("Enter a number less than 100.")
        if rank > 100:
            rank = int(input("enter a number less than 100  :"))
        if rank == False:
            rank = int(input("enter a number less than 100  :"))
        if rank == True:
            rank = int(input("for validation retype his classification  :"))
        time.sleep(0.0001)
        player['ranking'] = rank
        print(player)
        return player


class TournamentView:
    def reference_report(self, players):
        """information request spins"""
        print()
        ref_tournament = {'name_tournament': input("name tournament??:  "),
                          'location_tournament': input("location_tournament??:  "),
                          'date_tournament': input("date_tournament??:  "),
                          'description_tournament': input("description_tournament:  "),
                          'control_time': input("bullet or blitz ou un coup rapide??:  "),
                          'player': players}
        print()
        print()
        return ref_tournament

    def run(self, players):
        """listing players in descending ranking mode"""
        print()
        print()
        print("THE TOURNAMENT BEGINS  -------------------------------------\n")
        print()
        print()
        print()
        print("LISTING OF PLAYERS ACCORDING TO THEIR RANKING-----------------------------------\n")
        print()
        print("in descending order                      ")
        print()

        def rank(e):
            return e['ranking']

        players.sort(reverse=True, key=rank)
        count = 0
        for i in players:
            count = count + 1
            print("player", count, i)
        return players

    def split_list(self, players):
        """creation of 2 groups of players"""
        print()
        print("+++++++++++++++++++++++++++++++++++++++   ROUND1   +++++++++++++++++++++++++++++++++++++++++++++\n")
        print()
        # coupe la liste players en deux parties
        print("the first 4 in the standings are:\n")
        count = 0
        for i in players:
            count = count + 1
            print("player", count, i)
            if count == 4:
                print()
                print("the last 4 in the standings are\n")
        print()
        print()

    def players_face_to_face(self, players):
        """match and scores"""
        info_winners = []
        info_egality = []
        infos_egalitys = []
        update = []
        for i in range(4):
            print()
            print()
            print("      MATCH  ", i + 1, "                                                    \n")
            print()
            print()
            print(players[i]['lastname'], "    VS    ", players[i + 4]['lastname'])
            print()
            winner_infos = input("is there equality enter yes or no:  ")
            if winner_infos == "yes":
                print(players[i]['lastname'], "    VS    ", players[i + 4]['lastname'], "=>   EGALITY   ")
                info_egality.append(players[i]['lastname'])
                info_egality.append(players[i + 4]['lastname'])
                infos_egalitys.append(info_egality)
            else:
                print()
                winner_info = input("who is the winner enter 1 for player one and 2 for player two")
                if winner_info == str(1):
                    player1 = players[i]['lastname']
                    print("so the winner is", player1)
                    info_winners.append(players[i]['lastname'])

                else:
                    player2 = players[i + 4]['lastname']
                    print("so th winner is", player2)
                    info_winners.append(players[i + 4]['lastname'])

    def update_ranking(self):
        pass

    def report(self):
        pass
