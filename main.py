import perso

print("Choisisez votre personnage : \n1. Chevalier\n2. Sorcier\n3. Elfe")
joueur = input("1,2 ou 3 : ")

if joueur == "1":
    joueur = perso.Chevalier(15, 10, 3)
elif joueur == "2":
    joueur = perso.Sorcier(15, 10, 3, 5)
elif joueur == "3":
    joueur = perso.Elfe(15, 10 ,3)
else:
    print("Veuillez choisir un personnage valide")
    joueur = input("1,2 ou 3 : ")

troll = perso.Troll(15, 3)
vampire = perso.Vampire(7, 2)
loupGarou = perso.LoupGarou(10, 2)

while joueur.vie > 0:
    pass

