def insere(a, tab):
    l = list(tab)
    l.append(a)
    i = len(l) - 2
    while i >= 0 and a < tab[i] : 
      l[i+1] = l[i]
      l[i] = a
      i = i - 1
    return l