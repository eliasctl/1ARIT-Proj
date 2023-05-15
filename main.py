# Jefferson-Cylinder Par William BERGUE & Elias MOUSSA - SupInfo 2022/2023 - BenG1

import random
from datetime import datetime
from time import strftime

class Creer():
    def __init__(self, nbCylindre):
        self.alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.nomFichier = "cylindre_" + datetime.now().strftime("%d_%m_%Y__%H_%M_%S") + ".txt"
        self.creerFichierTexte()
        self.nbCylindre = nbCylindre
        while self.nbCylindre > 0:
            self.cylindre = self.creerCylindre()
            self.fichier = self.ecritureFichierTexte()
            self.nbCylindre -= 1
        
        
    def creerCylindre(self):
        # Création d'un cylindre avec les lettres de l'alphabet dans un ordre aléatoire
        cylindre = []
        for i in range(0, 26):
            cylindre.append(self.alphabet[i])
        random.shuffle(cylindre)
        return cylindre
    
    def creerFichierTexte(self):
        # Création d'un fichier texte avec le cylindre
        fichier = open(self.nomFichier, "x")
        fichier.close()

    def ecritureFichierTexte(self):
        # Ecriture du cylindre dans un fichier texte
        fichier = open(self.nomFichier, "a")
        for i in range(0, 26):
            fichier.write(self.cylindre[i])
        if self.nbCylindre > 1:
            fichier.write("\n")
        fichier.close()

Creer(5)


