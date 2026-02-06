def fusion(lsta, lstb) :
    '''
    Si lsta et lstb sont triés dans l'ordre croissant, alors la fonction retourne
    une fusion triées des deux listes
    '''
    i = 0 #position dans lsta
    j = 0 #position dans lstb
    reponse = []
    while i < len(lsta) and j < len(lstb) :
        if lsta[i] <= lstb[j] :
            reponse.append(lsta[i])
            i += 1
        else :
            reponse.append(lstb[j]) 
            j += 1

    if i == len(lsta) : 
        while j < len(lstb[j]) :  
            reponse.append(lstb[j]) 
            j += 1
    else :
        while i < len(lsta) :
            reponse.append(lstb[i])
            i += 1
    return reponse