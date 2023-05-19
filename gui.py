import tkinter as tk
count = 0


# fonction qui stoque dans une liste les lignes d'un fichier
def getEncryption():
    with open("cryptage.txt", "r") as f:
        liste = f.readlines()
        for i in range(len(liste)):
            liste[i] = " ".join(liste[i].replace("\n", " "))
    # print(liste)
    return liste


def clear_grid():
    for widget in window.grid_slaves():
        widget.grid_forget()


# fonction qui verifie si la liste est ordonnée
def checkIfOrdonated():
    global count
    if count == 5:
        clear_grid()
        update_liste_window()
        create_rotate_button()


# fonction qui ajoute un element a un indice donné dans une liste finale
def add_to_liste_finale(indice):
    liste_finale.append(liste_totale[indice])
    boutons[indice].grid_remove()
    global count
    count += 1
    update_liste_window()
    checkIfOrdonated()


# fonction qui crée un bouton pour faire tourner la liste
def create_rotate_button():
    for i in range(len(liste_totale)):
        bouton = tk.Button(window, text=str("rotate Liste"),
                           command=lambda index=i: rotate_liste(index))
        bouton.grid(row=i, column=5)
        boutons.append(bouton)


# fonction qui fait tourner une chaine de caractère de 2 caractères
def rotate_string(string):
    rotated = string[-2:] + string[:-2]
    return rotated


# fonction qui est apellée quand on clique sur le bouton pour faire tourner la liste
def rotate_liste(index):
    strin_to_rotate = liste_finale[index]
    liste_finale[index] = rotate_string(strin_to_rotate)
    clear_grid()
    update_liste_window()
    create_rotate_button()


# fonction qui affiche la liste triée dans la fenêtre
def update_liste_window():
    # Supprimer les anciens labels de la liste finale
    for label in labels_liste_finale:
        label.destroy()

    # Afficher les éléments de la liste finale à côté des boutons
    for i in range(len(liste_finale)):
        label = tk.Label(window, text=liste_finale[i])
        label.grid(row=i, column=3)
        labels_liste_finale.append(label)


# Liste des elements non triés
liste_totale = getEncryption()
# Liste des elements triés
liste_finale = []
# Liste des boutons
boutons = []
# Liste des labels de la liste finale
labels_liste_finale = []


# fonction qui crée la fenetre
def create_window():
    global window

    # Création de la fenêtre
    window = tk.Tk()

    # Titre de la fenêtre
    window.title("Disque de jefferson")

    # Taille de la fenêtre
    window.geometry("800x500")

    # Création des labels et des boutons
    for i in range(len(liste_totale)):
        tk.Label(window, text=liste_totale[i]).grid(row=i, column=0)
        tk.Label(window, text="->").grid(row=i, column=2)
        bouton = tk.Button(window, text=str(
            i), command=lambda index=i: add_to_liste_finale(index))
        bouton.grid(row=i, column=1)
        boutons.append(bouton)

    # Boucle principale de la fenêtre
    window.mainloop()


# Appel de la fonction pour créer la fenêtre
create_window()
