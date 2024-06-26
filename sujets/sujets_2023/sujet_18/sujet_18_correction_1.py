def max_et_indice(tab):
    """
    Prend en paramÃ¨tre une liste non vide tab de nombres entiers 
    et renvoie la valeur du plus grand Ã©lÃ©ment de cette liste 
    ainsi que lâindice de sa premiÃ¨re apparition dans cette liste.
    """
    index_m = 0
    maxi = tab[0]
    for i in range(1, len(tab)):
        if tab[i] > maxi:
            index_m = i
            maxi = tab[i]
    return maxi, index_m


assert max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)
assert max_et_indice([-2]) == (-2, 0)
assert max_et_indice([-1, -1, 3, 3, 3]) == (3, 2)
assert max_et_indice([1, 1, 1, 1]) == (1, 0)

        