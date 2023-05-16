# Jefferson-Cylinder Par William BERGUE & Elias MOUSSA - SupInfo 2022/2023 - BenG1

import random
from datetime import datetime
from time import strftime


class CreerCylindres():
    def __init__(self, nbCylindre):
        self.alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                         "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.nomFichier = "cylindre_" + \
            datetime.now().strftime("%d_%m_%Y__%H_%M_%S") + ".txt"
        self.creerFichierTexte()
        self.nbCylindre = nbCylindre
        while self.nbCylindre > 0:
            self.cylindre = self.creerCylindre()
            self.fichier = self.ecritureFichierTexte()
            self.nbCylindre -= 1

    def creerCylindre(self):
        # Création d'un cylindre avec les lettres de l'alphabet dans un ordre aléatoire
        cylindre = []
        for i in range(26):
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


CreerCylindres(5)


def FichierTexteEnDictionnaire(nomFichier):
    # Lecture du fichier texte et création d'un dictionnaire {ligne: [cylindre]}
    fichier = open(nomFichier, "r")
    dictionnaire = {}
    nbLigne = 0
    for ligne in fichier:
        nbLigne += 1
        dictionnaire[nbLigne] = []
        for lettre in ligne:
            if lettre != "\n":
                dictionnaire[nbLigne].append(lettre)
    fichier.close()
    return dictionnaire


nomFichier = "test.txt"
# print(FichierTexteEnDictionnaire(nomFichier))
cylindres = FichierTexteEnDictionnaire(nomFichier)


class cryptageManuel():
    def __init__(self):
        #self.cylindres = FichierTexteEnDictionnaire(nomFichier)
        self.cylindres = cylindres
        self.ordreCylindres = self.choisirOrdreCylindres()
        # for ligne in self.cylindres:
        #     self.ordreCylindres.append(ligne)

    def afficherCylindres(self):
        textOrdreCylindres = ""
        nbCylindres = len(self.cylindres)
        for i in self.cylindres:
            textOrdreCylindres += str(self.ordreCylindres[i-1]) + " "
        print(textOrdreCylindres)
        for i in range(26):
            for j in range(nbCylindres):
                print(self.cylindres[self.ordreCylindres[j]][i], end=" ")
            print("")

    def tournerCylindre(self, numCylindre, sens):
        if sens == 1:
            self.cylindres[numCylindre].insert(
                0, self.cylindres[numCylindre].pop())
        elif sens == 0:
            self.cylindres[numCylindre].append(
                self.cylindres[numCylindre].pop(0))

    def choisirOrdreCylindres(self):
        ordreCylindres = []
        for i in self.cylindres:
            # On demande à l'utilisateur de choisir l'ordre des cylindres
            cylindreChoisi = int(
                input("Choisissez le cylindre " + str(i) + " : "))
            while cylindreChoisi in ordreCylindres or cylindreChoisi > len(self.cylindres) or cylindreChoisi < 1:
                print("Ce cylindre a déjà été choisi")
                cylindreChoisi = int(
                    input("Choisissez le cylindre " + str(i) + " : "))
            ordreCylindres.append(cylindreChoisi)
        return ordreCylindres


cryptageManuel().afficherCylindres()
