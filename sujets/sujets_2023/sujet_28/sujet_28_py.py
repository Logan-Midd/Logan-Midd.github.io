def dichotomie(tab, x):
    """
        tab : tableau triÃ© dans lâordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """
    # cas du tableau vide
    if ...:
        return False, 1
    # cas oÃ¹ x n'est pas compris entre les valeurs extrÃªmes
    if (x < tab[0]) or ...:
        return False, 2
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = ...
        if x == tab[m]:
            return ...
        if x > tab[m]:
            debut = m + 1
        else:
            fin = ...
    return ...
