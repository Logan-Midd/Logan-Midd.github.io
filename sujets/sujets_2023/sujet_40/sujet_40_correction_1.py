def nombre_de_mots(phrase):
    nb = 0
    id_der = len(phrase)-1
    for c in phrase:
        if c == " ":
            nb = nb + 1
    if phrase[id_der] == "?" or phrase[id_der] == "!":
        return nb
    else :
        return nb+1