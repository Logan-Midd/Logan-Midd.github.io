def moyenne(liste_notes):
    s_n = 0
    s_c = 0
    for v in liste_notes:
        s_n = s_n + v[0]*v[1]
        s_c = s_c + v[1]
    return s_n / s_c

