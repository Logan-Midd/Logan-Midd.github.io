t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

def mini(releve, date):
    m = releve[0]
    indice = 0
    for i in range(1, len(releve)):
        if releve[i]<m:
            m = releve[i]
            indice = i
    return m, date[indice]
    

