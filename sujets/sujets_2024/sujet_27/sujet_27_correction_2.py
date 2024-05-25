def colore_comp1(M, i, j, val):
    if M[i][j] != 1:
        return

    M[i][j] = val

    if i-1 >= 0: # propage Ã  gauche
        colore_comp1(M, i-1, j, val)
    if i+1 < len(M): # propage Ã  droite 
        colore_comp1(M, i+1, j, val) 
    if j-1 >= 0 : # propage en haut 
        colore_comp1(M, i, j-1, val) 
    if j+1 < len(M[0]): # propage en bas 
        colore_comp1(M, i, j+1, val) 
