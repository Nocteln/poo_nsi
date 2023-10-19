import random
class Personnage:
    def __init__(self, vie, faim, nb_viande):
        self.vie = vie
        self.faim = faim
        self.nom = input("Comment vous appelez vous : ")
        self.nb_viande = nb_viande

    def attaquer(self, cible, nb_degats):
        cible.vie -= nb_degats
        self.faim -= 1
    def manger(self):
        if self.faim < 10 and self.nb_viande > 1:
            self.faim+=1
            self.nb_viande -= 1
    def perdreVie(self):
        self.vie -= 1


class Mob():
    def __init__(self, vie, nb_degats):
        self.vie = vie
        self.nb_degats = nb_degats

    def attaquer(self, cible):
        cible.vie -= self.nb_degats