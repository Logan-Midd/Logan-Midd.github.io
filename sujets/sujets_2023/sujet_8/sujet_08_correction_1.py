def max_dico(dico):
    maxi_v = 0
    maxi_n = ""
    for nom, val in dico.items():
        if val > maxi_v:
            maxi_v = val
            maxi_n = nom
    return maxi_n, maxi_v

