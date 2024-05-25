def liste_puissances(a, n):
    tab = [a]
    for _ in range(2, n+1):
        r = tab[-1]*a
        tab.append(r)
    return tab

def liste_puissances_borne(a, borne):
    if borne <= a:
        return []
    tab = [a]
    c = True
    while c:
        r = tab[-1]*a
        if r < borne:
            tab.append(r)
        else :
            c = False
    return tab
            
    
  