class Noeud:
    def __init__(self, valeur):
        '''MÃ©thode constructeur pour la classe Noeud. ParamÃ¨tre d'entrÃ©e : valeur (int)'''
        self.valeur = valeur
        self.gauche = None
        self.droit = None
    def getValeur(self):
        '''MÃ©thode accesseur pour obtenir la valeur du noeud Aucun paramÃ¨tre en entrÃ©e'''
        return self.valeur
    def droitExiste(self):
        '''MÃ©thode renvoyant True si le sous-arbre droit est non vide Aucun paramÃ¨tre en entrÃ©e'''
        return (self.droit is not None)
    def gaucheExiste(self):
        '''MÃ©thode renvoyant True si le sous-arbre gauche est non vide Aucun paramÃ¨tre en entrÃ©e'''
        return (self.gauche is not None)
    def inserer(self, cle):
        '''MÃ©thode d'insertion de clÃ© dans un arbre binaire de recherche ParamÃ¨tre d'entrÃ©e : cle (int)'''
        if cle < ... :
            # on insÃ¨re Ã  gauche
            if self.gaucheExiste():
                # on descend Ã  gauche et on recommence le test initial
                ...
            else:
                # on crÃ©e un fils gauche
                self.gauche = ...
        elif cle > ...:
            # on insÃ¨re Ã  droite
            if ...:
                # on descend Ã  droite et on recommence le test initial
                ...
            else:
                # on crÃ©e un fils droit
                ...  = Noeud(cle)
