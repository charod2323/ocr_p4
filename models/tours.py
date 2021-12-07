from players import * :


class Tours:
    def __init__(self, nom1_score, nom2_score, date, heure_debut, heure_fin):
        self.nom1_score = nom1_score
        self.nom2_score = nom2_score
        self.date = date
        self.heure_debut = heure_debut
        self.heure_fin = heure_fin

    def show_result(self):
        print(self.nom1_score+" VS "+self.nom2_score)

    def new_tours(Tours):
        """4 tours par default"""

        def __init__(self, nom1_score, nom2_score, date, heure_debut, heure_fin):
            super().__init__(self, nom1_score, nom2_score, date, heure_debut, heure_fin)

            self.compteur_de_matchs = compteur_de_matchs
            if self.compteur_de_matchs > 4:
                print("terminer")

#nombre de tours est de 4 par default
round1 = Tours([p1.lastname , 0],[p2.lastname , 1],[21,7,21],[14],[18])
round2 = Tours([p3.lastname , 0],[p4.lastname , 1],[21,8,21],[14],[18])
round3 = Tours([p5.lastname , 0],[p6.lastname , 0],[21,9,21],[14],[18])
round4 = Tours([p7.lastname , 1],[p8.lastname , 0],[21,10,21],[14],[18])
