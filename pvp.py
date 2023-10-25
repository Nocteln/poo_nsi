import random
userpv = 50
ennemipv = 50
nb_potions = 3
premierj = ""
ennemy_name = ""

def pvp():
    premierj = input("Quel est le nom du premier joueur? ? ")
    secondj = input("Quel est le nom du second joueur? ? ")

    while userpv > 0 and ennemipv > 0:
        user_choices = input(
            "Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
        user_choices = int(user_choices)
        if user_choices != 1 and user_choices != 2:
            print("Veuillez entrer un nombre valide. 1 ou 2")
            continue

        if user_choices == 1:
            ennemipv = ennemipv - random.randint(5, 10)
            if ennemipv < 1:
                print(f"{secondj} est mort, vous avez gagné")
                break
            else:
                print(f"{secondj} n'a plus que {ennemipv} pv. ⚔️")

        elif user_choices == 2:
            if userpv == 50:
                print(
                    f"{premierj} Vous ne pouvez pas vous rajouter de la potion, vous avez 50 pv.")
            elif nb_potions == 0:
                print(f"{premierj} Vous n'avez plus de potion")
                continue
            else:
                nb_potions = nb_potions - 1
                userpv = userpv + random.randint(15, 50)
                if userpv > 50:
                    userpv = 50
                    print(f"{premierj} Vous avez maintenant {userpv} points de vie")
        # attaque de l'ennemi
        userpv = userpv - random.randint(5, 15)
        if userpv < 1:
            print(f"{premierj} Vous avez perdu, {secondj} a triomphé.")
            break
        else:
            print(
                f"{ennemy_name} a attaqué, {premierj} vous n'avez plus que {userpv} points de vie. ⚔️")
