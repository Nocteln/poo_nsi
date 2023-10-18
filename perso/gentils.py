import perso


class Chevalier(perso.Personnage):
    def __init__(self, vie, faim, nb_viande):
        super().__init__(vie, faim, nb_viande)


class Elfe(perso.Personnage):
    def __init__(self, vie, faim, nb_viande):
        super().__init__(vie, faim, nb_viande)


class Sorcier(perso.Personnage):
    def __init__(self, vie, faim, nb_viande, nb_potion):
        super().__init__(vie, faim, nb_viande)
        self.nb_potion = nb_potion

    def soigne(self):
        if self.nb_potion > 1 and self.vie < 10:
            self.vie += 1
            self.nb_potion -= 1
