import perso

# definition de la classe enfant de Mob

class Troll(perso.Mob):
    def __init__(self, vie, nb_degats):
        super().__init__(vie, nb_degats)
