import secrets
from itertools import islice

class TournamentView:




    def run(self, players):
        score = [0, 1]
        player_score = []
        update_rawk = []
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
        print("                           in descending order                      ")
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
            print()
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
        print()
        print("++++++++++++++++++++++++++++++++++++++   ROUND2   +++++++++++++++++++++++++++++++++++++++++++++++++++")
        print()
        print()
        print()
        print()
        # nouvelles variables
        player_score2 = []
        array_player1 = []
        array_player2 = []
        update_rawk2 = []
        scores = [0,1]
        # on enregistre la position des premiers joueurs
        for i in range(1, 5):
            array_player2.append(players[(i * 2) - 1]["lastname"])
        # on enregistre la position des adversaires
        for i in range(4):
            array_player1.append(players[i * 2]["lastname"])
        print()
        print()


        # demarrage des matchs
        for i in range(4):
            print()
            print()
            print("      MATCH  ", i + 1, "                            SCORE  ", i + 1, "                           \n")
            print()
            print()
            # choisir en mode aléatoire le score
            nbr_score5 = secrets.choice(scores)
            nbr_score6 = secrets.choice(scores)
            if nbr_score5 == nbr_score6:
                print("EGALITY")
                print("each player receives 0.5 points")
                nbr_score5 = 0.5
                nbr_score6 = 0.5
                # afficher la variable "lastname" des deux joueurs opposés
                print(array_player1[i], "  VS  ", array_player2[i], "                             ",
                      nbr_score5, "  ", nbr_score6)

                # enregistrer variables players[] et nbr_sore dans la liste player_score sous forme de tuple
                player_score2.append((array_player1[i], nbr_score5))
                player_score2.append((array_player2[i], nbr_score6))
            if nbr_score5 > nbr_score6:
                print(array_player1[i], "VS", array_player2[i], "                                 ",
                      nbr_score5, "  ", nbr_score6)
                print(array_player1[i], "WON")
                player_score2.append((array_player1[i], nbr_score5))
                player_score2.append((array_player2[i], nbr_score6))
                print()
                print()
            if nbr_score5 < nbr_score6:
                print(array_player1[i], "VS", array_player2[i], "                                 ",
                      nbr_score5, "  ", nbr_score6)
                print(array_player1[i], "LOST")
                player_score2.append((array_player1[i], nbr_score5))
                player_score2.append((array_player2[i], nbr_score6))
                print()
                print()
        print()
        print()
        print("listing of matches")
        match = player_score2
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
        count = 0
        for i in player_score2:
            count = count + 1
            print(i)
        print()
        print()
        print()
        print()
        for i in range(0, 8):
            for j in range(0, 1):
                total_scores = player_score[i][1] + player_score2[i][1]
                print()
                print("", "player  | score1", "|", "score2  | total score")
                print("", "--------------------------------------------------------------------------------")
                for nombre in range(1):
                    print("  ", player_score[i][0], "    |", " ", player_score[i][1], " |", "  ", player_score2[i][1],
                          " ",  "", "|        "
                          , total_scores, "")
                    print("", "------------------------------------------------------------------------------")

        print()
        print()
        print("________________new classement____________________")
        print()
        for i in range(8):
            print(players[i]["lastname"] ,"=>" ,players[i]["rank" ] +player_score[i][1 ] +player_score2[i][1])
        print()
        print()
        print()



        print("++++++++++++++++++++++++++++++++++   ROUND3   +++++++++++++++++++++++++++++++++++++++++++++++")
        print()
        print()
        print()
        print()
        # nouvelles variables
        player_score3 = []
        array_player3 = []
        array_player4 = []
        update_rawk2 = []
        scores = [0,1]
        # on enregistre la position des premiers joueurs
        for i in range(1, 5):
            array_player3.append(players[(i * 2) - 1]["lastname"])
        # on enregistre la position des adversaires
        for i in range(4):
            array_player4.append(players[i * 2]["lastname"])
        print()
        print()

        # demarrage des matchs
        for i in range(4):
            print()
            print()
            print("      MATCH  ", i + 1, "                            SCORE  ", i + 1, "                           \n")
            print()
            print()
            # choisir en mode aléatoire le score
            nbr_score6 = secrets.choice(scores)
            nbr_score7 = secrets.choice(scores)
            if nbr_score6 == nbr_score7:
                print("EGALITY")
                print("each player receives 0.5 points")
                nbr_score6 = 0.5
                nbr_score7 = 0.5
                # afficher la variable "lastname" des deux joueurs opposés
                print(array_player3[i], "  VS  ", array_player4[i], "                             ",
                      nbr_score6, "  ", nbr_score7)

                # enregistrer variables players[] et nbr_sore dans la liste player_score sous forme de tuple
                player_score3.append((array_player3[i], nbr_score6))
                player_score3.append((array_player4[i], nbr_score7))
            if nbr_score6 > nbr_score7:
                print(array_player3[i], "VS", array_player4[i], "                                 ",
                      nbr_score6, "  ", nbr_score7)
                print(array_player3[i], "WON")
                player_score3.append((array_player3[i], nbr_score6))
                player_score3.append((array_player4[i], nbr_score7))
                print()
                print()
            if nbr_score6 < nbr_score7:
                print(array_player3[i], "VS", array_player4[i], "                                 ",
                      nbr_score6, "  ", nbr_score7)
                print(array_player3[i], "LOST")
                player_score3.append((array_player3[i], nbr_score6))
                player_score3.append((array_player4[i], nbr_score7))
                print()
                print()

        print()
        print()
        print("listing of matches")
        match2 = player_score3
        matches2 = list(x for t in match2 for x in t)
        length_to_split2 = [len(matches2) // 4] * 4
        lst2 = iter(matches2)
        match_player_score2 = [list(islice(lst2, elem))
                               for elem in length_to_split2]
        print("     MATCH1          MATCH2           MATCH3             MATCH4   ")
        print(match_player_score2)
        print()
        print()

        print()
        print("list of players with total points")
        print()
        print()
        count = 0
        for i in player_score3:
            count = count + 1
            print(i)
        print()
        print()
        print()
        print()
        for i in range(0, 8):
            for j in range(0, 1):
                total_scores = player_score[i][1] + player_score2[i][1] + player_score3[i][1]
                print()
                print("", "player  | score1", "|", "score2  | score3", "", " total score")
                print("", "--------------------------------------------------")
                for nombre in range(1):
                    print("  ", player_score[i][0], "    |", " ", player_score[i][1], " |", "  ", player_score2[i][1],
                          " ", "| ", player_score3[i][1], "  ", "", "|        "
                          , total_scores, "")
                    print("", "------------------------------------------------")

        print()
        print()
        print("________________new classement____________________")
        print()
        for i in range(8):
            print(players[i]["lastname"], "=>", players[i]["rank"] + player_score[i][1] + player_score2[i][1] + player_score3[i][1])
        print()
        print()
        print()
        print()
        print()
        print("++++++++++++++++++++++++++++++++++   ROUND4   +++++++++++++++++++++++++++++++++++++++++++++++")
        print()
        print()
        print()
        print()
        # nouvelles variables
        player_score4 = []
        array_player5 = []
        array_player6 = []
        update_rawk3 = []
        scores = [0, 1]
        # on enregistre la position des premiers joueurs
        for i in range(1, 5):
            array_player5.append(players[(i * 2) - 1]["lastname"])
        # on enregistre la position des adversaires
        for i in range(4):
            array_player6.append(players[i * 2]["lastname"])
        print()
        print()

        # demarrage des matchs
        for i in range(4):
            print()
            print()
            print("      MATCH  ", i + 1, "                            SCORE  ", i + 1, "                           \n")
            print()
            print()
            # choisir en mode aléatoire le score
            nbr_score6 = secrets.choice(scores)
            nbr_score7 = secrets.choice(scores)
            if nbr_score6 == nbr_score7:
                print("EGALITY")
                print("each player receives 0.5 points")
                nbr_score6 = 0.5
                nbr_score7 = 0.5
                # afficher la variable "lastname" des deux joueurs opposés
                print(array_player5[i], "  VS  ", array_player6[i], "                             ",
                      nbr_score6, "  ", nbr_score7)

                # enregistrer variables players[] et nbr_sore dans la liste player_score sous forme de tuple
                player_score4.append((array_player5[i], nbr_score6))
                player_score4.append((array_player6[i], nbr_score7))
            if nbr_score6 > nbr_score7:
                print(array_player5[i], "VS", array_player6[i], "                                 ",
                      nbr_score6, "  ", nbr_score7)
                print(array_player5[i], "WON")
                player_score4.append((array_player5[i], nbr_score6))
                player_score4.append((array_player6[i], nbr_score7))
                print()
                print()
            if nbr_score6 < nbr_score7:
                print(array_player5[i], "VS", array_player6[i], "                                 ",
                      nbr_score6, "  ", nbr_score7)
                print(array_player5[i], "LOST")
                player_score4.append((array_player5[i], nbr_score6))
                player_score4.append((array_player6[i], nbr_score7))
                print()
                print()

        print()
        print()
        print("listing of matches")
        match4 = player_score4
        matches4 = list(x for t in match4 for x in t)
        length_to_split4 = [len(matches4) // 4] * 4
        lst4 = iter(matches4)
        match_player_score4 = [list(islice(lst4, elem))
                               for elem in length_to_split4]
        print("     MATCH1          MATCH2           MATCH3             MATCH4   ")
        print(match_player_score4)
        print()
        print()

        print()
        print("list of players with total points")
        print()
        print()
        count = 0
        for i in player_score4:
            count = count + 1
            print(i)
        print()
        print()
        print()
        print()
        for i in range(0, 8):
            for j in range(0, 1):
                total_scores = player_score[i][1] + player_score2[i][1] + player_score3[i][1]+ player_score4[i][1]
                print()
                print("", "player  | score1", "|", "score2  | score3", "|","score4 | total score")
                print("", "--------------------------------------------------")
                for nombre in range(1):
                    print("  ", player_score[i][0], "    |", " ", player_score[i][1], " |", "  ", player_score2[i][1],
                          " ", "| ", player_score3[i][1], "  ", "     ", "| ",player_score4[i][1]
                          , total_scores, "")
                    print("", "------------------------------------------------")

        print()
        print()
        print("________________new classement____________________")
        print()
        for i in range(8):
            print(players[i]["lastname"], "=>",
                  players[i]["rank"] + player_score[i][1] + player_score2[i][1] + player_score3[i][1]+ player_score4[i][1])
        print()
        return player_score, player_score2, player_score3, player_score4

