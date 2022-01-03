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
            sex = input("sex m/f? : ")
            age = input("age? : ")
            rank = input("rank /10? : ")
            print()
            print("player identity {}".format(counts + 1))
            print()


        def createList(name, n):
            result = {}
            for i in range(n):
                nameList = name + str(i + 1)
                result[nameList] = []
            return result

        res = createList("liste", 5)  # création de 5 listes dont le nom commence par list

        for i in range(5):
            res["liste" + str(i + 1)].extend([2, 4])  # on ajoute 2 à list3

        print(res)  # {'list1': [], 'list5': [], 'list2': [], 'list4': [], 'list3': [2]}


class TournamentView:
    def run(self):
        pass


class LeaveView:
    def run(self):
        sys.exit()
