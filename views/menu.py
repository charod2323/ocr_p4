import sys


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

        numberplayers = input("how many players ??:  ")
        try:
            numberplayers = int(numberplayers)
        except ValueError:
            sys.exit("you must enter an integer")

        for counts in range(numberplayers):
            i=0
            player = "player"
            print()
            print("the player number {}".format(counts + 1))
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
            print("player identity {}".format(counts + 1))
            print()
            print(lastname.center(100))
            print(firstname.center(100))
            print(birth_date.center(100))
            print(birth_month.center(100))
            print(birth_year.center(100))
            print(sex.center(100))
            print(age.center(100))
            print(rank.center(100))


            def createList(name, n):
                result = {}
                for i in range(n):
                    nameList = name + str(i + 1)
                    result[nameList] = []
                return result

            res = createList("player", numberplayers)

            for i in range(numberplayers):
                res["player" + str(i + 1)].extend([lastname,firstname])

            print(res)


class TournamentView:
    def run(self):
        pass


class LeaveView:
    def run(self):
        sys.exit()
