def parcours(adj, x, acc):
    '''RÃ©alise un parcours en profondeur rÃ©cursif
    du graphe donnÃ© par les listes d'adjacence adj 
    depuis le sommet x en accumulant les sommets
    rencontrÃ©s dans acc'''
    if x not in acc: 
        acc.append(x)
        for y in adj[x]: 
            parcours(adj, y, acc) 

def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donnÃ© par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, x, acc) 
    return acc


