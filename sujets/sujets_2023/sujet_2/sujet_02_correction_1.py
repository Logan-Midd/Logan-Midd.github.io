def indices_maxi(tab):
    t_maxi = []
    maxi = tab[0]
    n = len(tab)
    for i in range(1,n):
        if tab[i]>maxi:
            maxi = tab[i]
    for i in range(n):
        if tab[i] == maxi:
            t_maxi.append(i)
    return maxi, t_maxi