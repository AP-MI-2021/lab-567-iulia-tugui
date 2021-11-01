from Domain.vanzare import toString
from Logic.CRUD import adaugareVanzare, stergereVanzare, modificareVanzare
from Logic.cerinte import aplicareDiscount, modificareaGenuluiPentruTitlu, pretMinimPentruFiecareGen


def printMenu():
    print("1. Adaugare vanzare")
    print("2. Stergere vanzare")
    print("3. Modificare vanzare")
    print("4. Aplicare discount")
    print("5. Modificarea genului pentru un titlu dat")
    print("6. Determinarea pretului minim pentru fiecare gen")
    print("a. Afisare vanzari")
    print("x. Iesire")


def uiAdaugaVanzare(lista):
    try:
        id = input("Dati id-ul: ")
        titlu_carte = input("Dati titlul cartii: ")
        gen_carte = input("Dati genul cartii: ")
        pret = input("Dati pretul cartii: ")
        tip_reducere_client = input("Dati tipul de reducere al clientului: ")
        return adaugareVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeVanzare(lista):
    try:
        id = input("Dati id-ul vanzarii de sters: ")
        return stergereVanzare(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificaVanzare(lista):
    try:
        id = input("Dati id-ul vanzarii de modificat: ")
        titlu_carte = input("Dati un nou titlu cartii: ")
        gen_carte = input("Dati un nou gen cartii: ")
        pret = float(input("Dati un nou pret cartii: "))
        tip_reducere_client = input("Dati un nou tip de reducere al clientului: ")
        return modificareVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def showAll(lista):
    for vanzare in lista:
        print(toString(vanzare))


def uiAplicareDiscount(lista):
    return aplicareDiscount(lista)

def uiModificareGen(lista):
    try:
        titlu = str(input("Dati titlul cartii al carei gen se modifica: "))
        gen = str(input("Dati noul gen: "))
        return modificareaGenuluiPentruTitlu(titlu, gen, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiPretMinimPentruFiecareGen(lista):
    listaPreturi = pretMinimPentruFiecareGen(lista)
    for pret in listaPreturi:
        print(pret)



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
        elif optiune == "5":
            lista = uiModificareGen(lista)
        elif optiune == "6":
            uiPretMinimPentruFiecareGen(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print ("Optiunea este gresita!")



