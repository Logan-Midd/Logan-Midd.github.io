from random import randint

def lancer(n):
    t = []
    for _ in range(n):
        t.append(randint(1,6))
    return t

    
def paire_6(tab) :
    n = 0
    for v in tab:
        if v == 6:
            n = n + 1
    return n >= 2