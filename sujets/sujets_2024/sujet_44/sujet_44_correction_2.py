class Noeud:
    """Classe reprÃ©sentant un noeud d'un arbre binaire"""
    def __init__(self, etiquette, gauche, droit):
        """CrÃ©e un noeud de valeur etiquette avec 
        gauche et droit comme fils."""
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit

def parcours(arbre, liste):
    """parcours rÃ©cursivement l'arbre en ajoutant les Ã©tiquettes
    de ses noeuds Ã  la liste passÃ©e en argument en ordre infixe."""
    if arbre != None:
        parcours(arbre.gauche, liste)
        liste.append(arbre.etiquette)
        parcours(arbre.droit, liste)
    return liste

def insere(arbre, cle):
    """insere la cle dans l'arbre binaire de recherche
    reprÃ©sentÃ© par arbre.
    Retourne l'arbre modifiÃ©."""
    if arbre == None:
        return Noeud(cle, None, None) # creation d'une feuille
    else:
        if cle < arbre.etiquette: 
            arbre.gauche = insere(arbre.gauche, cle)
        else:
            arbre.droit = insere(arbre.droit, cle) 
        return arbre


a_5 = Noeud(5,None, None)
a_2 = insere(a_5,2)
a_7 = insere(a_2,7)
a_3 = insere(a_7,3)
