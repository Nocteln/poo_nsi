import perso
import random

class Joueur(perso.Personnage):
    def __init__(self, nom, vie, faim, nb_viande, nb_potion):
        super().__init__(vie, faim, nb_viande)
        self.nom = nom  # Assurez-vous que le nom soit correctement attribué
        self.nb_potions = nb_potion

    def utiliser_potion(self):
        if self.nb_potions == 0:
            print(f"{self.nom}, vous n'avez plus de potion.")
        else:
            potion_soin = random.randint(15, 40)
            self.vie += potion_soin
            if self.vie > self.pv_max:  # Vérifiez la valeur correcte des points de vie max
                self.vie = self.pv_max
            self.nb_potions -= 1
            print(f"{self.nom} utilise une potion et récupère {potion_soin} points de vie.")
            print(f"{self.nom} a maintenant {self.vie} points de vie.")  # Utilisez self.vie ici

def pvp():
    joueur1 = Joueur(input("Quel est le nom du premier joueur? "), 40, 10, 3, 3)  # Assurez-vous d'ajuster les valeurs correctement
    joueur2 = Joueur(input("Quel est le nom du second joueur? "), 40, 10, 3, 3)  # Assurez-vous d'ajuster les valeurs correctement

    current_player = joueur1  # Le joueur 1 commence

    while joueur1.vie > 0 and joueur2.vie > 0:
        print(f"{current_player.nom}, c'est à votre tour.")
        user_choices = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

        if user_choices not in ["1", "2"]:
            print("Veuillez entrer un choix valide (1 ou 2).")
            continue

        user_choices = int(user_choices)

        if user_choices == 1:
            current_player.attaquer(joueur1 if current_player == joueur2 else joueur2)
        elif user_choices == 2:
            current_player.utiliser_potion()

        # Changement de joueur
        current_player = joueur1 if current_player == joueur2 else joueur2

    # Affichage du résultat
    if joueur1.vie <= 0:
        print(f"{joueur1.nom} n'a plus de points de vie. {joueur2.nom} remporte la partie!")
    else:
        print(f"{joueur2.nom} n'a plus de points de vie. {joueur1.nom} remporte la partie!")
