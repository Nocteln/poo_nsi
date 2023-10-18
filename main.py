from perso.gentils import *

print("Choisisez votre personnage : \n1. Chevalier\n2. Sorcier\n3. Elfe")
perso = input("1,2 ou 3 : ")

if perso == "1":
    perso = Chevalier(10, 8, 3)
elif perso == "2":
    perso = Sorcier(10, 8, 2, 5)
elif perso == "3":
    perso = Elfe(10, 8 ,5)
else:
    print("Veuillez choisir un personnage valide")
    perso = input("1,2 ou 3 : ")

while perso.vie > 0:
    pass

