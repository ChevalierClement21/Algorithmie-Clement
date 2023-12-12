Tab = []
i = 0

def comptageLettre (mot):
    Tab = []
    i = 0
    while mot != 'STOP':
        Tab.append(len(mot))
        i += 1
        mot = input ("Ecrivez un mot de votre choix pour arrêter ecrivez STOP ")
    for j in range (0,i):
        print(Tab[j])
    return Tab

mot = input ("Ecrivez un mot de votre choix pour arrêter ecrivez STOP ")
comptageLettre(mot)




