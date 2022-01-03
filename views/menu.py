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

            print()
            print("the player number {}".format(counts + 1))
            print()
            lastname = ""
            while lastname == "":
                lastname = input("lastname? : ")

            firstname = ""
            while firstname == "":
                firstname = input("firstname? : ")

            birth_date = input("birth_date? : ")

            sex = ""
            while sex != "m" or sex !="f":
                sex = input("sex m/f? : ")

            age = input("age? : ")
            try:
                age = int(age)
            except ValueError:
                sys.exit("you must enter an integer")
            rank = input("rank /10? : ")


class TournamentView:
    def run(self):
        pass


class LeaveView:
    def run(self):
        sys.exit()
