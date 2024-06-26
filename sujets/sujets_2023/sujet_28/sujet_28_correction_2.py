def dichotomie(tab, x):
    if len(tab) == 0:
        return False, 1
    if (x < tab[0]) or (x > tab[len(tab)-1]):
        return False, 2
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False, 3
