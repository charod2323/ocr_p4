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

        player = {}
        print()
        print()
        player = {
            "lastname": input("lastname?:  "),
            "firstname": input("firstname?:  "),
            "age": input("age?:  "),
            "birthdate": input("birthdate?:  "),
        }
        print()
        print("players:", player)
        print()
        return player

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
        return rank


class TournamentView:
    def reference_report(self, players):
        print()
        ref_tournament = {'name_tournament': input("            name tournament??:  "),
                          'location_tournament': input("                   location_tournament??:  "),
                          'date_tournament': input("                       date_tournament??:  "),
                          'description_tournament': input("               description_tournament:  "),
                          'control_time': input("                         bullet or blitz ou un coup rapide??:  "),
                          'player': players}
        print()
        print()
        return ref_tournament

    def run(self, players):
        print()
        print()
        print("------------------------------ THE TOURNAMENT BEGINS  -------------------------------------\n")
        print()
        print()
        print()
        print("-----------------LISTING OF PLAYERS ACCORDING TO THEIR RANKING-----------------------------------\n")
        print()
        print("                           in descending order                      ")
        print()

        # fonction qui trie chaques dictionnaires(dans la liste players)
        # en mode décroissant par rapport à leur classement
        def rank(e):
            return e['ranking']

        players.sort(reverse=True, key=rank)
        count = 0
        # afficher le contenu players ligne par ligne
        for i in players:
            count = count + 1
            print("player", count, i)
        return players

    def split_list(self, players):
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
        info_winner = {}
        infos_winners = []
        for i in range(4):
            print()
            print()
            print("      MATCH  ", i + 1, "                                                    \n")
            print()
            print()
            # afficher la variable "lastname" des deux joueurs opposés
            print(players[i]['lastname'], "    VS    ", players[i + 4]['lastname'])
            print()
            info_winner = {"lastname_winner": input(" note the name of the winning player:  "),
                           "score_winner": input(" note the score of the winning player:  ")}
            infos_winners.append(info_winner)
            print()
            print()
        # afficher le contenu players ligne par ligne
        for i in infos_winners:
            print(i)

        return infos_winners
    def update_rawk(self, players,infos_winners):

        print("                                 ROUND2                                             ")
        print()
