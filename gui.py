import tkinter as tk
count = 0
decalage = 6


# fonction qui stoque dans une liste les lignes d'un fichier
def getEncryption():
    with open("cryptage.txt", "r") as f:
        liste = f.readlines()
        for i in range(len(liste)):
            liste[i] = "".join(liste[i].replace("\n", ""))
    return liste


def clear_grid():
    for widget in window.grid_slaves():
        widget.grid_forget()


# fonction qui verifie si la liste est ordonnée
def checkIfOrdonated():
    global count
    if count == len(liste_non_trié):
        clear_grid()
        update_liste_window()
        create_rotate_button()


# fonction qui ajoute un element a un indice donné dans une liste finale
def add_to_liste_trié(indice):
    liste_trié.append(liste_non_trié[indice])
    boutons[indice].grid_remove()
    global count
    count += 1
    update_liste_window()
    checkIfOrdonated()


# fonction qui crée un bouton pour faire tourner la liste
def create_rotate_button():
    for i in range(len(liste_non_trié)):
        bouton = tk.Button(window, text=str("rotate Liste"),
                           command=lambda index=i: rotate_liste(index))
        bouton.grid(row=i, column=5)
        boutons.append(bouton)


# fonction qui fait tourner une chaine de caractère de 2 caractères
def rotate_string(string):
    rotated = string[-1] + string[:-1]
    return rotated


# fonction qui est apellée quand on clique sur le bouton pour faire tourner la liste
def rotate_liste(index):
    strin_to_rotate = liste_trié[index]
    liste_trié[index] = rotate_string(strin_to_rotate)
    clear_grid()
    update_liste_window()
    create_rotate_button()
    create_sub()


# fonction qui affiche la liste triée dans la fenêtre
def update_liste_window():
    # Supprimer les anciens labels de la liste finale
    for label in labels_liste_trié:
        label.destroy()

    # Afficher les éléments de la liste finale à côté des boutons
    for i in range(len(liste_trié)):
        label = tk.Label(window, text=liste_trié[i])
        label.grid(row=i, column=3)
        labels_liste_trié.append(label)


# fonction qui affiche le mot crypté
def get_encrypted_word():
    liste_mot_crypte = []
    for i in range(len(liste_trié)):
        liste_mot_crypte.append(liste_trié[i][0])
    return liste_mot_crypte


# fonction qui affiche le mot décrypté
def get_decrypted_word():
    liste_mot_decrypte = []
    for i in range(len(liste_trié)):
        liste_mot_decrypte.append(liste_trié[i][decalage])
    return liste_mot_decrypte


def decalage_plus_moins(arg):
    global decalage
    if arg > 0:
        if decalage < 25:
            decalage += 1
    elif arg < 0:
        if decalage > 3:
            decalage -= 1
    clear_grid()
    update_liste_window()
    create_rotate_button()
    create_sub()


def create_button_plus_moins():
    bouton = tk.Button(window, text=str("+"),
                       command=lambda decalage=1: decalage_plus_moins(decalage))
    bouton.grid(row=len(liste_trié) + 10, column=3)

    bouton = tk.Button(window, text=str("-"),
                       command=lambda decalage=-1: decalage_plus_moins(decalage))
    bouton.grid(row=len(liste_trié) + 20, column=3)


def create_sub():
    tk.Label(window, text="Mot cryptée : " + str(get_encrypted_word())).grid(
        row=len(liste_trié) + 1, column=3)
    tk.Label(window, text="Mot décryptée : " + str(get_decrypted_word())).grid(
        row=len(liste_trié) + 3, column=3)
    tk.Label(window, text="Décalage : " + str(decalage)).grid(
        row=len(liste_trié) + 7, column=3)
    create_button_plus_moins()


# Liste des elements non triés
liste_non_trié = getEncryption()
# Liste des elements triés
liste_trié = []
# Liste des boutons
boutons = []
# Liste des labels de la liste finale
labels_liste_trié = []


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
    for i in range(len(liste_non_trié)):
        tk.Label(window, text=liste_non_trié[i]).grid(row=i, column=0)
        tk.Label(window, text="->").grid(row=i, column=2)
        bouton = tk.Button(window, text=str(
            i), command=lambda index=i: add_to_liste_trié(index))
        bouton.grid(row=i, column=1)
        boutons.append(bouton)

    # Boucle principale de la fenêtre
    window.mainloop()


# Appel de la fonction pour créer la fenêtre
create_window()
