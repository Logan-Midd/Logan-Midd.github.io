def recherche(caractere, chaine):
    n = 0
    for c in chaine:
        if c == caractere:
            n = n + 1
    return n

