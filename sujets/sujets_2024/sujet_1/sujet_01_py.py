def echange(tab, i, j):
    '''Echange les Ã©lÃ©ments d'indice i et j dans le tableau tab.'''
    temp = ... 
    tab[i] = ... 
    tab[j] = ... 

def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la mÃ©thode du tri par sÃ©lection.'''
    N = len(tab)
    for k in range(...): 
        imin = ... 
        for i in range(..., N): 
            if tab[i] < ...: 
                imin = i
        echange(tab, ..., ...) 


