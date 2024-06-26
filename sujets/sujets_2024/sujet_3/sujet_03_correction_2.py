class Pile:
    """Classe dÃ©finissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie un boolÃ©en indiquant si la pile est vide."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'Ã©lÃ©ment v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'Ã©lÃ©ment placÃ© au sommet de la pile,
        si la pile nâest pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()

def bon_parenthesage(ch):
    """Renvoie un boolÃ©en indiquant si la chaÃ®ne ch 
    est bien parenthÃ©sÃ©e"""
    p = Pile()
    for c in ch:
        if c == '(': 
            p.empiler(c)
        elif c == ')': 
            if p.est_vide():
                False
            else:
                p.depiler()
    return p.est_vide() 


