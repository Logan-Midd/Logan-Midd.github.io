def recherche_indices_classement(elt, tab):
    l_eg = []
    l_sup = []
    l_inf = []
    for i in range(len(tab)):
        if tab[i]>elt:
            l_sup.append(i)
        elif tab[i]<elt:
            l_inf.append(i)
        else:
            l_eg.append(i)
    return l_inf, l_eg, l_sup