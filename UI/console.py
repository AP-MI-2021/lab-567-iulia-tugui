from Domain.vanzare import toString
from Logic.CRUD import adaugareVanzare, stergereVanzare, modificareVanzare
from Logic.cerinte import aplicareDiscount, modificareaGenuluiPentruTitlu, pretMinimPentruFiecareGen, \
    ordonareCrescatorDupaPret, afisareNumarTitluriDistincte, Undo, Redo



def printMenu():
    print("1. Adaugare vanzare")
    print("2. Stergere vanzare")
    print("3. Modificare vanzare")
    print("4. Aplicare discount")
    print("5. Modificarea genului pentru un titlu dat")
    print("6. Determinarea pretului minim pentru fiecare gen")
    print("7. Ordonarea crescatoare a vanzarilor in functie de pret")
    print("8. Afișarea numărului de titluri distincte pentru fiecare gen")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare vanzari")
    print("x. Iesire")


def uiAdaugaVanzare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul: ")
        titlu_carte = input("Dati titlul cartii: ")
        gen_carte = input("Dati genul cartii: ")
        pret = input("Dati pretul cartii: ")
        tip_reducere_client = input("Dati tipul de reducere al clientului: ")
        undoList.append(lista)
        redoList.clear()
        return adaugareVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeVanzare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul vanzarii de sters: ")
        undoList.append(lista)
        redoList.clear()
        return stergereVanzare(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificaVanzare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul vanzarii de modificat: ")
        titlu_carte = input("Dati un nou titlu cartii: ")
        gen_carte = input("Dati un nou gen cartii: ")
        pret = float(input("Dati un nou pret cartii: "))
        tip_reducere_client = input("Dati un nou tip de reducere al clientului: ")
        undoList.append(lista)
        redoList.clear()
        return modificareVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def showAll(lista):
    for vanzare in lista:
        print(toString(vanzare))


def uiAplicareDiscount(lista, undoList, redoList):
    undoList.append(lista)
    redoList.clear()
    return aplicareDiscount(lista)

def uiModificareGen(lista, undoList, redoList):
    try:
        titlu = str(input("Dati titlul cartii al carei gen se modifica: "))
        gen = str(input("Dati noul gen: "))
        undoList.append(lista)
        redoList.clear()
        return modificareaGenuluiPentruTitlu(titlu, gen, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiPretMinimPentruFiecareGen(lista):
    listaPreturi = pretMinimPentruFiecareGen(lista)
    for pret in listaPreturi:
        print(pret)

def uiOrdonareCrescatorDupaPret(lista, undoList, redoList):
    undoList.append(lista)
    redoList.clear()
    showAll(ordonareCrescatorDupaPret(lista))

def uiAfisareNumarTitluriDistincte(lista):
    listaNumarTitluri = afisareNumarTitluriDistincte(lista)
    for numar in listaNumarTitluri:
        print(numar)



def runMenu(lista):
    undoList = []
    redoList = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaVanzare(lista, undoList, redoList)
        elif optiune == "2":
            lista = uiStergeVanzare(lista, undoList, redoList)
        elif optiune == "3":
            lista = uiModificaVanzare(lista, undoList, redoList)
        elif optiune == "4":
            lista = uiAplicareDiscount(lista, undoList, redoList)
        elif optiune == "5":
            lista = uiModificareGen(lista, undoList, redoList)
        elif optiune == "6":
            uiPretMinimPentruFiecareGen(lista)
        elif optiune == "7":
            uiOrdonareCrescatorDupaPret(lista, undoList, redoList)
        elif optiune == "8":
            uiAfisareNumarTitluriDistincte(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "u":
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "x":
            break
        else:
            print ("Optiunea este gresita!")



