from Domain.vanzare import getPret, getTitluCarte, getGenCarte
from Logic.CRUD import getById, adaugareVanzare
from Logic.cerinte import aplicareDiscount, modificareaGenuluiPentruTitlu, listaGenuri, pretMinimPentruFiecareGen


def testAplicareDiscount():
    lista = []
    lista = adaugareVanzare("1", "Harry Potter", "fantastic", 40, "silver", lista)
    lista = adaugareVanzare("2", "Eseu despre orbire", "fictiune", 40, "gold", lista)
    lista = adaugareVanzare("3", "Scufita Rosie", "povesti", 30, "none", lista)

    lista = aplicareDiscount(lista)

    assert getPret(getById("1", lista)) == 38
    assert getPret(getById("2", lista)) == 36
    assert getPret(getById("3", lista)) == 30

def testModificareaGenuluiPentruTitlu():
    lista = []
    lista = adaugareVanzare("1", "Harry Potter", "fantastic", 40, "silver", lista)
    lista = adaugareVanzare("2", "Eseu despre orbire", "fictiune", 40, "gold", lista)
    lista = adaugareVanzare("3", "Scufita Rosie", "povesti", 30, "none", lista)
    lista = adaugareVanzare("4", "Scufita Rosie", "SF", 200, "silver", lista)

    lista = modificareaGenuluiPentruTitlu("Scufita Rosie", "povesti", lista)

    assert getGenCarte(getById("1", lista)) == "fantastic"
    assert getGenCarte(getById("3", lista)) == "povesti"
    assert getGenCarte(getById("4", lista)) == "povesti"

def testListaGenuri():
    lista = []
    listaGen = []
    lista = adaugareVanzare("1", "Harry Potter", "fictiune", 40, "silver", lista)
    lista = adaugareVanzare("2", "Eseu despre orbire", "fictiune", 40, "gold", lista)
    lista = adaugareVanzare("3", "Scufita Rosie", "povesti", 30, "none", lista)
    lista = adaugareVanzare("4", "Scufita Rosie", "SF", 200, "silver", lista)

    listaGen = listaGenuri(lista)

    assert len(listaGen) == 3
    assert listaGen[0] == "fictiune"
    assert listaGen[1] == "povesti"
    assert listaGen[2] == "SF"

def testPretMinimPentruFiecareGen():
    lista = []
    listaPreturi = []
    lista = adaugareVanzare("1", "Harry Potter", "fictiune", 40, "silver", lista)
    lista = adaugareVanzare("2", "Eseu despre orbire", "povesti", 43, "gold", lista)
    lista = adaugareVanzare("3", "Scufita Rosie", "povesti", 30, "none", lista)
    lista = adaugareVanzare("4", "Ion", "SF", 200, "silver", lista)
    lista = adaugareVanzare("5", "Invitatie la vals", "fictiune", 54, "none", lista)
    lista = adaugareVanzare("6", "Marile sperante", "dragoste", 40, "gold", lista)
    lista = adaugareVanzare("7", "Blandetea noptii", "fictiune", 28, "silver", lista)

    listaPreturi = pretMinimPentruFiecareGen(lista)

    assert listaPreturi[0] == 28
    assert listaPreturi[1] == 30
    assert listaPreturi[2] == 200
    assert listaPreturi[3] == 40
