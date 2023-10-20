import perso


class LoupGarou(perso.Mob):
    def __init__(self, vie, nb_degats):
        super().__init__(vie, nb_degats)