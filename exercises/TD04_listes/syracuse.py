def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    l=[]
    while n!=1:
        if n%2==0:
            n//=2
        else:
            n=(n*3+1)
        l.append(n)
    return l

print(syracuse(3))



def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 1 à n_max """
    for i in range(1,n_max+1):
        syracuse(i)
    return True

print(testeConjecture(10000))


def tempsVol(n):
    """ Retourne le temps de vol de n """
    return len(syracuse(n))-1

print("Le temps de vol de", 3, "est", tempsVol(3))



def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    return [tempsVol(i) for i in range (1,n_max+1)]

print(tempsVolListe(100))



l=tempsVolListe(10000)
t_max=max(l)
print("l entier", l.index(t_max)+1,"a le plus grand temps", t_max)



def alt_max(n):
    return max(syracuse(n))

def alt_max_liste(alt_max):
    return [alt_max(i)for i in range (1,alt_max+1)]
    
l_alt=alt_max_liste(10000)
b=max(l_alt)
print("l entier ")