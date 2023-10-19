import perso


class Sorcier(perso.Personnage):
    def __init__(self, vie, faim, nb_viande, nb_potion):
        super().__init__(vie, faim, nb_viande)
        self.nb_potion = nb_potion

    def soigne(self):
        if self.nb_potion > 1 and self.vie < 10:
            self.vie += 4
            self.nb_potion -= 1
