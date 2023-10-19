import perso
import random

nb_degats = random.randint(1, 4)

print("Choisisez votre personnage : \n1. Chevalier\n2. Sorcier\n3. Elfe")
joueur = input("1,2 ou 3 : ")

if joueur == "1":
    joueur = perso.Chevalier(15, 10, 3)
elif joueur == "2":
    joueur = perso.Sorcier(15, 10, 3, 5)
elif joueur == "3":
    joueur = perso.Elfe(15, 10 ,3)
else:
    print("Veuillez choisir un personnage valide")
    joueur = input("1,2 ou 3 : ")

troll = perso.Troll(15, nb_degats)
vampire = perso.Vampire(7, nb_degats)
loupGarou = perso.LoupGarou(10, nb_degats)


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
        ennemi_choisi = random.choice([troll, vampire, loupGarou])

        joueur.attaquer(ennemi_choisi, nb_degats)
        print(f"Vous infligez {nb_degats} points de dégâts à {ennemi_choisi.__class__.__name__}.")

        if ennemi_choisi.vie <= 0:
            print(f"{ennemi_choisi.__class__.__name__} a été vaincu !")
        else:
            print(f"{ennemi_choisi.__class__.__name__} a maintenant {ennemi_choisi.vie} points de vie restants.")
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

    # Tour de l'ennemi
    ennemi_choisi = random.choice([troll, vampire, loupGarou])

    ennemi_choisi.attaquer(joueur)
    print(f"{ennemi_choisi.__class__.__name__} vous inflige {nb_degats} points de dégâts.\nIl vous rest {joueur.vie}pv")

    if joueur.vie <= 0:
        print("Vous avez été vaincu par l'ennemi.")
        break  # La boucle s'arrête si le joueur perd
    elif troll.vie == 0 and vampire.vie == 0 and loupGarou.vie == 0:
        print("Vous avez gagné")
    print("\n\n")

print("Fin du jeu. Merci d'avoir joué !")

