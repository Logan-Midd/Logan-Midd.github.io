def couples_consecutifs(tab):
    """
    prend en paramÃ¨tre une liste de nombres entiers tab non vide, et qui renvoie la liste (Ã©ventuellement vide) des couples d'entiers consÃ©cutifs successifs qu'il peut y avoir dans tab.
    """
    t = []
    for i in range(len(tab)-1):
        if tab[i+1] -  tab[i] == 1:
            t.append((tab[i], tab[i+1]))
    return t

assert couples_consecutifs([1, 4, 3, 5]) == []
assert couples_consecutifs([1, 4, 5, 3]) == [(4, 5)]
assert couples_consecutifs([1, 1, 2, 4]) == [(1, 2)]
assert couples_consecutifs([7, 1, 2, 5, 3, 4]) == [(1, 2), (3, 4)]
assert couples_consecutifs ([5, 1, 2, 3, 8, -5, -4, 7]) == [(1, 2), (2, 3), (-5, -4)]

