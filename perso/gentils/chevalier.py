import perso

# definition de la classe enfant de Personnage
class Chevalier(perso.Personnage):
    def __init__(self, vie, faim, nb_viande):
        super().__init__(vie, faim, nb_viande)
