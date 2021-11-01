from Teste.testCRUD import testAdaugareVanzare, testStergereVanzare, testModificareVanzare, testGetById
from Teste.testCerinte import testAplicareDiscount, testModificareaGenuluiPentruTitlu, testListaGenuri, \
    testPretMinimPentruFiecareGen
from Teste.testDomain import testVanzare


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

