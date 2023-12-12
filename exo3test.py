def verificationINT(nb):
    while nb.isdigit()==False:
        nb = input("Ecrire un nombre correct :")
    nb = int(nb)
    return nb


def index():
    somme = 0
    index1 = input("Choisir un nombre pour le premier index")
    index1 =verificationINT(index1)
    index1 = int(index1)
    
    while index1 > len(Tab):
        index1 = input("Choisir un nombre pour le premier index")
        index1 =verificationINT(index1)
        index1 = int(index1)
    index2 = input("Choisir un nombre pour le deuxieme index")
    index2 = verificationINT(index2)
    index2 = int(index2)
    
    while index2 > len(Tab):
        index2 = input("Choisir un nombre pour le deuxieme index")
        index2 = verificationINT(index2)
        index2 = int(index2)
    somme = Tab[index1] + Tab[index2]
    return somme

    


Tab = []
resultat = 0
nb = input("Ecrire un nombre :")
verificationINT(nb)
nb = int(nb)
while nb != 0:
    Tab.append(nb)
    resultat += nb
    if resultat > 100:
        break
    nb = input("Ecrire un nombre :")
    verificationINT(nb)
    nb = int(nb)
    

print(index())

