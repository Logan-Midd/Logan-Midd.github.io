def ecriture_binaire_entier_positif(n):
    tab = [n%2]
    n = n // 2
    while n > 0:
        tab.append(n%2)
        n = n // 2
    tab.reverse()
    return tab
        