import sys
import time


class MenuView:
    def run(self):
        print("                                CREATE A PLAYER                                 ")
        print("                                                                                ")
        print("                           1  create a new players                              ")
        print("                           2  classification update                             ")
        print("                           3       report                                       ")
        print("                           4    return choice 1                                 ")
        print("                           5         quit                                       ")
        print("                                                                                ")
        print("                                CREATE A TOURNAMENT                             ")
        print("                                                                                ")
        print("                          6  create a new tournament                            ")
        print("                          7         report                                      ")
        print("                          8     return choice 4                                 ")
        print("                          9          quit                                       ")
        print("                                                                                ")

        choice = input("Enter your choice:  ")
        return choice


class PlayerView:

    def run(self):

        numberplayers = input("how many players (8 by default)??:  ")
        try:
            numberplayers = int(numberplayers)
        except ValueError:
            sys.exit("you must enter an integer")

        i = 0
        while numberplayers != 8:
            i = i + 1
            player = "player"
            print()
            print("the player number {}".format(i + 1))
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
            print("player{}".format(i + 1), "identity")
            print()
            print("lastname => ", lastname)
            print("firstname => ", firstname)
            print("birth_date => ", birth_date)
            print("birth_month => ", birth_month)
            print("birth_year => ", birth_year)
            print("sex => ", sex)
            print("age =>", age)
            print("rank =>", rank)

            def createList(name, n):
                result = {}
                for i in range(n):
                    nameList = name + str(i + 1)
                    result[nameList] = []
                return result

            res = createList("player", numberplayers)

            res["player" + str(i + 1)].extend(
                [lastname, firstname, birth_date, birth_month, birth_year, sex, age, rank])

            print("data :")
            print(res)


class TournamentView:
    def run(self):
        nbrround = input("how many rounds (4 by default):  ")
        while nbrround != 4:
            print()
            begin_time = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
            print(f"Début du tour : {begin_time}")
            return


class LeaveView:
    def run(self):
        sys.exit()
