import random
import perso







def attaque(joueur, mobs, nb_degats_joueur, nb_degats_mob):
    ennemi_choisi = random.choice(mobs)

    joueur.attaquer(ennemi_choisi, nb_degats_joueur)
    print(f"Vous infligez {nb_degats_joueur} points de dégâts à {ennemi_choisi.__class__.__name__}.")

    if ennemi_choisi.vie <= 0:
        print(f"{ennemi_choisi.__class__.__name__} a été vaincu !")
    else:
        print(f"{ennemi_choisi.__class__.__name__} a maintenant {ennemi_choisi.vie} points de vie restants.")

    if ennemi_choisi.vie >= 0:

        ennemi_choisi.attaquer(joueur)
        print(
            f"{ennemi_choisi.__class__.__name__} vous inflige {nb_degats_mob} points de dégâts.\nIl vous rest {joueur.vie}pv")
        if ennemi_choisi.vie <= 0:
            mobs.remove(ennemi_choisi)