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
    def modifier_degats():
        nouveau_degats = simpledialog.askinteger("Modifier les degats", "Nouveau nombre de dégats que le joueur peut mettre :")
        if nouveau_degats is not None:
            default_joueur[3] = int(nouveau_degats)


    def fermer():
        fenetre.destroy()
    # Code pour créer l'interface
    fenetre = tk.Tk()
    fenetre.title("Paramètres du jeu")

    bouton_modifier_vie = tk.Button(fenetre, text="Modifier les points de vie", command=modifier_vie)
    bouton_modifier_vie.pack()
    bouton_modifier_viande = tk.Button(fenetre, text="Modifier la viande que l'on possède au départ",command=modifier_viande)
    bouton_modifier_viande.pack()
    bouton_modifier_degats = tk.Button(fenetre, text="Modifier les dégâts du joueur", command=modifier_degats)
    bouton_modifier_degats.pack()

    bouton_valider = tk.Button(fenetre, text="Valider", command=fermer)
    bouton_valider.pack(side="bottom")

    fenetre.mainloop()
    return default_joueur

"""parametre à ajouter : 
vie_mob_min/max
degats_mob_min/max
potion pour le sorcier


+ avancé mais a faire :
ajouter un joueur


"""