def moyenne(tab):
    assert len(tab) != 0, "aucune note"
    s = 0
    for v in tab :
        s = s + v
    return s/len(tab)

