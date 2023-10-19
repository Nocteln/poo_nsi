import random
import perso


nb_degats_joueur = random.randint(1, 4)
nb_degats_mob = random.randint(0,3)


troll = perso.Troll(15, nb_degats_mob)
vampire = perso.Vampire(7, nb_degats_mob)
loupGarou = perso.LoupGarou(10, nb_degats_mob)


def attaque(joueur):
    ennemi_choisi = random.choice([troll, vampire, loupGarou])

    joueur.attaquer(ennemi_choisi, nb_degats_joueur)
    print(f"Vous infligez {nb_degats_joueur} points de dégâts à {ennemi_choisi.__class__.__name__}.")

    if ennemi_choisi.vie <= 0:
        print(f"{ennemi_choisi.__class__.__name__} a été vaincu !")
    else:
        print(f"{ennemi_choisi.__class__.__name__} a maintenant {ennemi_choisi.vie} points de vie restants.")

    ennemi_choisi = random.choice([troll, vampire, loupGarou])

    ennemi_choisi.attaquer(joueur)
    print(
        f"{ennemi_choisi.__class__.__name__} vous inflige {nb_degats_mob} points de dégâts.\nIl vous rest {joueur.vie}pv")
    return [troll, vampire, loupGarou]