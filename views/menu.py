import secrets
import sys
import time


class MenuView:
    def run(self):
        import sys, time
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
                  " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ENTER THE NUMBER OF YOUR CHOICE~~~~~~~~~~~~~~~~~~~~~~ "

        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print()
        started = input("                                       ??  ")
        time.sleep(1)
        return started


class PlayerView:

    def run(self):
        players = []
        identity_and_rank = {}
        scores = [1, 0, 0.5]
        i = 0
        numberplayers = 4
        print()

        for i in range(numberplayers):
            player = "player"
            print()
            message = ("..................THE PlAYER NUMBER {}.................".format(i + 1))
            for char in message:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.100)
            print()
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
            print("PLAYER{} ".format(i + 1) + " <identity and rank>")
            print()
            print("lastname => ", lastname)
            print("firstname => ", firstname)
            print("rank =>", rank)
            print()
            time.sleep(1)
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

        return players


class TournamentView:
    def run(self, players):
        tournament_name = []
        tournament_place = []
        tournament_date = []
        tournament_nbr_rounds = []
        tournament_description = []
        match = []
        scores = {}
        score = [0, 0.5, 1]
        print()
        print()
        info = "------------------ THE TOURNAMENT BEGINS  --------------"
        i = 0
        for char in info:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.100)

        nbr_match = int(input("how many matchs do you want to do (even number)??:  "))
        while nbr_match % 2 != 0:
            print()
            print("............you must enter an even number...........")
        for i in range(nbr_match):
            number_score1 = secrets.choice(score)
            number_score2 = secrets.choice(score)
            print()
            print("THE MATCH NUMBER {}".format(i + 1))
            print()
            print((players[i]['lastname'].upper()).center(50), number_score1)
            print("VS".center(50))
            print((players[i + 1]['lastname'].upper()).center(50), number_score2)
            time.sleep(2)
            if number_score1 == number_score2:
                print("EGALITY")
            elif number_score1 > number_score2:
                print("THE WINNER IS", players[0]['lastname'])
                scores[players[0]] = number_score1
            else:
                print("THE WINNER IS", players[1]['lastname'])
                scores[players[1]] = number_score2

            print(scores)


class LeaveView:
    def run(self):
        sys.exit()
