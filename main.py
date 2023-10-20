import perso
import random
import histoire


# definir le nombre de dégats que les mobs mettent
degats_mob_min = 0
degats_mob_max = 3
vie_mob_min = 5
vie_mob_max =  50


nb_degats_joueur = random.randint(degats_mob_min+1, degats_mob_max+1) #definir le nombre de dégats que le joueur met

default_vie = 10
default_nb_viande = 3
default_nb_potion = 3
default_joueur = [default_vie, default_nb_potion, default_nb_viande]




troll = perso.Troll( random.randint(vie_mob_min, vie_mob_max),  random.randint(degats_mob_min, degats_mob_max))
vampire = perso.Vampire( random.randint(vie_mob_min, vie_mob_max),  random.randint(degats_mob_min, degats_mob_max))
loupGarou = perso.LoupGarou( random.randint(vie_mob_min, vie_mob_max),  random.randint(degats_mob_min, degats_mob_max))
mob = [troll, vampire, loupGarou]

choix_debut = ""

while choix_debut != "1":
    print("\n----La Quête des Légendes | Menu ----")
    print("1. Lancer le jeu\n2. Paramètres du jeu")
    choix_debut = input("Saisissez votre choix : ")

    if choix_debut == "2":
        # Fonction pour modifier les points de vie
        default_joueur = histoire.parametres([default_vie, default_nb_potion, default_nb_viande])


print("\n\nBonjours, Bienvenue dans La Quête des Légendes!\nPrépare toi à entrer dans un monde mysterieux plein de mystère\nDurant ton aventure, tu devra affronter de multiples danger et faire fasse à tout types d'épreuves! \nTient toi prêt, cela va commencer")

print("Commencons par choisir votre Joueur !\n")

joueur = histoire.select_perso([default_vie, default_nb_potion, default_nb_viande])

joueur.vie = default_joueur[0]
joueur.nb_viande = default_joueur[2]
if isinstance(joueur, perso.Sorcier):
    joueur.nb_potion = default_joueur[1]
print(joueur.vie)

print("\r\r")
while joueur.vie > 0:
    # Tour du joueur
    print(f"{joueur.nom}, que souhaitez-vous faire?")
    print("1. Attaquer")
    print("2. Manger (si vous avez de la viande)")
    if isinstance(joueur, perso.Sorcier):
        print("3. Se soigner (pour les sorciers)")

    if isinstance(joueur, perso.Sorcier):
        choix = input("Saisissez 1, 2 ou 3 : ")
    else:
        choix = input("Saisissez 1 ou 2 : ")
    print("\n\n")

    if choix == "1":
       mob = histoire.attaque(joueur, mob, nb_degats_joueur, nb_degats_mob)
    elif choix == "2" and joueur.nb_viande > 0:
        joueur.nb_viande -= 1
        joueur.manger()
        print(f"Vous mangez de la viande et avez maintenant {joueur.vie} points de vie.\nIl vous reste {joueur.nb_viande} viande")
    elif choix == "3" and isinstance(joueur, perso.Sorcier):
        histoire.soigner(joueur)
    else:
        print("Choix invalide. Veuillez choisir une option valide.")


    if joueur.vie <= 0:
        print("Vous avez été vaincu par l'ennemi.")
        break  # La boucle s'arrête si le joueur perd
    elif len(mob)==0:
        print("Vous avez gagné")
        break

    if choix != "2":
        joueur.faim -= 0.5
        if (joueur.faim <= 4):
            print(f"Attention, vous commencez à avoir faim ({joueur.faim}/10)")
        if (joueur.faim <= 2):
            print(f"Vous avez tellement faim que vous perdez {default_joueur[0] / 20} points de vie")
            joueur.vie -= default_joueur[0] / 20
    print("\n\n")
