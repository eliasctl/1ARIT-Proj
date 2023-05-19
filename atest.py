import tkinter as tk


def on_button_click():
    selected_number = spinbox.get()
    print("Nombre sélectionné :", selected_number)


# Création de la fenêtre principale
window = tk.Tk()

# Création du widget Spinbox avec une plage de 0 à 100
spinbox = tk.Spinbox(window, from_=0, to=100)
spinbox.pack()

# Création du bouton
button = tk.Button(window, text="Sélectionner", command=on_button_click)
button.pack()

# Lancement de la boucle principale de l'application
window.mainloop()
