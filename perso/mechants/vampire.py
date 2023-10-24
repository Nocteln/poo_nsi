import perso

# definition de la classe enfant de Mob
class Vampire(perso.Mob):
    def __init__(self, vie, nb_degats):
        super().__init__(vie, nb_degats)
    def attaquer(self, cible):  # Modification de la méthode attaquer de la classe Mob
        self.vie += 1
        cible.vie -= self.nb_degats