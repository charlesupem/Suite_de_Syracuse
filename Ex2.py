def vol_alt(a,lst):
    '''Fonction renvoyant le temps de vol et l'altitude pour la suite de Syracuse.
    
    Paramètres : a (int) : Valeur > 0
                 lst (liste) : liste vide

    >>>vol, alt = vol_alt(6,[])
    Temps de vol pour n = 5 : 8, altitude : 16
    
    '''
    lst.append(a)

    if a == 1 :
        return 0, lst
    elif a % 2 == 0 :
        vol,lst = vol_alt(a//2,lst) 
        vol+=1
        return vol,lst
    else:
        vol,lst = vol_alt(3*a+1,lst) 
        vol += 1
        return vol,lst

'''vol, alt = vol_alt(36791537,[])
alt = max(alt)

print('Temps de vol pour n = 5 : '+str(vol)+', altitude : '+str(alt))'''

vol = 0
i = 36791535

while vol < 745  :


    vol, alt = vol_alt(i,[])
    alt = max(alt)

    i +=1

print('Temps de vol pour n = 5 : '+str(vol)+', altitude : '+str(alt))