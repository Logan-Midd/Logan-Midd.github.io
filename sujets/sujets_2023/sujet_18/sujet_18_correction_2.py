def est_un_ordre(tab):
    for i in range(1, len(tab)+1):
        if i not in tab :
            return False
    return True


def nombre_points_rupture(ordre):
    assert est_un_ordre(ordre) 
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: 
        nb = nb + 1
    i = 0
    while i < len(ordre)-1:
        if (ordre[i+1] - ordre[i]) not in [-1, 1]:
            nb = nb + 1
        i = i + 1
    if ordre[n-1] != n:
        nb = nb + 1
    return nb
