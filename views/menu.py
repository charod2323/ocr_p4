# import secrets
import sys
import time


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

    def run(self):
        players = []
        scores = [1, 0, 0.5]
        i = 0
        numberplayers = 8

        print()

        for i in range(numberplayers):
            player = "player"
            print()
            message = ("..................THE PlAYER NUMBER {}.................".format(i + 1))

            for char in message:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0001)
            print()
            print()

            lastname = input("lastname? : ")
            firstname = input("firstname? : ")
            birth_date = input("birth_date? : ")
            birth_month = input("birth_month? : ")
            birth_year = input("birth_year? : ")
            sex = input("sex m/f? : ")
            age = input("age? : ")
            rank = 0
            rank = int(input("rank/100?  :"))
            while True:
                try:
                    rank = rank < 100

                    break
                except ValueError:
                    print("Enter a number less than 100.")

            if rank == False:
                rank = int(input("enter a number less than 100  :"))
            if rank == True:
                rank = int(input("for validation retype his classification please  :"))

            time.sleep(0.0001)
            print()
            print("PLAYER{} ".format(i + 1) + " <identity and rank>")
            print()
            print("lastname => ", lastname)
            print("rank =>", rank)
            print()

            time.sleep(0)
            key_player = "key_player"
            key_players = key_player + str(i + 1)
            value_player = "value_player"
            value_players = value_player + str(i + 1)
            data_player = "data_player"
            data_players = data_player + str(i + 1)
            key_players = ['lastname', 'firstname', 'birth_date', 'birth_month', 'birth_year', 'sex', 'age', 'rank']
            value_players = [lastname, firstname, birth_date, birth_month, birth_year, sex, age, rank]
            data_players = dict(zip(key_players, value_players))

            print()

            players.append(data_players)
        count = 0
        for i in players:
            count = count + 1
            print("player", count, i)

        return players


class TournamentView:

    def run(self, players):
        score = [0, 0.5, 1]

        print()
        print()
        print("------------------------------ THE TOURNAMENT BEGINS  -------------------------------------\n")
        print()
        print()
        print()
        print()
        print()
        print("identity => rank")
        for i in range(8):
            print(players[i]["lastname"], "=>", players[i]["rank"])

        print()
        print()
        print()
        print("-----------------LISTING OF PLAYERS ACCORDING TO THEIR RANKING-----------------------------------\n")
        print()
        print()
        print()

        def ranking(e):
            return e['rank']

        players.sort(reverse=True, key=ranking)
        count = 0
        for i in players:
            count = count + 1
            print("player", count, i)
        print()
        print()
        print()
        print("----------------------------------------ROUND 1----------------------------------------\n")
        print()
        print()
        print()
        print("the first 4 in the standings are:\n")
        count = 0
        for i in players:
            count = count + 1
            print("player", count, i)
            if count == 4:
                print()


class LeaveView:
    def run(self):
        sys.exit()
