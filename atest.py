import tkinter as tk


# Function to read encryption data from a file
def get_encryption():
    with open("cryptage.txt", "r") as f:
        return [line.strip() for line in f]


# Function to clear the grid of widgets in the window
def clear_grid():
    for widget in window.grid_slaves():
        widget.grid_forget()


# Function to add an element to the sorted list
def add_to_liste_trie(indice):
    liste_trie.append(liste_non_trie[indice])
    boutons[indice].grid_remove()
    update_liste_window()
    check_if_ordonated()


# Function to rotate a string by one position
def rotate_string(string):
    return string[-1] + string[:-1]


# Function called when the rotate button is clicked
def rotate_liste(index):
    string_to_rotate = liste_trie[index]
    liste_trie[index] = rotate_string(string_to_rotate)
    clear_grid()
    update_liste_window()
    create_rotate_button()
    create_sub()


# Function to update the window with the sorted list
def update_liste_window():
    for label in labels_liste_trie:
        label.destroy()

    for i, element in enumerate(liste_trie):
        label = tk.Label(window, text=element)
        label.grid(row=i, column=3)
        labels_liste_trie.append(label)


# Function to get the encrypted word
def get_encrypted_word():
    return [element[0] for element in liste_trie]


# Function to get the decrypted word
def get_decrypted_word():
    return [element[decalage] for element in liste_trie]


# Function to handle increment or decrement of the shift value
def decalage_plus_moins(arg):
    global decalage
    if arg > 0 and decalage < 25:
        decalage += 1
    elif arg < 0 and decalage > 3:
        decalage -= 1
    clear_grid()
    update_liste_window()
    create_rotate_button()
    create_sub()


# Function to create the plus and minus buttons for shift value
def create_button_plus_moins():
    plus_button = tk.Button(
        window, text="+", command=lambda: decalage_plus_moins(1))
    plus_button.grid(row=len(liste_trie) + 10, column=3)

    minus_button = tk.Button(
        window, text="-", command=lambda: decalage_plus_moins(-1))
    minus_button.grid(row=len(liste_trie) + 20, column=3)


# Function to create the labels for encrypted and decrypted words
def create_sub():
    tk.Label(window, text="Mot crypte : " + str(get_encrypted_word())
             ).grid(row=len(liste_trie) + 1, column=3)
    tk.Label(window, text="Mot decrypte : " + str(get_decrypted_word())
             ).grid(row=len(liste_trie) + 3, column=3)
    tk.Label(window, text="Decalage : " + str(decalage)
             ).grid(row=len(liste_trie) + 7, column=3)
    create_button_plus_moins()


# Function to create rotate buttons for each element in the list
def create_rotate_button():
    for i, _ in enumerate(liste_non_trie):
        button = tk.Button(window, text="Rotate Liste",
                           command=lambda index=i: rotate_liste(index))
        button.grid(row=i, column=5)
        boutons.append(button)


# Function to check if the list is fully sorted
def check_if_ordonated():
    global count
    count += 1
    if count == len(liste_non_trie):
        clear_grid()
        update_liste_window()
        create_rotate_button()


# Function to create the main window
def create_window():
    global window
    window = tk.Tk()
    window.title("Disque de Jefferson")
    window.geometry("800x500")

    for i, element in enumerate(liste_non_trie):
        tk.Label(window, text=element).grid(row=i, column=0)
        tk.Label(window, text="->").grid(row=i, column=2)
        button = tk.Button(window, text=str(
            i), command=lambda index=i: add_to_liste_trie(index))
        button.grid(row=i, column=1)
        boutons.append(button)

    window.mainloop()


# Initialize variables
liste_non_trie = get_encryption()
liste_trie = []
boutons = []
labels_liste_trie = []
count = 0
decalage = 6

# Create the main window
create_window()
