def maxliste(tab):
    maxi = tab[0]
    for v in tab:
        if v > maxi:
            maxi = v
    return maxi