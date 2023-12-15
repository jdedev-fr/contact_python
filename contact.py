class Contact(object):
    
    def __init__(self,nom="",prenom="",code_postal=""):
        self.nom = nom
        self.prenom=prenom
        self.code_postal=code_postal
        
    
    def __str__(self):
        return f"{self.nom.upper()} {self.prenom.capitalize()} {self.code_postal}"
    
    def __repr__(self):
        return f"{self.nom.upper()}|{self.prenom.capitalize()}|{self.code_postal}"
    
    def __eq__(self,other):
        if self.nom.upper()==other.nom.upper() and self.prenom.capitalize()==other.prenom.capitalize() and self.code_postal==other.code_postal:
            return True
        else:
            return False
        
    def __hash__(self) -> int:
        return int(self.code_postal)
        

    