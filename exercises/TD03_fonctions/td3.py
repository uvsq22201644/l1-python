#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return temps[0]*24*60*60+temps[1]*60*60+temps[2]*60+temps[3]

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

