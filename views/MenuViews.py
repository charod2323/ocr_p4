import sys
import time


# from itertools import islice


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
        player = {}
        print()
        print()
        for i in range(8):
            message = ("..................THE PlAYER NUMBER {}.................".format(i + 1))
            for char in message:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0001)
            print()
            print()
            player = {
                "lastname": input("lastname?"),
                "firstname": input("firstname?"),
                "age": input("age?"),
                "birthdate": input("birthdate?"),
            }
            print()
            print("players:", player)
            print()
            print()

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