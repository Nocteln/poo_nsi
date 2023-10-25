import perso
import random
import histoire
from pvp import pvp
from colorama import Fore, Back, Style, init
init(autoreset=True)

# ****************** Variables **********************

# definir les parametres des mobs
degats_mob_min = 0
degats_mob_max = 3
vie_mob_min = 5
vie_mob_max =  15
nb_degats_mob = random.randint(degats_mob_min, degats_mob_max)

# definir les parametres des joueurs
nb_degats_joueur = random.randint(degats_mob_min+1, degats_mob_max+1)
default_vie = 15
default_nb_viande = 3
default_nb_potion = 3
default_joueur = [default_vie, default_nb_potion, default_nb_viande, nb_degats_joueur]

count = 0  # Compteur du nombre de tours (easter egg)

# Instanciation des Mobs
troll = perso.Troll( random.randint(vie_mob_min, vie_mob_max),  nb_degats_mob+2)
vampire = perso.Vampire( random.randint(vie_mob_min, vie_mob_max),  nb_degats_mob)
loupGarou = perso.LoupGarou( random.randint(vie_mob_min, vie_mob_max),  nb_degats_mob+1)
mob = [troll, vampire, loupGarou]


# ******************* JEU ***************************
choix_debut = ""

while choix_debut != "1": # Tant que la partie n'est pas lancée :
    print("\n----" + Fore.RED +"La Quête des Légendes" + Fore.RESET + "|" + Fore.GREEN + "Menu" + Fore.RESET +"----")
    print("1." + Style.BRIGHT + " Lancer le jeu en solo" + Style.RESET_ALL +"\n2." +  Style.BRIGHT + " Paramètres du jeu" + Style.RESET_ALL +"\n3." +  Style.BRIGHT + " Joueur contres joueurs")
    choix_debut = input("Saisissez votre choix : ") # Recupère le choix de l'utilisateur sur le lancement de la partie

    if choix_debut == "2":
        # Fonction pour modifier certains parametres du jeu
        default_joueur = histoire.parametres(default_joueur)
    elif choix_debut == "3":
        pvp() # Lance un mode pvp


print("\n\nBonjours et bienvenue dans" + Fore.RED +"La Quête des Légendes" + Fore.RESET + "\nPrépare toi à entrer dans un monde mysterieux plein de mystère\nDurant ton aventure, tu devra affronter de multiples danger et faire fasse à tout types d'épreuves! \nTient toi prêt, cela va commencer")

print("Commencons par choisir votre Joueur !\n")

joueur = histoire.select_perso(default_joueur)  # Selection du personnage

# application des parametres modifié
joueur.vie = default_joueur[0]
joueur.nb_viande = default_joueur[2]
if isinstance(joueur, perso.Sorcier):
    joueur.nb_potion = default_joueur[1]
print(joueur.vie)

print("\n\n")
# lancement de la boucle qui va finir lorseque le joueur n'aura plus de vie
while True:
    # Choix du joueur
    print(Fore.CYAN + f"{joueur.nom}" + Fore.RESET + ", que souhaitez-vous faire?")
    print("1." + Style.BRIGHT + " Attaquer")
    print("2." + Style.BRIGHT + " Manger (si vous avez de la viande)")
    if isinstance(joueur, perso.Sorcier): # si le personnage choisi est un sorcier, on lui propose aussi de se soigner
        print("3." + Style.BRIGHT + " Se soigner")

    if isinstance(joueur, perso.Sorcier):
        choix = input("Saisissez 1, 2 ou 3 : ")
    else:
        choix = input("Saisissez 1 ou 2 : ")
    print("\n\n")

    if choix == "1": # == attaquer
        mob = joueur.attaquer(mob)
        if len(mob) == 0:
            print("Vous avez gagné")
            break  # la boucle s'arrête si le joueur gagne car il n'y as plus de mobs

        mob_choisi = random.choice(mob)
        mob_choisi.attaquer(joueur)
    elif choix == "2" and joueur.nb_viande > 0: # == manger
        joueur.manger()
        count += 1

    elif choix == "3" and isinstance(joueur, perso.Sorcier):
        joueur.soigne(default_joueur[0])
        count += 1
    else:
        print("Choix invalide. Veuillez choisir une option valide.")


    if joueur.vie <= 0:
        print("Vous avez été vaincu par l'ennemi.")
        break  # La boucle s'arrête si le joueur perd
    elif len(mob)==0:
        print("Vous avez gagné")
        break  # la boucle s'arrête si le joueur gagne
    elif count >= 3:
        print("\n\nVous avez choisi la voie passive et pour cela les mobs vous remercie en vous laissant passer sans vous déranger\n\nVous avez gagné (fin secrete)")
        break

    if choix != "2":  # si l'on n'est pas en train de manger
        joueur.faim -= 0.5
        if (joueur.faim <= 4 and joueur.faim >=2):
            print(f"Attention, vous commencez à avoir faim ({joueur.faim}/10)")
        elif (joueur.faim <= 2):
            print(f"Vous avez tellement faim que vous perdez {default_joueur[0] / 20} points de vie")
            joueur.vie -= default_joueur[0] / 20
        elif joueur.faim <=0:
            print(f"Vous avez tellement faim que vous perdez {default_joueur[0] / 10} points de vie")
            joueur.vie -= default_joueur[0] / 10

    print("\n\n")
