def renverse(pile):
    '''renvoie une pile contenant les mÃªmes Ã©lÃ©ments que pile,
    mais dans l'ordre inverse.
    Cette fonction dÃ©truit pile.'''
    pile_inverse = [] 
    while pile != []:
        pile_inverse.append(pile.pop()) 
    return pile_inverse


def positifs(pile):
    '''renvoie une pile contenant les Ã©lÃ©ments positifs de pile,
    dans le mÃªme ordre. Cette fonction dÃ©truit pile.'''
    pile_positifs = []
    while pile != []:
        v = pile.pop() 
        if v >= 0:
            pile_positifs.append(v)
    return renverse(pile_positifs) 


