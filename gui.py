import tkinter as tk
# from liste import *

# Liste de test
liste_totale = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
liste_finale = []
boutons = []
labels_liste_finale = []


def add_to_liste_finale(indice):
    liste_finale.append(liste_totale[indice])
    boutons[indice].grid_remove()
    update_liste_finale()


def update_liste_finale():
    # Supprimer les anciens labels de la liste finale
    for label in labels_liste_finale:
        label.destroy()

    # Afficher les éléments de la liste finale à côté des boutons
    for i in range(len(liste_finale)):
        label = tk.Label(window, text=liste_finale[i])
        label.grid(row=i, column=3)
        labels_liste_finale.append(label)


def create_window():
    global window  # Déclarer window en tant que variable globale
    # Création de la fenêtre
    window = tk.Tk()

    # Titre de la fenêtre
    window.title("Jeff")

    # Taille de la fenêtre
    window.geometry("800x800")

    # Création des labels et des boutons
    for i in range(len(liste_totale)):
        tk.Label(window, text=liste_totale[i]).grid(row=i, column=0)
        tk.Label(window, text="->").grid(row=i, column=2)
        bouton = tk.Button(window, text=str(
            i), command=lambda index=i: add_to_liste_finale(index))
        bouton.grid(row=i, column=1)
        boutons.append(bouton)

    # Mise à jour de l'affichage de la liste finale
    update_liste_finale()

    # Boucle principale de la fenêtre
    window.mainloop()


# Appel de la fonction pour créer la fenêtre
create_window()
