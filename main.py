import perso
import random
import histoire
import ctypes
import tkinter as tk
from tkinter import simpledialog




joueur = histoire.select_perso()

print(joueur.vie)





# Fonction pour modifier les points de vie
def modifier_vie():
    nouveau_vie = simpledialog.askinteger("Modifier les points de vie", "Nouveau nombre de points de vie :")
    if nouveau_vie is not None:
        joueur.vie = nouveau_vie
    fenetre.destroy()  # Ferme la fenêtre après la modification
def modifier_viande():
    nouveau_viande = simpledialog.askinteger("Modifier la viande de départ", "Nouveau nombre de points de viande :")
    if nouveau_viande is not None:
        joueur.nb_viande = nouveau_viande
    fenetre.destroy()

# Code pour créer l'interface
fenetre = tk.Tk()
fenetre.title("Interface de Modification")

bouton_modifier_vie = tk.Button(fenetre, text="Modifier les points de vie", command=modifier_vie)
bouton_modifier_vie.pack()
bouton_modifier_viande = tk.Button(fenetre, text="Modifier la viande que l'on possède au départ", command=modifier_viande)
bouton_modifier_viande.pack()
fenetre.mainloop()


print(joueur.vie)

nb_degats_joueur = random.randint(1, 4)
nb_degats_mob = random.randint(0,3)



mymessage = 'A message'
title = 'Popup window'
ctypes.windll.user32.MessageBoxW(0, mymessage, title, 0)
"""

lancement du jeu :

demande : modifier les parametres (vie des perso, nb de stuff au depart, ...
          lancer le jeu

"""


troll = perso.Troll(1, nb_degats_mob)
vampire = perso.Vampire(1, nb_degats_mob)
loupGarou = perso.LoupGarou(1, nb_degats_mob)
mob = [troll, vampire, loupGarou]

print("\r\r")
while joueur.vie > 0:
    # Tour du joueur
    print(f"{joueur.nom}, que souhaitez-vous faire?")
    print("1. Attaquer")
    if isinstance(joueur, perso.Sorcier):
        print("2. Se soigner (pour les sorciers)")
    print("3. Manger (si vous avez de la viande)")

    choix = input("Saisissez 1, 2 ou 3 : ")
    print("\n\n")

    if choix == "1":
       mob = histoire.attaque(joueur, mob, nb_degats_joueur, nb_degats_mob)
    elif choix == "2" and isinstance(joueur, perso.Sorcier):
        histoire.soigner(joueur)
    elif choix == "3" and joueur.nb_viande > 0:
        joueur.nb_viande -= 1
        joueur.manger()
        print(f"Vous mangez de la viande et avez maintenant {joueur.vie} points de vie.\nIl vous reste {joueur.nb_viande} viande")
    else:
        print("Choix invalide. Veuillez choisir une option valide.")


    if joueur.vie <= 0:
        print("Vous avez été vaincu par l'ennemi.")
        break  # La boucle s'arrête si le joueur perd
    elif len(mob)==0:
        print("Vous avez gagné")
        break
    print("\n\n")
