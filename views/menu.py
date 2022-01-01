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

        choice = input("Enter your choice: ")
        return choice






class PlayerView:

    def run(self):
        print("")

        numberplayers = input("how many players??: ")
        try:
            numberplayers = int(numberplayers)
        except ValueError:
            sys.exit("you must enter an integer")

        player_info = []

        count = 0
        results = {}

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
            count = count + 1
            player_info.extend([lastname])

            name = "list"
            numberlist = 0
            i = 0
            n = numberplayers
            for i in range(n):
                nameList = name + str(i + 1)
                results[nameList] = []

                results["list" + str(i + 1 )].append([lastname])  # on ajoute 2 à list3
                print(results)  # {'list1': [], 'list5': [], 'list2': [], 'list4': [], 'list3': [2]}

            return





        return


class TournamentView:
    def run(self):
        pass


class LeaveView:
    def run(self):
        sys.exit()





