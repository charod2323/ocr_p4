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
    def reference_tournament(self,players):
        print()
        ref_tournament = {'name_tournament': input("            name tournament??:  "),
               'location_tournament': input("                   location_tournament??:  "),
               'date_tournament': input("                       date_tournament??:  "),
               'description_tournament': input("               description_tournament:  "),
               'control_time': input("                         bullet or blitz ou un coup rapide??:  "),
               'player': players}
        print()
        print("")
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
        for i in range(4):
            print()
            print()
            print("      MATCH  ", i + 1, "                                                    \n")
            print()
            print()
            # afficher la variable "lastname" des deux joueurs opposés
            print (players[i]['lastname'],"    VS    ",players[i+4]['lastname'])
            print()


"""        
        # enregistrer variables players[] et nbr_score dans la liste player_score sous forme de tuple
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
        print("________mises à jours classement________")
        print()
        print()
        print(players[i]["lastname"], "=>", nbr_score1 + players[i]["rank"], players[i + 4]["lastname"], "=>",
              nbr_score2 + players[i + 4]["rank"], )
        print()
        print()
        update_rawk.append(players[i]["lastname"])
        update_rawk.append(nbr_score1 + players[i]["rank"])
        update_rawk.append(players[i + 4]["lastname"])
        update_rawk.append(nbr_score2 + players[i + 4]["rank"])
        print()
        print()
    print()
    print("listing of matches")
    match = player_score
    matches = list(x for t in match for x in t)
    length_to_split = [len(matches) // 4] * 4
    lst = iter(matches)
    match_player_score = [list(islice(lst, elem))
                          for elem in length_to_split]
    print("     MATCH1          MATCH2           MATCH3             MATCH4   ")
    print(match_player_score)

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
    print("new ranking")
    print()
    print()
    print(update_rawk)
    print()
    print()
    print()
    print()
"""
