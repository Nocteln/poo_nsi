import perso


def select_perso(joueur):
    if joueur == "1":
        joueur = perso.Chevalier(15, 10, 3)
    elif joueur == "2":
        joueur = perso.Sorcier(15, 10, 3, 5)
    elif joueur == "3":
        joueur = perso.Elfe(15, 10, 3)
    else:
        print("Veuillez choisir un personnage valide")
        joueur = input("1,2 ou 3 : ")
    return joueur