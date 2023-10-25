import random

class Personnage:
    def __init__(self, vie, faim, nb_viande):
        self.vie = vie
        self.faim = faim
        self.nom = input("Comment vous appelez vous : ")
        self.nb_viande = nb_viande

    def attaquer(self, mobs):
        cible = random.choice(mobs)
        degats = random.randint(5, 10)
        cible.vie -= degats
        print(f"{self.nom} attaque et inflige {degats} points de dégâts à {cible.__class__.__name__}.")
        if cible.vie > 0:
            print(f"{cible.__class__.__name__} a maintenant {cible.vie} points de vie restants.")
        else:
            print(f"Vous avez battu {cible.__class__.__name__}")
        self.faim -= 1
        return mobs
    def manger(self):
        if self.faim < 10 and self.nb_viande > 1:
            self.faim+=3
            self.nb_viande -= 1
            print(f"Vous mangez de la viande et avez maintenant {self.faim} points de faim.\nIl vous reste {self.nb_viande} viande")
        else:
            print("Vous n'avez pas faim!")


class Mob():
    def __init__(self, vie, nb_degats):
        self.vie = vie
        self.nb_degats = nb_degats

    def attaquer(self, cible):
        cible.vie -= self.nb_degats
        print(f"{self.__class__.__name__} attaque et inflige {self.nb_degats} points de dégâts à {cible.nom}.")
        print(f"Il vous reste maintenant {cible.vie} points de vie restants.")


# Pour le pvp
class Joueur:
    def __init__(self, nom, pv_max, nb_potions):
        self.nom = nom
        self.pv_max = pv_max
        self.pv = pv_max
        self.nb_potions = nb_potions

    def attaquer(self, cible):
        degats = random.randint(5, 10)
        cible.pv -= degats
        print(f"{self.nom} attaque et inflige {degats} points de dégâts à {cible.nom}.")
        print(f"{cible.nom} a maintenant {cible.pv} points de vie restants.")

    def utiliser_potion(self):
        if self.nb_potions == 0:
            print(f"{self.nom}, vous n'avez plus de potion.")
        else:
            potion_soin = random.randint(15, 40)
            self.pv += potion_soin
            if self.pv > self.pv_max:
                self.pv = self.pv_max
            self.nb_potions -= 1
            print(f"{self.nom} utilise une potion et récupère {potion_soin} points de vie.")
            print(f"{self.nom} a maintenant {self.pv} points de vie.")
