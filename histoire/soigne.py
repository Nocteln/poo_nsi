


def soigner(joueur):
    if joueur.nb_potion == 0:
        print("Vous n'avez plus de potion.")
    else:
        joueur.nb_potion -= 1
        joueur.soigne()
        print(
            f"Vous vous soignez et avez maintenant {joueur.vie} points de vie.\nIl vous reste {joueur.nb_potion} potion")
