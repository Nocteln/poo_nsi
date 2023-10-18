from perso.gentils import *


chev = Chevalier(10,5, 5)

elfe = Elfe(10, 7, 6)

chev.attaquer(elfe)
print(chev.faim)
chev.manger()
print(chev.faim)
print(chev.nb_viande)