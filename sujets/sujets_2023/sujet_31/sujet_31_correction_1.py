def nb_repetitions(elt, tab):
    c = 0
    for v in tab:
        if v == elt:
            c = c + 1
    return c
