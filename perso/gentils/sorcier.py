import perso

# definition de la classe enfant de Personnage

class Sorcier(perso.Personnage):
    def __init__(self, nom, vie, faim, nb_viande, nb_potion):
        super().__init__(nom, vie, faim, nb_viande)
        self.nb_potion = nb_potion

    def soigne(self, default_vie):  # Ajout d'une méthode à la classe Sorcier
        if self.nb_potion >= 1:
            self.vie += default_vie/5  # Permet de ne pas trop heal
            self.nb_potion -= 1
            print(f"Vous vous soignez et avez maintenant {self.vie} points de vie.\nIl vous reste {self.nb_potion} potion(s)!")
        else:
            print("Vous n'avez plus de potion (dommage😊)")
