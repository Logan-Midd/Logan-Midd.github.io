romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def traduire_romain(nombre) :
    if len(nombre) == 1:
        return romains[nombre[0]]

    elif romains[nombre[0]] >= romains[nombre[1]] :
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return  traduire_romain(nombre[1:]) - romains[nombre[0]]