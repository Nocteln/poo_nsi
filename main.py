import perso
import random
import histoire


print("Choisisez votre personnage : \n1. Chevalier\n2. Sorcier\n3. Elfe")
joueur = input("1,2 ou 3 : ")

joueur = histoire.select_perso(joueur)





print("\r\r")
while joueur.vie > 0:
    # Tour du joueur
    print(f"{joueur.nom}, que souhaitez-vous faire?")
    print("1. Attaquer")
    if isinstance(joueur, perso.Sorcier):
        print("2. Se soigner (pour les sorciers)")
    print("3. Manger (si vous avez de la viande)")

    choix = input("Saisissez 1, 2 ou 3 : ")
    print("\n\n")

    if choix == "1":
       mob = histoire.attaque(joueur)
    elif choix == "2" and isinstance(joueur, perso.Sorcier):
        if joueur.nb_potion == 0:
            print("Vous n'avez plus de potion.")
        else:
            joueur.nb_potion -= 1
            joueur.soigne()
            print(f"Vous vous soignez et avez maintenant {joueur.vie} points de vie.\nIl vous reste {joueur.nb_potion} potion")

    elif choix == "3" and joueur.nb_viande > 0:
        joueur.nb_viande -= 1
        joueur.manger()
        print(f"Vous mangez de la viande et avez maintenant {joueur.vie} points de vie.\nIl vous reste {joueur.nb_viande} viande")
    else:
        print("Choix invalide. Veuillez choisir une option valide.")


    if joueur.vie <= 0:
        print("Vous avez été vaincu par l'ennemi.")
        break  # La boucle s'arrête si le joueur perd
    elif mob[0].vie == 0 and mob[1].vampire.vie == 0 and mob[2].vie == 0:
        print("Vous avez gagné")
    print("\n\n")

print("Fin du jeu. Merci d'avoir joué !")

