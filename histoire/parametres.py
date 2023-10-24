import tkinter as tk
from tkinter import simpledialog

def parametres(default_joueur):
    print("Veuillez vous rendre dans la fenetre qui vient de s'ouvrir pour modifier les parametres")
    def modifier_vie():
        nouveau_vie = simpledialog.askinteger("Modifier les points de vie", "Nouveau nombre de points de vie :")
        if nouveau_vie is not None:
            default_joueur[0] = int(nouveau_vie)
        print("Nouveau nombre de points de vie :", default_joueur[0])  # Ajout d'un print de test

    def modifier_viande():
        nouveau_viande = simpledialog.askinteger("Modifier la viande de départ", "Nouveau nombre de points de viande :")
        if nouveau_viande is not None:
            default_joueur[2] = int(nouveau_viande)
        print("Nouveau nombre de points de viande :", default_joueur[2])  # Ajout d'un print de test

    def modifier_degats():
        nouveau_degats = simpledialog.askinteger("Modifier les dégâts du joueur", "Nouveau nombre de dégâts du joueur :")
        if nouveau_degats is not None:
            default_joueur[3] = int(nouveau_degats)
        print("Nouveaux dégâts du joueur :", default_joueur[3])  # Ajout d'un print de test

    def fermer_fenetre():
        fenetre.destroy()

    # Code pour créer l'interface
    fenetre = tk.Tk()
    fenetre.title("Paramètres du jeu")

    bouton_modifier_vie = tk.Button(fenetre, text="Modifier les points de vie", command=modifier_vie)
    bouton_modifier_vie.pack()

    bouton_modifier_viande = tk.Button(fenetre, text="Modifier la viande de départ", command=modifier_viande)
    bouton_modifier_viande.pack()

    bouton_modifier_degats = tk.Button(fenetre, text="Modifier les dégâts du joueur", command=modifier_degats)
    bouton_modifier_degats.pack()

    bouton_valider = tk.Button(fenetre, text="Valider", command=fermer_fenetre)
    bouton_valider.pack(side="bottom")

    fenetre.mainloop()
    return default_joueur