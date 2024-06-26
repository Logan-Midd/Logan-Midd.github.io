class Expr:
    """Classe implÃ©mentant un arbre d'expression."""

    def __init__(self, g, v, d):
        """un objet Expr possÃ¨de 3 attributs :
        - gauche : la sous-expression gauche ;
        - valeur : la valeur de l'Ã©tiquette, opÃ©rande ou nombre ;
        - droite : la sous-expression droite."""
        self.gauche = g
        self.valeur = v
        self.droite = d

    def est_une_feuille(self):
        """renvoie True si et seulement 
        si le noeud est une feuille"""
        return self.gauche is None and self.droite is None

    def infixe(self):
        """renvoie la reprÃ©sentation infixe de l'expression en
        chaine de caractÃ¨res"""
        s = ... 
        if self.gauche is not None:
            s = '(' + s + ... .infixe() 
        s = s + ... 
        if ... is not None: 
            s = s + ... + ... 
        return s


