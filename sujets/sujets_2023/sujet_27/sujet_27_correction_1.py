def recherche_min(tab):
    indice_mini = 0
    mini = tab[0]
    for i in range(1, len(tab)):
        if tab[i] < mini:
            indice_mini = i
            mini = tab[i]
    return indice_mini