def selection_enclos(table_animaux, num_enclos):
    tab = []
    for d in table_animaux:
        if d['enclos'] == num_enclos:
            tab.append(d)
    return tab
    





