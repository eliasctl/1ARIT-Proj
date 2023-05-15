# Jefferson-Cylinder Par William BERGUE & Elias MOUSSA - SupInfo 2022/2023 - BenG1

import random
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def creerCylindre():
    # Création d'un cylindre avec les lettres de l'alphabet dans un ordre aléatoire
    cylindre = []
    for i in range(0, 26):
        cylindre.append(alphabet[i])
    random.shuffle(cylindre)
    return cylindre

print(creerCylindre())
print(creerCylindre())


