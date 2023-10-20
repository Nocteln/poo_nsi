import tkinter as tk
from tkinter import simpledialog

# Fonction pour modifier les points de vie
def parametres(default_joueur):
    def modifier_vie():
        nouveau_vie = simpledialog.askinteger("Modifier les points de vie", "Nouveau nombre de points de vie :")
        if nouveau_vie is not None:
            default_joueur[0] = int(nouveau_vie)

    def modifier_viande():
        nouveau_viande = simpledialog.askinteger("Modifier la viande de départ",
                                                 "Nouveau nombre de points de viande :")
        if nouveau_viande is not None:
            default_joueur[2] = int(nouveau_viande)

    # Code pour créer l'interface
    fenetre = tk.Tk()
    fenetre.title("Interface de Modification")

    bouton_modifier_vie = tk.Button(fenetre, text="Modifier les points de vie", command=modifier_vie)
    bouton_modifier_vie.pack()
    bouton_modifier_viande = tk.Button(fenetre, text="Modifier la viande que l'on possède au départ",command=modifier_viande)
    bouton_modifier_viande.pack()
    fenetre.mainloop()
    return default_joueur

"""parametre à ajouter : 
vie_mob_min/max
degats_mob_min/max
potion pour le sorcier


+ avancé mais a faire :
ajouter un joueur


"""