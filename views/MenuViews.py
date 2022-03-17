import sys
import time


class MenuView:
    def run(self):
        """Creation menu"""
        print()
        print()
        print("CHESS TOURNAMENT                    ")
        print()
        message = " CREATE A NEW PLAYER ~~~~~~~~~\n " \
                  "                                \n " \
                  "1   create a new players        \n " \
                  "2      update-players           \n " \
                  "3      report players           \n " \
                  "                                \n" \
                  "                                \n" \
                  "                                \n" \
                  "CREATE A TOURNAMENT ~~~~~~~~~~\n " \
                  "                                \n " \
                  "4 create a new tournament       \n " \
                  "5   report tournaments          \n " \
                  "6         exit                  \n" \
                  "                                \n" \
                  "                                 \n" \
                  " ENTER THE NUMBER ONE TO START ~~\n" \
                  "or enter the number 7 to quit    "
        time.sleep(0.01)
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print()
        print()
        print()
        started = input("ENTER A NUMBER TO START      =>: ")
        time.sleep(0.01)
        return started


class PlayerView:

    def create_new_player(self):
        """creation new player"""
        player = {}
        print()
        print()
        player = {
            "lastname": input("lastname?:  "),
            "firstname": input("firstname?:  "),
            "age": input("age?:  "),
            "birthdate": input("birthdate?:  "),
        }
        return player

    def verification_rank(self, player):
        """force the user to enter a number less than 100"""
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
        player['ranking'] = rank
        print(player)
        return player


class TournamentView:
    def reference_report(self, players):
        """information request spins"""
        print()
        ref_tournament = {'name_tournament': input("name tournament??:  "),
                          'location_tournament': input("location_tournament??:  "),
                          'date_tournament': input("date_tournament??:  "),
                          'description_tournament': input("description_tournament:  "),
                          'control_time': input("bullet or blitz ou un coup rapide??:  "),
                          'player': players}
        print()
        print()
        return ref_tournament

    def run(self, players):
        """listing players in descending ranking mode"""
        print()
        print()
        print("THE TOURNAMENT BEGINS  -------------------------------------\n")
        print()
        print()
        print()
        print("LISTING OF PLAYERS ACCORDING TO THEIR RANKING-----------------------------------\n")
        print()
        print("in descending order                      ")
        print()
        def rank(e):
            return e['ranking']

        players.sort(reverse=True, key=rank)
        count = 0
        for i in players:
            count = count + 1
            print("player", count, i)
        return players

    def split_list(self, players):
        """creation of 2 groups of players"""
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
        """match and scores"""
        info_winners = []
        info_scores = []
        for i in range(4):
            print()
            print()
            print("      MATCH  ", i + 1, "                                                    \n")
            print()
            print()
            print(players[i]['lastname'], "    VS    ", players[i + 4]['lastname'])
            print()
            number_winner = input("which is the winner (type 1 for player 1 or 2 for player 2 or 3 for egality):  ")
            score_winner = input("which score(1 for winner or 0.5 for egality):  ")
            if number_winner == "1":
                number_winner = players[int(number_winner) - 1]['lastname']
                print(number_winner)
            if number_winner == "2":
                number_winner = players[int(number_winner) + 2]['lastname']
                print(number_winner)
