def min_et_max(tab):
    mini = tab[0]
    maxi = tab[0]
    for v in tab:
        if v > maxi:
            maxi = v
        if v < mini:
            mini = v
    return {'min':mini, 'max': maxi}
