import perso

def pvp():
    joueur1 = perso.Joueur(input("Quel est le nom du premier joueur? "), 40, 3)
    joueur2 = perso.Joueur(input("Quel est le nom du second joueur? "), 40, 3)

    current_player = joueur1  # Le joueur 1 commence

    while joueur1.pv > 0 and joueur2.pv > 0:
        print(f"{current_player.nom}, c'est à votre tour.")
        user_choices = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

        if user_choices not in ["1", "2"]:
            print("Veuillez entrer un choix valide (1 ou 2).")
            continue

        user_choices = int(user_choices)

        if user_choices == 1:
            current_player.attaquer(joueur1 if current_player == joueur2 else joueur2)
        elif user_choices == 2:
            current_player.utiliser_potion()

        # Changement de joueur
        current_player = joueur1 if current_player == joueur2 else joueur2

    # Affichage du résultat
    if joueur1.pv <= 0:
        print(f"{joueur1.nom} n'a plus de points de vie. {joueur2.nom} remporte la partie!")
    else:
        print(f"{joueur2.nom} n'a plus de points de vie. {joueur1.nom} remporte la partie!")

# Appel de la fonction pour lancer le PvP
pvp()
