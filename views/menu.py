import random
import sys
import time


class MenuView:
    def run(self):
        print("                                CREATE A PLAYER                                 ")
        print("                                                                                ")
        print("                           1  create a new players                              ")
        print("                           2  classification update                             ")
        print("                           3       report                                       ")
        print("                           4    return choice 1                                 ")
        print("                           5         quit                                       ")
        print("                                                                                ")
        print("                                                                                ")
        print("                           6        CREATE A GAME                               ")
        print("                                                                                ")
        print("                           7        print players                               ")
        print("                           8           scores                                   ")
        print("                                       quit                                     ")
        print("                                                                                ")
        print("                                                                                ")
        print("                                CREATE A TOURNAMENT                             ")
        print("                                                                                ")
        print("                           9  create a new tournament                           ")
        print("                           10         report                                    ")
        print("                           11     return choice 4                               ")
        print("                           12          quit                                     ")
        print("                                                                                ")
        print()
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~press key 1 to start~~~~~~~~~~~~~~~~~~~~~~")
        started = input("                                       ")
        return started


class PlayerView:

    def run(self):
        i = 0
        numberplayers = input("how many players??:  ")
        try:
            numberplayers = int(numberplayers)
        except ValueError:
            sys.exit("you must enter an integer")
        for i in range(numberplayers):
            player = "player"
            print()
            print("the player number {}".format(i + 1))
            print()

            lastname = input("lastname? : ")
            firstname = input("firstname? : ")
            birth_date = input("birth_date? : ")
            birth_month = input("birth_month? : ")
            birth_year = input("birth_year? : ")
            sex = input("sex m/f? : ")
            age = input("age? : ")
            rank = input("rank /10? : ")
            print()
            print("player{}".format(i + 1) + "identity")
            print()
            print("lastname => ", lastname)
            print("firstname => ", firstname)
            print("birth_date => ", birth_date)
            print("birth_month => ", birth_month)
            print("birth_year => ", birth_year)
            print("sex => ", sex)
            print("age =>", age)
            print("rank =>", rank)
            print()
            print()

            list_data_players = []

            key_player = "key_player"
            key_players = key_player + str(i + 1)
            value_player = "value_player"
            value_players = value_player + str(i + 1)
            data_player = "data_player"
            data_players = data_player + str(i + 1)

            key_players = ['lastname', 'firstname', 'birth_date', 'birth_month', 'birth_year', 'sex', 'age', 'rank']
            value_players = [lastname, firstname, birth_date, birth_month, birth_year, sex, age, rank]
            data_players = dict(zip(key_players, value_players))
            print("                                                  DATA PLAYERS                                    ")
            print()
            print(data_players)
            list_data_players.append(data_players)


class GamesView:
    def run(self):
        games = []
        score = [0, 0.5, 1]

        print("...........match.......unique........")
        # demarrer le chrono
        # fin de game arreter le chrono
        # afficher le gagant et le score attribué
        # afficher le perdant
        nbr_match_unique = int(input("how many match unique??:  "))
        for y in range(nbr_match_unique):
            pass


class TournamentView:
    def run(self):
        i = 0
        nbrround = input("how many rounds (4 by default):  ")
        while nbrround != 4:
            print()
            start_time = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
            print(f" start of the round {i + 1}: {start_time}")
            return


class LeaveView:
    def run(self):
        sys.exit()
