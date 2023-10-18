import perso

class Chevalier(perso.Personnage):
    def __init__(self, vie, faim, nb_viande):
        super().__init__(vie, faim, nb_viande)


#chev = Chevalier(10,5)
#print(chev.nom)

class Elfe(perso.Personnage):
    pass
class Sorcier(perso.Personnage):
    pass