import tkinter as tk


# fonction qui stoque dans une liste les lignes d'un fichier
def getEncryption():
    with open("cryptage.txt", "r") as f:
        liste = f.readlines()
        for i in range(len(liste)):
            liste[i] = liste[i].replace("\n", "")
    return liste


def swap_labels(label1, label2):
    row1 = label1.grid_info()["row"]
    row2 = label2.grid_info()["row"]
    column1 = label1.grid_info()["column"]
    column2 = label2.grid_info()["column"]

    label1.grid(row=row2, column=column2)
    label2.grid(row=row1, column=column1)


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
    boutons = []

    for i in range(len(liste_totale)):
        label = tk.Label(window, text=liste_totale[i])
        liste_labels.append(label)
        label.grid(row=i, column=0)
        bouton = tk.Button(window, text=str(i), command=lambda idx=i: swap_labels(
            liste_labels[idx], liste_labels[0]))
        bouton.grid(row=i, column=1)
        boutons.append(bouton)

    # Boucle principale de la fenêtre
    window.mainloop()


main()
