import perso


def select_perso(defalut_perso):
    print("Choisisez votre personnage : \n1. Chevalier\n2. Sorcier\n3. Elfe")
    joueur = input("1,2 ou 3 : ")

    if joueur == "1":
        joueur = perso.Chevalier(defalut_perso[0], 10, defalut_perso[2])
    elif joueur == "2":
        joueur = perso.Sorcier(defalut_perso[0], 10, defalut_perso[2], defalut_perso[1])
    elif joueur == "3":
        joueur = perso.Elfe(defalut_perso[0], 10, defalut_perso[2])
    else:
        print("Veuillez choisir un personnage valide")
        joueur = input("1,2 ou 3 : ")
    return joueur