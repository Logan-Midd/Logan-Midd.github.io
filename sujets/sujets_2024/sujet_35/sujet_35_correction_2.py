def inverse_chaine(chaine):
    '''Retourne la chaine inversÃ©e'''
    resultat = "" 
    for caractere in chaine:
        resultat = caractere + resultat 
    return resultat

def est_palindrome(chaine):
    '''Renvoie un boolÃ©en indiquant si la chaine ch
    est un palindrome'''
    inverse = inverse_chaine(chaine)
    return inverse == chaine 

def est_nbre_palindrome(nbre):
    '''Renvoie un boolÃ©en indiquant si le nombre nbre 
    est un palindrome'''
    chaine = str(nbre) 
    return est_palindrome(chaine)



