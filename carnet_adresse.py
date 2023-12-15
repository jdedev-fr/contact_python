from contact import Contact
from carnet import Carnet

mon_carnet = Carnet()

mon_carnet.ajout(Contact("demettre","julien","56190"))
mon_carnet.ajout(Contact("aissasnou","abdeljalil","44000"))
mon_carnet.ajout(Contact("altujjar","razan","44000"))
mon_carnet.ajout(Contact("alves","anthony","75000"))

def affiche_contact(liste=[]):
    for index,contact in enumerate(liste):
        print(index+1,contact.affiche())
    print('-----------------------')

def ajoute_contact():
    nom = input('Entrez un nom : ')
    prenom = input('Entrez un prenom : ')
    code_postal = input('Entrez un code postal : ')
    mon_carnet.ajout(Contact(nom,prenom,code_postal))

def supp_contact():
    num = input('Entrez le numéro de contact à supprimer : ')
    if num.isdigit():
        mon_carnet.supp(int(num)-1)

def recherche_cp_contact():
    cp = input('Entrez un code postal : ')
    for contact in mon_carnet.rechercher_cp(cp):
        print(contact.affiche())
    

for i in mon_carnet:
    print(i)

while True:
    print("1 pour afficher les contacts")
    print("2 pour ajouter un contact")
    print("3 pour supprimer un contacts")
    print("4 pour quitter")
    print("5 pour recherche par cp")
    reponse = input("Entrez votre choix : ")
    if reponse=="1":
        affiche_contact(mon_carnet.liste)
    elif reponse=="2":
        ajoute_contact()
    elif reponse=="3":
        supp_contact()
    elif reponse=="4":
        break
    elif reponse=="5":
        recherche_cp_contact()
    else:
        print("Je n'ai pas compris")
