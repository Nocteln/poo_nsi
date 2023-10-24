import random


def pvp():
    user1pv = 40
    user2pv = 40
    nb_potions = 3
    premierj = input("Quel est le nom du premier joueur? ? ")
    secondj = input("Quel est le nom du second joueur? ? ")

    while user1pv > 0 and user2pv > 0:
        user_choices = input(
            "Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
        user_choices = int(user_choices)
        if user_choices != 1 and user_choices != 2:
            print("Veuillez entrer un nombre valide. 1 ou 2")
            continue

        if user_choices == 1:
            user2pv = user2pv - random.randint(5, 10)
            if user2pv < 1:
                print(f"{secondj} est mort, vous avez gagné")
                break
            else:
                print(f"{secondj} n'a plus que {user2pv} pv. ⚔️")

        elif user_choices == 2:
            if user1pv == 50:
                print(
                    f"{premierj} Vous ne pouvez pas vous rajouter de la potion, vous avez 50 pv.")
            elif nb_potions == 0:
                print(f"{premierj} Vous n'avez plus de potion")
                continue
            else:
                nb_potions = nb_potions - 1
                user1pv = user1pv + random.randint(15, 50)
                if user1pv > 50:
                    user1pv = 50
                    print(f"{premierj} Vous avez maintenant {user1pv} points de vie")
        # attaque de l'ennemi
        user1pv = user1pv - random.randint(5, 15)
        if user1pv < 1:
            print(f"{premierj} Vous avez perdu, {secondj} a triomphé.")
            break
        else:
            print(
                f"{secondj} a attaqué, {premierj} vous n'avez plus que {user1pv} points de vie. ⚔️")
