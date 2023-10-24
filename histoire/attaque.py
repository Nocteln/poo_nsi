import random
import perso



def attaque(joueur, mobs, default_joueur, nb_degats_mob):
    ennemi_choisi = random.choice(mobs) # choisi un mob à attaquer aléatoirement

    joueur.attaquer(ennemi_choisi, default_joueur[3])   # appel de la méthode attaquer
    print(f"Vous infligez { default_joueur[3]} points de dégâts à {ennemi_choisi.__class__.__name__}.")

    if ennemi_choisi.vie <= 0:  # si le mob n'as plus de vie
        print(f"{ennemi_choisi.__class__.__name__} a été vaincu !")
        mobs.remove(ennemi_choisi)
    else:
        print(f"{ennemi_choisi.__class__.__name__} a maintenant {ennemi_choisi.vie} points de vie restants.")
        ennemi_choisi.attaquer(joueur)  # le mob attaque le joueur à son tour s'il a encore de la vie
        print(
            f"{ennemi_choisi.__class__.__name__} vous inflige {nb_degats_mob} points de dégâts.\nIl vous reste {joueur.vie}pv")
    return mobs