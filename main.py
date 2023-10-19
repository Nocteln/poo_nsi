import perso
import random
import histoire



print("Choisisez votre personnage : \n1. Chevalier\n2. Sorcier\n3. Elfe")
joueur = input("1,2 ou 3 : ")

joueur = histoire.select_perso(joueur)


nb_degats_joueur = random.randint(1, 4)
nb_degats_mob = random.randint(0,3)



troll = perso.Troll(5, nb_degats_mob)
vampire = perso.Vampire(5, nb_degats_mob)
loupGarou = perso.LoupGarou(5, nb_degats_mob)


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
       mob = histoire.attaque(joueur, [troll,vampire,loupGarou], nb_degats_joueur, nb_degats_mob)
    elif choix == "2" and isinstance(joueur, perso.Sorcier):
        histoire.soigner(joueur)
    elif choix == "3" and joueur.nb_viande > 0:
        joueur.nb_viande -= 1
        joueur.manger()
        print(f"Vous mangez de la viande et avez maintenant {joueur.vie} points de vie.\nIl vous reste {joueur.nb_viande} viande")
    else:
        print("Choix invalide. Veuillez choisir une option valide.")


    if joueur.vie <= 0:
        print("Vous avez été vaincu par l'ennemi.")
        break  # La boucle s'arrête si le joueur perd
    elif troll.vie <= 0 and vampire.vie <= 0 and loupGarou.vie <= 0:
        print("Vous avez gagné")
        break
    print("\n\n")
