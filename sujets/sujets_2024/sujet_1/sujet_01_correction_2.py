def echange(tab, i, j):
    '''Echange les Ã©lÃ©ments d'indice i et j dans le tableau tab.'''
    temp = tab[i] 
    tab[i] = tab[j] 
    tab[j] = temp 

def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la mÃ©thode du tri par sÃ©lection.'''
    N = len(tab)
    for k in range(N-1): 
        imin = k 
        for i in range(k+1, N): 
            if tab[i] < tab[imin]: 
                imin = i
        echange(tab, k, imin) 
