urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin]=1
    return resultat

def vainqueur(election):
    vainqueur = '' #cette variable ne sert Ã  rien
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat #cette ligne ne sert Ã  rien !
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale
