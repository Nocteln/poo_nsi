import perso

def select_perso(default_perso):
    while True:  # tourne tant que le joueur n'as pas choisi son personnage
        print("Choisisez votre personnage : \n1. Chevalier\n2. Sorcier\n3. Elfe")
        joueur = input("1, 2 ou 3 : ")

        if joueur == "1":
            joueur = perso.Chevalier(input("Comment vous appelez vous : "),default_perso[0], 10, default_perso[2])
            break  # On sort de la boucle si le choix est valide
        elif joueur == "2":
            joueur = perso.Sorcier(input("Comment vous appelez vous : "), default_perso[0], 10, default_perso[2], default_perso[1])
            break  # On sort de la boucle si le choix est valide
        elif joueur == "3":
            joueur = perso.Elfe(input("Comment vous appelez vous : "), default_perso[0], 10, default_perso[2])
            break  # On sort de la boucle si le choix est valide
        else:
            print("\nChoisissez un chiffre valide\n")

    return joueur
