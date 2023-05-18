import tkinter as tk

# Liste de test
liste_totale = ["Element 1", "Element 2",
                "Element 3", "Element 4", "Element 5"]
liste_finale = []
boutons = []
labels_liste_finale = []


def add_to_liste_finale(indice):
    liste_finale.append(liste_totale[indice])
    boutons[indice].grid_remove()
    print(liste_finale)
    update_liste_finale()


def update_liste_finale():
    # Supprimer les anciens labels de la liste finale
    for label in labels_liste_finale:
        label.destroy()

    # Afficher les éléments de la liste finale à côté des boutons
    for i in range(len(liste_finale)):
        label = tk.Label(window, text=liste_finale[i])
        label.grid(row=i, column=2)
        labels_liste_finale.append(label)


def create_list_window():
    global window
    # Création de la fenêtre
    window = tk.Toplevel()

    # Titre de la fenêtre
    window.title("Listes")

    # Taille de la fenêtre
    window.geometry("800x800")

    # Création des labels et des boutons
    for i in range(len(liste_totale)):
        tk.Label(window, text=liste_totale[i]).grid(row=i, column=0)
        bouton = tk.Button(window, text=str(
            i), command=lambda index=i: add_to_liste_finale(index))
        bouton.grid(row=i, column=1)
        boutons.append(bouton)

    # Mise à jour de l'affichage de la liste finale
    update_liste_finale()


def open_window():
    # Création de la fenêtre principale
    main_window = tk.Tk()

    # Titre de la fenêtre principale
    main_window.title("Fenêtre principale")

    # Taille de la fenêtre principale
    main_window.geometry("400x200")

    # Fonction pour ouvrir la fenêtre avec les listes
    def open_list_window():
        create_list_window()

    # Bouton pour ouvrir la fenêtre avec les listes
    open_button = tk.Button(
        main_window, text="Ouvrir la fenêtre avec les listes", command=open_list_window)
    open_button.pack()

    # Boucle principale de la fenêtre principale
    main_window.mainloop()


# Appel de la fonction principale pour ouvrir la fenêtre principale
open_window()
