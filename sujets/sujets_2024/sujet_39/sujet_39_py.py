class AdresseIP:
    def __init__(self, adresse):
        self.adresse =... 

    def liste_octets(self):
        """renvoie une liste de nombres entiers,
        la liste des octets de l'adresse IP"""
        # Note : split dÃ©coupe la chaine de caractÃ¨res 
        # en fonction du sÃ©parateur
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
        rÃ©servÃ©e, False sinon"""
        reservees = [ ... ] 
        return ... 

    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse
        IP qui suit l'adresse self si elle existe et None sinon"""
        octets = ... 
        if ... == 254: 
            return None
        octet_nouveau = ... + ... 
        return AdresseIP('192.168.0.' + ...) 

