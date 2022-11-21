carre_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]
print(carre_mag)


carre_pas_mag=[]
for lignes in range(len(carre_mag)):
    carre_pas_mag.append([])
    for colonnes in range(len(carre_mag[lignes])):
        carre_pas_mag[lignes].append(carre_mag[lignes][colonnes])
carre_pas_mag[3][2]=7
print(carre_pas_mag)


carre_pas_mag=[]
for lignes in carre_mag:
    carre_pas_mag.append(lignes.copy())
carre_pas_mag[3][2]=7
print(carre_pas_mag)



carre_pas_mag=[lignes[:]for lignes in carre_mag]
carre_pas_mag[3][2]=7
print(carre_pas_mag)



def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for i in carre:
        print(i)
    print()

afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    somme=sum(carre[0])
    for lignes in carre:
        if sum(lignes)!=somme:
            return -1
    return somme

print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))



def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    colonne1=[lignes[0] for lignes in carre]
    somme=sum(colonne1)
    for j in range(1,len(carre)):
        colonne=[lignes[j]for lignes in carre]
        if sum(colonne)!=somme:
            return -1
    return somme
        
print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))



def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    taille=len(carre)
    diag1=[carre[i][i] for i in range(taille)]
    diag2=[carre[i][taille-i-1] for i in range(taille)]
    somme=sum(diag1)
    if sum(diag2)!= somme :
        return -1
    else:
        return somme 

print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))



def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    return testLignesEgales(carre) == testColonnesEgales(carre) and testLignesEgales(carre)== testDiagonalesEgales(carre) and testLignesEgales(carre)!=-1

print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))



def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    liste=[]
    for lignes in carre:
        liste.extend(lignes)
    taille=len(carre)
    for entier in range(1,taille*taille+1):
        if entier not in liste:
            return False
    return True
   

print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))