class Contact(object):
    
    def __init__(self,nom="",prenom="",code_postal=""):
        self.nom = nom
        self.prenom=prenom
        self.code_postal=code_postal
        
    
    def __str__(self):
        return f"{self.nom.upper()} {self.prenom.capitalize()} {self.code_postal}"
    
    def __repr__(self):
        return f"{self.nom.upper()}|{self.prenom.capitalize()}|{self.code_postal}"

    