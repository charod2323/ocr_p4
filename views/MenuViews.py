#import secrets
import sys
import time
#from itertools import islice


class MenuView:
    def run(self):
        print()
        print()
        print("                                                                       CHESS TOURNAMENT              ")
        print()
        message = "              CREATE A NEW PLAYER         \n " \
                  "                                          \n " \
                  "        1   create a new players          \n " \
                  "        2   classification update         \n " \
                  "        3        report                   \n " \
                  "                                          \n " \
                  "                                          \n" \
                  "                                          \n" \
                  "                                          \n" \
                  "             CREATE A TOURNAMENT          \n " \
                  "                                          \n " \
                  "        4 create a new tournament         \n " \
                  "        5         scores                  \n " \
                  "        6         report                  \n" \
                  "         7          quit                   \n " \
                  "                                           \n" \
                  "                                           \n" \
                  " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ENTER THE NUMBER ONE TO START ~~~~~~~~~~~~~~~~~~~~~\n" \
                  "                                                                                                        \n" \
                  "                                                                                                        \n" \
                  "                                                    or enter the number 7 to quit                         "
        time.sleep(0.0001)
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.0001)
        print()
        print()
        print()
        started = input("                   ENTER A NUMBER TO START            =>: ")
        time.sleep(0)
        return started


class PlayerView:

    def create_new_player(self):
        i = 0

        print()
        print()
        message = ("..................THE PlAYER NUMBER {}.................".format(i + 1))
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.0001)
        print()
        print()

        # création du joueurs par l'utilisateur
        value_player = []

        lastname = input("lastname? : ")
        firstname = input("firstname? : ")
        birth_date = input("birth_date? : ")
        birth_month = input("birth_month? : ")
        birth_year = input("birth_year? : ")
        sex = input("sex m/f? : ")
        age = input("age? : ")

        value_player.append(lastname)
        value_player.append(firstname)
        value_player.append(birth_date)
        value_player.append(birth_year)
        value_player.append(birth_month)
        value_player.append(sex)
        value_player.append(age)
        return value_player

    def verification_rank(self):
        # obliger l'utilisateur à entrer un nombre < 100
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
        print()
        return rank

    def display_listing(self):
        i = 0
        key_player = "key_player"
        key_players = key_player + str(i + 1)
        value_player = "value_player"
        value_players = value_player + str(i + 1)
        data_player = "data_player"
        data_players = data_player + str(i + 1)
        key_players = ['lastname', 'firstname', 'birth_date', 'birth_month', 'birth_year', 'sex', 'age',
                       'rank']
        data_players = dict(zip(key_players, listing))
        print()
        players = []
        players.append(data_players)
        print(players)
