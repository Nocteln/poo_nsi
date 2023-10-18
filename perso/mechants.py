import perso

class Troll(perso.Mob):
    def __init__(self, vie, nb_degats):
        super().__init__(vie, nb_degats)


class Vampire(perso.Mob):
    def __init__(self, vie, nb_degats):
        super().__init__(vie, nb_degats)
    def attaquer(self, cible):
        self.vie += 1
        cible.vie -= self.nb_degats


class LoupGarou(perso.Mob):
    def __init__(self, vie, nb_degats):
        super().__init__(vie, nb_degats)