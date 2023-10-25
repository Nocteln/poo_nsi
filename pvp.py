import random

class Joueur:
    def __init__(self, nom, pv_max, nb_potions):
        self.nom = nom
        self.pv_max = pv_max
        self.pv = pv_max
        self.nb_potions = nb_potions

    def attaquer(self, cible):
        degats = random.randint(5, 10)
        cible.pv -= degats
        print(f"{self.nom} attaque et inflige {degats} points de dégâts à {cible.nom}.")
        print(f"{cible.nom} a maintenant {cible.pv} points de vie restants.")

    def utiliser_potion(self):
        if self.nb_potions == 0:
            print(f"{self.nom}, vous n'avez plus de potion.")
        else:
            potion_soin = random.randint(15, 40)
            self.pv += potion_soin
            if self.pv > self.pv_max:
                self.pv = self.pv_max
            self.nb_potions -= 1
            print(f"{self.nom} utilise une potion et récupère {potion_soin} points de vie.")
            print(f"{self.nom} a maintenant {self.pv} points de vie.")

def pvp():
    joueur1 = Joueur(input("Quel est le nom du premier joueur? "), 40, 3)
    joueur2 = Joueur(input("Quel est le nom du second joueur? "), 40, 3)

    current_player = joueur1  # Le joueur 1 commence

    while joueur1.pv > 0 and joueur2.pv > 0:
        print(f"{current_player.nom}, c'est à votre tour.")
        user_choices = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
        user_choices = int(user_choices)

        if user_choices != 1 and user_choices != 2:
            print("Veuillez entrer un nombre valide (1 ou 2).")
            continue

        if user_choices == 1:
            current_player.attaquer(joueur1 if current_player == joueur2 else joueur2)
        elif user_choices == 2:
            current_player.utiliser_potion()

        # Changement de joueur
        current_player = joueur1 if current_player == joueur2 else joueur2

    # Affichage du résultat
    if joueur1.pv <= 0:
        print(f"{joueur1.nom} n'a plus de points de vie. {joueur2.nom} remporte la partie!")
    else:
        print(f"{joueur2.nom} n'a plus de points de vie. {joueur1.nom} remporte la partie!")


