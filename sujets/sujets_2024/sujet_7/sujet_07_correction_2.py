def tri_insertion(tab):
    '''Trie le tableau tab par ordre croissant
    en appliquant l'algorithme de tri par insertion'''
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i] 
        # la variable j sert Ã  dÃ©terminer 
        # oÃ¹ placer la valeur Ã  ranger
        j = i 
        # tant qu'on n'a pas trouvÃ© la place de l'Ã©lÃ©ment Ã 
        # insÃ©rer on dÃ©cale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j-1]: 
            tab[j] = tab[j-1]
            j = j - 1 
        tab[j] = valeur_insertion 


