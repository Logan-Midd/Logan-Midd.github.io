def ou_exclusif(t1, t2):
    n = len(t1)
    t = [0]*n
    for i in range(n):
        if t1[i] == t2[i]:
            t[i] = 0
        else :
            t[i] = 1
    return t
    