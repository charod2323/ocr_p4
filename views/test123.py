"""
print("\t", "Nombre  | Puissance de 2")
print("\t", "------------------------")
for nombre in range(1, 11):
    print("\t","  ", nombre,"\t |"," ",nombre ** 2,"\t\t")
    print("\t", "------------------------")


print("", "Nombre  | Puissance de 2")
print("", "------------------------")
for nombre in range(1):
    print("","  ", nombre," |"," ",nombre ** 2,"")
    print("", "------------------------")

    print('Saisissez un nombre pour continuer, ou 0 pour terminer.')

    nombre = int(input("Saisissez un nombre : "))
    somme = 0

    while nombre != 0:
        somme = somme + nombre
        nombre = int(input("Saisissez un nombre : "))

    print("La somme des nombres que vous avez saisis est de : ", somme)   


on = True
while on:
    print('La boucle est en mode on')
    on = False
print('La boucle est en mode off')
Puisque la condition est True, le bloc de code de la boucle s’exécute la première fois. Mais, dès qu’il arrive à la ligne qui modifie la condition à False, la boucle ne s’exécutera plus et passe à l’instruction suivante.

Ce qui donne :

La boucle est en mode on
La boucle est en mode off

"""

"""
        print()
        print()
        print("listing of matches")
        print()
        print("     MATCH1                 MATCH2                  MATCH3                 MATCH4          ")
        # extraction des éléments dans la liste player_sore pour enregistrer les matchs sous formes de listes
        m = [[0] * 4 for i in range(4)]
        # [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        count = 0
        # player_score contient le nom des joueurs et son score

        m[count][count] = player_score[0][0]
        m[count][count + 1] = player_score[0][1]
        m[count][count + 2] = player_score[1][0]
        m[count][count + 3] = player_score[1][1]
        m[count + 1][count] = player_score[2][0]
        m[count + 1][count + 1] = player_score[2][1]
        m[count + 1][count + 2] = player_score[3][0]
        m[count + 1][count + 3] = player_score[3][1]
        m[count + 2][count] = player_score[4][0]
        m[count + 2][count + 1] = player_score[4][1]
        m[count + 2][count + 2] = player_score[5][0]
        m[count + 2][count + 3] = player_score[5][1]
        m[count + 3][count] = player_score[6][0]
        m[count + 3][count + 1] = player_score[6][1]
        m[count + 3][count + 2] = player_score[7][0]
        m[count + 3][count + 3] = player_score[7][1]
        print(m)
        """