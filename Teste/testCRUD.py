from Domain.vanzare import getId, getTitluCarte, getGenCarte, getPret, getTipReducereClient
from Logic.CRUD import adaugareVanzare, getById, stergereVanzare, modificareVanzare


def testAdaugareVanzare():
    lista = []
    lista = adaugareVanzare("1", "Harry Potter", "fantastic", 40, "silver", lista)

    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getTitluCarte(getById("1", lista)) == "Harry Potter"
    assert getGenCarte(getById("1", lista)) == "fantastic"
    assert getPret(getById("1", lista)) == 40
    assert getTipReducereClient(getById("1", lista)) == "silver"

def testStergereVanzare():
    lista = []
    lista = adaugareVanzare("1", "Harry Potter", "fantastic", 40, "silver", lista)
    lista = adaugareVanzare("2", "Eseu despre orbire", "fictiune", 40, "gold", lista)
    lista = stergereVanzare("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

    try:
        lista = stergereVanzare("3", lista)
        assert False
    except ValueError:
        assert len(lista) == 1
        assert getById("2", lista) is not None
    except Exception:
        assert False

def testModificareVanzare():
    lista = []
    lista = adaugareVanzare("1", "Harry Potter", "fantastic", 40, "silver", lista)
    lista = adaugareVanzare("2", "Eseu despre orbire", "fictiune", 40, "gold", lista)

    lista = modificareVanzare("1", "Ion", "realist", 20, "none", lista)

    vanzareModificata = getById("1", lista)
    assert getId(vanzareModificata) == "1"
    assert getTitluCarte(vanzareModificata) == "Ion"
    assert getGenCarte(vanzareModificata) == "realist"
    assert getPret(vanzareModificata) == 20
    assert getTipReducereClient(vanzareModificata) == "none"

    vanzareNemodificata = getById("2", lista)
    assert getId(vanzareNemodificata) == "2"
    assert getTitluCarte(vanzareNemodificata) == "Eseu despre orbire"
    assert getGenCarte(vanzareNemodificata) == "fictiune"
    assert getPret(vanzareNemodificata) == 40
    assert getTipReducereClient(vanzareNemodificata) == "gold"

    lista = []
    lista = adaugareVanzare("1", "Harry Potter", "fantastic", 40, "silver", lista)

    try:
        lista = modificareVanzare("3", "Eseu despre orbire", "fictiune", 40, "gold", lista)
    except ValueError:
        vanzareNemodificata = getById("1", lista)
        assert getId(vanzareNemodificata) == "1"
        assert getTitluCarte(vanzareNemodificata) == "Harry Potter"
        assert getGenCarte(vanzareNemodificata) == "fantastic"
        assert getPret(vanzareNemodificata) == 40
        assert getTipReducereClient(vanzareNemodificata) == "silver"
    except Exception:
        assert False

def testGetById():
    lista = []
    lista = adaugareVanzare("1", "Harry Potter", "fantastic", 40, "silver", lista)
    lista = adaugareVanzare("2", "Eseu despre orbire", "fictiune", 40, "gold", lista)
    assert getById("1", lista) == lista[0]
    assert getById("2", lista) == lista[1]
    assert getById("3", lista) is None