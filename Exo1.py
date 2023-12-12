

def motEnEtoile(mot):
    MotDePasse = ''
    for i in range (0,len(mot)):
        MotDePasse += '*'
    return MotDePasse

mot = input("Ecrire votre mot ")
print(motEnEtoile(mot))