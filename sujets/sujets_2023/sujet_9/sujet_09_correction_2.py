def chercher(tab, n, i, j):
    if i < 0 or j > len(tab):
        return None
    elif i > j:
        return None
    m = (i + j) // 2
    if tab[m] < n:
        return chercher(tab, n, m+1, j)
    elif tab[m] > n:
        return chercher(tab, n, i, m-1)
    else:
        return m