def rangement_valeurs(notes_eval):
    tab = [0]*11
    for n in notes_eval:
        tab[n] = tab[n] + 1
    return tab

def notes_triees(effectifs_notes):
    tab = []
    for i in range(len(effectifs_notes)):
        for _ in range(effectifs_notes[i]):
            tab.append(i)
    return tab


