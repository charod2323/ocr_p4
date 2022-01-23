import secrets
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
            # création du joueurs par l'utilisateur
            lastname = input("lastname? : ")
            firstname = input("firstname? : ")
            birth_date = input("birth_date? : ")
            birth_month = input("birth_month? : ")
            birth_year = input("birth_year? : ")
            sex = input("sex m/f? : ")
            age = input("age? : ")

            rank = 0
            # obliger l'utilisateur à entrer un nombre < 100
            while True:
                try:
                    rank = int(input("rank ?:  "))

                    break
                except ValueError:
                    print("Enter a number less than 100.")

            if rank > 100:
                rank = int(input("enter a number less than 100  :"))
            if rank == False:
                rank = int(input("enter a number less than 100  :"))
            if rank == True:
                rank = int(input("for validation retype his classification please  :"))

            time.sleep(0.0001)
            print()
            # afficher l'identiter et le classement du joueurs
            print("PLAYER{} ".format(i + 1) + " <identity and rank>")
            print()
            print("lastname => ", lastname)
            print("rank =>", rank)
            print()

            time.sleep(0)
            # création des dictionnaires "identités complètes avec classement"
            # numéroter les clées,les valeurs,les données avec str(i+1)
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
            # enregistrer les dictionnaires dans une liste "players"
            players.append(data_players)
        count = 0
        for i in players:
            count = count + 1
            # afficher le contenu de la liste players
            print("player", count, i)

        return players


class TournamentView:

    def run(self, players):
        score = [0, 1]
        player_score = []

        print()
        print()
        print("------------------------------ THE TOURNAMENT BEGINS  -------------------------------------\n")
        print()
        print()
        print()
        print()
        print()
        # afficher les éléments lastname et rank de la liste players
        print("identity => rank")
        for i in range(8):
            print(players[i]["lastname"], "=>       ", players[i]["rank"])

        print()
        print()
        print()
        print("-----------------LISTING OF PLAYERS ACCORDING TO THEIR RANKING-----------------------------------\n")
        print()
        print()
        print()

        # fonction qui trie chaques dictionnaires(dans la liste players)
        # en mode décroissant par rapport à leur classement
        def ranking(e):
            return e['rank']

        players.sort(reverse=True, key=ranking)
        count = 0
        # afficher le contenu players ligne par ligne
        for i in players:
            count = count + 1
            print("player", count, i)

        print()
        print()
        print()
        print()
        print("+++++++++++++++++++++++++++++++++++++++   ROUND1   +++++++++++++++++++++++++++++++++++++++++++++\n")
        print()
        print()
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
        for i in range(4):
            print()
            print()
            print("      MATCH  ", i + 1, "                         SCORE  ", i + 1, "                           \n")
            print()
            print()

            # choisir en mode aléatoire le score
            nbr_score1 = secrets.choice(score)
            nbr_score2 = secrets.choice(score)

            if nbr_score1 == nbr_score2:
                print("EGALITY")
                print("each player receives 0.5 points")
                nbr_score1 = 0.5
                nbr_score2 = 0.5

            # afficher la variable "lastname" des deux joueurs opposés
            print(players[i]["lastname"], "  VS  ", players[i + 4]["lastname"], "                             ",
                  nbr_score1, "  ", nbr_score2)
            # enregistrer variables players[] et nbr_sore dans la liste player_score sous forme de tuple
            player_score.append((players[i]["lastname"], nbr_score1))
            player_score.append((players[i + 4]["lastname"], nbr_score2))

            if nbr_score1 > nbr_score2:
                print(players[i]["lastname"], "WON")
                print()
                print()
            if nbr_score1 < nbr_score2:
                print(players[i]["lastname"], "LOST")
                print()
                print()

        print()
        print()
        print("listing of matches")
        print()
        print("     MATCH1                 MATCH2                  MATCH3                 MATCH4          ")
        # extraction des éléments dans la liste player_sore pour enregistrer les matchs sous formes de listes
        m = [[0] * 4 for i in range(4)]
        # [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        count = 0
        # player_score contient le nom des joueurs et son score
        m[count][count] = player_score[0][0]
        m[count][count + 1] = player_score[0][1]
        m[count][count + 2] = player_score[1][0]
        m[count][count + 3] = player_score[1][1]

        m[count + 1][count] = player_score[2][0]
        m[count + 1][count + 1] = player_score[2][1]
        m[count + 1][count + 2] = player_score[3][0]
        m[count + 1][count + 3] = player_score[3][1]

        m[count + 2][count] = player_score[4][0]
        m[count + 2][count + 1] = player_score[4][1]
        m[count + 2][count + 2] = player_score[5][0]
        m[count + 2][count + 3] = player_score[5][1]

        m[count + 3][count] = player_score[6][0]
        m[count + 3][count + 1] = player_score[6][1]
        m[count + 3][count + 2] = player_score[7][0]
        m[count + 3][count + 3] = player_score[7][1]
        print(m)

        print()
        print()
        print()
        print("list of players with total points")
        print()
        print()
        # afficher ligne par ligne le contenu de player_score
        count = 0
        for i in player_score:
            count = count + 1
            print(i)

        print()
        print()
        print("listing of players by ranking")
        print()
        print()
        # afficher ligne par ligne le contenu de players('lastname',et'rank')
        for y in range(8):
            print("player", y + 1, "    ", "identity:", players[y]['lastname'], "       ", "rawking:",
                  players[y]['rank'])
        print()
        print()
        print("++++++++++++++++++++++++++++++++++++++   ROUND2   +++++++++++++++++++++++++++++++++++++++++++++++++++")
        print()
        print()
        print()
        print()
        player_score2 = []
        array_player1 = []
        array_player2 = []
        for i in range(1, 5):
            array_player2.append(players[(i * 2) - 1]["lastname"])
        for i in range(4):
            array_player1.append(players[i * 2]["lastname"])
        for i in range(4):
            print()
            print()
            print("      MATCH  ", i + 1, "                            SCORE  ", i + 1, "                           \n")
            print()
            print()

            # choisir en mode aléatoire le score
            nbr_score3 = secrets.choice(score)
            nbr_score4 = secrets.choice(score)
            nbr_score5 = secrets.choice(score)
            nbr_score6 = secrets.choice(score)

            if nbr_score3 == nbr_score4:
                print("EGALITY")
                print("each player receives 0.5 points")
                nbr_score3 = 0.5
                nbr_score4 = 0.5
                # afficher la variable "lastname" des deux joueurs opposés
                print(array_player1[i], "  VS  ", array_player2[i], "                             ",
                      nbr_score3, "  ", nbr_score4)
                # enregistrer variables players[] et nbr_sore dans la liste player_score sous forme de tuple
                player_score.append((array_player1[i], nbr_score3))
                player_score.append((array_player2[i], nbr_score4))
            if nbr_score5 > nbr_score6:
                print(array_player1[i],"VS",array_player2[i],"                                 ",
                      nbr_score5, "  ", nbr_score6)
                print(array_player1[i], "WON")
                print()
                print()
            if nbr_score5 < nbr_score6:
                print(array_player1[i], "VS", array_player2[i], "                                 ",
                      nbr_score5, "  ", nbr_score6)
                print(array_player1[i], "LOST")
                print()
                print()

        print()
        print()
        print()
        print("list of players with total points")
        print()
        print()
        count = 0
        for i in player_score:
            count = count + 1
            print(i)


class LeaveView:
    def run(self):
        sys.exit()
