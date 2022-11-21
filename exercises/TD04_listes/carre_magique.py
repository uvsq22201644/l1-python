carre_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]
print(carre_mag)


carre_pas_mag=carre_mag.copy()
carre_pas_mag[3][2]=7
print(carre_pas_mag)


def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for i in range (len(carre)):
        for j in range(len(carre[i])):
            print(carre[i][j],end=" ")
        print()

carre_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]
afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    for i in range(len(carre)):
        if sum(carre[0])==sum(carre[i]):
            continue
        else:
            return -1
    return sum(carre[0])

carre_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]
print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))


def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    for i in range(len(carre)):
        for j in range (len(carre[i])):
            if sum(carre[0][0])==sum(carre[i][j]):
                continue
            else:
                return -1
    return sum(carre[0][0])

        
print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))


def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    diag1=0
    diag2=0
    for k in range(len(carre)):
        diag1+=carre[k][k]
        diag2+=carre[len(carre)-k-1][i]

carre_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]
print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))



def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    if testLignesEgales() == testColonnesEgales() and testColonnesEgales()== testDiagonalesEgales() :
        return True 
    else:
        return False

print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))


def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    n=len(carre)
    nv_carre=[]
    for i in range(n):
        for j in range(n):
            nv_carre.append(carre[i][j])
    nv_carre.sort()
    for a in range(1,n**2):
        if a==(nv_carre[a]-1):
            continue
        else:
            return('carre pas normal')
    return('carre normal')
        

print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))