import tkinter as tk


# fonction qui stocke dans une liste les lignes d'un fichier
def getEncryption():
    with open("cryptage.txt", "r") as f:
        liste = f.readlines()
        for i in range(len(liste)):
            liste[i] = liste[i].replace("\n", "")
    return liste


def add_to_liste_finale(indice, liste_finale, bouton):
    liste_finale.append(liste_finale[indice])
    bouton.grid_forget()


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
    liste_finale = []

    for i in range(len(liste_totale)):
        label = tk.Label(window, text=liste_totale[i])
        liste_labels.append(label)
        label.grid(row=i, column=0)
        bouton = tk.Button(window, text=str(i), command=lambda id=i,
                           btn=boutons[i]: add_to_liste_finale(id, liste_finale, btn))
        bouton.grid(row=i, column=1)
        boutons.append(bouton)

    # Boucle principale de la fenêtre
    window.mainloop()


main()
