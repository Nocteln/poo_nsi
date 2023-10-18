import perso

print("Choisisez votre personnage : \n1. Chevalier\n2. Sorcier\n3. Elfe")
joueur = input("1,2 ou 3 : ")

if joueur == "1":
    joueur = perso.Chevalier(10, 8, 3)
elif joueur == "2":
    joueur = perso.Sorcier(10, 8, 3, 5)
elif joueur == "3":
    joueur = perso.Elfe(10, 8 ,3)
else:
    print("Veuillez choisir un personnage valide")
    joueur = input("1,2 ou 3 : ")



while joueur.vie > 0:
    pass

