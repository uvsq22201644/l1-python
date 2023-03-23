#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return temps[0]*24*60*60+temps[1]*60*60+temps[2]*60+temps[3]

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jours=seconde//(24*60*60)
    r=seconde%(24*60*60)
    heures=r//3600
    d=r%3600
    minutes=d//60
    secondes=r%60
    return(jours,heures,minutes,secondes)
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes") 


#fonction auxiliaire ici
def affichePluriel(mot,nb):
    if nb > 0:
        print(" ",nb,mot,end="")
    if nb > 1:
        print("s",end="")

def afficheTemps(temps):
    affichePluriel("jour",temps[0])
    affichePluriel("heure",temps[1])
    affichePluriel("minute",temps[2])
    affichePluriel("seconde",temps[3])
    
afficheTemps((1,0,14,23))  

def demandeTemps():
    j=-1
    h=-1
    m=-1
    s=-1
    while j< 0:
        j=int(input("entrez un nombre"))
    while (h<0 or h >=24):
        h=int(input("entrez un nombre"))
    while (m<0 or m>=60):
        m=int(input("entrez un nombre"))
    while (s<0 or s>=60):
        s=int(input("entrez un nombre"))
        return (j,h,m,s)

afficheTemps(demandeTemps())



def sommeTemps(temps1,temps2):
    return secondeEnTemps(tempsEnSeconde(temps1)+tempsEnSeconde(temps2))

sommeTemps((2,3,4,25),(5,22,57,1))


def proportionTemps(temps,proportion):
    return secondeEnTemps(tempsEnSeconde(temps)*proportion)

afficheTemps(proportionTemps((2,0,36,0),0.2))
afficheTemps(proportionTemps(proportion=0.2,temps=(2,0,36,0)))
#appeler la fonction en échangeant l'ordre des arguments



import time 
def tempsEnDate(temps):
    a=1970+temps[0]//365
    j=1+temps[0]%365
    return (a,j,temps[1],temps[2],temps[3])

def afficheDate(date: tuple=()):
    if len(date)==0:
        date= tempsEnDate(secondeEnTemps(int(time.time())))
    print("jour numero",date[1],"de l'année",date[0],"a",str(date[2])+":"+str(date[3])+":"+str(date[4]))
    
temps=secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate()

print(time.time)