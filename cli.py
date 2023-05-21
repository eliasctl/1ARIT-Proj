# Jefferson-Cylinder Par William BERGUE & Elias MOUSSA - SupInfo 2022/2023 - BenG1

import random

def header():
    # console clear
    print("\033[H\033[J")
    print("______________________________________________________________________")
    print("  . .-. .-. .-. .-. .-. .-. .-. . .   .-. . . .   .-. . . .-. .-. .-.")
    print("  | |-  |-  |-  |-  |(  `-. | | |\|   |    |  |    |  |\| |  )|-  |(")
    print("`-' `-' '   '   `-' ' ' `-' `-' ' `   `-'  `  `-' `-' ' ` `-' `-' ' '")
    print("______________________________________________________________________")


class CreerCylindres():
    def __init__(self):
        self.alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        tempNom = input("Entrez le nom du fichier sans l'extention : ")
        if tempNom != "":
            self.nomFichier = tempNom + ".txt"
        self.creerFichierTexte()
        self.nbCylindre = 0
        while self.nbCylindre <= 0:
            print("Le nombre de cylindre doit un entier et être supérieur à 0")
            nbCylindre = input("Entrez le nombre de cylindre : ")
            try:
                self.nbCylindre = int(nbCylindre)
            except:
                self.nbCylindre = 0
        while self.nbCylindre > 0:
            self.cylindre = self.creerCylindre()
            self.fichier = self.ecritureFichierTexte()
            self.nbCylindre -= 1
        print("Le fichier " + self.nomFichier + " a été créé")

    def creerCylindre(self):
        cylindre = []
        for i in range(26):
            cylindre.append(self.alphabet[i])
        random.shuffle(cylindre)
        return cylindre

    def creerFichierTexte(self):
        fichier = open(self.nomFichier, "x")
        fichier.close()

    def ecritureFichierTexte(self):
        fichier = open(self.nomFichier, "a")
        for i in range(len(self.alphabet)):
            fichier.write(self.cylindre[i])
        if self.nbCylindre > 1:
            fichier.write("\n")
        fichier.close()


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


class cryptageOuDecryptage():
    def __init__(self):
        self.nomFichier = input("Entrez le nom du fichier sans l'extention : ")
        self.cylindres = FichierTexteEnDictionnaire(self.nomFichier + ".txt")
        self.ordreCylindres = self.choisirOrdreCylindres()
        self.numLigne = 0
        while self.numLigne <= 2 or 25 <= self.numLigne:
            print("La ligne doit être un entier entre 2 et 25")
            numLigne = input("Entrez la ligne où vous voulez que le texte en claire apparaisse (ligne verte) : ")
            try:
                self.numLigne = int(numLigne)
            except:
                self.numLigne = 0
        self.afficherCylindres()


    def afficherCylindres(self):
        textOrdreCylindres = ""
        nbCylindres = len(self.cylindres)
        for i in self.cylindres:
            textOrdreCylindres += str(self.ordreCylindres[i-1]) + " "
        print(textOrdreCylindres)
        print(" ")
        for i in range(26):
            if i == 0:
                print("\033[31m", end="")
            elif i == self.numLigne:
                print("\033[32m", end="")
            for j in range(nbCylindres):
                print(self.cylindres[self.ordreCylindres[j]][i], end=" ")
            print("\033[0m")
        print(" ")

    def tournerCylindre(self, numCylindre, sens):
        if sens == 1:
            self.cylindres[self.ordreCylindres[numCylindre-1]].insert(0, self.cylindres[self.ordreCylindres[numCylindre-1]].pop())
        elif sens == 0:
            self.cylindres[self.ordreCylindres[numCylindre-1]].append(self.cylindres[self.ordreCylindres[numCylindre-1]].pop(0))

    def choisirOrdreCylindres(self):
        ordreCylindres = []
        for i in self.cylindres:
            cylindreChoisi = int(input("Choisissez le cylindre " + str(i) + " : "))
            while cylindreChoisi in ordreCylindres or cylindreChoisi > len(self.cylindres) or cylindreChoisi < 1:
                print("Ce cylindre a déjà été choisi")
                cylindreChoisi = int(input("Choisissez le cylindre " + str(i) + " : "))
            ordreCylindres.append(cylindreChoisi)
        return ordreCylindres

header()

ChoixCreerCylindres = input("Voulez-vous créer un fichier de cylindres ? (O/N) : ")
if ChoixCreerCylindres == "O" or ChoixCreerCylindres == "o":
    CreerCylindres()
ChoixCryptageOuDecryptage = input("Voulez-vous crypter ou décrypter un fichier ? (O/N) : ")
if ChoixCryptageOuDecryptage == "O" or ChoixCryptageOuDecryptage == "o":
    cryptageOuDecryptage = cryptageOuDecryptage()
    Fin = False
    while Fin == False:
        ChoixTournerCylindre = input("Voulez-vous tourner un cylindre ? (O/N) : ")
        if ChoixTournerCylindre == "O" or ChoixTournerCylindre == "o":
            numCylindre = int(input("Entrez le numéro du cylindre à tourner : "))
            sens = int(input("Entrez le sens de rotation (0 pour haut, 1 pour bas) : "))
            cryptageOuDecryptage.tournerCylindre(numCylindre, sens)
            header()
            cryptageOuDecryptage.afficherCylindres()
        else:
            Fin = True

Print = input("Appuyez sur Entrée pour quitter")