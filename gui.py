import tkinter as tk
count = 0


# fonction qui stoque dans une liste les lignes d'un fichier
def getEncryption():
    with open("cryptage.txt", "r") as f:
        liste = f.readlines()
        for i in range(len(liste)):
            liste[i] = liste[i].replace("\n", "")
    return liste


# fonction qui ajoute un element a un indice donné dans une liste finale
def add_to_liste_finale(indice):
    liste_finale.append(liste_totale[indice])
    boutons[indice].grid_remove()
    global count
    count += 1
    # print(count)
    checkIfOrdonated()
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


def checkIfOrdonated():
    global count
    if count == 5:
        for label in liste_finale:
            print(label)
            label.destroy()


# Liste de test
liste_totale = getEncryption()
liste_finale = []
boutons = []
labels_liste_finale = []


# fonction qui crée la fenetre
def create_window():
    global window

    # Création de la fenêtre
    window = tk.Tk()

    # Titre de la fenêtre
    window.title("Disque de jefferson")

    # Taille de la fenêtre
    window.geometry("800x800")

    # Création des labels et des boutons
    for i in range(len(liste_totale)):
        tk.Label(window, text=liste_totale[i]).grid(row=i, column=0)
        tk.Label(window, text="->").grid(row=i, column=2)
        bouton = tk.Button(window, text=str(i), command=lambda index=i: add_to_liste_finale(index))
        bouton.grid(row=i, column=1)
        boutons.append(bouton)

    # Mise à jour de l'affichage de la liste finale
    update_liste_finale()

    # Boucle principale de la fenêtre
    window.mainloop()


# Appel de la fonction pour créer la fenêtre
create_window()
