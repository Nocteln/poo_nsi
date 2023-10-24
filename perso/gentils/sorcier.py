import perso

# definition de la classe enfant de Personnage

class Sorcier(perso.Personnage):
    def __init__(self, vie, faim, nb_viande, nb_potion):
        super().__init__(vie, faim, nb_viande)
        self.nb_potion = nb_potion

    def soigne(self, default_vie):  # Ajout d'une méthode à la classe Sorcier
        if self.nb_potion > 1:
            self.vie += 10
            self.nb_potion -= 1
