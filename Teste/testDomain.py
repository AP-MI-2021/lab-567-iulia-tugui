from Domain.vanzare import creeazaVanzare, getId, getTitluCarte, getGenCarte, getPret, getTipReducereClient


def testVanzare():
    vanzare = creeazaVanzare("1", "Harry Potter", "fantastic", 40, "silver")
    assert getId(vanzare) == "1"
    assert getTitluCarte(vanzare) == "Harry Potter"
    assert getGenCarte(vanzare) == "fantastic"
    assert getPret(vanzare) == 40
    assert getTipReducereClient(vanzare) == "silver"