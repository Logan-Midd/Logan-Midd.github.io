def a_doublon(tab):
    n = len(tab)
    if n < 2 :
        return False
    for i in range(n-1):
        if tab[i] == tab[i+1]:
            return True
    return False