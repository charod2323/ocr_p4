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
        print("")

        numberplayers = input("how many players ??:  ")
        try:
            numberplayers = int(numberplayers)
        except ValueError:
            sys.exit("you must enter an integer")

        count = 0




        while count < numberplayers:
            print("")
            print("the player number {}".format(count + 1))
            print("")

            lastname = input("lastname? : ")
            firstname = input("firstname? : ")
            birth_date = input("birth_date? : ")
            sex = input("sex m/f? : ")
            age = input("age? : ")
            rank = input("rank /10? : ")

            def createList(name, n):
                result = {}
                for i in range(n):
                    nameList = name + str(i + 1)
                    result[nameList] = []
                return result

            res = createList("player", 5)
            res["player3"].extend([lastname])
            print(res)



            return


class TournamentView:
    def run(self):
        pass


class LeaveView:
    def run(self):
        sys.exit()
