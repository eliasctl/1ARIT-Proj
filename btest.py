import random


# fonctio qui renvoie une liste melangé des 26 lettres de l'disque
def melangeDisque():
    disque = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
              "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    random.shuffle(disque)
    return disque


# fonction qui renvoie une liste de n listes de 26 lettres melangé
def listeTotale(n):
    liste = []
    for i in range(n):
        liste.append(melangeDisque())
    return liste


# fonction qui stoque dans une liste les lignes d'un fichier
def getEncryption():
    with open("cryptage.txt", "r") as f:
        liste = f.readlines()
        # on enleve les \n
        for i in range(len(liste)):
            liste[i] = liste[i].replace("\n", "")
    return liste


getEncryption()
