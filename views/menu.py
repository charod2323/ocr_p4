import sys
import time
import secrets


class MenuView:
    def run(self):
        import sys, time
        banner = "                   CHESS TOURNAMENT              "
        for char in banner:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
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
        started = input("                                       ")
        time.sleep(1)
        return started


class PlayerView:

    def run(self):
        players = []
        identity_and_rank = {}
        scores = [1, 0, 0.5]
        i = 0
        numberplayers = 2
        print()
        info = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~ YOU MUST BE CREATE 8 PLAYERS  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        for char in info:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.100)

        for i in range(numberplayers):
            player = "player"
            print()
            print("THE PlAYER NUMBER {}".format(i + 1))
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


class GamesView(PlayerView):
    def run(self):
        i = 0
        score = [0, 0.5, 1]

        print("...........match.......unique........")

        # presenter les players
        # commencer le match
        # demarrer le chrono
        start_time = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        print(f" start of the round {i + 1}: {start_time}")

        # fin de game
        # arreter le chrono
        end_time = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        print(f" end of the round {i + 1}: {start_time}")

        # afficher le gagant et le score attribué
        # afficher le perdant et le score attribué
        nbr_match_unique = int(input("how many match unique??:  "))
        for y in range(nbr_match_unique):
            pass


class TournamentView:
    def run(self, players):
        match = []
        score_winner = []
        score_losing = []
        score = [0, 0.5, 1]
        print()
        print()
        info = "------------------ THE TOURNAMENT BEGINS  --------------"
        i = 0
        for char in info:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.100)
        # VOIR SCHEMA DES TOURNOIS
        #print("how many matchs do you want to do (even number)")
        print("THE MATCH NUMBER {}".format(i + 1))
        print()
        print(players[0]['lastname'])
        print("vs")
        print(players[1]['lastname'])
        number_core1 = secrets.choice(score)
        number_core2 = secrets.choice(score)

        print("THE WINNER IS")


class LeaveView:
    def run(self):
        sys.exit()
