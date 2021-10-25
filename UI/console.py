from Domain.vanzare import toString
from Logic.CRUD import adaugareVanzare, stergereVanzare, modificareVanzare
from Logic.cerinte import aplicareDiscount


def printMenu():
    print("1. Adaugare vanzare")
    print("2. Stergere vanzare")
    print("3. Modificare vanzare")
    print("4. Aplicare discount")
    print("a. Afisare vanzari")
    print("x. Iesire")


def uiAdaugaVanzare(lista):
    id = input("Dati id-ul: ")
    titlu_carte = input("Dati titlul cartii: ")
    gen_carte = input("Dati genul cartii: ")
    pret = input("Dati pretul cartii: ")
    tip_reducere_client = input("Dati tipul de reducere al clientului: ")
    return adaugareVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client, lista)


def uiStergeVanzare(lista):
    id = input("Dati id-ul vanzarii de sters: ")
    return stergereVanzare(id, lista)


def uiModificaVanzare(lista):
    id = input("Dati id-ul vanzarii de modificat: ")
    titlu_carte = input("Dati un nou titlu cartii: ")
    gen_carte = input("Dati un nou gen cartii: ")
    pret = float(input("Dati un nou pret cartii: "))
    tip_reducere_client = input("Dati un nou tip de reducere al clientului: ")
    return modificareVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client, lista)


def showAll(lista):
    for vanzare in lista:
        print(toString(vanzare))


def uiAplicareDiscount(lista):
    return aplicareDiscount(lista)


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaVanzare(lista)
        elif optiune == "2":
            lista = uiStergeVanzare(lista)
        elif optiune == "3":
            lista = uiModificaVanzare(lista)
        elif optiune == "4":
            lista = uiAplicareDiscount(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print ("Optiunea este gresita!")



