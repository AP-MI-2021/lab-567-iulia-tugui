from Domain.vanzare import getPret
from Logic.CRUD import getById, adaugareVanzare
from Logic.cerinte import aplicareDiscount


def testAplicareDiscount():
    lista = []
    lista = adaugareVanzare("1", "Harry Potter", "fantastic", 40, "silver", lista)
    lista = adaugareVanzare("2", "Eseu despre orbire", "fictiune", 40, "gold", lista)
    lista = adaugareVanzare("3", "Scufita Rosie", "povesti", 30, "none", lista)

    lista = aplicareDiscount(lista)

    assert getPret(getById("1", lista)) == 38
    assert getPret(getById("2", lista)) == 36
    assert getPret(getById("3", lista)) == 30