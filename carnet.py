class Carnet(object):
    liste = []

    def ajout(self,contact):
        Carnet.liste.append(contact)

    def supp(self,num):
        Carnet.liste.pop(num)

    def __iter__(self):
        for i in Carnet.liste:
            yield i.affiche()

    def rechercher_cp(self,cp):
        for contact in Carnet.liste:
            if contact.code_postal==cp:
               yield contact


    def rechercher_nom(self,nom):
        pass