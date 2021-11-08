from Teste.testCRUD import testAdaugareVanzare, testStergereVanzare, testModificareVanzare, testGetById
from Teste.testCerinte import testAplicareDiscount, testModificareaGenuluiPentruTitlu, testListaGenuri, \
    testPretMinimPentruFiecareGen, testOrdonareCrescatorDupaPret, testListaTitluriPentruFiecareGen, \
    testAfisareNumarTitluriDistincte
from Teste.testDomain import testVanzare
from Teste.testUndoRedo import testUndoRedo


def runAllTests():
    testVanzare()
    testAdaugareVanzare()
    testStergereVanzare()
    testModificareVanzare()
    testAplicareDiscount()
    testGetById()
    testModificareaGenuluiPentruTitlu()
    testListaGenuri()
    testPretMinimPentruFiecareGen()
    testOrdonareCrescatorDupaPret()
    testListaTitluriPentruFiecareGen()
    testAfisareNumarTitluriDistincte()
    testUndoRedo()

