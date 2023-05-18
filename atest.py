import tkinter as tk


# fonction qui stoque dans une liste les lignes d'un fichier
def getEncryption():
    with open("cryptage.txt", "r") as f:
        liste = f.readlines()
        for i in range(len(liste)):
            liste[i] = liste[i].replace("\n", "")
    return liste


# fonction principale
def main():
    # Création de la fenêtre
    window = tk.Tk()

    # Titre de la fenêtre
    window.title("Disque de jefferson")

    # Taille de la fenêtre
    window.geometry("600x600")

    liste_totale = getEncryption()
    liste_labels = []

    for i in range(len(liste_totale)):
        label = tk.Label(window, text=liste_totale[i])
        liste_labels.append(label)
        label.grid(row=i, column=0)

    # on efface le premier label
    liste_labels[0].destroy()
    # liste_labels[0].grid_remove()

    # Boucle principale de la fenêtre
    window.mainloop()


main()
