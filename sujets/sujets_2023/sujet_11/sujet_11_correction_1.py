def convertir(tab):
    n = len(tab)
    s = 0
    for i in range(n):
        s = s + tab[i]*2**(n-i-1)
    return s
        
