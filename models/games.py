from players import * :


class Games:
    def __init__(self,lastname_score1,lastname_score2):
        self.lastname_score1 = lastname_score1
        self.lastname_score2 = lastname_score2

    def show_result(self):
        print(all_match)

unique_match1 = Games([p1.lastname , 0],[p2.lastname , 1])
unique_match2 = Games([p3.lastname , 0],[p4.lastname , 1])
unique_match3 = Games([p5.lastname , 0],[p6.lastname , 0])
unique_match4 = Games([p7.lastname , 1],[p8.lastname , 0])

all_unique_match = (unique_match1,unique_match2,unique_match3,unique_match4)

for all_match in all_unique_match:
    all_match.show_result()
